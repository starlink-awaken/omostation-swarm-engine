# AGENTS.md — Swarm Engine

> eCOS v5 群体智能调度引擎 · 多 Agent 协作 + 任务分解 + 结果聚合

## Quick Commands

```bash
cd projects/swarm-engine
uv run pytest tests/ -q
uv run ruff check src/
```

## Architecture

群体智能调度层，与 AetherForge 蜂群体系协同：

```
aetherforge/                  ── 蜂群核心引擎
aetherforge-swarm-ext/        ── 扩展模块
swarm-engine/                 ── 群体智能调度（本仓）
```

### 能力

- **任务分解** — 复杂任务自动分解为子任务
- **Agent 分配** — 按能力路由子任务到合适 Agent
- **结果聚合** — 多 Agent 结果归并、冲突解决
- **进度追踪** — 子任务 DAG 状态管理和可视化

## Dependencies

- Python >=3.10, uv
- 依赖 aetherforge 消息协议

## Testing

```bash
uv run pytest tests/ -q
```
