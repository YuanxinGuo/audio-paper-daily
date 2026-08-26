---
title: "Pre-Decoding Acoustic Triage for Budgeted Vision-Language Captioning of Untrimmed Egocentric Video"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频字幕生成"]
summary: "提出音频优先的预解码分流策略，在不解码视频帧的情况下选择关键窗口，减少VLM调用成本，提升动作覆盖。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频字幕生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频优先</span> <span class="tag-pill tag-pill-soft">#预算受限</span> <span class="tag-pill tag-pill-soft">#视觉语言模型</span> <span class="tag-pill tag-pill-soft">#动作覆盖</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.22359</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/masjalayer/PreDecoding-AcousticTriage" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">masjalayer/PreDecoding-AcousticTriage</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.22359" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.22359" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/masjalayer/PreDecoding-AcousticTriage" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出音频优先的预解码分流策略，在不解码视频帧的情况下选择关键窗口，减少VLM调用成本，提升动作覆盖。
</div>

## 👥 作者与机构

**Masoud Jalayer** ¹ · Changyi Li · Yu Xiao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事视频理解、多模态高效推理的研究者。重点阅读方法部分（§3）和实验对比（§4），可先看表2和表3。若关注效率，可参考其代码实现。

## 🌍 研究背景

长时程自我中心视频分析在物流、建筑等领域需求增长，但现有VLM处理固定窗口成本高。先前分流策略或均匀采样或依赖视觉特征，后者需解码视频，违背预算初衷。本文提出音频优先分流，利用轻量级音频特征在解码前选择窗口，旨在降低计算成本同时保持动作覆盖。

## 💡 核心创新

1. 音频优先分流：在视频解码前使用音频特征选择窗口
2. 目标为每动作触发一次，而非逐帧检测
3. 使用冻结的AudioSet预训练特征，无需领域特定标签
4. 与token压缩或量化自然兼容
5. 在多个数据集上验证有效性

## 🏗️ 模型架构

输入为未修剪视频的音频流，提取AudioSet预训练特征（冻结），送入轻量级选择器（可能是MLP或RNN），输出每个窗口的触发概率，根据预算选择触发窗口。触发窗口再输入VLM生成字幕。选择器训练目标为每动作触发一次，使用对比或分类损失。

## 📚 数据集

- EPIC-KITCHENS-100 (EK-100)（评估）
- Ego4D（评估，247个片段）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 动作覆盖提升 | EK-100 | 均匀采样等 | **4.0-10.8个百分点** | +4.0~10.8% |
| VLM调用减少 | EK-100 | 均匀采样 | **9-20%** | -9~20% |

在EK-100上，音频优先分流在匹配覆盖度下减少9-20%的VLM调用；在Ego4D上，优于均匀采样和两个视觉关键帧选择器。动作覆盖提升4.0-10.8个百分点，且使用少于一半的调用。

## 🎯 结论与影响

音频优先分流有效降低VLM调用成本，同时保持动作覆盖，为长视频理解提供高效方案。该方法可与其他压缩技术结合，对工业应用有实际意义。

## ⚠️ 局限与未解决问题

未报告推理延迟或计算开销细节；依赖AudioSet预训练特征，可能对域外音频泛化有限；未与更多先进视觉分流方法对比；未提供消融实验验证各组件贡献。

## 🔗 开源资源

- **代码**：<https://github.com/masjalayer/PreDecoding-AcousticTriage>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
