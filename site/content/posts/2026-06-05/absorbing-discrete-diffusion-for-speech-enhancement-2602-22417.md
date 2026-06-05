---
title: "Absorbing Discrete Diffusion for Speech Enhancement"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出ADDSE，利用吸收离散扩散模型对语音编解码码字进行条件生成，实现语音增强。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#离散扩散</span> <span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#残差向量量化</span> <span class="tag-pill tag-pill-soft">#非自回归采样</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.22417</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.22417" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.22417" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ADDSE，利用吸收离散扩散模型对语音编解码码字进行条件生成，实现语音增强。
</div>

## 👥 作者与机构

**Philippe Gonzalez** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和扩散模型方向的研究者阅读。建议重点看§3的RQDiT架构设计和§4的实验结果，特别是低信噪比下的表现。可先浏览图2和表1。

## 🌍 研究背景

语音增强旨在从带噪语音中恢复干净语音。现有方法包括基于掩蔽的时频域方法和基于扩散的生成方法。扩散模型在语音增强中展现出潜力，但通常需要大量采样步骤。同时，神经音频编解码器（如EnCodec）提供了高效的离散潜在表示。本文结合两者，提出使用吸收离散扩散模型对干净语音的残差向量量化（RVQ）码字进行条件生成，以实现快速且高质量的语音增强。

## 💡 核心创新

1. 提出ADDSE，将语音增强建模为离散码字的吸收扩散过程
2. 设计RQDiT架构，结合RQ-Transformer和扩散Transformer处理RVQ层次结构
3. 实现非自回归采样，显著减少推理步骤
4. 在低信噪比条件下表现优异

## 🏗️ 模型架构

输入带噪语音经预训练神经音频编解码器（如EnCodec）编码为RVQ码字序列。ADDSE采用吸收离散扩散模型，前向过程逐步将干净码字掩蔽为[MASK]标记，反向过程通过RQDiT网络预测被掩蔽的码字。RQDiT由多个DiT块堆叠，每个块包含自注意力、交叉注意力和前馈层，并引入层次位置编码以建模RVQ的层级结构。输出为预测的干净码字，再经解码器重建语音。

## 📚 数据集

- DNS-Challenge（训练和评估，包含多种噪声和混响）
- VCTK-DEMAND（评估，16 kHz）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | SGMSE+ 2.58 | **2.71** | +0.13 |
| SI-SDR (dB) | DNS-Challenge | SGMSE+ 13.2 | **13.8** | +0.6 |
| PESQ | VCTK-DEMAND | SGMSE+ 2.86 | **2.92** | +0.06 |

ADDSE在DNS-Challenge和VCTK-DEMAND上均取得优于SGMSE+的PESQ和SI-SDR，尤其在低SNR条件下提升更明显。仅需25步采样即可达到与50步SGMSE+相当的性能，推理效率更高。消融实验验证了RQDiT中层次位置编码和交叉注意力的有效性。

## 🎯 结论与影响

ADDSE将离散扩散模型成功应用于语音增强，利用神经编解码器的潜在空间实现了高效的非自回归生成。该方法在客观指标上达到竞争性能，且采样步数少，为实时语音增强提供了新思路。未来可探索更优的编解码器或扩散调度策略。

## ⚠️ 局限与未解决问题

实验仅在两个数据集上进行，缺乏跨数据集泛化验证；未报告主观听感测试（如MOS）；未与最新扩散方法（如StoRM）对比；推理延迟未给出具体数值；对编解码器质量依赖较强，编解码器失真可能影响最终性能。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
