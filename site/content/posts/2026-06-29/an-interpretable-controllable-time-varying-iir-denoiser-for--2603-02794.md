---
title: "An Interpretable, Controllable Time-Varying IIR Denoiser for On-Device Assistive Hearing"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种可解释、低延迟的时变IIR滤波器语音增强模型，仅24k参数，10.7ms延迟，适用于助听设备。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#IIR滤波</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02794</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02794" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02794" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种可解释、低延迟的时变IIR滤波器语音增强模型，仅24k参数，10.7ms延迟，适用于助听设备。
</div>

## 👥 作者与机构

**Riccardo Rota** ¹ · Kiril Ratmanski · Jozef Coldenhoff · Milos Cernak

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和可解释AI研究者。重点读§3模型架构和§4实验对比，尤其是HASPI/HASQI指标与DFNet3的比较。可关注其可控性设计（§3.3）。

## 🌍 研究背景

助听设备中的语音增强需满足低延迟、低功耗和可解释性。现有深度模型（如DFNet3）性能好但参数量大（2.3M）、不可解释。传统信号处理方法可解释但性能有限。本文旨在设计一个轻量、可解释且性能接近大模型的实时降噪方案。

## 💡 核心创新

1. 可微分的35阶IIR双二阶滤波器级联
2. 24k参数的小型神经控制器实时预测滤波器系数
3. 显式的抑制-保留权衡控制，可在推理时调整
4. 10.7ms算法延迟，完全设备端运行

## 🏗️ 模型架构

输入噪声语音 → 轻量神经控制器（24k参数）预测35个双二阶IIR滤波器的系数 → 可微分级联滤波器处理信号 → 输出增强语音。整个处理链可解释，每个滤波器对应一个显式均衡曲线。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和干净语音）
- Hearing-aid specific test set（评估HASPI/HASQI）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| HASPI | 助听测试集 | DFNet3 (2.3M) 约0.85 | **约0.83** | -0.02 |
| HASQI | 助听测试集 | DFNet3 (2.3M) 约0.80 | **约0.78** | -0.02 |
| PESQ | DNS-Challenge | DFNet3 较高 | **较低** | 未明确数值 |

24k参数模型在HASPI/HASQI上仅比2.3M参数的DFNet3低约0.02，计算量减少约29倍。但在PESQ等参考指标上仍落后于大型黑盒模型。消融实验验证了可控性和可解释性。

## 🎯 结论与影响

TVF证明了紧凑、可解释、可控的降噪器在助听设备上的可行性。其显式均衡曲线和推理时可控性为可解释语音增强提供了新方向，有望推动工业落地。

## ⚠️ 局限与未解决问题

在PESQ等指标上不如大模型；仅验证了降噪任务，未涉及混响等；未报告实际设备功耗；可控性仅通过混合输入输出实现，可能引入失真。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
