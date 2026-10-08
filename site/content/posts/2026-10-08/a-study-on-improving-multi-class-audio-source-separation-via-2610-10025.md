---
title: "A Study on Improving Multi-class Audio Source Separation Via Decoupled CLAP Query Optimization and an Automated Data Engine"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出自动化数据引擎清洗训练数据，并用两阶段优化类特定 CLAP 控制信号，提升多类音频源分离性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语言查询音频分离</span> <span class="tag-pill tag-pill-soft">#CLAP</span> <span class="tag-pill tag-pill-soft">#数据工程</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.10025</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.10025" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.10025" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出自动化数据引擎清洗训练数据，并用两阶段优化类特定 CLAP 控制信号，提升多类音频源分离性能。
</div>

## 👥 作者与机构

**Amirhossein Hajavi** ¹ · Hanhee Lee · Pushya Jain · Sky Qiao · Emmanuel Ko · Yuanhao Yu · Irina Kezele

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 LASS / 语言查询分离与数据清洗的研究者阅读。建议重点看数据引擎的筛选准则与两阶段 CLAP 优化流程，以及七类声音上的客观对比表；主观实验部分可略读。若关注 CLAP 控制信号微调，可先看方法 §3 与消融。

## 🌍 研究背景

语言查询音频源分离（LASS）用自然语言提取任意声源，主流做法以 CLAP 嵌入作为控制信号驱动分离网络。但适配到特定应用声类时，训练数据含噪、CLAP 语义覆盖不足，导致控制信号不精准、分离性能受限。本文针对这两点，提出数据清洗与类特定控制信号优化框架。

## 💡 核心创新

1. 自动化数据引擎，按质量准则清洗训练数据
2. 两阶段优化类特定 CLAP 控制信号
3. 在七类声音上验证数据精炼与控制优化的增益
4. 17 人主观评测对比基线及商用模型

## 🏗️ 模型架构

输入为混合音频与自然语言查询。先用自动化数据引擎对训练集做质量筛选与标注净化，得到干净训练对；分离主干沿用 CLAP 控制的条件分离网络，将文本经 CLAP 编码为控制嵌入。核心是两阶段优化：第一阶段在清洗数据上微调分离网络，第二阶段针对每个目标声类优化 CLAP 控制信号，使类特定语义更聚焦。输出为提取出的目标声源波形。摘要未给参数量。

## 📚 数据集

- 七类声音自建数据集（训练与评估，具体名称摘要未给出）

## 📊 实验结果

摘要仅说明在七类声音上客观评估，数据精炼与控制信号优化均一致提升分离性能；17 人主观评测显示优化控制信号后的模型优于基线与相近商用模型。摘要未给出 SI-SDR、PESQ 等具体数值，故无法列表对比。

## 🎯 结论与影响

最强结论是数据清洗加类特定 CLAP 控制信号优化能稳定提升多类音频源分离，并在主观听感上超过商用模型。这提示 LASS 落地瓶颈部分在数据与控制信号而非仅网络容量，后续研究可沿数据引擎与语义控制优化方向推进。

## ⚠️ 局限与未解决问题

摘要未给具体指标、数据集名称与参数量，客观提升幅度无法核验；缺少与主流 LASS 方法的定量对比表；数据引擎的筛选准则与误删风险未说明；主观实验仅 17 人，统计效力有限；未报推理延迟与模型规模。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-08/">← 返回 2026-10-08 速递</a></div>
