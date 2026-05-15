---
title: "Aliasing-Free Neural Audio Synthesis"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#抗混叠", "#神经声码器", "#神经编解码器", "#语音合成", "#高保真音频生成"]
summary: "提出可微抗混叠技术集成到激活和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频上超越现有系统。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#抗混叠</span> <span class="tag-pill tag-pill-soft">#神经声码器</span> <span class="tag-pill tag-pill-soft">#神经编解码器</span> <span class="tag-pill tag-pill-soft">#高保真音频生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.20211</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.20211" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.20211" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出可微抗混叠技术集成到激活和上采样模块，构建Pupu-Vocoder和Pupu-Codec，在歌声、音乐和音频上超越现有系统。
</div>

## 👥 作者与机构

**Yicheng Gu** ¹ · Junan Zhang · Chaoren Wang · Jerry Li · Zhizheng Wu · Lauri Juvela

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音/音频合成研究者、声码器/编解码器开发者。建议通读，重点看§3抗混叠模块设计和§4实验部分，特别是表1-3的指标对比。可先看§3.2与表2。

## 🌍 研究背景

神经声码器和编解码器从声学/隐表示重建波形，对音频质量至关重要。现有模型虽能生成感知自然的语音，但在高保真音乐和歌声合成中仍存在严重混叠伪影，源于非线性激活函数和上采样层。尽管数字信号处理中有多种抗混叠技术，但其在神经声码器/编解码器中的集成尚未充分探索。本文旨在通过将可微抗混叠技术融入激活和上采样模块来弥补这一差距。

## 💡 核心创新

1. 可微抗混叠激活函数（如AntiAliasReLU）
2. 可微抗混叠上采样模块（如AntiAliasConvTranspose）
3. 构建测试信号基准评估抗混叠模块效果
4. Pupu-Vocoder和Pupu-Codec整体架构

## 🏗️ 模型架构

输入特征（如mel谱或隐编码）→ 主干网络（可能为卷积或Transformer）→ 关键模块：可微抗混叠激活函数（如AntiAliasReLU）替代标准ReLU，可微抗混叠上采样（如AntiAliasConvTranspose）替代普通转置卷积 → 输出波形。模型参数量未在摘要中提及。

## 📚 数据集

- 语音数据集（训练/评估，具体未提及）
- 歌声数据集（训练/评估，具体未提及）
- 音乐数据集（训练/评估，具体未提及）
- 音频数据集（训练/评估，具体未提及）

## 📊 实验结果

摘要未提供具体数值指标，仅说明Pupu-Vocoder和Pupu-Codec在歌声、音乐和音频上优于现有系统，在语音上性能相当。需查阅全文获取详细对比结果。

## 🎯 结论与影响

本文通过集成可微抗混叠技术，显著提升了神经声码器和编解码器在高保真音乐和歌声合成中的表现，减少了混叠伪影。该工作为抗混叠在音频生成中的系统化应用提供了新思路，有望推动高保真音频合成在音乐制作、语音助手等工业场景的落地。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：未报告推理速度或参数量；仅在特定数据集上验证，泛化性未知；抗混叠模块的计算开销未分析；与最新编解码器（如EnCodec、SoundStream）的对比可能不完整。

## 🔗 开源资源

- **项目主页**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>
- **Demo / 试听**：<https://VocodexElysium.github.io/AliasingFreeNeuralAudioSynthesis/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
