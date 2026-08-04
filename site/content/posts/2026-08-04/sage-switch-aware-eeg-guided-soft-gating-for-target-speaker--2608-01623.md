---
title: "SAGE: Switch-Aware EEG-Guided Soft Gating for Target Speaker Extraction with In-Trial Switching"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出SAGE框架，利用脑电信号引导软门控，实现试听注意力动态切换下的目标说话人提取，降低切换延迟并提升性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脑电引导</span> <span class="tag-pill tag-pill-soft">#软门控</span> <span class="tag-pill tag-pill-soft">#注意力切换</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.01623</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.01623" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.01623" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SAGE框架，利用脑电信号引导软门控，实现试听注意力动态切换下的目标说话人提取，降低切换延迟并提升性能。
</div>

## 👥 作者与机构

**Xuefei Wang** ¹ · Ximin Chen · Yuting Ding · Chunlin Li · Fei Chen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事脑电与语音结合、目标说话人提取的研究者。建议重点阅读第3节（方法）和第4节（实验），特别是门控模块和延迟补偿设计。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

脑电引导的目标说话人提取在试听注意力切换场景下具有挑战性，因为神经噪声和内在延迟会导致注意力跟踪不稳定。传统方法难以处理动态切换，常在切换点产生不连续。现有方法多假设注意力固定，缺乏对切换的显式建模。本文旨在解决动态切换下的鲁棒提取问题，通过软门控和延迟补偿提升性能。

## 💡 核心创新

1. 提出开关感知软门控框架，将试听切换建模为动态选择
2. 设计脑电引导的开关感知门控模块，生成平滑融合权重
3. 引入延迟补偿对齐，处理脑电信号与语音的时序失配
4. 采用不确定性驱动的保守策略，应对脑电信噪波动
5. 在切换场景下实现低延迟（2.04s）和高性能（SI-SDR 8.67dB）

## 🏗️ 模型架构

输入为混合语音和脑电信号。混合语音经鲁棒分离器生成两个候选语音流；脑电信号经特征提取后，与开关信息结合，输入开关感知门控模块，生成平滑融合权重。门控模块采用软门控机制，结合延迟补偿对齐和不确定性估计，输出最终提取的目标语音。整体框架端到端训练。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | 未指定 | 未给出 | **8.67 dB** | 未给出 |
| STOI | 未指定 | 未给出 | **88.24%** | 未给出 |

摘要报告SAGE在SI-SDR和STOI上优于基线，平均切换延迟降至2.04秒。但未提供具体基线数值和数据集细节，也未提及消融实验或跨数据集泛化。

## 🎯 结论与影响

SAGE通过耦合神经解码与语音分离，实现了动态场景下的鲁棒目标提取，显著降低切换延迟并提升性能。该工作为脑电引导的语音处理提供了新思路，有望推动脑机接口与助听设备的结合，实现更自然的听觉注意力控制。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可看出：未报告具体数据集和基线，缺乏与现有方法的定量对比；未讨论脑电采集的实用性和实时性；未分析门控模块的复杂度和计算开销；未验证在真实噪声环境下的鲁棒性。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
