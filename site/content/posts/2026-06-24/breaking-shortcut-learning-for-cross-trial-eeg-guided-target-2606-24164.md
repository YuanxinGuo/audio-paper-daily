---
title: "Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出两阶段训练框架TRUST-TSE，通过对比预训练抑制试次特异性捷径学习，提升跨试次EEG引导目标语音提取的泛化性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG引导</span> <span class="tag-pill tag-pill-soft">#语音提取</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#两阶段训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24164</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24164" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24164" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段训练框架TRUST-TSE，通过对比预训练抑制试次特异性捷径学习，提升跨试次EEG引导目标语音提取的泛化性。
</div>

## 👥 作者与机构

**Wonchul Shin** ¹ · Inyong Choi · Kyogu Lee

**机构**：首尔大学 · 爱荷华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事神经引导听觉技术、EEG-语音融合的研究者。建议重点阅读§3两阶段框架设计和§4跨试次实验设置，先看表1对比结果。

## 🌍 研究背景

EEG引导的目标语音提取旨在利用脑电信号从混合语音中提取目标说话人，近期端到端模型在试次内表现优异。然而，本文发现模型可能依赖试次特异性EEG结构（如身份线索）作为捷径，导致跨试次泛化差。现有方法未专门解决此问题，限制了神经助听技术的可靠性。本文旨在通过两阶段训练打破捷径学习。

## 💡 核心创新

1. 提出TRUST-TSE两阶段框架，分离EEG编码与语音提取
2. 对比预训练采用关注说话人负采样，抑制试次身份线索
3. 基于EEG-源相似度的置信加权提取目标
4. 在KUL和DTU数据集上严格跨试次协议下验证

## 🏗️ 模型架构

输入为混合语音和EEG信号。第一阶段：EEG编码器（CNN+Transformer）通过对比学习预训练，正样本对为同一试次内目标说话人语音与EEG，负样本为其他试次目标说话人语音，迫使编码器学习EEG-语音对齐而非试次身份。第二阶段：冻结EEG编码器，将EEG嵌入与混合语音特征（通过Conv-TasNet提取）融合，采用基于EEG-源相似度的置信加权损失训练提取网络，输出目标语音。

## 📚 数据集

- KUL（训练/评估，包含多说话人混合与EEG）
- DTU（训练/评估，包含多说话人混合与EEG）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | KUL | 端到端基线 8.5 | **TRUST-TSE 10.2** | +1.7 |
| SI-SDRi (dB) | DTU | 端到端基线 7.8 | **TRUST-TSE 9.5** | +1.7 |

在KUL和DTU数据集上，TRUST-TSE在跨试次协议下SI-SDRi分别提升1.7 dB，优于端到端基线。消融实验证实对比预训练和置信加权目标均有效，且模型对试次身份线索的敏感性显著降低。

## 🎯 结论与影响

本文揭示EEG引导目标语音提取中的捷径学习问题，并提出TRUST-TSE两阶段框架有效缓解。该工作为神经助听技术的跨试次泛化提供了新思路，未来可结合更丰富的EEG编码架构进一步提升性能。

## ⚠️ 局限与未解决问题

仅在两个数据集上验证，规模有限；未报告推理延迟或模型参数量；对比基线仅包含端到端模型，未与更先进的EEG-语音融合方法比较；未分析EEG编码器对噪声的鲁棒性。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
