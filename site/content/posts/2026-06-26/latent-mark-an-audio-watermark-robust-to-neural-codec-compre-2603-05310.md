---
title: "Latent-Mark: An Audio Watermark Robust to Neural Codec Compression"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "提出Latent-Mark，首个在神经音频编解码器压缩下鲁棒的零比特音频水印框架，通过将水印嵌入编解码器不变潜在空间实现。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#潜在空间</span> <span class="tag-pill tag-pill-soft">#跨编解码器优化</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05310</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05310" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05310" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Latent-Mark，首个在神经音频编解码器压缩下鲁棒的零比特音频水印框架，通过将水印嵌入编解码器不变潜在空间实现。
</div>

## 👥 作者与机构

**Yen-Shan Chen** ¹ · Shih-Yu Lai · Ying-Jung Tsou · Yi-Cheng Lin · Bing-Yu Chen · Yun-Nung Chen · Hung-yi Lee · Shang-Tse Chen ✉

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频水印、神经编解码、生成式音频安全领域的研究者。建议通读，重点看§3方法（潜在空间嵌入与跨编解码器优化）和§4实验（零样本迁移与DSP鲁棒性）。可复现代码（若开源）验证跨编解码器效果。

## 🌍 研究背景

现有音频水印技术对传统DSP攻击（如MP3压缩、重采样）鲁棒，但面对现代神经音频编解码器（如EnCodec、SoundStream）时脆弱，因为编解码器作为噪声滤波器会丢弃水印嵌入的不可感知波形变化。本文旨在解决神经编解码压缩下的水印鲁棒性问题，提出首个针对该场景的零比特水印框架。

## 💡 核心创新

1. 潜在空间水印嵌入：在编解码器编码后的潜在表示中诱导可检测方向偏移
2. 跨编解码器优化：联合优化多个代理编解码器，学习共享潜在不变量
3. 自然音频流形约束：确保扰动不可感知且不偏离真实音频分布

## 🏗️ 模型架构

输入音频波形 → 通过多个代理神经编解码器（如EnCodec、SoundStream）编码得到潜在表示 → 优化波形使潜在表示产生特定方向偏移（通过梯度下降）→ 同时施加流形约束保持感知质量 → 解码时从潜在表示中检测偏移方向提取水印。无需修改编解码器，仅需优化输入波形。

## 📚 数据集

- LibriSpeech（训练/评估，用于语音水印测试）
- MUSDB18（评估，用于音乐水印测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 比特准确率 | LibriSpeech（EnCodec压缩） | AudioSeal 50.0% | **99.2%** | +49.2% |
| 比特准确率 | LibriSpeech（SoundStream压缩） | AudioSeal 50.0% | **98.5%** | +48.5% |
| 比特准确率 | MUSDB18（EnCodec压缩） | AudioSeal 50.0% | **97.8%** | +47.8% |

Latent-Mark在多个未见过的神经编解码器上实现零样本迁移，比特准确率>97%，而基线方法（AudioSeal）仅50%（随机猜测）。同时保持对传统DSP攻击（MP3、重采样等）的竞争力，且感知质量接近原始音频（PESQ>4.0）。消融实验验证了跨编解码器优化的必要性。

## 🎯 结论与影响

Latent-Mark首次证明通过将水印嵌入编解码器不变潜在空间可实现对神经压缩的鲁棒性，为音频水印在生成式AI时代提供了新范式。未来可扩展至多比特水印、对抗更强编解码器，并推动数字内容版权保护在流媒体和AIGC场景的落地。

## ⚠️ 局限与未解决问题

仅针对零比特水印，未探索多比特容量；依赖多个代理编解码器，计算开销较大；未测试对最新编解码器（如DAC）的鲁棒性；未提供推理延迟和参数量；流形约束可能限制水印强度。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
