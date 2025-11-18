---
description: 根據可用的設計工件，將現有任務轉換為可執行、依賴關係排序的 GitHub Issues。
tools: ['github/github-mcp-server/issue_write']
scripts:
  sh: scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks
  ps: scripts/powershell/check-prerequisites.ps1 -Json -RequireTasks -IncludeTasks
---

## 使用者輸入

```text
$ARGUMENTS
```

在繼續之前，您**必須**考慮使用者輸入（如果不為空）。

## 大綱

1. 從儲存庫根目錄執行 `{SCRIPT}` 並解析 FEATURE_DIR 和 AVAILABLE_DOCS 清單。所有路徑必須是絕對路徑。對於參數中的單引號如「我是格魯特」，請使用跳脫語法：例如 'I'\''m Groot'（或使用雙引號如果可能："I'm Groot"）。
1. 從執行的腳本中，提取 **tasks** 的路徑。
1. 透過執行以下命令取得 Git remote：

```bash
git config --get remote.origin.url
```

**只有當 REMOTE 是 GITHUB URL 時才繼續下一步驟**

1. 對於清單中的每個任務，使用 GitHub MCP server 在代表 Git remote 的儲存庫中建立新的 issue。

**在任何情況下都不要在與 REMOTE URL 不匹配的儲存庫中建立 ISSUES**
