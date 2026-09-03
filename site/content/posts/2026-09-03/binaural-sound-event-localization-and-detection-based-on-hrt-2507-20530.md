---
title: "Binaural Sound Event Localization and Detection based on HRTF Cues for Humanoid Robots"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出双耳声音事件定位与检测任务及合成基准数据集，并设计BTFF特征与CRNN模型BiSELDnet，实现多声源联合检测与定位。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#双耳音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2507.20530</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2507.20530" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2507.20530" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双耳声音事件定位与检测任务及合成基准数据集，并设计BTFF特征与CRNN模型BiSELDnet，实现多声源联合检测与定位。
</div>

## 👥 作者与机构

**Gyeong-Tae Lee** ¹ · Hyeonuk Nam · Yong-Hwa Park

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳音频、声音事件检测与定位的研究者阅读。建议重点阅读第3节（BTFF特征设计）与第4节（BiSELDnet架构），并参考表2与表3的消融实验。若关注机器人听觉，可先看引言与结论。

## 🌍 研究背景

声音事件定位与检测（SELD）在机器人听觉中至关重要，但现有方法多基于麦克风阵列，体积大且功耗高。人类通过双耳听觉实现空间感知，但双耳SELD研究较少，缺乏高质量数据集和有效特征。本文提出BiSELD任务，利用HRTF模拟真实场景，并设计BTFF特征以编码双耳线索，旨在实现类人听觉。

## 💡 核心创新

1. 提出BiSELD任务及合成基准数据集Binaural Set，基于实测HRTF模拟真实场景
2. 设计BTFF特征，融合左右耳mel谱、速度图、SC图及ITD/ILD图，覆盖多频段空间线索
3. 提出CRNN模型BiSELDnet，联合学习谱时模式与HRTF定位线索
4. 系统实现SELD误差0.110，F1 87.1%，定位误差4.4°，验证各子特征有效性

## 🏗️ 模型架构

输入为双耳音频，提取BTFF特征：包含左右耳mel谱、速度图（V-map）、SC-map、ITD/ILD-map共8通道。主干为CRNN：卷积层提取局部谱时特征，循环层（GRU）建模时序依赖，最后通过全连接层输出事件检测与定位结果。检测头输出事件类别概率，定位头输出空间方位（方位角/仰角）。

## 📚 数据集

- Binaural Set（合成数据集，用于训练与评估，包含多种声事件与HRTF模拟）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SELD误差 | Binaural Set | 未提供 | **0.110** | — |
| F-score | Binaural Set | 未提供 | **87.1%** | — |
| 定位误差 | Binaural Set | 未提供 | **4.4°** | — |

实验表明，BTFF各子特征均有贡献：V-map提升检测性能，ITD/ILD-map实现水平定位，SC-map捕捉垂直空间线索。最终系统在Binaural Set上达到SELD误差0.110，F1 87.1%，定位误差4.4°，验证了框架的有效性。

## 🎯 结论与影响

本文提出BiSELD任务及配套数据集和特征，有效模拟人类双耳听觉，实现多声源检测与定位。该方法为机器人听觉提供轻量级方案，有望推动双耳SELD研究，并为HRTF相关应用提供新思路。

## ⚠️ 局限与未解决问题

数据集为合成数据，缺乏真实场景验证；未与基于阵列的方法对比；未报告模型参数量与推理延迟；未探讨噪声和混响鲁棒性。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
