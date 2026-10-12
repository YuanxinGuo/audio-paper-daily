---
title: "Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用强化学习驱动的NAS搜索轻量音视频语音增强架构，仅2.9M参数即达14.5 dB SI-SNR提升，移动CPU实时因子降4.3倍。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#模型压缩</span> <span class="tag-pill tag-pill-soft">#神经架构搜索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.12796</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.12796" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.12796" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用强化学习驱动的NAS搜索轻量音视频语音增强架构，仅2.9M参数即达14.5 dB SI-SNR提升，移动CPU实时因子降4.3倍。
</div>

## 👥 作者与机构

**Khubaib Ahmed** ¹ · Ahsan Adeel · Nasir Saleem · Kia Dashtipour · Ahsan Ulhaq · Amir Hussain

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做边缘端多模态语音增强与模型压缩的研究者/工程师。建议通读，重点看搜索空间定义（音视频时序对齐约束）、奖励函数设计与PPO+约束动作掩码部分，以及架构分析中'更浅更宽TCN+激进视觉剪枝'的结论。表1/表2的SI-SNR与RTF对比是核心证据。

## 🌍 研究背景

音视频语音增强（AVSE）借助视觉线索在噪声下提升可懂度，但主流方法（如基于Conformer/Transformer的音视频融合网络）参数量常达20M以上，难以部署到手机、助听器等资源受限设备。已有轻量化工作多靠手工设计或剪枝，缺乏对音视频融合结构的系统性搜索；通用NAS又未考虑音视频时序对齐与增强性能-紧凑度的联合优化。本文要解决的是：如何在保持音视频对齐的前提下，自动搜索出既小又强的AVSE架构。

## 💡 核心创新

1. RL-NAS框架搜索紧凑AVSE架构，仅评估35个候选
2. 奖励函数联合优化SI-SNR提升与模型紧凑度
3. PPO+约束感知动作掩码保证音视频时序对齐
4. 发现更浅更宽TCN+激进视觉剪枝的有效设计规律

## 🏗️ 模型架构

输入为含噪语音波形/频谱与对应说话人视频帧（唇部ROI）。搜索空间以时序卷积块（TCN）为音频主干、视觉分支经卷积编码后与音频流做时序对齐融合，保留音视频帧级同步约束。控制器用PPO策略网络采样架构配置，动作空间含TCN层数/宽度、视觉通路剪枝率等；约束感知动作掩码剔除破坏对齐的非法动作。奖励=SI-SNR提升加权+参数量惩罚。最终搜索出2.9M参数模型（基线22M），输出增强语音波形。

## 📚 数据集

- 未在摘要中明确给出训练/评估数据集名称

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SNR improvement | 摘要未指明测试集 | 基线 15.2 dB | **14.5 dB** | -0.7 dB |
| 参数量 | — | 22 M | **2.9 M** | 约9倍缩减 |
| Real-Time Factor | 商用移动CPU | 基线 RTF | **降低4.3倍** | -4.3x |
| 搜索效率 | — | 随机搜索 | **RL-NAS** | +92% |

摘要给出：搜索仅评估35个候选架构，最终模型2.9M参数，SI-SNR提升14.5 dB，仅比22M基线低0.7 dB；移动CPU上RTF降低4.3倍；相比随机搜索效率高92%。架构分析显示更浅更宽的时序卷积块与激进视觉通路剪枝可维持性能。摘要未给出具体数据集名称、PESQ/STOI等指标及消融细节。

## 🎯 结论与影响

最强结论是：RL-NAS可在参数量缩减约9倍、移动端RTF降4.3倍的条件下，仅损失0.7 dB SI-SNR，证明强化学习引导的架构搜索能产出可部署的轻量AVSE模型。对边缘端多模态增强与NAS交叉方向有推动作用，工业上利于助听器、手机实时降噪落地。

## ⚠️ 局限与未解决问题

摘要未披露所用数据集、PESQ/STOI/WER等感知指标，也未给推理延迟绝对值与能耗；仅与单一22M基线对比，缺少与MobileNet类轻量AVSE或剪枝/蒸馏方法的横向比较；搜索空间与奖励权重敏感性、跨噪声/跨说话人泛化均未说明。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
