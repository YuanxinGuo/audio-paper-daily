---
title: "Hybrid acoustic and pretrained embedding feature fusion for unmanned aerial vehicle detection using stacking ensemble learning under a leakage-aware evaluation protocol"
date: 2026-11-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学场景分类"]
summary: "在源不重叠协议下，融合手工声学特征与YAMNet嵌入，用堆叠集成实现无人机二分类检测。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学场景分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#无人机检测</span> <span class="tag-pill tag-pill-soft">#声学事件检测</span> <span class="tag-pill tag-pill-soft">#特征融合</span> <span class="tag-pill tag-pill-soft">#集成学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.04714</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.04714" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.04714" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在源不重叠协议下，融合手工声学特征与YAMNet嵌入，用堆叠集成实现无人机二分类检测。
</div>

## 👥 作者与机构

**Zahid Iqbal** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做声学事件检测/无人机侦测的工程研究者与数据集评测方法学关注者。若只关心模型结构可略读；重点看§3的数据泄漏分析与分组协议设计、表2的随机划分vs分组划分对比、以及特征选择消融。可执行动作：先看分组协议定义与15折结果方差，再看YAMNet融合增益的逐折统计。

## 🌍 研究背景

小型多旋翼无人机的声学特征可用于低成本麦克风检测，公开DroneAudioDataset上此前报告的高准确率多基于随机片段级划分。但该数据集仅由7段录音切出的257个5秒块构成无人机类，非无人机类96.4%来自ESC-50，同一源片段可能同时出现在训练与测试中，造成数据泄漏与精度虚高。本文要解决的是：在源不重叠的严格评测协议下，重新评估该任务，并考察手工声学描述子与预训练嵌入融合是否带来真实增益。

## 💡 核心创新

1. 提出源不重叠的五折三次重复分组评测协议，量化随机划分的精度虚高
2. 融合57维手工声学描述子与1024维YAMNet嵌入的双视图特征
3. 采用mRMR+ReliefF混合与NSGA-II多目标两种特征选择策略对比
4. Random Forest与XGBoost双视图堆叠集成

## 🏗️ 模型架构

输入为1秒音频片段。两路特征：一路提取57个手工声学描述子，经混合mRMR与ReliefF选择或NSGA-II多目标搜索降维至16~18维（NSGA-II保留4~6维）；另一路用预训练YAMNet输出1024维嵌入。两视图分别训练Random Forest与XGBoost基学习器，再以stacking集成融合两视图预测，输出无人机/非无人机二分类概率。单片段推理在单CPU线程上耗时51.0 ms。

## 📚 数据集

- DroneAudioDataset（训练与评估，11,704个1秒片段，无人机类1,332条来自7段录音的257个5秒块）
- ESC-50（非无人机类来源，2,000条片段，其中98.78%作为未见源测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | DroneAudioDataset（分组协议，15测试折） | 随机划分四模型（虚高1.89~3.22点） | **95.29%（SD 1.62）** | 随机划分高估1.89~3.22点 |
| Specificity | DroneAudioDataset（分组协议） | 未给出 | **98.29%** | — |
| AUC | DroneAudioDataset（分组协议） | 未给出 | **0.990** | — |
| Accuracy | 未见ESC-50源片段 | 未给出 | **98.78%正确判为非无人机** | — |
| Accuracy | DroneAudioDataset（分组协议） | 仅手工特征视图 | **加入YAMNet嵌入** | +1.11点（12/15折更高） |

分组协议下双视图堆叠平均准确率95.29%，特异度98.29%，AUC 0.990，对未见ESC-50源片段98.78%正确判为非无人机。随机划分使四个模型准确率虚高1.89~3.22点。加入YAMNet嵌入提升1.11点且在12/15折更优。混合特征选择用16~18个特征即达到全部44个基线描述子的精度，NSGA-II仅保留4~6特征但精度下降。推理51.0 ms/片段。

## 🎯 结论与影响

最强结论是：该数据集上随机划分会系统性高估性能，源不重叠评测是公平基准的必要条件；手工描述子与预训练嵌入融合带来小而一致的增益。这为后续无人机声学检测的基准设定提供方法学参考，也提示工业部署需按录音源划分评估，避免乐观估计。

## ⚠️ 局限与未解决问题

仅单一数据集、单一预训练模型YAMNet，未与端到端CNN/Transformer声学模型对比；增益仅1.11点且方差较大，统计显著性未检验；未报告推理延迟在嵌入式端的实测；非无人机类高度依赖ESC-50，类别分布偏差仍存。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-04/">← 返回 2026-11-04 速递</a></div>
