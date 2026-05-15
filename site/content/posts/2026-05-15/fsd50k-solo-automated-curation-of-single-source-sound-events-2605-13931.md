---
title: "FSD50K-Solo: Automated Curation of Single-Source Sound Events"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#数据增强"]
summary: "提出一种基于扩散模型和预训练编码器的框架，自动从FSD50K中筛选单源声音事件样本，发布FSD50K-Solo子集。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#数据增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频数据集</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#单源事件检测</span> <span class="tag-pill tag-pill-soft">#数据筛选</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13931</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13931" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13931" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种基于扩散模型和预训练编码器的框架，自动从FSD50K中筛选单源声音事件样本，发布FSD50K-Solo子集。
</div>

## 👥 作者与机构

**Ningyuan Yang** ¹ · Sile Yin · Li-Chia Yang · Bryce Irvin · Xiao Quan · Marko Stamenovic · Shuo Zhang

**机构**：微软研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频数据增强、弱监督学习方向的研究者。建议重点阅读§3数据筛选框架和§4实验部分，尤其是表1的筛选效果对比。可跳过§2背景。

## 🌍 研究背景

高质量训练数据对神经网络性能至关重要，但音频领域缺乏大规模、强标注、单源的声音事件数据集。FSD50K虽大且开放，但包含大量多源样本（背景干扰或事件重叠），限制了其效用。现有数据筛选方法依赖人工或简单规则，难以规模化。本文旨在开发一种自动化框架，从大规模开放音频语料中识别并过滤多源样本。

## 💡 核心创新

1. 使用扩散模型合成干净单类事件构建受控混合样本
2. 预训练音频编码器+判别分类器自动筛选单源样本
3. 发布FSD50K-Solo子集，提供可扩展的数据筛选范式

## 🏗️ 模型架构

输入为音频片段；首先利用扩散模型（如AudioLDM2）合成干净的单类声音事件，与背景噪声混合生成受控多源样本作为训练数据；然后使用预训练音频编码器（如CLAP）提取特征，接一个线性分类器判别样本是否为单源；最后将训练好的分类器应用于FSD50K全量数据，筛选出单源样本。输出为筛选后的子集FSD50K-Solo。

## 📚 数据集

- FSD50K（全量，用于筛选和评估）
- 人类专家标注的测试集（评估筛选性能）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1-score | 人类专家标注测试集 | 无（本文首次提出） | **0.85** | N/A |

在人类专家标注的测试集上，框架达到0.85 F1-score，验证了筛选有效性。消融实验表明扩散模型合成的受控混合数据对训练分类器至关重要。未提供与简单规则或人工筛选的对比。

## 🎯 结论与影响

本文提出的数据筛选框架能有效从FSD50K中识别单源样本，发布FSD50K-Solo子集，为音频领域提供更高质量的训练数据。该方法可扩展到其他开放音频语料，推动弱监督和自监督学习研究。对工业应用而言，可降低数据清洗成本。

## ⚠️ 局限与未解决问题

依赖扩散模型合成质量，可能引入合成数据偏差；仅验证了FSD50K单一数据集；未报告筛选后子集在下游任务（如事件检测）上的性能提升；未与人工筛选或简单能量阈值方法对比。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
