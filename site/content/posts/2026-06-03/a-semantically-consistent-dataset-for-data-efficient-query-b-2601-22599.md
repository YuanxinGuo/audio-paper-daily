---
title: "A Semantically Consistent Dataset for Data-Efficient Query-Based Universal Sound Separation"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#通用音频分离"]
summary: "提出语义一致合成协议构建高质量数据集Hive，使小模型在查询基通用音频分离上达到与大数据训练SOTA相当的精度。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#通用音频分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#查询基音频分离</span> <span class="tag-pill tag-pill-soft">#数据效率</span> <span class="tag-pill tag-pill-soft">#语义一致性</span> <span class="tag-pill tag-pill-soft">#合成数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.22599</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://cslikai.cn/Hive" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">cslikai.cn/Hive</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.22599" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.22599" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://cslikai.cn/Hive" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出语义一致合成协议构建高质量数据集Hive，使小模型在查询基通用音频分离上达到与大数据训练SOTA相当的精度。
</div>

## 👥 作者与机构

**Kai Li** ¹ · Jintao Cheng · Chang Zeng · Zijun Yan · Helin Wang · Zixiong Su · Bo Zheng · Xiaolin Hu

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频分离、数据增强方向研究者。重点读§3合成协议与§4实验，特别是表2与图3的零样本泛化结果。可复现其数据生成流程。

## 🌍 研究背景

查询基通用音频分离旨在从混合音频中分离出指定类别的声源，但现有方法在复杂声学场景中残留干扰严重。根本原因是野外数据集存在弱标签与事件共现问题，导致模型学习到背景噪声与目标类别的虚假关联。此前SOTA如SAM-Audio依赖海量数据（~500倍于Hive）训练，数据效率低。本文旨在通过构建纯净监督信号解决数据瓶颈。

## 💡 核心创新

1. 提出语义一致合成协议消除事件共现
2. 构建2.4k小时高质量合成数据集Hive
3. 证明监督信号纯度可大幅提升数据效率
4. 实现小模型零样本泛化超越大数据模型

## 🏗️ 模型架构

输入混合音频→特征提取（预训练音频编码器）→查询编码器（目标类别embedding）→分离网络（基于Transformer的U-Net结构，含交叉注意力融合查询与混合特征）→输出分离音频。模型参数量未明确给出，但提及为开源模型（如ResUNet等）。

## 📚 数据集

- Hive（训练，2.4k小时，合成数据）
- Audioset（评估，野外数据）
- FSD50K（评估，零样本泛化）
- ESC-50（评估，零样本泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 分离精度（mAP） | Audioset | SAM-Audio（大数据） | **Hive训练模型（小数据）** | 竞争性（具体数值未给出） |
| 感知质量（MOS） | Audioset | SAM-Audio | **Hive训练模型** | 竞争性 |

实验表明，在Audioset上，基于Hive训练的开源模型（数据量仅为SAM-Audio的1/500）达到了与SAM-Audio竞争的分离精度和感知质量。在FSD50K和ESC-50零样本评估中，Hive训练模型表现出显著的泛化能力，优于其他小数据方法。消融实验验证了语义一致合成协议的有效性。

## 🎯 结论与影响

本文证明监督信号纯度比数据规模更重要，通过语义一致合成协议构建的Hive数据集使小模型达到大数据SOTA性能。该工作为训练鲁棒音频基础模型提供了数据高效的新范式，有望降低工业部署的计算成本。

## ⚠️ 局限与未解决问题

Hive为合成数据，与真实场景存在域差异；仅验证了开源模型，未探索更大规模模型；未报告推理延迟与计算开销；零样本泛化仅在有限类别上测试。

## 🔗 开源资源

- **代码**：<https://cslikai.cn/Hive>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
