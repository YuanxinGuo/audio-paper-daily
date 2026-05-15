---
title: "BioSEN: A Bio-acoustic Signal Enhancement Network for Animal Vocalizations"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#注意力机制", "#生物声学", "#语音增强", "#轻量化模型"]
summary: "提出BioSEN，一种针对动物叫声的语音增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个生物声学数据集上以更低计算量达到或超越SOTA语音增强模型。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.12534</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.12534" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.12534" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BioSEN，一种针对动物叫声的语音增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个生物声学数据集上以更低计算量达到或超越SOTA语音增强模型。
</div>

## 👥 作者与机构

**Tianyu Song** ¹ · Ton Viet Ta · Ngamta Thamwattana · Hisako Nomura · Linh Thi Hoai Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事生物声学、语音增强或轻量化模型研究的读者。建议通读，重点看§3的模块设计和§4的实验对比。可先看表1和表2了解性能与效率。

## 🌍 研究背景

语音增强主要针对人类语音，而生物声学中动物叫声因噪声复杂、谐波结构独特而研究不足。现有语音增强模型直接应用于生物声学效果不佳，且计算量大。本文旨在设计一个专为生物声学信号定制的轻量级增强网络，解决动物叫声在噪声环境下的增强问题。

## 💡 核心创新

1. 多尺度双轴注意力单元提取时频特征
2. 生物谐波多尺度增强单元捕获谐波结构
3. 能量自适应门控连接单元防止误删叫声
4. 整体轻量化设计，计算量远低于SOTA

## 🏗️ 模型架构

输入为带噪生物声学信号的时频谱。主干网络包含三个模块：1) 多尺度双轴注意力单元，沿时间和频率轴分别进行注意力计算，提取多尺度时频特征；2) 生物谐波多尺度增强单元，利用谐波结构信息增强目标叫声；3) 能量自适应门控连接单元，根据频率能量权重调整门控，保护叫声不被当作噪声抑制。输出为增强后的时频谱。

## 📚 数据集

- Bioacoustic dataset 1（训练/评估，具体名称未给出）
- Bioacoustic dataset 2（训练/评估）
- Bioacoustic dataset 3（训练/评估）

## 📊 实验结果

摘要未提供具体数值指标，仅说明BioSEN在三个生物声学数据集上匹配或超越SOTA语音增强模型，且计算量显著降低。建议读者查阅原文获取详细指标。

## 🎯 结论与影响

BioSEN在生物声学增强任务上以更低计算量达到SOTA性能，证明了针对动物叫声特性设计的模块的有效性。该工作为生物多样性监测和生态保护中的音频处理提供了实用工具，有望推动生物声学领域的深度学习应用。

## ⚠️ 局限与未解决问题

摘要未提及模型在真实复杂噪声环境下的鲁棒性，也未报告推理延迟或参数量等效率指标。数据集名称和规模未给出，可能影响可复现性。缺乏与专门生物声学增强方法的对比。

## 📋 引用

```bibtex
@article{song20262605,
  title  = {BioSEN: A Bio-acoustic Signal Enhancement Network for Animal Vocalizations},
  author = {Tianyu Song and  Ton Viet Ta and  Ngamta Thamwattana and  Hisako Nomura and  Linh Thi Hoai Nguyen},
  journal = {arXiv preprint arXiv:2605.12534},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
