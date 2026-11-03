---
title: "Deployment-constrained key estimation with a DSP-guided transformer reranker"
date: 2026-11-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "用21.5k参数的DSP引导Transformer重排序器，在115KB模型下把色度模板调性估计的MIREX从61.08提升到73.55。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#调性估计</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#轻量化部署</span> <span class="tag-pill tag-pill-soft">#DSP</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.02408</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.02408" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.02408" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用21.5k参数的DSP引导Transformer重排序器，在115KB模型下把色度模板调性估计的MIREX从61.08提升到73.55。
</div>

## 👥 作者与机构

**Pardis Noorzad** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐信息检索、端侧音频分析、模型轻量化的工程与研究读者。值得通读，重点看§3的DSP打分与Transformer重排序如何耦合，以及表2/表3中与madmom KeyCNN的对比和输入层参数消融。若只关心精度可跳过部署细节。

## 🌍 研究背景

调性估计是音乐信息检索的基础任务，本地音乐库导入场景要求分析器小、快、可进程内运行。传统色度模板法（如Krumhansl模板）体积小但精度有限；学习型方法如madmom KeyCNN精度更高，但模型与运行时依赖常达数十至数百MB，难以嵌入轻量应用。本文要在严格部署预算下缩小这一精度差距。

## 💡 核心创新

1. DSP色度模板打分作为先验，Transformer仅做重排序
2. 21.5k参数、115KB模型产物的极小重排序器
3. 12参数循环输入层替代468参数线性投影
4. 端到端ONNX Runtime部署足迹仅76.7MB

## 🏗️ 模型架构

输入为DSP阶段提取的色度特征与模板匹配得分，经一个仅12参数的循环（circular）输入编码层映射后送入小型Transformer编码器做重排序，输出24个调性类别的修正得分。整体仅21.5k参数，模型文件115KB，推理在确定性DSP打分基础上每曲仅增加0.32ms，并以ONNX Runtime进程内运行。

## 📚 数据集

- FMAK（训练，4,040曲）
- FMAK（验证，449曲）
- FMAKv2（评估，1,000曲，与训练不重叠）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MIREX | FMAKv2 | DSP色度模板 61.08 | **73.55 ± 0.46** | +12.47 |
| Exact Accuracy | FMAKv2 | DSP色度模板 52.30 | **67.07 ± 0.65** | +14.77 |
| MIREX | FMAKv2 | madmom KeyCNN 74.16 | **73.55 ± 0.46** | -0.61 |

三个随机种子下MIREX 73.55±0.46、精确准确率67.07±0.65，接近同清单本地madmom KeyCNN的74.16 MIREX，但模型体积与依赖远小。消融显示12参数循环输入层与468参数线性投影精度区间相当，说明输入映射可大幅压缩。摘要未报告推理延迟分布与跨数据集泛化。

## 🎯 结论与影响

最强结论是在百KB级模型预算下把模板法调性估计提升逾12个MIREX点，逼近学习型参考。这为端侧音乐库分析提供了可行路线，也提示DSP先验+极小重排序器可推广到其他轻量MIR任务。工业上可直接嵌入本地播放器导入流程。

## ⚠️ 局限与未解决问题

仅在FMAK/FMAKv2上评估，缺少跨数据集与流派偏差分析；对比基线仅DSP模板与单个madmom参考，未与更多轻量学习法比较；未报告延迟分布、内存峰值与移动端实测；重排序器对DSP前端错误的依赖未做误差传播分析。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-03/">← 返回 2026-11-03 速递</a></div>
