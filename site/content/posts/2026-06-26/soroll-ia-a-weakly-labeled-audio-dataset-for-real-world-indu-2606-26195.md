---
title: "Soroll-IA: A Weakly Labeled Audio Dataset for Real-World Industrial Port Monitoring"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频事件检测"]
summary: "发布了一个22小时、26类工业港口声音事件的弱标注数据集，含两个专家标注版本，并提供CNN14和MobileNetV2基准结果。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#弱监督学习</span> <span class="tag-pill tag-pill-soft">#工业声学</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#音频标注</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.26195</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.26195" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.26195" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布了一个22小时、26类工业港口声音事件的弱标注数据集，含两个专家标注版本，并提供CNN14和MobileNetV2基准结果。
</div>

## 👥 作者与机构

**Javier Naranjo-Alcazar** ¹ · Jordi Grau-Haro · Ruben Ribes-Serrano · Marta Garcia-Ballesteros · Pedro Zuccarello

**机构**：瓦伦西亚理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事环境声音检测、弱监督学习或工业声学监测的研究者。建议重点阅读§3数据集构建和§4基准实验，了解标注策略和模型性能。若关注边缘部署，可看MobileNetV2结果。

## 🌍 研究背景

工业港口环境中的声音事件监测对安全与运营监控至关重要，但缺乏公开的专用数据集。现有环境声音数据集多聚焦城市或自然场景，工业港口声学条件复杂（强背景噪声、远距离源、事件重叠），且标注成本高。弱监督学习可降低标注负担，但需要高质量弱标注数据集。本文旨在填补这一空白，提供首个专门针对工业港口的弱标注音频数据集。

## 💡 核心创新

1. 首个工业港口专用弱标注音频数据集
2. 双版本标注策略（无交叉验证与交叉验证）
3. 固定双节点传感节点部署方案
4. 覆盖26类代表性工业港口声音事件

## 🏗️ 模型架构

数据集本身不涉及模型架构。基准实验采用两种架构：CNN14（高容量卷积网络，用于音频标记）和MobileNetV2（轻量级网络，适用于低资源边缘设备）。输入为音频片段，输出为26类事件的多标签预测。

## 📚 数据集

- Soroll-IA（训练/评估，22小时，7396个片段，26类）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1-score (macro) | Soroll-IA | CNN14: 0.52 (无交叉验证版本) | **CNN14: 0.52** | 0 |
| F1-score (macro) | Soroll-IA | MobileNetV2: 0.44 (无交叉验证版本) | **MobileNetV2: 0.44** | 0 |

摘要仅给出基准结果，无本文方法创新。CNN14在无交叉验证版本上macro F1为0.52，MobileNetV2为0.44。交叉验证版本指标略低。未提供与其他数据集的对比或消融实验。

## 🎯 结论与影响

Soroll-IA是首个专用于工业港口声学环境的弱标注数据集，包含22小时音频和26类事件，双版本标注策略考虑了标注者变异性。该数据集有望推动鲁棒环境声音分析在安全关键和运营监控中的应用。基准实验表明，现有模型在该数据集上仍有较大提升空间。

## ⚠️ 局限与未解决问题

数据集仅来自单一港口（Valencia），泛化性未知；弱标注缺乏时间边界，无法支持事件检测的精确时间定位；未提供跨数据集泛化实验；基准模型未采用最新架构（如Transformer）；未报告推理延迟或资源消耗。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
