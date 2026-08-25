---
title: "An Automated Pipeline for Few-Shot Bird Call Classification: A Case Study with the Tooth-Billed Pigeon"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "提出一种自动化少样本鸟鸣分类流程，利用大型分类网络的嵌入空间和余弦相似度，成功检测极危物种齿嘴鸠的叫声。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#少样本分类</span> <span class="tag-pill tag-pill-soft">#鸟鸣识别</span> <span class="tag-pill tag-pill-soft">#嵌入空间</span> <span class="tag-pill tag-pill-soft">#濒危物种</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2504.16276</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2504.16276" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2504.16276" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种自动化少样本鸟鸣分类流程，利用大型分类网络的嵌入空间和余弦相似度，成功检测极危物种齿嘴鸠的叫声。
</div>

## 👥 作者与机构

**Abhishek Jana** ¹ · Moeumu Uili · James Atherton · Mark O'Brien · Joe Wood · Leandra Brickson

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事生物声学、少样本分类或保护监测的研究者。建议重点阅读方法部分（§3）和实验部分（§4），特别是嵌入空间选择和预处理步骤。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

大型鸟鸣分类器如BirdNET和Perch对常见鸟类检测效果好，但缺乏对仅有1-3条录音的稀有物种的支持，这对监测濒危物种至关重要。现有方法需要大量训练数据，无法应对极稀有物种。本文旨在利用大型网络的嵌入空间，通过余弦相似度分类器，在极少样本下实现有效检测，并以齿嘴鸠为案例验证。

## 💡 核心创新

1. 利用大型分类网络嵌入空间进行少样本分类
2. 结合滤波和去噪预处理优化检测
3. 针对极稀有物种（仅3条录音）的自动化流程
4. 在真实场景中验证，达到实用水平
5. 开源系统，便于保护工作者使用

## 🏗️ 模型架构

输入音频经过预处理（滤波、去噪）后，送入大型鸟鸣分类网络（如BirdNET或Perch）提取嵌入向量。然后计算嵌入向量与目标物种参考嵌入的余弦相似度，设定阈值进行分类。流程包含人工质量控制步骤，确保数据质量。

## 📚 数据集

- Xeno-Canto（模拟场景评估）
- 齿嘴鸠录音（真实测试，3条确认录音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Recall | 齿嘴鸠真实测试 | 无 | **1.0** | N/A |
| Accuracy | 齿嘴鸠真实测试 | 无 | **0.95** | N/A |

在模拟场景中评估了不同嵌入空间，使用聚类指标选择最佳嵌入。在真实齿嘴鸠测试中，模型达到1.0召回率和0.95准确率，表明其实际可用性。实验还验证了预处理步骤的有效性，但未提供与其他少样本方法的对比。

## 🎯 结论与影响

本文提出的自动化少样本鸟鸣分类流程成功应用于极危物种齿嘴鸠，达到实用水平。该方法为保护工作者提供了监测稀有物种的工具，并展示了利用大型网络嵌入空间进行少样本分类的潜力。未来可扩展到其他稀有物种，促进生物声学监测。

## ⚠️ 局限与未解决问题

未与其他少样本学习方法对比，缺乏消融实验。测试数据仅来自单一物种，泛化性未知。依赖大型网络的嵌入质量，可能对域偏移敏感。未报告推理延迟和计算资源需求。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
