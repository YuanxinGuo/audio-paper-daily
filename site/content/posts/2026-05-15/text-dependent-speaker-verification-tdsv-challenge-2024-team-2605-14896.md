---
title: "Text-Dependent Speaker Verification (TdSV) Challenge 2024: Team Naive System Report"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人确认"]
summary: "针对TdSV挑战赛，采用ResNet-TDNN、NeXt-TDNN和EfficientNet-A0集成，在有限资源下实现低MinDCF和EER。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人确认</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本相关说话人确认</span> <span class="tag-pill tag-pill-soft">#说话人确认</span> <span class="tag-pill tag-pill-soft">#模型集成</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14896</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14896" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14896" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对TdSV挑战赛，采用ResNet-TDNN、NeXt-TDNN和EfficientNet-A0集成，在有限资源下实现低MinDCF和EER。
</div>

## 👥 作者与机构

**Amir Mohammad Rostami** ¹ · Pourya Jafarzadeh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合说话人确认领域研究者，尤其是关注挑战赛系统设计者。可重点看§3模型集成策略和§4数据增强方法。若时间有限，可跳过§2基线介绍。

## 🌍 研究背景

文本相关说话人确认（TdSV）要求同时验证说话人身份和短语内容，在金融、安防等领域有重要应用。2024年TdSV挑战赛旨在推动该技术发展。现有方法多基于深度神经网络，但挑战赛时间有限且资源受限，需要高效利用预训练模型。本文针对这一场景，探索了预训练模型微调与轻量级模型训练相结合的方案。

## 💡 核心创新

1. 采用ResNet-TDNN和NeXt-TDNN预训练模型微调
2. 设计轻量级EfficientNet-A0从头训练
3. 多模型集成策略联合说话人和短语验证

## 🏗️ 模型架构

输入为语音特征（如MFCC或滤波器组特征），主干网络包括三个分支：ResNet-TDNN和NeXt-TDNN（预训练于VoxCeleb，微调于挑战数据），以及EfficientNet-A0（从头训练）。每个分支输出说话人嵌入和短语嵌入，通过拼接或加权融合进行联合决策。最终输出为验证分数。

## 📚 数据集

- VoxCeleb（预训练ResNet-TDNN和NeXt-TDNN）
- TdSV Challenge 2024数据集（训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MinDCF | TdSV Challenge 2024评估集 | 未提供 | **0.0461** | N/A |
| EER | TdSV Challenge 2024评估集 | 未提供 | **1.3%** | N/A |

系统在TdSV挑战赛评估集上取得MinDCF 0.0461和EER 1.3%，表明多模型集成和微调策略有效。但摘要未提供与基线或其它参赛系统的对比，也未给出消融实验或跨数据集泛化结果。

## 🎯 结论与影响

本文通过集成预训练模型和轻量级模型，在TdSV挑战赛中取得优异性能，验证了多模型集成在说话人确认中的有效性。该工作为资源受限场景下的系统设计提供了参考，但缺乏与最新方法的对比，对工业落地的指导意义有限。

## ⚠️ 局限与未解决问题

摘要未提供与基线方法的对比，也未报告模型参数量、推理时间等效率指标。缺乏消融实验验证各组件贡献。仅使用单一挑战数据集，泛化性未知。未说明短语验证的具体实现细节。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
