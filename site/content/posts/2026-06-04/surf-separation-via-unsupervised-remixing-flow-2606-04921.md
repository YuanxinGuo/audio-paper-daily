---
title: "SURF: Separation via Unsupervised Remixing Flow"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出SURF，一种无监督流匹配方法，仅从混合信号学习源分离，无需干净源数据，在图像和音频基准上达到新SOTA。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#无监督学习</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#音频分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.04921</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://google.github.io/df-conformer/surf/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">google.github.io/df-conformer/surf/</span></span></a><a class="oc-chip oc-chip-demo" href="https://google.github.io/df-conformer/surf/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">google.github.io/df-conformer/surf/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.04921" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.04921" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://google.github.io/df-conformer/surf/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://google.github.io/df-conformer/surf/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SURF，一种无监督流匹配方法，仅从混合信号学习源分离，无需干净源数据，在图像和音频基准上达到新SOTA。
</div>

## 👥 作者与机构

**Henry Li** ¹ · Robin Scheibler · Efthymios Tzinis · Matt Shannon · Arnaud Doucet · John R. Hershey

**机构**：谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离、无监督学习方向的研究者。建议通读，重点看§3的remixing流程和§4与Wake-Sleep算法的联系。可先看实验部分表1-2了解性能提升。

## 🌍 研究背景

单通道源分离是病态问题，监督方法依赖大量干净源数据且对域偏移脆弱。现有无监督方法性能有限。本文旨在提出一种仅利用混合信号的无监督分离方法，避免对干净源数据的依赖。

## 💡 核心创新

1. 结合监督流匹配与自回归自监督技术
2. 提出remixing步骤从教师模型引导学生学习
3. 建立与Wake-Sleep算法的理论联系
4. 在图像和音频上验证无监督SOTA

## 🏗️ 模型架构

SURF基于流匹配框架。输入混合信号，通过教师模型（预训练监督流模型）生成初始估计，然后执行remixing（将估计源重新混合并与原混合对比）以自监督方式训练学生流模型。学生模型学习从混合到源的映射，无需干净源。

## 📚 数据集

- MNIST（图像分离评估）
- dSprites（图像分离评估）
- LibriMix（音频分离评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | LibriMix (2-speaker) | MixIT + Sinkhorn 10.2 | **SURF 13.8** | +3.6 dB |

在LibriMix 2说话人分离任务上，SURF的SI-SDRi达13.8 dB，显著优于现有无监督方法MixIT+Sinkhorn（10.2 dB）。在图像分离任务上，SURF也达到无监督SOTA。消融实验验证了remixing步骤和流匹配目标的有效性。

## 🎯 结论与影响

SURF首次将流匹配成功应用于无监督源分离，仅需混合信号即可学习，性能大幅超越现有无监督方法。该方法为缺乏干净源数据的场景提供了可行方案，有望推动语音分离在真实环境中的应用。

## ⚠️ 局限与未解决问题

实验仅在2源混合上验证，多源场景未测试；依赖教师模型初始化，教师质量影响性能；计算开销可能较大（流匹配推理需多次函数评估）。

## 🔗 开源资源

- **项目主页**：<https://google.github.io/df-conformer/surf/>
- **Demo / 试听**：<https://google.github.io/df-conformer/surf/>

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-04/">← 返回 2026-06-04 速递</a></div>
