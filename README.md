<div align="center">
    <img src="./media/logo_small.webp"/>
    <h1>🌱 Spec Kit TW</h1>
    <h3><em>更快地建置高品質軟體。</em></h3>
</div>

<p align="center">
    <strong>這是一項旨在幫助組織專注於產品場景而非編寫無差異化程式碼的努力，借助規範驅動開發（Spec-Driven Development）的力量。</strong>
</p>

<div align="center">

[![Release](https://github.com/Minidoracat/spec-kit-tw/actions/workflows/release.yml/badge.svg)](https://github.com/Minidoracat/spec-kit-tw/actions/workflows/release.yml)
[![GitHub Repo](https://img.shields.io/badge/GitHub-spec--kit--tw-blue?logo=github)](https://github.com/Minidoracat/spec-kit-tw.git)
[![Current Version](https://img.shields.io/badge/version-0.0.57-green)](https://github.com/Minidoracat/spec-kit-tw/releases)

</div>

> **💡 這是 [GitHub Spec Kit](https://github.com/github/spec-kit) 的官方中文複刻版本**
> **🔄 對應原版提交**: [`e3b456c4c88be456ab190b3bebdb1e97c94fa6db`](https://github.com/github/spec-kit/commit/e3b456c4c88be456ab190b3bebdb1e97c94fa6db)
> **📦 包名**: `specify-tw-cli` | **🛠️ 命令**: `specify-tw`

> **⚠️ 保持同步**: 本專案將定期與原版保持同步，確保中文使用者能夠享受最新的功能和改進。

---

## 目錄

- [目錄](#目錄)
  - [🎯 差異說明](#-差異說明)
- [🤔 什麼是規範驅動開發？](#-什麼是規範驅動開發)
- [⚡ 快速開始](#-快速開始)
  - [1. 安裝 Specify TW](#1-安裝-specify-tw)
    - [方式1：持久化安裝（推薦）](#方式1持久化安裝推薦)
    - [方式2：一次性使用](#方式2一次性使用)
  - [2. 建立專案原則](#2-建立專案原則)
  - [3. 建立規範](#3-建立規範)
  - [4. 建立技術實施計畫](#4-建立技術實施計畫)
  - [5. 分解任務](#5-分解任務)
  - [6. 執行實施](#6-執行實施)
- [📽️ 影片概述](#️-影片概述)
- [🤖 支援的AI代理](#-支援的ai代理)
- [🔧 Specify TW CLI 參考](#-specify-tw-cli-參考)
  - [命令](#命令)
  - [`specify-tw init` 參數和選項](#specify-tw-init-參數和選項)
  - [範例](#範例)
  - [可用的斜線命令](#可用的斜線命令)
  - [環境變數](#環境變數)
- [📚 核心理念](#-核心理念)
- [🌟 開發階段](#-開發階段)
- [🎯 實驗目標](#-實驗目標)
  - [技術獨立性](#技術獨立性)
  - [企業約束](#企業約束)
  - [以使用者為中心的開發](#以使用者為中心的開發)
  - [創意和迭代過程](#創意和迭代過程)
- [🔧 前置要求](#-前置要求)
- [📖 了解更多](#-了解更多)
- [📋 詳細流程](#-詳細流程)
  - [**步驟1：** 建立專案原則](#步驟1-建立專案原則)
  - [**步驟2：** 建立專案規範](#步驟2-建立專案規範)
  - [**步驟3：** 功能規範澄清（計畫前必需）](#步驟3-功能規範澄清計畫前必需)
  - [**步驟4：** 生成計畫](#步驟4-生成計畫)
  - [**步驟5：** 讓Claude Code驗證計畫](#步驟5-讓claude-code驗證計畫)
  - [**步驟6：** 實施](#步驟6-實施)
- [🔍 故障排除](#-故障排除)
  - [Linux上的Git憑證管理器](#linux上的git憑證管理器)
- [👥 維護者](#-維護者)
- [💬 支援](#-支援)
- [🙏 致謝](#-致謝)
- [📄 授權](#-授權)


### 🎯 差異說明

| 項目 | Spec Kit原版  | Spec Kit TW中文版 |
| ---- | ------------- | ----------------- |
| 命令 | `specify`     | `specify-tw`      |
| 包名 | `specify-cli` | `specify-tw-cli`  |
| 文檔 | 英文          | 中文              |

---

## 🤔 什麼是規範驅動開發？

規範驅動開發**徹底改變**了傳統軟體開發的方式。幾十年來，程式碼一直佔據主導地位——規範只是我們在編碼「真正工作」開始時建置和丟棄的腳手架。規範驅動開發改變了這一點：**規範變得可執行**，直接生成可工作的實作，而不僅僅是指導它們。

## ⚡ 快速開始

### 1. 安裝 Specify TW

選擇您偏好的安裝方式：

#### 方式1：持久化安裝（推薦）

一次安裝，隨處使用：

```bash
uv tool install specify-tw-cli --from git+https://github.com/Minidoracat/spec-kit-tw.git
```

然後直接使用工具：

```bash
specify-tw init <PROJECT_NAME>
specify-tw check
```

#### 方式2：一次性使用

直接執行，無需安裝：

```bash
uvx --from git+https://github.com/Minidoracat/spec-kit-tw.git specify-tw init <PROJECT_NAME>
```

**持久化安裝的優勢**：

- 工具保持安裝狀態並在 PATH 中可用
- 無需建立 shell 別名
- 更好的工具管理：`uv tool list`、`uv tool upgrade`、`uv tool uninstall`
- 更簡潔的 shell 配置

### 2. 建立專案原則

使用 **`/constitution`** 命令建立專案的指導原則和開發指南，這將指導所有後續開發。

```bash
/constitution 建立專注於程式碼品質、測試標準、使用者體驗一致性和效能要求的原則
```

### 3. 建立規範

使用 **`/specify`** 命令描述您想要建置的內容。專注於**做什麼**和**為什麼**，而不是技術堆疊。

```bash
/specify 建置一個可以幫助我將照片整理到不同相簿中的應用程式。相簿按日期分組，可以透過在主頁上拖曳來重新組織。相簿不會巢狀在其他相簿中。在每個相簿內，照片以瓷磚介面預覽。
```

### 4. 建立技術實施計畫

使用 **`/plan`** 命令提供您的技術堆疊和架構選擇。

```bash
/plan 應用程式使用Vite和最少數量的函式庫。盡可能使用純HTML、CSS和JavaScript。圖片不會上傳到任何地方，詮釋資料儲存在本地SQLite資料庫中。
```

### 5. 分解任務

使用 **`/tasks`** 從您的實施計畫建立可操作的任務清單。

```bash
/tasks
```

### 6. 執行實施

使用 **`/implement`** 執行所有任務並根據計畫建置您的功能。

```bash
/implement
```

詳細的分步說明，請參閱我們的[綜合指南](./spec-driven.md)。

## 📽️ 影片概述

想要觀看 Spec Kit 的實際操作？觀看我們的[影片概述](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)！

[![Spec Kit 影片標題](/media/spec-kit-video-header.jpg)](https://www.youtube.com/watch?v=a9eR1xsfvHg&pp=0gcJCckJAYcqIYzv)

## 🤖 支援的AI代理

| 代理                                                      | 支援 | 說明                                                                               |
| --------------------------------------------------------- | ---- | ---------------------------------------------------------------------------------- |
| [Claude Code](https://www.anthropic.com/claude-code)      | ✅    |                                                                                    |
| [GitHub Copilot](https://code.visualstudio.com/)          | ✅    |                                                                                    |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | ✅    |                                                                                    |
| [Cursor](https://cursor.sh/)                              | ✅    |                                                                                    |
| [Qwen Code](https://github.com/QwenLM/qwen-code)          | ✅    |                                                                                    |
| [opencode](https://opencode.ai/)                          | ✅    |                                                                                    |
| [Windsurf](https://windsurf.com/)                         | ✅    |                                                                                    |
| [Kilo Code](https://github.com/Kilo-Org/kilocode)         | ✅    |                                                                                    |
| [Auggie CLI](https://docs.augmentcode.com/cli/overview)   | ✅    |                                                                                    |
| [Roo Code](https://roocode.com/)                          | ✅    |                                                                                    |
| [Codex CLI](https://github.com/openai/codex)              | ⚠️    | Codex [不支援](https://github.com/openai/codex/issues/2890) 斜線命令的自訂參數。 |

## 🔧 Specify TW CLI 參考

`specify-tw` 命令支援以下選項：

### 命令

| 命令    | 描述                                                                                                                          |
| ------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `init`  | 從最新模板初始化新的 Specify TW 專案                                                                                          |
| `check` | 檢查已安裝的工具 (`git`, `claude`, `gemini`, `code`/`code-insiders`, `cursor-agent`, `windsurf`, `qwen`, `opencode`, `codex`) |

### `specify-tw init` 參數和選項

| 參數/選項              | 類型 | 描述                                                                                                                             |
| ---------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------- |
| `<project-name>`       | 參數 | 新專案目錄的名稱（使用 `--here` 時可選，或使用 `.` 表示目前目錄）                                                                                         |
| `--ai`                 | 選項 | 要使用的AI助手：`claude`, `gemini`, `copilot`, `cursor`, `qwen`, `opencode`, `codex`, `windsurf`, `kilocode`, `auggie`, 或 `roo` |
| `--script`             | 選項 | 要使用的指令碼變體：`sh` (bash/zsh) 或 `ps` (PowerShell)                                                                           |
| `--ignore-agent-tools` | 標誌 | 跳過AI代理工具的檢查，如 Claude Code                                                                                             |
| `--no-git`             | 標誌 | 跳過 git 儲存庫初始化                                                                                                              |
| `--here`               | 標誌 | 在目前目錄初始化專案，而不是建立新目錄                                                                                           |
| `--force`              | 標誌 | 在目前目錄中初始化時強制合併/覆寫（跳過確認）                                                                                    |
| `--skip-tls`           | 標誌 | 跳過 SSL/TLS 驗證（不推薦）                                                                                                      |
| `--debug`              | 標誌 | 啟用詳細除錯輸出以進行故障排除                                                                                                   |
| `--github-token`       | 選項 | API 請求的 GitHub 權杖（或設定 GH_TOKEN/GITHUB_TOKEN 環境變數）                                                                  |

### 範例

```bash
# 基本專案初始化
specify-tw init my-project

# 使用特定AI助手初始化
specify-tw init my-project --ai claude

# 使用 Cursor 支援初始化
specify-tw init my-project --ai cursor

# 使用 Windsurf 支援初始化
specify-tw init my-project --ai windsurf

# 使用 PowerShell 指令碼初始化（Windows/跨平台）
specify-tw init my-project --ai copilot --script ps

# 在目前目錄初始化
specify-tw init . --ai copilot
# 或使用 --here 標誌
specify-tw init --here --ai copilot

# 強制合併到目前（非空）目錄而無需確認
specify-tw init . --force --ai copilot
# 或
specify-tw init --here --force --ai copilot

# 跳過 git 初始化
specify-tw init my-project --ai gemini --no-git

# 啟用除錯輸出以進行故障排除
specify-tw init my-project --ai claude --debug

# 使用 GitHub 權杖進行 API 請求（對企業環境有幫助）
specify-tw init my-project --ai claude --github-token ghp_your_token_here

# 檢查系統要求
specify-tw check
```

### 可用的斜線命令

執行 `specify-tw init` 後，您的AI編碼代理將可以使用這些斜線命令進行結構化開發：

| 命令            | 描述                                                                           |
| --------------- | ------------------------------------------------------------------------------ |
| `/constitution` | 建立或更新專案指導原則和開發指南                                               |
| `/specify`      | 定義您想要建置的內容（需求和使用者故事）                                         |
| `/clarify`      | 澄清未充分說明的區域（必須在 `/plan` 之前執行，除非明確跳過；以前為 `/quizme`) |
| `/plan`         | 使用您選擇的技術堆疊建立技術實施計畫                                             |
| `/tasks`        | 為實施生成可操作的任務清單                                                     |
| `/analyze`      | 跨工件一致性和覆蓋範圍分析（在 /tasks 之後，/implement 之前執行）              |
| `/implement`    | 執行所有任務以根據計畫建置功能                                                 |

### 環境變數

| 變數              | 描述                                                                                                                                                                                           |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SPECIFY_FEATURE` | 為非 Git 儲存庫覆蓋功能偵測。設定為功能目錄名稱（例如，`001-photo-albums`）以在不使用 Git 分支的情況下處理特定功能。<br/>**必須在您正在使用的代理內容中設定，然後才能使用 `/plan` 或後續命令。 |

## 📚 核心理念

規範驅動開發是一個強調以下方面的結構化過程：

- **意圖驅動開發**，規範在「如何」之前定義「什麼」
- **豐富的規範建立**，使用護欄和組織原則
- **多步精煉**，而不是從提示一次性生成程式碼
- **高度依賴**高階AI模型能力進行規範解釋

## 🌟 開發階段

| 階段 | 重點 | 關鍵活動 |
|-------|-------|----------------|
| **0到1開發**（「新建專案」） | 從頭生成 | <ul><li>從高階需求開始</li><li>生成規範</li><li>規劃實施步驟</li><li>建置生產就緒的應用程式</li></ul> |
| **創意探索** | 並行實作 | <ul><li>探索多樣化的解決方案</li><li>支援多種技術堆疊和架構</li><li>實驗UX模式</li></ul> |
| **迭代增強**（「現有專案改造」） | 現有專案現代化 | <ul><li>迭代新增功能</li><li>現代化遺留系統</li><li>適應流程</li></ul> |

## 🎯 實驗目標

我們的研究和實驗專注於：

### 技術獨立性

- 使用多樣化的技術堆疊建立應用程式
- 驗證規範驅動開發是一個不依賴於特定技術、程式語言或框架的過程

### 企業約束

- 展示關鍵任務應用程式開發
- 融入組織約束（雲端提供商、技術堆疊、工程實踐）
- 支援企業設計系統和合規要求

### 以使用者為中心的開發

- 為不同使用者群體和偏好建置應用程式
- 支援各種開發方法（從氛圍編碼到AI原生開發）

### 創意和迭代過程

- 驗證並行實作探索的概念
- 提供強大的迭代功能開發工作流程
- 擴展流程以處理升級和現代化任務

## 🔧 前置要求

- **Linux/macOS**（或Windows上的WSL2）
- AI編碼代理：[Claude Code](https://www.anthropic.com/claude-code)、[GitHub Copilot](https://code.visualstudio.com/) 或 [Gemini CLI](https://github.com/google-gemini/gemini-cli)
- [uv](https://docs.astral.sh/uv/) 用於套件管理
- [Python 3.11+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

## 📖 了解更多

- **[完整的規範驅動開發方法論](./spec-driven.md)** - 深入了解完整流程
- **[詳細演練](#-詳細流程)** - 分步實施指南

---

## 📋 詳細流程

<details>
<summary>點擊展開詳細的分步演練</summary>

您可以使用Specify TW CLI來引導您的專案，這將在您的環境中引入所需的工件。執行：

```bash
specify-tw init <project_name>
```

或在目前目錄初始化：

```bash
specify-tw init .
# 或使用 --here 標誌
specify-tw init --here
# 跳過確認當目錄已有檔案時
specify-tw init . --force
# 或
specify-tw init --here --force
```

![Specify TW CLI在終端機中引導新專案](./media/specify_cli.gif)

系統會提示您選擇正在使用的AI代理。您也可以直接在終端機中主動指定：

```bash
specify-tw init <project_name> --ai claude
specify-tw init <project_name> --ai gemini
specify-tw init <project_name> --ai copilot
specify-tw init <project_name> --ai cursor
specify-tw init <project_name> --ai qwen
specify-tw init <project_name> --ai opencode
specify-tw init <project_name> --ai codex
specify-tw init <project_name> --ai windsurf
specify-tw init <project_name> --ai kilocode
specify-tw init <project_name> --ai auggie
specify-tw init <project_name> --ai roo
# 或在目前目錄：
specify-tw init --here --ai claude
specify-tw init --here --ai codex
# 強制合併到非空的目前目錄
specify-tw init --here --force --ai claude
```

CLI會檢查您是否安裝了Claude Code、Gemini CLI、Cursor CLI、Qwen CLI、opencode或Codex CLI。如果您沒有安裝，或者您希望在不檢查正確工具的情況下獲取模板，請在命令中使用 `--ignore-agent-tools`：

```bash
specify-tw init <project_name> --ai claude --ignore-agent-tools
```

### **步驟1：** 建立專案原則

轉到專案資料夾並執行您的AI代理。在我們的範例中，我們使用 `claude`。

![引導Claude Code環境](./media/bootstrap-claude-code.gif)

如果您看到 `/constitution`、`/specify`、`/plan`、`/tasks` 和 `/implement` 命令可用，就說明配置正確。

第一步應該是使用 `/constitution` 命令建立專案的指導原則。這有助於確保在所有後續開發階段中做出一致的決策：

```text
/constitution 建立專注於程式碼品質、測試標準、使用者體驗一致性和效能要求的原則。包括這些原則應如何指導技術決策和實施選擇的治理。
```

此步驟會建立或更新 `.specify/memory/constitution.md` 檔案，其中包含專案的基礎指南，AI代理將在規範、規劃和實施階段參考這些指南。

>[!IMPORTANT]
>盡可能明確地說明您要建置的_什麼_和_為什麼_。**此時不要關注技術堆疊**。

範例提示：

```text
開發Taskify，一個團隊生產力平台。它應該允許使用者建立專案、新增團隊成員、
分配任務、評論並以看板風格在板之間移動任務。在此功能的初始階段，
我們稱之為「建立Taskify」，我們將有多個使用者，但使用者將提前預定義。
我想要兩個不同類別的五個使用者，一個產品經理和四個工程師。讓我們建立三個
不同的範例專案。讓我們為每個任務的狀態使用標準的看板列，如「待辦」、
「進行中」、「審核中」和「已完成」。此應用程式將沒有登入，因為這只是
確保我們基本功能設定的第一次測試。對於UI中的任務卡片，
您應該能夠在看板工作板的不同列之間變更任務的目前狀態。
您應該能夠為特定卡片留下無限數量的評論。您應該能夠從該任務
卡片中分配一個有效使用者。當您首次啟動Taskify時，它會給您一個五個使用者的清單供您選擇。
不需要密碼。當您點擊使用者時，您進入主視圖，顯示專案清單。
當您點擊專案時，您會打開該專案的看板。您將看到列。
您將能夠在不同列之間來回拖放卡片。您將看到分配給您的任何卡片，
即目前登入使用者，與其他卡片顏色不同，以便您快速看到您的卡片。
您可以編輯您所做的任何評論，但不能編輯其他人所做的評論。您可以
刪除您所做的任何評論，但不能刪除其他人所做的評論。
```

輸入此提示後，您應該看到Claude Code啟動規劃和規範起草過程。Claude Code還將觸發一些內建指令碼來設定儲存庫。

完成此步驟後，您應該有一個新建立的分支（例如，`001-create-taskify`），以及 `specs/001-create-taskify` 目錄中的新規範。

生成的規範應包含一組使用者故事和功能需求，如模板中所定義。

在此階段，您的專案資料夾內容應類似於以下內容：

```text
└── .specify
    ├── memory
    │	 └── constitution.md
    ├── scripts
    │	 ├── check-task-prerequisites.sh
    │	 ├── common.sh
    │	 ├── create-new-feature.sh
    │	 ├── get-feature-paths.sh
    │	 ├── setup-plan.sh
    │	 └── update-claude-md.sh
    ├── specs
    │	 └── 001-create-taskify
    │	     └── spec.md
    └── templates
        ├── CLAUDE-template.md
        ├── plan-template.md
        ├── spec-template.md
        └── tasks-template.md
```

### **步驟2：** 建立專案規範

有了專案原則後，您現在可以建立功能規範。使用 `/specify` 命令，然後為您想要開發的專案提供具體需求。

```text
對於您建立的每個範例專案或專案，每個專案應該有5到15個之間的可變數量任務，
隨機分布到不同的完成狀態。確保每個完成階段至少有一個任務。
```

您還應該要求Claude Code驗證**審核和驗收清單**，勾選驗證/通過要求的項目，未通過的項目保持未勾選狀態。可以使用以下提示：

```text
閱讀審核和驗收清單，如果功能規範符合標準，請勾選清單中的每個項目。如果不符合，請留空。
```

重要的是，要將與Claude Code的互動作為澄清和圍繞規範提問的機會——**不要將其第一次嘗試視為最終版本**。

### **步驟3：** 功能規範澄清（計畫前必需）

建立了基線規範後，您可以繼續澄清在第一次嘗試中未正確捕獲的任何需求。

您應該在建立技術計畫之前執行結構化澄清工作流程，以減少下游的返工。

首選順序：
1. 使用 `/clarify`（結構化）- 順序的、基於覆蓋率的提問，將答案記錄在澄清部分。
2. 如果仍然感覺模糊，可以選擇性地進行臨時自由形式精煉。

如果您想跳過澄清（例如，技術驗證或探索性原型），請明確說明，這樣代理就不會因缺少澄清而阻塞。

範例自由形式精煉提示（如果需要，在 `/clarify` 之後）：

```text
我們將使用.NET Aspire生成這個，使用Postgres作為資料庫。前端應該使用
Blazor伺服器與拖放任務板、即時更新。應該建立一個REST API，包含專案API、
任務API和通知API。
```

此步驟的輸出將包括許多實施細節文件，您的目錄樹類似於：

```text
.
├── CLAUDE.md
├── memory
│	 └── constitution.md
├── scripts
│	 ├── check-task-prerequisites.sh
│	 ├── common.sh
│	 ├── create-new-feature.sh
│	 ├── get-feature-paths.sh
│	 ├── setup-plan.sh
│	 └── update-claude-md.sh
├── specs
│	 └── 001-create-taskify
│	     ├── contracts
│	     │	 ├── api-spec.json
│	     │	 └── signalr-spec.md
│	     ├── data-model.md
│	     ├── plan.md
│	     ├── quickstart.md
│	     ├── research.md
│	     └── spec.md
└── templates
    ├── CLAUDE-template.md
    ├── plan-template.md
    ├── spec-template.md
    └── tasks-template.md
```

檢查 `research.md` 文件，確保根據您的說明使用了正確的技術堆疊。如果任何元件突出顯示，您可以要求Claude Code完善它，甚至讓它檢查您想要使用的平台/框架的本地安裝版本（例如，.NET）。

此外，如果您選擇的技術堆疊是快速變化的（例如，.NET Aspire、JS框架），您可能想要要求Claude Code研究有關所選技術堆疊的詳細資訊，使用這樣的提示：

```text
我希望您檢視實施計畫和實施細節，尋找可能從額外研究中受益的領域，
因為.NET Aspire是一個快速變化的函式庫。對於您識別的需要進一步研究的那些領域，
我希望您使用有關我們將在Taskify應用程式中使用的特定版本的額外詳細資訊更新研究文件，
並啟動並行研究任務，使用網路研究澄清任何細節。
```

在此過程中，您可能會發現Claude Code卡在研究錯誤的內容——您可以使用這樣的提示幫助它朝著正確的方向推進：

```text
我認為我們需要將其分解為一系列步驟。首先，識別您在實施期間需要做的不確定
或從進一步研究中受益的任務清單。寫下這些任務的清單。然後對於這些任務中的每一個，
我希望您啟動一個單獨的研究任務，這樣最終結果是我們並行研究所有這些非常具體的任務。
我看到您所做的是看起來您在研究.NET Aspire一般情況，我認為這對我們不會有太大幫助。
那太沒有針對性的研究了。研究需要幫助您解決特定的針對性問題。
```

>[!NOTE]
>Claude Code可能過於急切，新增您沒有要求的元件。要求它澄清變更的理由和來源。

### **步驟4：** 生成計畫

您現在可以具體說明技術堆疊和其他技術要求。您可以使用專案模板中內建的 `/plan` 命令，使用這樣的提示：

```text
現在我希望您去審核實施計畫和實施細節檔案。
帶著確定是否存在從閱讀中可以明顯看出的您需要做的一系列任務的眼光來閱讀。
因為我不確定這裡是否足夠。例如，當我檢視核心實施時，參考實施細節中的適當位置
會很有用，以便在它執行核心實施或精煉中的每個步驟時可以找到資訊。
```

這有助於完善實施計畫，並幫助您避免Claude Code在其規劃週期中遺漏的潛在盲點。一旦初始精煉完成，在您可以進入實施之前，要求Claude Code再次檢查清單。

您也可以要求Claude Code（如果您安裝了[GitHub CLI](https://docs.github.com/en/github-cli/github-cli)）繼續從您目前的分支向 `main` 建立一個詳細描述的pull request，以確保工作得到正確追蹤。

>[!NOTE]
>在讓代理實施之前，還值得提示Claude Code交叉檢查細節，看看是否有任何過度設計的部分（記住——它可能過於急切）。如果存在過度設計的元件或決策，您可以要求Claude Code解決它們。確保Claude Code遵循[專案章程](base/memory/constitution.md)作為建立計畫時必須遵守的基礎。

### **步驟5：** 讓Claude Code驗證計畫

有了計畫後，您應該讓Claude Code檢查它，確保沒有遺漏的部分。您可以使用這樣的提示：

>[!IMPORTANT]
>Claude Code將執行本地CLI命令（如 `dotnet`）——確保您在機器上安裝了它們。

### **步驟6：** 實施

準備就緒後，使用 `/implement` 命令執行您的實施計畫：

```text
/implement
```

`/implement` 命令將：
- 驗證所有先決條件都已就緒（章程、規範、計畫和任務）
- 解析 `tasks.md` 中的任務分解
- 按正確順序執行任務，尊重相依性和並行執行標記
- 遵循任務計畫中定義的 TDD 方法
- 提供進度更新並適當處理錯誤

>[!IMPORTANT]
>AI代理將執行本地CLI命令（如 `dotnet`、`npm` 等）- 確保您在機器上安裝了所需的工具。

實施完成後，測試應用程式並解決任何在CLI日誌中可能不可見的執行階段錯誤（例如，瀏覽器主控台錯誤）。您可以將此類錯誤複製貼上回AI代理以進行解決。

</details>

---

## 🔍 故障排除

### Linux上的Git憑證管理器

如果您在Linux上遇到Git身份驗證問題，可以安裝Git憑證管理器：

```bash
#!/usr/bin/env bash
set -e
echo "正在下載Git憑證管理器v2.6.1..."
wget https://github.com/git-ecosystem/git-credential-manager/releases/download/v2.6.1/gcm-linux_amd64.2.6.1.deb
echo "正在安裝Git憑證管理器..."
sudo dpkg -i gcm-linux_amd64.2.6.1.deb
echo "正在配置Git使用GCM..."
git config --global credential.helper manager
echo "正在清理..."
rm gcm-linux_amd64.2.6.1.deb
```

## 👥 維護者

- Den Delimarsky ([@localden](https://github.com/localden))
- John Lam ([@jflam](https://github.com/jflam))

## 💬 支援

如需支援，請開啟[GitHub issue](https://github.com/Minidoracat/spec-kit-tw/issues/new)。我們歡迎錯誤報告、功能請求和關於使用規範驅動開發的問題。

## 🙏 致謝

這個專案深受[John Lam](https://github.com/jflam)的工作和研究的影響並基於其成果。

## 📄 授權

本專案根據MIT開源授權的條款授權。請參閱[LICENSE](./LICENSE)檔案了解完整條款。
