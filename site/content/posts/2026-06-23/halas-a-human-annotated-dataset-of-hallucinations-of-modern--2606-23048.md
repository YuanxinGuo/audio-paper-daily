---
title: "HALAS: A Human-Annotated Dataset of Hallucinations of Modern ASR Systems"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "首个针对自然语音中ASR幻觉的人工标注数据集HALAS，揭示跨模型词汇重叠及低WER下幻觉现象，并建立非人工基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#幻觉检测</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#ASR鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.23048</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.23048" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.23048" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个针对自然语音中ASR幻觉的人工标注数据集HALAS，揭示跨模型词汇重叠及低WER下幻觉现象，并建立非人工基准。
</div>

## 👥 作者与机构

**Mateusz Barański** ¹ · Jan Jasiński · Julitta Bartolewska · Marcin Witkowski · Konrad Kowalczyk

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR鲁棒性、幻觉检测研究者。建议通读，重点看§3数据集构建与§4分析结果，以及§5基准实验。可复现其检测方法。

## 🌍 研究背景

端到端ASR系统在自然语音中会产生幻觉（hallucination），但现有缓解方法多在非语音或人工破坏音频上评估，缺乏真实场景基准。本文构建首个自然发生幻觉的人工标注数据集HALAS，覆盖7个SOTA ASR模型在真实财报电话会议录音上的输出，提供span级标签，分析幻觉模式与严重程度，并建立检测基准。

## 💡 核心创新

1. 首个自然语音ASR幻觉人工标注数据集HALAS
2. 跨7个SOTA模型的幻觉模式分析，发现词汇重叠
3. 揭示低WER下幻觉仍存在
4. 建立非人工幻觉检测基准，SOTA方法F1仅53.1%

## 🏗️ 模型架构

无模型架构。HALAS数据集构建流程：选取7个SOTA ASR模型（如Whisper、Conformer等）在真实财报电话会议录音上解码，人工标注幻觉span（插入、替换、删除导致的语义错误），提供span级标签及严重程度评分。

## 📚 数据集

- HALAS（训练/评估，来自真实财报电话会议录音，7个ASR模型输出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ROC-AUC | HALAS | 字符/语义指标 81% | **SOTA检测方法 53.1% F1** | F1较低，表明检测困难 |

字符级和语义级指标作为幻觉检测代理达到81% ROC-AUC，但SOTA检测方法F1仅53.1%，表明自然幻觉检测极具挑战。跨模型词汇重叠分析显示不同ASR模型在相似位置产生幻觉，且低WER片段中幻觉仍存在。

## 🎯 结论与影响

HALAS是首个自然语音ASR幻觉基准，揭示现有检测方法在真实场景下性能不足，为幻觉缓解研究提供关键资源。后续可推动更鲁棒的检测与缓解方法，对工业ASR部署有重要价值。

## ⚠️ 局限与未解决问题

数据集仅基于财报电话会议录音，领域单一；未覆盖所有ASR架构；未提供缓解方法；检测基准仅评估现有方法，未提出新检测器。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
