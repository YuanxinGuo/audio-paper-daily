---
title: "Profy: Interpretable Visualization of Expertise-Dependent Motor Skills Toward Supporting Piano Practice"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐技能评估"]
summary: "提出弱监督系统Profy，利用聚合听众评分作为标签，生成时间对齐的高亮片段辅助钢琴练习，无需局部标注即可识别专家与业余演奏差异。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐技能评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#钢琴练习</span> <span class="tag-pill tag-pill-soft">#弱监督学习</span> <span class="tag-pill tag-pill-soft">#可解释可视化</span> <span class="tag-pill tag-pill-soft">#运动技能分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10627</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10627" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10627" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出弱监督系统Profy，利用聚合听众评分作为标签，生成时间对齐的高亮片段辅助钢琴练习，无需局部标注即可识别专家与业余演奏差异。
</div>

## 👥 作者与机构

**Kazuki Kawamura** ¹ · Fujiki Nakamura · Hayato Nishioka · Momoko Shioki · Shinichi Furuya · Jun Rekimoto

**机构**：东京大学 · 索尼计算机科学实验室 · 庆应义塾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐技术、人机交互领域研究者。建议重点阅读§3方法部分和§4实验设计，特别是弱监督训练策略和可视化评估。可先看表1和Fig.3了解系统框架。

## 🌍 研究背景

钢琴演奏质量取决于细微的时序、力度和发音控制，但现有练习反馈多为整体评分，难以指导具体改进。传统方法需要逐帧标注专家与业余差异，成本高且主观。本文旨在开发无需局部标注的系统，自动识别演奏中需改进的段落。

## 💡 核心创新

1. 弱监督学习：仅用曲目级标签训练，输出时间对齐的片段级高亮
2. 证据分数机制：在共享时间基上输出预测与证据分数，支持可视化
3. 大规模数据集：采集73名钢琴家的同步键运动与音频数据（1083个有效片段）

## 🏗️ 模型架构

输入为同步的1kHz键运动与音频信号，经特征提取后送入时序模型（未明确网络结构，推测为CNN或RNN），输出clip级预测和证据分数。模型在共享的降采样时间基上生成对齐的可视化高亮，支持用户浏览、循环和聚焦回放。

## 📚 数据集

- 自采集数据集（73名钢琴家，1083个有效片段，用于训练和评估）
- 20个业余短技术练习片段（由21名专家钢琴家标注，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Pearson r | 20个业余片段（专家标注） | 无（弱监督基线） | **0.61** | N/A |
| ROC-AUC | 20个业余片段（专家标注） | 无 | **0.75** | N/A |

在20个业余片段上，系统生成的高亮分数与专家标注的需改进段落显著相关（Pearson r=0.61, ROC-AUC=0.75），表明无需局部标注即可有效识别专家与业余差异。实验未提供与其他方法的对比，也未报告消融或效率指标。

## 🎯 结论与影响

Profy证明了弱监督学习在钢琴练习反馈中的可行性，通过聚合听众评分生成可解释的可视化高亮，帮助学习者定位需改进的段落。该方法有望推广至其他运动技能学习场景，但需更多对比实验验证其优势。

## ⚠️ 局限与未解决问题

缺乏与现有方法（如全监督或基于规则的系统）的定量对比；数据集仅包含钢琴演奏，泛化性未知；未报告模型参数量或推理延迟；弱监督标签依赖听众评分，可能存在主观偏差。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
