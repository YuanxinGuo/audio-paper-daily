---
title: "Deepfake Media Generation and Detection in the Generative AI Era: A Survey and Outlook"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#深度伪造检测"]
summary: "全面综述深度伪造生成与检测技术，涵盖图像、视频、音频和多模态，构建分类法并发布新基准。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#深度伪造生成</span> <span class="tag-pill tag-pill-soft">#深度伪造检测</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2411.19537</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/CroitoruAlin/biodeep" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">CroitoruAlin/biodeep</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2411.19537" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2411.19537" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CroitoruAlin/biodeep" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>全面综述深度伪造生成与检测技术，涵盖图像、视频、音频和多模态，构建分类法并发布新基准。
</div>

## 👥 作者与机构

**Florinel-Alin Croitoru** ¹ · Andrei-Iulian Hiji · Vlad Hondru · Nicolae Catalin Ristea · Paul Irofti · Marius Popescu · Cristian Rusu · Radu Tudor Ionescu · … 等 2 人

**机构**：布加勒斯特大学 · 罗马尼亚科学院 · MBZUAI · 中佛罗里达大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合深度伪造领域研究者快速了解全貌。建议重点阅读第3节（检测方法分类）和第5节（新基准与实验结果），可跳过第2节（生成方法）的细节。

## 🌍 研究背景

深度伪造技术快速发展，生成逼真的虚假媒体内容，对安全构成威胁。现有综述多聚焦单一模态或特定方法，缺乏跨模态、系统性的分类与评估。本文旨在填补这一空白，全面梳理生成与检测方法，并构建多模态基准评估泛化能力。

## 💡 核心创新

1. 构建深度伪造生成与检测的统一分类法
2. 覆盖图像、视频、音频、多模态四种媒体类型
3. 提出多模态分布外检测基准
4. 评估现有检测器在未见生成器上的泛化失败

## 🏗️ 模型架构

本文为综述，无具体模型架构。但基准测试采用多种现有检测器（如Xception、EfficientNet、MesoNet等）在图像、视频、音频数据集上评估，并引入多模态混合测试集。

## 📚 数据集

- FaceForensics++（图像/视频检测训练与评估）
- Celeb-DF（视频检测评估）
- DFDC（视频检测评估）
- FakeAVCeleb（多模态检测评估，新基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| AUC | FakeAVCeleb（多模态） | Xception 0.82 | **0.85** | +0.03 |

在FakeAVCeleb多模态基准上，最佳检测器（Xception）AUC为0.85，但跨域泛化测试显示，所有检测器在未见生成器上的AUC下降超过0.2，表明现有方法泛化能力不足。

## 🎯 结论与影响

本文系统梳理了深度伪造生成与检测技术，并揭示当前检测器在分布外数据上的脆弱性。未来研究需关注跨模态、跨生成器的鲁棒检测方法，对工业部署具有警示意义。

## ⚠️ 局限与未解决问题

综述未提供新检测方法，仅评估现有模型；基准规模有限（仅一个多模态数据集）；未深入分析音频专用检测器（如RawNet2）的性能。

## 🔗 开源资源

- **代码**：<https://github.com/CroitoruAlin/biodeep>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
