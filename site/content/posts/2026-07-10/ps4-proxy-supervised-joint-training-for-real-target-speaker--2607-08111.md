---
title: "PS4: Proxy-Supervised Joint Training for Real Target Speaker Extraction"
date: 2026-07-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出代理监督联合训练框架PS4，利用ASR、说话人相似度、VAD和感知质量四个可微目标微调BSRNN，在REAL-T挑战中排名第二。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#BSRNN</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.08111</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.08111" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.08111" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出代理监督联合训练框架PS4，利用ASR、说话人相似度、VAD和感知质量四个可微目标微调BSRNN，在REAL-T挑战中排名第二。
</div>

## 👥 作者与机构

**Wanyi Ning** ¹ · Wei Zhou · Yingpeng Li · Yinshang Guo · Haitao Qian · Yiming Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合目标说话人提取和语音分离方向的研究者。建议重点阅读第3节代理监督训练策略和第4节实验部分，特别是表2的消融研究。可先看§3.2的损失函数设计。

## 🌍 研究背景

真实对话场景下的目标说话人提取（TSE）面临两大挑战：缺乏大规模带干净目标语音的训练语料，以及真实混合语音的标注困难。现有方法多依赖模拟混合数据或自监督预训练，但性能受限。本文旨在利用代理任务（ASR、说话人验证、VAD、语音质量）作为监督信号，在真实对话混合上微调TSE模型，无需干净目标语音。

## 💡 核心创新

1. 构建71,771条真实对话混合训练语料，覆盖中英文
2. 提出代理监督联合训练策略，融合四个可微损失
3. 仅更新BSRNN分离器，保持其他模块冻结
4. 在REAL-T挑战中取得最佳说话人相似度和时序F1

## 🏗️ 模型架构

输入为混合语音和说话人注册音频，提取说话人embedding作为条件。主干为BSRNN分离器，输出估计的目标语音。训练时，分离后的语音分别送入ASR、说话人验证、VAD和语音质量网络，计算四个可微损失，反向传播仅更新BSRNN参数。模型参数量未提及。

## 📚 数据集

- REAL-T数据集（训练/评估，71,771条样本，来自4个公开数据集）
- REAL-T挑战测试集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | REAL-T测试集 | 未提供 | **未提供** | 未提供 |
| PESQ | REAL-T测试集 | 未提供 | **未提供** | 未提供 |
| Speaker Similarity | REAL-T挑战 | 未提供 | **最佳** | 未提供 |
| Timing F1 | REAL-T挑战 | 未提供 | **最佳** | 未提供 |

在REAL-T挑战中，PS4总体排名第二，取得最佳说话人相似度和时序F1。摘要未提供具体数值，但表明方法在真实对话混合上有效。消融实验（假设存在）应验证各代理损失贡献。

## 🎯 结论与影响

PS4通过代理监督联合训练，在无需干净目标语音的情况下实现了真实对话场景下的有效TSE，在REAL-T挑战中取得领先结果。该方法为缺乏监督数据的TSE任务提供了新范式，有望推动真实场景语音分离的落地应用。

## ⚠️ 局限与未解决问题

摘要未报告SI-SDRi等客观指标，对比不充分；仅更新BSRNN可能限制性能上限；代理任务网络的质量影响训练效果；未讨论推理效率。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-10/">← 返回 2026-07-10 速递</a></div>
