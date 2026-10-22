---
title: "Heard But Not Said: Prompting Understates Temporal Information of Musical Moments in Frozen Large Audio-Language Models"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "用配对查询探针检验冻结大型音频语言模型能否定位音乐片段中的时刻，发现提示方式低估了模型的时序验证能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#音乐时刻定位</span> <span class="tag-pill tag-pill-soft">#时序推理</span> <span class="tag-pill tag-pill-soft">#探测分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29256</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29256" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29256" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用配对查询探针检验冻结大型音频语言模型能否定位音乐片段中的时刻，发现提示方式低估了模型的时序验证能力。
</div>

## 👥 作者与机构

**Eunsik Shin** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究 LALM 时序理解与音乐信息检索交叉方向的研究者阅读。值得通读，重点看 §3 的配对查询探针设计与 §4 中三种提取方式（full-track prompting / windowed yes/no / attention）的对比实验。若只关心结论，可先看表 2 与关于 30s padded encoder 的讨论。

## 🌍 研究背景

大型音频语言模型（LALM）已能描述音乐内容，但在给定文字描述后定位对应时间片段仍表现不佳。此前工作多直接用整轨提示（full-track prompting）评估，若失败便归因于模型缺乏时序信息。然而提示接口本身可能是瓶颈：整轨输入下模型难以显式输出时间跨度，注意力也未必对齐。本文要区分“模型没有时序信息”与“提取方式受限”两种解释。

## 💡 核心创新

1. 构建基于 Slakh2100 stem 激活的配对查询探针（state query 与 change query 对应同一时间跨度）
2. 系统对比三种时间跨度提取方式：整轨提示、窗口化 yes/no 打分、注意力
3. 控制前文音频长度，量化上下文对 change query 的影响
4. 揭示 30s padded encoder 无法从上下文恢复时序信息

## 🏗️ 模型架构

方法不训练新网络，而是对冻结的 LALM 做探测。输入为音乐音频（Slakh2100 混音），按 stem 激活标注出目标时间跨度，构造两类查询：state query 描述该跨度内的乐器组合，change query 描述进入该跨度时的变化事件。评估路径有三：一是整轨提示，让模型直接生成/回答时刻；二是窗口化 yes/no 打分，将候选片段（含不同长度前文）送入模型判断是否匹配；三是读取模型注意力，检验其能否自行定位。输出为各路径下的匹配分数或注意力定位结果。

## 📚 数据集

- Slakh2100（构建探针查询与评估，基于 stem 激活）

## 📊 实验结果

摘要未给出具体数值指标，仅作定性结论：state query 在无上下文时即高于基线；change query 在多数短片段模型中随前文上下文增加而改善；30s padded encoder 无类似恢复。整轨提示与注意力几乎无法反映上述能力差异，说明提示失败低估了模型可验证（verify）的能力，但并未低估其可定位（locate）的能力。

## 🎯 结论与影响

最强结论是：LALM 的时序能力被提示接口系统性低估，且低估幅度由查询类型与编码器决定。这提示后续音乐时序定位研究应区分“验证”与“定位”两种能力，并谨慎使用整轨提示作为评测协议。对工业落地而言，基于窗口化打分的检索式接口可能比端到端时间戳生成更可靠。

## ⚠️ 局限与未解决问题

仅基于 Slakh2100 合成分轨数据，真实混音与多样音乐风格泛化未知；探针依赖 stem 激活标注，事件定义较人工；未报告推理延迟与计算开销；对比的冻结 LALM 数量与具体模型未在摘要说明；缺少对注意力路径失效原因的深入分析。

---

<div class="paper-footer"><span>评分：6.2</span><span>原始：6.2</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
