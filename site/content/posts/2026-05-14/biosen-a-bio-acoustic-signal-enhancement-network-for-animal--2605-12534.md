---
title: "BioSEN: A Bio-acoustic Signal Enhancement Network for Animal Vocalizations"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低计算量", "#注意力机制", "#生物声学", "#语音增强"]
summary: "提出BioSEN，一种针对动物发声的生物声学信号增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个数据集上以更低计算量达到或超越SOTA语音增强模型。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#低计算量</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.12534</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.12534" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.12534" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BioSEN，一种针对动物发声的生物声学信号增强网络，通过多尺度双轴注意力、谐波增强和能量自适应门控，在三个数据集上以更低计算量达到或超越SOTA语音增强模型。
</div>

## 👥 作者与机构

**Tianyu Song** ¹ · Ton Viet Ta · Ngamta Thamwattana · Hisako Nomura · Linh Thi Hoai Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、生物声学或低资源音频处理的研究者。建议重点阅读§3模型架构和§4实验部分，尤其是表1-3的结果对比。可先看§3.2生物谐波增强单元和§3.3能量自适应门控的设计思路。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 对野外录制的动物叫声进行降噪和增强，用于生物多样性监测与保护。 |
| **核心创新** | 多尺度双轴注意力同时捕捉时频局部与全局依赖 · 生物谐波增强单元利用动物发声的谐波结构 · 能量自适应门控防止将动物叫声误判为噪声 |
| **模型架构** | 输入带噪频谱 → 多尺度双轴注意力单元提取时频特征 → 生物谐波多尺度增强单元捕获谐波结构 → 能量自适应门控单元用频率权重保留发声 → 输出增强频谱。参数量未在摘要中给出。 |
| **数据集** | 三个生物声学数据集（未具体命名） |
| **关键结果** | 在三个生物声学数据集上，BioSEN匹配或超越SOTA语音增强模型（如SEPFormer、DCCRN等），同时计算量显著降低。具体指标数值未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与语音增强领域直接相关，但针对非人声信号。其多尺度双轴注意力和谐波增强思路可迁移至人声增强中的音乐或语音谐波建模；能量自适应门控对防止目标信号被抑制有参考价值。与目标说话人提取、语音分离、双耳音频、乐器分离无直接关联。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟或具体指标数值；未在标准语音增强数据集（如DNS-Challenge）上评估，难以直接对比人声增强性能；未进行消融实验验证各模块贡献；数据集未公开，可复现性存疑。

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

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
