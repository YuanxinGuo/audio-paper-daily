---
title: "Human-Likeness and Conversational Preference Diverge for Synthesized Agent Speech in Customer-Service Calls"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "在客服场景配对听测中发现，合成语音的拟人度与对话偏好排序不一致，且单音色测试会误判系统优劣。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.2</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#主观评测</span> <span class="tag-pill tag-pill-soft">#人机交互</span> <span class="tag-pill tag-pill-soft">#客服语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.16051</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.16051" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.16051" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在客服场景配对听测中发现，合成语音的拟人度与对话偏好排序不一致，且单音色测试会误判系统优劣。
</div>

## 👥 作者与机构

**Jeffrey M. Girard** ¹ · Antony D'Avirro · Jason Z. Zheng · Jacqueline R. Vertino · Benjamin Peloquin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TTS 主观评测、对话式语音产品选型的研究者与工程团队阅读。建议重点看 Study 1/2 的实验设计与偏好-拟人度分歧的统计部分，以及自动自然度分数失效的分析；结论部分可快速浏览。

## 🌍 研究背景

TTS 主观评测长期以拟人度（naturalness/MOS）为核心指标，工业选型也常以 MOS 或自动自然度分数（如 DNSMOS 类）为准。但真实客服场景中用户关心的是否愿意与该语音对话，而配对偏好测试很少被用于 TTS 评测，拟人度与对话偏好之间的关系缺乏实证。本文要回答：两者是否一致，以及单系统单音色测试是否会误导选型。

## 💡 核心创新

1. 用配对选择测试同时测拟人度与对话偏好
2. 跨 6 个商用 TTS、每系统 8 音色的方差分解
3. 引入演员原始录音作为真人上界对照
4. 检验三种自动自然度分数与两类主观判断的相关性

## 🏗️ 模型架构

非模型论文，属主观评测研究。刺激材料为演员即兴扮演客服代表的 120 个对话轮次；Study 1 中每轮由两个商用 TTS 系统（共 6 系统、每系统 8 音色）合成同一文本进行配对比较；Study 2 中一方为演员原始录音、另一方为系统合成。听者做二选一判断（更拟人 / 更愿意对话），并分析语速、停顿、音高变化等声学特征与判断的关系，同时对比三种自动自然度分数。

## 📚 数据集

- 自建客服对话轮次语料（120 turns，演员即兴录制，用于合成与评估）
- 6 个商用 TTS 系统输出（每系统 8 音色，用于配对听测）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 系统被选优于真人的比例（拟人度） | 自建客服轮次配对听测 | 演员原始录音 | **19%** | — |
| 系统被选优于真人的比例（对话偏好） | 自建客服轮次配对听测 | 演员原始录音 | **36%（最优系统 49%）** | — |

摘要给出关键数字：拟人度任务中系统胜过演员仅 19%，对话偏好任务升至 36%，最受偏好系统达 49%，说明两判断显著分歧。方差分解显示系统内音色差异约为系统间差异的四分之三。三种自动自然度分数中两个与更低拟人度相关，且均不能预测对话偏好；听者偏好语速更快、子句间停顿更少，对话偏好还偏好更大音高变化。

## 🎯 结论与影响

最强结论是拟人度与对话偏好可给出不同的系统排序，仅测拟人度或每系统只测一个音色会误判用户真正愿意对话的语音。这提示 TTS 评测应加入偏好类任务并覆盖多音色，对客服等对话式语音产品的选型与自动指标设计有直接影响。

## ⚠️ 局限与未解决问题

仅限客服即兴语料与 6 个商用系统，未覆盖其他语言与情感场景；未报告听者规模、置信区间与统计检验细节；自动自然度分数只测三种；未给出推理延迟等工程指标；偏好与声学特征的因果性未验证。

---

<div class="paper-footer"><span>评分：6.2</span><span>原始：6.2</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
