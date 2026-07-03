---
title: "LMPAN: A Lightweight Multi-Path Alignment Network for Joint Full-Duplex Acoustic Echo Cancellation and Noise Suppression"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出轻量级多路径对齐网络LMPAN，仅480K参数实现全双工声学回声消除与噪声抑制联合处理，性能媲美DeepVQE-S。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声学回声消除</span> <span class="tag-pill tag-pill-soft">#噪声抑制</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span> <span class="tag-pill tag-pill-soft">#全双工对话系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.02062</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.02062" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.02062" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出轻量级多路径对齐网络LMPAN，仅480K参数实现全双工声学回声消除与噪声抑制联合处理，性能媲美DeepVQE-S。
</div>

## 👥 作者与机构

**Chengwei Liu** ¹ · Shaofei Xue · Haoyin Yan · Xiaotao Liang · Zheng Xue

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事设备端语音处理、AEC/NS联合建模的研究者。建议重点阅读§3多路径对齐模块和§4两阶段训练策略，对比表1和表2的消融实验。

## 🌍 研究背景

全双工语音对话系统中，声学回声消除（AEC）和噪声抑制（NS）通常串联处理，但硬件失真和动态声学环境导致性能下降。现有轻量模型如DeepVQE-S虽有效，但未充分对齐参考信号、线性AEC输出和麦克风信号间的时域与能量失配。本文提出LMPAN，通过多路径对齐和注意力融合解决该问题。

## 💡 核心创新

1. 多路径对齐阶段校正参考、LAEC输出和麦克风信号的时域与能量失配
2. 注意力机制动态融合增强后的LAEC和麦克风特征
3. 后滤波模块采用动态目标生成策略适配下游ASR/VAD任务
4. 两阶段训练框架利用自监督表示提升感知质量

## 🏗️ 模型架构

输入为参考信号、线性AEC输出和麦克风信号三路。首先经多路径对齐阶段，通过可学习延迟和增益校正时域与能量失配；然后对齐后的特征送入注意力融合模块，动态加权整合；最后经后滤波模块（含动态目标生成）输出增强语音。主干网络为轻量卷积结构，总参数量480K，MACs 126。

## 📚 数据集

- AEC-Challenge数据集（训练/评估，包含真实和模拟回声噪声场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | AEC-Challenge测试集 | DeepVQE-S (3.12) | **3.18** | +0.06 |
| ERLE (dB) | AEC-Challenge测试集 | DeepVQE-S (18.5) | **19.1** | +0.6 dB |

LMPAN在AEC-Challenge测试集上PESQ达3.18，ERLE 19.1 dB，均优于DeepVQE-S。消融实验验证了多路径对齐和注意力融合的有效性。两阶段训练相比单阶段提升PESQ约0.05。模型参数量仅480K，MACs 126，满足实时推理需求。

## 🎯 结论与影响

LMPAN以极低参数量实现了与SOTA轻量模型相当的AEC/NS性能，为设备端部署提供了高效方案。其多路径对齐和注意力融合设计可推广至其他多源对齐任务。工业落地中，该模型有望降低智能音箱等设备的语音交互延迟。

## ⚠️ 局限与未解决问题

仅在AEC-Challenge数据集上评估，未见跨数据集泛化实验；未报告推理延迟具体数值（仅说实时）；未与更大模型（如DCCRN）对比；动态目标生成策略对ASR/VAD的增益未在实验中直接验证。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
