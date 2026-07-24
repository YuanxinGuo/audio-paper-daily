---
title: "LaDA-Band: Language Diffusion Models for Vocal-to-Accompaniment Generation"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出LaDA-Band，利用离散掩码扩散模型实现端到端的人声转伴奏生成，兼顾声学真实感、全局连贯性和动态编配。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#人声转伴奏</span> <span class="tag-pill tag-pill-soft">#离散掩码扩散</span> <span class="tag-pill tag-pill-soft">#非自回归生成</span> <span class="tag-pill tag-pill-soft">#音频编解码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.11052</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Duoluoluos/TME-LaDA-Band" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Duoluoluos/TME-LaDA-Band</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.11052" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.11052" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Duoluoluos/TME-LaDA-Band" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出LaDA-Band，利用离散掩码扩散模型实现端到端的人声转伴奏生成，兼顾声学真实感、全局连贯性和动态编配。
</div>

## 👥 作者与机构

**Qi Wang** ¹ · Zhexu Shen · Meng Chen · Guoxin Yu · Chaoxu Pang · Weifeng Zhao · Wenjiang Zhou

**机构**：腾讯音乐

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、音频编解码及扩散模型研究者。建议重点阅读§3的离散掩码扩散公式和§4的双轨前缀条件架构。先看§3.2与表2的对比结果。

## 🌍 研究背景

人声转伴奏（V2A）生成需同时满足声学真实感、与主旋律的全局连贯性及全曲动态编配，现有方法难以兼顾：连续潜变量模型能捕捉长程音乐结构但丢失细节，离散自回归模型保留局部保真度却因单向生成和误差累积导致长上下文问题。本文旨在提出一种全局非自回归的离散掩码扩散框架，统一解决上述三难困境。

## 💡 核心创新

1. 离散掩码扩散用于V2A任务
2. 双轨前缀条件架构
3. 替换令牌检测辅助目标
4. 两阶段渐进式课程学习

## 🏗️ 模型架构

输入为原始人声录音，经音频编解码器（如EnCodec）离散化为令牌序列。主干网络采用离散掩码扩散模型，以非自回归方式逐步去噪生成伴奏令牌。关键模块包括：双轨前缀条件架构（同时以人声令牌和可选参考音频为条件）、替换令牌检测辅助目标（用于弱锚定伴奏区域）、以及两阶段渐进式课程（先短片段再全曲）。输出为离散令牌序列，经解码器合成伴奏音频。

## 📚 数据集

- MUSDB18（训练/评估，含150首完整歌曲）
- 内部数据集（训练/评估，大规模真实歌曲）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | MUSDB18 | V2A-MelGAN 3.21 | **2.15** | -1.06 |
| CLAP Score | MUSDB18 | V2A-MelGAN 0.28 | **0.34** | +0.06 |
| MOS (Overall) | 内部测试集 | V2A-MelGAN 3.12 | **3.89** | +0.77 |

在MUSDB18和内部数据集上，LaDA-Band在FAD、CLAP Score和MOS指标上均显著优于V2A-MelGAN等基线。消融实验验证了双轨前缀条件、替换令牌检测目标和两阶段课程的有效性。即使无参考音频，性能仍保持强劲。

## 🎯 结论与影响

LaDA-Band首次将离散掩码扩散成功应用于人声转伴奏生成，在声学真实感、全局连贯性和动态编配上均取得显著提升。该工作为音乐生成中长程结构建模提供了新范式，有望推动AI辅助音乐制作工具的落地。

## ⚠️ 局限与未解决问题

论文未报告推理延迟和模型参数量；离散掩码扩散的采样步数对质量的影响未充分探讨；仅与V2A-MelGAN对比，缺少与更多最新扩散模型的比较；数据集仅含流行音乐，泛化性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/Duoluoluos/TME-LaDA-Band>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
