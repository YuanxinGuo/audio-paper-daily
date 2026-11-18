---
title: "ASR-Protected Fusion and Reference-Anchored Policy Optimization for Joint ASR and Word-Level Speech Anti-Spoofing"
date: 2026-11-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音伪造检测"]
summary: "把部分伪造检测建模为带标签ASR，用子空间门控融合伪造线索并用参考锚定策略优化联合训练。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音伪造检测</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#音频大模型</span> <span class="tag-pill tag-pill-soft">#强化学习微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.34156</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.34156" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.34156" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>把部分伪造检测建模为带标签ASR，用子空间门控融合伪造线索并用参考锚定策略优化联合训练。
</div>

## 👥 作者与机构

**Xueping Zhang** ¹ · Xiaoxiao Miao · Tiantian Feng · Ming Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音伪造检测与ASR联合建模、音频LLM对齐的研究者阅读。建议通读，重点看§3的APSGF子空间门控设计与§4的RAPO优势估计推导，再核对表2/表3中五个数据集上WER与词级检测F1的权衡；若只关心检测指标可先看实验节。

## 🌍 研究背景

现有反欺骗系统多输出句级分数或时间段，前者无法定位被伪造的词，后者需与转写后对齐，对齐误差会污染词级标签；标准ASR只输出文本，识别后伪造信息丢失，下游系统可能在不知情下使用被篡改的词。本文把部分反欺骗重新表述为带标签ASR，让模型在转写同时标记伪造词，使标签与输出词直接对应，并解决音频LLM联合训练中识别与检测特征相互干扰的问题。

## 💡 核心创新

1. 将部分反欺骗建模为带标签ASR，伪造标签直接绑定输出词
2. ASR-Protected Subspace Gated Fusion，仅在受保护子空间外注入伪造线索
3. Reference-Anchored Policy Optimization，用参考模型奖励锚定优势
4. 低采样随机性单样本生成，缓解组内奖励同质化

## 🏗️ 模型架构

输入为语音波形经音频编码器得到的声学特征，主干为音频大语言模型（audio LLM）。在LLM内部引入ASR-Protected Subspace Gated Fusion：将ASR特征投影到受保护子空间，伪造线索经门控后仅在该子空间的正交补方向注入，避免扰动识别表征；输出端同时产生转写token与词级伪造标记。先以交叉熵做SFT，再用RAPO微调：对每个输入低随机性采样单条响应，以参考模型的奖励作为锚点计算优势，强化优于参考的响应、抑制劣于参考的响应。摘要未给出参数量。

## 📚 数据集

- 五个数据集（训练与评估，具体名称摘要未列明）

## 📊 实验结果

摘要仅声明在五个数据集上验证了方法在联合检测伪造词与保持ASR准确率方面的有效性，未给出WER、词级检测F1/精度等具体数值，也未报告与基线方法的定量对比和消融结果，因此无法量化提升幅度。

## 🎯 结论与影响

最强结论是把词级反欺骗与ASR输出直接绑定，并通过子空间隔离与参考锚定策略优化在联合训练中兼顾检测与识别。这为音频LLM上的细粒度伪造定位提供了可复用范式，对需要可信转写的下游系统（如语音助手、会议记录）有落地价值。

## ⚠️ 局限与未解决问题

摘要未给出任何定量指标与基线对比，难以判断相对句级/时间段方法的实际增益；五个数据集名称与规模未说明，存在领域偏置风险；RAPO依赖参考模型奖励，参考模型质量与额外推理开销未讨论；缺少消融验证APSGF各组件贡献。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-18/">← 返回 2026-11-18 速递</a></div>
