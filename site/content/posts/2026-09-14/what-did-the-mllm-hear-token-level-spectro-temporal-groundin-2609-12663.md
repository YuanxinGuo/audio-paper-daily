---
title: "What Did the MLLM Hear? Token-Level Spectro-Temporal Grounding for Audio MLLM Explainability"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解可解释性"]
summary: "提出 STAG，首个针对音频 MLLM 生成 caption 的 token 级时频归因框架，用词汇投影与频谱遮挡合成相关性图。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解可解释性</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频MLLM</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#时频定位</span> <span class="tag-pill tag-pill-soft">#音频描述</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.12663</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.12663" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.12663" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 STAG，首个针对音频 MLLM 生成 caption 的 token 级时频归因框架，用词汇投影与频谱遮挡合成相关性图。
</div>

## 👥 作者与机构

**Lucia Cascone** ¹ · Valeria Fraenza · Michele Nappi · Fabio Narducci · Benedetto Simone

**机构**：萨莱诺大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频 MLLM 可解释性、音频描述归因的研究者阅读。建议通读，重点看 §3 的 token 级词汇投影与频谱遮挡设计，以及四个 grounding benchmark 上的对比表与 counterfactual deletion 实验。若只关心方法，可先看相关性图融合公式与八个 backbone 的零参数迁移结果。

## 🌍 研究背景

音频 MLLM 已能对复杂声景生成细粒度自然语言描述，但每个生成 token 究竟由输入音频的哪些时频区域支撑仍不清楚。声学证据在时间与频率上分布，且并发事件可能时间重叠而占据不同频带，使归因比图像更困难。现有 post-hoc 解释方法多针对视觉或分类模型，缺少面向音频 MLLM 生成式 caption 的 token 级时频定位工具，本文即填补这一空白。

## 💡 核心创新

1. 首个面向音频 MLLM caption 的 token 级时频归因框架 STAG
2. 用目标 token 特定词汇投影估计时间支撑
3. 用受控频谱遮挡度量频带相关性并融合成时频图
4. counterfactual deletion 验证解释的选择性与忠实性

## 🏗️ 模型架构

输入为音频波形及其编码表示，主干为冻结的音频 MLLM（八种 audio-language backbone，不更新参数）。STAG 分两路：一路对编码音频表示做目标 token 特定的词汇投影，估计该 token 的时间支撑；另一路对输入做受控频谱遮挡，测量各频带对生成该 token 的相关性。两路信号归一化后融合为一张时频相关性图，作为该 token 的解释输出。全程 post-hoc，无需重训练或微调。

## 📚 数据集

- 四个 grounding benchmark（评估，具体名称摘要未给出）

## 📊 实验结果

摘要称 STAG 在四个 grounding benchmark 上均取得最佳事件定位性能，优于十种 post-hoc 解释方法，并可零参数迁移到八个 audio-language backbone。counterfactual deletion 显示移除被识别证据会选择性降低对应事件的置信度，且常使该事件从重生成 caption 中消失。摘要未给出 SI-SDR、PESQ、WER 等具体数值，故不列量化结果。

## 🎯 结论与影响

最强结论是：token 级时频归因能定位音频 MLLM 生成 caption 所依赖的声学证据，且删除该证据会选择性改变输出。这为音频 MLLM 的可解释性提供了行为学证据，后续可推动更细粒度的归因评测与模型诊断。工业上可用于音频描述系统的审计与调试，但需先解决计算开销问题。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与频谱遮挡的计算成本，遮挡次数可能随频带数线性增长；四个 benchmark 的具体构成与规模未说明，存在评测偏差风险；仅用 counterfactual deletion 做行为验证，缺少与人类标注的定量一致性分析；未与基于梯度的归因方法做效率对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
