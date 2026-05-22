---
title: "Modulation Feature Enhancement with a Multi-Stage Attention Network for Underwater Acoustic Target Recognition"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#水下声学目标识别"]
summary: "提出基于VMD和3/2-D谱的调制特征增强方法，结合多阶段注意力网络和类别平衡损失，提升水下目标识别性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#水下声学目标识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#特征提取</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#类不平衡</span> <span class="tag-pill tag-pill-soft">#深度学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.16304</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.16304" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.16304" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于VMD和3/2-D谱的调制特征增强方法，结合多阶段注意力网络和类别平衡损失，提升水下目标识别性能。
</div>

## 👥 作者与机构

**Jiaping Yu** ¹ · Shefeng Yan · Linlin Mao · Zeping Sui · Chunjin Jiang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合水下声学、信号处理领域研究者。可重点阅读§3特征提取与§4注意力机制设计，以及§5.3的消融实验。若关注类不平衡问题，可看§4.3的损失函数。

## 🌍 研究背景

水下声学目标识别在海洋应用中至关重要，但舰船辐射噪声复杂多变，传统方法难以提取鲁棒特征。现有深度学习模型常忽略调制包络信息，且真实数据存在严重类别不平衡。本文旨在通过改进特征表示和注意力机制，并设计针对不平衡的损失函数，提升识别性能。

## 💡 核心创新

1. 基于VMD和3/2-D谱的DEMON谱特征提取与融合
2. 多阶段多类型注意力机制（MMATT）
3. 残差通道独立谱注意力（R-CISAM）
4. 多尺度分离融合谱注意力（MS-SFSAM）
5. 可调节类别平衡焦点损失（ACBFL）

## 🏗️ 模型架构

输入为舰船辐射噪声信号，首先通过VMD分解和3/2-D谱生成高保真2-D DEMON谱特征。然后送入1-D CNN主干网络，其中嵌入多阶段多类型注意力机制（MMATT），包含R-CISAM和MS-SFSAM模块，在不同网络深度自适应细化特征。最后通过全连接层输出分类结果。

## 📚 数据集

- 真实舰船辐射噪声数据集（训练与评估，未说明规模）

## 📊 实验结果

摘要未提供具体数值结果，仅说明在真实数据集上有效提升了水下目标识别性能。需查阅全文获取详细指标。

## 🎯 结论与影响

本文提出的调制特征增强与多阶段注意力网络有效提升了水下目标识别准确率，尤其在类不平衡场景下。该工作为水下声学特征工程和注意力机制设计提供了新思路，有望推动实际海洋监测系统的智能化。

## ⚠️ 局限与未解决问题

摘要未报告模型参数量、推理延迟等效率指标；仅在单一真实数据集上验证，缺乏跨数据集泛化实验；未与最新水下识别方法（如基于Transformer的模型）对比；注意力机制的计算开销未分析。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
