---
title: "NeuroCodec: EEG-Guided Latent-Domain Generative Model for High-Fidelity Target Speaker Extraction"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "首个在神经音频编解码器潜空间做EEG引导目标说话人提取的生成式框架，支持44.1kHz宽带重建与因果流式。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#脑电听觉注意解码</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#生成模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29815</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29815" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29815" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个在神经音频编解码器潜空间做EEG引导目标说话人提取的生成式框架，支持44.1kHz宽带重建与因果流式。
</div>

## 👥 作者与机构

**Julian Silva** ¹ · Jaliya Kodithuwakku · Navindu Sirimanna · Shaveen Herath · Wageesha N. Manamperi · Joshua P. Kulasingham

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TSE、神经引导听觉、音频生成的研究者与助听器工程团队阅读。建议通读：重点看§3的图卷积EEG编码器与Mamba跨模态融合、§4六阶段训练课程，以及表2感知指标与20人听测结果；流式部分看因果公式化一节。

## 🌍 研究背景

EEG引导的TSE是神经引导听觉注意解码的核心任务，助听器场景需求明确。此前SOTA如M3ANet、以及基于AAD的时频掩码方法（如SEPFormer式掩码估计）依赖时频掩码，在时频重叠区保真度低，且多受限于窄带音频（如16kHz以下），难以满足高保真助听需求。本文要解决的是：如何在潜空间生成式框架下实现宽带、高保真的EEG引导目标说话人提取。

## 💡 核心创新

1. 首个在神经音频编解码器潜空间做EEG引导TSE的生成框架
2. 图卷积建模EEG空间依赖 + Mamba时序建模的跨模态融合
3. 六阶段训练课程：潜重建→多尺度谱→对抗目标渐进稳定训练
4. 支持44.1kHz、20kHz谱内容的宽带重建
5. 给出因果流式公式化，面向实时助听处理

## 🏗️ 模型架构

输入为多通道EEG与混合语音；语音经神经音频编解码器编码为离散/连续潜表示，EEG分支用图卷积网络建模电极间空间依赖，随后通过注意力机制做EEG-语音跨模态融合，并以Mamba模块进行长时序建模，输出目标说话人潜表示，再由编解码器解码为44.1kHz波形。训练采用六阶段课程，逐步引入潜域重建损失、多尺度频谱损失与对抗损失。摘要未给出参数量。

## 📚 数据集

- Cocktail Party数据集（评估）
- KUL数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 主观听测平均分（20人） | Cocktail Party / KUL | M3ANet 49.63 | **NeuroCodec 82.24** | +32.61 |

摘要称在Cocktail Party与KUL上多项感知指标优于基线，但未给出SI-SDR、PESQ、WER等具体数值，仅报告20人听测平均分82.24对49.63。另指出可实现44.1kHz重建、谱内容延伸至20kHz，并给出因果流式变体，但未报告流式下的性能损失或推理延迟。

## 🎯 结论与影响

最强结论是潜空间生成式TSE在感知保真度上显著优于掩码式基线，并首次把宽带高保真重建引入EEG引导TSE。这将推动该子方向从掩码范式转向codec潜空间生成范式，对助听器实时神经引导处理有直接落地含义。

## ⚠️ 局限与未解决问题

摘要仅给主观分，缺SI-SDR/PESQ/WER等客观指标与消融；未报流式变体的延迟与性能折损；EEG数据集规模小、被试依赖性强，跨被试泛化未说明；六阶段课程的超参敏感性未讨论。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
