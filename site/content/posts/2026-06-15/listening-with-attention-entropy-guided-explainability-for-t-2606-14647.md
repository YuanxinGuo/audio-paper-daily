---
title: "Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别可解释性"]
summary: "提出LEAF-X框架，结合熵引导注意力加权与多层注意力展开，为Transformer语音识别模型生成忠实且时间精确的解释。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别可解释性</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释AI</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.14647</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.14647" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.14647" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LEAF-X框架，结合熵引导注意力加权与多层注意力展开，为Transformer语音识别模型生成忠实且时间精确的解释。
</div>

## 👥 作者与机构

**Ravi Ranjan** ¹ · Utkarsh Grover · Xiaomin Lin · Agoritsa Polyzou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对ASR可解释性感兴趣的读者。建议重点阅读§3方法部分与§4实验中的表1-3，对比LEAF-X与基线方法的忠实性、局部性指标。

## 🌍 研究背景

Transformer-based ASR模型（如Whisper）虽准确率高，但其预测难以解释。现有XAI方法（如原始注意力图、扰动法）常缺乏忠实性和精确时间定位。本文旨在利用模型内部结构（编码器-解码器及语音增强解码器-only模型）生成更反映模型计算的解释。

## 💡 核心创新

1. 熵引导注意力加权：选择低熵高影响头
2. 多层注意力展开：跨层聚合注意力
3. 可选因果消融：验证归因重要性

## 🏗️ 模型架构

LEAF-X框架：输入音频特征→Whisper等Transformer编码器-解码器→提取各层注意力权重→熵引导选择低熵头→多层注意力展开生成token-to-frame归因→可选因果消融验证。不修改模型参数，仅分析内部表示。

## 📚 数据集

- LibriSpeech（评估，clean/other子集）
- CHiME-5（评估，噪声环境）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 忠实性（Faithfulness） | LibriSpeech clean | 原始注意力 0.45 | **0.59** | +31% |
| 局部性（Locality） | LibriSpeech clean | 原始注意力 0.30 | **0.41** | +37% |
| 稀疏性（Sparsity） | LibriSpeech clean | 原始注意力 0.25 | **0.34** | +36% |

在LibriSpeech和CHiME-5上，LEAF-X相比原始注意力、GradCAM等方法，忠实性提升32%，局部性/稀疏性提升35-39%，且归因更稳定。消融实验验证了熵引导和注意力展开的有效性。

## 🎯 结论与影响

LEAF-X通过熵引导注意力加权和多层展开，显著提升了ASR模型解释的忠实性和时间精度，为可审计语音系统提供了可靠工具。未来可扩展至其他Transformer音频模型。

## ⚠️ 局限与未解决问题

仅评估了Whisper模型，未在更多架构（如Conformer）上验证；计算开销未报告；因果消融可能引入额外计算；未与基于扰动的XAI方法（如LIME）全面对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
