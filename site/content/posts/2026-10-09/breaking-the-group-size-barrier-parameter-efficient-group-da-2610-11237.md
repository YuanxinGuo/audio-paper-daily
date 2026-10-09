---
title: "Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "ChainDance 将群舞生成分解为逐舞者条件链式生成，用冻结单人扩散骨干加两个轻量模块，支持可变群组规模。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐驱动动作生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#参数高效</span> <span class="tag-pill tag-pill-soft">#图卷积网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11237</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11237" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11237" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ChainDance 将群舞生成分解为逐舞者条件链式生成，用冻结单人扩散骨干加两个轻量模块，支持可变群组规模。
</div>

## 👥 作者与机构

**Jing Xu** ¹ · Cunjian Chen · Qiuhong Ke

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐驱动动作生成、扩散模型条件建模的研究者。若关注参数高效微调与可变规模生成，值得通读；重点看 §3 的 Chain-of-Dancers 分解与 GAME 图卷积聚合，以及表 2 的参数量/训练时间对比。可先看 RATE 与 GAME 的消融。

## 🌍 研究背景

群舞生成需从音乐合成多舞者协调动作，既要建模舞者间密集依赖保证空间协调，又要保留每个舞者身份。此前方法（如 AIOZ-GDance 上的端到端 Transformer）将所有舞者联合建模，架构与固定群组规模绑定，换人数需重训，且逐帧身份易纠缠。本文要解决可变群组规模下的可扩展生成与身份保持问题。

## 💡 核心创新

1. 将群舞生成重述为 Chain-of-Dancers 逐舞者条件分解
2. Role-Aware Text Encoder (RATE) 做逐舞者语义条件
3. Group-Aware Motion Encoder (GAME) 用距离加权 GCN 聚合已生成舞者
4. 推理期无训练噪声优化强制全局空间一致性

## 🏗️ 模型架构

输入为音乐与逐舞者角色文本条件，主干为冻结的单人扩散模型。RATE 将角色语义编码为逐舞者条件注入扩散；GAME 以距离加权图卷积网络聚合此前已生成的舞者动作，形成链式条件；推理时加入无训练的噪声优化过程以增强全局空间协调。输出为逐舞者动作序列，模型可跨不同群组规模复用，无需重训。

## 📚 数据集

- AIOZ-GDance（训练与评估，群舞动作数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 参数量 | AIOZ-GDance | 先前方法（未给具体值） | **少 3-4 倍** | 3-4× 更少 |
| 训练时间 | AIOZ-GDance | 先前方法（未给具体值） | **少 3-6 倍** | 3-6× 更少 |

摘要称在 AIOZ-GDance 上达到 SOTA 的动作质量与群组协调性，并结构性保持逐舞者身份，参数量减少 3-4 倍、训练时间减少 3-6 倍。但未给出 FID、多样性、协调性等具体数值，也未说明与哪些基线逐项对比，量化证据不足。

## 🎯 结论与影响

最强结论是：链式逐舞者分解可在不重训的前提下跨群组规模生成群舞，并显著降低参数与训练成本。这为可变规模、身份保持的动作生成提供了新范式，对动画与交互内容创作的落地有成本优势。

## ⚠️ 局限与未解决问题

摘要未给出任何量化指标与逐项基线对比，SOTA 宣称缺乏数字支撑；未报告推理延迟与噪声优化的额外开销；身份保持仅称结构性，缺客观度量；群组规模上限与失败案例未讨论。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
