## 为 Spec Kit 做贡献

你好！我们很高兴你愿意为 Spec Kit 做出贡献。本项目的贡献内容根据[项目开源许可证](LICENSE)向公众发布。

请注意，本项目随[贡献者行为准则](CODE_OF_CONDUCT.md)一起发布。参与本项目即表示你同意遵守其条款。

## 运行和测试代码的先决条件

这些是在提交拉取请求（PR）过程中，能够在本地测试你的更改所需的一次性安装。

1. 安装 [Python 3.11+](https://www.python.org/downloads/)
1. 安装 [uv](https://docs.astral.sh/uv/) 用于包管理
1. 安装 [Git](https://git-scm.com/downloads)
1. 准备一个 AI 编码代理：推荐使用 [Claude Code](https://www.anthropic.com/claude-code)、[GitHub Copilot](https://code.visualstudio.com/) 或 [Gemini CLI](https://github.com/google-gemini/gemini-cli)，我们也在努力添加对其他代理的支持。

## 提交拉取请求

>[!NOTE]
>如果你的拉取请求引入了对 CLI 或仓库其他部分工作产生实质性影响的大型更改（例如，引入新模板、参数或其他重大更改），请确保该更改已**经过项目维护者的讨论和同意**。未经事先对话和同意的大型更改拉取请求将被关闭。

1. Fork 并克隆仓库
1. 配置和安装依赖项：`uv sync`
1. 确保 CLI 在你的机器上正常工作：`uv run specify-cn --help`
1. 创建新分支：`git checkout -b my-branch-name`
1. 进行更改，添加测试，并确保一切仍然正常工作
1. 如果相关，使用示例项目测试 CLI 功能
1. 推送到你的 fork 并提交拉取请求
1. 等待你的拉取请求被审查和合并。

以下是一些可以增加你的拉取请求被接受几率的方法：

- 遵循项目的编码规范。
- 为新功能编写测试。
- 如果你的更改影响用户可见的功能，请更新文档（`README.md`、`spec-driven.md`）。
- 尽可能保持你的更改专注。如果你想进行多个相互不依赖的更改，考虑将它们作为单独的拉取请求提交。
- 编写[良好的提交消息](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)。
- 使用 Spec-Driven Development 工作流测试你的更改以确保兼容性。

## 开发工作流

在处理 spec-kit 时：

1. 在你选择的编码代理中使用 `specify-cn` CLI 命令（`/specify`、`/plan`、`/tasks`）测试更改
2. 验证 `templates/` 目录中的模板是否正常工作
3. 测试 `scripts/` 目录中的脚本功能
4. 如果进行了重大的流程更改，确保更新内存文件（`memory/constitution.md`）

## 资源

- [Spec-Driven Development 方法论](./spec-driven.md)
- [如何为开源做贡献](https://opensource.guide/how-to-contribute/)
- [使用拉取请求](https://help.github.com/articles/about-pull-requests/)
- [GitHub 帮助](https://help.github.com)