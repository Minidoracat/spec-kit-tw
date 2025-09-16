---
name: tasks
description: "将计划分解为可执行任务。这是规范驱动开发生命周期的第三步。"
scripts:
  sh: scripts/bash/check-task-prerequisites.sh --json
  ps: scripts/powershell/check-task-prerequisites.ps1 -Json
---

将计划分解为可执行任务。

这是规范驱动开发生命周期的第三步。

根据提供的上下文参数，执行以下操作：

1. 从repo根目录运行 `scripts/check-task-prerequisites.sh --json` 并解析FEATURE_DIR和AVAILABLE_DOCS列表。所有路径必须是绝对路径。
2. 加载和分析可用的设计文档：
   - 始终阅读plan.md了解技术栈和库
   - 如果存在：阅读data-model.md了解实体
   - 如果存在：阅读contracts/了解API端点
   - 如果存在：阅读research.md了解技术决策
   - 如果存在：阅读quickstart.md了解测试场景

   注意：并非所有项目都有所有文档。例如：
   - CLI工具可能没有contracts/
   - 简单的库可能不需要data-model.md
   - 根据可用内容生成任务

3. 按照模板生成任务：
   - 使用 `/templates/tasks-template.md` 作为基础
   - 用基于以下内容的实际任务替换示例任务：
     * **设置任务**：项目初始化、依赖项、代码检查
     * **测试任务[P]**：每个合同一个，每个集成场景一个
     * **核心任务**：每个实体、服务、CLI命令、端点一个
     * **集成任务**：数据库连接、中间件、日志记录
     * **优化任务[P]**：单元测试、性能、文档

4. 任务生成规则：
   - 每个合同文件 → 标记为[P]的合同测试任务
   - data-model中的每个实体 → 标记为[P]的模型创建任务
   - 每个端点 → 实现任务（如果共享文件则不能并行）
   - 每个用户故事 → 标记为[P]的集成测试
   - 不同文件 = 可以并行[P]
   - 相同文件 = 顺序执行（无[P]）

5. 按依赖关系排序任务：
   - 设置优先于所有任务
   - 测试优先于实现（TDD）
   - 模型优先于服务
   - 服务优先于端点
   - 核心优先于集成
   - 所有任务优先于优化

6. 包含并行执行示例：
   - 分组可以一起运行的[P]任务
   - 显示实际的Task agent命令

7. 创建FEATURE_DIR/tasks.md，包含：
   - 来自实现计划的正确功能名称
   - 编号任务（T001、T002等）
   - 每个任务的清晰文件路径
   - 依赖关系说明
   - 并行执行指导

任务生成上下文：{ARGS}

tasks.md应该立即可执行 - 每个任务必须足够具体，以便LLM无需额外上下文即可完成。