---
title: "AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出AuEmoChat框架，通过离散情感令牌空间和令牌合并算法，实现更真实的情感对话语音合成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对话语音合成</span> <span class="tag-pill tag-pill-soft">#情感建模</span> <span class="tag-pill tag-pill-soft">#情绪编码</span> <span class="tag-pill tag-pill-soft">#流匹配</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15755</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15755" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15755" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AuEmoChat框架，通过离散情感令牌空间和令牌合并算法，实现更真实的情感对话语音合成。
</div>

## 👥 作者与机构

**Zhenqi Jia** ¹ · Yuan Zhao · Aruukhan · Rui Liu · Haizhou Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、情感计算方向的研究者。建议重点阅读§3.1 AuEmoCodec和§3.3 Authentic Emotion Flow Matching，以及表2的实验结果。可先看§1引言了解动机。

## 🌍 研究背景

对话语音合成（CSS）旨在生成具有类人情感表达和上下文一致性的语音。现有方法受限于预定义情感标签（如七类），无法表达真实情感；同时多轮对话中的冗余多模态令牌干扰上下文理解。本文提出AuEmoChat，通过学习离散真实情感令牌空间和情感引导的令牌合并，解决情感表达不真实和上下文理解困难的问题。

## 💡 核心创新

1. AuEmoCodec: 有限标量量化学习离散真实情感令牌空间
2. AuEmoToMe: 真实情感引导的多模态令牌合并算法
3. Authentic Emotion Flow Matching: 联合条件的情感流匹配渲染

## 🏗️ 模型架构

输入为文本和对话历史（多模态令牌）。首先通过AuEmoCodec（基于FSQ的编码器）将情感语音编码为离散情感令牌。AuEmoToMe根据情感相关性合并冗余令牌，保留情感上下文。然后自回归文本-语音模型预测目标情感令牌和语音令牌。最后Authentic Emotion Flow Matching以合并后的对话上下文、目标情感令牌和声学先验为条件，通过流匹配生成语音波形。

## 📚 数据集

- NCSSD-EmCap（训练和评估，规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（自然度） | NCSSD-EmCap | VALL-E 2 (3.85) | **4.12** | +0.27 |
| MOS（情感表达） | NCSSD-EmCap | EmoVALL-E (3.72) | **4.08** | +0.36 |

在NCSSD-EmCap数据集上，AuEmoChat在自然度和情感表达MOS上均超越VALL-E 2、EmoVALL-E等基线。消融实验验证了AuEmoCodec和AuEmoToMe的有效性。未提供跨数据集泛化或效率指标。

## 🎯 结论与影响

AuEmoChat通过离散真实情感令牌和情感引导令牌合并，显著提升了对话语音合成的情感真实性和上下文一致性。该工作为情感CSS提供了新范式，有望推动人机交互中更自然的情感表达。工业上可用于虚拟助手、有声书等场景。

## ⚠️ 局限与未解决问题

仅在单一数据集NCSSD-EmCap上评估，缺乏跨数据集泛化验证；未报告推理速度或模型参数量；情感令牌空间的可解释性未讨论；未与基于扩散或GAN的方法对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
