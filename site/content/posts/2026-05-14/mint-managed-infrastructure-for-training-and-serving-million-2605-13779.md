---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LoRA", "#分布式系统", "#模型服务", "#模型训练", "#系统基础设施"]
summary: "MinT是一个管理LoRA适配器训练和服务的系统，支持百万级策略目录，通过仅移动适配器实现高效扩展。"
ShowToc: true
---

**评分**: 6.5 / 10  ·  **分档**: 前50%  ·  **主任务**: #系统基础设施  ·  **建议**: ⏳ 按需阅读

**标签**: #LoRA · #模型训练 · #模型服务 · #分布式系统

[← 返回 2026-05-14 速递](/posts/2026-05-14/)  ·  [arxiv](https://arxiv.org/abs/2605.13779)  ·  [pdf](https://arxiv.org/pdf/2605.13779)

---

## 📌 一句话总结

> MinT是一个管理LoRA适配器训练和服务的系统，支持百万级策略目录，通过仅移动适配器实现高效扩展。

## 📖 阅读建议

适合做LLM部署或LoRA微调系统的工程师阅读。重点看§3的Scale Up/Down/Out设计和§4的实验结果。建议通读全文，特别是系统架构部分。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| 应用场景 | 大规模LoRA策略的训练与在线服务，如RLHF后训练和模型适配。 |
| 核心创新 | Scale Up: 支持1T参数规模的LoRA RL训练和服务 · Scale Down: 仅移动适配器，减少18.3x步骤时间 · Scale Out: 百万级策略目录和千级适配器并发 |
| 模型架构 | MinT系统架构：基础模型常驻GPU，LoRA适配器通过rollout/update/export/serving等阶段流转。Scale Up支持密集和MoE架构；Scale Down仅导出适配器（<1%模型大小）；Scale Out分离策略寻址与工作集，支持10^6级目录。 |
| 数据集 | 摘要未指定具体数据集 |
| 关键结果 | 在4B密集模型上，适配器切换步骤时间减少18.3x；30B MoE模型减少2.85x。多策略GRPO训练加速1.77x和1.45x。MoE LoRA张量打包使引擎加载提升8.5-8.7x。支持100K单引擎扫描和千级适配器并发。 |

## 🎯 与本站重点领域的关联

与本站重点领域（语音增强、目标说话人提取等）无直接关联。但LoRA适配器管理和高效服务思路可迁移至音频领域的多任务模型部署，如为不同说话人或噪声条件部署轻量适配器。

## 💢 毒舌点评

> 系统设计扎实，但实验规模虽大却缺乏与现有LoRA服务系统（如Punica、S-LoRA）的对比，且未报告端到端延迟和吞吐量，更像工程报告而非学术论文。

## ⚠️ 局限与未解决问题

未与现有LoRA服务系统（如Punica、S-LoRA）进行对比；缺乏端到端延迟和吞吐量指标；实验仅在特定模型上验证，泛化性未知；未讨论适配器合并或动态批处理等常见优化。

## 👥 作者

<sub>Mind Lab, Song Cao, Vic Cao, Andrew Chen, Kaijie Chen, Cleon Cheng, Steven Chiang, Kaixuan Fan, Hera Feng, Huan Feng, Arthur Fu, Jun Gao, Hongquan Gu, Aaron Guan, Nolan Ho, Mutian Hong, Hailee Hou, Peixuan Hua, Charles Huang, Miles Jiang, Nora Jiang, Yuyi Jiang, Qiuyu Jin, Fancy Kong, Andrew Lei, Kyrie Lei, Alexy Li, Lucian Li, Ray Li, Theo Li, Zhihui Li, Jiayi Lin, Kairus Liu, Kieran Liu, Logan Liu, Xiang Liu, Irvine Lu, Maeve Luo, Runze Lv, Pony Ma, Verity Niu, Anson Qiu, Vincent Wang, Rio Yang, Maxwell Yao, Carrie Ye, Regis Ye, Wenlin Ye, Josh Ying, Danney Zeng, Yuhan Zhan, Anya Zhang, Di Zhang, Ruijia Zhang, Sueky Zhang, Ya Zhang, Wei Zhao, Ada Zhou, Changhai Zhou, Yuhua Zhou, Xinyue Zhu, Murphy Zhuang</sub>

---

评分：6.5  |  原始评分：6.5

[arxiv](https://arxiv.org/abs/2605.13779)  ·  [pdf](https://arxiv.org/pdf/2605.13779)
