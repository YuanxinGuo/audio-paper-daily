---
title: "StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "StuPASE在PASE基础上引入流匹配模块和干目标微调，实现低幻觉的录音室级语音增强。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#生成式语音增强</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#低幻觉</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.09234</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://xiaobin-rong.github.io/stupase_demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">xiaobin-rong.github.io/stupase_demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.09234" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.09234" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://xiaobin-rong.github.io/stupase_demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>StuPASE在PASE基础上引入流匹配模块和干目标微调，实现低幻觉的录音室级语音增强。
</div>

## 👥 作者与机构

**Xiaobin Rong** ¹ · Jun Gao · Zheng Wang · Mansur Yesilbursa · Kamil Wojcicki · Jing Lu ✉

**机构**：中国科学院声学研究所 · Google

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强研究者，尤其是关注生成式方法和幻觉问题的读者。建议重点阅读第3节方法部分和第4节实验部分，对比PASE与StuPASE的差异。可先看§3.2流匹配模块的设计。

## 🌍 研究背景

生成式语音增强旨在提升感知质量，但常引入幻觉（hallucination）问题。PASE方法在低幻觉方面表现稳健，但在强噪声和混响条件下感知质量有限。现有方法如GAN-based SE在质量与幻觉之间难以平衡。本文旨在改进PASE，在保持低幻觉的同时实现录音室级质量。

## 💡 核心创新

1. 使用干目标（dry targets）微调PASE，改善去混响
2. 用流匹配模块替换GAN生成模块，提升强噪声下质量
3. 在保持低幻觉的同时实现录音室级感知质量

## 🏗️ 模型架构

StuPASE基于PASE架构，输入含噪语音特征，主干网络包含编码器-解码器结构。关键改进：1) 使用干目标（无早期反射）微调整个模型；2) 将PASE中的GAN生成器替换为流匹配（flow-matching）模块，该模块通过连续归一化流生成高质量语音。输出为增强后的语音波形。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和混响）
- VCTK（训练，干净语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge测试集 | PASE 3.12 | **StuPASE 3.45** | +0.33 |
| SI-SDR (dB) | DNS-Challenge测试集 | PASE 18.5 | **StuPASE 20.1** | +1.6 dB |
| HAL (Hallucination Score) | DNS-Challenge测试集 | PASE 0.12 | **StuPASE 0.10** | -0.02 |

StuPASE在DNS-Challenge测试集上PESQ达3.45，SI-SDR达20.1 dB，均优于PASE和现有SOTA。幻觉分数HAL为0.10，与PASE相当，表明低幻觉特性得以保持。消融实验验证了干目标微调和流匹配模块各自的有效性。

## 🎯 结论与影响

StuPASE通过干目标微调和流匹配模块，在保持低幻觉的同时显著提升了生成式语音增强的感知质量，达到录音室级水平。该方法为低幻觉高质量SE提供了新思路，有望推动生成式SE在实际通信系统中的应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量和推理延迟，可能影响实时应用。实验仅在DNS-Challenge数据集上评估，跨数据集泛化性未知。流匹配模块的采样速度可能较慢，需进一步优化。

## 🔗 开源资源

- **Demo / 试听**：<https://xiaobin-rong.github.io/stupase_demo/>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
