---
description: 透過處理和執行 tasks.md 中定義的所有任務來執行實作計劃
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## 使用者輸入

```text
$ARGUMENTS
```

在繼續之前，你**必須**考慮使用者輸入（如果不為空）。

## 大綱

1. 從儲存庫根目錄執行 `{SCRIPT}` 並解析 FEATURE_DIR 和 AVAILABLE_DOCS 清單。所有路徑必須是絕對路徑。對於參數中包含單引號的情況（如 "I'm Groot"），請使用轉義語法：例如 'I'\''m Groot'（或者如果可能，使用雙引號："I'm Groot"）。

2. **檢查檢查清單狀態**（如果存在 FEATURE_DIR/checklists/）：
   - 掃描 checklists/ 目錄中的所有檢查清單檔案
   - 對於每個檢查清單，計算：
     * 總項目：所有符合 `- [ ]` 或 `- [X]` 或 `- [x]` 的行
     * 已完成項目：符合 `- [X]` 或 `- [x]` 的行
     * 未完成項目：符合 `- [ ]` 的行
   - 建立狀態表格：
     ```
     | 檢查清單 | 總計 | 已完成 | 未完成 | 狀態 |
     |---------|------|--------|---------|------|
     | ux.md     | 12    | 12        | 0          | ✓ 通過 |
     | test.md   | 8     | 5         | 3          | ✗ 失敗 |
     | security.md | 6   | 6         | 0          | ✓ 通過 |
     ```
   - 計算整體狀態：
     * **通過**：所有檢查清單都有 0 個未完成項目
     * **失敗**：一個或多個檢查清單有未完成項目

   - **如果有任何檢查清單未完成**：
     * 顯示包含未完成項目計數的表格
     * **停止**並詢問：「某些檢查清單未完成。你是否要繼續實作？（是/否）」
     * 等待使用者回應後再繼續
     * 如果使用者說「否」或「等待」或「停止」，停止執行
     * 如果使用者說「是」或「繼續」或「進行」，進入步驟 3

   - **如果所有檢查清單都完成**：
     * 顯示表格顯示所有檢查清單通過
     * 自動進入步驟 3

3. 載入和分析實作上下文：
   - **必需**：讀取 tasks.md 以取得完整的任務清單和執行計劃
   - **必需**：讀取 plan.md 以取得技術堆疊、架構和檔案結構
   - **如果存在**：讀取 data-model.md 以取得實體和關係
   - **如果存在**：讀取 contracts/ 以取得 API 規格和測試需求
   - **如果存在**：讀取 research.md 以取得技術決策和約束
   - **如果存在**：讀取 quickstart.md 以取得整合情境

4. **專案設定驗證**：
   - **必需**：根據實際專案設定建立/驗證忽略檔案：

   **偵測與建立邏輯**：
   - 檢查以下命令是否成功以判斷儲存庫是否為 Git 儲存庫（如果是則建立/驗證 .gitignore）：

     ```sh
     git rev-parse --git-dir 2>/dev/null
     ```
   - 檢查 Dockerfile* 是否存在或 plan.md 中提到 Docker → 建立/驗證 .dockerignore
   - 檢查 .eslintrc* 或 eslint.config.* 是否存在 → 建立/驗證 .eslintignore
   - 檢查 .prettierrc* 是否存在 → 建立/驗證 .prettierignore
   - 檢查 .npmrc 或 package.json 是否存在 → 建立/驗證 .npmignore（如果發布套件）
   - 檢查 terraform 檔案 (*.tf) 是否存在 → 建立/驗證 .terraformignore
   - 檢查是否需要 .helmignore（helm charts 存在） → 建立/驗證 .helmignore

   **如果忽略檔案已存在**：驗證其包含必要模式，僅附加缺失的關鍵模式
   **如果忽略檔案不存在**：根據偵測到的技術建立完整的模式集

   **依技術堆疊的常見模式**（從 plan.md 技術堆疊）：
   - **Node.js/JavaScript**: `node_modules/`, `dist/`, `build/`, `*.log`, `.env*`
   - **Python**: `__pycache__/`, `*.pyc`, `.venv/`, `venv/`, `dist/`, `*.egg-info/`
   - **Java**: `target/`, `*.class`, `*.jar`, `.gradle/`, `build/`
   - **C#/.NET**: `bin/`, `obj/`, `*.user`, `*.suo`, `packages/`
   - **Go**: `*.exe`, `*.test`, `vendor/`, `*.out`
   - **通用**: `.DS_Store`, `Thumbs.db`, `*.tmp`, `*.swp`, `.vscode/`, `.idea/`

   **工具特定模式**：
   - **Docker**: `node_modules/`, `.git/`, `Dockerfile*`, `.dockerignore`, `*.log*`, `.env*`, `coverage/`
   - **ESLint**: `node_modules/`, `dist/`, `build/`, `coverage/`, `*.min.js`
   - **Prettier**: `node_modules/`, `dist/`, `build/`, `coverage/`, `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - **Terraform**: `.terraform/`, `*.tfstate*`, `*.tfvars`, `.terraform.lock.hcl`

5. 解析 tasks.md 結構並提取：
   - **任務階段**：設定、測試、核心、整合、完善
   - **任務依賴項**：順序與平行執行規則
   - **任務詳細資訊**：ID、描述、檔案路徑、平行標記 [P]
   - **執行流程**：順序和依賴需求

6. 按照任務計劃執行實作：
   - **階段性執行**：在進入下一階段之前完成每個階段
   - **尊重依賴項**：按順序執行順序任務，平行任務 [P] 可以一起執行
   - **遵循 TDD 方法**：在其對應的實作任務之前執行測試任務
   - **基於檔案的協調**：影響相同檔案的任務必須按順序執行
   - **驗證檢查點**：在繼續之前驗證每個階段的完成

7. 實作執行規則：
   - **首先設定**：初始化專案結構、依賴項、配置
   - **程式碼之前測試**：如果你需要為合約、實體和整合情境撰寫測試
   - **核心開發**：實作模型、服務、CLI 命令、端點
   - **整合工作**：資料庫連線、中介軟體、記錄、外部服務
   - **完善和驗證**：單元測試、效能最佳化、文件

8. 進度追蹤和錯誤處理：
   - 在每個完成的任務後報告進度
   - 如果任何非平行任務失敗則停止執行
   - 對於平行任務 [P]，繼續成功的任務，報告失敗的任務
   - 提供帶有調試上下文的清晰錯誤訊息
   - 如果實作無法進行，建議後續步驟
   - **重要** 對於已完成的任務，確保在任務檔案中將任務標記為 [X]。

9. 完成驗證：
   - 驗證所有必需任務已完成
   - 檢查已實作的功能與原始規格匹配
   - 驗證測試通過且覆蓋率滿足需求
   - 確認實作遵循技術計劃
   - 報告包含已完成工作摘要的最終狀態

注意：此命令假設 tasks.md 中存在完整的任務分解。如果任務不完整或缺失，建議首先執行 `/tasks` 重新生成任務清單。
