---
title: "Self-Supervised Speech Representations Track Spoken Language Convergence to Adult Models in Infants and Children Who Are Deaf/Hard-of-Hearing"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音发展评估"]
summary: "利用HuBERT嵌入距离追踪聋儿与照护者语音的收敛，实现语言发展的可扩展评估。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音发展评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音嵌入</span> <span class="tag-pill tag-pill-soft">#儿童语音</span> <span class="tag-pill tag-pill-soft">#听力障碍</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.20396</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.20396" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.20396" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用HuBERT嵌入距离追踪聋儿与照护者语音的收敛，实现语言发展的可扩展评估。
</div>

## 👥 作者与机构

**L. Choy** ¹ · A. S. Khan · S. Patrizi · D. Ye · J. Gross · M. Cychosz

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音发展、计算语言学和临床研究人员。建议重点阅读方法部分（嵌入提取与距离计算）和结果部分（与标准化测试的相关性）。可先看摘要和图表，再深入方法细节。

## 🌍 研究背景

语言发展研究中，儿童语音逐渐向成人模式收敛是核心指标，但传统测量依赖人工转录和语言专家，难以跨语言和大规模应用。本文利用自监督语音表示（HuBERT）直接从长时录音中捕捉这一收敛过程，无需转录，为语言发展评估提供可扩展方案。

## 💡 核心创新

1. 使用HuBERT嵌入距离作为语音收敛的单一指标
2. 在自然日常录音中验证，而非实验室环境
3. 控制音高和发声时长等混淆因素
4. 与多种标准化语言测试建立关联
5. 支持跨语言、无需专家标注的评估

## 🏗️ 模型架构

输入为儿童和照护者的语音片段，使用HuBERT-BASE提取每帧嵌入，计算儿童与照护者嵌入之间的平均距离（如余弦距离），并控制音高和时长。该距离作为语音收敛的度量，与标准化语言测试分数进行相关分析。

## 📚 数据集

- 儿童和照护者日常录音（>925小时观察，训练/评估）

## 📊 实验结果

摘要未提供具体数值，但报告嵌入距离随听力年龄增加而减小，且与多种标准化语言测试相关，表明该指标的有效性。

## 🎯 结论与影响

本研究证明自监督语音嵌入可有效追踪儿童语音向成人模式的收敛，为语言发展评估提供可扩展、语言中性的方法。对临床和跨语言研究有重要影响，可能推动自动化评估工具的开发。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：样本仅限聋儿群体，未验证正常听力儿童；未报告与其他基线方法的对比；未提供具体相关性和效应量；未讨论计算成本。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
