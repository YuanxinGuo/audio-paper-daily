---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LoRA", "#分布式训练", "#大模型训练与推理", "#强化学习", "#模型服务"]
summary: "MinT是一个管理百万级LoRA策略的分布式基础设施，支持前沿规模模型的后训练与在线服务，通过适配器分离实现高效扩展。"
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
<span class="tldr-tag">TL;DR</span>MinT是一个管理百万级LoRA策略的分布式基础设施，支持前沿规模模型的后训练与在线服务，通过适配器分离实现高效扩展。
</div>

## 👥 作者与机构

Mind Lab · **Song Cao** ¹ · **Vic Cao** ¹ · **Andrew Chen** ¹ · Kaijie Chen · Cleon Cheng · Steven Chiang · Kaixuan Fan · … 等 54 人

**机构**：Mind Lab

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事大模型训练/推理系统、LoRA微调或RLHF的工程师/研究者。建议重点阅读§3（Scale Up）、§4（Scale Down）和§5（Scale Out）及表1、2、3。可先看§4的适配器切换延迟对比。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 管理大量基于LoRA的模型策略（如RL后训练）的分布式训练与在线服务。 |
| **核心创新** | 提出适配器分离架构，避免合并完整检查点 · 三轴扩展：Scale Up/Scale Down/Scale Out · 支持百万级可寻址策略目录与千级活跃适配器 |
| **模型架构** | 输入：基础模型（稠密或MoE）与LoRA适配器。主干：MinT服务接口，管理适配器生命周期（导出、更新、评估、服务、回滚）。关键模块：分布式训练引擎、调度器、数据移动层。输出：通过服务接口提供LoRA适配器的训练与推理。参数量：支持超过1T总参数的基础模型。 |
| **数据集** | 未明确指定数据集 |
| **关键结果** | 在4B稠密模型上，适配器切换延迟降低18.3倍；30B MoE模型降低2.85倍。并发多策略GRPO训练加速1.77倍（4B）和1.45倍（30B）。打包MoE LoRA张量使引擎加载提升8.5-8.7倍。支持单引擎扫描100K策略目录。 |

## 🎯 与本站重点领域的关联

与本站5个重点领域无直接关联。但其中的适配器分离、高效切换和分布式扩展思路可迁移至语音领域的个性化模型服务（如说话人自适应、多任务LoRA），值得关注。

## ⚠️ 局限与未解决问题

未报告端到端训练/推理吞吐量对比；缺乏与现有系统（如vLLM、SGLang）的定量比较；未讨论适配器精度损失；实验仅基于内部模型，未见开源复现。

## 📋 引用

```bibtex
@article{cao20262605,
  title  = {MinT: Managed Infrastructure for Training and Serving Millions of LLMs},
  author = {Mind Lab and  Song Cao and  Vic Cao and  Andrew Chen and  Kaijie Chen and  Cleon Cheng and  Steven Chiang and  Kaixuan Fan and  Hera Feng and  Huan Feng and  Arthur Fu and  Jun Gao and  Hongquan Gu and  Aaron Guan and  Nolan Ho and  Mutian Hong and  Hailee Hou and  Peixuan Hua and  Charles Huang and  Miles Jiang and  Nora Jiang and  Yuyi Jiang and  Qiuyu Jin and  Fancy Kong and  Andrew Lei and  Kyrie Lei and  Alexy Li and  Lucian Li and  Ray Li and  Theo Li and  Zhihui Li and  Jiayi Lin and  Kairus Liu and  Kieran Liu and  Logan Liu and  Xiang Liu and  Irvine Lu and  Maeve Luo and  Runze Lv and  Pony Ma and  Verity Niu and  Anson Qiu and  Vincent Wang and  Rio Yang and  Maxwell Yao and  Carrie Ye and  Regis Ye and  Wenlin Ye and  Josh Ying and  Danney Zeng and  Yuhan Zhan and  Anya Zhang and  Di Zhang and  Ruijia Zhang and  Sueky Zhang and  Ya Zhang and  Wei Zhao and  Ada Zhou and  Changhai Zhou and  Yuhua Zhou and  Xinyue Zhu and  Murphy Zhuang},
  journal = {arXiv preprint arXiv:2605.13779},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
