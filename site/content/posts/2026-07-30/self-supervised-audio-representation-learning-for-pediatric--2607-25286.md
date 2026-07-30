---
title: "Self-Supervised Audio Representation Learning for Pediatric Asthma Detection in Emergency Care Using Digital Stethoscope Recordings"
date: 2026-07-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "利用预训练自监督语音模型（HuBERT、WavLM、Wav2Vec 2.0）提取特征，结合传统分类器检测儿童哮喘，在31名患者的小样本上取得0.84准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#音频表示学习</span> <span class="tag-pill tag-pill-soft">#医学诊断</span> <span class="tag-pill tag-pill-soft">#呼吸音分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25286</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25286" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25286" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用预训练自监督语音模型（HuBERT、WavLM、Wav2Vec 2.0）提取特征，结合传统分类器检测儿童哮喘，在31名患者的小样本上取得0.84准确率。
</div>

## 👥 作者与机构

**Fatemeh Bagheri** ¹ · Thalia Pandolfi · Ervin Sejdic · Rohit Mohindra

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对医学音频分析或自监督表示学习迁移应用感兴趣的读者。可重点阅读§3方法部分和§4实验结果，但需注意数据集规模极小，结论泛化性有限。

## 🌍 研究背景

儿童哮喘在急诊科诊断困难，因症状重叠、时间紧迫且肺功能测试难以实施。现有方法依赖临床判断或复杂设备。自监督语音模型在呼吸音分析中尚未充分探索。本文旨在验证利用预训练自监督音频表示（HuBERT、WavLM、Wav2Vec 2.0）进行儿童哮喘检测的可行性，以提供非侵入性辅助诊断手段。

## 💡 核心创新

1. 首次将自监督语音模型用于儿童哮喘检测
2. 融合患者年龄和性别信息到特征表示
3. 采用两种交叉验证策略评估泛化性

## 🏗️ 模型架构

输入为30秒呼吸音录音，从6个胸部位置采集。使用预训练的HuBERT、WavLM或Wav2Vec 2.0模型提取特征，并将患者年龄和性别作为额外特征拼接。随后训练传统机器学习分类器（如直方图梯度提升），输出哮喘/非哮喘二分类结果。

## 📚 数据集

- 自采集数据集（31名儿童，10哮喘/21非哮喘，6个胸部位置，30秒录音，用于训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | 自采集数据集 | 未明确基线 | **0.84** | N/A |
| 敏感性 | 自采集数据集 | 未明确基线 | **0.80** | N/A |
| 特异性 | 自采集数据集 | 未明确基线 | **0.86** | N/A |
| F1分数 | 自采集数据集 | 未明确基线 | **0.76** | N/A |

Wav2Vec 2.0结合直方图梯度提升在两种验证策略（分层5折交叉验证和留一患者交叉验证）下均表现最佳，准确率0.84，敏感性0.80，特异性0.86，F1分数0.76。性能一致性表明模型对未见患者有良好泛化潜力。但未与专用呼吸音模型或传统声学特征对比。

## 🎯 结论与影响

预训练自监督音频表示（特别是Wav2Vec 2.0）在儿童哮喘检测中展现出潜力，提供了一种非侵入性辅助诊断方法。该方向后续可探索更大规模数据集、端到端微调以及与其他临床指标融合。对工业落地而言，需考虑实时性和设备兼容性。

## ⚠️ 局限与未解决问题

数据集仅31名患者，样本量极小，且类别不平衡（10哮喘/21非哮喘）。未与专用呼吸音特征或端到端深度学习模型对比。未报告模型参数量或推理延迟。未进行跨数据集验证。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-30/">← 返回 2026-07-30 速递</a></div>
