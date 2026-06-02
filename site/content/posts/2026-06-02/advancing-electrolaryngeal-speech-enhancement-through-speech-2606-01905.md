---
title: "Advancing Electrolaryngeal Speech Enhancement Through Speech-Text Representation Learning"
date: 2026-06-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种融合语音和文本表征的seq2seq语音转换框架，用于将电子喉语音增强为自然语音，通过多级融合策略和重构损失提升映射质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音转换</span> <span class="tag-pill tag-pill-soft">#表征学习</span> <span class="tag-pill tag-pill-soft">#喉切除者语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.01905</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.01905" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.01905" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种融合语音和文本表征的seq2seq语音转换框架，用于将电子喉语音增强为自然语音，通过多级融合策略和重构损失提升映射质量。
</div>

## 👥 作者与机构

**Ding Ma** ¹ · Jinyi Mi · Fengji Li · Lester Phillip Violeta · Jiajun He · Wenchin Huang · Kazuhiro Kobayashi · Tomoki Toda

**机构**：名古屋大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、语音转换或辅助通信技术的研究者阅读。建议重点阅读第III节的方法部分（融合策略和重构训练），以及第IV节的实验结果（表I-III）。可先看§III-B和§III-C了解核心创新。

## 🌍 研究背景

喉切除者依赖电子喉设备产生电子喉语音，但该语音存在严重失真、音素变化有限、韵律不自然和时间偏移等问题，降低了自然度和可懂度。现有基于seq2seq语音转换的EL2SP方法因EL与正常语音之间的巨大差异导致累积映射误差，性能受限。本文旨在通过引入文本表征来改进表征学习，减少映射误差，提升EL语音增强效果。

## 💡 核心创新

1. 提出语音-文本联合表征学习框架，融合预训练模块
2. 设计三种融合策略：中间层、输入层和混合层融合
3. 引入重构损失优化表征迁移，不增加模型复杂度
4. 结合数据增强方法进一步提升性能

## 🏗️ 模型架构

输入EL语音特征和对应文本（通过ASR获取）→ 预训练语音编码器（如WavLM）和文本编码器（如BERT）分别提取表征 → 融合模块（中间/输入/混合融合）生成联合表征 → 自编码器风格的重构训练，解码器为seq2seq VC模型（如FastSpeech2或VITS）输出增强语音。模型参数量未明确给出。

## 📚 数据集

- EL2SP数据集1（训练/评估，规模未说明）
- EL2SP数据集2（训练/评估，规模未说明）

## 📊 实验结果

摘要未提供具体数值指标，但声称在多个EL2SP数据集上，所提方法结合数据增强一致优于仅依赖语音表征的基线，且随着融合策略深入（中间→输入→混合）性能逐步提升，验证了方法的有效性。

## 🎯 结论与影响

本文提出的语音-文本表征学习框架有效提升了电子喉语音增强的质量，通过多级融合和重构损失缓解了映射误差问题。该工作为辅助通信技术提供了可扩展的实用方法，未来可探索更高效的融合机制或扩展到其他失声语音场景。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟、模型复杂度或实时性；未报告在真实噪声环境下的泛化能力；数据集规模未说明，可能影响结论的普适性；缺乏与最新VC方法的对比（如HiFi-GAN、SVC等）。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-02/">← 返回 2026-06-02 速递</a></div>
