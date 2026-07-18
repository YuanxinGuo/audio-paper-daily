---
title: "MIDI-RAE-JEPA: Hierarchical Representation Learning and Generation for Symbolic Music"
date: 2026-07-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐表示学习"]
summary: "提出MIDI-RAE-JEPA，结合等变性和JEPA框架学习符号音乐的层次化表示，用于生成和理解。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#层次表示</span> <span class="tag-pill tag-pill-soft">#音乐生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14537</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14537" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14537" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MIDI-RAE-JEPA，结合等变性和JEPA框架学习符号音乐的层次化表示，用于生成和理解。
</div>

## 👥 作者与机构

**Scott H. Hawley** ¹

**机构**：贝尔蒙特大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和自监督学习研究者。重点看§3的等变目标设计和§4的生成实验。可先读图2架构概览。

## 🌍 研究背景

符号音乐理解需要丰富的内部表示，但自监督方法在符号音乐领域探索不足，尤其缺乏对层次化多尺度结构的编码。现有方法如Haar散射变换表示能力有限。本文旨在通过等变性和JEPA框架学习具有层次结构的表示，并验证其在生成和下游任务中的有效性。

## 💡 核心创新

1. 提出音高-时间平移等变目标，鼓励模型学习时间关系
2. 结合LeJEPA与Swin Transformer V2编码器，实现层次化表示
3. 使用SIGReg防止表示坍塌，无需负样本
4. 基于流匹配的生成模型，条件于学习到的表示
5. 在情感分类任务上超越Haar散射变换基线

## 🏗️ 模型架构

输入为钢琴卷帘图像（时间×音高）。主干为Swin Transformer V2编码器，结合LeJEPA框架。训练目标包括掩码嵌入预测（MEP）和音高-时间平移等变损失。表示通过SIGReg正则化防止坍塌。解码器（独立训练）从冻结编码器嵌入重建输入，F1达0.995。生成模型使用流匹配，条件于编码器嵌入。

## 📚 数据集

- MAESTRO（训练/评估，约1200首钢琴曲）
- Emotion分类数据集（下游评估，未指定名称）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Reconstruction F1 | MAESTRO | N/A | **0.995** | N/A |
| Emotion Classification Accuracy | 未命名数据集 | Haar散射变换（未给出具体值） | **优于基线** | 未量化 |

重建F1达0.995，表明表示保留足够信息。生成实验显示，条件匹配时输出在音高注册和节奏密度上接近条件片段，不匹配时仍产生音乐上合理的输出。嵌入距离随平移幅度单调增加，验证了等变性。情感分类任务上优于Haar散射变换基线。

## 🎯 结论与影响

本文证明基于等变性的自监督目标结合足够细粒度的编码器能学到语义丰富、可用于生成的符号音乐表示。对音乐理解与生成子方向有启发，可能推动音乐AI辅助创作工具的发展。

## ⚠️ 局限与未解决问题

仅在钢琴音乐上评估，未测试多乐器或复杂编曲。生成质量仅定性分析，缺乏客观指标（如FAD）。未与对比学习方法（如SimCLR）比较。未报告推理速度或模型参数量。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-18/">← 返回 2026-07-18 速递</a></div>
