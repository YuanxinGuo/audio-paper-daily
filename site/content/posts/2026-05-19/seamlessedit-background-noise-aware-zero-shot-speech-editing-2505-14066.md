---
title: "SeamlessEdit: Background Noise Aware Zero-Shot Speech Editing with in-Context Enhancement"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑"]
summary: "提出SeamlessEdit框架，通过频带感知噪声抑制和上下文内增强实现噪声环境下的零样本语音编辑。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音编辑</span> <span class="tag-pill tag-pill-soft">#噪声抑制</span> <span class="tag-pill tag-pill-soft">#零样本语音合成</span> <span class="tag-pill tag-pill-soft">#频带感知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2505.14066</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2505.14066" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2505.14066" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SeamlessEdit框架，通过频带感知噪声抑制和上下文内增强实现噪声环境下的零样本语音编辑。
</div>

## 👥 作者与机构

**Kuan-Yu Chen** ¹ · Jeng-Lin Li · De-Yan Lu · Jian-Jiun Ding

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编辑和语音增强领域的研究者阅读。建议重点看§3.2频带感知噪声抑制模块和§3.3上下文内增强策略，以及表1-2的定量结果。可先通读摘要和引言了解动机。

## 🌍 研究背景

零样本语音合成技术发展迅速，语音编辑（插入/替换）在清洁语音场景下已取得较好效果。然而，现有方法未考虑真实环境中的背景噪声，导致编辑质量严重下降。本文旨在解决噪声场景下的语音编辑问题，提出噪声鲁棒的SeamlessEdit框架。

## 💡 核心创新

1. 频带感知噪声抑制模块
2. 上下文内增强策略
3. 首个针对噪声场景的语音编辑框架

## 🏗️ 模型架构

SeamlessEdit基于编码器-解码器架构。输入含噪语音和编辑文本，首先通过频带感知噪声抑制模块（FBNSM）对频谱进行频带级噪声抑制，然后利用上下文内增强策略（ICRS）在编辑区域周围进行上下文增强，最后通过零样本语音合成器生成编辑后的干净语音。

## 📚 数据集

- LibriTTS（训练/评估，清洁语音）
- DNS-Challenge（噪声数据，用于模拟噪声场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS | 自建噪声测试集 | EditSpeech 3.2 | **4.1** | +0.9 |
| CER (%) | 自建噪声测试集 | EditSpeech 8.5 | **5.2** | -3.3% |

在自建噪声测试集上，SeamlessEdit在MOS和CER指标上均优于EditSpeech等基线。消融实验验证了频带感知噪声抑制和上下文内增强的有效性。在清洁语音场景下，SeamlessEdit也保持了与现有方法相当的性能。

## 🎯 结论与影响

SeamlessEdit首次实现了噪声环境下的零样本语音编辑，通过频带感知噪声抑制和上下文内增强有效提升了编辑质量。该工作为语音编辑在真实场景中的应用奠定了基础，有望推动语音编辑在语音助手、内容制作等领域的落地。

## ⚠️ 局限与未解决问题

仅在模拟噪声场景下评估，未在真实噪声环境中验证；未报告模型参数量和推理速度；噪声抑制模块可能对语音音色造成轻微影响；未与其他语音增强+编辑级联方法对比。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
