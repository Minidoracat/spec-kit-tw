# 變更紀錄

本專案的重要變更將記錄在此檔案中。

格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
並且本專案遵循[語義化版本](https://semver.org/lang/zh-TW/)。

## [0.0.78] - 2025-01-22

### 同步原版
- 同步原版 [v0.0.73](https://github.com/github/spec-kit/releases/tag/v0.0.73) 至 [v0.0.78](https://github.com/github/spec-kit/releases/tag/v0.0.78)
- 對應原版提交範圍：`e0dda02...926836e`（6個版本，36個檔案，+588/-194行）

### 新增功能
- **Amp AI 助手支援**：新增 Amp CLI 助手整合（`amp` 命令，目錄 `.agents/`）
- **技術棧擴充**：implement.md 新增 Swift、R 和 Kubernetes/k8s 的 .gitignore 模式支援
- **錯誤處理改善**：update-agent-context 腳本現在可處理沒有 "Active Technologies" 和 "Recent Changes" 區段的檔案，自動在檔案末尾新增缺失區段

### 變更內容
- 更新 CLI 核心（src/specify_cli/__init__.py）：
  - 新增 AGENT_CONFIG 中的 amp 配置
  - 更新 --ai 選項和說明文字以包含 amp
- 更新腳本系統：
  - scripts/bash/update-agent-context.sh：新增 AMP_FILE 變數、改善區段存在性檢查邏輯
  - scripts/powershell/update-agent-context.ps1：同步所有 bash 版本變更
- 更新命令模板：
  - templates/commands/implement.md：新增 Swift、R、Kubernetes/k8s 技術棧支援

### 技術改進
- 改善 update-agent-context 腳本的健壯性，支援不完整的代理檔案結構
- 自動偵測並補充缺失的 Markdown 區段（Active Technologies、Recent Changes）

### 未包含在此版本
- DevContainer 配置（.devcontainer/）- 計劃在後續版本中新增
- Markdown 格式標準化配置（.markdownlint-cli2.jsonc）- 計劃在後續版本中新增
- 命令模板的格式微調（analyze.md, checklist.md, clarify.md 等）- 功能已同步，格式美化待後續完善

## [0.0.72] - 2025-01-21

### 同步原版
- 同步原版 v0.0.70 至 v0.0.72（3個版本）
- 對應原版提交：[3b000fc...3e85f46](https://github.com/github/spec-kit/compare/3b000fc...3e85f46)
- 變更統計：9 個檔案，+98/-12 行

### 核心功能更新

#### **VS Code Settings 智慧合併功能**（v0.0.70）
- **新增功能**：`.vscode/settings.json` 現在採用智慧合併而非覆蓋
- **新增函式**：
  - `handle_vscode_settings()` - 處理 VS Code 設定檔案的合併或複製
  - `merge_json_files()` - 深度合併 JSON 檔案
- **合併邏輯**：
  - 保留現有設定
  - 新增 Spec Kit 設定
  - 遞迴合併巢狀物件
  - 防止意外丟失自訂 VS Code 工作區配置

#### **IDE 整合型 AI 助手 CLI 檢查邏輯優化**（v0.0.70）
- **優化內容**：
  - IDE 整合型助手（GitHub Copilot, Cursor, Windsurf）跳過 CLI 檢查
  - CLI 型助手（Claude Code, Gemini CLI 等）執行 CLI 檢查
  - IDE 型助手標記為「IDE 型，無需 CLI 檢查」

#### **修復 create-new-feature.sh 參數解析**（v0.0.71）
- **修復內容**：
  - 修正迴圈條件：`while [ $i -lt $# ]` → `while [ $i -le $# ]`
  - 修正迴圈起始值：`i=0` → `i=1`
  - 改善 `--short-name` 參數驗證邏輯
  - 新增檢查下一個參數是否為選項的邏輯

#### **修復 update-agent-context.sh 命令格式**（v0.0.72）
- **修復內容**：
  - 修正 JavaScript/TypeScript 命令格式：`echo "npm test \&\& npm run lint"` → `echo "npm test \\&\\& npm run lint"`

#### **媒體檔案優化**（v0.0.72）
- 優化 5 個媒體檔案，總體減少約 45% 檔案大小
  - `bootstrap-claude-code.gif`（541KB → 309KB）
  - `logo_large.webp`（84KB → 46KB）
  - `logo_small.webp`（11KB → 6KB）
  - `spec-kit-video-header.jpg`（188KB → 104KB）
  - `specify_cli.gif`（3.1MB → 1.7MB）

### 繁體中文本地化更新
- 完成所有新增函式和訊息的繁體中文翻譯
- 更新 README.md 使用提示為繁體中文
- 保持 `--version` 功能的繁體中文輸出

### 技術細節
- 在 `src/specify_cli/__init__.py` 中新增兩個 JSON 處理函式（約 90 行）
- 修改 `download_and_extract_template()` 函式整合 VS Code 設定檔案合併邏輯
- 修改 `check()` 函式優化 IDE 型 AI 助手的 CLI 檢查邏輯
- 更新版本號至 0.0.72（`pyproject.toml` 和 `__init__.py`）

### 繁體中文版本獨有功能（保留）
- **`--version` / `-v` 選項**：
  - 顯示 Specify TW CLI 版本資訊
  - 顯示對應的原版 spec-kit 版本
  - 輸出範例：
    ```
    Specify TW CLI 版本 0.0.72
    對應原版 spec-kit v0.0.72
    ```

---

## [0.0.69] - 2025-01-17

### 同步原版
- 同步原版 v0.0.65 至 v0.0.69（5個版本）
- 時間範圍：2025-01-16 之後發布
- 對應原版提交：[7b55522...3b000fc](https://github.com/github/spec-kit/compare/7b55522...3b000fc)
- 主要版本：v0.0.20（智慧分支命名系統）
- 變更統計：60 個檔案，+402/-72 行

### 核心功能更新

#### **智慧分支命名系統**（v0.0.20）
- **自訂分支名稱支援**：
  - Bash: 新增 `--short-name` 參數
  - PowerShell: 新增 `-ShortName` 參數
  - 允許開發者提供自訂的 2-4 詞短名稱

- **自動停用詞過濾**：
  - 過濾常見停用詞：I, want, to, the, for, of, in, on, at, by, with, from, is, are, was, were, be, been, being, have, has, had, do, does, did, will, would, should, could, can, may, might, must, shall, this, that, these, those, my, your, our, their, want, need, add, get, set
  - 自動移除長度小於 3 個字元的詞（除非是大寫縮寫）
  - 保留技術術語和縮寫（OAuth2、API、JWT、SQL 等）

- **智慧關鍵詞提取**：
  - 自動選取 3-4 個最有意義的關鍵詞
  - 偵測並保留原文中的大寫縮寫
  - 範例轉換：
    - "I want to create user authentication" → `001-create-user-authentication`
    - "Implement OAuth2 integration for API" → `001-implement-oauth2-integration-api`
    - "Fix payment processing bug" → `001-fix-payment-processing`

- **GitHub 限制驗證**：
  - 強制執行 244 字元分支名稱限制
  - 超過限制時自動截斷並顯示警告
  - 在詞邊界截斷以保持可讀性
  - 警告訊息範例：
    ```
    [specify] Warning: Branch name exceeded GitHub's 244-byte limit
    [specify] Original: 001-very-long-branch-name... (250 bytes)
    [specify] Truncated to: 001-very-long-branch... (244 bytes)
    ```

#### **CodeBuddy CLI 品牌更新**
- 名稱更新：CodeBuddy → **CodeBuddy CLI**
- 安裝連結更新：`https://www.codebuddy.ai` → `https://www.codebuddy.ai/cli`
- 影響檔案：
  - `src/specify_cli/__init__.py` - AGENT_CONFIG 配置
  - `AGENTS.md` - AI 助手表格
  - `README.md` - 支援列表
  - `docs/installation.md` - 安裝指南

### 腳本系統完全重構

#### **create-new-feature.sh**（Bash 版本）
- 新增 `--short-name` 參數解析邏輯
- 新增 `generate_branch_name()` 函式（~50 行）
- 實作停用詞過濾和長度驗證
- 實作 244 字元限制檢查和警告
- 新增說明文字和使用範例
- 總計新增 ~120 行核心邏輯

#### **create-new-feature.ps1**（PowerShell 版本）
- 新增 `-ShortName` 參數和 `-Help` 開關
- 新增 `Get-BranchName` 函式
- 實作 PowerShell 版本的停用詞陣列
- 實作等效的過濾和驗證邏輯
- 完整的 PowerShell 慣例和錯誤處理
- 總計新增 ~100 行核心邏輯

#### **common.sh**（Bash 通用函式）
- 新增 `find_feature_dir_by_prefix()` 函式
- 支援多分支共享同一規範（例如：004-fix-bug, 004-add-feature）
- 按數字前綴查找特性目錄而非精確匹配
- 改善錯誤處理和多重匹配檢測
- 更新 `get_feature_paths()` 使用新函式

#### **common.ps1**（PowerShell 通用函式）
- 完全同步 Bash 版本的功能
- PowerShell 等效的實作
- 保持跨平台一致性

### 模板增強（繁體中文翻譯）

#### **specify.md 命令模板**
- **新增步驟 1**：生成簡潔短名稱（2-4 詞）
  - 分析功能描述並提取最有意義的關鍵詞
  - 使用「動作-名詞」格式（例如：add-user-auth）
  - 保留技術術語和縮寫
  - 提供 4 個詳細範例

- **更新步驟 2**：附加 short-name 參數
  - Bash: `--short-name "your-generated-short-name"`
  - PowerShell: `-ShortName "your-generated-short-name"`
  - 新增引號轉義指引
  - 強調只執行一次的重要性

- **步驟重新編號**：原步驟 2-6 變更為 3-7

#### **implement.md 命令模板**
- **新增 6 種程式語言的 .gitignore 模式**：
  - **Ruby**: `.bundle/`, `log/`, `tmp/`, `*.gem`, `vendor/bundle/`
  - **PHP**: `vendor/`, `*.log`, `*.cache`, `*.env`
  - **Rust**: `target/`, `debug/`, `release/`, `*.rs.bk`, `*.rlib`, `*.prof*`, `.idea/`, `*.log`, `.env*`
  - **Kotlin**: `build/`, `out/`, `.gradle/`, `.idea/`, `*.class`, `*.jar`, `*.iml`, `*.log`, `.env*`
  - **C++**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.so`, `*.a`, `*.exe`, `*.dll`, `.idea/`, `*.log`, `.env*`
  - **C**: `build/`, `bin/`, `obj/`, `out/`, `*.o`, `*.a`, `*.so`, `*.exe`, `Makefile`, `config.log`, `.idea/`, `*.log`, `.env*`

### 文件更新（繁體中文翻譯）

#### **README.md**
- **標語更新**：
  - 原文：專注於產品情境而非撰寫無差異化的程式碼
  - 新文：專注於產品情境和可預測的結果，而不是從頭開始盲目編碼

- **標題規範化**（Title Case 調整）：
  - ⚡ 開始使用（Get Started）
  - 📚 核心理念（Core Philosophy）
  - 🌟 開發階段（Development Phases）
  - 🎯 實驗目標（Experimental Goals）
  - 📖 了解更多（Learn More）
  - 📋 詳細流程（Detailed Process）

- **CodeBuddy 更新**：
  - 支援列表中的連結和名稱更新
  - 說明文字保持一致

- **先決條件簡化**：
  - 移除冗長的 AI 助手列表
  - 改為連結到「支援的 AI 助手」章節
  - 更簡潔的表達方式

#### **docs/installation.md**
- **AI 助手列表更新**：
  - 新增 CodeBuddy CLI 到先決條件列表
  - 更新為新的安裝連結

- **安裝範例新增**：
  ```bash
  uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <project_name> --ai codebuddy
  ```

### 技術改進
- **檔案規範化**：
  - 新增 `.gitattributes` 檔案（LF 行結束符規範）
  - 所有檔案新增尾隨空行（符合 POSIX 標準）

- **媒體資源更新**：
  - `media/bootstrap-claude-code.gif` - 二進位更新
  - `media/logo_large.webp` - 二進位更新
  - `media/logo_small.webp` - 二進位更新
  - `media/spec-kit-video-header.jpg` - 二進位更新
  - `media/specify_cli.gif` - 二進位更新

### 繁體中文本地化
- **完整翻譯所有新增內容**：
  - 智慧分支命名工作流程指引
  - 命令模板的新增步驟和說明
  - README 和文件的所有變更
  - 新增語言的 .gitignore 模式說明

- **品牌標識保持**：
  - 套件名稱：`specify-tw-cli`
  - 命令名稱：`specify-tw`
  - GitHub 倉庫：`Minidoracat/spec-kit-tw`

- **術語一致性**：
  - 保留技術術語英文：OAuth2, API, JWT, Git, GitHub
  - 翻譯概念性術語：功能規範、實施計劃、程式碼品質
  - 統一使用繁體中文標點符號

### 貢獻者（原版）
感謝 GitHub Spec Kit 團隊對 v0.0.65-v0.0.69 的貢獻

### 已知問題
- 無

### 下一步計劃
- 持續追蹤原版更新
- 保持功能對等和繁體中文品質
- 優化智慧分支命名演算法

---

## [0.0.64] - 2025-01-16

### 同步原版
- 同步原版 v0.0.59 至 v0.0.64（7個版本，6天內發布）
- 時間範圍：2025-01-10 至 2025-01-16
- 同步提交區間：[89f4b0b...9dd20e1](https://github.com/github/spec-kit/compare/89f4b0b...9dd20e1)
- 詳細分析報告：見 `spec-kit-0.0.58-to-0.0.64-update-report.md`

### 核心架構重構
- **AGENT_CONFIG 架構**：
  - 從簡單的 `AI_CHOICES` 字典重構為結構化的 `AGENT_CONFIG`
  - 新增 `name`、`folder`、`install_url`、`requires_cli` 欄位
  - 統一使用實際 CLI 工具名稱作為鍵值（如 "cursor-agent"）
  - 簡化特殊情況處理邏輯

- **Git 錯誤處理增強**：
  - `init_git_repo()` 回傳型別改為 `Tuple[bool, Optional[str]]`
  - 提供詳細的錯誤訊息而非布林值
  - 改善錯誤診斷和使用者體驗

- **工具檢查統一化**：
  - `check_tool()` 函式支援可選的 tracker 參數
  - 統一進度追蹤介面
  - 簡化程式碼重複

### 新增 AI 助手支援
- **CodeBuddy**：
  - 新增 CodeBuddy 作為第 12 個支援的 AI 助手
  - 配置資訊：`.codebuddy/` 目錄，需要 CLI 工具
  - 安裝指引：https://www.codebuddy.ai
  - 新增工具檢查邏輯和安裝說明

### 命令模板增強（繁體中文翻譯）
- **plan.md**：
  - 修正 constitution.md 路徑引用（從 `.specify/memory/` 改為 `/memory/`）

- **clarify.md**：
  - 新增 AI 智慧推薦系統
  - 多選題自動分析並推薦最佳選項
  - 簡答題提供建議答案
  - 支援「是」、「推薦」、「建議」快速確認
  - 格式化推薦展示：`**推薦：** 選項 [X] - <理由>`

- **implement.md**：
  - 新增「專案設定驗證」步驟（Step 4）
  - 自動偵測並建立 .gitignore、.dockerignore、.eslintignore 等
  - 技術堆疊特定模式（Node.js、Python、Java、C#/.NET、Go）
  - 工具特定模式（Docker、ESLint、Prettier、Terraform）
  - 智慧追加缺失模式，避免覆蓋現有配置

- **tasks.md**：
  - 新增「檢查清單格式（必需）」嚴格規範
  - 標準化任務格式：`- [ ] [TaskID] [P?] [Story?] Description with file path`
  - 提供正確與錯誤範例說明
  - 明確定義任務組件：核取方塊、ID、平行標記、故事標籤、描述
  - 階段結構清晰化：Setup → Foundational → User Stories → Polish

### 文件更新
- 新增 `spec-kit-0.0.58-to-0.0.64-update-report.md` 詳細分析報告
- 新增 `SYNC-PROGRESS.md` 同步進度追蹤文件
- 更新 `CLAUDE.md` 專案記憶檔案（v0.0.64 架構資訊）

### 技術改進
- 14 個檔案變更，新增 477 行，刪除 283 行
- 完整繁體中文本地化所有新功能和訊息
- 改善 CLI 輸出的可讀性和一致性
- 優化模板結構以符合最新標準

### 貢獻者（原版）
感謝以下貢獻者對 spec-kit v0.0.59-v0.0.64 的貢獻：
- @irthomasthomas
- @hamelsmu

### 已知問題
- 核心程式碼 `src/specify_cli/__init__.py` 尚未完成 AGENT_CONFIG 重構（進行中）
- 腳本檔案 `scripts/` 尚未同步 CodeBuddy 支援（待處理）

### 下一步計劃
- 完成核心程式碼的 AGENT_CONFIG 架構遷移
- 同步所有腳本檔案以支援 CodeBuddy
- 更新 README.md 和 AGENTS.md 文件
- 執行完整功能測試驗證

## [0.0.58] - 2025-10-09

### 同步原版
- 同步原版 [v0.0.58](https://github.com/github/spec-kit/releases/tag/v0.0.58)
- 對應原版提交：[89f4b0b](https://github.com/github/spec-kit/commit/89f4b0b38a42996376c0f083d47281a4c9196761)

### 新增功能（v0.0.58）
- **Amazon Q Developer CLI 支援**：
  - 新增 Amazon Q Developer CLI 作為可選 AI 助手
  - 在 `AI_CHOICES` 中新增 `"q": "Amazon Q Developer CLI"`
  - 新增 Amazon Q 工具檢查邏輯和安裝指引
  - 在 `check()` 命令中新增 Amazon Q 檢查項目
  - 更新 `agent_folder_map` 包含 `.amazonq/` 目錄
  - 更新命令說明文字包含 Amazon Q 選項

- **命令模板引號轉義指引**：
  - 在所有命令模板中新增引號轉義使用說明
  - 影響檔案：analyze.md, checklist.md, clarify.md, implement.md, plan.md, specify.md, tasks.md
  - 指引內容：「對於參數中包含單引號的情況（如 "I'm Groot"），請使用轉義語法：例如 'I'\''m Groot'（或者如果可能，使用雙引號："I'm Groot"）」

### 翻譯改進
- **術語統一**：
  - 將 `memory/constitution.md` 中的「套件」統一修正為「函式庫」
  - 更準確地反映 Library 的技術含義
  - 影響 5 處範例註解

### 已知問題
- 無

## [0.0.57] - 2025-01-09

### 同步原版
- 同步原版 [v0.0.57](https://github.com/github/spec-kit/releases/tag/v0.0.57)
- 完整對應 spec-kit v0.0.57 版本的所有功能

### 繁體中文本地化
- **品牌識別轉換**：
  - 套件名稱：`specify-cn-cli` → `specify-tw-cli`
  - 命令名稱：`specify-cn` → `specify-tw`
  - 倉庫地址：`Linfee/spec-kit-cn` → `Minidoracat/spec-kit-tw`
  - 橫幅標語：「GitHub Spec Kit CN」 → 「GitHub Spec Kit TW - 規範驅動開發工具包」

- **完整繁體中文轉換**：
  - 所有使用者介面文字轉換為繁體中文
  - 所有文件和說明轉換為繁體中文
  - 所有模板檔案轉換為繁體中文
  - 所有命令模板轉換為繁體中文

### 新增功能（v0.0.57）
- **新增檢查清單功能**：
  - 新增 `templates/checklist-template.md` 模板
  - 新增 `templates/commands/checklist.md` 命令檔案
  - 支援為功能規範生成詳細的檢查清單
  - 檢查清單作為「需求的單元測試」，確保功能完整性

- **VS Code 整合**：
  - 新增 `templates/vscode-settings.json` 設定檔
  - 支援 VS Code 使用者更好的開發體驗

- **增強實施命令**：
  - `/implement` 命令新增檢查清單狀態驗證步驟
  - 在實施前確保所有前置需求已完成
  - 新增 PASS/FAIL 狀態表格輸出
  - 新增使用者確認機制

- **規範品質驗證**：
  - `/specify` 命令新增完整的品質驗證工作流程
  - 使用檢查清單驗證規範完整性
  - 限制 NEEDS CLARIFICATION 標記最多 3 個
  - 新增表格格式提醒

### 模板系統更新（v0.0.57）
- **核心模板重寫**：
  - `spec-template.md`：採用使用者故事優先級系統（P1, P2, P3）
  - `tasks-template.md`：新增 Foundational Phase 概念
  - `plan-template.md`：新增 agent_scripts YAML 區塊

- **測試策略變更**：
  - 測試現在標記為 OPTIONAL（可選）
  - 只在明確要求時才生成測試任務

- **Agent 腳本整合**：
  - 計劃模板新增 agent_scripts 支援
  - 自動更新 AI 助手上下文檔案

### 技術改進
- 完整的繁體中文化所有使用者可見文字
- 改善 CLI 輸出的可讀性
- 優化模板結構以符合 v0.0.57 標準

### 文件更新
- 完整重寫 `CLAUDE.md` 為繁體中文版本
- 更新專案記憶檔案以反映 TW 版本
- 新增 uvx 安裝指令說明
- 更新所有文件中的倉庫連結

### 已知問題
- 無

---

## [0.0.55] - 2025-10-02

### 同步原版
- 同步原版 [v0.0.55](https://github.com/github/spec-kit/releases/tag/v0.0.55)
- 對應原版提交：`e3b456c` (包含 13 個功能增強和 bug 修復提交)
- 主要提交：
  - `68eba52` - feat: support 'specify init .' for current directory initialization
  - `721ecc9` - feat: Add emacs-style up/down keys
  - `6a3e81f` - docs: fix the paths of generated files (moved under a `.specify/` folder)
  - `b2f749e` - fix: add UTF-8 encoding to file read/write operations in update-agent-context.ps1
  - `cc75a22` - Update URLs to Contributing and Support Guides in Docs

### 新增功能
- **新增 `specify init .` 支援**：可以使用 `.` 作為當前目錄初始化的簡寫，等同於 `--here` 標誌但更直觀
- **Emacs 風格快捷鍵**：新增 Ctrl+P (上) 和 Ctrl+N (下) 鍵盤支援
- **專案檔案結構更新**：生成的檔案現在統一放在 `.specify/` 目錄下

### 修復
- **UTF-8 編碼支援**：修復 PowerShell 腳本中的檔案讀寫編碼問題
- **文件連結修正**：更新貢獻指南和支援指南的連結位址

### 中文本地化更新
- 更新 README.md 中的命令列參數說明和範例
- 完善所有新增功能的使用範例和中文說明
- 更新專案結構描述，反映 `.specify/` 目錄變更

### 已知問題
- 無

---

## [0.0.54] - 2025-09-28

### 同步原版
- 同步原版 [v0.0.54](https://github.com/github/spec-kit/releases/tag/v0.0.54)
- 對應原版提交：`1c0e7d14d5d5388fbb98b7856ce9f486cc273997`

### 中文本地化更新
- 更新 README.md 中的版本資訊和原版對應關係
- 更新 `src/specify_cli/__init__.py` 檔案，從原版 spec-kit 專案複製並完全本地化
- 品牌標識更新：套件名稱 `specify-cn-cli`，命令名稱 `specify-cn`，GitHub 儲存庫 `Linfee/spec-kit-cn`
- 使用者介面完全中文化：所有錯誤訊息、狀態提示、說明文件、操作指導均已翻譯為中文
- 功能完整性驗證：核心 CLI 功能與原版完全對等，11 種 AI 助手支援完全一致

### 技術架構同步
- 核心程式碼架構：所有類別和函式名稱、方法簽章、演算法邏輯與原版保持一致
- 依賴管理：typer、rich、httpx 等依賴函式庫版本與原版同步
- 建置配置：hatchling 建置系統配置保持同步
- AI 助手支援：Claude Code、Gemini CLI、GitHub Copilot、Cursor、Qwen Code 等 11 種助手完全支援

### 已知問題
- 無

---

## [1.0.0] - 2024-09-16

### 新增
- 初始版本發布
- Spec-Driven Development 方法論完整實作
- CLI 工具支援
- 模板系統
- 文件生成功能
