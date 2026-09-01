---
title: "PhysWave: Physics-Guided Latent Diffusion Models for Controllable Spatial Audio Generation"
date: 2026-09-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频生成"]
summary: "PhysWave提出物理引导的潜在扩散模型，通过共享路点-字幕表示和声学先验实现可控文本到FOA空间音频生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#声学先验</span> <span class="tag-pill tag-pill-soft">#双耳音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.29549</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.29549" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.29549" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PhysWave提出物理引导的潜在扩散模型，通过共享路点-字幕表示和声学先验实现可控文本到FOA空间音频生成。
</div>

## 👥 作者与机构

**Lingfeng Yao** ¹ · Chenpei Huang · Xingke Yang · Ziye Geng · Changqing Luo · Hao Wang · Jiang Liu · Miao Pan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、空间音频和扩散模型研究者阅读。建议重点阅读第3节方法部分和第4节实验，特别是物理先验的设计和消融实验。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

文本到空间音频生成（如FOA）在游戏和电影行业有巨大需求，但现有方法主要依赖数据驱动，可能违反声源方向与距离的声学关系，且分离描述性和参数控制，导致用户需在易用性和精度间权衡。PhysWave旨在通过物理引导的扩散模型解决这些问题，实现统一控制和物理一致性。

## 💡 核心创新

1. 共享路点-字幕表示统一自然语言和轨迹控制
2. 球谐方向一致性先验增强方向准确性
3. 逆平方距离一致性先验保证距离衰减
4. 构建300K剪辑FOA数据集支持动态空间生成
5. 物理先验可用于推理时无训练空间细化

## 🏗️ 模型架构

PhysWave采用潜在扩散模型，输入为文本和轨迹路点，通过编码器映射到潜在空间，主干为扩散模型（如U-Net），关键模块包括共享路点-字幕表示和两个可微声学先验（球谐方向一致性和逆平方距离一致性），输出为FOA音频。训练时先验作为损失项，推理时可用作引导。

## 📚 数据集

- 自建300K剪辑FOA数据集（训练/评估）

## 📊 实验结果

摘要提到物理先验帮助生成空间一致的FOA音频，同时保持音频质量，但未给出具体数值。分析表明先验在训练中提升空间一致性，并可用于推理时无训练细化。

## 🎯 结论与影响

PhysWave通过物理引导的潜在扩散模型实现了可控文本到FOA生成，统一了自然语言和轨迹控制，并提升了空间一致性。该工作为空间音频生成提供了新思路，有望推动游戏和电影行业的应用，但需进一步验证其泛化能力。

## ⚠️ 局限与未解决问题

摘要未提供定量结果，缺乏与现有方法的对比。数据集为自建，可能缺乏多样性。物理先验的权重和泛化性未详细讨论。推理效率未提及。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-01/">← 返回 2026-09-01 速递</a></div>
