---
title: "On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音表示学习"]
summary: "系统研究语音VAE中不同蒸馏损失对齐方式对重建、理解、生成三类任务的影响，提出联合边缘对齐与自适应加权方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#语音重建</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#变分自编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.12383</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.12383" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.12383" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究语音VAE中不同蒸馏损失对齐方式对重建、理解、生成三类任务的影响，提出联合边缘对齐与自适应加权方法。
</div>

## 👥 作者与机构

**Changhao Cheng** ¹ · Wei Wang · Wangyou Zhang · Dongya Jia · Jian Wu · Zhuo Chen · Yanmin Qian ✉

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音表示学习、生成模型研究者。重点读§3蒸馏损失设计、§4实验对比与表2。可先看§4.1整体性能对比，再深入§3.2联合边缘对齐。

## 🌍 研究背景

连续语音表示（如VAE）相比频谱图或离散token在生成任务中有优势。近期工作通过对齐自监督学习（SSL）特征来丰富VAE隐空间的结构信息，但常用的时间轴蒸馏对齐方式在多任务场景下是否最优尚不明确。本文系统探索不同对齐方法对重建、理解、生成三类任务的影响。

## 💡 核心创新

1. 系统比较时间轴、分布对齐等蒸馏损失设计
2. 提出联合边缘对齐（joint-marginal alignment）方法
3. 引入自适应加权平衡多任务性能

## 🏗️ 模型架构

输入语音特征（如mel谱）→ VAE编码器 → 隐变量z → 与SSL特征（如HuBERT）通过蒸馏损失对齐 → VAE解码器输出重建语音。蒸馏损失包括时间轴对齐（如L1/L2）、分布对齐（如KL散度）及联合边缘对齐。自适应加权根据任务重要性调整损失权重。

## 📚 数据集

- LibriSpeech（训练/评估，100h clean）
- VCTK（评估重建）
- LibriTTS（评估生成）
- SLURP（评估理解）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | LibriSpeech test-clean | 时间轴对齐 3.12 | **联合边缘对齐 3.45** | +0.33 |
| WER (%) | SLURP | 时间轴对齐 18.5 | **联合边缘对齐 16.2** | -2.3% |
| MOS | LibriTTS test | 时间轴对齐 3.8 | **联合边缘对齐 4.1** | +0.3 |

联合边缘对齐在重建（PESQ 3.45）、理解（WER 16.2%）、生成（MOS 4.1）上均优于时间轴对齐基线。自适应加权进一步平衡三类任务，消融实验验证了各组件有效性。

## 🎯 结论与影响

本文证明联合边缘对齐蒸馏损失能统一提升语音VAE在重建、理解、生成上的性能，为多任务语音表示学习提供了新范式。后续可探索更复杂的SSL特征融合及动态任务权重。

## ⚠️ 局限与未解决问题

仅在100h LibriSpeech上训练，未验证更大规模数据；未与离散token方法对比；自适应加权需手动设定初始权重，可能不鲁棒。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
