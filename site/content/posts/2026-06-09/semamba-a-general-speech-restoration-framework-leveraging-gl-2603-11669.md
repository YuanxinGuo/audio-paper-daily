---
title: "SEMamba++: A General Speech Restoration Framework Leveraging Global, Local, and Periodic Spectral Patterns"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出SEMamba++，通过全局-局部-周期频域模块和多分辨率时频双处理块，在多种语音恢复任务上达到最优性能且保持高效。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音恢复</span> <span class="tag-pill tag-pill-soft">#状态空间模型</span> <span class="tag-pill tag-pill-soft">#频域特征</span> <span class="tag-pill tag-pill-soft">#多分辨率处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.11669</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.11669" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.11669" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SEMamba++，通过全局-局部-周期频域模块和多分辨率时频双处理块，在多种语音恢复任务上达到最优性能且保持高效。
</div>

## 👥 作者与机构

**Yongjoon Lee** ¹ · Jung-Woo Choi ✉

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强/恢复方向的研究者。建议重点阅读§3的GLP模块和多分辨率并行双处理块设计，以及§4的表1和表2对比结果。可复现代码验证其效率优势。

## 🌍 研究背景

通用语音恢复任务要求模型能处理多种失真（噪声、混响等）。现有SOTA如SEMamba基于状态空间模型，但未充分利用语音的频谱周期性和多分辨率特性。本文旨在通过引入语音特定的归纳偏置来提升恢复质量。

## 💡 核心创新

1. 提出GLP模块，利用频率bin的全局、局部和周期特性
2. 设计多分辨率并行时频双处理块，捕获多样频谱模式
3. 引入可学习映射增强模型性能
4. 整体架构在多种失真下保持计算高效

## 🏗️ 模型架构

输入波形经STFT得到频谱，送入GLP模块（包含全局、局部、周期三个分支）提取频域特征；然后通过多分辨率并行时频双处理块（包含不同分辨率下的时域和频域处理子块）融合特征；最后经可学习映射和iSTFT恢复波形。模型参数量未明确给出，但声称计算高效。

## 📚 数据集

- DNS-Challenge（训练/评估，含噪声和混响）
- VCTK+DEMAND（训练/评估，语音去噪）
- LibriTTS（训练/评估，语音恢复）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge 测试集 | SEMamba 3.12 | **3.28** | +0.16 |
| SI-SDR (dB) | VCTK+DEMAND 测试集 | SEMamba 18.5 | **19.2** | +0.7 dB |

在DNS-Challenge和VCTK+DEMAND上，SEMamba++在PESQ和SI-SDR上均超越SEMamba等基线，且参数量和推理时间相近。消融实验验证了GLP模块和多分辨率双处理块的有效性。

## 🎯 结论与影响

本文提出的SEMamba++通过引入语音特定的频域归纳偏置，在多种语音恢复任务上达到SOTA，且保持高效。该工作为将领域知识融入状态空间模型提供了新思路，有望推动语音恢复系统的实际部署。

## ⚠️ 局限与未解决问题

未在真实场景（如远场、多说话人）下评估；未报告推理延迟的具体数值；缺乏与最新Transformer/CNN方法的对比（如MP-SENet）。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
