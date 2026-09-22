---
title: "COT-TTS: Audio Context-Aware Text-to-Speech with Chain-of-Thought Reasoning"
date: 2026-09-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出上下文感知推理式TTS任务，用历史对话音频推断说话风格，构建900万样本双语数据集与800条基准，开源0.6B/1.7B自回归模型。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#上下文感知</span> <span class="tag-pill tag-pill-soft">#链式推理</span> <span class="tag-pill tag-pill-soft">#情感语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.22697</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://luckybian.github.io/COT-TTS" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">luckybian.github.io/COT-TTS</span></span></a><a class="oc-chip oc-chip-demo" href="https://luckybian.github.io/COT-TTS" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">luckybian.github.io/COT-TTS</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.22697" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.22697" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://luckybian.github.io/COT-TTS" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://luckybian.github.io/COT-TTS" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出上下文感知推理式TTS任务，用历史对话音频推断说话风格，构建900万样本双语数据集与800条基准，开源0.6B/1.7B自回归模型。
</div>

## 👥 作者与机构

**Weizhen Bian** ¹ · Sitong Cheng · Rongxiu Zhong · Jiahao Pan · Liumeng Xue · Boyi Kang · Shilei Zhang · Jinglei Liu · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做表现力TTS、对话语音合成与LLM推理式生成的研究者。建议通读，重点看 §3 任务定义与推理中间表示设计、§4 数据构建管线与 source-disjoint 划分、表 2 与大规模基线对比。可先跑 demo 页听情感/重音一致性样例，再决定是否复现数据管线。

## 🌍 研究背景

当前 TTS 在表现力与可控性上进展明显，但说话风格通常依赖用户显式指令（如情感标签、风格描述）。自然对话中，风格应由前文语境自然推断，而非人工指定。已有上下文 TTS 工作多停留在拼接文本历史或简单情感分类，缺少显式推理与大规模对话语音监督，且缺乏 source-disjoint 评测基准，导致模型易过拟合说话人/录音条件。本文要解决的是：给定历史对话音频、目标文本与参考音色，如何推断并合成符合语境的语音。

## 💡 核心创新

1. 定义上下文感知推理式TTS任务，需从历史对话音频推断显式中间推理
2. 构建900万样本双语对话语音数据集，含100万高质量子集
3. 构建800条人工校验的 source-disjoint 基准与强基线
4. 0.6B/1.7B 自回归模型联合生成情感标注转写、可编辑风格推理与语音 token

## 🏗️ 模型架构

输入为历史对话音频、目标文本与参考语音。系统先经语音编码器提取历史音频表征，与文本拼接送入自回归主干（0.6B / 1.7B 参数），以链式推理方式依次生成情感标注转写、可编辑的语音风格推理文本，再生成离散语音 token，最后由声码器还原波形并保持参考音色。推理中间结果可人工编辑，实现风格可控。摘要未给出具体主干网络名（如 Conformer / Transformer）与声码器细节。

## 📚 数据集

- 自建双语对话语音数据集（训练，900万样本，含100万高质量子集）
- 自建 source-disjoint 基准（评估，800条人工校验样本）

## 📊 实验结果

摘要仅给出定性结论：所提模型以显著更少参数达到与大规模基线系统相当的性能，并在时长一致性与情感一致性上表现良好，能依据对话上下文生成合适的情感、重音与节奏变化。未提供 SI-SDR / PESQ / MOS / WER 等具体数值，也未给出消融与效率指标，需查阅正文确认。

## 🎯 结论与影响

最强结论是：显式链式推理可让 TTS 从对话历史中推断说话风格，且小参数模型可媲美大规模基线。这为表现力 TTS 提供了“推理式风格建模”的新范式，并可能推动对话助手、有声书与虚拟人的语境自适应语音合成落地。

## ⚠️ 局限与未解决问题

摘要未给任何量化指标与消融，难以判断推理模块的实际增益；数据集为自建，来源与说话人分布未说明，存在 bias 风险；未报推理延迟与实时率；与现有上下文 TTS / 情感 TTS 的对比基线细节不足；source-disjoint 基准仅800条，统计功效有限。

## 🔗 开源资源

- **项目主页**：<https://luckybian.github.io/COT-TTS>
- **Demo / 试听**：<https://luckybian.github.io/COT-TTS>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-22/">← 返回 2026-09-22 速递</a></div>
