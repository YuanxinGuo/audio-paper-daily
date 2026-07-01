---
title: "DialogueSidon: Recovering Full-Duplex Dialogue Tracks from In-the-Wild Dialogue Audio"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出DialogueSidon，结合VAE与扩散模型，从退化单声道双人对话音频中恢复并分离出全双工对话轨道。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#全双工对话</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09344</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09344" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09344" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DialogueSidon，结合VAE与扩散模型，从退化单声道双人对话音频中恢复并分离出全双工对话轨道。
</div>

## 👥 作者与机构

**Wataru Nakata** ¹ · Yuki Saito · Kazuki Yamauchi · Emiru Tsunoo · Hiroshi Saruwatari

**机构**：东京大学 · 索尼

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离与增强领域的研究者。建议重点阅读§3模型架构与§4实验部分，特别是VAE压缩SSL特征的细节和扩散预测器的设计。可先看表1与表2对比结果。

## 🌍 研究背景

全双工对话音频（每个说话人独立轨道）是口语对话研究的重要资源，但大规模采集困难。现实中的双人对话通常以退化的单声道混合形式存在，无法直接用于需要干净说话人信号的系统。现有方法在分离退化混合音频时性能有限，且推理速度慢。本文旨在同时恢复和分离退化单声道双人对话音频，提升可懂度和分离质量，并实现快速推理。

## 💡 核心创新

1. VAE压缩SSL特征到紧凑潜空间
2. 扩散潜预测器从退化混合恢复说话人潜表示
3. 联合恢复与分离的端到端框架
4. 在英语、多语言和野外数据集上验证

## 🏗️ 模型架构

输入为退化单声道双人对话音频。首先提取WavLM SSL特征，通过VAE编码器压缩为潜变量。扩散潜预测器以退化混合的潜特征为条件，逐步去噪生成两个说话人的干净潜表示。VAE解码器将潜表示映射回波形。整体模型联合优化VAE和扩散模块，输出两路分离的干净语音。

## 📚 数据集

- LibriMix（训练/评估，英语）
- WSJ0-2mix（评估，英语）
- 多语言对话数据集（评估）
- 野外对话数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | Libri2Mix | SepFormer 17.5 | **18.9** | +1.4 dB |
| PESQ | Libri2Mix | SepFormer 3.12 | **3.28** | +0.16 |

在Libri2Mix上，DialogueSidon的SI-SDRi达18.9 dB，PESQ 3.28，均优于SepFormer基线。在多语言和野外数据集上，可懂度（STOI）和分离质量（SDR）也显著提升。推理速度比基线快约5倍，得益于潜空间扩散的高效性。消融实验证实VAE和扩散预测器均不可或缺。

## 🎯 结论与影响

DialogueSidon通过VAE压缩SSL特征与扩散潜预测器，有效解决了退化单声道双人对话的恢复与分离问题，在多个数据集上取得SOTA性能且推理更快。该方法为全双工对话音频的获取提供了实用方案，有望推动口语对话系统研究。工业上可用于会议记录、语音助手等场景。

## ⚠️ 局限与未解决问题

论文未报告模型参数量及在极端噪声/混响下的表现。仅评估了双人对话，未扩展到多人场景。VAE潜空间的可解释性未探讨。对比基线仅包含SepFormer，缺少与最新扩散分离方法的比较。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
