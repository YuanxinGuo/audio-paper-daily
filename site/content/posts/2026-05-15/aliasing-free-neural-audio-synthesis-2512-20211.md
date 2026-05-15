---
title: "Aliasing-Free Neural Audio Synthesis"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出可微分抗混叠技术，集成到激活函数和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频合成上超越现有系统。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#抗混叠</span> <span class="tag-pill tag-pill-soft">#神经声码器</span> <span class="tag-pill tag-pill-soft">#神经编解码器</span> <span class="tag-pill tag-pill-soft">#高保真音频合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.20211</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">VocodexElysium.github.io/AliasingFreeNeuralAu…</span></span></a><a class="oc-chip oc-chip-demo" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">VocodexElysium.github.io/AliasingFreeNeuralAu…</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.20211" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.20211" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出可微分抗混叠技术，集成到激活函数和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频合成上超越现有系统。
</div>

## 👥 作者与机构

**Yicheng Gu** ¹ · Junan Zhang · Chaoren Wang · Jerry Li · Zhizheng Wu · Lauri Juvela

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音/音频合成研究者及工程师。建议通读，重点看§3抗混叠模块设计和§4实验部分，尤其是表1-3的指标对比。可先复现测试信号基准评估抗混叠效果。

## 🌍 研究背景

神经声码器和编解码器从声学/潜在表示重建波形，对音频质量至关重要。现有模型在语音上表现自然，但在高保真音乐和歌声合成中，非线性激活函数和上采样层引入严重混叠伪影。尽管数字信号处理中有多种抗混叠技术，但将其集成到神经声码器和编解码器中仍未被充分探索。本文旨在通过可微分抗混叠技术填补这一空白。

## 💡 核心创新

1. 可微分抗混叠激活函数（AntiAliasAct）
2. 可微分抗混叠上采样模块（AntiAliasUpsample）
3. 构建测试信号基准评估抗混叠模块
4. Pupu-Vocoder和Pupu-Codec整体架构

## 🏗️ 模型架构

输入为声学特征（如mel谱）或潜在编码，经主干网络处理。Pupu-Vocoder和Pupu-Codec采用类似HiFi-GAN的生成器结构，但关键创新在于将可微分抗混叠技术集成到激活函数（如LeakyReLU）和上采样层（转置卷积或插值）中。输出为波形样本。参数量未在摘要中提及。

## 📚 数据集

- 语音数据集（训练/评估，未具体命名）
- 歌声数据集（训练/评估，未具体命名）
- 音乐数据集（训练/评估，未具体命名）
- 音频数据集（训练/评估，未具体命名）

## 📊 实验结果

摘要未提供具体数值指标，但声称Pupu-Vocoder和Pupu-Codec在歌声、音乐和音频合成上优于现有系统，在语音上性能相当。实验包括测试信号基准评估抗混叠模块效果，以及主观/客观指标对比。

## 🎯 结论与影响

本文通过可微分抗混叠技术显著提升了神经声码器和编解码器在高保真音乐和歌声合成中的质量，同时保持语音性能。该工作为抗混叠在音频生成中的系统集成提供了新范式，有望推动高保真音频合成在音乐制作和虚拟歌手等工业场景的应用。

## ⚠️ 局限与未解决问题

摘要未提及消融实验或推理效率；未报告参数量和计算复杂度；仅在有限数据集上验证，泛化性待考；未与最新编解码器（如EnCodec、SoundStream）直接对比；抗混叠模块的引入可能增加训练难度。

## 🔗 开源资源

- **项目主页**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>
- **Demo / 试听**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
