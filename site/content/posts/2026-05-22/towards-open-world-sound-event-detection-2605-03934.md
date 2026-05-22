---
title: "Towards Open World Sound Event Detection"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声音事件检测"]
summary: "提出开放世界声音事件检测范式OW-SED，设计WOOT框架，利用可变形注意力与特征解耦实现已知事件检测、未知事件识别与增量学习。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声音事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#开放世界学习</span> <span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#特征解耦</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.03934</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.03934" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.03934" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出开放世界声音事件检测范式OW-SED，设计WOOT框架，利用可变形注意力与特征解耦实现已知事件检测、未知事件识别与增量学习。
</div>

## 👥 作者与机构

**P. H. Hai** ¹ · L. T. Minh · L. H. Son

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合SED与开放世界学习研究者。建议重点阅读§3的WOOT架构设计与§4的实验对比。可先看表1与图3了解性能提升。

## 🌍 研究背景

传统SED系统在封闭世界假设下工作，无法处理真实环境中不断出现的新声音事件。受计算机视觉开放世界学习启发，本文首次将开放世界范式引入SED，需同时检测已知事件、识别未知事件并增量学习。现有方法难以处理重叠和模糊事件，本文提出可变形注意力与特征解耦来解决。

## 💡 核心创新

1. 提出OW-SED范式，定义开放世界声音事件检测任务
2. 设计1D可变形注意力架构，自适应聚焦显著时域区域
3. 引入特征解耦分离类特定与类无关表示
4. 提出一对多匹配策略与多样性损失增强表示多样性

## 🏗️ 模型架构

输入音频特征 → 1D可变形编码器（可变形注意力自适应聚焦时域区域）→ 特征解耦模块（分离类特定与类无关表示）→ 一对多匹配解码器（结合多样性损失）→ 输出事件类别与边界。整体为WOOT（Open-World Deformable Sound Event Detection Transformer）框架。

## 📚 数据集

- DCASE 2023 Task 4（训练/评估，含合成与真实数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PSDS | DCASE 2023 Task 4 | Baseline (CRNN) 0.43 | **0.48** | +0.05 |

在DCASE 2023 Task 4上，WOOT在封闭世界设置下PSDS达0.48，优于基线CRNN的0.43；在开放世界场景下，未知事件检测F1显著优于现有基线。消融实验验证了可变形注意力与特征解耦的有效性。

## 🎯 结论与影响

本文首次将开放世界学习引入SED，提出WOOT框架，在封闭与开放场景均取得领先性能。该工作为SED领域开辟了新方向，有望推动智能监控、智慧城市等应用中的自适应音频感知系统发展。

## ⚠️ 局限与未解决问题

实验仅在DCASE 2023 Task 4数据集上进行，泛化性待验证；未报告推理延迟与模型参数量；开放世界增量学习部分仅初步验证，长期增量场景下的灾难性遗忘问题未深入探讨。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
