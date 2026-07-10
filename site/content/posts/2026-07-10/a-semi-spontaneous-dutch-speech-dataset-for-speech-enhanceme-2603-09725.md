---
title: "A Semi-spontaneous Dutch Speech Dataset for Speech Enhancement and Speech Recognition"
date: 2026-07-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "发布一个1.5小时荷兰语半自发语音数据集DRES，用于评估语音增强和ASR在真实嘈杂室内环境中的表现。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#真实场景</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.09725</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.09725" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.09725" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布一个1.5小时荷兰语半自发语音数据集DRES，用于评估语音增强和ASR在真实嘈杂室内环境中的表现。
</div>

## 👥 作者与机构

**Dimme de Groot** ¹ · Yuanyuan Zhang · Jorge Martinez · Odette Scharenborg

**机构**：代尔夫特理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和ASR领域的研究者阅读。重点看数据集构建细节（§2）和实验结果（§4），特别是SE对ASR无正向影响的发现。建议先看表1和表2。

## 🌍 研究背景

现有语音增强和ASR模型多在干净或合成噪声数据上评估，缺乏真实嘈杂环境下的测试集。真实场景中背景说话人和噪声共存，对模型鲁棒性提出挑战。本文构建了DRES数据集，旨在填补这一空白，并评估SOTA模型在真实场景中的表现。

## 💡 核心创新

1. 构建1.5小时荷兰语半自发语音数据集DRES
2. 80位说话人在真实嘈杂室内环境录制
3. 四通道线性麦克风阵列记录
4. 评估5种SE算法和8种ASR模型
5. 发现单通道SE对ASR无正向影响

## 🏗️ 模型架构

本文不提出新模型，而是构建数据集并评估现有模型。数据集DRES包含80位说话人在嘈杂室内环境（如咖啡馆、大厅）中录制的半自发语音，使用四通道线性麦克风阵列。评估的SE算法包括5种单通道方法（如Wiener滤波、DNN-based），ASR模型包括8种SOTA离线模型（如Whisper、Wav2Vec2）。

## 📚 数据集

- DRES（评估集，1.5小时，80位说话人，嘈杂室内环境）
- 未提及训练集

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | DRES | 无SE时最佳ASR模型WER < 22% | **SE后WER无显著改善** | 无正向提升 |

在DRES上，8个ASR模型中有5个WER低于22%，表明现有ASR在真实嘈杂环境下已具一定鲁棒性。然而，应用5种单通道SE算法后，ASR性能并未提升，甚至略有下降，与近期研究结论相反，凸显了真实场景评估的重要性。

## 🎯 结论与影响

DRES数据集为真实场景语音增强和ASR评估提供了宝贵资源。实验表明，单通道SE在真实嘈杂环境下对ASR无正向帮助，提示未来研究需关注更复杂的多通道或联合优化方法。该数据集有望推动领域向真实场景迁移。

## ⚠️ 局限与未解决问题

数据集规模较小（1.5小时），仅覆盖荷兰语和特定室内场景。未评估多通道SE算法，也未分析SE对语音质量（如PESQ）的影响。ASR模型均为离线版本，未测试流式模型。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-10/">← 返回 2026-07-10 速递</a></div>
