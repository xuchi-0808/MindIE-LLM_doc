---
hide:
  - navigation
  - toc
---

# MindIE LLM

MindIE LLM 是大语言模型推理引擎。

## 快速开始

### 安装

```bash
pip install mindie-llm
```

### 基本使用

```python
from mindie_llm import LLM, SamplingParams

llm = LLM(model="your-model-path")
params = SamplingParams(max_tokens=128)
outputs = llm.generate("你好", params)
print(outputs)
```

## 文档导航

| 分类 | 内容 |
|------|------|
| **用户指南** | [快速入门](user_guide/quick_start.md) · [安装指南](user_guide/installation_guide.md) · [示例](user_guide/examples.md) · [模型支持列表](user_guide/model_support_list.md) · [优化与调优](user_guide/optimization_and_tuning.md) |
| **使用手册** | [离线推理](user_guide/user_manual/offline_inference.md) · [服务参数配置](user_guide/user_manual/service_parameter_configuration.md) · [模型参数配置](user_guide/user_manual/model_parameter_configuration.md) · [环境变量](user_guide/user_manual/environment_variable.md) · [性能调优](user_guide/user_manual/performance_tuning.md) |
| **特性** | [量化 (W8A8/W8A16/...)](user_guide/feature/w8a8.md) · [并行 (张量/数据/专家/...)](user_guide/feature/tensor_parallel.md) · [调度 (异步/SplitFuse/...)](user_guide/feature/asynchronous_scheduling.md) · [MoE](user_guide/feature/moe.md) · [MLA](user_guide/feature/mla.md) · [Function Call](user_guide/feature/function_call.md) |
| **开发指南** | [架构概览](developer_guide/architecture_design/architecture_overview.md) · [迁移适配](developer_guide/migration_and_adaptation_guide/atb_models_migration_and_adaptation_guide.md) |
| **API 参考** | [概览](api_reference/README.md) |
| **常见问题** | [FAQ](faq.md) |

## 相关链接

- [GitHub](https://github.com/your-org/mindie-llm)
- [问题反馈](https://github.com/your-org/mindie-llm/issues)
