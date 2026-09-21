---
title: "HAMMER: Harmonic-Aware Parallel Context Modeling and Discriminator-Free Perceptual Optimization for Speech Enhancement"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出谐波感知的 TF-HAM 模块与无判别器的 MEPR 感知优化，在 VoiceBank+DEMAND 上以 2.39M 参数达 3.69 PESQ。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#感知指标优化</span> <span class="tag-pill tag-pill-soft">#自注意力</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.21171</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/shangfuu/HAMMER.git" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">shangfuu/HAMMER.git</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.21171" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.21171" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/shangfuu/HAMMER.git" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出谐波感知的 TF-HAM 模块与无判别器的 MEPR 感知优化，在 VoiceBank+DEMAND 上以 2.39M 参数达 3.69 PESQ。
</div>

## 👥 作者与机构

**Shang-Fu Chen** ¹ · Szu-Wei Fu · Sung-Feng Huang · Rong Chao · Wen-Huang Cheng · Yu Tsao

**机构**：台湾大学 · 中央研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强、Mamba/注意力混合架构与感知损失的研究者阅读。建议通读，重点看 §3 的 TF-HAM 双轴并行结构与自相关 FFN 设计，以及 MEPR 中可微 PESQ 与 LLR 损失的组合方式；表 2 的参数量-性能对比与推理期对比度拉伸实验值得细看。

## 🌍 研究背景

近期语音增强多采用自注意力与 Mamba 混合结构，以兼顾全局交互与长程依赖，代表工作如 SEMamba、MambaSE 等。但这类混合体多作为通用序列混合器，未显式建模语音的谐波周期性——这是噪声下保留浊音的关键线索。感知优化方面，PESQ 不可微，主流做法是训练辅助指标判别器，带来额外复杂度与对抗训练不稳定。本文要解决的是：如何在无判别器条件下显式利用谐波结构并优化感知指标。

## 💡 核心创新

1. TF-HAM 块：自注意力与双向 Mamba 沿时频双轴并行
2. 语音自适应自相关 FFN 编码局部周期结构
3. MEPR：可微 PESQ + LLR 损失替代指标判别器
4. 推理期感知对比度拉伸，免重训提升 PESQ

## 🏗️ 模型架构

输入为含噪语音的幅度谱图。主干由堆叠的 TF-HAM 块构成：每个块内自注意力与双向 Mamba 沿时间轴和频率轴并行运行，分别捕获全局交互与长程依赖，随后经语音自适应自相关前馈网络（autocorrelation FFN）编码局部谐波周期结构，输出融合特征。整体为编码器-解码器式谱映射，输出增强幅度谱，配合相位重建波形。模型仅 2.39M 参数，训练目标为 MEPR，即结合可微 PESQ 与对数似然比（LLR）损失，无需学习型指标判别器。

## 📚 数据集

- VoiceBank+DEMAND（训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | 判别器类方法（摘要未给具体值） | **3.69** | 优于或持平 |
| COVL | VoiceBank+DEMAND | 判别器类方法（摘要未给具体值） | **4.41** | 优于或持平 |
| PESQ（推理期对比度拉伸） | VoiceBank+DEMAND | 本文基础模型 3.69 | **3.79** | +0.10 |

摘要仅给出 VoiceBank+DEMAND 上的 PESQ 3.69、COVL 4.41 与 2.39M 参数量，并称优于或匹配基于判别器的系统；推理期感知对比度拉伸可免重训将 PESQ 提升至 3.79。摘要未提供 SI-SDR、STOI、WER 等指标，也未给出与具体基线（如 SEMamba、SEGAN、MetricGAN+）的逐项数值对比与消融结果。

## 🎯 结论与影响

最强结论是：无需指标判别器，仅靠谐波感知的并行注意力-Mamba 结构与可微 PESQ+LLR 损失，即可在 2.39M 参数下达到 3.69 PESQ，并可通过推理期对比度拉伸进一步提升。这为感知优化提供了一条更简洁、更稳定的替代路径，可能推动后续工作放弃对抗式指标判别器；工业上意味着更小模型、更易训练部署的增强前端。

## ⚠️ 局限与未解决问题

摘要未报告 SI-SDR、STOI 等保真度指标，也未给出与 SEMamba 等强基线的逐项数值对比；缺少 TF-HAM 各组件与 MEPR 各损失的消融。仅在 VoiceBank+DEMAND 单一合成数据集评估，真实录音与混响场景泛化未知。推理期对比度拉伸的机制与稳定性未详述，且未报推理延迟与实时性。

## 🔗 开源资源

- **代码**：<https://github.com/shangfuu/HAMMER.git>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
