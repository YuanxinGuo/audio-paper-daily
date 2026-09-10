---
title: "Audio Deepfake Detection Using Temporal Coherence Analysis"
date: 2026-09-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "基于 CLAP 嵌入的时序一致性分析，用轻量集成分类器区分真实与合成语音及音乐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频深度伪造检测</span> <span class="tag-pill tag-pill-soft">#CLAP</span> <span class="tag-pill tag-pill-soft">#对比学习表征</span> <span class="tag-pill tag-pill-soft">#可解释性分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.09489</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.09489" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.09489" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>基于 CLAP 嵌入的时序一致性分析，用轻量集成分类器区分真实与合成语音及音乐。
</div>

## 👥 作者与机构

**Justin D. Norman** ¹ · Sarah Barrington

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频取证、合成语音检测、CLAP 表征分析的读者。建议重点看 §3 时序一致性特征构造与 §4 特征-标签反转分析，这两节是本文最有信息量的部分。若只关心检测性能，可先看表 2 与跨域实验；若关心可解释性，通读第 4 节。

## 🌍 研究背景

音频深度伪造检测此前主流是端到端深度网络（如 AASIST、RawNet2）或基于频谱伪影的 CNN，在域内数据集上表现强，但跨域泛化差、可解释性弱、算力开销大。CLAP 等语言-音频对比预训练模型提供了通用音频表征，但尚未被系统用于伪造检测的时序一致性建模。本文要解决的是：能否用 CLAP 嵌入的段间相似度统计量，构建轻量、可解释、跨语音与音乐域通用的检测框架。

## 💡 核心创新

1. 用 CLAP 段嵌入的成对余弦相似度分布构造 29 维统计特征
2. 轻量集成分类器替代端到端深度网络，算力开销低
3. 发现 21/29 特征在训练与真实部署间发生判别方向反转
4. 揭示语音与音乐伪造中熵的判别方向相反现象

## 🏗️ 模型架构

输入音频切分为固定长度片段，经冻结的 CLAP 音频编码器得到每段嵌入；对嵌入两两计算余弦相似度，形成相似度分布；从该分布提取 29 个统计特征（均值、方差、熵、偏度、峰度等）；将特征送入轻量集成分类器（如随机森林 / GBDT 类）输出真伪二分类。整体不含可训练深度主干，参数量与推理成本远低于 AASIST 类模型。

## 📊 实验结果

摘要未给出具体指标数值、数据集名称或与基线的定量对比，仅声称在语音与音乐域达到 competitive performance。两项实证发现（特征-标签反转、语音-音乐熵方向反转）是本文主要贡献，但缺乏可核验的数字支撑。

## 🎯 结论与影响

最强结论是：CLAP 嵌入的时序一致性统计量可作为轻量、可解释的音频伪造检测信号，且跨语音与音乐域通用。这为后续研究提供了两条线索：一是特征在部署域会反转，提示需做域自适应或特征稳定性筛选；二是语音与音乐伪造机制不同，需分域建模。工业上适合作为低成本前置筛查模块。

## ⚠️ 局限与未解决问题

摘要未报告任何具体指标、数据集规模与推理延迟，无法判断 competitive 的实际含义；未与 AASIST、RawNet2 等强基线做定量对比；特征-标签反转现象仅描述未给出缓解方案；CLAP 编码器冻结，未探索微调收益。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-10/">← 返回 2026-09-10 速递</a></div>
