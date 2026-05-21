---
title: "Music of Changing Lines: Toward a Culturally Situated Approach to the I-Ching"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出一个交互系统，将易经占卜与LLM和生成音乐模型结合，实现文化意义驱动的音乐生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#交互系统</span> <span class="tag-pill tag-pill-soft">#生成式AI</span> <span class="tag-pill tag-pill-soft">#易经</span> <span class="tag-pill tag-pill-soft">#计算机音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.20386</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.20386" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.20386" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一个交互系统，将易经占卜与LLM和生成音乐模型结合，实现文化意义驱动的音乐生成。
</div>

## 👥 作者与机构

**Ling Qi** ¹ · Aleksandra Teng Ma · Alexandria Smith

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对计算机音乐、人机交互或文化计算感兴趣的读者。可重点阅读系统设计部分（§3）和讨论部分（§5），了解如何将文化框架融入AI流程。若对技术细节或评估感兴趣，本文可能不够深入。

## 🌍 研究背景

易经作为中国哲学经典，在西方实验音乐中被用作随机操作工具（如John Cage），但常剥离其文化意义。现有计算机音乐系统多聚焦技术生成，缺乏对文化仪式和解释过程的整合。本文旨在设计一个交互系统，让AI作为解释中介而非创作权威，重新赋予易经以意义承载功能。

## 💡 核心创新

1. 将易经占卜过程（文王法）实时映射为概率音乐过程
2. 使用LLM（Gemini）对卦象进行上下文解释
3. 将解释文本转化为生成音乐模型（Lyria）的提示
4. 强调参与和仪式感，而非预设音乐结构

## 🏗️ 模型架构

用户通过文王法投掷硬币生成卦象和变爻，系统实时以概率音乐过程伴奏。卦象和变爻输入LLM（Gemini），结合用户问题生成文本解释。该解释作为提示输入生成音乐模型Lyria，输出音乐片段。系统不预设音乐结构，完全由占卜过程和解释驱动。

## 📊 实验结果

摘要未提供定量实验结果或用户研究数据，仅描述系统设计和概念框架。缺乏对生成音乐质量、用户参与度或文化准确性的评估。

## 🎯 结论与影响

本文提出一个将易经文化框架与生成AI结合的交互音乐系统，强调意义驱动而非随机操作。对计算机音乐中文化敏感设计有启发意义，但缺乏实证评估，影响说服力。工业落地可能性较低，更多是艺术探索。

## ⚠️ 局限与未解决问题

未提供任何定量或定性评估，缺乏用户研究或专家评审。系统依赖外部LLM和音乐模型，未讨论延迟或可靠性。文化解释的准确性未验证，可能简化易经哲学。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
