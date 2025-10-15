#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "typer",
#     "rich",
#     "platformdirs",
#     "readchar",
#     "httpx",
# ]
# ///
"""
Specify TW CLI - Setup tool for Specify projects

Usage:
    uvx specify-tw-cli.py init <project-name>
    uvx specify-tw-cli.py init --here

Or install globally:
    uv tool install --from specify-tw-cli.py specify-tw-cli
    specify-tw init <project-name>
    specify-tw init --here
"""

import os
import subprocess
import sys
import zipfile
import tempfile
import shutil
import shlex
import json
from pathlib import Path
from typing import Optional, Tuple

import typer
import httpx
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.text import Text
from rich.live import Live
from rich.align import Align
from rich.table import Table
from rich.tree import Tree
from typer.core import TyperGroup

# For cross-platform keyboard input
import readchar
import ssl
import truststore

ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client = httpx.Client(verify=ssl_context)

def _github_token(cli_token: str | None = None) -> str | None:
    """Return sanitized GitHub token (cli arg takes precedence) or None."""
    return ((cli_token or os.getenv("GH_TOKEN") or os.getenv("GITHUB_TOKEN") or "").strip()) or None

def _github_auth_headers(cli_token: str | None = None) -> dict:
    """Return Authorization header dict only when a non-empty token exists."""
    token = _github_token(cli_token)
    return {"Authorization": f"Bearer {token}"} if token else {}

# Constants
AGENT_CONFIG = {
    "copilot": {
        "name": "GitHub Copilot",
        "folder": ".github/",
        "install_url": None,  # IDE-based, no CLI check needed
        "requires_cli": False,
    },
    "claude": {
        "name": "Claude Code",
        "folder": ".claude/",
        "install_url": "https://docs.anthropic.com/en/docs/claude-code/setup",
        "requires_cli": True,
    },
    "gemini": {
        "name": "Gemini CLI",
        "folder": ".gemini/",
        "install_url": "https://github.com/google-gemini/gemini-cli",
        "requires_cli": True,
    },
    "cursor-agent": {
        "name": "Cursor",
        "folder": ".cursor/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "qwen": {
        "name": "Qwen Code",
        "folder": ".qwen/",
        "install_url": "https://github.com/QwenLM/qwen-code",
        "requires_cli": True,
    },
    "opencode": {
        "name": "opencode",
        "folder": ".opencode/",
        "install_url": "https://opencode.ai",
        "requires_cli": True,
    },
    "codex": {
        "name": "Codex CLI",
        "folder": ".codex/",
        "install_url": "https://github.com/openai/codex",
        "requires_cli": True,
    },
    "windsurf": {
        "name": "Windsurf",
        "folder": ".windsurf/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "kilocode": {
        "name": "Kilo Code",
        "folder": ".kilocode/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "auggie": {
        "name": "Auggie CLI",
        "folder": ".augment/",
        "install_url": "https://docs.augmentcode.com/cli/setup-auggie/install-auggie-cli",
        "requires_cli": True,
    },
    "codebuddy": {
        "name": "CodeBuddy",
        "folder": ".codebuddy/",
        "install_url": "https://www.codebuddy.ai",
        "requires_cli": True,
    },
    "roo": {
        "name": "Roo Code",
        "folder": ".roo/",
        "install_url": None,  # IDE-based
        "requires_cli": False,
    },
    "q": {
        "name": "Amazon Q Developer CLI",
        "folder": ".amazonq/",
        "install_url": "https://aws.amazon.com/developer/learning/q-developer-cli/",
        "requires_cli": True,
    },
}

# 從 AGENT_CONFIG 生成輔助字典
AI_CHOICES = {key: config["name"] for key, config in AGENT_CONFIG.items()}
AGENT_FOLDER_MAP = {key: config["folder"] for key, config in AGENT_CONFIG.items()}

# Add script type choices
SCRIPT_TYPE_CHOICES = {"sh": "POSIX Shell (bash/zsh)", "ps": "PowerShell"}

# Claude CLI local installation path after migrate-installer
CLAUDE_LOCAL_PATH = Path.home() / ".claude" / "local" / "claude"

# ASCII Art Banner
BANNER = """
███████╗██████╗ ███████╗ ██████╗██╗███████╗██╗   ██╗
██╔════╝██╔══██╗██╔════╝██╔════╝██║██╔════╝╚██╗ ██╔╝
███████╗██████╔╝█████╗  ██║     ██║█████╗   ╚████╔╝ 
╚════██║██╔═══╝ ██╔══╝  ██║     ██║██╔══╝    ╚██╔╝  
███████║██║     ███████╗╚██████╗██║██║        ██║   
╚══════╝╚═╝     ╚══════╝ ╚═════╝╚═╝╚═╝        ╚═╝   
"""

TAGLINE = "GitHub Spec Kit TW - 規範驅動開發工具包"
class StepTracker:
    """Track and render hierarchical steps without emojis, similar to Claude Code tree output.
    Supports live auto-refresh via an attached refresh callback.
    """
    def __init__(self, title: str):
        self.title = title
        self.steps = []  # list of dicts: {key, label, status, detail}
        self.status_order = {"pending": 0, "running": 1, "done": 2, "error": 3, "skipped": 4}
        self._refresh_cb = None  # callable to trigger UI refresh

    def attach_refresh(self, cb):
        self._refresh_cb = cb

    def add(self, key: str, label: str):
        if key not in [s["key"] for s in self.steps]:
            self.steps.append({"key": key, "label": label, "status": "pending", "detail": ""})
            self._maybe_refresh()

    def start(self, key: str, detail: str = ""):
        self._update(key, status="running", detail=detail)

    def complete(self, key: str, detail: str = ""):
        self._update(key, status="done", detail=detail)

    def error(self, key: str, detail: str = ""):
        self._update(key, status="error", detail=detail)

    def skip(self, key: str, detail: str = ""):
        self._update(key, status="skipped", detail=detail)

    def _update(self, key: str, status: str, detail: str):
        for s in self.steps:
            if s["key"] == key:
                s["status"] = status
                if detail:
                    s["detail"] = detail
                self._maybe_refresh()
                return
        # If not present, add it
        self.steps.append({"key": key, "label": key, "status": status, "detail": detail})
        self._maybe_refresh()

    def _maybe_refresh(self):
        if self._refresh_cb:
            try:
                self._refresh_cb()
            except Exception:
                pass

    def render(self):
        tree = Tree(f"[cyan]{self.title}[/cyan]", guide_style="grey50")
        for step in self.steps:
            label = step["label"]
            detail_text = step["detail"].strip() if step["detail"] else ""

            # Circles (unchanged styling)
            status = step["status"]
            if status == "done":
                symbol = "[green]●[/green]"
            elif status == "pending":
                symbol = "[green dim]○[/green dim]"
            elif status == "running":
                symbol = "[cyan]○[/cyan]"
            elif status == "error":
                symbol = "[red]●[/red]"
            elif status == "skipped":
                symbol = "[yellow]○[/yellow]"
            else:
                symbol = " "

            if status == "pending":
                # Entire line light gray (pending)
                if detail_text:
                    line = f"{symbol} [dim]{label} ({detail_text})[/dim]"
                else:
                    line = f"{symbol} [dim]{label}[/dim]"
            else:
                # Label white, detail (if any) light gray in parentheses
                if detail_text:
                    line = f"{symbol} [white]{label}[/white] [dim]({detail_text})[/dim]"
                else:
                    line = f"{symbol} [white]{label}[/white]"

            tree.add(line)
        return tree



MINI_BANNER = """
╔═╗╔═╗╔═╗╔═╗╦╔═╗╦ ╦
╚═╗╠═╝║╣ ║  ║╠╣ ╚╦╝
╚═╝╩  ╚═╝╚═╝╩╚   ╩ 
"""

def get_key():
    """Get a single keypress in a cross-platform way using readchar."""
    key = readchar.readkey()
    
    # Arrow keys
    if key == readchar.key.UP or key == readchar.key.CTRL_P:
        return 'up'
    if key == readchar.key.DOWN or key == readchar.key.CTRL_N:
        return 'down'
    
    # Enter/Return
    if key == readchar.key.ENTER:
        return 'enter'
    
    # Escape
    if key == readchar.key.ESC:
        return 'escape'
        
    # Ctrl+C
    if key == readchar.key.CTRL_C:
        raise KeyboardInterrupt

    return key



def select_with_arrows(options: dict, prompt_text: str = "Select an option", default_key: str = None) -> str:
    """
    Interactive selection using arrow keys with Rich Live display.
    
    Args:
        options: Dict with keys as option keys and values as descriptions
        prompt_text: Text to show above the options
        default_key: Default option key to start with
        
    Returns:
        Selected option key
    """
    option_keys = list(options.keys())
    if default_key and default_key in option_keys:
        selected_index = option_keys.index(default_key)
    else:
        selected_index = 0
    
    selected_key = None

    def create_selection_panel():
        """Create the selection panel with current selection highlighted."""
        table = Table.grid(padding=(0, 2))
        table.add_column(style="cyan", justify="left", width=3)
        table.add_column(style="white", justify="left")
        
        for i, key in enumerate(option_keys):
            if i == selected_index:
                table.add_row("▶", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")
            else:
                table.add_row(" ", f"[cyan]{key}[/cyan] [dim]({options[key]})[/dim]")

        table.add_row("", "")
        table.add_row("", "[dim]使用 ↑/↓ 導航，Enter 選擇，Esc 取消[/dim]")
        
        return Panel(
            table,
            title=f"[bold]{prompt_text}[/bold]",
            border_style="cyan",
            padding=(1, 2)
        )
    
    console.print()

    def run_selection_loop():
        nonlocal selected_key, selected_index
        with Live(create_selection_panel(), console=console, transient=True, auto_refresh=False) as live:
            while True:
                try:
                    key = get_key()
                    if key == 'up':
                        selected_index = (selected_index - 1) % len(option_keys)
                    elif key == 'down':
                        selected_index = (selected_index + 1) % len(option_keys)
                    elif key == 'enter':
                        selected_key = option_keys[selected_index]
                        break
                    elif key == 'escape':
                        console.print("\n[yellow]選擇已取消[/yellow]")
                        raise typer.Exit(1)
                    
                    live.update(create_selection_panel(), refresh=True)

                except KeyboardInterrupt:
                    console.print("\n[yellow]選擇已取消[/yellow]")
                    raise typer.Exit(1)

    run_selection_loop()

    if selected_key is None:
        console.print("\n[red]選擇失敗。[/red]")
        raise typer.Exit(1)

    # Suppress explicit selection print; tracker / later logic will report consolidated status
    return selected_key



console = Console()


class BannerGroup(TyperGroup):
    """Custom group that shows banner before help."""
    
    def format_help(self, ctx, formatter):
        # Show banner before help
        show_banner()
        super().format_help(ctx, formatter)


app = typer.Typer(
    name="specify-tw",
    help="Specify 規範驅動開發專案設置工具",
    add_completion=False,
    invoke_without_command=True,
    cls=BannerGroup,
)


def show_banner():
    """Display the ASCII art banner."""
    # Create gradient effect with different colors
    banner_lines = BANNER.strip().split('\n')
    colors = ["bright_blue", "blue", "cyan", "bright_cyan", "white", "bright_white"]
    
    styled_banner = Text()
    for i, line in enumerate(banner_lines):
        color = colors[i % len(colors)]
        styled_banner.append(line + "\n", style=color)
    
    console.print(Align.center(styled_banner))
    console.print(Align.center(Text(TAGLINE, style="italic bright_yellow")))
    console.print()


@app.callback()
def callback(ctx: typer.Context):
    """Show banner when no subcommand is provided."""
    # Show banner only when no subcommand and no help flag
    # (help is handled by BannerGroup)
    if ctx.invoked_subcommand is None and "--help" not in sys.argv and "-h" not in sys.argv:
        show_banner()
        console.print(Align.center("[dim]執行 'specify-tw --help' 查看使用資訊[/dim]"))
        console.print()


def run_command(cmd: list[str], check_return: bool = True, capture: bool = False, shell: bool = False) -> Optional[str]:
    """Run a shell command and optionally capture output."""
    try:
        if capture:
            result = subprocess.run(cmd, check=check_return, capture_output=True, text=True, shell=shell)
            return result.stdout.strip()
        else:
            subprocess.run(cmd, check=check_return, shell=shell)
            return None
    except subprocess.CalledProcessError as e:
        if check_return:
            console.print(f"[red]執行命令錯誤：[/red] {' '.join(cmd)}")
            console.print(f"[red]退出碼：[/red] {e.returncode}")
            if hasattr(e, 'stderr') and e.stderr:
                console.print(f"[red]錯誤輸出：[/red] {e.stderr}")
            raise
        return None


def check_tool_for_tracker(tool: str, tracker: StepTracker) -> bool:
    """Check if a tool is installed and update tracker."""
    if shutil.which(tool):
        tracker.complete(tool, "可用")
        return True
    else:
        tracker.error(tool, "未找到")
        return False


def check_tool(tool: str, install_hint: str = None, tracker: StepTracker = None) -> bool:
    """Check if a tool is installed, optionally updating tracker.

    Args:
        tool: The tool name to check
        install_hint: Optional install URL (for backwards compatibility, not used with tracker)
        tracker: Optional StepTracker to update with results

    Returns:
        True if tool is found, False otherwise
    """

    # Special handling for Claude CLI after `claude migrate-installer`
    # See: https://github.com/github/spec-kit/issues/123
    # The migrate-installer command REMOVES the original executable from PATH
    # and creates an alias at ~/.claude/local/claude instead
    # This path should be prioritized over other claude executables in PATH
    if tool == "claude":
        if CLAUDE_LOCAL_PATH.exists() and CLAUDE_LOCAL_PATH.is_file():
            if tracker:
                tracker.complete(tool, "可用")
            return True

    if shutil.which(tool):
        if tracker:
            tracker.complete(tool, "可用")
        return True
    else:
        if tracker:
            tracker.error(tool, "未找到")
        return False


def is_git_repo(path: Path = None) -> bool:
    """Check if the specified path is inside a git repository."""
    if path is None:
        path = Path.cwd()
    
    if not path.is_dir():
        return False

    try:
        # Use git command to check if inside a work tree
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            cwd=path,
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def init_git_repo(project_path: Path, quiet: bool = False) -> bool:
    """Initialize a git repository in the specified path.
    quiet: if True suppress console output (tracker handles status)
    """
    try:
        original_cwd = Path.cwd()
        os.chdir(project_path)
        if not quiet:
            console.print("[cyan]正在初始化 git 儲存庫...[/cyan]")
        subprocess.run(["git", "init"], check=True, capture_output=True)
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        subprocess.run(["git", "commit", "-m", "Initial commit from Specify template"], check=True, capture_output=True)
        if not quiet:
            console.print("[green]✓[/green] Git 儲存庫已初始化")
        return True

    except subprocess.CalledProcessError as e:
        if not quiet:
            console.print(f"[red]初始化 git 儲存庫錯誤：[/red] {e}")
        return False
    finally:
        os.chdir(original_cwd)


def download_template_from_github(ai_assistant: str, download_dir: Path, *, script_type: str = "sh", verbose: bool = True, show_progress: bool = True, client: httpx.Client = None, debug: bool = False, github_token: str = None) -> Tuple[Path, dict]:
    repo_owner = "Minidoracat"
    repo_name = "spec-kit-tw"
    if client is None:
        client = httpx.Client(verify=ssl_context)
    
    if verbose:
        console.print("[cyan]正在取得最新版本資訊...[/cyan]")
    api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    
    try:
        response = client.get(
            api_url,
            timeout=30,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        )
        status = response.status_code
        if status != 200:
            msg = f"GitHub API returned {status} for {api_url}"
            if debug:
                msg += f"\nResponse headers: {response.headers}\nBody (truncated 500): {response.text[:500]}"
            raise RuntimeError(msg)
        try:
            release_data = response.json()
        except ValueError as je:
            raise RuntimeError(f"Failed to parse release JSON: {je}\nRaw (truncated 400): {response.text[:400]}")
    except Exception as e:
        console.print(f"[red]取得版本資訊錯誤[/red]")
        console.print(Panel(str(e), title="取得錯誤", border_style="red"))
        raise typer.Exit(1)
    
    # Find the template asset for the specified AI assistant
    assets = release_data.get("assets", [])
    pattern = f"spec-kit-template-{ai_assistant}-{script_type}"
    matching_assets = [
        asset for asset in assets
        if pattern in asset["name"] and asset["name"].endswith(".zip")
    ]

    asset = matching_assets[0] if matching_assets else None

    if asset is None:
        console.print(f"[red]未找到符合的發布資源[/red] for [bold]{ai_assistant}[/bold] (預期模式: [bold]{pattern}[/bold])")
        asset_names = [a.get('name', '?') for a in assets]
        console.print(Panel("\n".join(asset_names) or "(無資源)", title="可用資源", border_style="yellow"))
        raise typer.Exit(1)

    download_url = asset["browser_download_url"]
    filename = asset["name"]
    file_size = asset["size"]
    
    if verbose:
        console.print(f"[cyan]找到模板：[/cyan] {filename}")
        console.print(f"[cyan]大小：[/cyan] {file_size:,} 位元組")
        console.print(f"[cyan]版本：[/cyan] {release_data['tag_name']}")

    zip_path = download_dir / filename
    if verbose:
        console.print(f"[cyan]正在下載模板...[/cyan]")
    
    try:
        with client.stream(
            "GET",
            download_url,
            timeout=60,
            follow_redirects=True,
            headers=_github_auth_headers(github_token),
        ) as response:
            if response.status_code != 200:
                body_sample = response.text[:400]
                raise RuntimeError(f"Download failed with {response.status_code}\nHeaders: {response.headers}\nBody (truncated): {body_sample}")
            total_size = int(response.headers.get('content-length', 0))
            with open(zip_path, 'wb') as f:
                if total_size == 0:
                    for chunk in response.iter_bytes(chunk_size=8192):
                        f.write(chunk)
                else:
                    if show_progress:
                        with Progress(
                            SpinnerColumn(),
                            TextColumn("[progress.description]{task.description}"),
                            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
                            console=console,
                        ) as progress:
                            task = progress.add_task("下載中...", total=total_size)
                            downloaded = 0
                            for chunk in response.iter_bytes(chunk_size=8192):
                                f.write(chunk)
                                downloaded += len(chunk)
                                progress.update(task, completed=downloaded)
                    else:
                        for chunk in response.iter_bytes(chunk_size=8192):
                            f.write(chunk)
    except Exception as e:
        console.print(f"[red]下載模板錯誤[/red]")
        detail = str(e)
        if zip_path.exists():
            zip_path.unlink()
        console.print(Panel(detail, title="下載錯誤", border_style="red"))
        raise typer.Exit(1)
    if verbose:
        console.print(f"已下載：{filename}")
    metadata = {
        "filename": filename,
        "size": file_size,
        "release": release_data["tag_name"],
        "asset_url": download_url
    }
    return zip_path, metadata


def download_and_extract_template(project_path: Path, ai_assistant: str, script_type: str, is_current_dir: bool = False, *, verbose: bool = True, tracker: StepTracker | None = None, client: httpx.Client = None, debug: bool = False, github_token: str = None) -> Path:
    """Download the latest release and extract it to create a new project.
    Returns project_path. Uses tracker if provided (with keys: fetch, download, extract, cleanup)
    """
    current_dir = Path.cwd()
    
    # Step: fetch + download combined
    if tracker:
        tracker.start("fetch", "contacting GitHub API")
    try:
        zip_path, meta = download_template_from_github(
            ai_assistant,
            current_dir,
            script_type=script_type,
            verbose=verbose and tracker is None,
            show_progress=(tracker is None),
            client=client,
            debug=debug,
            github_token=github_token
        )
        if tracker:
            tracker.complete("fetch", f"release {meta['release']} ({meta['size']:,} bytes)")
            tracker.add("download", "下載模板")
            tracker.complete("download", meta['filename'])
    except Exception as e:
        if tracker:
            tracker.error("fetch", str(e))
        else:
            if verbose:
                console.print(f"[red]下載模板錯誤：[/red] {e}")
        raise
    
    if tracker:
        tracker.add("extract", "解壓模板")
        tracker.start("extract")
    elif verbose:
        console.print("正在解壓模板...")
    
    try:
        # Create project directory only if not using current directory
        if not is_current_dir:
            project_path.mkdir(parents=True)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # List all files in the ZIP for debugging
            zip_contents = zip_ref.namelist()
            if tracker:
                tracker.start("zip-list")
                tracker.complete("zip-list", f"{len(zip_contents)} 個項目")
            elif verbose:
                console.print(f"[cyan]ZIP 包含 {len(zip_contents)} 個項目[/cyan]")
            
            # For current directory, extract to a temp location first
            if is_current_dir:
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    zip_ref.extractall(temp_path)
                    
                    # Check what was extracted
                    extracted_items = list(temp_path.iterdir())
                    if tracker:
                        tracker.start("extracted-summary")
                        tracker.complete("extracted-summary", f"暫存 {len(extracted_items)} 個項目")
                    elif verbose:
                        console.print(f"[cyan]已解壓 {len(extracted_items)} 個項目到暫存位置[/cyan]")
                    
                    # Handle GitHub-style ZIP with a single root directory
                    source_dir = temp_path
                    if len(extracted_items) == 1 and extracted_items[0].is_dir():
                        source_dir = extracted_items[0]
                        if tracker:
                            tracker.add("flatten", "扁平化巢狀目錄")
                            tracker.complete("flatten")
                        elif verbose:
                            console.print(f"[cyan]發現巢狀目錄結構[/cyan]")
                    
                    # Copy contents to current directory
                    for item in source_dir.iterdir():
                        dest_path = project_path / item.name
                        if item.is_dir():
                            if dest_path.exists():
                                if verbose and not tracker:
                                    console.print(f"[yellow]正在合併目錄：[/yellow] {item.name}")
                                # Recursively copy directory contents
                                for sub_item in item.rglob('*'):
                                    if sub_item.is_file():
                                        rel_path = sub_item.relative_to(item)
                                        dest_file = dest_path / rel_path
                                        dest_file.parent.mkdir(parents=True, exist_ok=True)
                                        shutil.copy2(sub_item, dest_file)
                            else:
                                shutil.copytree(item, dest_path)
                        else:
                            if dest_path.exists() and verbose and not tracker:
                                console.print(f"[yellow]正在覆蓋檔案：[/yellow] {item.name}")
                            shutil.copy2(item, dest_path)
                    if verbose and not tracker:
                        console.print(f"[cyan]模板檔案已合併到目前目錄[/cyan]")
            else:
                # Extract directly to project directory (original behavior)
                zip_ref.extractall(project_path)
                
                # Check what was extracted
                extracted_items = list(project_path.iterdir())
                if tracker:
                    tracker.start("extracted-summary")
                    tracker.complete("extracted-summary", f"{len(extracted_items)} 個頂層項目")
                elif verbose:
                    console.print(f"[cyan]已解壓 {len(extracted_items)} 個項目到 {project_path}：[/cyan]")
                    for item in extracted_items:
                        console.print(f"  - {item.name} ({'目錄' if item.is_dir() else '檔案'})")
                
                # Handle GitHub-style ZIP with a single root directory
                if len(extracted_items) == 1 and extracted_items[0].is_dir():
                    # Move contents up one level
                    nested_dir = extracted_items[0]
                    temp_move_dir = project_path.parent / f"{project_path.name}_temp"
                    # Move the nested directory contents to temp location
                    shutil.move(str(nested_dir), str(temp_move_dir))
                    # Remove the now-empty project directory
                    project_path.rmdir()
                    # Rename temp directory to project directory
                    shutil.move(str(temp_move_dir), str(project_path))
                    if tracker:
                        tracker.add("flatten", "扁平化巢狀目錄")
                        tracker.complete("flatten")
                    elif verbose:
                        console.print(f"[cyan]已扁平化巢狀目錄結構[/cyan]")
                    
    except Exception as e:
        if tracker:
            tracker.error("extract", str(e))
        else:
            if verbose:
                console.print(f"[red]解壓模板錯誤：[/red] {e}")
                if debug:
                    console.print(Panel(str(e), title="解壓錯誤", border_style="red"))
        # Clean up project directory if created and not current directory
        if not is_current_dir and project_path.exists():
            shutil.rmtree(project_path)
        raise typer.Exit(1)
    else:
        if tracker:
            tracker.complete("extract")
    finally:
        if tracker:
            tracker.add("cleanup", "移除暫存檔案")
        # Clean up downloaded ZIP file
        if zip_path.exists():
            zip_path.unlink()
            if tracker:
                tracker.complete("cleanup")
            elif verbose:
                console.print(f"已清理：{zip_path.name}")
    
    return project_path


def ensure_executable_scripts(project_path: Path, tracker: StepTracker | None = None) -> None:
    """Ensure POSIX .sh scripts under .specify/scripts (recursively) have execute bits (no-op on Windows)."""
    if os.name == "nt":
        return  # Windows: skip silently
    scripts_root = project_path / ".specify" / "scripts"
    if not scripts_root.is_dir():
        return
    failures: list[str] = []
    updated = 0
    for script in scripts_root.rglob("*.sh"):
        try:
            if script.is_symlink() or not script.is_file():
                continue
            try:
                with script.open("rb") as f:
                    if f.read(2) != b"#!":
                        continue
            except Exception:
                continue
            st = script.stat(); mode = st.st_mode
            if mode & 0o111:
                continue
            new_mode = mode
            if mode & 0o400: new_mode |= 0o100
            if mode & 0o040: new_mode |= 0o010
            if mode & 0o004: new_mode |= 0o001
            if not (new_mode & 0o100):
                new_mode |= 0o100
            os.chmod(script, new_mode)
            updated += 1
        except Exception as e:
            failures.append(f"{script.relative_to(scripts_root)}: {e}")
    if tracker:
        detail = f"{updated} 已更新" + (f", {len(failures)} 失敗" if failures else "")
        tracker.add("chmod", "遞迴設定腳本權限")
        (tracker.error if failures else tracker.complete)("chmod", detail)
    else:
        if updated:
            console.print(f"[cyan]已遞迴更新 {updated} 個腳本的執行權限[/cyan]")
        if failures:
            console.print("[yellow]部分腳本無法更新：[/yellow]")
            for f in failures:
                console.print(f"  - {f}")

@app.command()
def init(
    project_name: str = typer.Argument(None, help="新專案目錄名稱（使用 --here 時可選，或使用 '.' 表示目前目錄）"),
    ai_assistant: str = typer.Option(None, "--ai", help="使用的 AI 助手：claude, gemini, copilot, cursor-agent, qwen, opencode, codex, windsurf, kilocode, auggie, codebuddy, roo, 或 q"),
    script_type: str = typer.Option(None, "--script", help="使用的腳本類型：sh 或 ps"),
    ignore_agent_tools: bool = typer.Option(False, "--ignore-agent-tools", help="跳過 AI 代理工具檢查（如 Claude Code）"),
    no_git: bool = typer.Option(False, "--no-git", help="跳過 git 儲存庫初始化"),
    here: bool = typer.Option(False, "--here", help="在目前目錄初始化專案，而非建立新目錄"),
    force: bool = typer.Option(False, "--force", help="使用 --here 時強制合併/覆蓋（跳過確認）"),
    skip_tls: bool = typer.Option(False, "--skip-tls", help="跳過 SSL/TLS 驗證（不建議）"),
    debug: bool = typer.Option(False, "--debug", help="顯示網路和解壓失敗的詳細診斷輸出"),
    github_token: str = typer.Option(None, "--github-token", help="用於 API 請求的 GitHub token（或設定 GH_TOKEN 或 GITHUB_TOKEN 環境變數）"),
):
    """
    從最新模板初始化新的 Specify 專案。

    此命令將會：
    1. 檢查必要工具是否已安裝（git 為可選）
    2. 讓你選擇 AI 助手（Claude Code、Gemini CLI、GitHub Copilot、Cursor、Qwen Code、opencode、Codex CLI、Windsurf、Kilo Code、Auggie CLI、CodeBuddy、Roo Code 或 Amazon Q Developer CLI）
    3. 從 GitHub 下載適當的模板
    4. 將模板解壓到新專案目錄或目前目錄
    5. 初始化新的 git 儲存庫（如果未使用 --no-git 且不存在儲存庫）
    6. 可選設定 AI 助手命令

    範例：
        specify-tw init my-project
        specify-tw init my-project --ai claude
        specify-tw init my-project --ai gemini
        specify-tw init my-project --ai copilot --no-git
        specify-tw init my-project --ai cursor-agent
        specify-tw init my-project --ai qwen
        specify-tw init my-project --ai opencode
        specify-tw init my-project --ai codex
        specify-tw init my-project --ai windsurf
        specify-tw init my-project --ai auggie
        specify-tw init my-project --ai codebuddy
        specify-tw init my-project --ai roo
        specify-tw init my-project --ai q
        specify-tw init --ignore-agent-tools my-project
        specify-tw init . --ai claude         # 在目前目錄初始化
        specify-tw init .                     # 在目前目錄初始化（互動式選擇 AI）
        specify-tw init --here --ai claude    # 目前目錄的替代語法
        specify-tw init --here --ai codex
        specify-tw init --here
        specify-tw init --here --force  # 目前目錄不為空時跳過確認
    """
    # Show banner first
    show_banner()

    # Handle '.' as shorthand for current directory (equivalent to --here)
    if project_name == ".":
        here = True
        project_name = None  # Clear project_name to use existing validation logic

    # Validate arguments
    if here and project_name:
        console.print("[red]錯誤：[/red] 不能同時指定專案名稱和 --here 標誌")
        raise typer.Exit(1)

    if not here and not project_name:
        console.print("[red]錯誤：[/red] 必須指定專案名稱、使用 '.' 表示目前目錄，或使用 --here 標誌")
        raise typer.Exit(1)
    
    # Determine project directory
    if here:
        project_name = Path.cwd().name
        project_path = Path.cwd()
        
        # Check if current directory has any files
        existing_items = list(project_path.iterdir())
        if existing_items:
            console.print(f"[yellow]警告：[/yellow] 目前目錄不為空 ({len(existing_items)} 個項目)")
            console.print("[yellow]模板檔案將與現有內容合併並可能覆蓋現有檔案[/yellow]")
            if force:
                console.print("[cyan]--force 已提供：跳過確認並繼續合併[/cyan]")
            else:
                # Ask for confirmation
                response = typer.confirm("是否要繼續？")
                if not response:
                    console.print("[yellow]操作已取消[/yellow]")
                    raise typer.Exit(0)
    else:
        project_path = Path(project_name).resolve()
        # Check if project directory already exists
        if project_path.exists():
            error_panel = Panel(
                f"目錄 '[cyan]{project_name}[/cyan]' 已存在\n"
                "請選擇不同的專案名稱或刪除現有目錄。",
                title="[red]目錄衝突[/red]",
                border_style="red",
                padding=(1, 2)
            )
            console.print()
            console.print(error_panel)
            raise typer.Exit(1)
    
    # Create formatted setup info with column alignment
    current_dir = Path.cwd()
    
    setup_lines = [
        "[cyan]Specify 專案設置[/cyan]",
        "",
        f"{'專案':<15} [green]{project_path.name}[/green]",
        f"{'工作路徑':<15} [dim]{current_dir}[/dim]",
    ]

    # Add target path only if different from working dir
    if not here:
        setup_lines.append(f"{'目標路徑':<15} [dim]{project_path}[/dim]")
    
    console.print(Panel("\n".join(setup_lines), border_style="cyan", padding=(1, 2)))
    
    # Check git only if we might need it (not --no-git)
    # Only set to True if the user wants it and the tool is available
    should_init_git = False
    if not no_git:
        should_init_git = check_tool("git", "https://git-scm.com/downloads")
        if not should_init_git:
            console.print("[yellow]未找到 Git - 將跳過儲存庫初始化[/yellow]")

    # AI assistant selection
    if ai_assistant:
        if ai_assistant not in AI_CHOICES:
            console.print(f"[red]錯誤：[/red] 無效的 AI 助手 '{ai_assistant}'。請選擇：{', '.join(AI_CHOICES.keys())}")
            raise typer.Exit(1)
        selected_ai = ai_assistant
    else:
        # Use arrow-key selection interface
        selected_ai = select_with_arrows(
            AI_CHOICES,
            "選擇你的 AI 助手：",
            "copilot"
        )
    
    # Check agent tools unless ignored
    if not ignore_agent_tools:
        agent_config = AGENT_CONFIG.get(selected_ai)
        if agent_config and agent_config["requires_cli"]:
            # Determine the CLI tool name to check
            cli_tool = selected_ai

            install_url = agent_config["install_url"]
            if not check_tool(cli_tool, install_url):
                error_panel = Panel(
                    f"未找到 [cyan]{selected_ai}[/cyan]\n"
                    f"安裝位置：[cyan]{install_url}[/cyan]\n"
                    f"需要 {AI_CHOICES[selected_ai]} 才能繼續此專案類型。\n\n"
                    "提示：使用 [cyan]--ignore-agent-tools[/cyan] 跳過此檢查",
                    title="[red]代理程式偵測錯誤[/red]",
                    border_style="red",
                    padding=(1, 2)
                )
                console.print()
                console.print(error_panel)
                raise typer.Exit(1)
    
    # Determine script type (explicit, interactive, or OS default)
    if script_type:
        if script_type not in SCRIPT_TYPE_CHOICES:
            console.print(f"[red]錯誤：[/red] 無效的腳本類型 '{script_type}'。請選擇：{', '.join(SCRIPT_TYPE_CHOICES.keys())}")
            raise typer.Exit(1)
        selected_script = script_type
    else:
        # Auto-detect default
        default_script = "ps" if os.name == "nt" else "sh"
        # Provide interactive selection similar to AI if stdin is a TTY
        if sys.stdin.isatty():
            selected_script = select_with_arrows(SCRIPT_TYPE_CHOICES, "選擇腳本類型（或按 Enter）", default_script)
        else:
            selected_script = default_script

    console.print(f"[cyan]選擇的 AI 助手：[/cyan] {selected_ai}")
    console.print(f"[cyan]選擇的腳本類型：[/cyan] {selected_script}")
    
    # Download and set up project
    # New tree-based progress (no emojis); include earlier substeps
    tracker = StepTracker("初始化 Specify 專案")
    # Flag to allow suppressing legacy headings
    sys._specify_tracker_active = True
    # Pre steps recorded as completed before live rendering
    tracker.add("precheck", "檢查必要工具")
    tracker.complete("precheck", "完成")
    tracker.add("ai-select", "選擇 AI 助手")
    tracker.complete("ai-select", f"{selected_ai}")
    tracker.add("script-select", "選擇腳本類型")
    tracker.complete("script-select", selected_script)
    for key, label in [
        ("fetch", "取得最新版本"),
        ("download", "下載模板"),
        ("extract", "解壓模板"),
        ("zip-list", "歸檔內容"),
        ("extracted-summary", "解壓摘要"),
        ("chmod", "確保腳本可執行"),
        ("cleanup", "清理"),
        ("git", "初始化 git 儲存庫"),
        ("final", "完成")
    ]:
        tracker.add(key, label)

    # Use transient so live tree is replaced by the final static render (avoids duplicate output)
    with Live(tracker.render(), console=console, refresh_per_second=8, transient=True) as live:
        tracker.attach_refresh(lambda: live.update(tracker.render()))
        try:
            # Create a httpx client with verify based on skip_tls
            verify = not skip_tls
            local_ssl_context = ssl_context if verify else False
            local_client = httpx.Client(verify=local_ssl_context)

            download_and_extract_template(project_path, selected_ai, selected_script, here, verbose=False, tracker=tracker, client=local_client, debug=debug, github_token=github_token)

            # Ensure scripts are executable (POSIX)
            ensure_executable_scripts(project_path, tracker=tracker)

            # Git step
            if not no_git:
                tracker.start("git")
                if is_git_repo(project_path):
                    tracker.complete("git", "偵測到現有儲存庫")
                elif should_init_git:
                    if init_git_repo(project_path, quiet=True):
                        tracker.complete("git", "已初始化")
                    else:
                        tracker.error("git", "初始化失敗")
                else:
                    tracker.skip("git", "git 不可用")
            else:
                tracker.skip("git", "--no-git 標誌")

            tracker.complete("final", "專案就緒")
        except Exception as e:
            tracker.error("final", str(e))
            console.print(Panel(f"初始化失敗：{e}", title="失敗", border_style="red"))
            if debug:
                _env_pairs = [
                    ("Python", sys.version.split()[0]),
                    ("Platform", sys.platform),
                    ("CWD", str(Path.cwd())),
                ]
                _label_width = max(len(k) for k, _ in _env_pairs)
                env_lines = [f"{k.ljust(_label_width)} → [dim]{v}[/dim]" for k, v in _env_pairs]
                console.print(Panel("\n".join(env_lines), title="調試環境", border_style="magenta"))
            if not here and project_path.exists():
                shutil.rmtree(project_path)
            raise typer.Exit(1)
        finally:
            # Force final render
            pass

    # Final static tree (ensures finished state visible after Live context ends)
    console.print(tracker.render())
    console.print("\n[bold green]專案就緒。[/bold green]")
    
    # Agent folder security notice
    if selected_ai in AGENT_FOLDER_MAP:
        agent_folder = AGENT_FOLDER_MAP[selected_ai]
        security_notice = Panel(
            f"某些代理程式可能會在專案內的代理程式資料夾中儲存憑證、身份驗證令牌或其他識別和私有工件。\n"
            f"考慮將 [cyan]{agent_folder}[/cyan]（或其部分）加入到 [cyan].gitignore[/cyan] 以防止意外洩露憑證。",
            title="[yellow]代理程式資料夾安全[/yellow]",
            border_style="yellow",
            padding=(1, 2)
        )
        console.print()
        console.print(security_notice)
    
    # Boxed "Next steps" section
    steps_lines = []
    if not here:
        steps_lines.append(f"1. 進入專案資料夾：[cyan]cd {project_name}[/cyan]")
        step_num = 2
    else:
        steps_lines.append("1. 你已經在專案目錄中！")
        step_num = 2

    # Add Codex-specific setup step if needed
    if selected_ai == "codex":
        codex_path = project_path / ".codex"
        quoted_path = shlex.quote(str(codex_path))
        if os.name == "nt":  # Windows
            cmd = f"setx CODEX_HOME {quoted_path}"
        else:  # Unix-like systems
            cmd = f"export CODEX_HOME={quoted_path}"

        steps_lines.append(f"{step_num}. 執行 Codex 前設定 [cyan]CODEX_HOME[/cyan] 環境變數：[cyan]{cmd}[/cyan]")
        step_num += 1

    steps_lines.append(f"{step_num}. 開始使用斜線命令與你的 AI 助手：")

    steps_lines.append("   - [cyan]/constitution[/] - 建立專案原則")
    steps_lines.append("   - [cyan]/specify[/] - 建立基線規範")
    steps_lines.append("   - [cyan]/plan[/] - 建立實施計畫")
    steps_lines.append("   - [cyan]/tasks[/] - 產生可執行任務")
    steps_lines.append("   - [cyan]/implement[/] - 執行實施")

    steps_panel = Panel("\n".join(steps_lines), title="後續步驟", border_style="cyan", padding=(1,2))
    console.print()
    console.print(steps_panel)

    enhancement_lines = [
        "可用於規範的選用命令 [bright_black]（提高品質和信心）[/bright_black]",
        "",
        f"○ [cyan]/clarify[/] [bright_black]（選用）[/bright_black] - 在規劃前提出結構化問題以降低模糊區域的風險（如果使用則在 [cyan]/plan[/] 前執行）",
        f"○ [cyan]/analyze[/] [bright_black]（選用）[/bright_black] - 跨工件一致性和對齊報告（在 [cyan]/tasks[/] 後，[cyan]/implement[/] 前）"
    ]
    enhancements_panel = Panel("\n".join(enhancement_lines), title="增強命令", border_style="cyan", padding=(1,2))
    console.print()
    console.print(enhancements_panel)

    if selected_ai == "codex":
        warning_text = """[bold yellow]重要說明：[/bold yellow]

自訂提示在 Codex 中尚不支援參數。您可能需要直接在位於 [cyan].codex/prompts/[/cyan] 的提示檔案中手動指定其他專案指令。

更多資訊，請參見：[cyan]https://github.com/openai/codex/issues/2890[/cyan]"""

        warning_panel = Panel(warning_text, title="Codex 中的斜線命令", border_style="yellow", padding=(1,2))
        console.print()
        console.print(warning_panel)

@app.command()
def check():
    """檢查是否已安裝所有必要工具。"""
    show_banner()
    console.print("[bold]正在檢查已安裝的工具...[/bold]\n")

    tracker = StepTracker("檢查可用工具")

    # Add Git first
    tracker.add("git", "Git 版本控制")
    git_ok = check_tool_for_tracker("git", tracker)

    # Add all agents from AGENT_CONFIG
    agent_results = {}
    for agent_key, agent_config in AGENT_CONFIG.items():
        agent_name = agent_config["name"]
        # Use the agent key as CLI tool name
        cli_tool = agent_key

        tracker.add(cli_tool, agent_name)
        agent_results[agent_key] = check_tool_for_tracker(cli_tool, tracker)

    # Check VS Code variants (not in agent config)
    tracker.add("code", "Visual Studio Code")
    code_ok = check_tool_for_tracker("code", tracker)

    tracker.add("code-insiders", "Visual Studio Code Insiders")
    code_insiders_ok = check_tool_for_tracker("code-insiders", tracker)

    console.print(tracker.render())

    console.print("\n[bold green]Specify TW CLI 已準備就緒！[/bold green]")

    if not git_ok:
        console.print("[dim]提示：安裝 git 用於儲存庫管理[/dim]")

    if not any(agent_results.values()):
        console.print("[dim]提示：安裝 AI 助手以獲得最佳體驗[/dim]")


def main():
    app()


if __name__ == "__main__":
    main()
