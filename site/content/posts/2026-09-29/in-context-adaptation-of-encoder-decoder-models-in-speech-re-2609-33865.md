---
title: "In-Context Adaptation of Encoder-Decoder Models in Speech Recognition"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "系统研究六种编码器-解码器 ASR 模型能否通过推理时拼接语音-文本示例实现上下文自适应，发现该能力普遍存在。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#上下文学习</span> <span class="tag-pill tag-pill-soft">#说话人自适应</span> <span class="tag-pill tag-pill-soft">#编码器-解码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.33865</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.33865" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.33865" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究六种编码器-解码器 ASR 模型能否通过推理时拼接语音-文本示例实现上下文自适应，发现该能力普遍存在。
</div>

## 👥 作者与机构

**Yen Meng** ¹ · Sharon Goldwater · Hao Tang

**机构**：爱丁堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 ASR 自适应、上下文学习、LLM-based 语音模型的研究者阅读。建议通读，重点看 §3 的 collated vs interleaved 演示设计、§4 的 oracle 与 first-pass 实验，以及 §5 关于词汇与说话人信息贡献的受控实验。若只关心结论，看表 2 与表 4 即可。

## 🌍 研究背景

ASR 模型面对新说话人、口音和领域时通常需要微调，成本高且易遗忘。近期工作表明 LLM-based 语音模型可通过交错语音-文本示例在推理时做上下文自适应，但尚不清楚这是否为所有编码器-解码器模型的固有能力。本文要回答：传统 cross-attention 架构与 LLM-based 架构是否都能开箱即用地进行上下文自适应，以及演示形式与信息类型如何影响效果。

## 💡 核心创新

1. 系统对比六种编码器-解码器 ASR 模型的上下文自适应能力
2. 提出 collated 与 interleaved 两种演示形式并对比其效果
3. 通过受控实验分离词汇信息与说话人信息的贡献

## 🏗️ 模型架构

输入为拼接或交错的语音-文本演示序列，语音经编码器（如 Conformer 或 Whisper 风格编码器）提取声学表示，文本经解码器嵌入。主干涵盖传统 cross-attention 编码器-解码器与 LLM-based 架构。关键模块为演示拼接策略：collated 将示例集中置于目标语音前，interleaved 将语音-文本对交替排列。输出为转录文本。摘要未给出参数量。

## 📚 数据集

- 三个英语数据集（评估，具体名称摘要未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 相对 WER 改进（oracle） | 三个英语数据集 | 无演示基线 | **最高 30% 相对提升** | +30% |
| 相对 WER 改进（first-pass） | 三个英语数据集 | 无演示基线 | **最高 23% 相对提升** | +23% |

摘要报告 oracle 实验最高 30% 相对改进，使用 first-pass 假设时最高 23%。受控实验表明词汇与说话人信息均对自适应有贡献。interleaved 演示在部分场景有效，但 collated 演示在所有模型上表现一致。摘要未给出具体数据集名称、绝对 WER 值及消融细节。

## 🎯 结论与影响

本文最强结论是：ASR 的上下文自适应并非特定架构、训练方式或演示形式的专属能力，而是编码器-解码器模型的普遍特性。这为推理时自适应提供了更通用的依据，可能推动无需微调的个性化 ASR 落地，并启发后续研究探索演示选择与信息解耦。

## ⚠️ 局限与未解决问题

摘要未给出具体数据集名称与绝对 WER，无法判断提升的实际幅度；未报告推理延迟与演示长度对性能的影响；受控实验仅限英语，跨语言泛化未知；未与微调基线做效率对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
