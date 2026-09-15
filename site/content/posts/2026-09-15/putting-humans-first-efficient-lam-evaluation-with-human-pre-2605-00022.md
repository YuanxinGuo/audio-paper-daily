---
title: "Putting HUMANS first: Efficient LAM Evaluation with Human Preference Alignment"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频评测基准"]
summary: "研究用50条样本子集替代完整基准评测大音频模型，与全量分数相关性达0.93，并开源HUMANS基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频评测基准</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频模型评测</span> <span class="tag-pill tag-pill-soft">#子集选择</span> <span class="tag-pill tag-pill-soft">#人类偏好对齐</span> <span class="tag-pill tag-pill-soft">#语音助手</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.00022</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.00022" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.00022" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究用50条样本子集替代完整基准评测大音频模型，与全量分数相关性达0.93，并开源HUMANS基准。
</div>

## 👥 作者与机构

**Woody Haosheng Gan** ¹ · William Held · Diyi Yang

**机构**：斯坦福大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大模型评测、语音助手产品评估的研究者与工程团队阅读。建议重点看子集选择方法对比（10种方法）与人类偏好回归建模两节，以及相关性表格。若只关心语音增强/分离方法本身，可略读。

## 🌍 研究背景

大音频模型（LAM）数量激增，但完整基准评测成本高、数据冗余大。此前评测依赖全量 benchmark（如音频理解、语音任务集合），缺乏高效代理指标；同时基准分数与用户真实满意度是否一致尚不清楚。本文要解决两个问题：能否用极小子集可靠复现全量基准分数，以及这些分数能否预测人类偏好。

## 💡 核心创新

1. 系统对比10种子集选择方法，覆盖18个模型40个任务
2. 证明50条样本（0.3%数据）即可达0.93 Pearson相关
3. 在子集上训练回归模型预测人类偏好，相关达0.98
4. 开源HUMANS回归加权子集基准

## 🏗️ 模型架构

方法分两阶段：第一阶段对40个任务、18个LAM的完整评测分数矩阵，应用10种子集选择策略（含随机、聚类、回归加权等）挑选最小样本子集，以Pearson相关衡量子集分数与全量分数一致性；第二阶段收集776条真实语音助手对话的人类偏好评分，在选定子集上训练回归模型预测偏好，并与随机子集、全量基准训练的回归模型对比。输出为HUMANS子集及回归权重。

## 📚 数据集

- 40个LAM评测任务（子集选择分析，18个音频模型）
- 776条真实语音助手对话人类偏好评分（偏好预测训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Pearson correlation | 40任务全量基准 | 全量基准 1.00（参考） | **50样本子集 0.93** | 0.3%数据达0.93 |
| Pearson correlation | 人类偏好评分 | 全量基准 0.85 | **子集回归模型 0.98** | +0.13 |

摘要给出两组关键数字：50条样本子集与全量基准分数相关0.93；子集与全量基准对人类偏好相关均为0.85；在选定子集上训练的回归模型对人类偏好相关达0.98，优于随机子集和全量基准训练的回归模型。未提供消融细节、推理成本或跨模型泛化数据。

## 🎯 结论与影响

最强结论是精心挑选的小子集在回归建模中可超越全量基准预测人类偏好，体现质量优于数量。该工作为LAM高效评测提供可复用代理基准，可能推动评测从堆数据转向精选样本，对语音助手产品迭代有降本意义。

## ⚠️ 局限与未解决问题

人类偏好数据仅776条，规模偏小且来源单一，泛化性存疑；未报告子集选择与回归推理的计算开销；40任务覆盖是否代表全部LAM能力未验证；缺少与已有高效评测基准的直接对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
