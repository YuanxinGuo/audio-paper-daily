---
title: "SE-MSB: End-to-End Unpaired Speech Enhancement using Mamba Schr\\\"odinger Bridges"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用 Mamba 扩散模型实现端到端无配对语音增强，基于 Diffusion Schrödinger Bridge 学习干净与退化语音分布间的随机传输。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#无配对学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.26000</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.26000" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.26000" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用 Mamba 扩散模型实现端到端无配对语音增强，基于 Diffusion Schrödinger Bridge 学习干净与退化语音分布间的随机传输。
</div>

## 👥 作者与机构

**Andreas Bagge** ¹ · **Andreas Nymand** ¹ · Michael Riis Andersen · Bj{\o}rn Sand Jensen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做扩散/桥模型语音增强与高效生成的研究者。建议通读，重点看 §3 的 DSB 公式与 Mamba 主干设计，以及表 2 的推理速度对比。可先看方法图与消融，再核对与有配对基线的公平性设置。

## 🌍 研究背景

语音增强长期依赖配对数据：干净语音经合成加噪/加混响得到训练对，代表方法如基于 Conformer/BSRNN 的监督模型在 DNS-Challenge 上取得高 PESQ。但合成退化与真实环境声学不匹配，域外泛化差；无配对方法（如 CycleGAN、无配对扩散）虽缓解该问题，却常需在训练中模拟微分方程，计算开销大、推理慢。本文要解决的是：在无配对设定下，用高效端到端波形模型学习干净—退化分布间的随机传输，兼顾性能与推理速度。

## 💡 核心创新

1. 用 Diffusion Schrödinger Bridge 建模干净与退化语音分布间的随机传输，无需配对数据
2. 提出面向端到端波形处理的高效 Mamba 扩散模型主干，替代注意力/卷积
3. 训练中避免逐步模拟微分方程，显著降低训练与推理开销
4. 同一 DSB 框架可泛化到多种 SE 任务，无需任务特定重训

## 🏗️ 模型架构

输入为原始波形（端到端，不做 STFT 前端）。主干为 Mamba 扩散模型：以 Mamba 状态空间块沿时间轴建模长程依赖，替代 Transformer 注意力以降低序列复杂度；在 DSB 框架下学习前向/反向随机传输过程，通过迭代比例拟合或类似目标估计漂移项，训练时避免每步模拟 SDE。输出为增强后的干净波形。摘要未给出具体参数量与层数配置。

## 📊 实验结果

摘要仅给出定性结论：在配对与无配对 SOTA 方法及经典信号处理基线上，性能持平或更优，且推理速度快数个数量级；并称 DSB 公式的灵活性使模型可跨 SE 任务泛化。摘要未提供 SI-SDR、PESQ、WER 等具体数值、测试集名称或消融结果，无法量化对比。

## 🎯 结论与影响

最强结论是：无配对 DSB + Mamba 可在性能持平或超越配对/无配对基线的同时，把推理速度提升数个数量级。这为无配对语音增强提供了高效生成式范式，可能推动后续在真实退化域上的域泛化研究；工业上意味着可用目标环境录音直接适配，降低对合成配对数据的依赖。

## ⚠️ 局限与未解决问题

摘要未报告具体指标、数据集与参数量，难以判断提升幅度；缺少与最新无配对扩散/流匹配方法的完整对比；未说明 DSB 训练稳定性、采样步数与延迟；跨任务泛化仅定性宣称，缺消融与失败案例分析。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
