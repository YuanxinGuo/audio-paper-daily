---
title: "MeMo: Attentional Momentum for Real-time Audio-visual Speaker Extraction under Impaired Visual Conditions"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出MeMo框架，通过两个自适应记忆库在视觉线索缺失时维持注意力动量，实现鲁棒的实时视听目标说话人提取。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#视听融合</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#实时处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2507.15294</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2507.15294" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2507.15294" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MeMo框架，通过两个自适应记忆库在视觉线索缺失时维持注意力动量，实现鲁棒的实时视听目标说话人提取。
</div>

## 👥 作者与机构

**Junjie Li** ¹ · Wenxuan Wu · Shuai Wang · Zexu Pan · Kong Aik Lee · Helen Meng · Haizhou Li

**机构**：香港中文大学 · 新加坡国立大学 · 香港理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事视听语音分离、目标说话人提取的研究者。建议重点阅读§3的MeMo架构和§4.2的视觉退化实验。可先看图2和表1了解整体性能。

## 🌍 研究背景

视听目标说话人提取（AV-TSE）利用视觉线索（如唇部运动）从多说话人混合中提取目标语音。现有方法严重依赖视觉质量，当视觉线索缺失或严重退化时性能急剧下降。人类能在无辅助信息时维持对目标说话人的注意力，受此启发，本文旨在设计一种能在视觉退化条件下保持鲁棒性的实时AV-TSE系统。

## 💡 核心创新

1. 提出注意力动量机制，通过记忆库维持注意力状态
2. 设计两个自适应记忆库：视觉记忆库和注意力记忆库
3. 支持实时处理，无需未来帧信息
4. 在视觉完全缺失时仍能保持至少2 dB SI-SNR提升

## 🏗️ 模型架构

输入为多通道音频和视频帧。音频经Conformer编码，视频经3D CNN提取视觉特征。核心模块为两个自适应记忆库：视觉记忆库存储历史视觉特征，注意力记忆库存储历史注意力权重。通过门控机制融合当前视觉特征与记忆库信息，生成注意力掩码，再与音频特征相乘得到目标语音。输出为时域波形。

## 📚 数据集

- VoxCeleb2（训练，包含多说话人视频）
- LRS3（评估，用于视听语音分离）
- 模拟混合数据集（训练/评估，多说话人混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SNR (dB) | 模拟混合测试集（视觉正常） | AV-ConvTasNet 12.5 | **14.8** | +2.3 dB |
| SI-SNR (dB) | 模拟混合测试集（视觉缺失） | AV-ConvTasNet 8.1 | **10.5** | +2.4 dB |

在视觉正常和缺失条件下，MeMo均显著优于基线AV-ConvTasNet，SI-SNR提升超过2 dB。消融实验验证了记忆库的有效性，且模型参数量仅增加约10%，满足实时要求。

## 🎯 结论与影响

MeMo通过注意力动量机制有效解决了视觉退化下的AV-TSE问题，在视觉完全缺失时仍保持鲁棒性。该工作为视听融合中的鲁棒注意力建模提供了新思路，对工业级实时语音分离系统具有实用价值。

## ⚠️ 局限与未解决问题

实验仅在模拟混合数据上进行，未在真实嘈杂环境中验证；未报告推理延迟的具体数值；记忆库的更新策略可能对长序列存在遗忘问题。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
