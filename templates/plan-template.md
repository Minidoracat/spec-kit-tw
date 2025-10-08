---
description: "功能開發的實施計畫模板"
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

# 實施計畫：[FEATURE]

**分支**: `[###-feature-name]` | **日期**: [DATE] | **規格**: [link]
**輸入**: 來自 `/specs/[###-feature-name]/spec.md` 的功能規格

**注意**: 此模板由 `/speckit.plan` 命令填寫。請參閱 `.specify/templates/commands/plan.md` 以了解執行工作流程。

## 摘要

[從功能規格中擷取：主要需求 + 來自研究的技術方法]

## 技術背景

<!--
  需要的操作：將此區塊的內容替換為專案的技術細節。
  此處呈現的結構僅供參考，以指導迭代過程。
-->

**語言/版本**: [例如，Python 3.11, Swift 5.9, Rust 1.75 或需要澄清]
**主要依賴**: [例如，FastAPI, UIKit, LLVM 或需要澄清]
**儲存**: [如果適用，例如，PostgreSQL, CoreData, files 或不適用]
**測試**: [例如，pytest, XCTest, cargo test 或需要澄清]
**目標平台**: [例如，Linux 伺服器，iOS 15+, WASM 或需要澄清]
**專案類型**: [單一/web/行動 - 決定原始碼結構]
**效能目標**: [特定領域，例如 1000 req/s, 10k lines/sec, 60 fps 或需要澄清]
**限制**: [特定領域，例如 <200ms p95, <100MB memory, offline-capable 或需要澄清]
**規模/範圍**: [特定領域，例如 10k users, 1M LOC, 50 screens 或需要澄清]

## 章程檢查

*關卡：必須在階段 0 研究之前通過。在階段 1 設計後重新檢查。*

[根據章程檔案確定的關卡]

## 專案結構

### 文件（此功能）

```
specs/[###-feature]/
├── plan.md              # 此檔案（/speckit.plan 命令輸出）
├── research.md          # 階段 0 輸出（/speckit.plan 命令）
├── data-model.md        # 階段 1 輸出（/speckit.plan 命令）
├── quickstart.md        # 階段 1 輸出（/speckit.plan 命令）
├── contracts/           # 階段 1 輸出（/speckit.plan 命令）
└── tasks.md             # 階段 2 輸出（/speckit.tasks 命令 - 不由 /speckit.plan 建立）
```

### 原始碼（儲存庫根目錄）
<!--
  需要的操作：將下方的佔位符樹狀結構替換為此功能的具體佈局。
  刪除未使用的選項，並使用真實路徑擴展所選結構（例如，apps/admin, packages/something）。
  交付的計畫不得包含選項標籤。
-->

```
# [若未使用則移除] 選項 1：單一專案（預設）
src/
├── models/
├── services/
├── cli/
└── lib/

tests/
├── contract/
├── integration/
└── unit/

# [若未使用則移除] 選項 2：Web 應用程式（當偵測到 "frontend" + "backend" 時）
backend/
├── src/
│   ├── models/
│   ├── services/
│   └── api/
└── tests/

frontend/
├── src/
│   ├── components/
│   ├── pages/
│   └── services/
└── tests/

# [若未使用則移除] 選項 3：行動應用 + API（當偵測到 "iOS/Android" 時）
api/
└── [與上方的 backend 相同]

ios/ 或 android/
└── [平台特定結構：功能模組、UI 流程、平台測試]
```

**結構決策**: [記錄所選結構並參考上方擷取的實際目錄]

## 複雜度追蹤

*僅在章程檢查有必須證明合理性的違規時填寫*

| 違規 | 需要原因 | 拒絕的更簡單替代方案 |
|------|----------|-------------------|
| [例如，第 4 個專案] | [目前需求] | [為何 3 個專案不足] |
| [例如，Repository 模式] | [特定問題] | [為何直接資料庫存取不足] |

## 階段 0：大綱與研究
1. **從上方的技術背景中擷取未知內容**：
   - 對於每個需要澄清的內容 → 研究任務
   - 對於每個依賴 → 最佳實踐任務
   - 對於每個整合 → 模式任務

2. **產生並派遣研究代理**：
   ```
   對於技術背景中的每個未知內容：
     任務："為 {feature context} 研究 {unknown}"
   對於每個技術選擇：
     任務："在 {domain} 中找到 {tech} 的最佳實踐"
   ```

3. **在 `research.md` 中整合發現**，使用格式：
   - 決策：[選擇了什麼]
   - 理由：[為什麼選擇]
   - 考慮的替代方案：[還評估了什麼]

**輸出**: research.md，所有需要澄清的內容都已解決

## 階段 1：設計與合約
*前提條件：research.md 完成*

1. **從功能規格中擷取實體** → `data-model.md`：
   - 實體名稱、欄位、關係
   - 來自需求的驗證規則
   - 狀態轉換（如果適用）

2. **從功能需求產生 API 合約**：
   - 對於每個使用者操作 → 端點
   - 使用標準 REST/GraphQL 模式
   - 輸出 OpenAPI/GraphQL 模式到 `/contracts/`

3. **代理情境更新**：
   - 執行 `{AGENT_SCRIPT}`
   - 這些腳本會偵測正在使用的 AI 代理
   - 更新適當的代理特定情境檔案
   - 僅新增當前計畫中的新技術
   - 保留標記之間的手動新增內容

4. **從合約產生合約測試**：
   - 每個端點一個測試檔案
   - 斷言請求/回應模式
   - 測試必須失敗（尚未實作）

5. **從使用者故事中擷取測試場景**：
   - 每個故事 → 整合測試場景
   - 快速入門測試 = 故事驗證步驟

**輸出**: data-model.md, /contracts/*, 失敗的測試, quickstart.md, 代理特定檔案

## 階段 2：任務規劃方法
*本節描述 /speckit.tasks 命令將做什麼 - 不要在 /speckit.plan 期間執行*

**任務產生策略**：
- 載入 `.specify/templates/tasks-template.md` 作為基礎
- 從階段 1 設計文件產生任務（合約、資料模型、快速入門）
- 每個合約 → 合約測試任務 [P]
- 每個實體 → 模型建立任務 [P]
- 每個使用者故事 → 整合測試任務
- 使測試通過的實作任務

**排序策略**：
- TDD 順序：測試在實作之前
- 依賴順序：模型在服務之前，服務在 UI 之前
- 標記 [P] 用於並行執行（獨立檔案）

**預計輸出**: tasks.md 中 25-30 個編號的、有序的任務

**重要說明**: 此階段由 /speckit.tasks 命令執行，而不是由 /speckit.plan 執行

## 階段 3+：未來實作
*這些階段超出了 /speckit.plan 命令的範圍*

**階段 3**: 任務執行（/speckit.tasks 命令建立 tasks.md）
**階段 4**: 實作（按照專案章程原則執行 tasks.md）
**階段 5**: 驗證（執行測試，執行 quickstart.md，效能驗證）

## 進度追蹤
*此檢查清單在執行流程期間更新*

**階段狀態**：
- [ ] 階段 0：研究完成（/speckit.plan 命令）
- [ ] 階段 1：設計完成（/speckit.plan 命令）
- [ ] 階段 2：任務規劃完成（/speckit.plan 命令 - 僅描述方法）
- [ ] 階段 3：任務產生（/speckit.tasks 命令）
- [ ] 階段 4：實作完成
- [ ] 階段 5：驗證通過

**關卡狀態**：
- [ ] 初始章程檢查：通過
- [ ] 設計後章程檢查：通過
- [ ] 所有需要澄清的內容已解決
- [ ] 複雜性偏差已記錄

---
*基於專案章程 v2.1.1 - 參見 `/memory/constitution.md`*
