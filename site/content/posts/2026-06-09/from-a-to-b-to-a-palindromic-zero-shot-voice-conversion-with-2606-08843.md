---
title: "From A to B to A: Palindromic Zero-Shot Voice Conversion with Non-Parallel Data"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音转换"]
summary: "提出基于KNN检索WavLM表征的零样本语音转换框架，利用非平行数据构建合成训练对，支持多语言且仅用英文数据训练。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本语音转换</span> <span class="tag-pill tag-pill-soft">#KNN检索</span> <span class="tag-pill tag-pill-soft">#WavLM</span> <span class="tag-pill tag-pill-soft">#非平行数据</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.08843</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://palindromic-vc.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">palindromic-vc.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.08843" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.08843" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://palindromic-vc.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于KNN检索WavLM表征的零样本语音转换框架，利用非平行数据构建合成训练对，支持多语言且仅用英文数据训练。
</div>

## 👥 作者与机构

**Moshe Mandel** ¹ · Shlomo E. Chazan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音转换、零样本学习方向的研究者。建议通读，重点看§3的KNN检索对齐方法和§4的说话人损失设计。可先看表1对比结果。

## 🌍 研究背景

语音转换旨在改变说话人身份而保留语言内容。现有方法依赖平行数据或复杂对齐，难以扩展到多语言场景。本文提出利用KNN检索WavLM表征来对齐非平行源和目标语音，构建合成训练对，实现零样本语音转换。

## 💡 核心创新

1. KNN检索WavLM表征实现非平行数据对齐
2. 合成-真实训练范式无需平行语料
3. 说话人损失确保目标身份一致性
4. 仅英文训练即可泛化到多语言

## 🏗️ 模型架构

输入源语音和目标语音分别提取WavLM特征，对源语音的每一帧在目标语音特征中执行KNN检索，用检索到的目标帧替换源帧，形成合成输入。合成输入与真实目标语音构成训练对，送入VC模型（如AutoVC或AdaIN-VC）进行监督学习。同时加入预训练说话人验证模型的说话人损失。

## 📚 数据集

- VCTK（英文训练）
- CMU Arctic（英文评估）
- CSTR VCTK（多语言评估）
- LibriTTS（多语言评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（自然度） | VCTK | AutoVC 3.2 | **3.8** | +0.6 |
| MOS（相似度） | VCTK | AutoVC 3.0 | **3.7** | +0.7 |

在英文VCTK上，本文方法在自然度和相似度MOS上均优于AutoVC等基线。跨语言实验（中文、德语、法语）表明，仅英文训练的模型也能取得高相似度，验证了零样本泛化能力。消融实验显示KNN检索和说话人损失均贡献显著。

## 🎯 结论与影响

本文提出一种简洁有效的零样本语音转换框架，利用KNN检索实现非平行数据对齐，仅英文训练即可泛化到多语言。该方法为低资源语言VC提供了新思路，有望推动多语言语音转换的实用化。

## ⚠️ 局限与未解决问题

依赖WavLM特征质量，对噪声鲁棒性未评估；KNN检索计算开销较大，未报告推理速度；仅评估了有限语言，更多语言需验证。

## 🔗 开源资源

- **Demo / 试听**：<https://palindromic-vc.github.io>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
