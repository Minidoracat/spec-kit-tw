# 變更紀錄

本專案的重要變更將記錄在此檔案中。

格式基於 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.0.0/)，
並且本專案遵循[語義化版本](https://semver.org/lang/zh-TW/)。

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
