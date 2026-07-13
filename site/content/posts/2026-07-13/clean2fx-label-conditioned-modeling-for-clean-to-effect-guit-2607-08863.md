---
title: "Clean2FX: Label-conditioned modeling for clean-to-effect guitar audio transformations"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频效果转换"]
summary: "提出Clean2FX任务，用标签条件模型将干净吉他音频转换为带效果音频，评估四种神经网络架构。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频效果转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#吉他音频处理</span> <span class="tag-pill tag-pill-soft">#条件生成</span> <span class="tag-pill tag-pill-soft">#U-Net</span> <span class="tag-pill tag-pill-soft">#变分自编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08863</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08863" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08863" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Clean2FX任务，用标签条件模型将干净吉他音频转换为带效果音频，评估四种神经网络架构。
</div>

## 👥 作者与机构

**Oliverio Bombicci Pontelli** ¹ · Iran R. Roman

**机构**：罗彻斯特大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频效果处理或音乐信息检索方向的研究者。可重点阅读第3节模型架构和第4节实验结果，特别是表1中的性能对比。

## 🌍 研究背景

吉他效果器广泛应用于音乐制作，但现有方法多针对特定效果或需要配对数据。Clean2FX任务旨在实现从干净吉他音频到多种效果（如失真、延迟、混响）的转换，且保持音乐内容不变。之前的工作多采用循环一致性或非配对训练，而本文利用EGFxSet数据集中的配对单音录音构建和弦、旋律等复杂样本，进行受控比较。

## 💡 核心创新

1. 提出Clean2FX任务及配套数据集构建方法
2. 对比四种神经网络在频谱变换下的效果
3. 引入条件敏感性诊断验证模型对标签的响应
4. 在真实吉他演奏上展示跨域泛化能力

## 🏗️ 模型架构

输入为干净吉他音频的线性或对数幅度谱，输出为对应效果音频的幅度谱。评估四种模型：两个变分自编码器（VAE）和两个U-Net，分别操作在线性幅度谱和对数幅度谱上。U-Net采用编码器-解码器结构，跳跃连接保留细节；VAE则学习潜在空间分布。所有模型均以效果标签为条件，通过嵌入层注入。输出幅度谱与相位结合（使用输入相位）重构波形。

## 📚 数据集

- EGFxSet（训练和评估，包含单音录音，用于构建配对和弦、旋律等）
- 真实吉他演奏（测试，来自网络，用于演示泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 线性幅度谱MSE | EGFxSet测试集 | VAE (线性) 0.042 | **U-Net (线性) 0.023** | -0.019 |
| Fréchet Audio Distance (FAD) | EGFxSet测试集 | VAE (线性) 1.82 | **U-Net (线性) 1.21** | -0.61 |

U-Net模型在MSE和FAD上均优于VAE变体。线性幅度谱表示略优于对数幅度谱。按效果类型分析，失真效果改进最大，延迟和混响效果FAD提升有限但频谱误差显著降低。条件敏感性诊断显示最佳模型能区分不同效果标签。

## 🎯 结论与影响

Clean2FX展示了标签条件模型在吉他效果转换中的潜力，U-Net架构效果最佳。该工作为可控音频效果生成提供了基准，未来可探索更复杂的条件机制或时域模型。工业上可用于吉他效果器模拟或音乐制作辅助。

## ⚠️ 局限与未解决问题

仅评估幅度谱变换，未处理相位；使用输入相位可能导致音质损失。实验仅在单一数据集上，未与其他非配对方法对比。未报告模型参数量或推理速度。效果标签有限，未涵盖所有常见效果。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
