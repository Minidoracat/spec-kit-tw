# 版本历史记录

本文档记录了 Spec Kit CN 中文版本与原版 Spec Kit 的版本对应关系，以及每个版本的关键更新内容。

## 版本对应表

| 中文版本 | 发布日期 | 对应原版提交ID | 原版提交信息 | 关键更新 |
|-------------|-------------|----------------------|-------------------|-------------|
| **v0.0.4** | 2025-09-16 | `bfeb40cebc6f1d08cf055e19433967d3328a522c` | 合并 PR #124 - Claude 迁移安装程序兼容性修复 | 首个正式版本，完整中文本地化 |

## 详细版本信息

### v0.0.4 (当前版本)
**发布日期**: 2025年9月16日
**对应原版提交**: [bfeb40cebc6f1d08cf055e19433967d3328a522c](https://github.com/github/spec-kit/commit/bfeb40cebc6f1d08cf055e19433967d3328a522c)
**原版提交信息**: 合并 PR #124 - 修复Claude迁移安装程序兼容性问题

#### 主要特性
- ✅ 完整中文本地化（327个文档）
- ✅ 命令行工具更名为 `specify-cn`
- ✅ 包名更改为 `specify-cn-cli`
- ✅ 依赖管理现代化（使用uv）
- ✅ 完整的CI/CD工作流
- ✅ 所有自动化脚本
- ✅ 文档系统配置

#### 文档翻译统计
- README.md - 项目主文档
- spec-driven.md - 规范驱动开发核心理念
- 所有模板文件（spec/plan/tasks templates）
- 所有命令模板文件
- 维护文档（CONTRIBUTING, CODE_OF_CONDUCT, SUPPORT, SECURITY）
- 记忆系统文档（constitution）
- 安装与开发指南

## 版本维护策略

### 同步机制
- 每个中文版本都会明确标注对应的原版提交ID
- 建议每隔一个原版发布周期同步一次
- 重要的功能更新应及时同步

### 发布流程
1. 暂停原版同步，确定对应提交ID
2. 更新`VERSION_HISTORY.md`中的对应关系
3. 更新`README.md`中的提交ID链接
4. 检查所有安装命令是否指向正确仓库
5. 打包发布中文版本

## 与原版差异说明

| 项目 | 原版 Spec Kit | Spec Kit CN |
|--------|-----------------|-------------|
| 主要语言 | 英文 | 中文 |
| CLI命令 | `specify` | `specify-cn` |
| 包名 | `specify-cli` | `specify-cn-cli` |
| GitHub仓库 | github/spec-kit | Linfee/spec-kit-cn |
| 依赖管理 | pip/pipx推荐 | uv推荐 |
| 文档数量 | 20个 | 27个（增加测试报告）|

---

## 联系与支持

- **中文版本问题**: [Linfee/spec-kit-cn/issues](https://github.com/Linfee/spec-kit-cn/issues)
- **原版问题**: [github/spec-kit/issues](https://github.com/github/spec-kit/issues)
- **中文社区支持**: 参考 [SUPPORT.md](SUPPORT.md)

---

**最后更新**: 2025年9月16日
**下一次检查**: 2025年10月16日