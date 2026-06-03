---
title: "Speech Emotion Recognition using Attention-based LSTM-Network with Residual Connection"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "提出ResLSTM-SA，一种结合残差连接和软注意力的轻量LSTM模型，在RAVDESS上以46.8k参数达到65.17% UAR。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#LSTM</span> <span class="tag-pill tag-pill-soft">#注意力机制</span> <span class="tag-pill tag-pill-soft">#残差连接</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.03359</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Mak-Sim/ResLSTM-SER" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Mak-Sim/ResLSTM-SER</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.03359" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.03359" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Mak-Sim/ResLSTM-SER" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ResLSTM-SA，一种结合残差连接和软注意力的轻量LSTM模型，在RAVDESS上以46.8k参数达到65.17% UAR。
</div>

## 👥 作者与机构

**Daniil Krasnoproshin** ¹ · Maxim Vashkevich

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对轻量级语音情感识别模型感兴趣的读者。可重点阅读§3模型架构和§4实验结果，特别是表1的对比。代码已开源，可复现。

## 🌍 研究背景

语音情感识别在人机交互中重要，但现有方法多依赖大型预训练模型，计算和内存需求高，难以部署在边缘设备。传统LSTM和CNN方法性能有限。本文旨在设计轻量级模型，在保持竞争力的同时大幅降低参数量。

## 💡 核心创新

1. 引入残差连接缓解LSTM梯度消失
2. 结合软注意力机制聚焦情感相关帧
3. 仅46.8k参数，比大规模模型少三个数量级

## 🏗️ 模型架构

输入为40维MFCC特征序列。主干为两层LSTM，每层后接残差连接（跳跃连接将LSTM输入与输出相加）。随后应用软注意力机制（soft attention）对时间步加权求和得到句子级表示。最后通过全连接层和softmax输出情感类别。模型变体ResLSTM-SA-h64使用64维隐藏层。

## 📚 数据集

- RAVDESS（训练/评估，说话人独立划分，共1440样本）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| UAR | RAVDESS | Attention-LSTM (0.5938) | **0.6517** | +0.0579 |

在RAVDESS上，ResLSTM-SA-h64达到65.17% UAR，优于传统Attention-LSTM（59.38%）及多个CNN/CNN-LSTM基线。参数量仅46.8k，远少于大规模自监督模型（如wav2vec 2.0等），但性能接近。消融实验验证了残差连接和注意力的有效性。

## 🎯 结论与影响

ResLSTM-SA以极低参数量实现了有竞争力的语音情感识别性能，证明了轻量模型在资源受限场景的潜力。后续可探索更高效的特征或跨数据集泛化。对工业界边缘设备部署有实际意义。

## ⚠️ 局限与未解决问题

仅在单一数据集RAVDESS上评估，缺乏跨数据集泛化验证；未与最新轻量模型（如MobileNet、TinyML方法）对比；未报告推理延迟或实际部署指标；UAR绝对值仍较低（65%），实际应用价值有限。

## 🔗 开源资源

- **代码**：<https://github.com/Mak-Sim/ResLSTM-SER>

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
