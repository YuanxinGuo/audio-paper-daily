---
title: "SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "发布 SmoothConv 与 DuplexConv 两个共 2100 小时中文多方对话语料，含同步说话人级音轨与细粒度标注，并给出分离/MSASR/轮次检测基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#多说话人语音识别</span> <span class="tag-pill tag-pill-soft">#语料库构建</span> <span class="tag-pill tag-pill-soft">#轮次检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11150</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11150" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11150" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布 SmoothConv 与 DuplexConv 两个共 2100 小时中文多方对话语料，含同步说话人级音轨与细粒度标注，并给出分离/MSASR/轮次检测基准。
</div>

## 👥 作者与机构

**Chengyou Wang** ¹ · **Mingchen Shao** ¹ · Chunjiang He · Zeyu Zhu · Jierui Guo · Bingshen Mu · Zikai Liu · Hanke Xie · … 等 3 人

**机构**：西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多方对话建模、语音分离与 MSASR 的研究者与数据工程团队阅读。建议先看语料构建与标注流程一节，再看 SmoothConv Benchmark 的实验设置与表 2 的分离/MSASR 结果；若关注数据管线可重点读 DuplexConv 的自动标注部分。

## 🌍 研究背景

大音频语言模型推动语音交互系统发展，但需建模轮次切换、重叠语音与说话人协调等复杂行为。现有多方对话语料多为英文，中文语料常缺同步的说话人级音轨与完整标注，难以支撑分离、MSASR 与轮次检测的统一评测。本文构建两个互补的中文多方对话语料并给出基准，以填补数据与评测缺口。

## 💡 核心创新

1. SmoothConv 人工校验语料，提供可靠评测
2. DuplexConv 可扩展自动标注管线，支撑大规模训练
3. 同步说话人级音轨 + 多维细粒度标注
4. 发布 SmoothConv Benchmark 覆盖三类任务

## 🏗️ 模型架构

论文为语料与基准工作，非单一网络。数据侧：采集多方对话录音，经说话人日志与对齐得到同步说话人级音轨，SmoothConv 由人工校验，DuplexConv 由自动管线批量标注，输出转写、说话人、时间戳与重叠信息。基准侧：在 SmoothConv Benchmark 上分别搭建语音分离、MSASR 与轮次检测基线系统进行评测。

## 📚 数据集

- SmoothConv（人工校验，评估/分析）
- DuplexConv（自动标注，训练，大规模）
- SmoothConv Benchmark（评测基准）

## 📊 实验结果

摘要仅说明在语音分离、MSASR 与轮次检测三类任务上验证了资源有效性，未给出具体指标数值、基线名称或提升幅度，故无法列出定量结果表。需查阅原文实验章节获取 SI-SDR、WER 等具体数据。

## 🎯 结论与影响

最强结论是同步说话人级音轨加多维标注的中文多方对话语料可有效支撑分离、MSASR 与轮次检测建模。该资源有望成为中文多方语音交互研究的数据基础，推动统一评测。工业上可用于会议转录、智能助手多方交互等场景的数据与评测支撑。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果与基线对比，难以判断语料相对现有中文多方数据的实际增益；DuplexConv 自动标注质量缺乏量化验证；未提及说话人数量、场景多样性、录音设备与领域偏差，也未报告基准系统的推理效率。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
