---
title: "MADB: A Large-Scale Music Aesthetics Dataset with Professional and Multi-Dimensional Annotations"
date: 2026-07-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐美学评估"]
summary: "提出包含9999首曲目、10个感知维度和文本注释的大规模音乐美学数据集MADB，并建立统一评估框架，揭示现有模型与人类判断的显著差距。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐美学评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#音乐理解</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#感知评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06929</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/knownree/madb" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">knownree/madb</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06929" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06929" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/knownree/madb" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出包含9999首曲目、10个感知维度和文本注释的大规模音乐美学数据集MADB，并建立统一评估框架，揭示现有模型与人类判断的显著差距。
</div>

## 👥 作者与机构

**Sirui Zhang** ¹ · Tianle Wang · Xinyi Tong · Peiyang Yu · Jishang Chen · Liangke Zhao · Haoxin Zhang · Duo Xu · … 等 3 人

**机构**：北京大学 · 清华大学 · 北京通用人工智能研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、音频感知评估领域的研究者。建议重点阅读第3节（数据集构建）和第4节（评估框架与结果），以了解标注流程和模型性能差距。

## 🌍 研究背景

音乐美学评估旨在量化人类对音乐的感知判断，但该领域因缺乏大规模、多维度标注数据集而进展缓慢。现有数据集规模小、维度单一，且缺乏统一评估基准。本文旨在构建一个大规模、多维度、专业标注的音乐美学数据集，并建立标准化评估框架，以推动模型与人类感知对齐的研究。

## 💡 核心创新

1. 构建9999首曲目的大规模音乐美学数据集
2. 10个感知维度加1个总体评分的多维度标注
3. 30名专业标注员，每首曲目约10人标注
4. 包含文本评论支持多模态分析
5. 统一评估框架覆盖多个预训练模型

## 🏗️ 模型架构

数据集构建：从公开音乐库筛选9999首曲目，由30名经过培训的标注员在10个感知维度（如愉悦度、悲伤度、力量感等）和1个总体评分上进行标注，每首曲目约10人评分，并收集文本评论。评估框架：使用多个预训练模型（如CLAP、MusicFM等）进行特征提取，通过线性探测或微调预测各维度分数，与人类评分对比。

## 📚 数据集

- MADB（9999首曲目，训练/评估/测试划分）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Pearson相关系数 | MADB测试集 | CLAP 0.45 | **最佳模型 0.52** | +0.07 |

实验表明，现有预训练模型在音乐美学评估任务上表现有限，最佳模型与人类评分的Pearson相关系数仅为0.52，远低于人类间一致性（约0.7）。模型在细粒度维度（如悲伤度、力量感）上表现更差，揭示当前模型缺乏对音乐情感和美学特征的深层理解。

## 🎯 结论与影响

MADB数据集为音乐美学评估提供了大规模、多维度、专业标注的基准，揭示了现有模型与人类感知之间的显著差距。该工作将推动音乐理解模型向更精细、更符合人类感知的方向发展，并为音乐推荐、音乐治疗等应用提供评估基础。

## ⚠️ 局限与未解决问题

数据集仅包含西方流行音乐和古典音乐，缺乏非西方音乐类型；标注员均为中国人，可能存在文化偏差；未提供模型推理效率或参数量对比；未进行跨数据集泛化实验。

## 🔗 开源资源

- **代码**：<https://github.com/knownree/madb>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-09/">← 返回 2026-07-09 速递</a></div>
