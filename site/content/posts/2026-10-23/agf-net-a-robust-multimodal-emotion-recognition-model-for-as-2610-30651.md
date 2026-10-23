---
title: "AGF-Net: A Robust Multimodal Emotion Recognition Model for Asynchronous Audio-Visual Signals Based on Predictive Dynamic Fusion with Negative Learning"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态情感识别"]
summary: "提出AGF-Net，用音频引导融合、多模态负学习与预测动态融合，在自动分段与含噪音视频下做情感识别。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频情感识别</span> <span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#负学习</span> <span class="tag-pill tag-pill-soft">#自动语音分段</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.30651</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.30651" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.30651" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AGF-Net，用音频引导融合、多模态负学习与预测动态融合，在自动分段与含噪音视频下做情感识别。
</div>

## 👥 作者与机构

**Chuan Han Li** ¹ · Yun Chien Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态情感识别与音视频融合的研究者阅读。建议重点看§3的AGF与PDF模块设计及负学习的损失形式，表2/表3的噪声鲁棒性对比值得细读；若只关心语音增强/分离可跳过。可复现其自动分段流程作为数据预处理参考。

## 🌍 研究背景

音视频情感识别此前多依赖人工标注的话语边界，并以早期/晚期融合拼接音频与视觉特征，代表工作多在IEMOCAP等基准上报告结果。痛点有二：一是人工边界在真实连续对话中不可得，自动分段会引入错位与噪声；二是模态质量不均衡时简单融合易被劣质模态拖累。本文要在自动分段与含噪条件下保持融合鲁棒性。

## 💡 核心创新

1. Audio-Guided Fusion：用音频特征引导视觉分支的跨模态融合
2. Multimodal Negative Learning：以负学习缓解模态不均衡
3. Predictive Dynamic Fusion：按模态质量动态加权融合
4. 自动话语分段替代人工边界标注

## 🏗️ 模型架构

输入为连续对话经自动分段得到的候选片段，分别提取音频声学特征与视觉帧级特征；主干为双流编码器，音频流经Audio-Guided Fusion向视觉流注入引导信息完成跨模态对齐，融合层采用Predictive Dynamic Fusion按各模态可靠性预测动态权重，训练时叠加Multimodal Negative Learning约束模态平衡，最终经分类头输出情感类别。摘要未给出参数量与具体骨干网络名。

## 📚 数据集

- 音视频情感对话数据集（评估，摘要未具名）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 干净条件（摘要未具名） | 未给出 | **64.92%** | — |
| F1-score | 干净条件（摘要未具名） | 未给出 | **65.47%** | — |
| Accuracy | 中等噪声条件 | 未给出 | **62.13%** | — |
| Accuracy | 较高噪声条件 | 未给出 | **58.19%** | — |

摘要仅报告自身绝对指标：干净条件64.92% Acc/65.47% F1，中等噪声62.13%/63.08%，高噪声58.19%/59.41%，显示随噪声增强性能平缓下降。未给出与人工分段基线或其他融合方法的对比数值，也未报告消融实验，故改进幅度无法量化评估。

## 🎯 结论与影响

最强结论是自动分段加动态融合可在噪声下维持较稳的情感识别性能，降低对人工边界的依赖。对多模态情感识别后续研究的潜在影响在于把分段误差纳入融合鲁棒性建模；工业上可用于客服通话等连续对话的自动情感分析，但需补足与强基线的对比。

## ⚠️ 局限与未解决问题

缺少与人工分段及主流融合方法的定量对比，无消融验证AGF/MNL/PDF各自贡献；数据集与噪声注入方式未说明，泛化性存疑；未报告推理延迟与参数量，自动分段错误传播的影响也未分析。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
