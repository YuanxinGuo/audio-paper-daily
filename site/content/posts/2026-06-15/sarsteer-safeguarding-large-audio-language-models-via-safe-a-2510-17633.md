---
title: "SARSteer: Safeguarding Large Audio-Language Models via Safe-Ablated Refusal Steering"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频安全"]
summary: "提出首个针对大型音频语言模型的推理时安全防御框架SARSteer，通过文本衍生的拒绝引导和解耦安全空间消融，有效提升有害查询拒绝率同时保持良性响应。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大型音频语言模型</span> <span class="tag-pill tag-pill-soft">#安全对齐</span> <span class="tag-pill tag-pill-soft">#推理时防御</span> <span class="tag-pill tag-pill-soft">#拒绝引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.17633</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/linweiii/SARSteer" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">linweiii/SARSteer</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.17633" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.17633" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/linweiii/SARSteer" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个针对大型音频语言模型的推理时安全防御框架SARSteer，通过文本衍生的拒绝引导和解耦安全空间消融，有效提升有害查询拒绝率同时保持良性响应。
</div>

## 👥 作者与机构

**Weilin Lin** ¹ · Jianze Li · Hui Xiong · Li Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态大模型安全、音频对齐的研究者阅读。建议重点读§3方法部分和§4实验，特别是表1和表2的对比结果。可先看§3.2的拒绝引导和解耦消融设计。

## 🌍 研究背景

大型音频语言模型（LALM）在现实应用中日益重要，但音频输入比文本更容易引发有害响应，带来新的部署风险。现有LLM和视觉语言模型的安全对齐方法直接迁移到LALM面临两个问题：1）基于LLM的引导因激活分布差异在音频输入下失效；2）基于提示的防御导致对良性语音查询过度拒绝。本文旨在解决LALM的安全对齐问题，提出首个推理时防御框架。

## 💡 核心创新

1. 提出SARSteer，首个LALM推理时安全防御框架
2. 利用文本衍生的拒绝引导向量，无需修改音频输入
3. 引入解耦安全空间消融，缓解过度拒绝问题

## 🏗️ 模型架构

SARSteer是一个推理时干预框架，不修改LALM模型参数。输入为音频查询，首先通过LALM的音频编码器提取特征，然后与文本衍生的拒绝引导向量结合，在潜在空间进行干预。关键模块包括：1）文本衍生拒绝引导：从安全对齐的LLM中提取拒绝方向向量，映射到LALM空间；2）解耦安全空间消融：识别并移除良性查询中与拒绝方向重叠的成分，减少误拒。输出为模型生成的文本响应。

## 📚 数据集

- HarmfulQA-Audio（构建的有害音频查询集，用于评估）
- BenignQA-Audio（构建的良性音频查询集，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 有害查询拒绝率（%） | HarmfulQA-Audio | 无防御 0.0 | **92.3** | +92.3% |
| 良性查询准确率（%） | BenignQA-Audio | 无防御 100.0 | **97.5** | -2.5% |

实验表明，SARSteer在有害查询拒绝率上达到92.3%，显著优于无防御基线（0%）和基于提示的防御（约30%），同时良性查询准确率仅下降2.5%，优于对比方法的过度拒绝问题。消融实验验证了解耦消融模块对减少误拒的关键作用。

## 🎯 结论与影响

SARSteer是首个针对LALM的推理时安全防御框架，通过文本衍生的拒绝引导和解耦安全空间消融，有效平衡了安全性与可用性。该工作为多模态音频模型的安全对齐提供了新范式，有望推动LALM在敏感场景的落地应用。

## ⚠️ 局限与未解决问题

方法依赖文本衍生的拒绝方向，可能无法覆盖所有音频特有的有害模式；实验仅在特定LALM架构上验证，泛化性未知；未报告推理延迟开销；良性查询准确率仍有下降空间。

## 🔗 开源资源

- **代码**：<https://github.com/linweiii/SARSteer>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
