---
title: "Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频到音频生成"]
summary: "提出Flowley，一种端到端单阶段视频到音频生成架构，通过渐进式软掩码交叉注意力实现音视频同步，并引入SoundCap生成声音感知描述以提升音频质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频到音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#跨模态对齐</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#视频到音频生成</span> <span class="tag-pill tag-pill-soft">#音频描述生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06405</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06405" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06405" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Flowley，一种端到端单阶段视频到音频生成架构，通过渐进式软掩码交叉注意力实现音视频同步，并引入SoundCap生成声音感知描述以提升音频质量。
</div>

## 👥 作者与机构

**Thanh V. T. Tran** ¹ · Ngoc-Son Nguyen · Luong Tran · Long-Khanh Pham · Paarth Neekhara · Shezheen Hussain · Van Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合视频到音频生成、多模态学习领域的研究者。建议重点阅读§3.2的渐进式软掩码交叉注意力机制和§3.3的SoundCap描述生成方法。可先看表1和表2的性能对比，再深入理解架构细节。

## 🌍 研究背景

视频到音频生成旨在为无声视频合成语义一致且时间同步的音频。现有方法多采用多阶段训练，计算成本高、运行时间长；或依赖文本到音频模型，丢失细粒度时间线索。本文提出Flowley，通过单阶段端到端训练，结合视觉特征与文本提示，并引入渐进式软掩码交叉注意力实现零额外计算成本的音视频同步。同时，针对现有基准缺乏声音导向描述的问题，提出SoundCap生成详细描述以提升音频质量。

## 💡 核心创新

1. 渐进式软掩码交叉注意力，零额外计算成本实现音视频同步
2. SoundCap：即插即用的声音感知描述生成管道
3. 端到端单阶段训练架构，避免多阶段级联误差
4. 无需预训练音视频对齐模块即达SOTA

## 🏗️ 模型架构

Flowley采用端到端单阶段架构。输入为视频帧序列和可选文本提示，视觉特征通过预训练视觉编码器提取，文本提示通过文本编码器编码。核心是渐进式软掩码交叉注意力模块，在注意力层内嵌入音视频同步，通过逐步调整掩码强度实现时间对齐。解码器基于扩散模型生成梅尔频谱图，最终通过声码器合成波形。模型参数量未在摘要中提及。

## 📚 数据集

- VGGSound（训练与评估，包含大量视频-音频对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | VGGSound | 现有最佳方法（未具名） | **Flowley达到SOTA** | 具体数值未给出 |
| IS | VGGSound | 现有最佳方法 | **Flowley达到SOTA** | 具体数值未给出 |
| KL散度 | VGGSound | 现有最佳方法 | **Flowley达到SOTA** | 具体数值未给出 |

Flowley在VGGSound数据集上，在FID、IS、KL散度等多个指标上达到SOTA。结合SoundCap后，在零样本设置下音频质量甚至超越最强的闭源方法。摘要未提供具体数值，但声称显著优于现有方法。

## 🎯 结论与影响

Flowley通过单阶段端到端训练和渐进式软掩码交叉注意力，实现了高效的视频到音频生成，无需额外对齐模块。SoundCap进一步提升了音频质量。该方法为视频到音频生成提供了简洁高效的范式，有望推动多模态内容生成的发展，并降低计算成本，便于工业部署。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度等效率指标；未在更多数据集（如AudioSet）上验证泛化性；渐进式掩码策略的收敛性分析缺失；SoundCap依赖预训练模型，可能引入偏差；零样本性能提升的具体幅度未量化。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
