---
title: "Controllable Dysarthric Speech Synthesis with Patient-Specific Conditioning for Speaker-Diverse ASR Augmentation"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用可学习病理前缀与音色前缀解耦，基于LoRA微调的codec语言模型合成构音障碍语音，用于ASR数据增强。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#病理语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.08696</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.08696" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.08696" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用可学习病理前缀与音色前缀解耦，基于LoRA微调的codec语言模型合成构音障碍语音，用于ASR数据增强。
</div>

## 👥 作者与机构

**Haoshen Wang** ¹ · Xueli Zhong · Bingbing Lin · Jia Huang · Xingduo Pan · Shengxiang Liang · Nizhuan Wang · Wai Ting Siok

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做病理语音识别、低资源ASR数据增强的研究者阅读。建议重点看 §3 前缀解耦机制与双分类器+梯度反转设计，以及表 2 的 TORGO 上真实/合成数据混合实验。若只关心通用 TTS 可略读。

## 🌍 研究背景

构音障碍语音识别受限于说话人差异大、标注数据稀缺。此前主流做法是用 TTS 或 voice conversion 合成病理语音做数据增强，但往往把说话人身份与病理发音耦合在一起，无法独立控制病理程度，也难以把病理特征迁移到不同说话人（含健康人）。本文要解决的核心问题是：如何将病理发音与说话人音色解耦，实现可控、说话人多样的构音障碍语音合成以增强 ASR。

## 💡 核心创新

1. 可学习患者特异性病理前缀与提示音色前缀分离
2. 加性条件融合双前缀，基于 LoRA 适配 codec 语言模型
3. 双分类器+梯度反转促进病理/音色因子解耦
4. 基于语音转换的反事实增强提升说话人多样性

## 🏗️ 模型架构

输入为文本与提示语音，经预训练 neural codec 语言模型提取离散 token。主干为冻结的 codec LM，通过 LoRA 低秩适配微调。关键模块包括：由提示导出的音色前缀、可学习的患者特异性病理前缀，二者以加性条件方式注入 LM 隐层；训练时叠加双分类器目标，并用梯度反转层迫使隐表示分离病理与说话人因子；推理时可将病理前缀与任意目标说话人（含健康人）配对生成。输出为 codec token 解码后的波形。

## 📚 数据集

- TORGO（训练与评估，构音障碍语音语料）

## 📊 实验结果

摘要未给出具体 SI-SDR / WER / PESQ 数值，仅定性说明：生成语音可部分替代真实构音障碍训练数据；与真实数据结合时提供有效的说话人多样增强。客观 ASR、感知、因子分离与音素级分析显示目标说话人音色得以保留，且病理模式与真实构音障碍语音一致。

## 🎯 结论与影响

最强结论是病理前缀与音色前缀的解耦使合成语音可跨说话人迁移并部分替代真实数据。这为低资源病理 ASR 增强提供了可控合成范式，后续可扩展到其他病理语音或跨语言场景。工业上可降低病理语音数据采集与标注成本，但需验证真实临床部署的鲁棒性。

## ⚠️ 局限与未解决问题

仅在 TORGO 单一数据集验证，规模小、说话人少，泛化性存疑；摘要未报 WER 等具体数值与推理延迟；缺少与 SEPFormer 类增强基线或扩散 TTS 的定量对比；因子解耦的定量指标与消融细节未在摘要呈现。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
