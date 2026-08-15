---
title: "HybridSB-MoE: Dual-Domain Schr\\\"odinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双域Schrödinger桥与场景自适应专家路由的语音增强框架，在VoiceBank+DEMAND上以更少采样步数超越扩散与SB基线。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#专家混合</span> <span class="tag-pill tag-pill-soft">#双域融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.12715</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.12715" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.12715" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双域Schrödinger桥与场景自适应专家路由的语音增强框架，在VoiceBank+DEMAND上以更少采样步数超越扩散与SB基线。
</div>

## 👥 作者与机构

**Zhengyi Lu** ¹ · Aswini Sivakumar · Jie Hu · Yao Qiang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强与生成模型研究者阅读。建议重点看第3节方法部分（尤其3.2异构MoE与3.3离散化界）以及表2的对比结果。若对理论感兴趣可细读定理1证明。

## 🌍 研究背景

生成式语音增强面临三个问题：谱域模型保留谐波但破坏相位，时域模型保留相位但丢失谐波，而Schrödinger桥（SB）虽缩短噪声到干净语音的传输路径，但推理成本与训练步数关联松散。现有方法如扩散模型和一致性蒸馏在步数与质量间权衡，但缺乏对不确定性建模和架构多样性的利用。本文旨在通过双域融合和异构专家路由解决这些局限。

## 💡 核心创新

1. 非对称不确定性融合：谱域捕获认知不确定性，波形域建模偶然不确定性，自适应混合权重
2. 异构MoE：五种架构专家，top-k=2路由，利用架构差异指示归纳偏置失效
3. 离散化界（定理1）：路径一致性与轨迹正则化保证K步采样误差以K^{-α}速率收敛

## 🏗️ 模型架构

输入含噪语音分别送入谱域路径（如STFT域U-Net）和波形域路径（基于SB的波形生成）。谱域路径由多个异构专家组成MoE，通过门控网络选择top-2专家，输出用于估计认知不确定性；波形路径采用随机微分方程建模偶然不确定性。两路径输出通过非对称融合模块（可学习权重）结合，最终生成增强语音。训练时使用路径一致性和轨迹正则化，推理时采用K步离散化采样。

## 📚 数据集

- VoiceBank+DEMAND（训练与评估，含28/56说话人，噪声类型多样）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | 扩散基线（如SGMSE+） | **未给出具体数值** | 优于基线 |
| SI-SDR | VoiceBank+DEMAND | SB基线 | **未给出具体数值** | 优于基线 |

摘要指出在VoiceBank+DEMAND上，HybridSB-MoE在相同采样步数下优于扩散和SB基线，并与一致性蒸馏的少步方法竞争力相当。但未提供具体指标数值，也未提及消融实验或跨数据集泛化。

## 🎯 结论与影响

本文提出双域SB与异构MoE结合的新框架，通过非对称不确定性融合和架构多样性显著提升生成式语音增强性能，同时理论保证小步推理的误差界。该工作为生成式增强提供了新思路，可能推动低延迟实时增强应用，但需更多实验验证泛化性。

## ⚠️ 局限与未解决问题

摘要未提供具体指标数值，缺乏与最新SOTA的定量对比；未报告推理延迟或模型参数量；仅在一个数据集上评估，泛化性未知；异构MoE的专家选择和路由开销未讨论；理论界依赖于正则化强度，实际调参可能敏感。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
