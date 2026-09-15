---
title: "The VoiceMOS Challenge 2026: Evaluating Speech Enhancement, Emotional TTS and Accented TTS Systems"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音质量评估"]
summary: "VoiceMOS Challenge 2026 第五届，聚焦语音领域设三条赛道：增强语音绝对/比较评分、情感TTS自然度与情感、编解码合成语音的说话人与口音相似度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#情感TTS</span> <span class="tag-pill tag-pill-soft">#口音TTS</span> <span class="tag-pill tag-pill-soft">#MOS预测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.13792</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.13792" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.13792" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VoiceMOS Challenge 2026 第五届，聚焦语音领域设三条赛道：增强语音绝对/比较评分、情感TTS自然度与情感、编解码合成语音的说话人与口音相似度。
</div>

## 👥 作者与机构

**Wen-Chin Huang** ¹ · Wei Wang · Marvin Sach · Xiaoxue Gao · Nicholas Sanders · Erica Cooper · Toda Tomoki

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 MOS 自动预测、语音增强评测、TTS 主观评价的研究者与评测组织者阅读。建议重点看三条赛道的任务定义、基线设置与 top 系统方法对比，以及参与者反馈与未来方向一节；若只关心语音增强评测，可先看增强赛道结果表与所用数据集说明。

## 🌍 研究背景

自动预测主观语音评价（MOS 等）长期依赖昂贵人工听测，VoiceMOS Challenge 系列自 2022 年起提供统一数据与基线推动该方向。此前一届将范围扩展到音乐与通用音频，导致评价目标分散。本文回归语音本体，针对增强语音、情感 TTS、基于编解码的带口音 TTS 三类系统，分别设计绝对/比较类别评分、自然度与情感、说话人与口音相似度预测任务，检验现有 MOS 预测模型在细粒度感知维度上的泛化能力。

## 💡 核心创新

1. 三赛道设计：增强语音绝对+比较类别评分预测
2. 情感 TTS 赛道同时预测自然度与情感相关维度
3. 编解码 TTS 赛道预测说话人与口音相似度
4. 汇聚 18 支队伍并系统总结 top 系统与反馈

## 🏗️ 模型架构

本文为挑战赛总结报告，非单一模型论文。整体流程为：各赛道组织方提供训练/开发/评估集与官方基线（基于自监督语音表征如 wav2vec2 / WavLM 特征加注意力池化回归或排序头），参赛队伍在此基础上改进主干、池化与损失（如成对排序损失、多任务头）。摘要未给出统一网络结构或参数量，具体模块需参见各参赛系统描述。

## 📚 数据集

- 增强语音赛道数据集（训练/评估，含绝对与比较类别评分）
- 情感 TTS 赛道数据集（训练/评估，含自然度与情感标注）
- 编解码 TTS 赛道数据集（训练/评估，含说话人与口音相似度标注）

## 📊 实验结果

摘要仅说明共 18 支队伍参赛，且大多数队伍成功超越官方基线，未给出任何具体指标数值、测试集名称或提升幅度，因此无法列出定量结果表。具体各赛道的相关性指标（如 SRCC / MSE）与 top 系统得分需查阅论文正文。

## 🎯 结论与影响

最强结论是：在语音本体的三类主观评价任务上，现有 MOS 预测方法经适当改造后普遍可超过官方基线，说明该方向仍有稳定提升空间。对后续研究而言，比较类别评分、情感与口音相似度等细粒度维度可能成为新评测标准；对工业落地，意味着可用自动预测部分替代昂贵听测，用于增强与 TTS 系统的快速迭代筛选。

## ⚠️ 局限与未解决问题

作为挑战赛报告，摘要未披露各赛道数据规模、标注者数量与一致性，也未给出具体指标数值，难以判断提升幅度是否显著。缺少跨赛道方法对比与消融分析，且参赛队伍自选方法差异大，结论的普适性受限；此外未提及推理延迟与模型规模等实用指标。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：6.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
