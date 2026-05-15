---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LoRA", "#分布式训练", "#大模型训练与推理", "#强化学习", "#模型服务"]
summary: "MinT是一个管理百万级LoRA策略的分布式基础设施，支持在共享基座模型上高效训练和服务大量适配器，通过Scale Up/Down/Out三维扩展实现显著性能提升。"
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
<span class="tldr-tag">TL;DR</span>MinT是一个管理百万级LoRA策略的分布式基础设施，支持在共享基座模型上高效训练和服务大量适配器，通过Scale Up/Down/Out三维扩展实现显著性能提升。
</div>

## 👥 作者与机构

**Mind Lab** ¹ · Song Cao · Vic Cao · Andrew Chen · Kaijie Chen · Cleon Cheng · Steven Chiang · Kaixuan Fan · … 等 54 人

**机构**：Mind Lab

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事大模型训练推理系统、LoRA微调或RLHF的工程师和研究者。建议重点阅读§3（Scale Down的适配器移交机制）和§4（Scale Out的百万级策略编目），以及表1-3的性能对比。可先看摘要和§1引言了解整体设计。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 在共享基座模型上训练和服务数百万个LoRA策略，适用于RLHF后训练和在线推理。 |
| **核心创新** | Scale Up：支持超过1T参数的前沿密集和MoE架构的LoRA RL训练与服务 · Scale Down：仅传输LoRA适配器，减少18.3x步时间，并发多策略GRPO缩短1.77x墙钟时间 · Scale Out：分离策略寻址与工作集，支持10^6级编目和千级活跃适配器，冷加载作为调度服务 |
| **模型架构** | 基座模型常驻GPU，LoRA适配器通过导出、更新、评估、服务、回滚等阶段移动。Scale Up扩展至1T参数模型；Scale Down仅传输适配器（<1%基座大小）；Scale Out通过张量并行支持百万级策略编目，打包MoE LoRA张量提升加载8.5-8.7x。 |
| **数据集** | 未明确指定数据集，使用内部RL训练数据 |
| **关键结果** | 在4B密集模型上，适配器移交减少18.3x步时间；30B MoE模型上减少2.85x。并发多策略GRPO缩短墙钟时间1.77x（4B）和1.45x（30B），不增加峰值内存。单引擎扫描100K策略，打包MoE LoRA张量提升加载8.5-8.7x。 |

## 🎯 与本站重点领域的关联

与本站5个重点领域无直接关联。但Scale Down的适配器移交思路可迁移至语音领域的个性化模型服务（如说话人自适应），减少存储和传输开销。Scale Out的编目机制对大规模语音模型库管理有参考价值。

## ⚠️ 局限与未解决问题

未提供与现有系统（如vLLM、S-LoRA）的定量对比；实验仅在内部模型和任务上验证，缺乏公开基准；未报告推理延迟和吞吐量指标；未讨论适配器之间的干扰问题。

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
