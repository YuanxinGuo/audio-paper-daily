---
title: "Listening or Reading? Evaluating Speech Awareness in Chain-of-Thought Speech-to-Text Translation"
date: 2026-08-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "本文通过归因分析、鲁棒性测试和韵律感知评估，发现CoT语音翻译主要依赖转录文本，对语音信息利用不足，并提出训练干预增强语音感知。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音翻译</span> <span class="tag-pill tag-pill-soft">#思维链</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.03115</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.03115" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.03115" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文通过归因分析、鲁棒性测试和韵律感知评估，发现CoT语音翻译主要依赖转录文本，对语音信息利用不足，并提出训练干预增强语音感知。
</div>

## 👥 作者与机构

Jacobo Romero-D\'iaz · Gerard I. G\'allego · Oriol Pareras · Federico Costa · Javier Hernando · Cristina Espa\~na-Bonet

**机构**：加泰罗尼亚理工大学 · 德国萨尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音翻译、多模态LLM和可解释性研究者阅读。建议重点阅读第3节（归因方法）和第4节（鲁棒性实验），可先看摘要和结论快速了解核心发现。

## 🌍 研究背景

级联式S2TT系统（ASR+T2TT）存在错误传播和无法利用韵律等声学线索的问题。CoT提示被引入以期望联合访问语音和转录能克服这些局限。然而，CoT是否真正利用语音信息尚不明确。本文通过归因分析、鲁棒性评估和韵律感知测试，系统探究CoT在S2TT中的实际行为，挑战其假设优势。

## 💡 核心创新

1. 提出基于归因的方法分析CoT对语音和文本的依赖
2. 设计鲁棒性评估（损坏转录）揭示CoT的级联行为
3. 引入韵律感知测试评估CoT对声学线索的利用
4. 提出简单训练干预（直接S2TT数据、噪声转录）增强语音归因

## 🏗️ 模型架构

本文不提出新模型，而是分析现有CoT S2TT系统。系统通常由语音编码器（如Whisper）和LLM组成，输入语音和转录，通过CoT生成翻译。归因方法可能基于梯度或注意力，鲁棒性测试通过扰动转录输入，韵律感知测试通过修改韵律特征。

## 📚 数据集

- CoVoST 2（评估，多语言语音翻译）
- MuST-C（评估，多语言语音翻译）

## 📊 实验结果

摘要未提供具体数值，但定性结果表明CoT主要依赖转录，语音归因较低；训练干预（直接S2TT数据、噪声转录注入）能提升语音归因和鲁棒性。

## 🎯 结论与影响

CoT在S2TT中并未有效利用语音信息，主要依赖转录，挑战其假设优势。研究强调需要显式集成声学信息的架构。对后续研究有重要启示，可能推动多模态LLM在语音翻译中的改进。

## ⚠️ 局限与未解决问题

未提供具体实验数值，缺乏与强基线的定量对比；归因方法可能不精确；训练干预的效果未充分消融；未讨论推理效率。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-21/">← 返回 2026-08-21 速递</a></div>
