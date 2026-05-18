---
title: "Leveraging Local and Global Knowledge Integration with Time-Frequency Calibrated Distillation for Speech Enhancement"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出I²SRF-TFCKD框架，通过组内组间递归融合和时频校准蒸馏，提升低复杂度学生模型在语音增强上的性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.6</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#时频校准</span> <span class="tag-pill tag-pill-soft">#递归融合</span> <span class="tag-pill tag-pill-soft">#DPDCRN</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2506.13127</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2506.13127" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2506.13127" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出I²SRF-TFCKD框架，通过组内组间递归融合和时频校准蒸馏，提升低复杂度学生模型在语音增强上的性能。
</div>

## 👥 作者与机构

**Jiaming Cheng** ¹ · Ruiyu Liang · Ye Ni · Chao Xu · Jing Li · Wei Zhou · Rui Liu · Bj\"orn W. Schuller · … 等 1 人

**机构**：江南大学 · 帝国理工学院 · 慕尼黑工业大学 · 北京航空航天大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和知识蒸馏方向的研究者。建议重点阅读§3的蒸馏框架设计和§4的实验结果，特别是表1-3的对比和消融实验。可先看§3.2的时频交叉校准机制。

## 🌍 研究背景

语音增强中，知识蒸馏（KD）常用于压缩模型，但现有方法未充分利用语音的时频差分信息，且缺乏对局部和全局知识的协同蒸馏。之前SOTA如DPDCRN在L3DAS23挑战赛SE赛道第一，但模型复杂度高。本文旨在设计一种蒸馏策略，使低复杂度学生模型能有效学习教师模型的时频特征，同时兼顾局部聚焦和全局知识流通。

## 💡 核心创新

1. 提出组内组间递归融合框架（I²SRF），实现局部和全局知识交互
2. 设计双流时频交叉校准蒸馏，动态分配各层蒸馏权重
3. 将蒸馏策略应用于DPDCRN，在单/多通道SE上验证有效性

## 🏗️ 模型架构

输入特征（时频谱）→ 教师和学生模型均为DPDCRN（双路径扩张卷积循环网络），包含时域和频域双路径处理。蒸馏框架：① 组内蒸馏：将多层特征分组，组内教师-学生特征对匹配校准；② 组间递归融合：每组生成代表性特征，递归融合形成融合特征集，实现组间知识交互；③ 多层级交互蒸馏：基于双流时频交叉校准，分别计算时域和频域的相似性权重，交叉加权后分配各层蒸馏贡献。输出为增强后的时频谱。

## 📚 数据集

- L3DAS23 SE track dataset（训练/评估，多通道）
- DNS-Challenge dataset（训练/评估，单通道）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | L3DAS23 SE track | DPDCRN student without KD (2.85) | **I²SRF-TFCKD (3.12)** | +0.27 |
| STOI | L3DAS23 SE track | DPDCRN student without KD (0.92) | **I²SRF-TFCKD (0.94)** | +0.02 |
| PESQ | DNS-Challenge | DPDCRN student without KD (2.65) | **I²SRF-TFCKD (2.89)** | +0.24 |
| STOI | DNS-Challenge | DPDCRN student without KD (0.90) | **I²SRF-TFCKD (0.92)** | +0.02 |

在L3DAS23和DNS-Challenge数据集上，I²SRF-TFCKD相比无蒸馏学生模型在PESQ和STOI上均有提升，且优于其他蒸馏方案（如FitNet、AT、SP）。消融实验验证了组内组间递归融合和时频交叉校准的有效性。多通道实验也显示一致改进。

## 🎯 结论与影响

本文提出的I²SRF-TFCKD蒸馏框架能有效提升低复杂度SE模型的性能，通过组内组间递归融合和时频校准实现更优的知识迁移。该策略可推广至其他SE架构，对工业部署轻量级模型有参考价值。

## ⚠️ 局限与未解决问题

未报告推理延迟或参数量对比；仅在DPDCRN上验证，泛化性未知；缺乏在更多噪声类型和低信噪比下的详细分析；蒸馏框架复杂度较高，可能抵消学生模型的效率优势。

---

<div class="paper-footer"><span>评分：8.6</span><span>原始：7.6</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
