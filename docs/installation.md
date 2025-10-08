# 安裝指南

## 前置要求

- **Linux/macOS**（或在Windows上的WSL2）
- AI編碼助手：[Claude Code](https://www.anthropic.com/claude-code)、[GitHub Copilot](https://code.visualstudio.com/)或[Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [uv](https://docs.astral.sh/uv/) 用於套件管理
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 安裝

### 初始化新專案

最簡單的入門方式是初始化一個新專案：

```bash
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <PROJECT_NAME>
```

或者在目前目錄中初始化：

```bash
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init .
# 或使用 --here 旗標
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init --here
```

### 指定AI助手

您可以在初始化時主動指定您的AI助手：

```bash
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <project_name> --ai claude
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <project_name> --ai gemini
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <project_name> --ai copilot
```

### 忽略助手工具檢查

如果您希望取得範本而不檢查正確的工具：

```bash
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <project_name> --ai claude --ignore-agent-tools
```

## 驗證

初始化後，您應該在AI助手中看到以下可用命令：
- `/specify` - 建立規範
- `/plan` - 產生實施計劃
- `/tasks` - 分解為可執行任務

## 疑難排解

### Linux上的Git憑證管理器

如果您在Linux上遇到Git身份驗證問題，可以安裝Git憑證管理器：

```bash
#!/usr/bin/env bash
set -e
echo "正在下載Git憑證管理器v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "正在安裝Git憑證管理器..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "正在設定Git使用GCM..."
git config --global credential.helper manager
echo "正在清理..."
rm gcm-linux_amd64.2.6.1.deb
```
