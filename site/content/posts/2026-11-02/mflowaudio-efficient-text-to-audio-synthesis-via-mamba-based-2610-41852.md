---
title: "MFlowAudio: Efficient Text-to-Audio Synthesis via Mamba-based Stateful Flow Matching"
date: 2026-11-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "用TCMamba主干结合状态化流匹配，实现线性复杂度、可流式的文本到音频合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#流式生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.41852</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/spaces/mflowaudio/MFlowAudio" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 spaces/mflowaudio/MFlowAudio</span></span></a><a class="oc-chip oc-chip-demo" href="https://huggingface.co/spaces/mflowaudio/MFlowAudio" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">🤗 spaces/mflowaudio/MFlowAudio</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.41852" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.41852" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/spaces/mflowaudio/MFlowAudio" target="_blank" rel="noopener">🤗 HuggingFace</a><a class="rsrc rsrc-demo" href="https://huggingface.co/spaces/mflowaudio/MFlowAudio" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用TCMamba主干结合状态化流匹配，实现线性复杂度、可流式的文本到音频合成。
</div>

## 👥 作者与机构

**Hao Dai** ¹ · Panyu Chen · Jagmohan Chauhan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTA/扩散加速与流式音频生成的研究者与工程团队阅读。建议通读：重点看§3的TCMamba双扫描结构与Stateful Flow Matching的O(1)缓存推导，以及§4的引导机制；实验部分先看效率对比表与1.8s流式延迟的评测设置，再核对与Transformer基线的公平性。

## 🌍 研究背景

当前文本到音频生成主流采用Transformer扩散/流匹配模型（如AudioLDM、Tango类），生成保真度高，但自注意力对长音频呈二次复杂度，长时合成与流式部署代价高。已有线性注意力、状态空间模型在语音/音乐生成中尝试替代注意力，但多聚焦离线整段生成，缺少对跨通道谐波结构与流式缓存的系统处理。本文要解决长时音频合成中的计算瓶颈与流式生成的一致性问题。

## 💡 核心创新

1. 提出TCMamba主干：TimeMamba做长程因果建模，ChannelMamba建模跨通道谐波相关
2. 提出Stateful Flow Matching，支持分块训练与O(1)缓存流式生成
3. 设计引导机制，缓解提示语义切换导致的向量场碰撞
4. 线性复杂度替代自注意力，实现14.5%以上生成加速

## 🏗️ 模型架构

输入为文本提示编码与潜空间音频表示，主干为自研TCMamba：由TimeMamba沿时间轴做双向/因果扫描以线性复杂度捕获长程依赖，ChannelMamba在通道维建模谐波等跨通道相关性，二者构成双扫描结构。训练采用Stateful Flow Matching，将连续时间流匹配离散为分块状态传递，使推理时仅需常数缓存即可流式生成；引导机制在采样中对条件向量场做修正以处理提示语义突变。输出为潜表示再经解码器还原波形。摘要未给出参数量。

## 📊 实验结果

摘要仅给出效率类结论：相对Transformer扩散基线生成加速超过14.5%，流式合成保持1.8秒恒定延迟，生成保真度与SOTA基线相当。未披露具体数据集、FAD/KL等客观指标数值及主观MOS结果，也无消融细节，需查阅正文核实对比公平性与评测规模。

## 🎯 结论与影响

最强结论是线性复杂度主干加状态化流匹配可在不牺牲保真度的前提下显著提速并支持恒定延迟流式TTA。这为长时音频与实时交互式生成提供了可复用范式，对工业端实时配音、交互式音频内容生产有直接意义。

## ⚠️ 局限与未解决问题

摘要缺少具体客观指标、数据集与主观评测细节，难以判断与基线的公平性；未报告显存占用与不同音频时长下的扩展性曲线；引导机制的有效性缺少消融；流式1.8秒延迟对交互场景仍偏高，未讨论进一步压缩空间。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/spaces/mflowaudio/MFlowAudio>
- **Demo / 试听**：<https://huggingface.co/spaces/mflowaudio/MFlowAudio>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-02/">← 返回 2026-11-02 速递</a></div>
