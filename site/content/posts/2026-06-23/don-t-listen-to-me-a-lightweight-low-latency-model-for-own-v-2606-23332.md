---
title: "Don't Listen to Me: A Lightweight, Low-Latency Model for Own-Voice Cancellation in Far-Field Speech Enhancement"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出自语音消除任务，用轻量低延迟模型从含噪混合中移除已注册说话人，保留其他语音。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#自语音消除</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.23332</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.23332" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.23332" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出自语音消除任务，用轻量低延迟模型从含噪混合中移除已注册说话人，保留其他语音。
</div>

## 👥 作者与机构

**Mads Østergaard** ¹ · Alexander Neergaard Zahid · Karl Ulbæk · Andreas Hansen Bagge · Kenny Falkær Olsen · Rasmus Malik Høegh Lindrup

**机构**：奥尔堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和低延迟系统研究者。重点看§3模型设计和§4实验对比。可先看表1和表2了解性能与延迟。

## 🌍 研究背景

远场语音增强中，设备将增强音频流回用户时，往返延迟易超过自语音失真感知阈值，产生伪影。现有目标说话人提取（TSE）提取目标语音，但无法消除自身语音。本文提出自语音消除（OVC）作为TSE的互补任务，旨在移除已注册说话人并保留其他语音，需极低延迟。

## 💡 核心创新

1. 提出自语音消除（OVC）新任务
2. Mamba-MinGRU掩码网络实现2ms算法延迟
3. 线性RNN编码器替代ConvTasNet辅助网络
4. 轻量模型在低延迟下提升SDR和pMOS

## 🏗️ 模型架构

输入为多说话人混合波形，经短时帧处理（2ms延迟）。主干为Mamba-MinGRU掩码网络：Mamba块处理序列，MinGRU进行时间混合，生成时域掩码。辅助网络采用线性RNN编码器从注册语音提取说话人嵌入，替代ConvTasNet。输出为分离后的剩余语音波形。模型参数量轻量。

## 📚 数据集

- WSJ0-2mix（训练/评估，混合语音）
- LibriMix（训练/评估，含噪声版本）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | WSJ0-2mix | TD-SpeakerBeam 12.3 | **Mamba-MinGRU 13.8** | +1.5 dB |
| PESQ | WSJ0-2mix | TD-SpeakerBeam 2.45 | **Mamba-MinGRU 2.68** | +0.23 |

在WSJ0-2mix上，Mamba-MinGRU相比TD-SpeakerBeam在SI-SDR提升1.5dB，PESQ提升0.23。线性RNN编码器替换ConvTasNet辅助网络进一步改善SDR和pMOS，同时降低计算量。模型仅2ms算法延迟，适合实时应用。

## 🎯 结论与影响

本文提出自语音消除任务，并设计轻量低延迟模型，在远场增强中有效移除已注册说话人。Mamba-MinGRU结合线性RNN编码器在低延迟下取得优于TD-SpeakerBeam的性能。该工作为低延迟语音交互系统提供了新思路，有望推动设备端实时处理。

## ⚠️ 局限与未解决问题

仅在WSJ0-2mix和LibriMix上评估，未在真实远场数据测试；未报告推理延迟的具体数值（除算法延迟）；未与更多低延迟基线（如DCCRN）对比；未消融Mamba与MinGRU各自贡献。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
