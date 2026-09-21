---
title: "Curriculum-Based Noise Adaptation for Phoneme-to-Text Reconstruction in Visual Speech Recognition"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视觉语音识别"]
summary: "提出渐进式错误课程训练PECT，用合成扰动与伪标签逐步适配NLLB音素到文本重建模型，降低视觉语音识别WER。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视觉语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#课程学习</span> <span class="tag-pill tag-pill-soft">#音素到文本重建</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.20839</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.20839" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.20839" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出渐进式错误课程训练PECT，用合成扰动与伪标签逐步适配NLLB音素到文本重建模型，降低视觉语音识别WER。
</div>

## 👥 作者与机构

**Matthew Kit Khinn Teng** ¹ · Haibo Zhang · Takeshi Saitoh

**机构**：Kyushu Institute of Technology

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视觉语音识别（VSR）与音素级后处理的研究者阅读。建议重点看课程设计的三阶段（合成扰动→多域伪标签→目标域伪标签）与消融实验，以及表2中不同前端（V-ASR/PV-ASR/HP-VSR）的泛化结果。若只关心端到端VSR可略读。

## 🌍 研究背景

音素中心的视觉语音识别先预测音素再重建句子，整体性能高度依赖音素到文本重建模型的鲁棒性。现有重建方法多在干净音素序列或人工合成损坏输入上训练，与推理时视觉识别器产生的真实音素预测错误存在分布不匹配，导致重建精度下降。本文针对这一训练-推理失配问题，提出渐进式课程训练来缩小差距。

## 💡 核心创新

1. 提出PECT渐进式错误课程训练框架
2. 三阶段课程：合成扰动→多域伪标签→目标域伪标签
3. 基于NLLB的重建模型适配真实音素错误
4. 跨多种VSR前端验证通用性

## 🏗️ 模型架构

输入为视觉语音识别前端输出的音素序列（含预测错误），主干为基于NLLB的序列到序列音素到文本重建模型。训练采用三阶段课程：先用合成音素扰动构造受控错误，再引入多域伪标签扩大错误分布，最后用目标域视觉识别器生成的伪标签逼近真实推理错误分布，逐步提升错误强度。输出为重建的文本句子。摘要未给出参数量。

## 📚 数据集

- LRS2（训练/评估）
- LRS3（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LRS2 | HP-VSR-FiLMFuse (L4) 23.3% | **22.2%** | -1.1% |
| WER | LRS3 | HP-VSR-ResFiLM 30.3% | **29.7%** | -0.6% |

在LRS2与LRS3上，PECT对V-ASR、PV-ASR、HP-VSR多种前端均带来一致提升，HP-VSR-FiLMFuse(L4)在LRS2上WER从23.3%降至22.2%，HP-VSR-ResFiLM在LRS3上从30.3%降至29.7%。消融与定性分析表明渐进适配真实音素错误有效，但摘要未报告推理延迟或参数量等效率指标。

## 🎯 结论与影响

PECT证明课程式渐进适配真实音素预测错误可稳定提升音素中心VSR的句子重建精度，且对多种前端通用。该思路可推广到其他依赖中间符号预测的两阶段识别系统，对工业级VSR后处理模块的鲁棒化有参考价值。

## ⚠️ 局限与未解决问题

提升幅度较小（LRS2约1.1%、LRS3约0.6%），未报告推理开销与训练成本；伪标签质量依赖前端识别器，存在误差累积风险；仅在LRS2/LRS3两个英语唇读基准验证，跨语言与噪声场景泛化未知。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
