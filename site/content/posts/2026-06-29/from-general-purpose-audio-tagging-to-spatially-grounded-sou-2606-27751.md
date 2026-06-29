---
title: "From General-Purpose Audio Tagging to Spatially Grounded Sound Event Localization and Detection"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声音事件定位与检测"]
summary: "提出AT2SELD框架，利用预训练通用音频标记模型通过多阶段神经架构搜索实现声音事件定位与检测。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声音事件定位与检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频标记</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#神经架构搜索</span> <span class="tag-pill tag-pill-soft">#迁移学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.27751</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.27751" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.27751" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AT2SELD框架，利用预训练通用音频标记模型通过多阶段神经架构搜索实现声音事件定位与检测。
</div>

## 👥 作者与机构

**Stefano Giacomelli** ¹ · Stefano Damiano · Claudia Rinaldi · Fabio Graziosi · Toon van Waterschoot

**机构**：拉奎拉大学 · 鲁汶大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合SELD和音频标记领域的研究者。重点阅读§3的NAS三阶段设计和§4的跨数据集评估。可先看§3.2关于空间编码的容量分析。

## 🌍 研究背景

声音事件定位与检测（SELD）需要同时识别事件类别和空间位置。现有方法通常从头训练，数据稀缺且计算成本高。通用音频标记（GP-AT）模型在大规模数据上预训练，但缺乏空间感知能力。本文探索如何将GP-AT模型扩展为SELD系统，通过多阶段NAS设计高效的空间-语义融合架构。

## 💡 核心创新

1. 提出AT2SELD框架，将GP-AT模型与FOA空间处理结合
2. 多阶段NAS设计，识别关键容量敏感组件
3. 晚期交叉连接融合语义与空间特征
4. 活动条件DOA监督和阈值校准策略

## 🏗️ 模型架构

输入为FOA四通道音频，提取谱FOA描述子（幅度、相位、强度向量）作为特征。主干网络采用预训练的GP-AT模型（如CNN14）作为语义编码器，同时使用早期残差空间编码模块处理空间特征。晚期通过交叉连接融合语义和空间流，随后进行逐轨SED和笛卡尔DOA估计。使用置换感知损失和活动条件DOA监督训练。

## 📚 数据集

- STARSS23（评估）
- TAU-NIGENS2021（训练/评估）
- TAU-NIGENS2020（评估）
- TAU2019（评估）

## 📊 实验结果

摘要未提供具体数值指标，但通过诊断实验分析了类别平衡、焦点损失、活动条件DOA监督和阈值校准的影响。焦点损失改善活动点，活动条件DOA监督缓解非活动目标主导，验证集阈值恢复校准。跨数据集分析显示在TAU2019上强固定源定位，TAU-NIGENS2021上可迁移表示，STARSS23上表现有意义但不确定。

## 🎯 结论与影响

GP-AT先验在空间感知架构中通过集成校准和部署优化策略，对SELD设计有前景。多阶段NAS揭示了早期残差空间编码是关键容量敏感组件，晚期交叉连接优于早期融合。该工作为利用预训练音频模型进行空间听觉任务提供了系统方法论。

## ⚠️ 局限与未解决问题

摘要未报告具体SELD指标（如F1、DOA误差），缺乏与SOTA方法的定量对比。跨数据集分析中STARSS23表现不确定，可能因域差异。未讨论推理延迟和模型参数量。NAS搜索空间可能受限，未探索更先进的时序模型如Transformer。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
