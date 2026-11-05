---
title: "Which One Is Sounding? Binaural Sounding Instance Disambiguation for Audio-Visual Segmentation"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "用双耳声的耳间差提供声源方向约束，在同类别多候选场景中消歧出真正发声的实例，实现视听实例分割。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视听分割</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#实例分割</span> <span class="tag-pill tag-pill-soft">#空间音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.06074</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.06074" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.06074" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用双耳声的耳间差提供声源方向约束，在同类别多候选场景中消歧出真正发声的实例，实现视听实例分割。
</div>

## 👥 作者与机构

**Haoze Ma** ¹ · Yidi Li · Yu Ma · Pengyuan Zhao · Yi Shi · Bin Ren · Yanwen Guo · Dimitrios Kanoulas

**机构**：伦敦大学学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视听分割、双耳空间音频、机器人听觉感知的研究者。值得通读，重点看 §3 中双耳线索到图像平面空间响应图的投影方式，以及双级空间条件（特征级+解码器级）的设计；实验部分先看多候选子集上的 mIoU 表与消融。

## 🌍 研究背景

视听分割（AVS）此前主要预测与声音相关的区域或类别掩码，代表方法多基于单通道音频与视觉骨干的跨模态融合，在同类别多个候选实例共存时无法判断哪个在发声。近期的视听实例分割方法依赖运动线索与跨帧关联，在稀疏观测或运动不明显时不可靠。本文引入双耳音频，利用耳间时间差/强度差编码的声源方向信息，为同类别候选提供空间约束，从而消歧真正的发声实例。

## 💡 核心创新

1. 引入双耳耳间差作为声源方向空间约束，用于同类别候选消歧
2. 音频提示先定位类别一致的候选区域
3. 将双耳线索投影为图像平面空间响应图
4. 特征级与解码器级的双级空间条件精化发声实例掩码

## 🏗️ 模型架构

输入为双耳音频与视频帧。先用音频提示（audio prompting）在视觉特征上定位类别一致的候选区域；同时将双耳音频的耳间差线索投影为图像平面的空间响应图，编码声源方向。随后通过双级空间条件机制，在特征层与解码器层分别注入该空间响应，逐步把类别级候选响应精化为真实发声实例的掩码。输出为实例级分割掩码。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- AVS-Synthetic（双耳扩展版，评估，含多候选子集）
- Habitat-AVS（机器人室内感知，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 实例级 mIoU | AVS-Synthetic 多候选子集 | 现有 AVS/视听实例分割方法（摘要未给具体数值） | **本文方法** | +35.19 百分点 |
| 实例级 mIoU | Habitat-AVS 多候选子集 | 现有方法（摘要未给具体数值） | **本文方法** | +41.21 百分点 |

在两个基准的多候选子集上取得最佳性能，实例级 mIoU 分别提升 35.19 与 41.21 个百分点，并显著降低对同类别非发声区域的误激活。摘要未给出整体子集、单候选子集的绝对数值，也未报告推理延迟或参数量，消融细节需查阅正文。

## 🎯 结论与影响

最强结论是双耳空间线索能有效解决同类别多候选下的发声实例消歧，大幅提升实例级分割精度。这为视听分割引入空间音频信息提供了新思路，对机器人室内听觉感知与具身智能中的声源定位落地有潜在价值。

## ⚠️ 局限与未解决问题

依赖双耳录音，单通道或真实复杂混响下耳间差可靠性存疑；基准为合成双耳扩展与仿真 Habitat 数据，真实场景泛化未验证；摘要未给绝对指标、消融与推理开销，与运动类方法的对比细节不足。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
