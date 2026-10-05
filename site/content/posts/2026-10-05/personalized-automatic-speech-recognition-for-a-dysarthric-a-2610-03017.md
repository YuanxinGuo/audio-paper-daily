---
title: "Personalized Automatic Speech Recognition for a Dysarthric and Tracheostomic Speaker using Artificial Conversations"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "为一名气管造口伴严重构音障碍的捷克语者构建个性化Whisper ASR，发布33小时人工对话数据集，CER相对降低50%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#个性化ASR</span> <span class="tag-pill tag-pill-soft">#病理语音</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.03017</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.03017" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.03017" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>为一名气管造口伴严重构音障碍的捷克语者构建个性化Whisper ASR，发布33小时人工对话数据集，CER相对降低50%。
</div>

## 👥 作者与机构

**David Nadrchal** ¹ · Monorama Swain · Florian Schmid · Gerhard Widmer · Paul Primus

**机构**：约翰内斯·开普勒大学林茨分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合病理语音、个性化ASR与低资源适配方向的研究者与工程团队阅读。建议重点看 §3 的多阶段训练流程与 §4 的三类近实时场景评测，以及数据集构建协议部分；若关注数据采集可先看 artificial conversation 协议设计。

## 🌍 研究背景

构音障碍与气管造口语音对标准ASR极不友好，此前多依赖说话人大量标注或专用声学模型，通用 Whisper 等大模型在该类语音上 CER 极高。痛点在于：病理语音数据稀缺、采集成本高、说话人差异大，且现有方案少有面向真实交互场景的评测。本文针对单一重度障碍说话人，试图用有限数据与声学模拟实现可用的个性化 ASR。

## 💡 核心创新

1. 提出 artificial conversation 协议采集33小时高参与度对话语音
2. 多阶段训练：标准捷克语→模拟气管造口语音→说话人数据
3. 基于 Whisper Base 的个性化微调流程
4. 在脚本、问答、自发对话三类近实时场景系统评测

## 🏗️ 模型架构

以 Whisper Base 为骨干，输入为说话人语音的 log-Mel 特征，经编码器-解码器 Transformer 输出字符序列。训练分三阶段：先在标准捷克语语音上微调，再在声学模拟的气管造口语音上适配，最后在说话人真实数据上个性化微调。摘要未给出参数量与具体模块改动，推测沿用 Whisper 原始结构，仅通过数据与训练策略实现个性化。

## 📚 数据集

- 自建捷克语气管造口说话人数据集（33小时，训练/评估）
- 标准捷克语语音数据（训练，规模未说明）
- 声学模拟气管造口语音（训练，规模未说明）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | 三类近实时场景（脚本/问答/自发对话） | Whisper Base | **相对降低50%** | -50% 相对 |

摘要报告相对 Whisper Base 的 CER 降低约50%，并在孤立话语识别上超过该说话人日常助理的平均识别准确率。定量结果与说话人反馈共同支持系统可用性。摘要未给出绝对 CER、各场景分项数值、消融实验与推理延迟，跨说话人泛化也未验证。

## 🎯 结论与影响

最强结论是：即便对严重障碍语音，通过多阶段微调与专用对话数据也能获得有帮助的 ASR。该工作为病理语音个性化适配提供了可复用的数据采集与训练范式，对辅助沟通类工业落地有直接参考价值，但单说话人设定限制了推广性。

## ⚠️ 局限与未解决问题

仅针对单一说话人，无法验证跨说话人泛化；缺少绝对 CER、分场景数值与消融实验；声学模拟气管造口语音的有效性未量化；未报告推理延迟与模型效率；对比基线仅 Whisper Base，未与病理语音专用方法比较。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-05/">← 返回 2026-10-05 速递</a></div>
