---
title: "KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音克隆"]
summary: "基于FishAudio-S2-Pro，通过语言标签提示、RL微调和词汇匹配提升跨语言语音克隆的语音质量和领域术语发音。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音克隆</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#跨语言语音克隆</span> <span class="tag-pill tag-pill-soft">#多语言TTS</span> <span class="tag-pill tag-pill-soft">#语言标签提示</span> <span class="tag-pill tag-pill-soft">#强化学习微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07240</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07240" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07240" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>基于FishAudio-S2-Pro，通过语言标签提示、RL微调和词汇匹配提升跨语言语音克隆的语音质量和领域术语发音。
</div>

## 👥 作者与机构

**Seymanur Akti** ¹ · Alexander Waibel

**机构**：卡尔斯鲁厄理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音克隆、多语言TTS的研究者。可重点阅读§3方法部分（语言标签提示和词汇匹配），以及§4实验结果。建议对比基线方法理解改进幅度。

## 🌍 研究背景

跨语言语音克隆旨在用源语言参考语音保留说话人身份，生成目标语言语音。现有方法在口音变化和领域特定词汇上常出现可懂度和自然度下降。IWSLT 2026赛道聚焦此任务。本文基于FishAudio-S2-Pro多语言TTS模型，针对上述问题提出改进。

## 💡 核心创新

1. 引入语言标签提示增强语言控制，减少口音泄漏
2. 应用强化学习微调提升任务适应性
3. 提出参考条件词汇匹配方法改善领域术语发音

## 🏗️ 模型架构

基于FishAudio-S2-Pro多语言TTS模型。输入：文本和语言标签；主干：FishAudio-S2-Pro；关键模块：语言标签提示（在输入中拼接语言token）、RL微调（使用奖励模型优化可懂度）、词汇匹配（参考文本与目标文本对齐后替换发音）。输出：目标语言语音。

## 📚 数据集

- IWSLT 2026 Cross-Lingual Voice Cloning track数据集（训练/评估）

## 📊 实验结果

摘要未提供具体数值。实验表明语言标签提示带来最大增益，词汇匹配在词汇重叠的子集上持续改进。RL微调提升了可懂度。

## 🎯 结论与影响

本文通过语言标签提示、RL微调和词汇匹配有效提升了跨语言语音克隆的质量，尤其在领域术语发音上。语言标签提示简单有效，可作为后续工作的标准组件。对工业语音翻译系统有实用价值。

## ⚠️ 局限与未解决问题

未报告具体指标和对比基线，缺乏定量分析。词汇匹配依赖词汇重叠，泛化性未知。未讨论推理效率。RL微调可能引入不稳定。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
