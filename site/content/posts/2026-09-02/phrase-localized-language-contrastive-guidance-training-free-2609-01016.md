---
title: "Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出无训练推理框架LCG，通过短语级语言对比引导和自注意力探测，恢复代码切换语音中外语短语的母语口音，无需微调或外部对齐。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#代码切换语音合成</span> <span class="tag-pill tag-pill-soft">#无训练推理</span> <span class="tag-pill tag-pill-soft">#语言对比引导</span> <span class="tag-pill tag-pill-soft">#自注意力探测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.01016</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.01016" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.01016" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无训练推理框架LCG，通过短语级语言对比引导和自注意力探测，恢复代码切换语音中外语短语的母语口音，无需微调或外部对齐。
</div>

## 👥 作者与机构

**Che Hyun Lee** ¹ · Sangkwon Park · Donghun Kang · Dongwook Lee · Youngho Cho · Heeseung Kim · Sungroh Yoon

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、多语言TTS研究者阅读。值得通读，重点看第3节方法（LCG框架）和第4节实验（口音自然度评估）。可先看§3.2自注意力探测和§3.3语言对比引导，再结合表2结果。

## 🌍 研究背景

当前语音合成在处理代码切换时，常将外语短语用主语言口音读出，缺乏母语自然度。现有方法多依赖训练数据或外部对齐，难以泛化。本文提出无训练推理框架LCG，通过短语级语言对比引导和自注意力探测，无需微调或辅助模型，即可提升代码切换短语的口音自然度，同时保持说话人身份和整体自然度。

## 💡 核心创新

1. 提出短语级语言对比引导（LCG），分区引导各语言口音
2. 自注意力探测技术，无需外部对齐即可定位短语边界
3. 无训练推理框架，无需微调或辅助模型
4. 跨语言对鲁棒提升口音自然度，抑制口音泄漏
5. 保持说话人身份和自然度，不牺牲合成质量

## 🏗️ 模型架构

输入文本序列，通过预训练TTS模型（如VITS）生成语音。LCG框架在推理时介入：首先利用自注意力探测模块分析文本编码器的注意力图，定位代码切换短语的边界；然后对每个区域应用对应的语言对比引导，通过对比损失调整生成过程，使每个区域的口音符合其语言。无需修改模型参数，仅调整推理时的引导信号。

## 📊 实验结果

摘要未提供具体数值，但声称在多种语言对上，LCG显著提升代码切换短语的母语自然度，同时抑制口音泄漏，并保持说话人身份和整体自然度。实验可能包括主观MOS评估和客观口音相似度指标，但具体数据未给出。

## 🎯 结论与影响

LCG框架有效解决代码切换TTS中的口音问题，无需训练即可提升短语母语自然度，为多语言语音合成提供新思路。未来可扩展至更多语言对和实时应用，对工业界多语言语音助手有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：依赖预训练TTS的注意力质量，对注意力不准的模型可能失效；未报告推理延迟，可能影响实时性；评估语言对有限，泛化性待验证；未与有监督方法对比，优势需进一步量化。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
