---
title: "Auditory Illusion Benchmark for Large Audio Language Models"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "首个针对大音频语言模型的听觉错觉基准，覆盖音乐、语音等十种错觉，结合人类对照实验揭示模型与人类感知差异。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听觉错觉</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#认知建模</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.02277</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/gillosae/aib" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">gillosae/aib</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.02277" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.02277" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/gillosae/aib" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个针对大音频语言模型的听觉错觉基准，覆盖音乐、语音等十种错觉，结合人类对照实验揭示模型与人类感知差异。
</div>

## 👥 作者与机构

**Hayoon Kim** ¹ · Eunice Hong · Kyogu Lee

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频理解、认知建模及LALM评估研究者。建议重点阅读第3节（基准设计）与第4节（实验结果），可先看表1与图2了解错觉分类和模型表现。若关注人类对比，可详读第5节讨论。

## 🌍 研究背景

听觉错觉长期用于探究人类认知偏差，但现有基准多聚焦视觉错觉或通用音频任务，缺乏对LALM听觉错觉的系统评估。本文旨在填补空白，通过构建首个听觉错觉基准，检验LALM是否复现人类感知倾向，并区分基于知识的先验与低层声学处理。

## 💡 核心创新

1. 首个听觉错觉基准AIB，覆盖十种错觉
2. 标注知识先验，区分低层与高层错觉
3. 结合人类对照实验，直接比较模型与人类
4. 揭示LALM在语言/音乐先验下更类人
5. 公开代码与数据，促进可复现研究

## 🏗️ 模型架构

基准不涉及模型架构，而是评估框架。包含十种听觉错觉刺激，分为音乐、语音、声音三类，每种标注是否依赖知识先验。评估方法为提示LALM生成响应，并与人类受试者对照。

## 📚 数据集

- AIB（评估，十种听觉错觉，含人类标注）

## 📊 实验结果

摘要未提供具体数值，但指出LALM在低层声学错觉上保持信号忠实，而在涉及语言或音乐先验时更接近人类，但无模型完全匹配人类感知轮廓。

## 🎯 结论与影响

听觉错觉可作为LALM认知能力的测试床，揭示其与人类感知的系统差异。该基准为神经黑箱模型提供新视角，推动音频认知理解。对LALM评估与认知建模有重要参考价值，但需扩展更多错觉与模型。

## ⚠️ 局限与未解决问题

仅覆盖十种错觉，样本有限；未提供模型具体响应细节或错误分析；人类对照实验规模未说明；未讨论模型架构差异对结果的影响。

## 🔗 开源资源

- **代码**：<https://github.com/gillosae/aib>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
