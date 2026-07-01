---
title: "MAGE: Modality-Agnostic Music Generation and Target-Source Extraction"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出MAGE框架，统一文本/视觉/混合条件进行音乐生成与目标源提取，在MUSIC基准上验证有效性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标源提取</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#MUSIC数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09803</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09803" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09803" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MAGE框架，统一文本/视觉/混合条件进行音乐生成与目标源提取，在MUSIC基准上验证有效性。
</div>

## 👥 作者与机构

**Muhammad Usama Saleem** ¹ · Tejasvi Ravi · Tianyu Xu · Rajeev Nongpiur · Ishan Chatterjee · Mayur Jagdishbhai Patel · Pu Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态音频生成与源分离研究者。建议重点阅读§3的Controlled Multimodal FluxFormer和§4.2的消融实验，了解动态模态掩蔽与跨门控调制机制。

## 🌍 研究背景

现有音乐生成系统通常针对单一模式：要么无参考混合生成，要么从混合中提取目标源。当同时存在文本、视觉和混合输入时，固定任务设计限制了灵活性。本文旨在构建一个模态无关的统一框架，在共享连续潜空间中同时支持条件音乐生成和混合引导的目标源提取。

## 💡 核心创新

1. Controlled Multimodal FluxFormer统一条件流建模
2. Audio-Visual Nexus Alignment对齐帧级视觉特征到音频潜序列
3. 跨门控调制机制融合视觉与文本语义
4. 动态模态掩蔽训练实现多条件兼容

## 🏗️ 模型架构

输入：文本/视觉/混合音频条件。主干：Controlled Multimodal FluxFormer，建模从噪声到目标音频潜的条件流。关键模块：Audio-Visual Nexus Alignment将视觉特征映射到音频潜序列；跨门控调制用对齐的视觉表示调节中间音频特征，文本提供独立语义引导。输出：生成或提取的音频潜。

## 📚 数据集

- MUSIC（训练与评估，包含音乐视频与混合音频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | MUSIC | 未见 | **未见** | 未见 |

摘要未提供具体数值，仅说明MAGE在无混合生成和混合引导目标源提取两种协议下均优于基线，且对齐与门控组件改善了提取任务中的干扰抑制。

## 🎯 结论与影响

MAGE首次实现模态无关的音乐生成与目标源提取统一框架，通过动态模态掩蔽和跨门控调制有效融合多模态条件。该工作为多模态音频生成与分离的联合建模提供了新范式，有望推动交互式音乐创作和音视频内容编辑的工业应用。

## ⚠️ 局限与未解决问题

仅在一个数据集（MUSIC）上评估，缺乏跨数据集泛化验证；未报告参数量、推理速度等效率指标；未与近期多模态生成模型（如AudioLDM2）进行对比；目标源提取性能可能受视觉对齐质量影响。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
