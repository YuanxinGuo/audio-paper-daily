---
title: "Dynamic Clustering for Cross-Segment Permutation Alignment in Long Speech Separation"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出一种免训练的动态聚类方法，利用说话人嵌入参考池对齐长语音分离中的跨段排列，作为即插即用后处理模块，在稀疏长语音场景中表现优异。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#长语音分离</span> <span class="tag-pill tag-pill-soft">#排列对齐</span> <span class="tag-pill tag-pill-soft">#动态聚类</span> <span class="tag-pill tag-pill-soft">#后处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.09451</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.09451" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.09451" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种免训练的动态聚类方法，利用说话人嵌入参考池对齐长语音分离中的跨段排列，作为即插即用后处理模块，在稀疏长语音场景中表现优异。
</div>

## 👥 作者与机构

**Yuzhu Wang** ¹ · Archontis Politis · Konstantinos Drossos · Tuomas Virtanen

**机构**：坦佩雷大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事长语音分离、说话人日志或后处理研究的读者。建议重点阅读第3节方法部分和第4节实验部分，尤其是表2和表3，以了解动态聚类和参考池更新的具体实现及在稀疏场景下的优势。

## 🌍 研究背景

长语音分离通常采用分段-分离-拼接范式，但跨段排列对齐是核心挑战。现有方法多依赖额外的说话人日志或聚类，计算开销大且对错误敏感。本文提出一种免训练的动态聚类方法，利用说话人嵌入参考池进行排列对齐，无需额外训练，可即插即用，在稀疏长语音场景中显著提升性能。

## 💡 核心创新

1. 免训练动态聚类，无需额外训练
2. 参考池更新策略，保留最具代表性嵌入
3. 即插即用后处理模块，兼容现有分离模型
4. 对说话人数量估计错误具有鲁棒性

## 🏗️ 模型架构

输入为长语音分离模型的段级嵌入序列。方法维护每个说话人的参考嵌入池，对当前段嵌入与参考池计算余弦相似度，预测排列。参考池通过保留与现有参考总体相似度最高的嵌入进行更新。该模块作为后处理，可插入任何分离模型之后，无需修改原模型。

## 📚 数据集

- WSJ0-2mix（评估，长语音场景）
- Libri2Mix（评估，长语音场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | WSJ0-2mix (dense) | EEND 17.2 | **18.1** | +0.9 |
| SI-SDR (dB) | WSJ0-2mix (sparse) | EEND 12.5 | **14.3** | +1.8 |
| SI-SDR (dB) | Libri2Mix (sparse) | EEND 13.8 | **15.2** | +1.4 |

实验表明，所提方法在密集和稀疏长语音场景下均优于现有方法，尤其在稀疏场景（说话人间隔较长）中提升显著。此外，在未知说话人数且估计错误的情况下，方法仍保持鲁棒性，性能下降较小。

## 🎯 结论与影响

本文提出的免训练动态聚类方法有效解决了长语音分离中的跨段排列对齐问题，作为即插即用模块可显著提升现有分离模型在长语音场景下的性能，尤其适用于稀疏场景。该方法对说话人数量估计错误具有鲁棒性，有望推动长语音分离在实际应用中的落地。

## ⚠️ 局限与未解决问题

方法依赖说话人嵌入的质量，若嵌入区分度不足可能影响性能。实验仅在双说话人场景下验证，未扩展到更多说话人。未报告计算开销和推理延迟，实际部署需进一步评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
