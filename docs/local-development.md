# 本地開發指南

本指南展示如何在本地對 `specify` CLI 進行迭代開發，無需先發布版本或提交到 `main` 分支。

## 1. 複製和切換分支

```bash
git clone https://github.com/Minidoracat/spec-kit-tw.git
cd spec-kit-tw
# 在功能分支上工作
git checkout -b your-feature-branch
```

## 2. 直接執行 CLI（最快的回饋）

您可以透過模組進入點執行 CLI，無需安裝任何東西：

```bash
# 從倉庫根目錄
python -m src.specify_cli --help
python -m src.specify_cli init demo-project --ai claude --ignore-agent-tools
```

如果您更喜歡呼叫指令檔的方式（使用 shebang）：

```bash
python src/specify_cli/__init__.py init demo-project
```

## 3. 使用可編輯安裝（隔離環境）

使用 `uv` 建立隔離環境，這樣相依性的解析方式與最終使用者完全一致：

```bash
# 建立並啟動虛擬環境（uv 自動管理 .venv）
uv venv
source .venv/bin/activate  # 或在 Windows 上：.venv\\Scripts\\activate

# 以可編輯模式安裝專案
uv pip install -e .

# 現在 'specify' 進入點可用
specify --help
```

由於是可編輯模式，程式碼編輯後重新執行無需重新安裝。

## 4. 使用 uvx 直接從 Git（目前分支）呼叫

`uvx` 可以從本地路徑（或 Git 參考）執行，以模擬使用者流程：

```bash
uvx --from . specify init demo-uvx --ai copilot --ignore-agent-tools
```

您也可以將 uvx 指向特定分支而無需合併：

```bash
# 首先推送您的工作分支
git push origin your-feature-branch
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git@your-feature-branch specify-tw init demo-branch-test
```

### 4a. 絕對路徑 uvx（從任何位置執行）

如果您在其他目錄中，使用絕對路徑代替 `.`：

```bash
uvx --from /mnt/c/GitHub/spec-kit specify --help
uvx --from /mnt/c/GitHub/spec-kit specify init demo-anywhere --ai copilot --ignore-agent-tools
```

為方便起見，設定環境變數：
```bash
export SPEC_KIT_SRC=/mnt/c/GitHub/spec-kit
uvx --from "$SPEC_KIT_SRC" specify init demo-env --ai copilot --ignore-agent-tools
```

（可選）定義 shell 函數：
```bash
specify-dev() { uvx --from /mnt/c/GitHub/spec-kit specify "$@"; }
# 然後
specify-dev --help
```

## 5. 測試指令檔權限邏輯

執行 `init` 後，檢查 shell 指令檔在 POSIX 系統上是否可執行：

```bash
ls -l scripts | grep .sh
# 期望所有者執行位（例如 -rwxr-xr-x）
```
在 Windows 上此步驟為空操作。

## 6. 執行 Lint / 基本檢查（新增您自己的）

目前沒有捆綁強制性的 lint 設定，但您可以快速檢查可匯入性：
```bash
python -c "import specify_cli; print('Import OK')"
```

## 7. 本地建置 Wheel（可選）

在發布前驗證打包：

```bash
uv build
ls dist/
```
如果需要，將建置的工件安裝到新的臨時環境中。

## 8. 使用臨時工作區

在髒目錄中測試 `init --here` 時，建立臨時工作區：

```bash
mkdir /tmp/spec-test && cd /tmp/spec-test
python -m src.specify_cli init --here --ai claude --ignore-agent-tools  # 如果倉庫複製到這裡
```
或者如果您想要更輕量的沙盒，只複製修改後的 CLI 部分。

## 9. 除錯網路 / TLS 跳過

如果在實驗時需要繞過 TLS 驗證：

```bash
specify check --skip-tls
specify init demo --skip-tls --ai gemini --ignore-agent-tools
```
（僅用於本地實驗。）

## 10. 快速編輯迴圈總結

| 操作 | 命令 |
|------|------|
| 直接執行 CLI | `python -m src.specify_cli --help` |
| 可編輯安裝 | `uv pip install -e .` 然後 `specify ...` |
| 本地 uvx 執行（倉庫根目錄） | `uvx --from . specify ...` |
| 本地 uvx 執行（絕對路徑） | `uvx --from /mnt/c/GitHub/spec-kit specify ...` |
| Git 分支 uvx | `uvx --from git+URL@branch specify ...` |
| 建置 wheel | `uv build` |

## 11. 清理

快速刪除建置工件 / 虛擬環境：
```bash
rm -rf .venv dist build *.egg-info
```

## 12. 常見問題

| 症狀 | 修復方法 |
|------|----------|
| `ModuleNotFoundError: typer` | 執行 `uv pip install -e .` |
| 指令檔不可執行（Linux） | 重新執行 init（邏輯會新增權限位）或 `chmod +x scripts/*.sh` |
| Git 步驟被跳過 | 您傳遞了 `--no-git` 或未安裝 Git |
| 企業網路上的 TLS 錯誤 | 嘗試 `--skip-tls`（不用於生產環境） |

## 13. 下一步

- 更新文件並使用您修改後的 CLI 執行快速入門
- 滿意後開啟 PR
- （可選）變更合併到 `main` 後標記發布版本
