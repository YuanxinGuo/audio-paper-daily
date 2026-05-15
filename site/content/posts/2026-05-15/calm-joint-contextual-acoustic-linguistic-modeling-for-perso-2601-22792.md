---
title: "CALM: Joint Contextual Acoustic-Linguistic Modeling for Personalization of Multi-Speaker ASR"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#上下文偏置", "#多说话人ASR", "#目标说话人提取", "#端到端", "#语音识别"]
summary: "提出CALM框架，联合声学-语言建模实现多说话人ASR中的个性化，通过说话人嵌入提取和动态词汇偏置降低偏置词错误率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
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

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.22792" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.22792" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CALM框架，联合声学-语言建模实现多说话人ASR中的个性化，通过说话人嵌入提取和动态词汇偏置降低偏置词错误率。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yosuke Fukumoto · Chikara Maeda · Chyi-Jiunn Lin · Shinji Watanabe

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多说话人ASR、个性化语音识别的研究者。建议通读，重点看§3的模型架构和§4的实验结果，尤其是表1和表2的B-WER/B-CER对比。

## 🌍 研究背景

多说话人ASR在重叠对话场景中面临目标说话人提取和上下文偏置的挑战。现有方法通常分别处理声学线索（如说话人嵌入）和语言线索（如词汇偏置），缺乏联合建模。本文提出CALM框架，在端到端系统中集成目标说话人提取和动态词汇偏置，以利用声学和语言线索的互补性。

## 💡 核心创新

1. 说话人嵌入驱动的目标说话人提取
2. 动态词汇偏置与声学-语言联合建模
3. 端到端框架整合提取与偏置
4. 跨语言（英日）验证有效性

## 🏗️ 模型架构

输入为多说话人混合语音，首先通过说话人嵌入提取目标说话人特征，然后送入基于Conformer的编码器-解码器架构。编码器输出与动态词汇偏置网络（基于注意力机制）融合，实现上下文偏置。最终输出目标说话人的转录文本。模型参数量未在摘要中提及。

## 📚 数据集

- LibriSpeechMix（训练/评估，模拟英语两说话人混合）
- CSJMix（训练/评估，模拟日语两说话人混合）
- AMI corpus IHM-mix（评估，标准化会议语音混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| B-WER | LibriSpeech2Mix | 12.7 | **4.7** | -8.0 |
| B-CER | CSJMix2 (eval3) | 16.6 | **8.4** | -8.2 |

在LibriSpeech2Mix上，CALM将偏置词错误率（B-WER）从12.7降至4.7，相对降低63%；在CSJMix2上，偏置字符错误率（B-CER）从16.6降至8.4，相对降低49%。在AMI IHM-mix上进一步验证了在标准化会议语音混合中的有效性，表明模型具有良好的泛化能力。

## 🎯 结论与影响

CALM通过联合声学-语言建模显著提升了多说话人ASR的个性化性能，在英日两种语言上均取得大幅改进。该框架为后续研究提供了将目标说话人提取与上下文偏置结合的新范式，对智能助手等工业场景具有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟或计算效率；仅测试了两说话人混合场景，未扩展到更多说话人；未报告非偏置词的整体WER，可能偏置词性能提升以牺牲非偏置词为代价；消融实验未在摘要中呈现。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
