---
title: "MERP: A Latent-Bottleneck Framework for Robust Multi-Modal Multi-Label Emotion Recognition"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态情感识别"]
summary: "提出MERP，用固定大小latent bank做多模态多标签情感识别，在测试时随机丢模态下保持鲁棒。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态情感识别</span> <span class="tag-pill tag-pill-soft">#缺失模态鲁棒性</span> <span class="tag-pill tag-pill-soft">#Perceiver</span> <span class="tag-pill tag-pill-soft">#多标签分类</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29430</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Creative-zcx/MERP" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Creative-zcx/MERP</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29430" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29430" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Creative-zcx/MERP" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MERP，用固定大小latent bank做多模态多标签情感识别，在测试时随机丢模态下保持鲁棒。
</div>

## 👥 作者与机构

**Chuangxin Zhao** ¹ · Meimei Zhang · Canran Xiao · Jiachen Luo · Jiajun He · Kaijie Chen · Huy Phan · Tomoki Toda · … 等 1 人

**机构**：清华大学 · 帝国理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态情感识别与缺失模态鲁棒性的研究者阅读。若关注latent bottleneck与原型对齐机制，建议通读§3方法部分并重点看表2的模态缺失实验；若只关心语音增强/分离则相关性低，可略读。可先看§3.2的latent bank设计与表2的audio-only对比。

## 🌍 研究背景

多模态情感识别（文本/视觉/声学）在CMU-MOSEI、M3ED等基准上已有较多工作，主流做法是融合三模态序列后接分类头，代表方法包括各类跨模态Transformer与图网络。但这些模型训练时依赖完整模态，部署时若某模态缺失（传感器故障、隐私限制）性能会急剧下降。已有缺失模态方法多需在训练中模拟缺失样本，或依赖生成式补全，代价高且泛化有限。本文要在不引入缺失模态训练样本的前提下，缩小训练-测试模态可用性差距。

## 💡 核心创新

1. 将联合序列映射到固定大小latent bank，推理与输入长度解耦
2. 在latent推理前后提取标签特定证据并用重建对齐两层
3. 正负类原型增强类间可分性
4. 频率塑形扰动的噪声门控特征增强器
5. 置信度感知的类级融合组合互补预测器

## 🏗️ 模型架构

输入为文本、视觉、声学三路序列特征，拼接为联合序列后送入Perceiver式主干：通过交叉注意力将变长联合序列压缩到固定大小的latent bank，再在latent空间做重复推理，使计算量与原始输入长度无关。在latent推理前后分别提取标签特定证据（label-specific evidence），并通过重建损失对齐两个层级。分类端引入正/负类原型提升可分性；训练时用带频率塑形扰动的噪声门控特征增强器模拟退化；最后以置信度感知的类级融合整合各预测器输出，得到多标签情感预测。摘要未给出参数量。

## 📚 数据集

- CMU-MOSEI（训练与评估，多模态情感识别基准）
- M3ED（训练与评估，多模态多标签情感数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| micro-F1 | CMU-MOSEI（20%测试时随机丢模态） | 最强评估基线 | **0.563** | +0.004 |
| micro-F1 | M3ED（20%测试时随机丢模态） | 最强评估基线 | **0.780** | +0.005 |
| micro-F1 | CMU-MOSEI（audio-only严重缺失） | LDDU 0.022 | **0.473** | +0.451 |

在20%测试时随机模态丢弃下，MERP在CMU-MOSEI与M3ED上分别取得0.563与0.780 micro-F1，较最强基线仅高0.004与0.005，提升幅度较小；但在CMU-MOSEI仅音频的严重缺失场景下保持0.473，而LDDU仅0.022，显示固定latent推理对极端缺失的鲁棒性优势明显。摘要未报告消融细节、推理延迟与完整模态下的性能。

## 🎯 结论与影响

最强结论是固定大小latent推理可在训练不见缺失样本的情况下显著缓解测试时模态缺失导致的性能崩塌，尤其在audio-only极端场景下远超LDDU。这为多模态情感识别的鲁棒性提供了一条不依赖缺失数据增强的路线，对部署中传感器不稳定或隐私受限的情感计算系统有参考价值。

## ⚠️ 局限与未解决问题

常规20%丢模态下相对最强基线仅提升0.004/0.005，统计显著性存疑；摘要未给出完整模态性能、消融实验与推理开销，难以判断latent bottleneck是否损失信息；仅两个数据集，且未与生成式补全类方法全面对比。

## 🔗 开源资源

- **代码**：<https://github.com/Creative-zcx/MERP>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
