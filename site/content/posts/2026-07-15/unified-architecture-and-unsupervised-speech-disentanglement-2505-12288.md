---
title: "Unified Architecture and Unsupervised Speech Disentanglement for Speaker Embedding-Free Enrollment in Personalized Speech Enhancement"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出两种模型USEF-PNet和DSEF-PNet，通过统一架构和无监督语音解耦，实现无需说话人嵌入的个性化语音增强，提升鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#个性化语音增强</span> <span class="tag-pill tag-pill-soft">#无监督语音解耦</span> <span class="tag-pill tag-pill-soft">#统一架构</span> <span class="tag-pill tag-pill-soft">#说话人嵌入无关</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2505.12288</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2505.12288" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2505.12288" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两种模型USEF-PNet和DSEF-PNet，通过统一架构和无监督语音解耦，实现无需说话人嵌入的个性化语音增强，提升鲁棒性。
</div>

## 👥 作者与机构

**Ziling Huang** ¹ · Haixin Guan · Yanhua Long

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和个性化语音增强方向的研究者。建议重点阅读§3的模型架构和§4的实验部分，特别是表1和表2的结果。可先看DSEF-PNet的无监督解耦机制。

## 🌍 研究背景

传统语音增强（SE）抑制噪声无需注册语音，而个性化语音增强（PSE）需注册语音提取目标说话人。两者常共享相似架构，但PSE对注册语音变化（如情感）敏感。现有方法依赖说话人嵌入，限制了鲁棒性。本文旨在统一SE和PSE框架，并解决注册语音变化问题。

## 💡 核心创新

1. USEF-PNet统一架构同时处理SE和PSE
2. DSEF-PNet无监督语音解耦分离说话人身份与情感内容
3. 长-短注册配对（LSEP）策略研究注册时长影响

## 🏗️ 模型架构

基于SEF-PNet框架扩展。输入为混合语音和注册语音（可选），通过共享编码器提取特征，经分离模块（可能含Conformer或类似结构）生成目标语音掩码。USEF-PNet统一处理注册语音分支；DSEF-PNet引入解耦模块，通过两个不同注册语音与混合语音配对，强制提取目标语音一致性，从而分离说话人身份。输出为增强后的目标语音。

## 📚 数据集

- Libri2Mix（训练和评估）
- VoiceBank DEMAND（训练和评估）

## 📊 实验结果

摘要未提供具体数值，但声称USEF-PNet和DSEF-PNet在Libri2Mix和VoiceBank DEMAND上均取得显著性能提升，且随机注册时长表现略优。

## 🎯 结论与影响

本文提出的USEF-PNet和DSEF-PNet有效统一了SE和PSE任务，并通过无监督解耦提升了PSE对注册语音变化的鲁棒性。该工作为部署单一模型处理多种增强任务提供了新思路，对工业落地有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提供具体指标对比，缺乏与SOTA方法的定量比较；无监督解耦的有效性需更多消融实验验证；未报告模型参数量和推理延迟。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
