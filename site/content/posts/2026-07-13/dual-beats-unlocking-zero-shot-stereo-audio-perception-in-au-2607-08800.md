---
title: "Dual-BEATs: Unlocking Zero-Shot Stereo Audio Perception in Audio Large Language Models via Dithering"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出Dual-BEATs架构，通过左右声道独立编码并注入抖动噪声，使音频大语言模型实现零样本立体声感知。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#零样本</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#抖动</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08800</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08800" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08800" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Dual-BEATs架构，通过左右声道独立编码并注入抖动噪声，使音频大语言模型实现零样本立体声感知。
</div>

## 👥 作者与机构

**Shuo-Chun Lin** ¹ · Hen-Hsen Huang

**机构**：台湾中央研究院 · 台湾阳明交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究音频LLM空间感知的读者。重点看§3的抖动机制和§4的零样本泛化实验。建议先读§3.2理解抖动如何绕过归一化瓶颈。

## 🌍 研究背景

多模态大语言模型在语义音频理解上表现优异，但受限于单声道表示，缺乏空间感知能力。现有空间音频方法依赖复杂房间模拟或定制立体声编码器，泛化性差。本文旨在通过简单架构修改，使标准多模态模型具备零样本立体声理解能力。

## 💡 核心创新

1. 双路独立编码架构Dual-BEATs
2. 静态不相关抖动噪声注入绕过归一化瓶颈
3. 零样本泛化到未见空间配置
4. 在细微0.5声像幅度上达97.2%定位准确率

## 🏗️ 模型架构

输入为左右声道立体声信号，分别送入两个相同的BEATs语义编码器（预训练音频表示模型）。编码前对每个声道注入静态、不相关的抖动噪声（dithering noise），该噪声建立宏方差下限，使空间几何信息在归一化层中得以保留。编码器输出特征融合后送入LLM进行空间分类。

## 📚 数据集

- 自建三元方向分类数据集（左/中/右，含0.5声像幅度）
- 未见空间配置测试集（零样本泛化评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 定位准确率 | 三元方向分类（0.5声像幅度） | 无抖动基线（未报告具体值） | **97.2%** | 显著提升 |

抖动模型在细微0.5声像幅度上达到97.2%定位准确率，并零样本泛化到未见空间配置。消融实验验证了抖动噪声的必要性，无抖动时模型退化为随机猜测。

## 🎯 结论与影响

本文证明通过简单的抖动正则化，标准多模态模型即可实现零样本立体声理解，无需复杂空间模块。该发现为音频LLM的空间感知能力提供了低成本方案，有望推动沉浸式语音交互应用。

## ⚠️ 局限与未解决问题

仅评估了三元方向分类任务，未涉及连续方位角估计或多源场景。抖动噪声的幅度和统计特性未深入优化。未与基于房间模拟的方法进行直接比较。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
