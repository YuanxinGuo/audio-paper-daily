---
title: "Generating Training Targets for Real-World Speech Enhancement via Close-to-Distant Microphone Projection"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出C2D投影方法，利用近远麦克风真实录音生成配对训练数据，提升远场语音增强性能。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#远场语音</span> <span class="tag-pill tag-pill-soft">#训练数据生成</span> <span class="tag-pill tag-pill-soft">#CHiME6</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13109</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13109" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13109" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出C2D投影方法，利用近远麦克风真实录音生成配对训练数据，提升远场语音增强性能。
</div>

## 👥 作者与机构

**Tomohiro Nakatani** ¹ · Rintaro Ikeshita · Naoyuki Kamo · Marc Delcroix · Shoko Araki

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和远场ASR研究者。重点读§3 C2D投影方法和§4实验设置与结果。建议对比GSS方法部分。

## 🌍 研究背景

远场语音增强中，神经网络训练需要配对的无失真和干净参考信号。通常通过仿真生成，但仿真与真实录音的失配严重限制增强精度。现有方法如GSS虽有效，但依赖复杂处理。本文旨在利用真实场景中近远麦克风录音生成高质量训练目标，解决仿真-真实失配问题。

## 💡 核心创新

1. 提出C2D投影方法，利用近远麦克风真实录音生成配对数据
2. 将投影矩阵估计与去噪联合优化，使用PMWF变体实现
3. 在CHiME6任务上超越GSS，且无需复杂预处理

## 🏗️ 模型架构

输入为近麦克风和远麦克风多通道录音。C2D投影估计一个最优投影矩阵，将近麦克风输入变换为与远麦克风对齐的干净参考信号，同时进行去噪。该投影通过参数化多通道维纳滤波器（PMWF）变体实现。训练时，神经网络以远麦克风信号为输入，以C2D投影生成的参考信号为目标进行学习。

## 📚 数据集

- CHiME6（训练/评估，真实远场录音，含近远麦克风配对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | CHiME6 | GSS (oracle diarization) 未给出具体值 | **优于GSS** | 未给出具体数值 |

实验在CHiME6晚餐派对ASR任务上进行，使用oracle diarization。NN以C2D投影数据训练，以GSS增强输出作为辅助输入，在WER上优于单独使用GSS。摘要未提供具体WER数值，但明确表明性能提升。

## 🎯 结论与影响

C2D投影方法有效利用真实录音生成训练目标，缓解仿真-真实失配问题，在CHiME6任务上超越GSS。该方法为远场语音增强训练数据生成提供了新思路，有望推动真实场景语音增强和ASR的实用化。

## ⚠️ 局限与未解决问题

实验仅在CHiME6单一数据集上评估，未报告其他场景或噪声条件下的泛化性。未提供具体WER数值，对比不够充分。方法依赖近远麦克风配对，应用场景受限。未分析计算开销。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
