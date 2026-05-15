---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LoRA", "#分布式训练", "#大模型训练与推理", "#强化学习", "#模型服务"]
summary: "MinT是一个管理百万级LoRA策略的训练和服务基础设施，通过仅传输适配器实现高效扩展。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#大模型训练与推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#LoRA</span> <span class="tag-pill tag-pill-soft">#分布式训练</span> <span class="tag-pill tag-pill-soft">#模型服务</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13779</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13779" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13779" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MinT是一个管理百万级LoRA策略的训练和服务基础设施，通过仅传输适配器实现高效扩展。
</div>

## 👥 作者与机构

**Mind Lab** ¹ · Song Cao · Vic Cao · Andrew Chen · Kaijie Chen · Cleon Cheng · Steven Chiang · Kaixuan Fan · … 等 54 人

**机构**：Mind Lab

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事大模型训练和服务系统研究的工程师和学者。建议重点阅读§3（Scale Up）、§4（Scale Down）和§5（Scale Out）以及表1、2、3。可先看§4的适配器切换实验和§5的百万级目录服务。

## 🌍 研究背景

在大模型时代，LoRA微调产生大量策略，传统方法将每个策略合并为完整检查点，导致存储和传输开销巨大。现有系统难以支持百万级策略的快速切换和高效服务。MinT通过保持基模型常驻、仅移动LoRA适配器，解决大规模策略管理中的训练、服务、调度和数据移动问题。

## 💡 核心创新

1. Scale Up：支持1T参数级稠密和MoE模型的LoRA RL训练与推理
2. Scale Down：适配器仅占基模型<1%，切换延迟降低18.3x
3. Scale Out：分离策略寻址与计算资源，支持百万级目录和千级并发
4. 打包MoE LoRA张量，引擎加载速度提升8.5-8.7x

## 🏗️ 模型架构

MinT采用服务化架构，基模型常驻GPU，LoRA适配器通过分布式存储管理。训练阶段使用GRPO进行多策略并发强化学习，适配器导出后通过rollout、update、export、evaluation、serving、rollback等阶段流转。推理时，调度器根据请求选择适配器，通过tensor-parallel部署支持大规模目录。关键模块包括适配器仓库、调度器、训练引擎和服务引擎。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 适配器切换延迟 | 4B稠密模型 | 完整检查点切换 | **适配器切换** | 18.3x加速 |
| 适配器切换延迟 | 30B MoE模型 | 完整检查点切换 | **适配器切换** | 2.85x加速 |
| 多策略GRPO训练墙钟时间 | 4B稠密模型 | 串行训练 | **并发GRPO** | 1.77x加速 |
| 多策略GRPO训练墙钟时间 | 30B MoE模型 | 串行训练 | **并发GRPO** | 1.45x加速 |
| 引擎加载速度 | MoE LoRA张量 | 未打包 | **打包** | 8.5-8.7x提升 |

MinT在4B稠密和30B MoE模型上验证了Scale Down效果，适配器切换延迟分别降低18.3x和2.85x。并发GRPO训练墙钟时间缩短1.77x和1.45x，且峰值内存不增加。Scale Out方面，单引擎可扫描100K策略，集群支持千级并发适配器，打包MoE LoRA张量使引擎加载速度提升8.5-8.7x。

## 🎯 结论与影响

MinT证明了通过仅移动LoRA适配器可以高效管理百万级策略，在1T参数级基模型上实现训练和服务。该系统对工业界大规模模型微调和服务具有重要参考价值，可显著降低存储和传输成本，提升策略切换效率。

## ⚠️ 局限与未解决问题

论文未讨论适配器之间的冲突或干扰问题，也未提供端到端服务质量（如延迟SLA）的详细分析。此外，实验仅在特定模型架构（4B稠密、30B MoE）上验证，泛化性有待进一步研究。

## 📋 引用

```bibtex
@article{lab20262605,
  title  = {MinT: Managed Infrastructure for Training and Serving Millions of LLMs},
  author = {Mind Lab and  Song Cao and  Vic Cao and  Andrew Chen and  Kaijie Chen and  Cleon Cheng and  Steven Chiang and  Kaixuan Fan and  Hera Feng and  Huan Feng and  Arthur Fu and  Jun Gao and  Hongquan Gu and  Aaron Guan and  Nolan Ho and  Mutian Hong and  Hailee Hou and  Peixuan Hua and  Charles Huang and  Miles Jiang and  Nora Jiang and  Yuyi Jiang and  Qiuyu Jin and  Fancy Kong and  Andrew Lei and  Kyrie Lei and  Alexy Li and  Lucian Li and  Ray Li and  Theo Li and  Zhihui Li and  Jiayi Lin and  Kairus Liu and  Kieran Liu and  Logan Liu and  Xiang Liu and  Irvine Lu and  Maeve Luo and  Runze Lv and  Pony Ma and  Verity Niu and  Anson Qiu and  Vincent Wang and  Rio Yang and  Maxwell Yao and  Carrie Ye and  Regis Ye and  Wenlin Ye and  Josh Ying and  Danney Zeng and  Yuhan Zhan and  Anya Zhang and  Di Zhang and  Ruijia Zhang and  Sueky Zhang and  Ya Zhang and  Wei Zhao and  Ada Zhou and  Changhai Zhou and  Yuhua Zhou and  Xinyue Zhu and  Murphy Zhuang},
  journal = {arXiv preprint arXiv:2605.13779},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
