---
title: "UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉身份替换"]
summary: "UniSwap提出首个流式联合音视频身份替换框架，通过扩散Transformer同时迁移外观和音色，并采用多种策略实现高效长视频生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉身份替换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#身份替换</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11752</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11752" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11752" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>UniSwap提出首个流式联合音视频身份替换框架，通过扩散Transformer同时迁移外观和音色，并采用多种策略实现高效长视频生成。
</div>

## 👥 作者与机构

**Yuxuan Zhang** ¹ · Haozhong Xiong · Jiayi Song · Jinpeng Yu · Yang Shi · Jiaming Liu · Ruihua Huang · Liwei Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究多模态生成、扩散模型和视频编辑的读者。建议重点阅读方法部分（第3节）和实验部分（第4节），特别是流式生成和身份保持的消融实验。可先看摘要和图表，再深入细节。

## 🌍 研究背景

说话视频中的人物替换需要同时迁移外观和声音，同时保持源视频的动作、场景、语言内容和音视频同步。现有方法通常分别优化视觉和音频模型，难以保证音视频一致性。此外，缺乏跨身份对齐的训练数据，且长视频生成存在效率问题。UniSwap旨在通过统一的音视频扩散Transformer解决这些问题，实现流式联合身份替换。

## 💡 核心创新

1. 提出swap-and-reconstruct训练策略，解决跨身份数据稀缺
2. 引入In-context Pretraining实现联合替换预训练
3. 设计Conditional Streaming Adaptation支持块级因果KV缓存流式生成
4. 采用Efficient Self-forcing DMD减少采样步数至3步
5. 提出Feature-RoPE Decomposition保持长序列位置编码稳定

## 🏗️ 模型架构

UniSwap采用音频-视觉扩散Transformer作为主干，输入源视频、参考图像和参考语音片段。通过swap-and-reconstruct训练，模型学习去除身份并重建。推理时，采用块级因果KV缓存实现流式生成，并使用DMD蒸馏减少采样步数。Multi-LoRA切换共享冻结主干，Feature-RoPE分解保持位置编码稳定。

## 📊 实验结果

实验表明UniSwap在音视频同步、身份保持、流式效率和长视频稳定性方面表现优异，但摘要未提供具体数值。

## 🎯 结论与影响

UniSwap首次实现流式联合音视频身份替换，通过统一框架和多种优化策略，在保持内容的同时高效迁移身份。该工作为多模态生成和视频编辑提供了新思路，有望推动实时虚拟人应用。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但可能包括：训练数据多样性不足、长视频生成中的累积误差、以及身份保持的鲁棒性。此外，缺乏与现有方法的定量对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
