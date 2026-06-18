---
title: "FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#句子嵌入分析"]
summary: "提出因子化线性投影（FLiP）模型，从句子嵌入中恢复词汇内容，揭示多模态多语言编码器的模态和语言偏差。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#句子嵌入分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#句子嵌入</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.18109</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/BUTSpeechFIT/FLiP" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">BUTSpeechFIT/FLiP</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.18109" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.18109" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/BUTSpeechFIT/FLiP" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出因子化线性投影（FLiP）模型，从句子嵌入中恢复词汇内容，揭示多模态多语言编码器的模态和语言偏差。
</div>

## 👥 作者与机构

**Santosh Kesiraju** ¹ · Bolaji Yusuf · \v{S}imon Sedl\'a\v{c}ek · Old\v{r}ich Plchot · Petr Schwarz

**机构**：布尔诺理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对句子嵌入可解释性、多模态/多语言表示分析感兴趣的读者。建议重点阅读第3节（FLiP模型）和第4节（实验结果），特别是表1和表2。可跳过第2节背景。

## 🌍 研究背景

预训练句子嵌入（如LaBSE、SONAR）广泛应用于跨语言和跨模态任务，但其内部表示缺乏可解释性。现有方法如线性探针或黑盒分析难以揭示嵌入中编码的词汇信息。本文旨在通过可解释的因子化线性投影，量化嵌入中的词汇内容，并分析模态和语言偏差。

## 💡 核心创新

1. 提出因子化线性投影（FLiP）模型用于嵌入分析
2. FLiP可恢复超过75%的词汇内容，显著优于非因子化基线
3. 揭示多模态编码器（SONAR）的模态偏差和语言偏差
4. 提供无需下游任务的编码器内在洞察方法

## 🏗️ 模型架构

FLiP模型：输入为预训练句子嵌入（如LaBSE、SONAR、Gemini），通过因子化线性投影（低秩矩阵分解）将嵌入映射到词汇空间（词袋表示）。训练目标为最小化预测词袋与真实词袋之间的损失。输出为词汇概率分布，用于恢复词汇内容。

## 📚 数据集

- Tatoeba（多语言句子对，用于训练和评估）
- FLoRes（多语言平行语料，用于评估）
- Europarl（多语言语料，用于训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 词汇召回率（Lexical Recall） | Tatoeba（多语言） | 非因子化线性探针（约60%） | **FLiP（>75%）** | +15%以上 |

FLiP在多个高资源和中等资源语言上均取得超过75%的词汇召回率，显著优于非因子化基线。实验还揭示了SONAR编码器存在模态偏差（文本嵌入优于语音嵌入）和语言偏差（高资源语言优于低资源语言）。

## 🎯 结论与影响

FLiP是一种有效的句子嵌入诊断工具，能定量揭示嵌入中的词汇信息及偏差。该方法为理解多模态多语言编码器提供了新视角，有助于改进嵌入质量和公平性。对工业应用中的模型选择与调试具有参考价值。

## ⚠️ 局限与未解决问题

FLiP仅恢复词汇内容，无法捕捉句法或语义信息；实验限于少数语言和模态；未评估对下游任务性能的影响；因子化线性投影假设可能过于简化嵌入结构。

## 🔗 开源资源

- **代码**：<https://github.com/BUTSpeechFIT/FLiP>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
