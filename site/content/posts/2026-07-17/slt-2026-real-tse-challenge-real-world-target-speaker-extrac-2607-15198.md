---
title: "SLT 2026 REAL-TSE Challenge: Real-world Target Speaker Extraction from Conversational Recordings"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "SLT 2026 REAL-TSE挑战赛聚焦真实对话录音中的目标说话人提取，提供在线和离线双赛道，并引入TER等新指标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#真实场景</span> <span class="tag-pill tag-pill-soft">#挑战赛</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15198</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15198" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15198" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>SLT 2026 REAL-TSE挑战赛聚焦真实对话录音中的目标说话人提取，提供在线和离线双赛道，并引入TER等新指标。
</div>

## 👥 作者与机构

**Shuai Wang** ¹ · Zihan Qian · Ke Zhang · Jiangyu Han · Zikai Liu · Xiaoyang Yu · Haoyu Li · Marc Delcroix · … 等 4 人

**机构**：上海交通大学 · 南京大学 · 香港中文大学 · 新加坡国立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事目标说话人提取、语音分离的研究者阅读。建议重点读§2任务定义、§4基线系统、§6条件分析。可对比各提交系统的设计差异。

## 🌍 研究背景

目标说话人提取（TSE）旨在从多说话人混合中提取特定目标语音，传统方法在模拟朗读语音上表现良好，但真实对话场景存在自然重叠、混响、噪声、信道失配等问题。现有基准缺乏真实录音评估，REAL-TSE挑战赛填补了这一空白，提供包含中英文的对话录音数据集，并设置在线低延迟和离线全上下文两个赛道。

## 💡 核心创新

1. 首次在真实对话录音上评估TSE
2. 双赛道设计：在线低延迟与离线全上下文
3. 引入Token Error Rate (TER)作为主要指标
4. 提供中英文双语真实对话数据集
5. 系统化分析不同条件（重叠、噪声等）下的性能

## 🏗️ 模型架构

挑战赛提供两个基线系统：基于Conformer的离线模型和基于TCN的在线模型。输入为多说话人混合音频和目标说话人注册语音，通过编码器提取特征，经分离网络（Conformer或TCN）生成目标说话人掩码，再与混合特征相乘得到目标语音。输出为估计的目标说话人波形。

## 📚 数据集

- REAL-TSE数据集（训练/评估，包含中英文真实对话录音，约100小时）
- 模拟数据（训练，用于数据增强）

## 📊 实验结果

摘要未提供具体数值结果，但描述了评估指标包括TER、SpkSim、DNSMOS和F1。挑战赛将报告各提交系统在不同条件（如重叠程度、信噪比、信道）下的性能，并分析在线与离线赛道的差异。

## 🎯 结论与影响

REAL-TSE挑战赛推动了目标说话人提取从模拟场景向真实对话场景的转变，通过双赛道设计兼顾了实时性和精度。其数据集和基线将为后续研究提供标准化评估平台，有望促进TSE技术在会议转录、助听器等实际应用中的落地。

## ⚠️ 局限与未解决问题

数据集规模有限（约100小时），且仅涵盖中英文，可能限制泛化性。未提供基线系统的详细参数量和推理延迟。挑战赛结果可能受提交系统多样性影响，缺乏对单一方法的深入消融。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
