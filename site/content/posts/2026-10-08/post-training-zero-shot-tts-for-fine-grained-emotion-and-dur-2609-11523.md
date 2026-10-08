---
title: "Post-Training Zero-Shot TTS for Fine-Grained Emotion and Duration Control via Natural Language"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用后训练框架（SFT+GRPO）为预训练TTS模型加自然语言细粒度情感与时长控制，无需额外推理模块。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#情感控制</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#指令跟随</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.11523</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.11523" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.11523" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用后训练框架（SFT+GRPO）为预训练TTS模型加自然语言细粒度情感与时长控制，无需额外推理模块。
</div>

## 👥 作者与机构

**Lianru Gao** ¹ · Yujie Guo · Yong Qin

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控TTS、指令跟随语音生成的研究者与工程团队阅读。建议重点看§3的后训练流程与奖励设计（情感/时长/内容/说话人四项），以及实验中的细粒度控制准确率与消融。若只关心架构创新可略读，本文核心在训练范式而非网络结构。

## 🌍 研究背景

可控TTS此前多依赖话语级风格向量或参考音频，如基于GST、风格嵌入或扩散模型的条件注入，难以在同一句话内实现分段情感与语速的细粒度变化。有声书、对话代理与配音场景恰恰需要这种段级动态控制。已有工作或需额外推理期控制模块，或控制粒度粗、泛化差。本文要解决的是：如何在不改动预训练TTS架构的前提下，用自然语言指令实现段级情感与时长控制。

## 💡 核心创新

1. 提出统一后训练框架，SFT建立指令条件生成能力
2. 引入GRPO强化学习，用情感与时长奖励精调控制精度
3. 联合内容与说话人保持目标，避免控制损伤可懂度与音色
4. 复用预训练架构，推理期无需额外控制模块

## 🏗️ 模型架构

输入为文本指令（含情感与时长描述）与待合成文本，主干沿用预训练TTS模型（摘要未指明具体网络，推测为自回归或非自回归声学模型）。第一阶段监督微调使模型学会按指令生成语音；第二阶段用GRPO进行强化学习，奖励由情感匹配、时长偏差、内容一致性与说话人相似度四部分构成，通过组内相对比较更新策略。输出为可控的梅尔谱或波形，推理时直接以自然语言指令驱动，不引入额外控制网络。

## 📊 实验结果

摘要仅给出定性结论：细粒度可控性显著提升，同时保持语音可懂度与说话人身份。未提供具体指标数值、测试集名称或与基线的定量对比，也未报告消融实验、推理延迟或参数量，因此无法量化评估改进幅度。

## 🎯 结论与影响

最强结论是后训练范式可有效为已有TTS模型赋予自然语言细粒度控制能力，且不增加推理开销。这为可控语音合成提供了一条低成本扩展路径，后续研究可探索更多属性（如韵律、口音）的指令化后训练。工业上意味着可在已有TTS产品上通过后训练快速上线细粒度控制，无需重构推理管线。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果、数据集与基线对比，实验充分性存疑；奖励设计中情感与时长奖励的具体实现、权重与潜在冲突未说明；GRPO训练成本与稳定性未知；未报告推理延迟与参数量；缺乏与指令TTS基线（如PromptTTS、InstructTTS）的直接比较。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-08/">← 返回 2026-10-08 速递</a></div>
