---
title: "Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video Generation"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视频生成"]
summary: "提出Unison统一框架，通过语义引导的音频解耦和双向跨模态强制策略，实现人体中心视频中运动、语音和音效的协同生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态生成</span> <span class="tag-pill tag-pill-soft">#语音-运动同步</span> <span class="tag-pill tag-pill-soft">#音频-视频对齐</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.08729</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.08729" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.08729" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Unison统一框架，通过语义引导的音频解耦和双向跨模态强制策略，实现人体中心视频中运动、语音和音效的协同生成。
</div>

## 👥 作者与机构

**Shihao Cheng** ¹ · **Jiaxu Zhang** ¹ · Quanyue Song · Shansong Liu · Zhizhi Guo · Xiaolei Zhang · Chi Zhang · Xuelong Li · … 等 1 人

**机构**：武汉大学 · 上海人工智能实验室 · 西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态生成、音频-视频对齐方向的研究者。建议重点阅读§3.2语义引导的音频解耦策略和§3.3双向跨模态强制策略，以及表2的定量对比。可先看§1引言了解问题动机。

## 🌍 研究背景

人体中心视频生成需同时协调运动、语音和音效，但三者时间特性异质，现有模型常出现模态间错位。例如语音与口型不同步、音效与动作不匹配。已有工作多聚焦于单一模态或两两对齐，缺乏统一框架。本文旨在解决多模态联合生成中的一致性问题。

## 💡 核心创新

1. 语义引导的音频解耦策略，分离语音和音效生成
2. 双向音频交叉注意力与语义条件门控实现自适应重组
3. 双向跨模态强制策略，用干净模态引导噪声模态
4. 渐进稳定策略增强去噪过程鲁棒性

## 🏗️ 模型架构

Unison基于扩散模型，输入为文本描述或视频条件。音频流采用语义引导解耦：先分别生成语音和音效潜变量，再通过双向音频交叉注意力（Bidirectional Audio Cross-Attention）和语义条件门控（Semantic-Conditioned Gating）进行自适应重组。运动-音频同步采用双向跨模态强制策略，在去噪过程中交替用运动特征引导音频生成和用音频特征引导运动生成，并辅以渐进稳定策略。输出为同步的视频（含运动）和音频（含语音和音效）。

## 📚 数据集

- HDTF（训练/评估，人脸视频数据集）
- VoxCeleb2（训练/评估，多说话人视频）
- AIST++（训练/评估，舞蹈视频含运动）
- YouTube随机视频（评估，泛化性测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | HDTF | VideoPoet 12.3 | **9.8** | -2.5 |
| FVD | HDTF | VideoPoet 85.6 | **72.1** | -13.5 |
| MOS（音频质量） | HDTF | VideoPoet 3.42 | **4.15** | +0.73 |
| Sync（唇同步） | HDTF | VideoPoet 0.78 | **0.89** | +0.11 |

在HDTF和VoxCeleb2上，Unison在FID、FVD、音频MOS和唇同步指标上均超越VideoPoet等基线。消融实验验证了语义解耦和双向强制策略的有效性。跨数据集泛化测试显示在未见过的YouTube视频上仍保持良好同步。

## 🎯 结论与影响

Unison通过显式多模态协调策略，在人体中心视频生成中实现了运动、语音和音效的强一致性，显著提升了生成视频的感知质量和同步精度。该工作为多模态联合生成提供了新范式，有望推动虚拟人、影视制作等应用发展。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理速度；缺乏对复杂场景（多人、背景噪声）的评估；音频解耦依赖预训练语义标签，可能引入误差；仅评估了英文语音，多语言泛化未知。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
