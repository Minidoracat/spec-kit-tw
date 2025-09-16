---
name: plan
description: "规划如何实现指定功能。这是规范驱动开发生命周期的第二步。"
scripts:
  sh: scripts/bash/setup-plan.sh --json
  ps: scripts/powershell/setup-plan.ps1 -Json
---

规划如何实现指定功能。

这是规范驱动开发生命周期的第二步。

根据提供的实现细节参数，执行以下操作：

1. 从repo根目录运行 `scripts/setup-plan.sh --json` 并解析JSON获取FEATURE_SPEC、IMPL_PLAN、SPECS_DIR、BRANCH。所有未来的文件路径必须是绝对路径。
2. 阅读和分析功能规范以了解：
   - 功能需求和用户故事
   - 功能和非功能需求
   - 成功标准和验收标准
   - 任何提到的技术约束或依赖关系

3. 阅读位于 `/memory/constitution.md` 的章程以了解章程要求。

4. 执行实现计划模板：
   - 加载 `/templates/plan-template.md`（已复制到IMPL_PLAN路径）
   - 将输入路径设置为FEATURE_SPEC
   - 运行执行流程（main）函数步骤1-10
   - 模板是自包含且可执行的
   - 按照指定的错误处理和门控检查
   - 让模板指导在$SPECS_DIR中生成工件：
     * 阶段0生成research.md
     * 阶段1生成data-model.md、contracts/、quickstart.md
     * 阶段2生成tasks.md
   - 将参数中提供的用户详细信息合并到技术上下文：{ARGS}
   - 完成每个阶段后更新进度跟踪

5. 验证执行完成：
   - 检查进度跟踪显示所有阶段完成
   - 确保生成了所有必需的工件
   - 确认执行中没有ERROR状态

6. 报告结果，包括分支名称、文件路径和生成的工件。

对所有文件操作使用带有repo根目录的绝对路径，以避免路径问题。