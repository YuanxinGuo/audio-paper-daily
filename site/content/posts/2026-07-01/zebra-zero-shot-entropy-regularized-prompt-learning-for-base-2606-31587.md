---
title: "ZEBRA: Zero-Shot Entropy-Regularized Prompt Learning for Base-to-Novel Generalization in Audio-Language Models"
date: 2026-07-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频分类"]
summary: "提出ZEBRA框架，通过融合零样本logits和自熵正则化，缓解音频-语言模型提示学习中的基类到新类泛化差距。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#提示学习</span> <span class="tag-pill tag-pill-soft">#零样本泛化</span> <span class="tag-pill tag-pill-soft">#音频-语言模型</span> <span class="tag-pill tag-pill-soft">#基类到新类泛化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.31587</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/asif-hanif/zebra" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">asif-hanif/zebra</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.31587" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.31587" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/asif-hanif/zebra" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ZEBRA框架，通过融合零样本logits和自熵正则化，缓解音频-语言模型提示学习中的基类到新类泛化差距。
</div>

## 👥 作者与机构

**Asif Hanif** ¹ · Mohammad Yaqub ✉

**机构**：穆罕默德·本·扎耶德人工智能大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究音频-语言模型、提示学习或零样本泛化的读者。建议重点阅读第3节方法部分和第4节实验，特别是表1和表2的对比结果。可先看§3.2的自熵正则化细节。

## 🌍 研究背景

音频-语言模型（ALMs）通过将音频与文本描述对齐实现强零样本性能。提示学习通过少量样本监督适应提升基类准确率，但常导致新类性能下降，甚至低于零样本基线，形成基类到新类的泛化差距。现有方法缺乏针对ALMs中该问题的解决方案。本文旨在通过融合零样本logits和自熵正则化来缩小这一差距。

## 💡 核心创新

1. 融合零样本logits与提示学习logits的plug-and-play框架
2. 自熵正则化减少对基类的过拟合
3. 无需额外训练或修改提示学习模型

## 🏗️ 模型架构

ZEBRA是一个轻量级后处理框架，输入为基类和新类的音频特征及文本嵌入。它分别计算零样本logits（通过原始ALM的相似度）和提示学习logits（通过微调后的提示），然后加权融合。融合权重通过自熵正则化优化，自熵基于预测概率的熵，鼓励模型在新类上保持不确定性，从而减少过拟合。输出为融合后的分类logits。

## 📚 数据集

- AudioSet（训练/评估，约200万样本）
- ESC-50（评估，50类环境声音）
- VGGSound（评估，309类）
- Clotho（评估，音频描述数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 基类准确率 | AudioSet | 提示学习 85.2 | **ZEBRA 84.9** | -0.3 |
| 新类准确率 | AudioSet | 提示学习 62.1 | **ZEBRA 68.7** | +6.6 |
| 基类准确率 | ESC-50 | 提示学习 92.3 | **ZEBRA 92.0** | -0.3 |
| 新类准确率 | ESC-50 | 提示学习 78.5 | **ZEBRA 84.2** | +5.7 |

ZEBRA在多个数据集上一致提升新类准确率（AudioSet +6.6%，ESC-50 +5.7%），同时基类准确率几乎不变（下降<0.3%）。消融实验验证了自熵正则化和logits融合的有效性。与标准提示学习相比，ZEBRA显著缩小了基类到新类的泛化差距。

## 🎯 结论与影响

ZEBRA通过简单的后处理框架有效缓解了ALMs中提示学习的基类到新类泛化差距，无需修改模型或额外训练。该方法对提升音频分类系统在开放场景下的鲁棒性有潜在价值，可推广至其他多模态模型。

## ⚠️ 局限与未解决问题

实验仅在音频分类任务上验证，未涉及更复杂的音频理解任务（如事件检测）。自熵正则化超参数需手动调整，可能影响泛化。未与更先进的提示学习方法（如CoCoOp）对比。代码已开源但未提供预训练模型。

## 🔗 开源资源

- **代码**：<https://github.com/asif-hanif/zebra>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-01/">← 返回 2026-07-01 速递</a></div>
