---
title: "AOR-Bench: Do Large Audio Language Models Over-Refuse Pseudo-Harmful Queries?"
date: 2026-08-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频安全"]
summary: "首个针对大音频语言模型的过度拒绝基准AOR-Bench，含3000个伪有害音频样本，评估12个模型发现过度拒绝普遍存在，并探索了两种缓解策略。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#过度拒绝</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#安全对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.21147</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.21147" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.21147" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个针对大音频语言模型的过度拒绝基准AOR-Bench，含3000个伪有害音频样本，评估12个模型发现过度拒绝普遍存在，并探索了两种缓解策略。
</div>

## 👥 作者与机构

**Jiaxi Yang** ¹ · Chaewan Chun · Jason Lucas · Yuchen Yang · Dongwon Lee

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、大模型对齐方向的研究者阅读。建议重点看第3节（基准构建）和第4节（评估结果），可先浏览图1和表2了解主要发现。若关注缓解方法，可看第5节。

## 🌍 研究背景

大音频语言模型（LALMs）在多种音频任务中表现优异，但其安全对齐至关重要。拒绝机制虽能防止有害响应，但会导致过度拒绝，错误拒绝良性查询。音频领域尤其复杂，因为孤立看似有害的语音结合背景声可能变得良性。现有研究缺乏针对LALMs的过度拒绝基准，本文填补此空白。

## 💡 核心创新

1. 首个LALM过度拒绝基准AOR-Bench
2. 包含3000个伪有害音频样本，覆盖6个场景类别
3. 系统评估12个代表性LALM，揭示过度拒绝普遍性
4. 探索CoT和激活引导两种轻量缓解策略
5. 分析安全判断模式，提供深入洞察

## 🏗️ 模型架构

AOR-Bench是一个基准测试，包含3000个伪有害音频样本，分为6个场景类别。评估12个LALM，来自6个主要模型家族。缓解策略包括Chain-of-Thought（CoT）和激活引导（activation steering）。

## 📚 数据集

- AOR-Bench（评估，3000个伪有害音频样本，6个场景类别）

## 📊 实验结果

摘要未提供具体量化指标，但指出过度拒绝普遍存在，并揭示了安全判断的若干重要模式。缓解策略（CoT和激活引导）初步探索，但未给出具体效果数值。

## 🎯 结论与影响

本文首次系统研究LALMs的过度拒绝问题，构建了AOR-Bench基准，发现过度拒绝普遍存在，并探索了缓解策略。该工作为音频安全对齐提供了重要评估工具，推动后续研究关注音频特有的安全挑战，对实际部署中的安全性与可用性平衡有指导意义。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为基准，可能缺乏对真实世界音频多样性的覆盖，且缓解策略效果未量化。此外，未讨论模型规模、训练数据等对过度拒绝的影响，也未提供与其他模态（如文本）过度拒绝的对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-27/">← 返回 2026-08-27 速递</a></div>
