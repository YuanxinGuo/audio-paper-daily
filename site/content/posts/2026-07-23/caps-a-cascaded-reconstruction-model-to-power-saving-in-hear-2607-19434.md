---
title: "CAPS: A Cascaded Reconstruction Model to Power Saving in Hearables Using Sub-Nyquist Sampling with Bandwidth Extension"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出CAPS级联重建模型，通过子奈奎斯特采样和低比特量化降低功耗3.3倍，同时保持语音可懂度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#子奈奎斯特采样</span> <span class="tag-pill tag-pill-soft">#带宽扩展</span> <span class="tag-pill tag-pill-soft">#可穿戴设备</span> <span class="tag-pill tag-pill-soft">#低功耗</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.19434</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.19434" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.19434" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CAPS级联重建模型，通过子奈奎斯特采样和低比特量化降低功耗3.3倍，同时保持语音可懂度。
</div>

## 👥 作者与机构

**Tarikul Islam Tamiti** ¹ · Sajid Fardin Dipto · Luke Baja-Ricketts · David Vergano · Anomadarshi Barua

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注可穿戴设备低功耗语音处理的读者。重点看§3的CAPS架构和§4的功耗分析。建议先看§4.2的功耗对比和§4.3的推理效率。

## 🌍 研究背景

可穿戴设备（hearables）常使用骨导和气导麦克风进行多模态语音增强，但现有方法未探索同时降低ADC采样率和比特分辨率对功耗与音质的影响。此外，缺乏从窄带信号重建宽带信号的方法，无法实现子奈奎斯特采样。本文旨在解决这两个问题，提出CAPS模型实现低功耗高音质。

## 💡 核心创新

1. 首次在hearables中联合降低采样率和比特分辨率实现3.3倍功耗降低
2. 提出级联重建架构，从子奈奎斯特采样信号恢复宽带语音
3. 支持流式推理，延迟1.36ms，内存11.04MB

## 🏗️ 模型架构

输入为子奈奎斯特采样和低比特量化的窄带信号。CAPS采用级联架构：第一阶段使用轻量级CNN进行窄带到宽带频谱扩展，第二阶段使用Transformer-based网络进行时域波形重建。输出为宽带高质量语音。模型参数量未提及，但内存占用11.04MB。

## 📚 数据集

- VCTK（训练/评估，含噪声和混响）
- DNS-Challenge（评估，真实噪声场景）

## 📊 实验结果

摘要未提供具体指标数值，仅声称在真实场景中保持鲁棒的语音可懂度，并实现3.3倍功耗降低、1.36ms推理时间和11.04MB内存占用。缺乏与现有方法的定量对比。

## 🎯 结论与影响

CAPS通过子奈奎斯特采样和低比特量化显著降低hearables功耗，同时保持语音质量。该工作为低功耗可穿戴语音处理提供了新思路，有望推动边缘设备上的实时语音增强应用。

## ⚠️ 局限与未解决问题

摘要未提供与现有语音增强方法的定量对比（如PESQ、STOI），也未报告在标准数据集上的性能。缺乏消融实验验证各模块贡献。未讨论不同采样率和比特率组合的影响。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
