---
title: "CALM: Joint Contextual Acoustic-Linguistic Modeling for Personalization of Multi-Speaker ASR"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#上下文偏置", "#多说话人ASR", "#目标说话人提取", "#端到端", "#语音识别"]
summary: "提出CALM框架，联合声学-语言建模实现多说话人ASR的个性化，通过说话人嵌入提取和动态词汇偏置显著降低偏置词错误率。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#上下文偏置</span> <span class="tag-pill tag-pill-soft">#端到端</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.22792</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.22792" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.22792" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CALM框架，联合声学-语言建模实现多说话人ASR的个性化，通过说话人嵌入提取和动态词汇偏置显著降低偏置词错误率。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yosuke Fukumoto · Chikara Maeda · Chyi-Jiunn Lin · Shinji Watanabe

**机构**：CMU

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多说话人ASR、个性化语音接口的研究者。建议重点阅读§3（方法）和§4（实验），尤其是表1和表2的对比结果。可先看§3.2的目标说话人提取和§3.3的上下文偏置模块。

## 🌍 研究背景

多说话人ASR在重叠对话场景中面临挑战，现有方法通常分别处理目标说话人提取和上下文偏置，未能充分利用声学和语言线索的联合信息。之前SOTA如端到端多说话人ASR模型（如Serialized Output Training）或独立偏置模块，但缺乏统一框架。本文旨在通过联合建模声学和语言上下文，提升个性化ASR在重叠语音中的性能。

## 💡 核心创新

1. 说话人嵌入驱动的目标说话人提取
2. 动态词汇库上下文偏置机制
3. 端到端联合声学-语言建模框架
4. 跨语言验证（英语和日语）

## 🏗️ 模型架构

输入为多说话人混合语音，首先通过说话人嵌入提取目标说话人特征，然后送入Conformer编码器进行声学建模。同时，动态词汇库根据上下文生成偏置向量，与声学特征融合。解码器采用Transformer，输出目标说话人的转录。整体为端到端训练，参数量未提及。

## 📚 数据集

- LibriSpeechMix（模拟英语混合，训练/评估）
- CSJMix（日语混合，训练/评估）
- AMI IHM-mix（标准会议混合，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| B-WER | LibriSpeech2Mix | 12.7 | **4.7** | -8.0 |
| B-CER | CSJMix2 (eval3) | 16.6 | **8.4** | -8.2 |

在LibriSpeech2Mix上，CALM将偏置词错误率（B-WER）从12.7降至4.7，相对降低63%；在CSJMix2上，偏置字符错误率（B-CER）从16.6降至8.4，相对降低49%。AMI IHM-mix上的结果进一步验证了在标准混合语音上的有效性。消融实验表明联合建模优于单独模块。

## 🎯 结论与影响

CALM通过联合声学-语言建模显著提升多说话人ASR的个性化性能，在英语和日语上均取得大幅改进。该框架为后续研究提供了统一范式，有望推动智能助手等工业应用中的重叠语音处理。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟和模型参数量；仅评估模拟混合数据，真实场景泛化性未知；未与近期端到端多说话人ASR模型（如WavLM+Serialized Output Training）对比；缺乏对说话人数量扩展性的分析。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
