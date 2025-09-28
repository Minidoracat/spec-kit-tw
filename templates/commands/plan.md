---
description: 使用计划模板执行实施规划工作流以生成设计工件。
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
---

用户输入可以直接由代理提供或作为命令参数提供给您 - 在继续执行提示之前您**必须**考虑它（如果不为空）。

用户输入：

$ARGUMENTS

鉴于作为参数提供的实现细节，执行以下操作：

1. 从仓库根目录运行 `{SCRIPT}` 并解析 JSON 以获取 FEATURE_SPEC、IMPL_PLAN、SPECS_DIR、BRANCH。所有未来的文件路径必须是绝对路径。
   - 在继续之前，检查 FEATURE_SPEC 中是否存在 `## 澄清` 部分且至少有一个 `会话` 子标题。如果缺失或存在明显的模糊区域（模糊形容词、未解决的关键选择），请暂停并指示用户首先运行 `/clarify` 以减少返工。只有在以下情况下才继续：(a) 澄清存在 OR (b) 提供了明确的用户覆盖（例如，"继续而不澄清"）。不要试图自己捏造澄清。
2. 阅读和分析功能规范以了解：
   - 功能需求和用户故事
   - 功能和非功能需求
   - 成功标准和验收标准
   - 任何提到的技术约束或依赖关系

3. 阅读位于 `/memory/constitution.md` 的章程以了解章程要求。

4. 执行实现计划模板：
   - 加载 `/templates/plan-template.md`（已复制到 IMPL_PLAN 路径）
   - 将输入路径设置为 FEATURE_SPEC
   - 运行执行流程（main）函数步骤 1-9
   - 模板是自包含且可执行的
   - 按照指定的错误处理和门控检查
   - 让模板指导在 $SPECS_DIR 中生成工件：
     * 阶段 0 生成 research.md
     * 阶段 1 生成 data-model.md、contracts/、quickstart.md
     * 阶段 2 生成 tasks.md
   - 将参数中提供的用户详细信息合并到技术上下文：{ARGS}
   - 完成每个阶段后更新进度追踪

5. 验证执行完成：
   - 检查进度追踪显示所有阶段完成
   - 确保生成了所有必需的工件
   - 确认执行中没有 ERROR 状态

6. 报告结果，包括分支名称、文件路径和生成的工件。

对所有文件操作使用带有仓库根目录的绝对路径，以避免路径问题。