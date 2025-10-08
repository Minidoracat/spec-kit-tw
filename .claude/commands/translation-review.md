---
name: translation-review
description: "Review and fix translation quality between spec-kit original and Chinese localized version"
---

使用者輸入可以直接由代理提供或作為命令引數提供給您 - 您**必須**考慮它（如果不為空）。

使用者輸入：

$ARGUMENTS

目標：系統性地review原專案spec-kit與中文版之間的翻譯質量，識別並修復所有翻譯錯誤、術語不一致和功能邏輯問題。

執行步驟：

1. 驗證環境準備：
   - 確認spec-kit目錄存在且包含原版檔案
   - 確認templates/和templates/commands/目錄結構完整
   - 確認memory/目錄存在

2. 目錄結構對比分析：
   - 對比原專案spec-kit中templates和templates/commands目錄結構
   - 對比當前專案templates目錄與原專案的差異
   - 對比當前專案memory目錄與原專案的差異

3. 翻譯質量系統性review：
   - **templates目錄核心檔案**：
     * agent-file-template.md - AI助手檔案模板
     * spec-template.md - 功能規範模板
     * plan-template.md - 實施計劃模板
     * tasks-template.md - 任務生成模板

   - **templates/commands目錄所有檔案**：
     * analyze.md - 分析命令
     * clarify.md - 澄清命令
     * constitution.md - 章程命令
     * implement.md - 實施命令
     * plan.md - 計劃命令
     * specify.md - 規範命令
     * tasks.md - 任務命令

   - **memory目錄**：
     * constitution.md - 專案章程模板
     
   - 上述目錄中新出現的一切沒有提到的檔案也需要review

4. 輸出結構化報告等待人類稽覈：

行為規則：
- 必須對比原版spec-kit中的對應檔案
- 使用Task工具並行對比
- 所有檔案翻譯後，必須確保和原版表達是一樣的語義，不能新增或減少內容
- 所有的路徑，不需要翻譯，都以原版為準
- 確保修復後的功能與原版完全一致
- 優先修復功能邏輯錯誤
- 保持技術術語的準確性
- 輸出詳細的修復報告
- 所有沒有問題，請直接告訴使用者
