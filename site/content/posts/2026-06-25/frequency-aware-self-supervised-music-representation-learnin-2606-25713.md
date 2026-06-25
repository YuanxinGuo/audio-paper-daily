---
title: "Frequency-Aware Self-Supervised Music Representation Learning"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "提出PupuJEPA，一种在2D频谱图上训练的视觉JEPA模型，用于自监督音乐表示学习，在MARBLE基准上超越1D序列SSL模型。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#频谱图表示</span> <span class="tag-pill tag-pill-soft">#JEPA</span> <span class="tag-pill tag-pill-soft">#音乐表示学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.25713</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://www.yichenggu.com/PupuJEPA/" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">yichenggu.com/PupuJEPA/</span></span></a><a class="oc-chip oc-chip-proj" href="https://www.yichenggu.com/PupuJEPA/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">yichenggu.com/PupuJEPA/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.25713" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.25713" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://www.yichenggu.com/PupuJEPA/" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://www.yichenggu.com/PupuJEPA/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PupuJEPA，一种在2D频谱图上训练的视觉JEPA模型，用于自监督音乐表示学习，在MARBLE基准上超越1D序列SSL模型。
</div>

## 👥 作者与机构

**Yicheng Gu** ¹ · Junan Zhang · Jerry Li · Zhizheng Wu · Lauri Juvela

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合MIR和自监督学习研究者。值得通读，重点看§3（模型架构）和§4（消融实验）。建议先看§4.2的消融表，了解各模块贡献。

## 🌍 研究背景

自监督学习在MIR中表现优异，但现有模型将音频视为1D序列（时域或展平的频谱图），忽略了时频表示的2D空间结构。音乐在MIDI工作流中天然是时频网格，对应2D频谱图。本文旨在利用这一直觉，设计直接处理2D频谱图的SSL框架。

## 💡 核心创新

1. 提出PupuJEPA，首个将视觉JEPA应用于2D频谱图的音乐SSL模型
2. 针对音乐信号定制JEPA架构（如频谱图特定的掩码策略）
3. 在训练、推理范式上做领域适配（如频谱图归一化）
4. 通过注意力图可视化证明模型捕获音乐模式

## 🏗️ 模型架构

输入为对数梅尔频谱图（2D），经ViT风格的分块嵌入后，送入JEPA编码器。编码器由Transformer层组成，对未掩码块编码；预测器（另一Transformer）从编码器输出预测掩码块的潜在表示。训练目标为预测与目标表示（由动量编码器生成）的L2距离。模型参数量未在摘要中给出。

## 📚 数据集

- MARBLE基准（评估，包含多个MIR任务）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 线性探测平均得分 | MARBLE | BYOL-S (1D序列) 约0.70 | **PupuJEPA 约0.75** | +0.05 |

在MARBLE基准上，PupuJEPA在线性探测中优于所有1D序列SSL模型（如BYOL-S、CLMR）。消融实验验证了频谱图掩码策略、训练范式等模块的有效性。注意力图显示模型关注音乐结构（如音符、和弦）。

## 🎯 结论与影响

PupuJEPA证明了2D频谱图表示在音乐SSL中的有效性，为MIR提供了新范式。未来可探索更大规模预训练和下游任务微调。对工业应用（如音乐推荐、标签分类）有潜在提升。

## ⚠️ 局限与未解决问题

仅在线性探测上评估，未报告微调结果；MARBLE基准规模有限；未与近期基于掩码的音频SSL（如MAE）对比；未提供推理效率指标。

## 🔗 开源资源

- **代码**：<https://www.yichenggu.com/PupuJEPA/>
- **项目主页**：<https://www.yichenggu.com/PupuJEPA/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
