---
title: "Absolute Quality Ratings of Speech Enhancement Systems by Listeners of Different Ages and Degrees of Hearing Loss"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "对比40名年轻正常听力与67名老年（含不同程度听力损失）听者对语音增强系统的主观绝对质量评分，发现老年组对系统间差异的区分度明显收缩。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#主观评测</span> <span class="tag-pill tag-pill-soft">#听力损失</span> <span class="tag-pill tag-pill-soft">#语音质量评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18714</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18714" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18714" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>对比40名年轻正常听力与67名老年（含不同程度听力损失）听者对语音增强系统的主观绝对质量评分，发现老年组对系统间差异的区分度明显收缩。
</div>

## 👥 作者与机构

**Matteo Torcoli** ¹ · Chih-Wei Wu · Andrea Esposito · Phillip A. Williams · Katrien Cambier · William Wolcott · Antonio Curci · Nicholas S. Reed · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强主观评测、助听器/听力辅助算法、以及 MOS 类指标研究的读者。建议重点看实验设计（被试筛选、听力图分层）与结果中"差异收缩"的统计部分，而非方法本身。若你只关心 SE 模型结构，可略读；若你在做面向老年用户的质量评估，值得通读。

## 🌍 研究背景

语音增强（SE）主要服务于老年及年龄相关听力损失人群，但当前 SQ 主观评测几乎全部由年轻正常听力听者完成，其评分能否外推到老年听者尚不清楚。已有 MOS 类指标（如 PESQ、POLQA、DNSMOS）也多在年轻听者数据上校准。本文要回答：不同年龄与听力图听者对 SE 系统的绝对质量评分是否存在系统性差异，以及听力损失程度是否调节这种差异。

## 💡 核心创新

1. 首次系统对比年轻正常听力与老年多听力图听者的 SE 绝对 SQ 评分
2. 发现老年组对 SE 系统间差异的区分度显著收缩
3. 指出听力损失严重度降低绝对评分但不解释收缩现象
4. 识别出少数老年听者呈年轻式评分模式，提示外周听力不足以解释

## 🏗️ 模型架构

本文为主观听音实验研究，无神经网络架构。流程为：被试筛选（40 名 20–30 岁正常听力 + 67 名 60–95 岁多听力图老年听者）→ 测试材料为带真实背景噪声的自然对话 → 经若干 SE 系统处理 → 听者给出绝对 SQ 评分。分析层面按年龄组与听力状态分层，比较各 SE 系统间评分的可分性，并考察听力损失严重度与评分收缩的关联。

## 📚 数据集

- 自然对话 + 真实背景噪声测试材料（评估，自建主观听音集）

## 📊 实验结果

摘要未给出具体数值指标（如 MOS、SI-SDR、PESQ 或统计量）。核心定性结论为：年轻听者能清晰区分的 SE 系统间 SQ 差异，在老年组中变小甚至不可分，且与听力状态无关；听力损失越重绝对评分越低，但并未强烈调节差异收缩；少数听力图混合的老年听者表现出接近年轻听者的评分模式。

## 🎯 结论与影响

最强结论是：SE 系统的主观质量差异在老年听者中会被显著压缩，仅靠年轻正常听力听者的评分无法代表目标用户群。这提示后续 SE 评测与 MOS 指标需纳入年龄与听力图多样性，对助听器与消费音频的工业评测流程有直接影响。

## ⚠️ 局限与未解决问题

摘要未报告效应量、统计检验细节与样本听力图分布；未说明所用 SE 系统数量与类型；未给出可复现的评分量表与实验协议；缺乏对"收缩"机制的解释性实验（如认知、中枢因素）。作为审稿人会要求补充统计功效分析与跨语言/跨材料泛化验证。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
