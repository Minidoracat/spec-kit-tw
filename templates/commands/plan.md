---
description: 使用計劃範本執行實作規劃工作流程以生成設計工件。
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
agent_scripts:
  sh: scripts/bash/update-agent-context.sh __AGENT__
  ps: scripts/powershell/update-agent-context.ps1 -AgentType __AGENT__
---

## 使用者輸入

```text
$ARGUMENTS
```

在繼續之前，你**必須**考慮使用者輸入（如果不為空）。

## 大綱

1. **設定**：從儲存庫根目錄執行 `{SCRIPT}` 並解析 JSON 以取得 FEATURE_SPEC、IMPL_PLAN、SPECS_DIR、BRANCH。對於參數中包含單引號的情況（如 "I'm Groot"），請使用轉義語法：例如 'I'\''m Groot'（或者如果可能，使用雙引號："I'm Groot"）。

2. **載入上下文**：讀取 FEATURE_SPEC 和 `.specify/memory/constitution.md`。載入 IMPL_PLAN 範本（已複製）。

3. **執行計劃工作流程**：遵循 IMPL_PLAN 範本中的結構來：
   - 填寫技術上下文（將未知標記為「NEEDS CLARIFICATION」）
   - 從章程填寫章程檢查段落
   - 評估門控（如果違規無法證明則錯誤）
   - 階段 0：生成 research.md（解決所有 NEEDS CLARIFICATION）
   - 階段 1：生成 data-model.md、contracts/、quickstart.md
   - 階段 1：執行代理腳本更新代理上下文
   - 重新評估設計後的章程檢查

4. **停止並報告**：命令在階段 2 規劃後結束。報告分支、IMPL_PLAN 路徑和生成的工件。

## 階段

### 階段 0：大綱和研究

1. **從上述技術上下文中提取未知項**：
   - 對於每個 NEEDS CLARIFICATION → 研究任務
   - 對於每個依賴項 → 最佳實踐任務
   - 對於每個整合 → 模式任務

2. **生成並派遣研究代理**：
   ```
   對於技術上下文中的每個未知項：
     任務：「為 {功能上下文} 研究 {未知項}」
   對於每個技術選擇：
     任務：「在 {領域} 中尋找 {技術} 的最佳實踐」
   ```

3. **整合發現**到 `research.md` 中，使用格式：
   - 決策：[選擇了什麼]
   - 理由：[為什麼選擇]
   - 考慮的替代方案：[還評估了什麼]

**輸出**：包含所有已解決 NEEDS CLARIFICATION 的 research.md

### 階段 1：設計和合約

**先決條件：** `research.md` 完成

1. **從功能規格中提取實體** → `data-model.md`：
   - 實體名稱、欄位、關係
   - 來自需求的驗證規則
   - 如果適用，狀態轉換

2. **從功能需求生成 API 合約**：
   - 對於每個使用者動作 → 端點
   - 使用標準 REST/GraphQL 模式
   - 將 OpenAPI/GraphQL 架構輸出到 `/contracts/`

3. **代理上下文更新**：
   - 執行 `{AGENT_SCRIPT}`
   - 這些腳本檢測正在使用哪個 AI 代理
   - 更新適當的代理特定上下文檔案
   - 僅添加當前計劃中的新技術
   - 在標記之間保留手動添加

**輸出**：data-model.md、/contracts/*、quickstart.md、代理特定檔案

## 關鍵規則

- 使用絕對路徑
- 門控失敗或未解決的釐清時錯誤
