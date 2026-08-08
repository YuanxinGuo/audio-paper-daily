---
title: "LILAC: An Idempotent Neural Speech Codec"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编码"]
summary: "LILAC 提出一种构造性幂等的 24kHz 语音编解码器，在 0.75 kbit/s 下重编码不改变 token，质量接近 SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#幂等性</span> <span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#低比特率</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05727</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05727" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05727" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>LILAC 提出一种构造性幂等的 24kHz 语音编解码器，在 0.75 kbit/s 下重编码不改变 token，质量接近 SOTA。
</div>

## 👥 作者与机构

**June Young Yi** ¹ · Dongwook Lee · Jiheum Yeom · Sungroh Yoon

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编码、语音生成与编辑方向的研究者。建议重点阅读第 3 节（方法）与第 4 节（实验），尤其是幂等性构造与质量对比部分。可先看摘要与结论，再深入方法细节。

## 🌍 研究背景

神经音频编解码器（如 EnCodec、SoundStream）被广泛用于语音生成与编辑，作为 token 接口。然而现有编解码器不具备幂等性：解码-重编码会改变 token，平均至少 15% 的 token 被重写，这阻碍了其在多阶段流水线中的稳定使用。本文旨在设计一种构造性幂等的编解码器，确保任何有效 token 流解码后重编码仍得到相同 token，同时保持低比特率下的高质量。

## 💡 核心创新

1. 构造性幂等：通过设计保证重编码 token 不变
2. 全卷积架构：24kHz 采样率，9.375 Hz 帧率
3. 极低比特率：0.75 kbit/s 下达到 UTMOS 4.14/4.24
4. 与 SOTA 子 1 kbit/s 编解码器质量相当

## 🏗️ 模型架构

LILAC 采用全卷积架构，输入 24kHz 语音，通过编码器提取 9.375 Hz 的 token 序列，量化后以 0.75 kbit/s 传输。解码器将 token 映射回波形。关键设计在于编码器-解码器对的幂等性约束，确保任何 token 流解码后重编码得到相同 token。具体模块未在摘要中详述，但强调全卷积与构造性幂等。

## 📚 数据集

- LibriSpeech（评估）
- LibriTTS-R（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| UTMOS | LibriSpeech | SOTA sub-1 kbit/s codecs (未给出具体值) | **4.14** | N/A |
| UTMOS | LibriTTS-R | SOTA sub-1 kbit/s codecs (未给出具体值) | **4.24** | N/A |

摘要仅给出 UTMOS 分数，未提供与基线的具体差值。LILAC 在 LibriSpeech 和 LibriTTS-R 上分别达到 4.14 和 4.24，与 SOTA 子 1 kbit/s 编解码器相当。幂等性方面，所有配置下 token 重写率均为 0%，而基线平均至少 15%。

## 🎯 结论与影响

LILAC 通过构造性幂等解决了神经编解码器在重编码时 token 不稳定的问题，同时保持低比特率下的高质量。这一特性使其更适合作为语音生成流水线中的稳定 token 接口，可能推动多阶段语音处理系统的可靠性。对工业界，可减少因重编码导致的误差累积。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题：未报告推理延迟或计算复杂度；仅评估 UTMOS，缺乏主观 MOS 或下游任务（如 TTS）评估；未与更高比特率编解码器对比；幂等性构造可能限制模型容量或灵活性。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
