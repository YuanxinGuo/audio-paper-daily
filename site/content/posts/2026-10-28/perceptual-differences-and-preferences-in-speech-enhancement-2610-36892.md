---
title: "Perceptual Differences and Preferences in Speech Enhancement"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用众包三角测试与成对偏好测试，考察四个语音增强系统在可辨别性与偏好两个维度上的感知差异。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#主观听测</span> <span class="tag-pill tag-pill-soft">#感知评价</span> <span class="tag-pill tag-pill-soft">#众包评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.36892</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.36892" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.36892" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用众包三角测试与成对偏好测试，考察四个语音增强系统在可辨别性与偏好两个维度上的感知差异。
</div>

## 👥 作者与机构

**Simon Dahl Jepsen** ¹ · Jesper Rindom Jensen

**机构**：奥尔堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强评测、主观听测方法学的研究者阅读。值得通读，重点看实验设计与三角/成对测试的结果分析部分，以及客观指标与可辨别性、偏好相关性分析。可先看结果图表，再回看方法细节，思考如何把可辨别性纳入自己的评测流程。

## 🌍 研究背景

语音增强长期以 SI-SDR、PESQ、STOI 等客观指标和分类主观听测（MOS）评价质量与可懂度，SOTA 系统在这些指标上已接近饱和。但客观指标与人类感知存在偏差，且现有主观测试多为绝对评分，难以回答“处理后的语音是否可被听出差异”“日常听者是否更喜欢”这两个互补问题。本文针对这一评测盲区，系统考察可辨别性与偏好两个维度。

## 💡 核心创新

1. 引入三角测试测量可辨别性（discrimination）
2. 引入成对偏好测试测量听者偏好
3. 跨四个 SE 系统与干净参考做对比
4. 分析客观指标与可辨别性/偏好的相关性

## 🏗️ 模型架构

本文为评测方法学研究，不提出新的增强网络。实验选取四个语音增强系统作为被测对象，在多种声学条件下生成增强语音，与干净参考一并用于众包听测。听测包含两类任务：三角测试（每次给三段语音，其中两段相同，要求听者找出不同者）用于测量可辨别性；成对偏好测试（给两段语音要求选择更喜欢的一段）用于测量偏好。随后将 PESQ、SI-SDR 等客观指标与两类主观结果做相关性分析。

## 📚 数据集

- 四个语音增强系统的输出语音（评估，众包听测）
- 干净参考语音（评估，作为对比锚点）

## 📊 实验结果

摘要未给出具体数值。作者报告：听者的可辨别能力与是否存在系统性偏好均随系统和声学条件显著变化；客观指标与可辨别性、偏好的相关性不稳定，说明单一客观指标不足以刻画感知差异。

## 🎯 结论与影响

最强结论是：可辨别性与偏好是独立于传统质量/可懂度评分的互补评测维度，且随系统与条件变化明显。这提示后续 SE 研究应补充这两类测试，工业评测流程也可能需要引入三角与成对偏好任务。

## ⚠️ 局限与未解决问题

摘要未给出听测规模、听者筛选标准与置信区间；仅四个系统、条件覆盖有限；未报告客观指标相关性的具体数值与显著性；众包听者与目标用户群体可能存在偏差。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
