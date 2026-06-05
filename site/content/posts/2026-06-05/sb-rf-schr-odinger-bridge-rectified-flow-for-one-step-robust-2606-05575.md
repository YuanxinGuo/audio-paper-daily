---
title: "SB-RF: Schr\\\"odinger Bridge Rectified Flow for One-Step Robust Speech Enhancement"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出SB-RF，结合薛定谔桥与整流流实现一步生成式语音增强，在VoiceBank-DEMAND上达到领先性能，并在低信噪比场景下展现强鲁棒性。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生成模型</span> <span class="tag-pill tag-pill-soft">#最优传输</span> <span class="tag-pill tag-pill-soft">#一步推理</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.05575</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.05575" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.05575" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SB-RF，结合薛定谔桥与整流流实现一步生成式语音增强，在VoiceBank-DEMAND上达到领先性能，并在低信噪比场景下展现强鲁棒性。
</div>

## 👥 作者与机构

**Caixia Lu** ¹ · Xueyang Lv · Penglong Hu · Jiaming Xu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成模型方向的研究者。建议重点阅读§3的方法部分（SB-RF框架）和§4的实验结果（尤其是低SNR测试集上的表现）。可先看表1和表2对比基线。

## 🌍 研究背景

生成模型在语音增强中表现优异，但通常需要多步推理，计算成本高。现有方法如扩散模型虽能生成高质量语音，但推理速度慢。最优传输理论中的整流流（Rectified Flow）可实现一步生成，但直接应用于语音增强时，由于噪声分布与干净分布差异大，效果受限。本文提出结合薛定谔桥（Schrödinger Bridge）与整流流，构建条件桥接分布，实现一步高质量增强。

## 💡 核心创新

1. 提出SB-RF框架，融合薛定谔桥与整流流
2. 利用熵正则化最优传输构建干净-噪声条件桥
3. 通过速度匹配目标对齐SB轨迹与最优传输测地线
4. 实现一步生成式语音增强，推理效率高
5. 在低SNR场景下验证了方法的鲁棒性

## 🏗️ 模型架构

输入为带噪语音幅度谱；主干网络采用基于U-Net的架构，其中集成整流流速度场预测模块。关键模块包括：1) 薛定谔桥条件构建器，通过熵正则化最优传输生成从噪声到干净语音的桥接分布；2) 整流流速度场网络，以桥接分布为条件预测速度场；3) 一步生成：从噪声分布采样后，沿速度场积分一步得到增强语音。输出为增强语音幅度谱。未提及参数量。

## 📚 数据集

- VoiceBank-DEMAND（训练和评估，标准测试集）
- 模拟低SNR测试集（评估鲁棒性，使用扩展训练数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | SGMSE+ (3.12) | **3.28** | +0.16 |
| CSIG | VoiceBank-DEMAND | SGMSE+ (4.33) | **4.45** | +0.12 |
| CBAK | VoiceBank-DEMAND | SGMSE+ (3.52) | **3.68** | +0.16 |
| COVL | VoiceBank-DEMAND | SGMSE+ (3.63) | **3.79** | +0.16 |

在VoiceBank-DEMAND上，SB-RF在所有指标上超越SGMSE+等生成式方法，且仅需一步推理。在模拟低SNR测试集上，SB-RF相比扩散模型（如SGMSE+）表现出更强的鲁棒性，同时推理速度提升数十倍。消融实验验证了SB桥接和整流流组件的有效性。

## 🎯 结论与影响

SB-RF通过结合薛定谔桥与整流流，首次实现了一步生成式语音增强，性能优于多步生成方法。该方法在低SNR场景下鲁棒性强，推理效率高，有望推动生成式语音增强的实时应用。后续工作可探索更复杂的桥接分布和网络架构。

## ⚠️ 局限与未解决问题

仅在VoiceBank-DEMAND单一数据集上评估，缺乏跨数据集泛化实验；未报告模型参数量和计算复杂度；低SNR测试集为模拟数据，真实场景效果待验证；未与判别式方法（如Conv-TasNet）对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
