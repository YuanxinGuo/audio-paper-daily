---
title: "ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "ToolDF利用音频大语言模型作为编排器，通过工具集成推理实现混合真实性音频深度伪造检测，并引入新基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#源分离</span> <span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#混合真实性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.03620</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.03620" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.03620" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ToolDF利用音频大语言模型作为编排器，通过工具集成推理实现混合真实性音频深度伪造检测，并引入新基准。
</div>

## 👥 作者与机构

**Taewoo Kim** ¹ · Young Han Lee · Nam In Park · Chanwoo Kim

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频取证、深度伪造检测及多模态大模型研究者。建议重点阅读方法部分（§3）和实验部分（§4），特别是工具集成推理的设计和混合真实性基准的构建。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

音频深度伪造检测通常被视为单域音频的片段级二分类任务。然而，真实世界的篡改音频可能呈现混合真实性，即真实与伪造线索在时间转换、重叠源或两者中并存。现有方法难以处理此类复杂场景，且缺乏可解释性。ToolDF旨在通过工具集成推理框架，结合音频大语言模型，实现混合真实性音频的检测与证据定位。

## 💡 核心创新

1. 提出工具集成推理框架，利用音频大语言模型编排分析流程
2. 引入混合真实性音频深度伪造检测基准，涵盖时间转换、声学重叠和混合场景
3. 通过监督工具使用轨迹训练，实现自适应场景分析和专家路由
4. 提供可解释的判决，定位到时间区域和声学源
5. 在复合型检测上显著优于强基线和固定流水线

## 🏗️ 模型架构

ToolDF采用音频大语言模型作为编排器，输入音频场景，通过监督工具使用轨迹训练。编排器自适应分析场景，选择性执行源分离，将分离的组件路由到领域专家（如语音增强、伪造检测专家），并聚合证据生成可解释的判决。输出包括检测结果和定位到时间区域及声学源的证据。

## 📚 数据集

- 混合真实性ADD基准（评估，包含时间转换、声学重叠和混合场景）
- 公开音频深度伪造数据集（训练，具体名称未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-F1 | 混合真实性ADD基准 | 最强单体基线（未提及具体值） | **未提及具体值** | +3.72 |
| macro-F1 | 混合真实性ADD基准 | 固定流水线（未提及具体值） | **未提及具体值** | +14.39 |

实验表明，ToolDF在复合型检测上取得最佳整体性能，macro-F1较最强单体基线和固定流水线分别提升3.72和14.39点。同时，模型提供可解释的证据，定位到时间区域和声学源。但摘要未提供具体数值，仅给出提升量。

## 🎯 结论与影响

ToolDF通过工具集成推理，有效解决了混合真实性音频深度伪造检测问题，显著优于现有方法，并提供可解释的判决。该框架为音频取证领域提供了新思路，有望推动更复杂场景下的伪造检测研究。对工业应用而言，可提升检测系统的鲁棒性和可解释性。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题包括：依赖音频大语言模型的推理能力，计算开销较大；混合真实性基准的构建可能引入偏差；未与更多最新方法对比；未报告推理延迟等效率指标。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
