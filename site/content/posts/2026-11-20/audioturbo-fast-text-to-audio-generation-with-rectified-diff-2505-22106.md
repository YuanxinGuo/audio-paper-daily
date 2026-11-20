---
title: "AudioTurbo: Fast Text-to-Audio Generation with Rectified Diffusion"
date: 2026-11-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "将整流扩散引入预训练TTA扩散模型，学习一阶近似ODE路径，实现快速文本到音频生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型加速</span> <span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#整流扩散</span> <span class="tag-pill tag-pill-soft">#ODE求解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2505.22106</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2505.22106" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2505.22106" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将整流扩散引入预训练TTA扩散模型，学习一阶近似ODE路径，实现快速文本到音频生成。
</div>

## 👥 作者与机构

**Junqi Zhao** ¹ · Jinheng Zhao · Haohe Liu · Yun Chen · Lu Han · Haoyang Zhang · Xubo Liu · Mark Plumbley · … 等 1 人

**机构**：萨里大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做扩散加速与TTA生成的读者。值得通读，重点看§3的整流扩散训练目标与ODE路径构造，以及实验部分的推理步数与质量对比表；若关注落地可先看速度-质量权衡曲线。

## 🌍 研究背景

文本到音频（TTA）生成在扩散模型推动下质量与多样性显著提升，代表工作如AudioLDM、Tango等基于预训练扩散框架。但扩散采样需数十至上百步迭代，推理慢，难以落地。近期flow-matching类方法可加速，但通常需专门训练新的流式生成框架，无法直接复用已有强预训练扩散TTA模型。本文要在保留预训练扩散模型生成能力的前提下提升采样效率。

## 💡 核心创新

1. 将整流扩散迁移到预训练TTA扩散模型上做加速
2. 从确定性噪声-样本对学习一阶近似ODE路径
3. 无需重训专用流式框架，直接复用预训练权重

## 🏗️ 模型架构

输入为文本条件与高斯噪声，主干沿用预训练TTA扩散模型（如AudioLDM类潜空间扩散U-Net）。方法核心是整流扩散：先用预训练模型生成确定性噪声-样本配对，再训练一个速度场网络去拟合连接二者的近似直线ODE路径，从而用少量步数完成采样。输出为梅尔谱或潜变量，经声码器还原为音频波形。摘要未给出参数量。

## 📊 实验结果

摘要仅定性说明：在生成质量与推理速度两方面均优于一个基于flow-matching的加速模型，但未给出具体指标数值、数据集名称或加速倍数，无法量化比较。

## 🎯 结论与影响

最强结论是整流扩散可在不重训专用框架的前提下加速已有预训练TTA扩散模型，并同时优于flow-matching加速基线。这为复用现有扩散TTA权重做快速生成提供了可行路径，对实时音频生成落地有参考价值。

## ⚠️ 局限与未解决问题

摘要未报告具体加速倍数、步数与客观指标（如FAD、KL），也缺少与更多加速方法（DDIM、一致性模型）的对比；一阶近似ODE路径在少步采样下的质量上限与对预训练模型分布的依赖未讨论。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-11-20/">← 返回 2026-11-20 速递</a></div>
