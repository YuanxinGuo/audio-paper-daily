---
title: "Does per-frame early exit pay? A compute-matched study of dynamic depth for on-device speech enhancement"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "研究逐帧早退在端侧语音增强中是否划算，用监督所有中间深度并微调输出头的方式，得到比同算力静态模型更优的Pareto前沿。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#动态网络</span> <span class="tag-pill tag-pill-soft">#模型量化</span> <span class="tag-pill tag-pill-soft">#边缘推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29867</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29867" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29867" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究逐帧早退在端侧语音增强中是否划算，用监督所有中间深度并微调输出头的方式，得到比同算力静态模型更优的Pareto前沿。
</div>

## 👥 作者与机构

Cl\'ement Laroche · Riccardo Miccini

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做端侧语音增强、动态网络与量化部署的研究者与工程同学阅读。建议重点看训练协议（监督所有中间深度+输出头微调）与STM32N6上的延迟-质量前沿实验，表与图比正文更值得细读；若只关心算法精度可略读硬件部分。

## 🌍 研究背景

端侧语音增强（助听器、耳机）多依赖静态int8图加速，深度可变网络需拆成多张图并由策略调度，带来额外开销。此前动态深度/早退方法多关注云端或GPU场景，缺少在真实MCU上算力对齐的评估，也未回答逐帧早退是否真能换来更好的质量-算力折中。本文在算力对齐条件下系统研究该问题。

## 💡 核心创新

1. 监督一个因果模型的每个中间深度
2. 微调输出头保证深层不劣于浅层
3. 导出比同尺寸从头训练更Pareto高效的静态模型族
4. 在STM32N6上测int8延迟-质量前沿

## 🏗️ 模型架构

输入为因果语音增强模型的帧级特征，主干为单一因果网络，在每个中间深度都接输出头并施加监督，再微调各输出头使深层输出不差于浅层。由此可导出多个静态子模型，按策略逐帧选择深度。模型量化为int8部署于STM32N6 NPU，策略运行在Cortex-M55上。摘要未给出具体参数量与主干网络名。

## 📚 数据集

- VoiceBank-DEMAND（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 同算力从头训练的静态模型 | **同算力下高0.11** | +0.11 |
| PESQ | VoiceBank-DEMAND | 最佳PESQ所需算力 | **少30%算力达到同等最佳PESQ** | -30% 算力 |

摘要给出两项关键数字：同等算力下PESQ最高提升0.11，达到最佳PESQ只需约70%算力。硬件侧，策略在Cortex-M55上每帧仅26微秒，将增强器拆成多张NPU图仅增加2.2%延迟；在VoiceBank-DEMAND上动态增强器与静态模型处于同一延迟-质量前沿。摘要未报告SI-SDR、参数量或消融细节。

## 🎯 结论与影响

最强结论是：在算力对齐下，逐帧早退的动态执行几乎不付出额外代价，且能导出更优的静态模型族。这为端侧语音增强的动态深度部署提供了可复现的工程范式，后续研究可在此基础上探索更复杂策略与更多硬件后端。

## ⚠️ 局限与未解决问题

仅在一个因果模型与VoiceBank-DEMAND上验证，缺少多数据集与多主干泛化；未报告SI-SDR等常用指标与参数量；策略开销虽小但未与更强静态基线全面对比；输出头微调带来的训练成本未量化。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
