---
title: "Frequency-Weighted Soft-Constrained Spatially Selective Active Noise Control for Open-Fitting Hearables"
date: 2026-10-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "将软约束空间选择性主动噪声控制推广到频率相关加权，用LTASS或oracle加权在低失真下同时提升可懂度与音质。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动噪声控制</span> <span class="tag-pill tag-pill-soft">#空间选择性</span> <span class="tag-pill tag-pill-soft">#助听器</span> <span class="tag-pill tag-pill-soft">#语音可懂度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.00721</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.00721" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.00721" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将软约束空间选择性主动噪声控制推广到频率相关加权，用LTASS或oracle加权在低失真下同时提升可懂度与音质。
</div>

## 👥 作者与机构

**Tong Xiao** ¹ · Reinhild Roden · Matthias Blau · Simon Doclo

**机构**：德国奥尔登堡大学 · 德国 Hearing Systems 研究组

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做助听器/开放式耳机ANC、空间选择性降噪与语音可懂度优化的研究者阅读。建议通读，重点看 §2 的频域加权软约束公式与 §4 中 LTASS/oracle 加权对比表；若只关心结论，可先看 LTASS 与 oracle 的失真-可懂度权衡图。

## 🌍 研究背景

开放式助听器的空间选择性ANC（SSANC）此前用单一标量权衡参数在所有频率上折中降噪与目标语音保留，无法按频带差异化处理。语音可懂度主要依赖中高频，而低频对音质与失真更敏感，标量加权难以兼顾。本文要解决的是：在保持低延迟时域主动控制的前提下，引入频率相关加权，使降噪-保语音的折中更符合感知。

## 💡 核心创新

1. 将标量软约束推广为频率相关加权，保持低延迟时域实现
2. 比较SII、MIRS、LTASS与oracle四种频域加权策略
3. LTASS加权无需干净目标语音即可接近oracle感知折中

## 🏗️ 模型架构

输入为多麦克风参考信号与误差麦克风信号，经低延迟时域自适应滤波（FxLMS类结构）产生控制信号驱动扬声器。目标语音保留误差按频率加权后与降噪误差联合构成软约束代价函数，权重由SII、MIRS、LTASS或oracle生成。输出为控制滤波器系数，实时更新。摘要未给出参数量与具体网络层数。

## 📚 数据集

- 实测声学冲激响应（多说话人场景，训练/评估）

## 📊 实验结果

摘要仅给出定性结论：LTASS与oracle加权带来最大可懂度提升，音质提升与SII/MIRS相当，但失真显著更低；oracle整体感知折中最佳，LTASS无需干净目标语音即可接近。未提供SI-SDR、PESQ、STOI等具体数值，无法列表。

## 🎯 结论与影响

频率相关加权可让软约束SSANC在更低失真下获得更好可懂度-音质折中，LTASS加权因不依赖干净目标语音而最具实用潜力。该结论为开放式助听器空间选择性ANC的感知优化提供了可落地路径，后续可探索自适应权重估计与实时实现。

## ⚠️ 局限与未解决问题

仅用实测冲激响应仿真，未做真人听测；未报告推理延迟、计算量与收敛速度；oracle加权不可实现，LTASS为固定谱，未验证跨说话人/跨噪声泛化；缺少与硬约束SSANC及传统ANC的完整对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-02/">← 返回 2026-10-02 速递</a></div>
