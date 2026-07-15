---
title: "Breaking the Quality--Intelligibility Trade-off in Streaming Target Speaker Extraction via Deep-Feature-Anchored Preference Optimization"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出WavLM锚定的直接偏好优化策略，打破流式目标说话人提取中质量与可懂度的权衡，在560ms块大小下实现WER从0.138降至0.123。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#偏好优化</span> <span class="tag-pill tag-pill-soft">#WavLM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.10191</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.10191" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.10191" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出WavLM锚定的直接偏好优化策略，打破流式目标说话人提取中质量与可懂度的权衡，在560ms块大小下实现WER从0.138降至0.123。
</div>

## 👥 作者与机构

**Shuhai Peng** ¹ · Jinjiang Liu · Hui Lu · Liyang Chen · Guiping Zhong · Jiakui Li · Shiyin Kang · Zhiyong Wu

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事流式语音分离/提取的研究者。建议重点阅读§3.2的DPO策略和§4的实验结果，尤其是表2中的WER对比。可先看图2的框架概览。

## 🌍 研究背景

流式目标说话人提取（TSE）在实时应用中至关重要，但生成式模型常面临质量与可懂度的权衡：优化感知音频质量会损害语音可懂度。先前工作多受限于流式架构约束，但本文揭示该权衡源于不恰当的优化锚点——直接优化音频质量指标导致奖励黑客，系统性地擦除发音关键内容。本文旨在通过改进架构和优化策略打破这一瓶颈。

## 💡 核心创新

1. 扩大Conformer卷积核以增强局部谱时建模
2. 提出WavLM锚定的直接偏好优化（DPO）微调策略
3. 利用WavLM余弦相似度排序偏好对，抵抗奖励黑客

## 🏗️ 模型架构

输入为混合语音和目标说话人线索（如预注册embedding）。主干为流式Conformer编码器，采用扩大卷积核（如31x31）增强局部谱时建模。解码器生成目标语音。关键创新在于微调阶段：使用WavLM提取深层声学特征，构建偏好对（高质量/低可懂度 vs 低质量/高可懂度），通过DPO优化模型参数，使优化锚点从易被黑客的音频指标转向鲁棒的声学特征。

## 📚 数据集

- LibriMix（训练/评估，含2/3说话人混合）
- WSJ0-2mix（评估，2说话人混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriMix test | 基线模型 0.138 | **0.123** | -10.9% |

在LibriMix测试集上，所提方法在560ms流式块大小下将WER从0.138降至0.123（相对改善10.9%），同时音频质量和说话人相似度略有提升。消融实验验证了扩大卷积核和DPO策略各自的有效性。未报告跨数据集泛化结果。

## 🎯 结论与影响

本文通过WavLM锚定的DPO策略有效打破了流式TSE中质量与可懂度的权衡，为生成式流式模型提供了新的优化范式。该工作表明，选择鲁棒的深层特征作为优化锚点比直接优化音频指标更有效，对实时语音通信系统有重要启示。

## ⚠️ 局限与未解决问题

实验仅在LibriMix和WSJ0-2mix上评估，缺乏真实噪声/混响场景验证；未报告模型参数量和推理延迟；DPO依赖WavLM特征，可能引入额外计算开销；未与近期流式TSE方法（如Mamba-based）对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
