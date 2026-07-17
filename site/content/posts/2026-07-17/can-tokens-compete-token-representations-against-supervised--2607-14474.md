---
title: "Can Tokens Compete? Token Representations against Supervised CNN Backbones for BirdCLEF+ 2026"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "本文探索了基于token的表示（神经音频编解码器）与监督CNN骨干在BirdCLEF+2026鸟类声音检测任务中的对比，构建了一个集成基线系统。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#鸟鸣识别</span> <span class="tag-pill tag-pill-soft">#音频表示学习</span> <span class="tag-pill tag-pill-soft">#模型集成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14474</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/dsgt-arc/birdclef-2026" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">dsgt-arc/birdclef-2026</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14474" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14474" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/dsgt-arc/birdclef-2026" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文探索了基于token的表示（神经音频编解码器）与监督CNN骨干在BirdCLEF+2026鸟类声音检测任务中的对比，构建了一个集成基线系统。
</div>

## 👥 作者与机构

**Anthony Miyaguchi** ¹ · Murilo Gustineli · Adrian Cheung

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对生物声学或声音事件检测感兴趣的读者。可重点看§3.2的token表示对比实验和§4的集成方法。若时间有限，略读即可。

## 🌍 研究背景

BirdCLEF竞赛旨在从声景中检测动物叫声，2026版新增约1小时标注数据，转向监督学习。现有方法多采用预训练CNN骨干（如Perch v2）或基础模型嵌入。然而，token化表示（如神经音频编解码器）在生物声学中的潜力尚未充分探索。本文旨在对比两类表示，并构建一个计算高效的集成系统。

## 💡 核心创新

1. 集成冻结Perch v2、HGNetV2-B0和原型头的基线系统
2. 对比神经音频编解码器token与语义嵌入在生物声学中的表现
3. 在90分钟CPU预算内达到0.936私有榜分数

## 🏗️ 模型架构

输入为声景音频，经特征提取后分别送入三个分支：1) 冻结的Perch v2骨干（预训练生物声学模型）；2) 训练的HGNetV2-B0声音事件检测网络；3) 非鸟类原型头。三个分支的输出通过集成策略得到最终多标签预测。token表示部分对比了两种生物声学专家模型和四种基于AudioSet训练的token编码器。

## 📚 数据集

- BirdCLEF+2026（训练/评估，约1小时标注声景）

## 📊 实验结果

摘要未提供具体指标数值，仅给出私有榜分数0.936（排名1894/？）。token表示对比部分未给出量化结果，仅提及对比了两种生物声学专家模型和四种token编码器。

## 🎯 结论与影响

本文构建的集成基线在BirdCLEF+2026上取得了有竞争力的分数，但token表示尚未超越监督CNN骨干。该工作为生物声学中的表示学习提供了初步对比，但结论有限。对工业落地影响较小。

## ⚠️ 局限与未解决问题

实验仅在单一竞赛数据集上进行，缺乏跨数据集泛化验证；token表示对比未给出具体指标，结论不充分；未报告模型参数量或推理延迟；集成方法计算开销未分析。

## 🔗 开源资源

- **代码**：<https://github.com/dsgt-arc/birdclef-2026>

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
