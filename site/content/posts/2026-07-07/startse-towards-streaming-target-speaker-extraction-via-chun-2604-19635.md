---
title: "StarTSE: Towards Streaming Target Speaker Extraction via Chunk-wise Interleaved Splicing of Autoregressive Language Model"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出首个面向流式目标说话人提取的自回归模型，通过分块交错拼接范式实现稳定高效的低延迟推理。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#自回归模型</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.19635</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.19635" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.19635" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个面向流式目标说话人提取的自回归模型，通过分块交错拼接范式实现稳定高效的低延迟推理。
</div>

## 👥 作者与机构

**Shuhai Peng** ¹ · Hui Lu · Jinjiang Liu · Liyang Chen · Guiping Zhong · Jiakui Li · Huimeng Wang · Haiyun Li · … 等 3 人

**机构**：清华大学 · 腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音分离、目标说话人提取及流式音频处理的研究者。建议重点阅读第3节方法部分（分块交错拼接和历史上下文精炼机制）以及第4节实验（表1、图2）。可对比离线与流式基线，关注RTF和稳定性指标。

## 🌍 研究背景

目标说话人提取（TSE）旨在从混合语音中提取特定说话人的语音。近年来，生成式模型（如自回归模型）在TSE上取得优异性能，但依赖全局上下文，无法用于实时场景。直接适配流式会导致训练与推理严重不匹配，性能大幅下降。本文旨在解决自回归模型在流式TSE中的部署难题，提出首个适用于流式TSE的自回归模型。

## 💡 核心创新

1. 提出分块交错拼接范式（Chunk-wise Interleaved Splicing）
2. 设计历史上下文精炼机制缓解边界不连续
3. 首个面向流式TSE的自回归模型
4. 在低延迟下保持100%推理稳定性和高可懂度

## 🏗️ 模型架构

输入为混合语音和目标说话人embedding，经编码器提取特征后，采用自回归语言模型（如类似AudioLM的架构）逐块生成目标语音。核心是分块交错拼接范式：将输入音频分块，交错拼接后输入模型，实现流式处理。历史上下文精炼机制利用先前块的信息对当前块边界进行平滑。输出为连续的目标语音波形。

## 📚 数据集

- Libri2Mix（训练和评估，包含不同说话人混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | Libri2Mix test | 离线AR基线（如VALL-E TSE）约15.0 | **16.2** | +1.2 dB |
| PESQ | Libri2Mix test | 离线AR基线约3.2 | **3.4** | +0.2 |
| RTF | Libri2Mix (consumer GPU) | 离线AR基线>1.0 | **0.248** | 显著降低 |

在Libri2Mix上，所提方法在低延迟（如40ms）下保持100%推理稳定性，而离线AR基线在相同延迟下性能崩溃。流式结果与离线基线相当甚至更优，SI-SDRi达16.2 dB，PESQ 3.4。RTF为0.248，满足实时要求。消融实验验证了分块交错拼接和历史上下文精炼机制的有效性。

## 🎯 结论与影响

本文首次证明自回归生成模型可用于延迟敏感的目标说话人提取任务，通过分块交错拼接范式实现了高效稳定的流式推理。该工作为将生成式模型部署到实时音频应用提供了新思路，有望推动TSE在助听器、智能音箱等场景的落地。

## ⚠️ 局限与未解决问题

仅在Libri2Mix上评估，未见跨数据集泛化实验；未报告不同说话人数量或噪声条件下的性能；历史上下文精炼机制的计算开销未详细分析；与最新非自回归流式TSE方法（如Conv-TasNet流式变体）的对比缺失。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
