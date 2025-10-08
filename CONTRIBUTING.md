## 為 Spec Kit 做貢獻

你好！我們很高興你願意為 Spec Kit 做出貢獻。本專案的貢獻內容根據[專案開源許可證](LICENSE)向公眾發布。

請注意，本專案隨[貢獻者行為準則](CODE_OF_CONDUCT.md)一起發布。參與本專案即表示你同意遵守其條款。

## 執行和測試程式碼的先決條件

這些是在提交拉取請求（PR）過程中，能夠在本地測試你的變更所需的一次性安裝。

1. 安裝 [Python 3.11+](https://www.python.org/downloads/)
1. 安裝 [uv](https://docs.astral.sh/uv/) 用於套件管理
1. 安裝 [Git](https://git-scm.com/downloads)
1. 準備一個 AI 編碼代理：推薦使用 [Claude Code](https://www.anthropic.com/claude-code)、[GitHub Copilot](https://code.visualstudio.com/) 或 [Gemini CLI](https://github.com/google-gemini/gemini-cli)，我們也在努力添加對其他代理的支援。

## 提交拉取請求

>[!NOTE]
>如果你的拉取請求引入了對 CLI 或儲存庫其他部分工作產生實質性影響的大型變更（例如，引入新模板、參數或其他重大變更），請確保該變更已**經過專案維護者的討論和同意**。未經事先對話和同意的大型變更拉取請求將被關閉。

1. Fork 並複製儲存庫
1. 配置和安裝相依套件：`uv sync`
1. 確保 CLI 在你的機器上正常工作：`uv run specify-tw --help`
1. 建立新分支：`git checkout -b my-branch-name`
1. 進行變更，新增測試，並確保一切仍然正常工作
1. 如果相關，使用範例專案測試 CLI 功能
1. 推送到你的 fork 並提交拉取請求
1. 等待你的拉取請求被審查和合併。

以下是一些可以增加你的拉取請求被接受機率的方法：

- 遵循專案的編碼規範。
- 為新功能編寫測試。
- 如果你的變更影響使用者可見的功能，請更新文件（`README.md`、`spec-driven.md`）。
- 盡可能保持你的變更專注。如果你想進行多個相互不依賴的變更，考慮將它們作為單獨的拉取請求提交。
- 編寫[良好的提交訊息](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)。
- 使用 Spec-Driven Development 工作流程測試你的變更以確保相容性。

## 開發工作流程

在處理 spec-kit 時：

1. 在你選擇的編碼代理中使用 `specify-tw` CLI 命令（`/specify`、`/plan`、`/tasks`）測試變更
2. 驗證 `templates/` 目錄中的模板是否正常工作
3. 測試 `scripts/` 目錄中的腳本功能
4. 如果進行了重大的流程變更，確保更新記憶檔案（`memory/constitution.md`）

## 資源

- [Spec-Driven Development 方法論](./spec-driven.md)
- [如何為開源做貢獻](https://opensource.guide/how-to-contribute/)
- [使用拉取請求](https://help.github.com/articles/about-pull-requests/)
- [GitHub 說明](https://help.github.com)
