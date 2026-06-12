---
title: "BASENet: Band-Adapted Speech Enhancement Network with Cross-Band Attention"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出BASENet，按Bark尺度分配不同容量编码器，结合跨频带注意力，以0.83M参数在VoiceBank+DEMAND上达到3.55 PESQ。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Bark尺度</span> <span class="tag-pill tag-pill-soft">#跨频带注意力</span> <span class="tag-pill tag-pill-soft">#轻量化</span> <span class="tag-pill tag-pill-soft">#因果模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.12662</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.12662" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.12662" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BASENet，按Bark尺度分配不同容量编码器，结合跨频带注意力，以0.83M参数在VoiceBank+DEMAND上达到3.55 PESQ。
</div>

## 👥 作者与机构

**Damien Martins Gomes** ¹ · Fran\c{c}ois Capman

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和轻量化模型研究者。建议通读，重点看§3.2跨频带注意力和§4.2参数效率对比。可复现其Bark频带划分策略。

## 🌍 研究背景

现有语音增强模型通常对所有频率采用相同容量，忽略了人耳听觉的非均匀频谱分辨率。之前SOTA如Conv-TasNet、FullSubNet等虽性能好但参数量大。本文旨在设计频率自适应架构，在极低参数量下实现高PESQ，并支持因果模式用于实时流式处理。

## 💡 核心创新

1. Bark尺度容量分配编码器
2. 跨频带注意力模块（线性复杂度）
3. 密集连接倒残差块
4. 因果变体支持实时流式

## 🏗️ 模型架构

输入频谱经Bark滤波器组划分为24个频带，每个频带送入不同深度的编码器（低频深、高频浅），编码器由密集连接的倒残差块和卷积循环网络组成。之后跨频带注意力模块通过频率池化压缩表示，计算频带间依赖。最后解码器重构时域波形。总参数量0.83M，MACs 7.3G。

## 📚 数据集

- VoiceBank+DEMAND（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | DCCRN 3.27 | **3.55** | +0.28 |
| STOI (%) | VoiceBank+DEMAND | DCCRN 93.6 | **96.0** | +2.4 |

BASENet以0.83M参数达到3.55 PESQ和96% STOI，超越所有参数量大于它的方法。因果变体3.44 PESQ仍优于多数非因果基线。消融实验验证了Bark频带分配和跨频带注意力的有效性。

## 🎯 结论与影响

BASENet证明频率自适应容量分配可大幅提升参数效率，为资源受限设备上的实时语音增强提供了新思路。后续可探索更精细的听觉尺度划分或扩展到其他音频任务。

## ⚠️ 局限与未解决问题

仅在VoiceBank+DEMAND单一数据集上评估，未见跨数据集泛化实验。未报告推理延迟或实际设备运行速度。因果变体性能下降未充分分析。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
