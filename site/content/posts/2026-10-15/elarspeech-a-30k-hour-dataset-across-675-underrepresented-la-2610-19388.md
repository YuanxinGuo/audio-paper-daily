---
title: "ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented Languages for Long-Tail Multilingual Speech Technologies"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "发布 ELARSpeech，30,202 小时、675 种低资源语言的语音数据集，支持 ASR/TTS 长尾多语言建模与伪标签实验。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言语音</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.19388</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.19388" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.19388" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布 ELARSpeech，30,202 小时、675 种低资源语言的语音数据集，支持 ASR/TTS 长尾多语言建模与伪标签实验。
</div>

## 👥 作者与机构

**Sangmin Lee** ¹ · Yejin Jeon · David Ifeoluwa Adelani

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多语言 ASR/TTS、低资源语音、数据构建的研究者与工程团队阅读。建议先看数据构建与清洗流程一节，再看 ASR/TTS 实验与伪标签消融表，最后看语音表征分析部分以了解长尾迁移瓶颈。若只关心建模方法可略读语料统计细节。

## 🌍 研究背景

多语言语音建模近年进展显著（如 Whisper、MMS、SeamlessM4T 等大规模多语言模型），但训练资源与评测基准仍严重偏向高资源语言，语言长尾覆盖不足。现有低资源语料规模小、领域单一、标注稀缺，导致 ASR/TTS 在 675 类濒危/低资源语言上迁移困难。本文从 Endangered Languages Archive 构建大规模语料，旨在为长尾多语言语音技术提供资源与测试平台。

## 💡 核心创新

1. 从 ELAR 构建 30,202 小时、675 种低资源语言语料
2. 融合人工标注与无标注录音，支持伪标签半监督训练
3. 同时训练并开源 ASR 与 TTS 模型及完整数据流水线
4. 通过语音表征分析揭示长尾迁移的剩余局限

## 🏗️ 模型架构

论文以数据资源为核心，未提出单一新网络。ASR 侧基于现有多语言预训练模型（如 Whisper / MMS 类编码器-解码器）在 ELARSpeech 上微调，并利用无标注数据做伪标签自训练；TTS 侧采用多语言声学模型 + 声码器流水线，在低资源语言上微调。输入为多语言语音波形/梅尔特征，输出为文本或合成语音。摘要未给出具体参数量与模块细节。

## 📚 数据集

- ELARSpeech（训练/评估，30,202 小时，675 种低资源语言，源自 Endangered Languages Archive）

## 📊 实验结果

摘要未给出具体 SI-SDR / WER / MOS 等数值，仅定性说明 ELARSpeech 可支持将 ASR 与 TTS 能力扩展到多种低资源语言，且对无标注数据做伪标签能带来进一步收益；同时语音表征分析显示现有多语言模型向语言长尾迁移仍存在明显局限。具体指标需查阅正文。

## 🎯 结论与影响

最强结论是：30K 小时、675 种低资源语言的 ELARSpeech 能显著扩展 ASR/TTS 的语言覆盖，并作为长尾多语言语音的测试平台。该资源有望推动低资源语音建模、伪标签半监督与跨语言迁移研究，对工业界拓展多语言语音产品覆盖长尾语种具有直接价值。

## ⚠️ 局限与未解决问题

摘要未报告具体 WER/MOS、推理延迟与模型规模，缺少与强多语言基线的定量对比；语料源自单一档案库，录音条件与领域分布可能存在偏置；伪标签收益幅度与失败案例分析不足，需正文补充消融与误差分析。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-10-15/">← 返回 2026-10-15 速递</a></div>
