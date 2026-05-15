---
title: "Physics-Based iOCT Sonification for Real-time Interaction Awareness in Subretinal Injection"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉显示"]
summary: "提出基于物理的iOCT声化框架，将视网膜层特征映射为听觉反馈，提升视网膜下注射手术中的实时交互感知。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#听觉显示</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#医学超声</span> <span class="tag-pill tag-pill-soft">#实时反馈</span> <span class="tag-pill tag-pill-soft">#手术引导</span> <span class="tag-pill tag-pill-soft">#听觉显示</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14500</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14500" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14500" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于物理的iOCT声化框架，将视网膜层特征映射为听觉反馈，提升视网膜下注射手术中的实时交互感知。
</div>

## 👥 作者与机构

**Luis D. Reyes Vargas** ¹ · Veronica Ruozzi · Andrea K. M. Ross · Shervin Dehghani · Michael Sommersperger · Koorosh Faridpooya · Mohammad Ali Nasseri · Merle Fairhurst · … 等 2 人

**机构**：慕尼黑工业大学 · 约翰霍普金斯大学 · 汉诺威医学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合医学影像与听觉显示交叉领域研究者。建议重点阅读§3方法部分及§4用户实验设计，关注声化映射策略与实验结果。

## 🌍 研究背景

视网膜下注射手术需要精确的针尖定位，避免损伤RPE层。术中OCT提供高分辨率横截面图像，但需要医生同时关注显微镜视图，增加认知负荷。现有声化方法缺乏结构化映射，无法有效传达解剖特征。本文旨在通过物理启发的声化模型，将iOCT衍生的解剖特征实时转换为听觉反馈，降低视觉依赖。

## 💡 核心创新

1. 物理启发的声学模型驱动声化
2. 基于视网膜层分割的结构化映射
3. 针尖运动和视网膜位移作为激励输入
4. 用户实验验证事件识别准确率显著提升

## 🏗️ 模型架构

输入为iOCT B-scan流，经分割网络提取视网膜层（如RPE、神经纤维层等）。物理声学模型以分割层为声源，针尖运动和层位移作为激励，生成听觉反馈。输出为实时音频信号，映射工具位置和视网膜变形。

## 📚 数据集

- iOCT B-scan序列（用户实验，n=34）
- 专家评估（n=4）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 事件识别准确率 | 用户实验 | 基线方法 60.6% | **83.4%** | +22.8% |

用户实验（n=34）显示，所提声化方法在视网膜层识别和变形事件检测上显著优于基线（83.4% vs 60.6%, p<0.001），主要提升来自注射诱导的视网膜变形检测。专家评估（n=4）确认了临床相关性和术中应用潜力。

## 🎯 结论与影响

本文证明结构化iOCT声化可作为视网膜下注射手术中实时引导的有效补充模态，显著提升事件识别准确率。该工作为术中听觉反馈设计提供了新范式，有望降低手术认知负荷，提高安全性。

## ⚠️ 局限与未解决问题

实验规模有限（n=34用户，n=4专家），未报告推理延迟或实时性指标。声化映射策略可能需针对不同手术场景调整，泛化性未验证。缺乏与视觉反馈的对比实验。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
