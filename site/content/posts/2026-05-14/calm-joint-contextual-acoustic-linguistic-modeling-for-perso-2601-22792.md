---
title: "CALM: Joint Contextual Acoustic-Linguistic Modeling for Personalization of Multi-Speaker ASR"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#上下文偏置", "#个性化", "#多说话人ASR", "#目标说话人提取", "#语音识别"]
summary: "提出CALM框架，联合声学-语言建模，通过说话人嵌入提取目标说话人并动态词汇偏置，在多说话人ASR中显著降低偏置词错误率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#上下文偏置</span> <span class="tag-pill tag-pill-soft">#个性化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.22792</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.22792" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.22792" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CALM框架，联合声学-语言建模，通过说话人嵌入提取目标说话人并动态词汇偏置，在多说话人ASR中显著降低偏置词错误率。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yosuke Fukumoto · Chikara Maeda · Chyi-Jiunn Lin · Shinji Watanabe

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多说话人ASR、个性化语音识别的研究者。建议重点阅读§3模型架构和§4实验部分，尤其是表1-3的结果。可先看§3.2目标说话人提取和§3.3上下文偏置模块。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 多说话人重叠对话场景下的个性化语音识别 |
| **核心创新** | 联合声学-语言建模框架整合目标说话人提取与上下文偏置 · 基于说话人嵌入的动态目标说话人提取 · 基于动态词汇表的上下文偏置机制 |
| **模型架构** | 输入混合语音 → 说话人嵌入驱动的目标说话人提取模块 → 基于Conformer的声学编码器 → 动态词汇上下文偏置模块 → 解码器输出。参数量未在摘要中给出。 |
| **数据集** | LibriSpeechMix（模拟英语混合，训练与评估） · CSJMix（日语混合，训练与评估） · AMI IHM-mix（标准化混合，评估） |
| **关键结果** | 在LibriSpeech2Mix上，偏置词错误率(B-WER)从12.7降至4.7；在CSJMix2 (eval3)上，偏置字符错误率(B-CER)从16.6降至8.4。AMI IHM-mix结果未给出具体数值。 |

## 🎯 与本站重点领域的关联

与语音增强、目标说话人提取、语音分离领域相关。CALM中的目标说话人提取模块可视为个性化语音增强的一种形式，其联合声学-语言建模思路可迁移至语音分离中的说话人条件化。

## ⚠️ 局限与未解决问题

仅报告了模拟混合数据集结果，未在真实远场或噪声环境下评估；未提供模型参数量和推理延迟；缺乏对上下文偏置词汇表大小影响的消融实验。

## 📋 引用

```bibtex
@article{shakeel20262601,
  title  = {CALM: Joint Contextual Acoustic-Linguistic Modeling for Personalization of Multi-Speaker ASR},
  author = {Muhammad Shakeel and  Yosuke Fukumoto and  Chikara Maeda and  Chyi-Jiunn Lin and  Shinji Watanabe},
  journal = {arXiv preprint arXiv:2601.22792},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
