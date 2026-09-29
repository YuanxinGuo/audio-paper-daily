---
title: "JazzSAMBA: A Synchronous and Asynchronous Multi-take Band Audio Dataset of Jazz Standards for Live Music Models"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "发布首个爵士标准曲多轨数据集JazzSAMBA，含同步/异步录制、分轨音频与和弦小节标注，并给出爵士合奏分离与伴奏基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#音乐生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.34931</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.34931" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.34931" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布首个爵士标准曲多轨数据集JazzSAMBA，含同步/异步录制、分轨音频与和弦小节标注，并给出爵士合奏分离与伴奏基线。
</div>

## 👥 作者与机构

**Phillip Long** ¹ · Jacob Nguyen · Jace Hosto · Gage Hosto · Jett Takazawa · Fares Nofal · Sebastian Stade · Nithya Shikarpur · … 等 4 人

**机构**：加州大学圣地亚哥分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐分离、伴奏生成与MIR的研究者阅读。建议通读§3数据集构建与§4任务定义，重点看表2的分离基线与伴奏消融。若只关心分离，可直接看分离实验与stem设置；若关心标注，看小节/和弦/独奏者时间戳部分。

## 🌍 研究背景

音乐机器学习多依赖pop/rock多轨语料（如MUSDB18），爵士以即兴为核心，缺少干净分轨、带和弦与小节标注的标准曲合奏数据。现有爵士数据多为混音或转录标注，难以支撑chart-conditioned伴奏与combo分离。本文构建JazzSAMBA，提供同步与异步两种录制协议、preferred/alternate take及时间对齐标注，填补该空白。

## 💡 核心创新

1. 首个爵士标准曲多轨数据集，含同步与异步两种录制协议
2. 提供preferred/alternate take及小节、和弦、段落、独奏者时间标注
3. 给出爵士combo源分离基线与chart-conditioned伴奏消融

## 🏗️ 模型架构

论文为数据集与基线论文，未提出统一网络。分离基线采用分轨音频作为监督，输入混合信号，输出drums/bass/piano/trumpet/saxophone多stem；伴奏任务以和弦chart为条件，输入混合或伴奏轨，生成对应伴奏。摘要未给出具体主干网络名与参数量，仅说明提供per-stem音频、mixtures与MIDI。

## 📚 数据集

- JazzSAMBA（训练/评估，76首标准曲，8位乐手，drums/bass/piano/trumpet/saxophone，含分轨、混音与MIDI）

## 📊 实验结果

摘要仅说明在JazzSAMBA上演示了爵士combo源分离基线与chart-conditioned伴奏消融，未给出SI-SDR、SDR、PESQ等具体数值，也未报告与SEPFormer、BSRNN等方法的对比。因此无法量化其相对现有音乐分离系统的提升，需查阅原文实验表。

## 🎯 结论与影响

最强结论是JazzSAMBA提供了首个带同步/异步协议与丰富时间标注的爵士标准曲多轨数据集，可支撑combo分离与chart-conditioned伴奏。后续研究可基于该数据训练爵士专用分离与伴奏模型，工业上可用于爵士练习、自动伴奏与教育工具。

## ⚠️ 局限与未解决问题

仅8位乐手、76首标准曲，规模与风格多样性有限；摘要未给出分离指标、推理延迟与强基线对比，难以判断数据难度与实用性；同步/异步协议差异对模型泛化的影响未量化；标注一致性未报告。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
