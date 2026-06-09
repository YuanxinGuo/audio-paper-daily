---
title: "Universal Speech Content Factorization"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音转换"]
summary: "提出一种可逆线性方法，从语音中提取低秩表示，抑制音色同时保留内容，实现零样本语音转换和音色提示的TTS。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音内容分解</span> <span class="tag-pill tag-pill-soft">#零样本语音转换</span> <span class="tag-pill tag-pill-soft">#音色解耦</span> <span class="tag-pill tag-pill-soft">#文本转语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.08977</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.08977" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.08977" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种可逆线性方法，从语音中提取低秩表示，抑制音色同时保留内容，实现零样本语音转换和音色提示的TTS。
</div>

## 👥 作者与机构

**Henry Li Xinyuan** ¹ · Zexin Cai · Lin Zhang · Leibny Paola Garc\'ia-Perera · Berrak Sisman · Sanjeev Khudanpur · Nicholas Andrews · Matthew Wiesner

**机构**：约翰霍普金斯大学 · 德克萨斯大学达拉斯分校 · 南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音转换和TTS研究者。重点读§3方法部分和§4实验。可先看表1和表2对比结果，再读§3.2的通用映射学习。

## 🌍 研究背景

语音内容分解旨在从语音中分离出与说话人无关的内容特征，对语音转换和TTS至关重要。现有方法如Speech Content Factorization（SCF）仅适用于闭集场景，需要大量目标说话人数据。零样本VC方法通常依赖复杂神经网络或大量训练数据。本文提出USCF，通过最小二乘优化学习通用语音到内容映射，仅需几秒目标语音即可推导说话人特定变换，实现开放集零样本VC。

## 💡 核心创新

1. 提出通用语音内容分解（USCF），将闭集SCF扩展到开放集
2. 通过最小二乘优化学习通用语音到内容映射
3. 仅需几秒目标语音即可推导说话人特定变换
4. USCF特征可作为音色解耦声学表示用于TTS
5. 方法简单、可逆、线性，无需额外神经网络训练

## 🏗️ 模型架构

输入语音特征（如Mel谱）→ 通过最小二乘优化学习通用映射矩阵，将语音投影到低秩内容空间，抑制音色信息 → 从目标说话人少量语音中推导说话人特定变换矩阵 → 通过逆变换重构语音。整体为线性可逆变换，无神经网络模块。

## 📚 数据集

- VCTK（训练通用映射和评估VC）
- LibriTTS（评估零样本VC和TTS）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | VCTK | SCF 12.3% | **USCF 11.8%** | -0.5% |
| MOS自然度 | VCTK | SCF 3.8 | **USCF 3.9** | +0.1 |
| MOS相似度 | VCTK | SCF 3.5 | **USCF 3.6** | +0.1 |

USCF在零样本VC任务中，WER为11.8%，优于SCF的12.3%；自然度和相似度MOS分别达3.9和3.6，与需要更多数据或神经网络的基线相当。嵌入分析显示USCF有效去除音色变化。在TTS任务中，USCF特征作为声学表示，训练音色提示TTS模型，生成语音保持内容且音色可控。

## 🎯 结论与影响

USCF是一种简单有效的语音内容分解方法，通过线性变换实现零样本VC和音色解耦TTS。其可逆性和低数据需求对实际应用有潜力，但性能上限受限于线性假设，非线性复杂场景可能不足。

## ⚠️ 局限与未解决问题

线性假设可能限制对复杂声学变化的建模能力；实验仅在VCTK和LibriTTS上评估，泛化性待验证；未与最新神经VC方法（如VALL-E）直接对比；缺乏对噪声和混响鲁棒性的分析。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
