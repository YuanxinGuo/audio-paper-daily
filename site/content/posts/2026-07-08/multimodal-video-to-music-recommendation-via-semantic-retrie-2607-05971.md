---
title: "Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐推荐"]
summary: "提出VTMR两阶段框架，通过多模态语义检索和时序重排序实现视频到音乐推荐，在R@10和Median Rank上显著超越基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐推荐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音乐推荐</span> <span class="tag-pill tag-pill-soft">#多模态检索</span> <span class="tag-pill tag-pill-soft">#时序重排序</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.05971</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.05971" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.05971" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出VTMR两阶段框架，通过多模态语义检索和时序重排序实现视频到音乐推荐，在R@10和Median Rank上显著超越基线。
</div>

## 👥 作者与机构

**Seungheon Doh** ¹ · Minhee Lee · Sangmoon Lee · Ben Sangbae Chon · Juhan Nam

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐推荐、多模态检索方向的研究者。建议重点阅读§3.2时序重排序模块和§4.2表1的消融实验，理解粗检索与细对齐的互补增益。

## 🌍 研究背景

视频到音乐推荐旨在为视频匹配风格、情绪契合的背景音乐，是多媒体检索的重要任务。现有方法多依赖单模态特征或简单融合，难以捕捉视频与音乐间的细粒度时序对应关系。本文提出VTMR，通过两阶段框架先粗后精地实现语义对齐与时序匹配。

## 💡 核心创新

1. 联合音视频-文本表示空间对齐多模态信号
2. 粗粒度全局嵌入检索与细粒度时序重排序两阶段设计
3. 时序重排序模块利用交叉注意力捕捉帧-节拍对应关系
4. 人类偏好评估验证与商业基线相当的性能

## 🏗️ 模型架构

VTMR包含两阶段：Stage 1使用预训练的视频、音频、文本编码器提取特征，通过对比学习对齐到联合嵌入空间，用粗粒度全局嵌入进行高效检索；Stage 2对检索到的候选对，使用时序重排序模块（基于Transformer的交叉注意力）处理视频帧序列与音乐节拍序列，输出细粒度匹配分数。

## 📚 数据集

- 内部视频-音乐配对数据集（训练/评估，未公开规模）
- 商业基线数据集（评估，用于人类偏好研究）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| R@10 | 内部测试集 | 最强基线 14.2 | **18.3** | +4.1 |
| Median Rank | 内部测试集 | 最强基线 75 | **46** | -29 |

VTMR在内部测试集上，多模态检索阶段将R@10从14.2提升至15.9，Median Rank从75降至58；时序重排序进一步将R@10提升至18.3，Median Rank降至46。人类偏好研究表明VTMR在整体偏好上与商业基线持平，且音乐质量优于生成式基线。

## 🎯 结论与影响

VTMR通过粗检索与细重排序的级联设计，有效提升了视频到音乐推荐的准确性，验证了多模态对齐与时序匹配的互补价值。该框架为工业级推荐系统提供了可落地的两阶段范式，未来可探索更细粒度的跨模态交互。

## ⚠️ 局限与未解决问题

数据集未公开，复现困难；仅与一个商业基线和一个生成基线对比，缺乏与更多推荐方法的比较；未报告推理延迟，时序重排序可能增加计算开销；人类评估规模未明确。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
