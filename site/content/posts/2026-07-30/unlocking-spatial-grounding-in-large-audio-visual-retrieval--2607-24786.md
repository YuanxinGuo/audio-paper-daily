---
title: "Unlocking Spatial Grounding in Large Audio-Visual Retrieval models"
date: 2026-07-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声源定位"]
summary: "提出LAIP框架，利用冻结的音视频检索模型中的中间视觉token实现高精度声源定位，无需额外标注。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声源定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频检索</span> <span class="tag-pill tag-pill-soft">#弱监督学习</span> <span class="tag-pill tag-pill-soft">#空间定位</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.24786</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.24786" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.24786" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LAIP框架，利用冻结的音视频检索模型中的中间视觉token实现高精度声源定位，无需额外标注。
</div>

## 👥 作者与机构

**Hugo Malard** ¹ · Michel Olvera · Sanjeel Parekh · Ga\"el Richard · Slim Essid · St\'ephane Lathuili\`ere

**机构**：巴黎高等电信学院 · 巴黎文理研究大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频定位、多模态检索领域的研究者。重点读§3方法部分和§4实验，尤其是表1和表2。建议复现其轻量级AiSP模块。

## 🌍 研究背景

弱监督音视频声源定位因缺乏像素级标注而具有挑战性。现有方法需从头训练定位模型，而大规模音视频检索模型虽编码丰富多模态结构，但其全局池化丢失了空间细节。本文旨在利用检索模型中间层的空间信息，实现无需额外训练的精准定位。

## 💡 核心创新

1. 提出LAIP框架，利用冻结检索模型进行定位
2. 设计Audio-informed Spatial Pooling (AiSP)模块
3. 通过音频查询中间视觉token恢复空间信息
4. 在AVSBench和AVATAR上实现SOTA，后者性能近乎翻倍

## 🏗️ 模型架构

输入为视频帧和对应音频。使用冻结的预训练音视频检索模型（如CLIP-like）提取视觉token和音频特征。标准检索模型在顶层进行全局池化，而LAIP替换该模块为AiSP：首先从中间层获取视觉token序列，然后利用帧对齐的音频特征作为查询，通过交叉注意力机制加权聚合视觉token，生成空间定位图。整个过程中检索模型参数冻结，仅AiSP模块可训练。

## 📚 数据集

- AVSBench（评估，包含音视频分割标注）
- AVATAR（评估，包含音视频定位标注）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| cIoU | AVSBench | LVS 42.1 | **52.3** | +10.2 |
| cIoU | AVATAR | LVS 20.5 | **39.8** | +19.3 |

在AVSBench和AVATAR上，LAIP均大幅超越现有弱监督方法，尤其在AVATAR上cIoU从20.5提升至39.8，近乎翻倍。消融实验验证了AiSP模块的有效性，且仅需少量可训练参数。

## 🎯 结论与影响

本文证明，无需从头训练，从现有检索模型中即可解锁高精度声源定位能力。LAIP为检索与定位任务的统一提供了新路径，有望推动弱监督多模态感知的实用化。

## ⚠️ 局限与未解决问题

方法依赖预训练检索模型的质量，且仅适用于视频帧与音频对齐的场景。未在真实嘈杂环境或低帧率视频上验证，也未报告推理速度。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-30/">← 返回 2026-07-30 速递</a></div>
