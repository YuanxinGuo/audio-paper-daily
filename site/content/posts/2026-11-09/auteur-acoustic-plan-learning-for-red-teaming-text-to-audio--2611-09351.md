---
title: "AUTEUR: Acoustic Plan Learning for Red-Teaming Text-to-Audio Models"
date: 2026-11-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "用结构化声学计划（前景声/上下文/人声属性）做文本到音频模型的红队测试，通过波形反馈的强化学习迭代改写提示词。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#红队测试</span> <span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#安全对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.09351</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.09351" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.09351" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用结构化声学计划（前景声/上下文/人声属性）做文本到音频模型的红队测试，通过波形反馈的强化学习迭代改写提示词。
</div>

## 👥 作者与机构

**Jiashu Zhang** ¹ · Jiaming He · Zheming Zhang · Kaizheng Wang · Bing Li · Zhiyuan Zha · Yi Yu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TTA 安全对齐、红队测试与提示词优化的研究者阅读。若关注语音/音频生成安全，值得通读；重点看 §3 声学计划表示与 RL 反馈回路设计，以及表 2 的四系统攻击成功率对比。若只关心语音增强/分离，可跳过。

## 🌍 研究背景

文本到音频（TTA）模型如 TangoFlux、Kling 已能生成高保真音频，但其安全对齐主要依赖文本侧过滤，容易被绕过生成有害声学内容。现有红队方法多为手工提示或通用 LLM 改写，无法把目标模型实际输出的声音反馈回提示生成，导致攻击成功率低且难以复用。本文要解决的是：如何将测试描述结构化为可学习、可迭代修正的声学计划，并用波形反馈闭环提升攻击成功率与跨模型迁移性。

## 💡 核心创新

1. 提出结构化声学计划表示，拆分前景声/上下文/人声属性
2. 用波形反馈做 RL 训练计划生成器，目标模型冻结
3. 推理时保留前景、仅改写上下文与人声属性的迭代修正策略

## 🏗️ 模型架构

输入为测试意图文本，经计划生成器（基于 LLM 的 SFT 初始化）输出结构化声学计划：前景声、上下文、人声属性三段式字段。计划送入冻结的目标 TTA 模型（TangoFlux / Kling 等）合成波形，音频反馈经评分模块转为奖励信号，用于强化学习微调计划生成器。推理阶段同一模型先生成初始计划，再依据反馈迭代修订上下文与人声属性、保持前景不变，形成闭环。摘要未给出参数量与具体主干网络细节。

## 📚 数据集

- 四个目标 TTA 系统（评估，含 TangoFlux、Kling 等）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 攻击成功率 ASR | TangoFlux | 摘要未给基线值 | **79.4%** | — |
| 攻击成功率 ASR | Kling | 摘要未给基线值 | **95.6%** | — |

摘要报告在四个目标系统上的攻击成功率：TangoFlux 79.4%、Kling 95.6%，并称生成的测试提示可跨开源与闭源模型迁移，暗示存在共享声学脆弱性。但未给出与手工提示、LLM 改写等基线的对照数值，也未报告消融、查询预算与推理开销，实验细节需正文补充。

## 🎯 结论与影响

最强结论是结构化声学计划加波形反馈闭环能显著提升 TTA 红队攻击成功率并跨模型迁移。这提示 TTA 安全对齐需从纯文本过滤转向声学层面防御，对生成式音频平台的合规测试与内容审核有直接参考价值。

## ⚠️ 局限与未解决问题

摘要缺少与现有红队基线的定量对比、消融实验与查询成本分析；攻击成功率定义与人工判定标准未说明；仅四个目标系统，泛化性证据有限；未讨论防御侧缓解措施，伦理与滥用风险需正文交代。

---

<div class="paper-footer"><span>评分：5.8</span><span>原始：5.8</span><a href="/audio-paper-daily/posts/2026-11-09/">← 返回 2026-11-09 速递</a></div>
