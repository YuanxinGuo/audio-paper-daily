---
title: "EigeNet: Geometry-Informed Multi-Modal Learning for Few-shot Novel View RIR Prediction"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#房间冲激响应生成"]
summary: "提出EigeNet，利用几何信息引导的多模态框架，从稀疏观测中预测新视角的房间冲激响应，在少样本和模拟到真实场景中达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#房间冲激响应生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态学习</span> <span class="tag-pill tag-pill-soft">#少样本学习</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28101</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/FEAfeatherTHER/EigeNet" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">FEAfeatherTHER/EigeNet</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28101" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28101" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/FEAfeatherTHER/EigeNet" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出EigeNet，利用几何信息引导的多模态框架，从稀疏观测中预测新视角的房间冲激响应，在少样本和模拟到真实场景中达到SOTA。
</div>

## 👥 作者与机构

**Chong Jing** ¹ · Zitong Lan · Junan Zhang · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事空间音频、声学模拟、RIR预测的研究者阅读。建议重点阅读第3节方法部分（Cross-view Alternate-attention Transformer和几何调制模块）以及第4节实验（表1-3的对比结果）。可先看§3.2与表2。

## 🌍 研究背景

在沉浸式空间音频渲染中，从稀疏观测预测空间变化的房间冲激响应（RIR）是关键逆问题。现有方法依赖密集采样或先验几何，难以在少样本下泛化。本文提出EigeNet，利用多视角多模态信息（如音频、几何特征）进行时空推理，旨在解决少样本新视角RIR预测的挑战。

## 💡 核心创新

1. Cross-view Alternate-attention Transformer：交替细化帧内声学结构与帧间空间关系
2. 几何调制模块：基于声线追踪，将几何特征与RIR功率谱关联
3. 辅助损失：将单目标波形预测转为多任务学习，提升泛化性

## 🏗️ 模型架构

输入为稀疏多视角观测的音频和几何特征。主干网络采用Cross-view Alternate-attention Transformer，包含交替的帧内自注意力和帧间交叉注意力，以建模局部声学结构和全局空间关系。几何调制模块将几何特征（如房间尺寸、声源位置）通过调制机制注入到RIR功率谱预测中。输出为预测的RIR波形。参数量未提及。

## 📚 数据集

- 模拟数据集（训练/评估，包含多种房间几何和声源位置）
- 真实世界基准（评估，用于sim-to-real泛化测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| L1误差 | 模拟数据集 | NeuralRIR 0.12 | **0.09** | -0.03 |
| L1误差 | 真实世界基准 | NeuralRIR 0.18 | **0.14** | -0.04 |

在模拟和真实基准上，EigeNet在少样本新视角RIR预测任务中均达到SOTA，L1误差分别降低0.03和0.04。消融实验表明几何调制模块和辅助损失在不同骨干网络下均带来一致提升，验证了其架构无关的泛化性。

## 🎯 结论与影响

EigeNet通过几何信息引导的多模态学习，在少样本RIR预测中取得显著改进，证明了结合几何先验和注意力机制的有效性。该工作为空间音频渲染中的声场重建提供了新思路，有望推动虚拟现实和增强现实中的沉浸式音频应用。

## ⚠️ 局限与未解决问题

论文未报告推理延迟和模型参数量，实际部署效率未知。实验仅在有限房间几何和声源配置下进行，对复杂场景（如移动声源、非刚性边界）的泛化性未验证。辅助损失的贡献未与更复杂的多任务设计对比。

## 🔗 开源资源

- **代码**：<https://github.com/FEAfeatherTHER/EigeNet>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
