---
title: "KVAE: Family of Tokenizers for Multimodal Generative Models"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "KVAE 系列 tokenizer 覆盖音频、图像、视频，在重建和生成指标上匹配或超越多个前沿开源 tokenizer，并公开训练细节与代码。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态生成</span> <span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#潜在扩散模型</span> <span class="tag-pill tag-pill-soft">#音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05798</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/kandinskylab/kvae" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">kandinskylab/kvae</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05798" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05798" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/kandinskylab/kvae" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>KVAE 系列 tokenizer 覆盖音频、图像、视频，在重建和生成指标上匹配或超越多个前沿开源 tokenizer，并公开训练细节与代码。
</div>

## 👥 作者与机构

**Andrey Shutkin** ¹ · Denis Parkhomenko · Ivan Kirillov · Kirill Chernyshev · Kirill Malakhov · Ilia Vasiliev · Ilia Trushkin · Valeriya Kobenko · … 等 6 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态生成、潜在扩散模型和 tokenizer 设计的研究者。建议重点阅读第 3 节（模型架构）和第 4 节（实验对比），可先看表 2 和表 3 了解性能差异。若关注音频生成，可细读 KVAE-Audio 部分。

## 🌍 研究背景

潜在扩散模型（LDM）依赖 tokenizer 将输入信号压缩为潜在表示，tokenizer 的质量直接影响生成速度和样本质量。现有开源 tokenizer 如 VAE 在重建精度、压缩率或训练稳定性上存在不足，且缺乏系统的设计选择和训练细节公开。本文旨在提出一系列高性能 tokenizer（KVAE），覆盖音频、图像和视频，为后续文本条件生成提供坚实基础，并通过全面对比验证其有效性。

## 💡 核心创新

1. 提出 KVAE-Audio，连续全频带 48 kHz tokenizer，50 Hz 潜在率，64 通道
2. 提出 KVAE-3D，两种因果视频 tokenizer，支持 4x16x16 和 4x8x8 压缩
3. 提出 KVAE-2D，图像 tokenizer，8 倍压缩，32 通道
4. 公开训练细节、模型选择方法和设计选择消融
5. 在重建和生成指标上匹配或超越多个前沿开源 tokenizer

## 🏗️ 模型架构

KVAE 系列基于自编码器架构，采用编码器-解码器结构。KVAE-Audio 输入 48 kHz 波形，通过卷积编码器下采样至 50 Hz 潜在表示，通道数为 64，解码器对称上采样重建波形。KVAE-3D 为因果视频 tokenizer，分别实现 4x16x16 和 4x8x8 的时间-空间压缩，编码器使用 3D 卷积，解码器进行相应上采样。KVAE-2D 处理图像，8 倍空间压缩，32 通道。所有模型均采用潜在扩散训练目标，并可能包含残差连接和归一化层。具体细节未在摘要中给出。

## 📊 实验结果

摘要中未提供具体数值，但声称在重建指标（PSNR、LPIPS、PESQ 等）和生成指标（Frechet Distance、CLIP score、CLAP score 等）上匹配或超越多个前沿开源 tokenizer，包括 Wan-2.2、HunyuanVideo-1.5、FLUX.2、MovieGen、StableAudio 和 MMAudio。主观评估（side-by-side）也支持这一结论。

## 🎯 结论与影响

KVAE 系列 tokenizer 在多个模态上展示了与前沿开源模型相当或更优的性能，并公开了训练细节和设计选择，有助于社区复现和进一步研究。该工作为潜在扩散模型提供了更可靠的 tokenizer 基础，可能推动多模态生成的发展。工业上，高质量的 tokenizer 可提升生成效率和质量，降低计算成本。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但作为 tokenizer 报告，可能缺乏对下游任务（如文本到音频生成）的端到端评估，且未提供推理延迟或参数量等效率指标。对比的 baseline 虽多，但可能未涵盖所有最新模型。此外，训练细节虽公开，但复现成本可能较高。

## 🔗 开源资源

- **代码**：<https://github.com/kandinskylab/kvae>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
