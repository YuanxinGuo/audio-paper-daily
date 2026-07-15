---
title: "Teaching Speech Enhancement Models to Sing: Domain Adaptation from Speech Enhancement to Singing Voice Separation"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "将歌声分离视为从语音增强到歌声分离的域自适应，通过全微调或LoRA微调预训练语音增强模型，在数据稀缺场景下有效提升歌声分离性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#域自适应</span> <span class="tag-pill tag-pill-soft">#LoRA</span> <span class="tag-pill tag-pill-soft">#歌声分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.11630</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.11630" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.11630" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将歌声分离视为从语音增强到歌声分离的域自适应，通过全微调或LoRA微调预训练语音增强模型，在数据稀缺场景下有效提升歌声分离性能。
</div>

## 👥 作者与机构

**Paul A. Bereuter** ¹ · Mark D. Plumbley · Alois Sontacchi

**机构**：萨里大学 · 格拉茨科技大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、歌声分离或域自适应研究的读者。建议重点阅读§3微调策略和§4实验结果，特别是表1中LoRA与全微调的对比。可先看§4.2关于灾难性遗忘的分析。

## 🌍 研究背景

歌声分离任务面临训练数据有限的瓶颈，而语音增强模型受益于大规模标注数据集。现有歌声分离方法通常从头训练，性能受限于数据量。本文提出将歌声分离视为从语音增强到歌声分离的域自适应问题，利用预训练语音增强模型的知识，通过微调策略提升歌声分离性能，同时探索如何避免灾难性遗忘。

## 💡 核心创新

1. 将歌声分离形式化为语音增强到歌声分离的域自适应
2. 对比全微调与LoRA参数高效微调两种策略
3. 在判别式与生成式模型上验证域自适应有效性
4. LoRA仅用6-12%额外参数保持语音增强能力
5. 生成式模型在未见测试集上展现更好泛化性

## 🏗️ 模型架构

输入混合音频→预训练语音增强模型（判别式或生成式）→微调适配歌声分离。判别式模型采用U-Net架构，生成式模型基于扩散或GAN。微调方式包括全微调（更新全部参数）和LoRA（在注意力层注入低秩矩阵，仅更新少量参数）。输出为分离后的歌声和伴奏。

## 📚 数据集

- MUSDB18（训练/评估，150首歌曲）
- DSD100（评估，100首歌曲）
- LibriMix（语音增强预训练数据，未明确规模）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR (dB) | MUSDB18 | 从头训练U-Net (5.2) | **全微调U-Net (6.5)** | +1.3 dB |
| SDR (dB) | MUSDB18 | 从头训练扩散模型 (4.8) | **全微调扩散模型 (6.6)** | +1.8 dB |
| SDR (dB) | MUSDB18 | 从头训练U-Net (5.2) | **LoRA微调U-Net (5.5)** | +0.3 dB |
| SDR (dB) | MUSDB18 | 从头训练扩散模型 (4.8) | **LoRA微调扩散模型 (5.1)** | +0.3 dB |

全微调在歌声分离上取得最高SDR（U-Net 6.5 dB，扩散模型6.6 dB），但导致语音增强性能下降（灾难性遗忘）。LoRA微调以仅6-12%额外参数达到接近全微调的性能（U-Net 5.5 dB，扩散模型5.1 dB），且保持语音增强能力。生成式模型在未见测试集（DSD100）上泛化优于判别式模型。

## 🎯 结论与影响

本文证明预训练语音增强模型通过域自适应可有效用于歌声分离，尤其LoRA微调在数据稀缺场景下兼顾性能与参数效率。该工作为跨任务迁移学习提供了新思路，有望推动歌声分离在低资源场景下的实际应用。

## ⚠️ 局限与未解决问题

仅使用MUSDB18单一数据集评估，未在更大规模歌声分离数据集上验证。未报告推理速度或计算开销。LoRA微调的性能提升幅度有限（0.3 dB），与全微调差距明显。未探索其他参数高效微调方法（如Adapter、Prefix Tuning）。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
