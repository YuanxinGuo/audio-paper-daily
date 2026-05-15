---
title: "MinT: Managed Infrastructure for Training and Serving Millions of LLMs"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#大模型训练与推理"]
summary: "提出MinT系统，通过LoRA适配器管理实现百万级策略的分布式训练与在线服务，显著降低资源开销。"
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

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13779" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13779" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MinT系统，通过LoRA适配器管理实现百万级策略的分布式训练与在线服务，显著降低资源开销。
</div>

## 👥 作者与机构

Mind Lab · **Song Cao** ¹ · **Vic Cao** ¹ · **Andrew Chen** ¹ · **Kaijie Chen** ¹ · Cleon Cheng · Steven Chiang · Kaixuan Fan · … 等 54 人

**机构**：Mind Lab

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事大模型训练/推理系统、LoRA微调或RLHF的工程师和研究者。建议重点阅读§3（Scale Up/Down/Out）和§4（实验结果），特别是表1-3中的效率对比。可先看§3.2的适配器切换优化和§3.3的百万级目录管理。

## 🌍 研究背景

当前大模型后训练（如RLHF）常产生大量策略版本，传统方法需为每个策略保存完整检查点，导致存储和切换开销巨大。LoRA虽能减少适配器大小，但缺乏统一管理训练、评估、服务的系统。现有工作多关注单模型优化，未解决多策略并发场景下的资源调度和冷启动问题。MinT旨在构建一个托管基础设施，支持百万级LoRA策略的高效训练与在线服务。

## 💡 核心创新

1. Scale Up：支持1T参数级稠密/MoE模型的LoRA RL训练与推理
2. Scale Down：仅传输LoRA适配器（<1%模型大小），切换延迟降低18.3x
3. Scale Out：分离策略寻址与计算资源，支持10^6级目录和千级并发适配器
4. 打包MoE LoRA张量，引擎加载速度提升8.5-8.7x

## 🏗️ 模型架构

MinT采用服务化接口管理LoRA适配器生命周期（回滚、更新、导出、评估、服务、回退）。核心架构：基础模型常驻GPU，LoRA适配器作为独立对象存储。Scale Up通过分布式训练框架支持MLA和DSA注意力路径的LoRA RL；Scale Down通过适配器独占传输减少数据移动；Scale Out使用张量并行部署，将策略目录与工作集分离，冷加载作为调度任务处理。系统包含训练引擎、服务引擎和调度器。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 适配器切换延迟降低 | 4B稠密模型 | 完整检查点切换 | **18.3x** | -18.3x |
| 适配器切换延迟降低 | 30B MoE模型 | 完整检查点切换 | **2.85x** | -2.85x |
| 多策略GRPO墙钟时间缩短 | 4B稠密模型 | 顺序执行 | **1.77x** | -1.77x |
| 多策略GRPO墙钟时间缩短 | 30B MoE模型 | 顺序执行 | **1.45x** | -1.45x |
| MoE LoRA引擎加载速度提升 | 集群规模 | 未打包 | **8.5-8.7x** | +8.5-8.7x |

实验在4B稠密和30B MoE模型上验证，适配器切换延迟分别降低18.3x和2.85x；多策略GRPO并发训练墙钟时间缩短1.77x和1.45x，且峰值内存未增加。在集群规模下，单引擎可扫描100K策略目录，支持千级并发适配器，MoE LoRA打包使加载速度提升8.5-8.7x。系统总参数量超过1T。

## 🎯 结论与影响

MinT通过适配器级管理实现了百万级LoRA策略的高效训练与服务，在1T参数级模型上验证了Scale Up/Down/Out三维扩展能力。该系统为大规模后训练和在线服务提供了基础设施范式，有望降低工业界多策略部署的存储和计算成本，推动RLHF等技术的规模化应用。

## ⚠️ 局限与未解决问题

实验仅报告了效率指标，未提供下游任务（如推理、对话）的性能对比，无法评估LoRA策略质量是否受影响。系统依赖LoRA假设，不适用于全参数微调。未讨论适配器版本冲突或一致性保证。缺乏与现有系统（如vLLM、Ray Serve）的端到端对比。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
