# 变更日志

本项目的重要变更将记录在此文件中。

格式基于[Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
并且本项目遵循[语义化版本](https://semver.org/lang/zh-CN/)。

## [未发布]

### 新增
- 初始中文版本发布

### 变更
- 将所有文档从英文翻译为中文
- 更新命令引用从`specify`改为`specify-cn`

### 修复
- 修复文档中的链接引用

## [1.0.0] - 2024-09-16

### 新增
- 初始版本发布

## [1.0.54] - 2025-09-28

### 同步原版
- 同步原版 [v0.0.54](https://github.com/github/spec-kit/releases/tag/v0.0.54)
- 对应原版提交：`1c0e7d14d5d5388fbb98b7856ce9f486cc273997`

### 中文本地化更新
- 更新 README.md 中的版本信息和原版对应关系
- 更新 `src/specify_cli/__init__.py` 文件，从原版 spec-kit 项目复制并完全本地化
- 品牌标识更新：包名 `specify-cn-cli`，命令名 `specify-cn`，GitHub 仓库 `Linfee/spec-kit-cn`
- 用户界面完全中文化：所有错误消息、状态提示、帮助文档、操作指导均已翻译为中文
- 功能完整性验证：核心 CLI 功能与原版完全对等，11 种 AI 助手支持完全一致

### 技术架构同步
- 核心代码架构：所有类和函数名称、方法签名、算法逻辑与原版保持一致
- 依赖管理：typer、rich、httpx 等依赖库版本与原版同步
- 构建配置：hatchling 构建系统配置保持同步
- AI 助手支持：Claude Code、Gemini CLI、GitHub Copilot、Cursor、Qwen Code 等 11 种助手完全支持

### 已知问题
- 无
- Spec-Driven Development方法论完整实现
- CLI工具支持
- 模板系统
- 文档生成功能
