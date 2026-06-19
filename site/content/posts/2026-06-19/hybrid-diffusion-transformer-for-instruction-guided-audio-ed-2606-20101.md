---
title: "Hybrid Diffusion Transformer for Instruction-Guided Audio Editing via Rectified Flow"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频编辑"]
summary: "提出混合扩散Transformer架构，通过粗到精的两阶段策略实现高效指令引导音频编辑。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#指令引导</span> <span class="tag-pill tag-pill-soft">#音频编辑</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.20101</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.20101" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.20101" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出混合扩散Transformer架构，通过粗到精的两阶段策略实现高效指令引导音频编辑。
</div>

## 👥 作者与机构

**Liting Gao** ¹ · Yonggang Zhu · Yaru Chen · Dongyu Wang · Shubin Zhang · Zhenbo Li · Jean-Yves Guillemaut · Wenwu Wang

**机构**：中国农业大学 · 萨里大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频编辑和扩散模型研究者。建议重点阅读第3节架构设计和第4节实验部分，特别是表1和表2的结果。可先看§3.2的粗对齐阶段和§3.3的精修阶段。

## 🌍 研究背景

音频编辑任务旨在根据自然语言指令修改音频片段中的特定内容，同时保留其余部分。现有基于扩散模型的方法多采用卷积U-Net骨干，其局部归纳偏置和交叉注意力机制难以实现长程语义对齐和精确指令理解。扩散Transformer虽具备更强的全局建模和多模态融合能力，但现有架构简单堆叠MMDiT和DiT块，对所有token进行联合注意力导致二次复杂度。本文旨在平衡编辑性能与效率。

## 💡 核心创新

1. 提出混合两阶段扩散Transformer架构
2. 粗对齐阶段使用联合注意力建立语义对齐
3. 精修阶段交替使用联合注意力和交叉注意力
4. 基于整流流匹配实现高效训练
5. 在重叠音频事件和复杂指令任务上取得显著提升

## 🏗️ 模型架构

输入为音频潜变量和文本指令token。采用两阶段扩散Transformer：低分辨率阶段使用联合注意力（joint attention）对音频和文本token进行粗粒度语义对齐；高分辨率阶段交替使用联合注意力和交叉注意力（cross-attention）块细化编辑细节。整体基于整流流匹配（rectified flow matching）训练。模型参数量紧凑，具体未给出。

## 📚 数据集

- AudioCaps（训练/评估）
- Clotho（训练/评估）
- ESC-50（评估，用于零样本泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | AudioCaps | AUDIT 2.0 | **1.2** | -0.8 |
| CLAP Score | AudioCaps | AUDIT 0.35 | **0.42** | +0.07 |
| FAD | Clotho | AUDIT 2.5 | **1.8** | -0.7 |
| CLAP Score | Clotho | AUDIT 0.30 | **0.38** | +0.08 |

在AudioCaps和Clotho数据集上，所提方法在FAD和CLAP Score上均优于AUDIT基线，尤其在重叠音频事件和复杂指令任务上提升明显。模型参数量更小，推理速度更快。消融实验验证了两阶段设计和交替注意力机制的有效性。

## 🎯 结论与影响

本文提出的混合扩散Transformer架构通过粗到精的两阶段策略有效平衡了音频编辑的性能和效率，在多个基准上取得最优结果。该工作为指令引导音频编辑提供了新的设计范式，有望推动相关应用落地。

## ⚠️ 局限与未解决问题

未报告在更复杂场景（如多源混合）下的性能；缺乏与更多基线（如基于U-Net的方法）的对比；未提供推理延迟的具体数值；数据集规模有限，泛化性有待验证。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
