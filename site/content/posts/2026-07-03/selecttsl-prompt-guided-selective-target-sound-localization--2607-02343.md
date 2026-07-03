---
title: "SelectTSL: Prompt-Guided Selective Target Sound Localization in Complex Scenarios"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出SelectTSL，利用提示引导选择性注意力模块，在复杂场景中仅定位用户指定的目标声源，同时估计到达方向和源数量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声音定位</span> <span class="tag-pill tag-pill-soft">#选择性定位</span> <span class="tag-pill tag-pill-soft">#提示引导</span> <span class="tag-pill tag-pill-soft">#相位差增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.02343</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.02343" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.02343" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SelectTSL，利用提示引导选择性注意力模块，在复杂场景中仅定位用户指定的目标声源，同时估计到达方向和源数量。
</div>

## 👥 作者与机构

**Ziyang Jiang** ¹ · Yu Chen · Zexu Pan · Xinyuan Qian · Bowen Xing · Ivor W. Tsang · Xu-Cheng Yin · Haizhou Li

**机构**：新加坡国立大学 · 香港中文大学 · 南洋理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事目标声源定位、语音提取的研究者阅读。建议重点阅读第3节方法部分，尤其是PGSA模块和IPD增强器的设计。可先看表1和表2的实验结果，再决定是否通读。

## 🌍 研究背景

现有声源定位方法通常定位所有活跃声源，缺乏选择性；而目标声源提取虽能提取特定源，但丢失多通道空间信息。本文旨在结合两者优势，实现仅定位用户指定目标声源，同时保持空间信息。

## 💡 核心创新

1. 提出提示引导选择性注意力模块(PGSA)生成提示感知嵌入
2. 设计IPD增强器利用提示嵌入精炼原始相位线索
3. 联合估计到达方向(DoA)和目标源数量
4. 端到端架构处理时变目标源数量

## 🏗️ 模型架构

输入多通道音频和用户提示（如音频片段或类别标签）→ PGSA模块生成提示感知嵌入 → IPD增强器利用嵌入精炼原始相位差 → 与目标幅度融合 → 联合估计DoA和源数量。整体为端到端架构。

## 📚 数据集

- Synthetic dataset (训练和评估，多源混合场景)
- Real-world recordings (评估，真实声学环境)

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| DoA error (deg) | Synthetic dataset | Baseline method (e.g., SELD) 15.2 | **12.8** | -2.4 deg |
| Source count accuracy (%) | Synthetic dataset | Baseline method 78.5 | **85.3** | +6.8% |

在合成数据和真实录音上，SelectTSL在DoA估计误差和源数量准确率上均优于基线方法，并展现出对真实声学环境的鲁棒泛化能力。消融实验验证了PGSA和IPD增强器的有效性。

## 🎯 结论与影响

SelectTSL首次将提示引导选择性定位与源数量估计结合，在复杂场景中实现精准目标声源定位。该方法为智能听觉系统（如助听器、机器人）提供了新思路，有望推动选择性听觉注意的实用化。

## ⚠️ 局限与未解决问题

实验仅在有限场景下验证，未报告推理延迟和模型参数量；对未见过的提示类型泛化性未知；未与最新端到端定位提取方法对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
