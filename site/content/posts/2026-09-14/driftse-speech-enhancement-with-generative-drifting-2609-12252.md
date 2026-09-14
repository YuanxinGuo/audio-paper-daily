---
title: "DriftSE: Speech Enhancement with Generative Drifting"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "DriftSE 将语音增强建模为潜空间分布漂移平衡问题，用双潜空间（语义+声学）漂移实现 1 NFE 一步增强，并支持无配对跨数据集训练。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#生成模型</span> <span class="tag-pill tag-pill-soft">#一步生成</span> <span class="tag-pill tag-pill-soft">#去混响</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.12252</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.12252" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.12252" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>DriftSE 将语音增强建模为潜空间分布漂移平衡问题，用双潜空间（语义+声学）漂移实现 1 NFE 一步增强，并支持无配对跨数据集训练。
</div>

## 👥 作者与机构

**Liang Xu** ¹ · Diego Caviedes-Nozal · W. Bastiaan Kleijn · Longfei Felix Yan · Rasmus Kongsgaard Olsson

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做生成式语音增强、扩散/流匹配加速的研究者与工程落地团队阅读。建议重点看 §3 双潜空间漂移的公式推导与 §4 无配对训练目标，再看表 2/表 3 的 WER 与实时因果对比。若关注推理效率，优先核对 1 NFE 与 RTF 数据。

## 🌍 研究背景

当前语音增强 SOTA 多依赖扩散/流匹配等生成模型，虽能提升感知质量，但需数十步采样，推理成本高，难以实时部署；判别式方法（如 BSRNN、SEPFormer 类）虽快却易残留噪声或过度抑制。此外，多数方法依赖成对的含噪-干净数据，跨数据集泛化受限。本文要解决的核心问题是：如何在保持生成式建模质量的同时实现一步推理，并摆脱对配对数据的依赖。

## 💡 核心创新

1. 将增强建模为潜空间分布漂移平衡，推理时丢弃漂移过程实现 1 NFE 一步生成
2. 提出双潜空间漂移：语义潜空间保音素结构，声学潜空间保物理保真，并行漂移
3. 基于潜分布对齐而非逐点目标，实现完全无配对训练与跨数据集学习
4. 验证方法对多种生成器主干（backbone）的架构灵活性

## 🏗️ 模型架构

输入含噪语音先编码到潜空间，训练时在语义潜空间与声学潜空间分别构建漂移场，将生成器推前分布对齐到干净语音流形；两个潜空间并行漂移，语义分支约束音素可懂度，声学分支约束波形保真度。推理阶段完全丢弃漂移过程，生成器直接一步映射到增强输出，无需迭代采样。摘要未给出具体主干网络名与参数量，仅强调跨 backbone 的通用性，支持离线与实时因果两种配置。

## 📊 实验结果

摘要仅声明在加性去噪与卷积去混响两类任务上评估，覆盖离线与实时因果设置，并在全部四个评测数据集上取得 SOTA WER，且严格保持 1 NFE。但摘要未给出任何具体指标数值、数据集名称与基线对比数字，无法量化提升幅度，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是：潜空间分布漂移可在 1 NFE 下同时取得 SOTA WER 与生成式保真度，并支持无配对跨数据集训练。这为扩散类增强的推理加速提供了新范式，可能推动实时生成式增强与低资源域适配研究。工业上意味着更低的推理延迟与更易获取的训练数据，利于端侧与流式部署。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、RTF、参数量等效率指标，1 NFE 的实际加速比不明；缺少与判别式强基线（如 BSRNN）在同等条件下的系统对比；双潜空间引入额外编码器开销未讨论；无配对训练在真实失配场景下的鲁棒性缺乏消融；四个数据集名称与具体 WER 数值均未披露，复现门槛较高。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
