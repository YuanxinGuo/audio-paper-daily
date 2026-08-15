---
title: "ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频到音频生成"]
summary: "ControlFoley提出统一视频到音频生成框架，通过联合视觉编码、时频解耦和模态鲁棒训练，实现文本、视频和参考音频的精细控制，并引入VGGSound-TVC基准评估视觉-文本冲突下的可控性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频到音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可控生成</span> <span class="tag-pill tag-pill-soft">#多模态对齐</span> <span class="tag-pill tag-pill-soft">#音视频同步</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.15086</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/xiaomi-research/controlfoley" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">xiaomi-research/controlfoley</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.15086" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.15086" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/xiaomi-research/controlfoley" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ControlFoley提出统一视频到音频生成框架，通过联合视觉编码、时频解耦和模态鲁棒训练，实现文本、视频和参考音频的精细控制，并引入VGGSound-TVC基准评估视觉-文本冲突下的可控性。
</div>

## 👥 作者与机构

**Jianxuan Yang** ¹ · Xinyue Guo · Zhi Cheng · Kai Wang · Lipan Zhang · Jinjie Hu · Qiang Ji · Yihua Cao · … 等 5 人

**机构**：小米

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合视频到音频生成、多模态学习研究者阅读。建议重点阅读第3节方法部分（联合视觉编码、时频解耦、模态鲁棒训练）和第4节实验（VGGSound-TVC基准及对比结果）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

视频到音频生成旨在从视觉内容合成对应音频，但现有方法在视觉-文本冲突下文本可控性弱，且参考音频的风格控制因时间与音色信息纠缠而不精确。此外，缺乏标准化基准阻碍系统评估。ControlFoley旨在解决这些问题，提出统一框架实现视频、文本、参考音频的精细控制。

## 💡 核心创新

1. 联合视觉编码：CLIP与时空音视频编码器结合，提升对齐和文本可控性
2. 时频解耦：抑制冗余时间线索，保留判别性音色特征
3. 模态鲁棒训练：统一多模态表示对齐（REPA）和随机模态丢弃
4. 新基准VGGSound-TVC：评估视觉-文本冲突下的文本可控性

## 🏗️ 模型架构

ControlFoley采用多模态编码器：视频经CLIP和时空音视频编码器联合编码，文本经文本编码器，参考音频经时频解耦模块提取音色特征。各模态特征通过统一表示对齐（REPA）和随机模态丢弃进行融合，输入到生成主干（如扩散或自回归模型）合成音频。输出为对应视频的音频波形。

## 📚 数据集

- VGGSound（训练/评估，大规模视频-音频数据集）
- VGGSound-TVC（评估，新构建的文本可控性基准，含视觉-文本冲突）

## 📊 实验结果

摘要未提供具体数值指标，但声称在多个V2A任务（文本引导、文本控制、音频控制）上达到SOTA，在跨模态冲突下可控性优越，同时保持强同步和音频质量，并优于工业级V2A系统。

## 🎯 结论与影响

ControlFoley通过联合视觉编码、时频解耦和模态鲁棒训练，显著提升了视频到音频生成的可控性，尤其在视觉-文本冲突场景下。其提出的VGGSound-TVC基准为后续研究提供了标准化评估工具。该工作对多媒体内容创作、影视后期等工业应用具有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：基准仅基于VGGSound，多样性有限；未报告推理效率；对比基线可能不全面；时频解耦的有效性需更多消融实验验证。

## 🔗 开源资源

- **代码**：<https://github.com/xiaomi-research/controlfoley>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
