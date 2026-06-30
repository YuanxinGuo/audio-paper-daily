---
title: "TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出TF-MoE，在mel频带分割Conformer中引入时-频交替稀疏MoE，以几乎不增加推理成本提升语音分离性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#混合专家模型</span> <span class="tag-pill tag-pill-soft">#低计算量</span> <span class="tag-pill tag-pill-soft">#Conformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.29575</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.29575" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.29575" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TF-MoE，在mel频带分割Conformer中引入时-频交替稀疏MoE，以几乎不增加推理成本提升语音分离性能。
</div>

## 👥 作者与机构

**Qinzhe Hu** ¹ · Chenda Li · Wangyou Zhang · Shujie Liu · Yan Lu · Yanmin Qian

**机构**：上海交通大学 · 微软研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离和边缘部署研究者。建议重点阅读§3.2的MoE模块设计和§4.2的计算效率对比。可先看表1和表2。

## 🌍 研究背景

语音分离领域近期出现了参数量小的前端模型，但高计算成本仍是边缘设备部署的主要障碍。现有方法如BSRNN在计算量受限时性能有限。本文旨在通过稀疏MoE在几乎不增加推理成本的前提下提升模型容量，解决低计算量下的分离性能瓶颈。

## 💡 核心创新

1. 时域和频域交替的MoE模块，动态选择专家
2. 基于mel频带分割的Conformer主干
3. 稀疏MoE实现几乎零额外推理成本
4. 在低计算量设置下显著提升SDR

## 🏗️ 模型架构

输入mel谱图经mel频带分割后送入Conformer主干。主干中交替插入时域MoE和频域MoE模块：时域MoE对每个时间帧动态选择专家，频域MoE对每个mel频带动态选择专家。每个MoE模块包含多个专家前馈网络和门控网络，采用top-2稀疏路由。输出为分离后的语音谱图。模型参数量未明确给出，但推理成本为4.1 GMACs/s。

## 📚 数据集

- Libri2Mix（训练和评估，包含2说话人混合语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR | Libri2Mix | BSRNN (4.1 GMACs/s) 未给出具体值 | **TF-MoE (4.1 GMACs/s) 比BSRNN高3.8 dB** | +3.8 dB |

在Libri2Mix上，TF-MoE在相同计算成本（4.1 GMACs/s）下比BSRNN提升3.8 dB SDR。摘要未提供更多消融或跨数据集结果，但表明该方法在低计算量下具有显著优势。

## 🎯 结论与影响

TF-MoE通过时-频交替稀疏MoE在几乎不增加推理成本下显著提升语音分离性能，为边缘设备部署提供了有效方案。该工作展示了MoE在音频分离中的潜力，可能推动低计算量分离模型的发展。

## ⚠️ 局限与未解决问题

摘要未报告参数量、其他数据集（如WSJ0-2mix）结果、消融实验或推理延迟细节。仅对比BSRNN，缺乏与更多基线（如Conv-TasNet、DPRNN）的比较。未讨论专家负载均衡或训练稳定性。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
