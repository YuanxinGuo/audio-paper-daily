---
title: "Optimising Neural Speech Codecs for 300bps Communication using Reinforcement Learning"
date: 2026-05-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编码"]
summary: "提出ClariCodec，在300bps超低比特率下通过强化学习优化WER，实现3.55% WER。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#超低比特率语音编码</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#词错误率优化</span> <span class="tag-pill tag-pill-soft">#神经编解码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.19541</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.19541" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.19541" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ClariCodec，在300bps超低比特率下通过强化学习优化WER，实现3.55% WER。
</div>

## 👥 作者与机构

**Junyi Wang** ¹ · Chi Zhang · Jing Qian · Haifeng Luo · Hao Wang · Zengrui Jin · Chao Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编码、低带宽通信领域的研究者阅读。建议重点读§3的RL优化框架和§4的实验结果，尤其是表1的WER对比。可先看摘要和结论了解核心贡献。

## 🌍 研究背景

在卫星、水下等带宽受限场景，语音需以极低比特率传输，此时可懂度是首要目标。现有神经编解码器（如SoundStream、EnCodec）在超低比特率下因感知损失分配比特给细节，导致WER显著下降。本文旨在解决300bps下可懂度退化问题。

## 💡 核心创新

1. 将量化建模为随机策略，支持RL优化
2. 使用WER驱动奖励微调解码器，冻结声学重建流水线
3. 在300bps达到3.55% WER，优于更高比特率编解码器

## 🏗️ 模型架构

输入语音经编码器提取特征，量化器采用随机策略（Gumbel-Softmax）输出离散码字，解码器重建波形。编码器基于卷积网络，解码器使用SoundStream结构。RL阶段仅微调解码器，冻结编码器和量化器。参数量未提及。

## 📚 数据集

- LibriSpeech（训练/评估，test-clean和test-other）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER (%) | LibriSpeech test-clean | ClariCodec w/o RL 4.64 | **3.55** | -1.09 |
| WER (%) | LibriSpeech test-other | 未给出 | **10.4** | N/A |

ClariCodec在300bps下，无RL时test-clean WER为4.64%，已与更高比特率编解码器竞争。RL微调后WER降至3.55%（test-clean）和10.4%（test-other），相对降低23%，且感知质量保持。未提供与其他编解码器在相同比特率下的直接对比。

## 🎯 结论与影响

ClariCodec通过RL优化WER，在300bps超低比特率下实现了极低WER，证明RL可有效提升可懂度。该工作为极端带宽场景的语音通信提供了新思路，有望推动卫星、水下通信的实用化。

## ⚠️ 局限与未解决问题

仅在LibriSpeech上评估，未见跨数据集或噪声环境泛化实验；未报告推理延迟或模型大小；RL微调对感知质量的影响仅定性描述，缺乏客观指标（如PESQ）验证。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-20/">← 返回 2026-05-20 速递</a></div>
