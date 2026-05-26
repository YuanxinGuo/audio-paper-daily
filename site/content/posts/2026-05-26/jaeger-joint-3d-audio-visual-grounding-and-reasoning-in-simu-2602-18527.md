---
title: "JAEGER: Joint 3D Audio-Visual Grounding and Reasoning in Simulated Physical Environments"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉定位与推理"]
summary: "提出JAEGER框架，将音频-视觉大模型扩展到3D空间，通过RGB-D和一级环境声实现联合空间定位与推理。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉定位与推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#3D音频</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#声源定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.18527</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/liuzhan22/JAEGER" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">liuzhan22/JAEGER</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.18527" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.18527" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/liuzhan22/JAEGER" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出JAEGER框架，将音频-视觉大模型扩展到3D空间，通过RGB-D和一级环境声实现联合空间定位与推理。
</div>

## 👥 作者与机构

**Zhan Liu** ¹ · Changli Tang · Yuxin Wang · Zhiyuan Zhu · Youjun Chen · Yiwen Shao · Tianzi Wang · Lei Ke · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频-视觉多模态、空间音频处理方向的研究者。建议重点阅读§3的Neural IV表示和§4的SpatialSceneQA基准。可先看图2架构概览，再深入§3.2的Neural IV设计。

## 🌍 研究背景

现有音频-视觉大模型（AV-LLMs）主要基于2D RGB视频和单声道音频，无法在复杂3D环境中进行可靠的声源定位和空间推理。这种维度不匹配限制了模型在物理世界中的应用。本文旨在通过引入RGB-D观测和多通道一阶环境声，将AV-LLMs扩展到3D空间，实现联合空间定位与推理。

## 💡 核心创新

1. 提出Neural IV，一种学习到的空间音频表示，编码鲁棒的方向线索
2. 构建SpatialSceneQA基准，包含61k指令微调样本
3. 将AV-LLMs扩展到3D空间，融合RGB-D与一阶环境声
4. 在重叠声源等恶劣声学场景下仍能提升DOA估计
5. 开源代码、模型和数据集

## 🏗️ 模型架构

输入为RGB-D图像和多通道一阶环境声（FOA）。RGB-D经视觉编码器提取特征，FOA经音频编码器提取特征，其中音频编码器包含Neural IV模块，该模块从FOA中学习空间音频表示以增强方向估计。多模态特征通过跨模态注意力融合，输入大语言模型进行联合推理与定位。输出为文本描述或空间坐标。

## 📚 数据集

- SpatialSceneQA（训练/评估，61k指令微调样本，来自模拟物理环境）
- 模拟环境数据集（训练/评估，用于构建SpatialSceneQA）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 空间定位准确率 | SpatialSceneQA | 2D-centric AV-LLM（如AV-LLM基线） | **JAEGER** | 显著提升（具体数值未在摘要中给出） |

实验表明，JAEGER在多种空间感知与推理任务上持续超越2D-centric基线，尤其在重叠声源等恶劣声学场景下，Neural IV显著提升了DOA估计鲁棒性。具体数值未在摘要中详细列出，但强调了3D建模的必要性。

## 🎯 结论与影响

JAEGER通过引入3D空间建模和Neural IV表示，有效克服了2D AV-LLMs的维度不匹配问题，在空间定位与推理任务上取得显著提升。该工作为音频-视觉大模型在物理环境中的应用奠定了基础，有望推动机器人、增强现实等领域的落地。

## ⚠️ 局限与未解决问题

实验仅在模拟环境中进行，未在真实场景验证；未报告模型参数量、推理延迟等效率指标；与现有2D方法的对比可能不够全面（如未对比纯音频3D定位方法）。

## 🔗 开源资源

- **代码**：<https://github.com/liuzhan22/JAEGER>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
