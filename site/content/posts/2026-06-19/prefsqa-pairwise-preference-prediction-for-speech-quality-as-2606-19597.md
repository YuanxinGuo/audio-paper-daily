---
title: "PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音质量评估"]
summary: "提出PrefSQA，通过偏好预测替代MOS评分进行语音质量评估，并强调高质量偏好数据集的关键作用。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音质量评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#偏好预测</span> <span class="tag-pill tag-pill-soft">#MOS预测</span> <span class="tag-pill tag-pill-soft">#语音质量评估</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19597</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19597" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19597" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PrefSQA，通过偏好预测替代MOS评分进行语音质量评估，并强调高质量偏好数据集的关键作用。
</div>

## 👥 作者与机构

**Junyi Fan** ¹ · Donald S. Williamson ✉

**机构**：印第安纳大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音质量评估、主观测试研究者阅读。建议重点看§3模型设计（不确定性感知logits、损伤注意力头）和§4数据集构建与实验对比。可先看表2和表3了解性能提升。

## 🌍 研究背景

语音质量评估常用MOS分数，但MOS受评分者变异性和听测差异影响，存在标签噪声。偏好预测通过直接比较信号减少变异性，产生更干净的标签。现有方法多依赖MOS标签或合成偏好数据，缺乏对高质量偏好数据价值的系统研究。本文旨在探索无MOS的偏好预测方法，并验证高质量偏好数据集的重要性。

## 💡 核心创新

1. 提出不确定性感知logits模块
2. 设计损伤注意力头（Impairment Attention Head）
3. 引入非匹配参考比较模块
4. 构建并精炼五个偏好数据集
5. 系统验证高质量偏好数据对性能的提升

## 🏗️ 模型架构

输入为两个语音样本对，分别通过共享编码器提取特征，然后经过不确定性感知logits模块（估计每个样本的质量分布），再通过损伤注意力头聚焦于损伤区域，最后结合非匹配参考比较模块（利用不同内容参考）输出偏好预测。整体为端到端训练，输出为两个样本中哪个更优的二元判断。

## 📚 数据集

- TCD-VoIP（训练/评估，MOS衍生数据）
- NOIZEUS（训练/评估，低噪声模拟数据）
- TIMIT（训练/评估，低噪声模拟数据）
- P.808（训练/评估，人类偏好数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | TCD-VoIP | 基线方法（如MOS预测模型）约70% | **72.5%** | +2.5% |
| 准确率 | NOIZEUS | 基线方法约75% | **82.1%** | +7.1% |
| 准确率 | P.808 | 基线方法约78% | **85.3%** | +7.3% |

在MOS衍生数据集TCD-VoIP上提升较小（+2.5%），但在低噪声模拟数据集NOIZEUS和人类偏好数据集P.808上提升显著（+7.1%和+7.3%），表明高质量偏好数据对模型性能至关重要。消融实验验证了各模块的有效性，跨数据集泛化测试显示模型在未见数据上表现稳健。

## 🎯 结论与影响

PrefSQA通过偏好预测有效降低了标签噪声，在高质量偏好数据上显著优于基线。该工作强调了构建高质量偏好数据集的价值，为语音质量评估提供了新范式。未来可推动主观测试向偏好收集转变，并可能应用于其他感知质量评估任务。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；偏好数据集的构建成本较高；在MOS衍生数据上提升有限，可能受限于数据质量；未与其他偏好预测方法（如RankNet）对比；缺乏对非匹配参考比较模块的深入分析。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
