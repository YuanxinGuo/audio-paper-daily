---
title: "FoleySet: A Multi-Level Human-Annotated Foley Sound Dataset"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频数据集"]
summary: "FoleySet是一个包含10,000个音频片段、带两级Foley分类标注的公开数据集，旨在推动数据驱动的Foley音效研究。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频数据集</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Foley音效</span> <span class="tag-pill tag-pill-soft">#音效分类</span> <span class="tag-pill tag-pill-soft">#音效检索</span> <span class="tag-pill tag-pill-soft">#音效生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25980</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25980" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25980" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FoleySet是一个包含10,000个音频片段、带两级Foley分类标注的公开数据集，旨在推动数据驱动的Foley音效研究。
</div>

## 👥 作者与机构

**Sunshiyu Wang** ¹ · Alexander Lerch

**机构**：佐治亚理工学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音效分类、检索、生成的研究者阅读。建议重点看数据集构建方法（§3）和标注体系（§2），评估其分类体系是否适用于自己的任务。

## 🌍 研究背景

在影视后期制作中，Foley音效（如脚步声、衣物摩擦声）通常由专业拟音师录制，资源消耗大。数据驱动的Foley研究（分类、检索、生成）因缺乏高质量标注数据集而受限。现有数据集规模小、标注不一致或版权受限。本文提出FoleySet，一个10,000条音频、两级分类标注的公开数据集，以标准化资源推动该领域发展。

## 💡 核心创新

1. 构建10,000条Foley音效数据集
2. 提出两级Foley分类体系
3. 采用Creative Commons许可促进开放研究

## 🏗️ 模型架构

数据集构建流程：从多个开源音效库收集原始音频，经人工筛选和标注，形成两级分类体系（第一级6类：脚步声、衣物声、道具声等；第二级子类）。每个音频片段时长1-10秒，采样率44.1kHz，单声道。数据集划分为训练/验证/测试集（比例未明确）。

## 📚 数据集

- FoleySet（10,000条音频，训练/验证/测试）

## 📊 实验结果

摘要未提供具体实验结果，仅描述数据集规模与标注体系。论文可能包含数据集统计分析和基线实验，但摘要未提及。

## 🎯 结论与影响

FoleySet提供了首个大规模、标准化、开放许可的Foley音效数据集，有望推动分类、检索和生成任务的基准建立。对工业界，可降低拟音成本；对学术界，填补了高质量标注数据空白。

## ⚠️ 局限与未解决问题

数据集仅包含10,000条音频，类别分布可能不均衡；未提及音频时长分布和信噪比等质量控制细节；缺乏与现有数据集的对比分析；未报告基线模型性能。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
