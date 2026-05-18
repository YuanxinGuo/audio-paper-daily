---
title: "Global Rotation Equivariant Phase Modeling for Speech Enhancement with Deep Magnitude-Phase Interaction"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出全局旋转等变相位建模的幅度-相位双流框架，通过保持相位流旋转等变性提升语音增强性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#相位建模</span> <span class="tag-pill tag-pill-soft">#旋转等变</span> <span class="tag-pill tag-pill-soft">#幅度-相位交互</span> <span class="tag-pill tag-pill-soft">#双流网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.08556</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/wangchengzhong/GRE-Net" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">wangchengzhong/GRE-Net</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.08556" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.08556" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/wangchengzhong/GRE-Net" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出全局旋转等变相位建模的幅度-相位双流框架，通过保持相位流旋转等变性提升语音增强性能。
</div>

## 👥 作者与机构

**Chengzhong Wang** ¹ · Andong Li · Dingding Yao · Junfeng Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强研究者，重点关注§3的GRE特性、MPICM和HADF模块设计，以及§4的相位检索实验。建议通读，先看§3.2与表1。

## 🌍 研究背景

深度学习在语音增强中取得显著进展，但相位建模仍是挑战。传统网络在欧氏空间操作，难以建模相位的圆环拓扑。现有方法多忽略相位几何特性，导致相位估计不准确。本文旨在通过引入全局旋转等变性，使相位流对齐其内在圆环几何，从而提升相位建模能力。

## 💡 核心创新

1. 提出全局旋转等变(GRE)特性用于相位流
2. 设计幅度-相位交互卷积模块(MPICM)
3. 提出混合注意力双前馈网络(HADF)瓶颈
4. 在相位检索任务中降低相位距离超20%

## 🏗️ 模型架构

输入为带噪语音的幅度和相位谱，分别送入幅度流和相位流。相位流通过GRE约束的卷积模块保持旋转等变性，MPICM实现幅度-相位信息交换，HADF瓶颈进行统一特征融合。输出为增强后的幅度和相位谱。模型参数量未提及。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和混响）
- LibriTTS（训练/评估，干净语音）
- WSJ0（评估，用于零样本跨语料库测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Phase Distance | 相位检索任务 | 基线方法（未明确） | **降低超20%** | -20% |
| PESQ | 零样本跨语料库去噪 | 基线方法（未明确） | **提升超0.1** | +0.1 |

在相位检索任务中，所提方法将相位距离降低超过20%。在零样本跨语料库去噪评估中，PESQ提升超过0.1。在包含混合失真的通用SE任务中也表现出优越性。定性分析显示学习到的相位特征呈现周期性模式，与相位圆环性质一致。

## 🎯 结论与影响

本文通过全局旋转等变相位建模，有效提升了语音增强中的相位估计质量。该工作为相位建模提供了新视角，有望推动基于几何先验的语音增强方法发展。对工业落地，可改善助听器、通信等场景的语音质量。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；消融实验不够充分，未单独分析MPICM和HADF的贡献；仅在特定数据集上评估，泛化性需进一步验证。

## 🔗 开源资源

- **代码**：<https://github.com/wangchengzhong/GRE-Net>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
