# Spec Kit TW

> **專案性質**：GitHub Spec Kit 的繁體中文版本，基於 spec-kit-cn 二次開發，專注繁體中文本地化

## 專案標識

### 核心資訊
- **專案名稱**：Spec Kit TW
- **原版專案**：[github/spec-kit](https://github.com/github/spec-kit)
- **基礎專案**：[Linfee/spec-kit-cn](https://github.com/Linfee/spec-kit-cn)
- **當前專案**：[Minidoracat/spec-kit-tw](https://github.com/Minidoracat/spec-kit-tw)
- **套件名稱**：`specify-tw-cli`
- **命令名稱**：`specify-tw`
- **文件語言**：繁體中文

### 核心原則
1. **功能對等**：與原版保持完全一致的功能，不添加新特性
2. **繁體中文化**：專注於繁體中文翻譯和本地化適配
3. **同步優先**：定期與原版同步，保持技術更新

### 關鍵差異
| 專案 | 原版          | 簡體版               | 繁體版               |
| ---- | ------------- | -------------------- | -------------------- |
| 套件 | `specify-cli` | `specify-cn-cli`     | `specify-tw-cli`     |
| 命令 | `specify`     | `specify-cn`         | `specify-tw`         |
| 文件 | English       | 简体中文             | 繁體中文             |
| 倉庫 | github/spec-kit | Linfee/spec-kit-cn | Minidoracat/spec-kit-tw |

---

## 快速參考

### 常用命令
```bash
# 開發環境
uv sync                              # 同步依賴
uv run specify-tw --help             # 執行 CLI
uv run specify-tw check              # 檢查工具鏈

# 測試功能
specify-tw init test-project --ai claude    # 測試專案初始化
specify-tw --help | grep -E "繁體|Spec Kit TW"  # 驗證繁體輸出

# 使用 uvx 直接從 GitHub 執行
uvx --from git+https://github.com/Minidoracat/spec-kit-tw spec-kit-tw init
```

### 專案目錄結構
```
專案根目錄/
├── src/specify_cli/           # 核心代碼（必須同步）
├── templates/                 # 模板檔案（需要本地化）
│   ├── 核心模板/             # 需要繁體翻譯
│   └── commands/             # 需要繁體翻譯
├── scripts/                   # 建置腳本（完全同步，不翻譯）
├── .github/                   # CI配置（謹慎同步，不翻譯）
├── docs/                     # 專案文件（需要本地化）
├── memory/                    # 專案章程（需要本地化）
│   └── constitution.md       # 專案章程檔案
├── spec-kit/                 # 原版專案（.gitignore）
├── CHANGELOG.md              # 版本記錄（獨立維護）
└── CLAUDE.md                 # 專案記憶檔案
```

### 檔案分類與處理策略
| 類別     | 目錄/檔案                     | 同步策略 | 本地化策略          |
| -------- | ----------------------------- | -------- | ------------------- |
| 核心代碼 | `src/specify_cli/`            | 必須同步 | CLI輸出訊息需繁體   |
| 模板系統 | `templates/`                  | 結構同步 | 完全繁體翻譯        |
| 建置腳本 | `scripts/`                    | 完全同步 | 不翻譯              |
| CI配置   | `.github/`                    | 謹慎同步 | 不翻譯              |
| 專案文件 | `docs/`, `README.md`          | 結構參考 | 完全繁體翻譯        |
| 專案章程 | `memory/constitution.md`      | 結構同步 | 完全繁體翻譯        |
| 原版追蹤 | `spec-kit/`                   | 不提交   | 不適用              |

### 版本對應關係
- **當前版本**：v0.0.79（查看 `pyproject.toml` 中的 `version` 欄位）
- **原版版本**：v0.0.79（Git tag，對應原版 CLI v0.0.20）
- **同步狀態**：已完成智慧分支編號系統同步（查看 `CHANGELOG.md` 中的同步記錄）
- **同步日期**：2025-10-27
- **同步範圍**：v0.0.78 → v0.0.79（3個檔案，+230/-35行）
- **核心功能**：防止分支編號重複的智慧檢測機制

### 緊急情況處理
1. **同步衝突**：優先保留原版功能，僅在本地化內容上保留修改
2. **版本不一致**：檢查 `pyproject.toml` 和 `CHANGELOG.md`
3. **功能異常**：對比原版專案，確認是否為同步問題

### 版本管理要求
- **重要**：任何對 `src/specify_cli/__init__.py` 的修改都需要：
  - 更新 `pyproject.toml` 中的版本號
  - 在 `CHANGELOG.md` 中新增相應條目
  - 同步原版更新時記錄對應的原版提交資訊

### AGENTS.md 比對檢查清單
每次同步原版版本時，必須檢查：
- [ ] 新增的 AI 助手支援
- [ ] 版本管理要求變化
- [ ] 整合步驟更新
- [ ] 重要技術細節補充
- [ ] CLI 工具檢查要求變化
- [ ] 目錄結構變更
- [ ] 命令格式調整

---

## 技術架構

### 核心組件

#### Specify CLI 結構 (`src/specify_cli/__init__.py`)
**主要類別和函式**：
- `StepTracker` - 分層步驟進度追蹤 UI 元件
- `select_with_arrows()` - 互動式箭頭鍵選擇介面
- `download_template_from_github()` - GitHub releases 模板下載
- `download_and_extract_template()` - 模板下載和解壓縮
- `handle_vscode_settings()` - VS Code 設定檔案智慧合併處理（v0.0.70 新增）
- `merge_json_files()` - 深度合併 JSON 檔案（v0.0.70 新增）
- `init()` - 主要專案初始化命令
- `check()` - 工具可用性檢查

**關鍵特性**：
- 支援多種 AI 程式碼助手
- 即時進度追蹤和樹狀顯示
- 跨平台支援（Linux/macOS/Windows）
- 自動腳本權限設定（POSIX）
- Git 儲存庫自動初始化
- VS Code 設定智慧合併（v0.0.70 新增）- 防止覆蓋使用者自訂配置
- IDE 型 AI 助手智慧檢測（v0.0.70 新增）- 跳過不必要的 CLI 檢查

### `__init__.py` 同步策略

#### 同步原則
**核心策略**：採用「**核心同步，介面本地化**」的策略，確保與原版功能完全對等的同時，為繁體中文使用者提供友善的母語介面。

#### 必須同步的內容
- ✅ **所有類別和函式名稱**
- ✅ **方法簽章和參數**：完全與原版一致，確保功能對等
- ✅ **核心演算法邏輯**：模板下載、解壓縮、Git初始化等核心流程
- ✅ **依賴函式庫和版本**：typer、rich、httpx 等依賴保持同步，同步更新 pyproject.toml
- ✅ **AI助手支援**：所有AI助手的支援邏輯完全一致
- ✅ **建置配置**：hatchling 建置系統保持同步

#### 需要本地化的內容
- 📝 **品牌標識**：套件名稱、命令名稱、GitHub儲存庫、橫幅標語
- 📝 **使用者介面文字**：錯誤訊息、狀態提示、互動介面
- 📝 **說明文件**：使用說明、操作指導、除錯資訊
- 📝 **輸出訊息**：CLI 輸出、進度顯示、工具檢查結果

### AI 助手支援（v0.0.64更新）
| 助手                    | CLI 工具       | 目錄格式               | 命令格式 | 類型   | 版本    |
| ----------------------- | -------------- | ---------------------- | -------- | ------ | ------- |
| Claude Code             | `claude`       | `.claude/commands/`    | Markdown | CLI    | 基線    |
| Gemini CLI              | `gemini`       | `.gemini/commands/`    | TOML     | CLI    | 基線    |
| GitHub Copilot          | 無（IDE 整合） | `.github/prompts/`     | Markdown | IDE    | 基線    |
| Cursor                  | `cursor-agent` | `.cursor/commands/`    | Markdown | CLI    | 基線    |
| Qwen Code               | `qwen`         | `.qwen/commands/`      | TOML     | CLI    | 基線    |
| opencode                | `opencode`     | `.opencode/command/`   | Markdown | CLI    | 基線    |
| Windsurf                | 無（IDE 整合） | `.windsurf/workflows/` | Markdown | IDE    | 基線    |
| Codex                   | `codex`        | `.codex/`              | Markdown | CLI    | 基線    |
| Kilocode                | `kilocode`     | `.kilocode/`           | Markdown | CLI    | 基線    |
| Auggie                  | `auggie`       | `.auggie/`             | Markdown | CLI    | 基線    |
| **CodeBuddy CLI**       | `codebuddy`    | `.codebuddy/`          | Markdown | CLI    | v0.0.64 |
| Roo Code                | `roo`          | `.roo/`                | Markdown | CLI    | 基線    |
| Amazon Q Developer CLI  | `q`            | `AGENTS.md`            | Markdown | CLI    | 基線    |

### 模板系統

#### 核心模板 (`templates/`)
- `spec-template.md` - 功能規範模板
- `plan-template.md` - 實施計劃模板
- `tasks-template.md` - 任務生成模板
- `agent-file-template.md` - AI 助手配置模板
- `checklist-template.md` - 檢查清單模板（v0.0.57 新增）
- `vscode-settings.json` - VS Code 設定檔（v0.0.57 新增）

#### 專案章程 (`memory/`)
- `constitution.md` - 專案章程模板（v0.0.54 新增）
  - 作用：定義專案核心原則和開發標準
  - 特點：AI 開發時必須遵循的「架構DNA」
  - 格式：使用佔位符模板，專案初始化時填充具體內容

#### 命令模板 (`templates/commands/`)
- `analyze.md` - 分析問題的命令
- `clarify.md` - 釐清需求的命令
- `constitution.md` - 管理專案章程的命令
- `implement.md` - 實施功能的命令
- `plan.md` - 生成實施計劃的命令
- `specify.md` - 建立功能規格的命令
- `tasks.md` - 生成可執行任務的命令
- `checklist.md` - 生成檢查清單的命令（v0.0.57 新增）

### 腳本系統

#### Bash 腳本 (`scripts/bash/`)
- `check-prerequisites.sh` - 檢查前置條件
- `common.sh` - 通用函式和變數
  - `find_feature_dir_by_prefix()` - 按數字前綴查找特性目錄（v0.0.69 新增）
  - 支援多分支共享同一規範
- `create-new-feature.sh` - 建立新功能分支和規範
  - **智慧分支命名系統**（v0.0.69 新增）：
    - `--short-name` 參數支援自訂分支名稱
    - `generate_branch_name()` 函式：自動停用詞過濾和關鍵詞提取
    - GitHub 244 字元限制驗證和自動截斷
- `setup-plan.sh` - 設定計劃環境
- `update-agent-context.sh` - 更新 AI 助手上下文檔案

#### PowerShell 腳本 (`scripts/powershell/`)
- 對應的 PowerShell 版本，提供相同功能
- `create-new-feature.ps1` - **智慧分支命名系統**（v0.0.69 新增）：
  - `-ShortName` 參數和 `-Help` 開關
  - `Get-BranchName` 函式：PowerShell 版本的智慧命名邏輯
  - 完整的停用詞過濾和 244 字元限制驗證
- `common.ps1` - PowerShell 版本的通用函式庫

---

## 維護工作流程

### 版本同步策略

#### 基本原則
- **版本號**：本專案 tag 單獨迭代，不需要和原版同步
- **功能同步**：定期從上游合併，不新增新功能
- **發布節奏**：跟隨原版發布，不獨立發布新功能

#### 同步機制

**spec-kit 目錄工作機制**：
```
專案根目錄/
├── spec-kit/              # 原版專案目錄（.gitignore）
│   ├── .git/             # 原版 git 歷史
│   ├── src/              # 原版原始碼
│   ├── templates/        # 原版模板
│   └── ...
├── .gitignore            # 忽略 spec-kit/ 目錄
└── ...                   # 本專案檔案
```

**同步工作流程**：
1. 檢查當前版本對應的原版 tag/commit
2. 在 `spec-kit/` 目錄檢出對應原版版本
3. 對比分析原版變更內容
4. **關鍵步驟**：將原版 `AGENTS.md` 複製到當前專案，比對專案記憶是否有缺失並補充
5. 根據檔案分類策略執行同步
6. 更新 CHANGELOG.md 記錄同步資訊

**AGENTS.md 比對的重要性**：
- 原版 `AGENTS.md` 包含最新的 AI 助手支援資訊和技術細節
- 每次同步時必須比對，確保專案記憶的準確性
- 重點關注：新助手支援、版本管理要求、整合步驟變化
- 比對後及時更新 `CLAUDE.md` 中的相關內容

**新 AI 助手整合注意事項**：
- 如需新增新的 AI 助手支援，必須同步原版更新
- 需要更新的檔案包括：`src/specify_cli/__init__.py`、`scripts/` 目錄下腳本、`.github/` 工作流
- 參考原版 `AGENTS.md` 檔案取得完整的整合步驟

### CHANGELOG 維護

**維護原則**：
- `CHANGELOG.md` 由本專案獨立維護，不與原版同步
- 記錄每個版本同步的原版資訊和繁體中文本地化更新

**記錄格式**：
```markdown
## [0.0.57] - 2025-01-09

### 同步原版
- 同步原版 [v0.0.57](https://github.com/github/spec-kit/releases/tag/v0.0.57)
- 對應原版提交：`abc123def456...`

### 繁體中文本地化更新
- 完成所有模板檔案的繁體中文翻譯
- 更新 CLI 介面為繁體中文
- 修正文件編碼問題

### 已知問題
- 無
```

### 繁體中文本地化標準

#### 本地化範圍

**需要完全繁體中文本地化的內容**：
- 使用者文件：`README.md`、`spec-driven.md`、`docs/` 目錄
- 模板系統：`templates/` 和 `templates/commands/` 目錄下的所有檔案
- 專案章程：`memory/constitution.md`（包括佔位符和說明文字）
- CLI 介面：`src/specify_cli/` 中的輸出訊息、說明文字、錯誤訊息

**保持英文不翻譯的內容**：
- 建置腳本：`scripts/` 目錄（完全同步原版）
- 媒體資源：`media/` 目錄（完全同步原版）
- CI配置：`.github/` 目錄（謹慎同步，不翻譯）
- 程式碼層面：變數名稱、函式名稱、類別名稱等識別符號
- 章程佔位符：如 `[PROJECT_NAME]`、`[PRINCIPLE_1_NAME]` 等（保持原格式）

#### 翻譯標準

**翻譯原則**：
- **使用者導向**：面向繁體中文開發者，翻譯使用者介面和文件
- **技術保留**：程式碼層面保持英文，確保技術準確性
- **功能對等**：翻譯後功能必須與原版完全一致

**術語處理**：

**不翻譯的英文術語**：
- CLI, API, JSON, TOML, YAML
- Git, GitHub, Repository, Branch, Commit
- Python, JavaScript, TypeScript
- Framework, Library, Package, Dependency
- Template, Script, Command, Argument
- AI 助手名稱：Claude Code, Gemini CLI, GitHub Copilot, Cursor

**需要翻譯的概念**：
- "Spec-Driven Development" → "規範驅動開發"
- "User Story" → "使用者故事"
- "Acceptance Criteria" → "驗收標準"
- "Implementation Plan" → "實施計劃"
- "Code Quality" → "程式碼品質"
- "Feature Specification" → "功能規範"

**語言風格**：
- 使用簡潔、準確的技術繁體中文
- 避免過度口語化，保持專業性
- 句式結構清晰，避免長難句
- 統一術語使用

**中英文混排規則**：
```markdown
✅ 推薦：
- 使用 Claude Code CLI 進行開發
- 支援 JSON 格式的設定檔
- 透過 GitHub API 取得資料

❌ 避免：
- 使用Claude Code CLI進行開發
- 支援 JSON 格式的設定檔
```

**標點符號**：
- 使用繁體中文標點（，。：；！？）
- 英文術語後使用英文標點
- 程式碼範例中使用英文標點

**品牌處理**：
- GitHub → GitHub（不翻譯）
- Claude Code → Claude Code（不翻譯）
- Spec Kit → Spec Kit（不翻譯，可加註「規範工具包」）
- 版本號保持原樣（v0.0.57）

---

## 品質保證

### 翻譯品質檢查清單

翻譯完成後必須檢查：
- [ ] 術語使用是否一致
- [ ] 中英文混排是否恰當
- [ ] 技術準確性是否保持
- [ ] 語句是否通順易懂
- [ ] 格式是否統一規範
- [ ] 連結和引用是否正確
- [ ] 程式碼範例是否保持原樣
- [ ] 與原版功能是否完全一致

### 功能一致性檢查

**必須保持一致**：
- 核心功能和 API
- 專案結構和檔案組織
- 支援的 AI 助手列表
- 模板和命令的工作流程

**允許差異**：
- 套件名稱和命令名稱（specify-tw vs specify）
- 文件語言（繁體中文 vs 英文）
- GitHub releases 下載源
- 預設配置和選項

### 程式碼品質檢查

由於是複刻專案，重點關注：
- 測試基本功能
- 檢查模板檔案是否包含繁體中文
- 驗證 CLI 輸出是否正確本地化
- 確保同步後的功能完整性

---

## 附錄

### 術語表

| 英文                    | 繁體中文     | 說明                   |
| ----------------------- | ------------ | ---------------------- |
| Spec-Driven Development | 規範驅動開發 | SDD 方法論             |
| User Story              | 使用者故事   | 需求描述方式           |
| Acceptance Criteria     | 驗收標準     | 功能完成條件           |
| Implementation Plan     | 實施計劃     | 開發執行方案           |
| Feature Specification   | 功能規範     | 功能詳細說明           |
| CLI                     | CLI          | 命令列介面（不翻譯）   |
| API                     | API          | 應用程式介面（不翻譯） |
| Template                | 模板         | 專案初始化模板         |

### 檔案模板

**新版本同步記錄模板**：
```markdown
## [x.x.x] - YYYY-MM-DD

### 同步原版
- 同步原版 [v.x.x](連結)
- 對應原版提交：`commit-hash`

### 繁體中文本地化更新
- [具體的本地化更新內容]

### 已知問題
- [已知問題和解決方案]
```

### 參考連結

- **原版專案**：[github/spec-kit](https://github.com/github/spec-kit)
- **原版文件**：[spec-kit/docs](https://github.com/github/spec-kit/tree/main/docs)
- **原版 AGENTS.md**：[spec-kit/AGENTS.md](https://github.com/github/spec-kit/blob/main/AGENTS.md)
- **GitHub Releases**：[spec-kit/releases](https://github.com/github/spec-kit/releases)
- **簡體版儲存庫**：[Linfee/spec-kit-cn](https://github.com/Linfee/spec-kit-cn)
- **繁體版儲存庫**：[Minidoracat/spec-kit-tw](https://github.com/Minidoracat/spec-kit-tw)

---

## 文件維護說明

本文件是 Spec Kit TW 專案的核心記憶檔案，用於指導 Claude Code 進行專案維護。請確保：

1. **及時更新**：同步原版更新後及時更新相關內容
2. **保持準確**：所有命令、路徑、版本號必須準確
3. **結構清晰**：維護良好的文件結構，便於快速查找
4. **內容完整**：確保所有重要的維護資訊都已包含

**最後更新**：2025-01-17 - 完成 v0.0.69 版本同步（智慧分支命名系統與 CodeBuddy CLI 更新）
