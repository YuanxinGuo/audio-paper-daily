---
title: "HarmonicAttack: An Adaptive Cross-Domain Audio Watermark Removal"
date: 2026-05-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印移除"]
summary: "提出HarmonicAttack，一种无需访问目标水印检测器的自适应跨域音频水印移除方法，在多个SOTA水印方案上达到高攻击成功率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印移除</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#跨域泛化</span> <span class="tag-pill tag-pill-soft">#AI生成音频安全</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.21577</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.21577" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.21577" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出HarmonicAttack，一种无需访问目标水印检测器的自适应跨域音频水印移除方法，在多个SOTA水印方案上达到高攻击成功率。
</div>

## 👥 作者与机构

**Kexin Li** ¹ · Xiao Hu · Ilya Grishchenko · David Lie

**机构**：多伦多大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、水印鲁棒性评估方向的研究者。建议通读，重点看§3方法设计和§4实验部分，特别是跨域泛化实验（表2/3）。可复现其开源代码验证攻击效果。

## 🌍 研究背景

AI生成音频的滥用（如虚假信息、语音克隆欺诈）促使水印技术成为关键防御手段。然而，现有水印移除攻击通常假设可访问目标水印检测器，这在实际中不现实，导致对水印鲁棒性的过度自信。本文旨在提出一种更实用的黑盒攻击方法，仅需少量原始和水印样本即可训练通用移除模型，并验证其跨域泛化能力。

## 💡 核心创新

1. 无需访问目标水印检测器的黑盒攻击设置
2. 自适应跨域训练策略，支持分布外泛化
3. 在AudioSeal、WavMark等四种SOTA水印上均显著优于基线

## 🏗️ 模型架构

输入为原始音频和水印音频的配对，通过一个基于卷积和Transformer的混合网络（类似U-Net结构）处理，中间包含自适应特征调制模块，输出移除水印后的音频。模型参数量未在摘要中给出。

## 📚 数据集

- LibriSpeech（训练，用于生成水印样本）
- VCTK（评估，跨域测试）
- FMA（评估，跨域测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ASR（攻击成功率） | VCTK | 最佳基线 38% | **92%** | +54% |
| ASR | FMA | 最佳基线 44%（WavMark） | **100%** | +56% |

在VCTK上，HarmonicAttack对AudioMarkNet的ASR达92%，远超最佳基线38%；在FMA上，对所有水印方案均达100% ASR，而最佳基线仅对WavMark达44%。攻击后音频保持高感知质量（未给出具体MOS值）。跨域泛化实验表明，即使训练集（LibriSpeech）与测试集分布不同，性能下降极小。

## 🎯 结论与影响

HarmonicAttack证明了在无需访问目标检测器的黑盒设置下，音频水印可被高效移除，且跨域泛化能力强。该工作警示现有水印方案可能过于脆弱，推动设计更鲁棒的水印算法。对工业界而言，部署水印时需考虑此类攻击的威胁。

## ⚠️ 局限与未解决问题

摘要未报告攻击的计算开销或推理延迟；未提供感知质量的具体指标（如PESQ、SI-SDR）；仅针对四种水印方案，更多方案（如DWT-DCT）未测试；训练需原始-水印配对，实际中可能难以获取。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-20/">← 返回 2026-05-20 速递</a></div>
