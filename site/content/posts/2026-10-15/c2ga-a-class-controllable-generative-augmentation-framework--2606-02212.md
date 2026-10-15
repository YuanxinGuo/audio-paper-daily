---
title: "C2GA: A Class-Controllable Generative Augmentation Framework for Respiratory Sound Classification"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "用条件VQ-VAE构建离散隐空间，配合Transformer自回归先验生成类别可控的呼吸音梅尔谱，用于呼吸音分类数据增强。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#VQ-VAE</span> <span class="tag-pill tag-pill-soft">#医学音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.02212</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.02212" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.02212" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用条件VQ-VAE构建离散隐空间，配合Transformer自回归先验生成类别可控的呼吸音梅尔谱，用于呼吸音分类数据增强。
</div>

## 👥 作者与机构

**Ziqi Ma** ¹ · Mengyu Han · Anteng Cai · Zhanchong Liu · Bowen Feng · Hang Yu · Sheng Hu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做医学音频/小样本音频分类与生成式数据增强的研究者阅读。建议重点看 §3 的 VQ-VAE 离散隐空间与类别原型解耦设计，以及 §4 的分类增益与消融实验。若只关心语音增强/分离，可略读。可先看表 2 的类别可控性对比。

## 🌍 研究背景

呼吸音分类在肺部病理临床识别中很关键，但真实听诊数据集规模小、噪声重、类别极不平衡。传统音频增强（加噪、变速、SpecAugment）易扭曲细微病理特征；VAE/GAN 生成方法样本保真度有限、类别语义可控性差，在弱监督下尤甚。本文要解决的是：如何在标注稀缺条件下生成高保真且类别语义可控的呼吸音样本，以提升分类鲁棒性与泛化。

## 💡 核心创新

1. 条件VQ-VAE构建离散隐空间，将局部声学token与全局类别原型显式解耦
2. Transformer自回归先验生成标签一致的token序列
3. 生成token与类别原型融合后解码为高保真梅尔谱

## 🏗️ 模型架构

输入为呼吸音梅尔谱，先经条件VQ-VAE编码到离散隐空间，其中局部声学token与全局类别原型显式解耦；随后训练一个基于Transformer的自回归先验，在类别条件下生成标签一致的token序列；生成token与对应类别原型融合后送入解码器，重建高保真梅尔谱用于数据增强。摘要未给出参数量与具体层数。

## 📊 实验结果

摘要仅给出定性结论，称C2GA提供了有效且语义可靠的增强策略，能提升呼吸音分类在真实临床场景下的鲁棒性与泛化，但未报告具体指标数值、数据集名称或与基线的定量对比，无法据此判断增益幅度。

## 🎯 结论与影响

本文最强结论是：类别可控的离散生成式增强可缓解呼吸音数据稀缺与不平衡问题。对医学音频小样本方向，提供了token-原型解耦的可控生成范式，可能推动后续在ICBHI等基准上的生成式增强研究。工业上或可用于听诊AI的数据扩增与长尾补全。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果、数据集与基线对比，难以评估真实增益；缺少消融验证token-原型解耦与自回归先验各自贡献；未报告推理延迟与生成成本；生成样本的临床有效性缺乏医生评估。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-15/">← 返回 2026-10-15 速递</a></div>
