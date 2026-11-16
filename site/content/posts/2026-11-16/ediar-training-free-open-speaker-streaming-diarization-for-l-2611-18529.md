---
title: "eDIAR: Training-Free Open-Speaker Streaming Diarization for Long Meetings and Large Archives via e-means"
date: 2026-11-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人日志"]
summary: "用 e-means 聚类替换固定槽位上限，实现免训练、说话人数不限的流式说话人日志。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人日志</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#聚类</span> <span class="tag-pill tag-pill-soft">#免训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.18529</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.18529" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.18529" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用 e-means 聚类替换固定槽位上限，实现免训练、说话人数不限的流式说话人日志。
</div>

## 👥 作者与机构

**Kyudan Jung** ¹ · Jihwan Kim · Minwoo Lee · Eunji Shin · Jaegul Choo

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做说话人日志、流式会议转写与语料库构建的读者。值得通读，重点看 §3 的槽位内 e-means 重聚类机制与有界窗口标签修正策略，以及长会议误差累积对比实验；工程落地者可先看成本随会议时长不增长的复杂度分析。

## 🌍 研究背景

流式说话人日志此前以 Streaming Sortformer、Nemotron-3 等固定输出槽位的神经日志器为代表，它们在线运行且精度较高，但槽位数固定，说话人数超过槽位即失效；长会议中误差还会持续累积。传统离线聚类方案（如谱聚类、Lloyd's k-means）虽无人数上限，却难以在线化且计算昂贵。本文要在不重训练模型的前提下解除槽位上限，并让长会议与大规模档案的说话人链接变得可行。

## 💡 核心创新

1. 槽位内用官方 e-means 聚类，突破固定槽位人数上限
2. 流式下有界窗口重聚类 + 数秒标签修正 + 槽位身份锚定
3. 免训练改造：四槽 Streaming Sortformer 直接变为开放说话人系统
4. e-means 默认配方在数百到百万级 embedding 上稳定运行

## 🏗️ 模型架构

输入为流式音频帧，经冻结的 Streaming Sortformer 槽位头（slot head）输出各槽位的活动与重叠语音判决及对应说话人 embedding。当所有槽位被占用后，对槽位内累积的 embedding 用 e-means 做聚类以扩展身份数；流式模式下重聚类限制在有界窗口内，标签在数秒内被修订，身份锚定回槽位头的槽位以保持时序一致。输出为不定数量的说话人标签序列，单次更新成本不随会议时长增长。

## 📚 数据集

- 长会议录音（评估，时长增长至一小时）
- 大规模对话语料档案（评估，帧级说话人链接）

## 📊 实验结果

摘要未给出具体数值指标，仅定性说明：在说话人数超过槽位的场景下，固定槽位模型失效而本方法保持准确；在一小时长会议上精度显著优于会累积误差的 Streaming Sortformer，且单次更新成本不随时长增长；e-means 在大规模档案帧级链接任务上达到 Lloyd's k-means 的聚类质量且快数倍。

## 🎯 结论与影响

最强结论是无需重训练即可把固定槽位日志器变为开放说话人系统，并在长会议上避免误差累积。这为流式日志的可扩展性提供了低成本路径，对会议转写与大规模语料标注的工程落地有直接价值。

## ⚠️ 局限与未解决问题

摘要缺少具体指标、消融与推理延迟数据；e-means 与 k-means 的质量对比仅定性描述；有界窗口重聚类带来的标签抖动与延迟未量化；对比基线仅限 Streaming Sortformer 与 Nemotron-3，未与离线聚类方案全面比较。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-16/">← 返回 2026-11-16 速递</a></div>
