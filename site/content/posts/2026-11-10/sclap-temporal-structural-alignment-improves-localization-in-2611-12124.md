---
title: "SCLAP: Temporal structural alignment improves localization in long-form audio"
date: 2026-11-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频文本检索"]
summary: "用单调一维最优传输对齐音频帧与文本词元，从片段级描述中获得细粒度时序监督，提升长音频检索与零样本定位。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频文本检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#时序定位</span> <span class="tag-pill tag-pill-soft">#CLAP</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.12124</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.12124" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.12124" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用单调一维最优传输对齐音频帧与文本词元，从片段级描述中获得细粒度时序监督，提升长音频检索与零样本定位。
</div>

## 👥 作者与机构

**Yacouba Kaloga** ¹ · Ina Kodrasi

**机构**：Idiap 研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频-文本对比学习、CLAP 改进、声音事件定位的研究者阅读。值得通读，重点看 §3 的单调 OT 对齐公式与传输计划如何转化为帧-词余弦定位分数，以及 §4 中 CASTELLA 长音频上随事件-上下文比下降的定位曲线；表 1/表 2 的短音频检索对比可快速扫过。

## 🌍 研究背景

CLAP 类音频-文本模型通常将帧序列与词元序列均匀池化为全局嵌入，丢弃时序结构，导致检索与定位性能受限，尤其对长录音中的短事件。已有工作如 Text-aware Attention Pooling 尝试引入注意力池化，但仍缺乏帧级监督。本文要在仅有片段级描述的条件下获得细粒度时序对齐，改善长音频检索与零样本声音事件定位。

## 💡 核心创新

1. 用单调一维最优传输对齐音频帧与文本词元
2. 从传输计划导出帧级时序监督，无需帧级标注
3. 学习边缘分布提供软对齐，替代均匀池化
4. 推理时免 OT 计算，定位用帧-文本余弦分数

## 🏗️ 模型架构

输入为音频帧级特征序列与文本词元序列，分别经音频编码器与文本编码器得到帧嵌入和词元嵌入。核心模块为单调一维最优传输：在帧与词元之间求解带单调约束的传输计划，得到学习到的边缘分布与对齐矩阵，并以此构造序列级对比损失进行训练。输出包括用于检索的池化嵌入与用于定位的帧-词余弦相似度序列。摘要未给出参数量。

## 📚 数据集

- Clotho（短音频 15-30s，评估检索与定位）
- TACOS（短音频 15-30s，评估检索与定位）
- CASTELLA（长音频至 300s，评估检索与定位）

## 📊 实验结果

摘要未给出具体数值指标。作者报告：在 Clotho 与 TACOS 短音频上检索性能与 CLAP 相当，零样本定位优于 CLAP 与 Text-aware Attention Pooling；在 CASTELLA 长音频上检索提升，且定位优势随事件-上下文比降低而扩大。推理阶段无需最优传输计算。

## 🎯 结论与影响

最强结论是单调 OT 对齐可在仅用片段级描述时提供有效帧级时序监督，并在长音频短事件场景放大定位收益。这为 CLAP 类模型的时序建模提供了轻量替代方案，对长录音检索与声音事件定位的落地有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与消融，难以判断各组件贡献；仅在三个数据集上评估，长音频仅 CASTELLA 一个；未报告推理延迟与计算开销；单调约束假设事件顺序与文本顺序一致，对乱序或多事件重叠场景可能失效。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-10/">← 返回 2026-11-10 速递</a></div>
