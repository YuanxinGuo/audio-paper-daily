---
title: "$C^3$ASD: Multi-Level Consistency-Driven Representation Learning"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#活动说话人检测"]
summary: "提出多级一致性驱动的活动说话人检测框架，通过嵌入级、序列级和预测级约束提升对音频/视觉/联合退化的鲁棒性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#活动说话人检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#一致性学习</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.03018</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.03018" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.03018" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多级一致性驱动的活动说话人检测框架，通过嵌入级、序列级和预测级约束提升对音频/视觉/联合退化的鲁棒性。
</div>

## 👥 作者与机构

**Jin Hong** ¹ · Jisoo Park · Junseok Kwon

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态说话人检测、鲁棒视听融合的研究者。建议重点阅读§3的多级一致性约束设计及§4的消融实验，对比不同退化条件下的性能提升。

## 🌍 研究背景

活动说话人检测（ASD）旨在判断视频中可见人物是否正在说话。现有视听融合方法在干净数据上表现良好，但在真实场景中常受背景噪声、遮挡或多模态同时退化影响。作者认为这是由于缺乏显式的一致性约束来促进跨模态鲁棒语义对齐，导致模型学习到脆弱的模态特定捷径。本文提出多级一致性框架来解决该问题。

## 💡 核心创新

1. 嵌入级跨模态一致性：对齐说话时的视听表示
2. 序列级模态内一致性：通过轨迹感知对比学习分离说话/非说话聚类
3. 预测级一致性：利用知识蒸馏稳定融合输出

## 🏗️ 模型架构

输入为视频帧和对应音频片段。音频经VGGish提取特征，视频经3D CNN提取面部特征。主干网络包含三个一致性模块：嵌入级使用对比损失对齐视听嵌入；序列级通过轨迹感知对比学习（track-aware contrastive learning）在时间维度上分离说话与非说话聚类；预测级使用教师-学生知识蒸馏稳定融合预测。最终输出每帧的说话/非说话二分类结果。

## 📚 数据集

- AVA-ActiveSpeaker（训练/评估，约3.6M帧）
- Columbia ASD（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| mAP | AVA-ActiveSpeaker (clean) | AV-FR 92.1 | **92.5** | +0.4 |
| mAP | AVA-ActiveSpeaker (audio corruption) | AV-FR 68.3 | **78.5** | +10.2 |
| mAP | AVA-ActiveSpeaker (visual corruption) | AV-FR 72.1 | **80.3** | +8.2 |
| mAP | AVA-ActiveSpeaker (joint corruption) | AV-FR 55.6 | **70.1** | +14.5 |

在AVA-ActiveSpeaker上，C3ASD在干净数据上保持竞争力（mAP 92.5 vs 92.1），在音频、视觉和联合退化条件下分别提升10.2、8.2和14.5个mAP点。在Columbia ASD上也有类似提升。消融实验验证了每个一致性模块的贡献，其中嵌入级和序列级约束对鲁棒性提升最为关键。

## 🎯 结论与影响

本文证明多级一致性约束能显著提升ASD在退化条件下的鲁棒性，同时不牺牲干净性能。该框架为鲁棒视听融合提供了新范式，未来可推广至其他多模态任务。工业上可用于视频会议、监控等场景的鲁棒说话人检测。

## ⚠️ 局限与未解决问题

未报告推理速度或参数量；仅在两个数据集上评估，泛化性待验证；退化类型为合成，真实场景效果未知；未与最新端到端方法（如基于Transformer的）对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
