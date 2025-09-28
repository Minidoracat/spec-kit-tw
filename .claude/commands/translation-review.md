---
name: translation-review
description: "Review and fix translation quality between spec-kit original and Chinese localized version"
---

用户输入可以直接由代理提供或作为命令参数提供给您 - 您**必须**考虑它（如果不为空）。

用户输入：

$ARGUMENTS

目标：系统性地review原项目spec-kit与中文版之间的翻译质量，识别并修复所有翻译错误、术语不一致和功能逻辑问题。

执行步骤：

1. 验证环境准备：
   - 确认spec-kit目录存在且包含原版文件
   - 确认templates/和templates/commands/目录结构完整
   - 确认memory/目录存在

2. 目录结构对比分析：
   - 对比原项目spec-kit中templates和templates/commands目录结构
   - 对比当前项目templates目录与原项目的差异
   - 对比当前项目memory目录与原项目的差异

3. 翻译质量系统性review：
   - **templates目录核心文件**：
     * agent-file-template.md - AI助手文件模板
     * spec-template.md - 功能规范模板
     * plan-template.md - 实施计划模板
     * tasks-template.md - 任务生成模板

   - **templates/commands目录所有文件**：
     * analyze.md - 分析命令
     * clarify.md - 澄清命令
     * constitution.md - 章程命令
     * implement.md - 实施命令
     * plan.md - 计划命令
     * specify.md - 规范命令
     * tasks.md - 任务命令

   - **memory目录**：
     * constitution.md - 项目章程模板
     
   - 上述目录中新出现的一切没有提到的文件也需要review

4. 输出结构化报告等待人类审核：

行为规则：
- 必须对比原版spec-kit中的对应文件
- 使用Task工具并行对比
- 所有文件翻译后，必须确保和原版表达是一样的语义，不能新增或减少内容
- 所有的路径，不需要翻译，都以原版为准
- 确保修复后的功能与原版完全一致
- 优先修复功能逻辑错误
- 保持技术术语的准确性
- 输出详细的修复报告
- 所有没有问题，请直接告诉用户
