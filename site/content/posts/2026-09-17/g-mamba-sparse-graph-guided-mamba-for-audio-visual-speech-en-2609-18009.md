---
title: "G-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech Enhancement"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用稀疏异构图引导 Mamba 主干做轻量音视频语音增强，在 LRS3 噪声条件下达 13.091 dB SI-SDR，计算量仅 3.45 G MACs。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#图神经网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18009</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18009" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18009" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用稀疏异构图引导 Mamba 主干做轻量音视频语音增强，在 LRS3 噪声条件下达 13.091 dB SI-SDR，计算量仅 3.45 G MACs。
</div>

## 👥 作者与机构

**Guo-Ruei Tseng** ¹ · Hung-Shin Lee · Hsin-Min Wang · Berlin Chen

**机构**：台湾大学 · 中央研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做轻量 AVSE、多模态融合与高效序列建模的研究者阅读。建议通读，重点看 §3 的稀疏异构图构建（模态内/跨帧边定义）与 Mamba 主干耦合方式，以及表 2 的 SI-SDR 与 MACs 对比；消融部分需确认图稀疏度与 audio skip 的贡献。

## 🌍 研究背景

音视频语音增强（AVSE）此前多依赖跨模态注意力（如 AV-Conformer、AV-DPRNN）做融合，性能强但计算开销大；轻量方案常用简单拼接或早期融合，关系建模能力弱，在强噪声下跨模态对应不可靠。本文要解决的核心问题是：如何在保持线性复杂度与低 MACs 的前提下，显式建模模态内与跨模态的结构化关系，从而提升轻量 AVSE 的增强质量与鲁棒性。

## 💡 核心创新

1. 稀疏异构图显式建模模态内与跨帧音视频关系
2. 图引导的线性复杂度 Mamba 主干捕获长时上下文
3. audio skip connection 保留频谱细节不牺牲降噪
4. 在 LRS3/VoxCeleb2 上验证结构先验提升鲁棒性与泛化

## 🏗️ 模型架构

输入为含噪语音特征与对应视频帧（唇部 ROI）特征，分别经模态特定编码器提取嵌入。核心模块为稀疏异构图：节点为各模态帧级特征，边由内容自适应注意力生成，包含模态内连接与跨帧音视频连接，经稀疏化后做图消息传递。图输出送入 Mamba 主干，以线性复杂度建模长时时序依赖，并与音频 skip connection 融合以保留频谱细节。最终经解码器重建增强语音波形/谱。整体为轻量设计，推理成本 3.45 G MACs（6.90 G FLOPs）。

## 📚 数据集

- LRS3（训练与评估，音视频语音增强）
- VoxCeleb2（评估，泛化性验证）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | LRS3（noise-only） | 强轻量基线（摘要未给具体值） | **13.091 dB** | 竞争性或更优 |
| MACs | LRS3 | 密集跨注意力基线（未给具体值） | **3.45 G MACs / 6.90 G FLOPs** | 轻量 |

摘要报告在 LRS3 噪声条件下 SI-SDR 达 13.091 dB，与强轻量基线相比具竞争力或更优；在多说话人混杂条件下保持鲁棒，计算成本为 3.45 G MACs（6.90 G FLOPs）。VoxCeleb2 上的结果提示显式结构先验有助于提升鲁棒性、泛化性与计算效率。摘要未给出 PESQ、STOI、WER 等指标，也未提供逐基线数值与消融细节。

## 🎯 结论与影响

最强结论是：稀疏异构图 + Mamba 的线性复杂度组合可在极低 MACs 下取得有竞争力的 AVSE 性能。这为轻量多模态语音增强提供了“结构先验替代密集注意力”的思路，后续可沿图稀疏策略与跨模态对齐方向继续挖掘；工业上利于在端侧/实时场景部署音视频降噪。

## ⚠️ 局限与未解决问题

摘要仅给出 SI-SDR 与 MACs，缺少 PESQ/STOI/WER 等感知与识别指标，也未报告推理延迟与参数量；未列出具体基线数值，难以判断提升幅度；图稀疏化策略、audio skip 的消融未在摘要体现；VoxCeleb2 结论较笼统，跨数据集泛化证据偏弱。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
