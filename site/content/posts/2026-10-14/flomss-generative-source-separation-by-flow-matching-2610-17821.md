---
title: "FLOMSS: Generative Source Separation by Flow Matching"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "系统研究 flow matching 用于四源全频带立体声音乐分离，考察预测目标、流路径、单源/多源建模与混合一致性约束。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#生成模型</span> <span class="tag-pill tag-pill-soft">#Flow Matching</span> <span class="tag-pill tag-pill-soft">#音乐源分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17821</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://ik4sumii.github.io/FLOMSS/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ik4sumii.github.io/FLOMSS/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17821" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17821" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://ik4sumii.github.io/FLOMSS/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究 flow matching 用于四源全频带立体声音乐分离，考察预测目标、流路径、单源/多源建模与混合一致性约束。
</div>

## 👥 作者与机构

**Shuyang Cui** ¹ · Zhi Zhong · Keisuke Toyama · Koichi Saito · Qiyu Wu · Yukara Ikemiya · Junghyun Koo · Kin Wai Cheuk · … 等 5 人

**机构**：索尼

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐源分离与生成式音频建模的研究者。建议通读，重点看 §3 关于预测目标与流路径的设计选择，以及表 2 的客观指标对比和消融；若关注生成范式可先看单源 vs 多源建模一节。

## 🌍 研究背景

音乐源分离长期由判别式方法主导，如 Demucs、HDemucs、BSRNN 等，在 MUSDB18 上已取得较高 SDR。近期 flow matching 在图像与音频生成中展现出建模复杂分布的能力，但将其系统用于全频带立体声四源 MSS 的研究仍不充分，预测目标、流路径、单源与多源建模、混合一致性等关键设计缺乏统一比较。本文旨在系统考察这些设计维度，并补充 embedding 指标与听测。

## 💡 核心创新

1. 系统比较 flow matching 的预测目标与流路径设计
2. 对比单源与多源建模策略在 MSS 中的表现
3. 引入混合一致性约束提升生成分离质量
4. 补充 embedding 指标与主观听测的综合评测

## 🏗️ 模型架构

输入为全频带立体声混合音频，经编码后送入基于 flow matching 的生成主干，在噪声到目标源的连续流路径上学习速度场。模型可对每个 stem 单独建模或联合多源建模，并施加混合一致性约束使各源之和逼近原始混合。输出为 Vocals、Bass、Drums、Other 四路立体声 stem。摘要未给出具体参数量与网络细节。

## 📚 数据集

- MUSDB18-HQ（训练与评估，全频带立体声四源）

## 📊 实验结果

摘要仅说明在 MUSDB18-HQ 上客观与主观测试均具竞争力，未给出具体 SDR、SI-SDR、PESQ 或 MOS 数值，也未列出与 Demucs、BSRNN 等基线的逐项对比。消融方面提到考察了预测目标、流路径、单源/多源建模与混合一致性，但具体增益未在摘要中量化。

## 🎯 结论与影响

本文表明 flow matching 可作为音乐源分离的可行生成式范式，在客观与主观评测中达到有竞争力的水平。其系统性的设计比较为后续生成式 MSS 研究提供了参考基线，也提示工业界在追求高保真 stem 时可考虑生成式建模路线。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与完整基线对比，难以判断相对判别式 SOTA 的真实差距；缺少推理延迟与计算成本报告；听测规模与统计显著性未说明；混合一致性约束的消融增益未量化。

## 🔗 开源资源

- **Demo / 试听**：<https://ik4sumii.github.io/FLOMSS/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
