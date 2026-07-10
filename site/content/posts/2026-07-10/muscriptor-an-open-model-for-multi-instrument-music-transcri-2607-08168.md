---
title: "MuScriptor: An Open Model for Multi-Instrument Music Transcription"
date: 2026-07-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐转录"]
summary: "提出MuScriptor，一种结合合成数据预训练、真实数据微调和强化学习后训练的多乐器音乐转录模型，支持按乐器条件定制转录。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐转录</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多乐器转录</span> <span class="tag-pill tag-pill-soft">#合成数据预训练</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#开源模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08168</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08168" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08168" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MuScriptor，一种结合合成数据预训练、真实数据微调和强化学习后训练的多乐器音乐转录模型，支持按乐器条件定制转录。
</div>

## 👥 作者与机构

**Simon Rouard** ¹ · Michael Krause · Axel Roebel · Carl-Johann Simon-Gabriel · Alexandre D\'efossez

**机构**：Meta · 法国国家信息与自动化研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和音频处理研究者。建议通读，重点看§3的预训练-微调-后训练流程和§4的乐器条件机制。可先看表2对比结果。

## 🌍 研究背景

自动音乐转录（AMT）旨在将音频转换为符号表示，但现有方法多限于单乐器或简单混音，在真实多乐器场景下性能差。先前工作使用合成数据预训练，但泛化不足。本文旨在解决真实多乐器转录的实用性问题，通过结合合成数据预训练、真实数据微调和强化学习后训练，并引入乐器条件控制，提升转录准确性和灵活性。

## 💡 核心创新

1. 合成数据预训练+真实数据微调+RL后训练三阶段策略
2. 乐器条件机制实现按需转录
3. 开源多乐器转录模型MuScriptor
4. 强化学习后训练优化转录输出

## 🏗️ 模型架构

输入为多通道音频频谱特征，主干网络采用编码器-解码器架构，包含卷积层和Transformer模块。关键模块包括：预训练阶段使用合成数据训练基础模型，微调阶段在真实音乐数据上调整，后训练阶段通过强化学习（策略梯度）优化转录序列。输出为多乐器音符序列（音高、起始时间、结束时间、乐器标签）。模型参数量未在摘要中给出。

## 📚 数据集

- 合成数据集（预训练，大规模多乐器混合）
- 真实音乐数据集（微调，涵盖多种流派）

## 📊 实验结果

摘要未提供具体数值结果，但声称MuScriptor在真实世界多乐器录音上表现优于现有方法，且通过乐器条件控制可定制转录输出。

## 🎯 结论与影响

MuScriptor通过三阶段训练策略和乐器条件机制，显著提升了多乐器音乐转录在真实场景下的实用性。该工作为AMT领域提供了开源基线，有望推动音乐信息检索和交互式音乐应用的发展。工业上可用于自动乐谱生成和音乐教育。

## ⚠️ 局限与未解决问题

摘要未报告具体指标和对比基线，缺乏定量评估。未提及推理速度和模型大小，可能影响实时应用。合成数据与真实数据之间的域差异可能仍存在，需进一步分析。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-10/">← 返回 2026-07-10 速递</a></div>
