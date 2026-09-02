---
title: "U-PAST: A Phase-Aware Audio Spectrogram Transformer-U-Net for Single-Channel Speech Enhancement"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出U-PAST，一种在复数谱域进行自注意力建模的Transformer-U-Net混合架构，用于单通道语音增强，在参数效率上优于大型基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#U-Net</span> <span class="tag-pill tag-pill-soft">#复数谱</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.00431</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.00431" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.00431" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出U-PAST，一种在复数谱域进行自注意力建模的Transformer-U-Net混合架构，用于单通道语音增强，在参数效率上优于大型基线。
</div>

## 👥 作者与机构

**Cao Duong Ly** ¹ · J\"orn Anem\"uller

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和音频Transformer研究者阅读。值得通读，重点看§3的架构设计和§4的实验对比。可先看§3.2的tokenization和§4.3的跨数据集泛化结果。

## 🌍 研究背景

语音增强中，CNN虽广泛使用，但通过连续卷积和池化只能间接捕获长距离时频依赖。Transformer在音频领域已展现长程建模能力，但现有AST仅处理幅度谱，忽略相位信息。本文旨在利用复数谱的相位信息，结合Transformer和U-Net，实现更优的增强效果。

## 💡 核心创新

1. 在复数STFT域进行tokenization，同时利用幅度和相位信息
2. 采用U-Net风格解码器重建增强复数谱，保留细节
3. 提出四种参数规模变体，最小1.17M，最大2.40M
4. 在多种失配条件下评估，验证鲁棒性

## 🏗️ 模型架构

输入为复数STFT，经tokenization后送入多层Transformer编码器，编码器通过自注意力建模长程依赖，然后由U-Net风格解码器逐步上采样并融合编码器特征，最终输出增强的复数谱。模型参数范围1.17M-2.40M，最大变体U-PAST-H。

## 📚 数据集

- DNS Challenge（训练/评估）
- VoiceBank-DEMAND（训练/评估）
- LibriMix（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | 声学失配条件 | 未明确 | **最佳** | 优于所有评估模型 |
| SI-SDR | 其余三种条件 | 大型卷积和时域基线 | **落后0.26-0.63 dB** | -0.26~-0.63 dB |
| DNSMOS | 数据集失配条件 | 未明确 | **最强** | 最佳感知质量 |

U-PAST在声学失配条件下取得最佳SI-SDR，在其余条件下接近大型基线，但参数少得多。在数据集失配下DNSMOS最佳。U-PAST-H为最强变体，性能与参数权衡良好。

## 🎯 结论与影响

U-PAST证明复数谱域Transformer-U-Net能高效增强语音，以极小参数达到接近大型模型的性能，为低资源场景提供新选择。未来可探索更大规模或结合其他任务。

## ⚠️ 局限与未解决问题

摘要未提供具体数值，缺乏与SOTA的详细对比。未提及推理延迟或计算量。未进行消融研究验证各组件贡献。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
