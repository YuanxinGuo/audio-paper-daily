---
title: "Speaker-Aware Temporal Aggregation Strategies on Segment Representations for Depression Detection in Dyadic Interaction: A Benchmark Study"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#抑郁检测"]
summary: "构建 DEPOOL 基准，在英/汉语抑郁语料上比较 6 种时序聚合架构与 6 种冻结语音骨干，揭示单种子稳定性与跨种子可靠性不一致。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#抑郁检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时序聚合</span> <span class="tag-pill tag-pill-soft">#自监督语音表征</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#临床语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.02904</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.02904" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.02904" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建 DEPOOL 基准，在英/汉语抑郁语料上比较 6 种时序聚合架构与 6 种冻结语音骨干，揭示单种子稳定性与跨种子可靠性不一致。
</div>

## 👥 作者与机构

**Anisha Pattanayak** ¹ · Huang-Cheng Chou · Shrikanth Narayanan · Sudarsana Reddy Kadiri

**机构**：南加州大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做临床语音、抑郁检测与自监督表征聚合的研究者阅读。值得通读，重点看 §3 的 72 组配置设计与 §4 关于单类坍缩和种子鲁棒性的分析；若只关心方法，可先看表 2 与坍缩统计表，再回看聚合架构定义。

## 🌍 研究背景

语音抑郁检测通常把短片段特征压缩为说话人级决策，这一时序聚合步骤长期被当作附属环节，少有独立研究。现有基准多固定单一自监督编码器和手工选定层，报告的性能增益可能来自整条流水线而非聚合方法本身，导致结论难以归因。本文要回答：不同聚合架构在多种冻结骨干、多种子下是否真正稳健，以及应如何为聚合方法建立可控评测。

## 💡 核心创新

1. 提出 DEPOOL 受控基准，解耦骨干与聚合方法
2. 跨 6 骨干 × 6 聚合的 72 组配置网格
3. 让配置自动学习骨干层权重而非手工选层
4. 揭示单类坍缩与种子鲁棒性失配问题

## 🏗️ 模型架构

输入为短音频片段经冻结自监督语音骨干提取的帧级/片段级表征；DEPOOL 不训练骨干，仅在其上接六种时序聚合架构（含注意力池化、统计池化、循环聚合等类别），每种配置学习骨干各层的加权组合，将变长片段表征压缩为说话人级向量，再经分类头输出抑郁/非抑郁决策。评测覆盖 6 种冻结骨干与 6 种聚合架构，形成 72 组配置，并在多种子重复训练下考察稳定性。

## 📚 数据集

- 英语抑郁语料（训练/评估，具体名称摘要未给出）
- 普通话抑郁语料（训练/评估，具体名称摘要未给出）

## 📊 实验结果

摘要未给出 SI-SDR、PESQ 等具体数值，仅报告定性统计：72 组配置中约三分之一坍缩为对全部说话人预测同一类别，该失败既与骨干有关也与聚合方法有关；单种子下最稳定的架构在跨种子重复训练时并不可靠。说明平均准确率不足以刻画聚合方法的真实可用性。

## 🎯 结论与影响

最强结论是：时序聚合的评测应以对骨干和种子的鲁棒性为一等标准，而非单流水线平均准确率。这为临床语音抑郁检测的基准设计提供了新视角，提示后续工作必须报告多种子方差与坍缩率；工业落地时也应优先选择跨骨干稳定的聚合方案而非刷榜配置。

## ⚠️ 局限与未解决问题

摘要未给出具体准确率、F1 或 UAR 数值，也未说明坍缩判据与种子数量；仅两个语料、六骨干六聚合的网格仍有限，缺少与端到端微调基线的对比，且未报告推理开销。作为基准研究，缺少公开排行榜或代码链接会削弱可复现性。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
