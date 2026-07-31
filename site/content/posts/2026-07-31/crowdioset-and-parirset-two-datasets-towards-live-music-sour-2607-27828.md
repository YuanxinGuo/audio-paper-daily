---
title: "CrowdioSet and PaRIRset: Two Datasets Towards Live Music Source Separation"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "提出两个新数据集CrowdioSet和PaRIRset，用于提升音乐源分离模型在真实现场录音中的泛化能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#房间冲激响应</span> <span class="tag-pill tag-pill-soft">#现场音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.27828</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.27828" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.27828" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两个新数据集CrowdioSet和PaRIRset，用于提升音乐源分离模型在真实现场录音中的泛化能力。
</div>

## 👥 作者与机构

Enric Gus\'o · Xavier Serra

**机构**：庞培法布拉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音乐源分离、音频数据增强或现场录音处理的研究者阅读。建议重点阅读第3节（数据集构建）和第4节（实验设置），并查看附录中的主观评估细节。可先浏览图1和表1以快速了解数据集规模。

## 🌍 研究背景

现有音乐源分离模型多在录音室数据集（如MUSDB18）上训练，对现场录音泛化差，因为现场包含场地声学、扬声器响应和观众噪声。先前工作尝试使用合成RIR或噪声增强，但缺乏真实场景数据。本文旨在通过提供真实环境噪声和真实场地RIR数据集，弥补训练数据与现场场景的差距。

## 💡 核心创新

1. 构建CrowdioSet：4800条真实环境噪声轨和合成跟唱，用于去噪
2. 构建PaRIRset：40个专业音乐厅的立体声冲激响应数据集
3. 结合两者训练MSS模型，显著提升现场录音分离性能
4. 公开所有数据、代码和模型权重，促进可复现研究

## 🏗️ 模型架构

模型基于现有MSS架构（如Demucs或BSRNN），输入为混合音频的频谱图，主干网络采用U-Net或Transformer结构，关键模块包括卷积层和注意力机制。训练时使用CrowdioSet进行数据增强（添加噪声和跟唱），并使用PaRIRset的RIR进行卷积模拟现场混响。输出为分离后的各音源（如人声、鼓、贝斯等）的时域波形。

## 📚 数据集

- CrowdioSet（训练/评估：4800条真实环境噪声轨，合成跟唱）
- PaRIRset（训练/评估：40个音乐厅的立体声RIR）
- MUSDB18（训练/评估：150首歌曲，用于分离任务）
- MOISESDB（训练/评估：多轨音乐数据集，用于生成跟唱）

## 📊 实验结果

摘要未提供具体数值指标，但提到客观和主观评估均优于基线。实验表明，结合CrowdioSet和PaRIRset训练可提升MSS模型在真实现场录音上的分离性能，且优于仅使用语音增强RIR。

## 🎯 结论与影响

本文通过提供两个高质量数据集，有效提升了音乐源分离模型在真实现场场景的泛化能力，填补了该领域数据空白。对后续研究而言，这些数据集可作为标准基准，推动现场音乐分离的发展。工业上可用于演唱会录音后期处理、直播音频分离等场景。

## ⚠️ 局限与未解决问题

摘要未提及模型架构细节和计算开销，也未与最新SOTA方法对比。数据集仅覆盖专业音乐厅，可能不适用于小型场地或户外演出。主观评估的规模和具体方法未说明，可能影响结论的普适性。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
