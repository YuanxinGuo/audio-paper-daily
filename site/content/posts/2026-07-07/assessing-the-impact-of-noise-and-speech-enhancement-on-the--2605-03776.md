---
title: "Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编解码"]
summary: "评估经典与神经语音编解码器在噪声条件下的可懂度，并探究编码前语音增强的影响。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音编解码</span> <span class="tag-pill tag-pill-soft">#可懂度评估</span> <span class="tag-pill tag-pill-soft">#噪声鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.03776</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.03776" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.03776" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>评估经典与神经语音编解码器在噪声条件下的可懂度，并探究编码前语音增强的影响。
</div>

## 👥 作者与机构

**Lyonel Behringer** ¹ · Anna Leschanowsky · Anjana Rajasekhar · Emily Kratsch · Guillaume Fuchs

**机构**：华为 · 慕尼黑大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编解码与语音增强领域的研究者。重点看§3实验设计与§4结果分析，尤其是图2-4。可关注客观可懂度指标与主观评分的相关性。

## 🌍 研究背景

语音编解码器需在通信中保持可懂度。近年来低比特率神经编解码器兴起，但其在噪声环境下的表现尚不明确。经典编解码器通常设计有噪声鲁棒性，而神经编解码器可能更脆弱。此外，编码前级联语音增强模块的潜在收益未被系统评估。本文旨在填补这一空白，系统比较经典与神经编解码器在干净和噪声条件下的可懂度与听努力度，并探究语音增强的影响。

## 💡 核心创新

1. 系统评估经典与神经编解码器噪声鲁棒性
2. 探究编码前语音增强对可懂度的影响
3. 使用听努力度指标揭示可懂度饱和时的差异
4. 验证ASR客观可懂度与主观评分高度相关

## 🏗️ 模型架构

本文为实验评估研究，不提出新模型架构。评估对象包括经典编解码器（如Opus、EVS）和神经编解码器（如Lyra、SoundStream）。语音增强模块采用预训练的降噪模型（如DNS-Challenge基线）。评估流程：输入语音（干净或加噪）→ 可选语音增强 → 编解码器编码/解码 → 输出语音，然后进行主观和客观可懂度测试。

## 📚 数据集

- TIMIT（干净语音，用于生成测试样本）
- DEMAND（噪声数据集，用于加噪）
- ITU-T P.835（主观听测试验标准）

## 📊 实验结果

摘要未提供具体数值结果，但指出经典编解码器比神经编解码器更鲁棒；语音增强可显著提升受噪声影响的编解码器的可懂度和听努力度；听努力度在可懂度饱和时能揭示细微差异；ASR客观可懂度与主观评分高度相关。

## 🎯 结论与影响

经典编解码器在噪声下优于神经编解码器，但编码前语音增强可弥补神经编解码器的不足。听努力度是比可懂度更敏感的指标。ASR客观指标可替代部分主观测试。该研究为低比特率神经编解码器的噪声鲁棒性设计提供了指导，并建议在实际通信系统中考虑语音增强前处理。

## ⚠️ 局限与未解决问题

仅评估了有限数量的编解码器和噪声类型；语音增强模块固定，未优化联合训练；未考虑编码后语音增强或端到端优化；主观测试规模可能有限；未报告计算复杂度或延迟。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
