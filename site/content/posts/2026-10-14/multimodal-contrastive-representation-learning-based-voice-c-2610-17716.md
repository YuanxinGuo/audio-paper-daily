---
title: "Multimodal Contrastive Representation Learning Based Voice Conversion for Electrolaryngeal Speech Enhancement"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用语音-文本跨模态对比学习与跨阶段对比学习，把多模态表征迁移到仅语音输入的电子喉语音转正常语音任务。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音转换</span> <span class="tag-pill tag-pill-soft">#多模态对比学习</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#病理语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17716</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17716" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17716" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用语音-文本跨模态对比学习与跨阶段对比学习，把多模态表征迁移到仅语音输入的电子喉语音转正常语音任务。
</div>

## 👥 作者与机构

**Ding Ma** ¹ · Jinyi Mi · Jiajun He · Kazuhiro Kobayashi · Naoki Nishio · Tomoki Toda

**机构**：名古屋大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音转换、病理/辅助语音、多模态表征学习的读者。建议通读，重点看 §3 的跨模态与跨阶段对比学习设计，以及表 1/表 2 与 speech-only、multimodal baseline 的对比；若关注落地，先看推理是否仍为纯语音输入这一节。

## 🌍 研究背景

电子喉（EL）语音与正常语音存在严重声学失配，自然度与可懂度差。此前 EL2SP 多依赖序列到序列语音转换（如基于 Transformer / Conformer 的 VC），但失配使模型难以学到鲁棒的中间表征。多模态方法引入文本可缓解，却常在推理时需要文本，破坏架构与推理简洁性。本文要解决的是：如何把多模态知识迁移到仅语音输入的 EL2SP，同时保持推理简单。

## 💡 核心创新

1. 语音-文本融合 + 跨模态对比学习，构建语义一致表征空间
2. 跨阶段对比学习，用融合表征作固定目标指导纯语音表征
3. 推理阶段仅需语音输入，保留架构与推理简洁性
4. 在 EL2SP 上同时超越 speech-only 与 multimodal baseline

## 🏗️ 模型架构

输入为 EL 语音声学特征与对应文本表征。主干沿用序列到序列语音转换框架（摘要未指明具体网络，推测为 Conformer/Transformer 类）。关键模块有二：一是跨模态对比学习，将 EL 语音与文本表征融合，拉近语义一致样本、推远不一致样本，得到多模态表征用于目标语音生成；二是跨阶段对比学习，把融合表征冻结为固定目标，约束纯语音分支学到的表征向其对齐，从而把多模态知识蒸馏进仅语音推理路径。输出为目标正常语音。摘要未给参数量。

## 📊 实验结果

摘要仅称所提方法在 EL2SP 上一致优于 speech-only 与 multimodal-based 两类基线，未给出 SI-SDR、PESQ、WER、MOS 等具体数值，也未说明数据集规模与评测集名称，因此无法列出量化结果表。需查阅正文确认对比方法与统计显著性。

## 🎯 结论与影响

最强结论是：跨模态 + 跨阶段对比学习可在不增加推理期文本依赖的前提下，把多模态知识迁移到纯语音 EL2SP 并稳定超过两类基线。对病理语音转换与多模态表征迁移方向有参考价值，提示对比学习可作为多模态到单模态的知识桥梁。工业上有利于低延迟、纯语音输入的辅助发声设备落地。

## ⚠️ 局限与未解决问题

摘要未给任何量化指标、数据集与消融，难以判断提升幅度与各模块贡献；跨阶段对比的固定目标是否引入教师偏差、文本缺失或错误时鲁棒性如何均未说明；未报推理延迟与参数量，也未与最新 EL2SP SOTA 做全面对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
