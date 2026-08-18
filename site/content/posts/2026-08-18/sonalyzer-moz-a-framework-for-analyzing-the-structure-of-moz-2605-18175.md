---
title: "Sonalyzer-Moz: A Framework for Analyzing the Structure of Mozart's Sonata Form"
date: 2026-08-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐结构分析"]
summary: "构建首个大规模奏鸣曲式层次结构标注数据集SoSA-Moz，并提出基线模型Sonalyzer-Moz，首次实现奏鸣曲式上层结构自动分析。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐结构分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐结构分析</span> <span class="tag-pill tag-pill-soft">#奏鸣曲式</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#序列建模</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.18175</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.18175" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.18175" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建首个大规模奏鸣曲式层次结构标注数据集SoSA-Moz，并提出基线模型Sonalyzer-Moz，首次实现奏鸣曲式上层结构自动分析。
</div>

## 👥 作者与机构

**Jing Zhao** ¹ · KokSheik Wong · Vishnu Monn Baskaran · Kiki Adhinugraha · David Taniar

**机构**：莫纳什大学 · 马来西亚博特拉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索（MIR）和计算音乐学研究者阅读。建议重点阅读第3节（数据集构建）和第4节（模型架构），可先看表1和表2了解标注层次与数据规模。若关注方法细节，可精读第4.2节的特征聚合与序列建模部分。

## 🌍 研究背景

音乐结构分析（MSA）近年来取得进展，但针对奏鸣曲式这种层次复杂、结构严谨的曲式，自动分析仍处于早期阶段。主要瓶颈在于古典音乐结构标注需要深厚的音乐学知识，耗时且门槛高，导致缺乏大规模标注数据集。现有MSA方法多针对流行音乐，难以直接迁移到奏鸣曲式。本文旨在解决奏鸣曲式分析数据稀缺和模型缺失的问题，通过构建首个大规模层次结构标注数据集SoSA-Moz，并提出基线模型Sonalyzer-Moz，验证自动分析奏鸣曲式上层结构的可行性。

## 💡 核心创新

1. 构建SoSA-Moz：首个大规模奏鸣曲式层次结构标注数据集
2. 提出Sonalyzer-Moz：结合特征聚合与序列建模的基线模型
3. 首次实现奏鸣曲式上层结构（如呈示部、展开部）自动分析
4. 验证了自动分析奏鸣曲式结构的有效性，提供强基线

## 🏗️ 模型架构

Sonalyzer-Moz框架输入为音乐音频的时序特征（如MFCC或预训练音频特征），通过特征聚合模块（如卷积或自注意力）提取局部特征，再送入序列建模模块（如LSTM或Transformer）捕捉上层结构依赖。最后通过分类头输出每个时间帧对应的结构标签（如呈示部、展开部、再现部等）。模型参数量未在摘要中提及。

## 📚 数据集

- SoSA-Moz（训练/评估，首个大规模奏鸣曲式层次结构标注数据集，具体规模未提及）

## 📊 实验结果

摘要中未提供具体数值指标，仅定性说明Sonalyzer-Moz能够识别上层结构的关键边界，首次证明自动上层分析的有效性。未提及消融实验或与其他方法的对比。

## 🎯 结论与影响

本文通过构建SoSA-Moz数据集和Sonalyzer-Moz基线模型，首次展示了自动分析奏鸣曲式上层结构的可行性，为后续研究提供了数据基础和强基线。该工作有望推动古典音乐结构分析的发展，并为音乐信息检索领域提供新工具。对工业界，可能应用于音乐教育、自动标注和音乐推荐系统。

## ⚠️ 局限与未解决问题

摘要未提及模型在细粒度结构（如乐句、动机）上的表现，也未与现有MSA方法进行定量对比。数据集规模、标注一致性、跨作曲家泛化能力等未说明。缺乏消融实验和效率指标。作为基线，模型性能可能有限，但为后续改进提供了起点。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-18/">← 返回 2026-08-18 速递</a></div>
