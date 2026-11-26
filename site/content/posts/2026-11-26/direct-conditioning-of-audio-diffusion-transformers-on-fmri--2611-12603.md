---
title: "Direct Conditioning of Audio Diffusion Transformers on fMRI Reveals Cortical Contributions to Sound Reconstruction"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出 MAAS，用 ROI 级 fMRI 响应经区域投影与脑 token 交叉注意力直接条件化 Stable Audio 扩散 Transformer，实现端到端脑活动到音频重建。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脑机接口</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#fMRI</span> <span class="tag-pill tag-pill-soft">#听觉神经科学</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.12603</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.12603" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.12603" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 MAAS，用 ROI 级 fMRI 响应经区域投影与脑 token 交叉注意力直接条件化 Stable Audio 扩散 Transformer，实现端到端脑活动到音频重建。
</div>

## 👥 作者与机构

**Matteo Ciferri** ¹ · Tonio Weidler · Matteo Ferrante · Nicola Toschi · Elia Formisano

**机构**：马斯特里赫特大学 · 哈佛大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合脑机接口、听觉神经科学与音频生成交叉方向的研究者阅读。值得通读，重点看 §3 的 ROI 投影与 cross-attention 条件化设计，以及 §4 中基于听觉神经计算模型的保真度指标与各皮层区域贡献分析。若只关心音频生成主干可略读实验细节。

## 🌍 研究背景

从脑活动重建音频是神经科学与生成模型的交叉难题。现有 brain-to-audio 流程多为两阶段：先把 fMRI 映射到预设刺激表征（如 mel 谱或音频 latent），再送入声码器或扩散模型合成，中间解码器的监督误差会累积。视觉领域已出现直接条件化扩散模型的工作，但音频扩散模型上尚未实现。本文要解决的是：能否跳过外部刺激表征的中间监督，让音频扩散 Transformer 直接以 ROI 级脑响应为条件生成声音。

## 💡 核心创新

1. ROI 级 fMRI 响应经区域专属投影直接条件化音频扩散 Transformer
2. 引入可学习 brain tokens 与专用 cross-attention 通路注入 Stable Audio
3. 提出基于听觉神经计算模型的保真度指标量化各皮层区域贡献

## 🏗️ 模型架构

输入为 7T fMRI 的 ROI 级响应，经各听觉皮层区域专属的线性投影映射为条件向量，并辅以一组可学习 brain tokens。这些条件经专用 cross-attention 通路注入预训练的 Stable Audio 扩散 Transformer（DiT 主干），在去噪过程中调制生成。输出为重建音频波形/latent，端到端训练，无需先监督解码器预测外部刺激表征。摘要未给出参数量。

## 📚 数据集

- 7T fMRI 数据集（训练与评估，具体规模摘要未给出）

## 📊 实验结果

摘要仅定性说明在声学与语义两类评估指标上均优于基线，包括两阶段 fMRI-to-latent 条件化方法，但未给出具体数值。此外提出基于听觉神经计算模型的保真度指标，用于量化单个听觉皮层区域对重建音频表征的贡献，具体消融数字摘要未披露。

## 🎯 结论与影响

最强结论是 ROI 级脑响应可直接条件化音频扩散 Transformer 并优于两阶段流程。这为脑到音频重建提供了绕过中间表征监督的新范式，其区域贡献分析也有助于理解听觉皮层的功能分工。对工业落地而言，目前仍属神经科学探索，离实用脑机音频接口尚远。

## ⚠️ 局限与未解决问题

摘要未报告具体指标数值、参数量与推理开销，对比基线数量有限；7T fMRI 数据规模小且采集昂贵，泛化性存疑；缺少充分消融验证各模块（brain tokens、区域投影）的独立贡献；保真度指标依赖特定听觉计算模型，其有效性需外部验证。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
