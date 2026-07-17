---
title: "Making Separation-First Multi-Stream Audio Watermarking Feasible via Joint Training"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "提出分离优先的多流音频水印框架，通过联合训练水印与分离器，显著提升分离后水印恢复率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多流水印</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#联合训练</span> <span class="tag-pill tag-pill-soft">#音频处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.16805</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.16805" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.16805" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出分离优先的多流音频水印框架，通过联合训练水印与分离器，显著提升分离后水印恢复率。
</div>

## 👥 作者与机构

**Houmin Sun** ¹ · Zi Hu · Linxi Li · Yechen Wang · Liwei Jin · Carsten Maple · Ming Li

**机构**：杜伦大学 · 华威大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频水印、语音分离领域研究者。建议重点阅读§3联合训练框架与§4实验部分，对比表1中不同分离器下的比特恢复率。

## 🌍 研究背景

现代音频常由多音轨混合而成，现有水印方法多针对单流或混合后嵌入，无法在分离后独立恢复各音轨水印。直接组合鲁棒水印与现成分离器效果差，因为分离引入的伪影未被水印模型考虑。本文旨在实现分离优先的多流水印，即先分离再解码，需解决分离伪影对水印恢复的破坏问题。

## 💡 核心创新

1. 提出分离感知的水印联合训练框架
2. 将分离器作为检测器的一部分进行联合优化
3. 在语音+音乐和歌声+伴奏混合上验证有效性

## 🏗️ 模型架构

输入为混合音频，先通过分离器（如Demucs或Conv-TasNet）分离成多个音轨，每个音轨使用独立密钥但共享结构的编码器嵌入水印，混合后再次分离，最后用解码器从每个分离输出中恢复水印。编码器与解码器为可微神经网络，分离器可固定或联合训练。

## 📚 数据集

- 语音+音乐混合（训练/评估，具体规模未提及）
- 歌声+伴奏混合（训练/评估，具体规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 比特恢复率 | 语音+音乐混合 | 鲁棒水印+现成分离器（约50%） | **联合训练后（约95%）** | +45% |
| 比特恢复率 | 歌声+伴奏混合 | 鲁棒水印+现成分离器（约55%） | **联合训练后（约93%）** | +38% |

实验表明，联合训练水印与分离器可大幅提升分离后水印恢复率，从约50%提升至95%以上，同时保持感知质量（通过客观指标如SI-SDR未显著下降）。消融实验显示，分离器参与训练是关键。

## 🎯 结论与影响

本文证明分离感知的联合训练是实现多流音频水印的有效途径，为版权保护中多音轨独立水印提供了可行方案。后续可探索更高效的分离器集成与更鲁棒的编码策略，对工业音频内容保护有潜在应用价值。

## ⚠️ 局限与未解决问题

实验仅在两种混合场景（语音+音乐、歌声+伴奏）上验证，未涉及更复杂多源混合；未报告推理延迟与模型参数量；未与现有水印方法（如扩频水印）进行公平对比；联合训练可能增加计算开销。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
