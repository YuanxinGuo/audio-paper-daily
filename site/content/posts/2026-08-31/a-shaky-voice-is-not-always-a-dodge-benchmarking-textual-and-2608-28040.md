---
title: "A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "提出DualEvasion基准，用于财报电话会议中文本和语音双模态的规避检测，发现现有模型在语音信心检测上表现不佳。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#语音特征</span> <span class="tag-pill tag-pill-soft">#基准数据集</span> <span class="tag-pill tag-pill-soft">#财报电话会议</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.28040</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.28040" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.28040" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DualEvasion基准，用于财报电话会议中文本和语音双模态的规避检测，发现现有模型在语音信心检测上表现不佳。
</div>

## 👥 作者与机构

**Mirae Kim** ¹ · Seonghun Jeong · Youngjun Kwak

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音情感识别、多模态分析研究者阅读。可重点看第3节数据集构建和第4节实验分析，了解标注方案和模型局限。若关注多模态融合，可细读第5节讨论。

## 🌍 研究背景

现有规避检测主要基于文本转录，忽略了语音中的声学线索。本文认为规避是多维的，包括内容（文本）和表达方式（语音）。为此构建了包含文本和语音标注的基准，并评估了多模态模型在语音信心检测上的表现，发现模型难以捕捉说话人相对基线的声学变化。

## 💡 核心创新

1. 构建DualEvasion基准，包含505个问答对的双模态标注
2. 提出文本规避和语音信心双标签标注方案
3. 揭示多模态模型在语音信心检测上的不足
4. 分析模型对声学线索的绝对而非相对理解
5. 验证说话人级参考可提升性能但仍有差距

## 🏗️ 模型架构

输入为财报电话会议中的问答对，包含文本转录和音频。文本特征通过预训练语言模型提取，音频特征通过预训练声学模型提取。多模态融合采用特征拼接或交叉注意力。模型输出两个二分类标签：文本规避（直接/规避）和语音信心（自信/不自信）。

## 📚 数据集

- DualEvasion（训练/评估，505个问答对，60场电话会议）

## 📊 实验结果

摘要未提供具体指标数值，但指出多模态模型在语音信心检测上表现不佳，尤其对不自信响应。提供说话人级参考可带来适度提升，但与人类表现仍有显著差距。

## 🎯 结论与影响

本文强调语音线索在规避检测中的重要性，并提供了首个双模态基准。未来工作可探索更有效的声学特征融合和说话人归一化方法。对工业界，该基准可用于改进财报电话会议的风险评估工具。

## ⚠️ 局限与未解决问题

基准规模较小（505对），可能限制泛化性。未提供模型性能的具体数值，对比不充分。未讨论音频特征提取的细节和计算成本。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
