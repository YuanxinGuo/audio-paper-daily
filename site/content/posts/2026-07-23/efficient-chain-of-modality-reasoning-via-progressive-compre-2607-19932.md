---
title: "Efficient Chain-of-Modality Reasoning via Progressive Compression for Spoken Language Models"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音语言模型推理"]
summary: "提出ECoM推理框架，通过渐进式压缩将文本推理融入口语语言模型，在口语数学问答上提升准确率并减少token开销。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音语言模型推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#链式推理</span> <span class="tag-pill tag-pill-soft">#模态压缩</span> <span class="tag-pill tag-pill-soft">#口语数学问答</span> <span class="tag-pill tag-pill-soft">#课程学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.19932</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.19932" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.19932" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ECoM推理框架，通过渐进式压缩将文本推理融入口语语言模型，在口语数学问答上提升准确率并减少token开销。
</div>

## 👥 作者与机构

**Pengchao Feng** ¹ · Chao-Hong Tan · Qian Chen · Wen Wang · Xiangang Li · Xie Chen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事口语语言模型、多模态推理的研究者阅读。建议重点读§3的ECoM架构和§4的渐进式压缩策略，以及表1的对比结果。可先看§3.2的压缩推理模块。

## 🌍 研究背景

口语语言模型（SLM）在口语数学问答任务上推理能力弱于文本大模型，主要原因是SLM需处理难以解释的口语化数学表达式。直接迁移文本推理受限于架构和计算开销。现有链式模态（CoM）方法先生成中间文本再生成语音，但token预算大。本文旨在通过压缩文本推理表示，在保持推理准确性的同时提高推理效率。

## 💡 核心创新

1. 提出ECoM推理框架，首次将压缩推理引入SLM
2. 设计渐进式压缩策略，从完整推理逐步过渡到压缩推理
3. 压缩文本组件同时作为语音引导和推理表示，减少token预算
4. 在口语数学问答基准上实现21%准确率提升，仅用40%文本token

## 🏗️ 模型架构

输入口语数学问题音频，经语音编码器提取特征。主干网络为预训练SLM（如HuBERT+LLM）。关键模块：压缩推理模块将文本推理压缩为紧凑表示，通过交叉注意力注入SLM解码器。输出为语音答案。渐进式压缩训练分阶段：先训练完整文本推理，再逐步压缩文本长度，最终实现高效推理。

## 📚 数据集

- Spoken MathQA（训练/评估，口语数学问答基准）
- LibriSpeech（可能用于预训练，未明确）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | Spoken MathQA | 标准CoM无显式推理（假设值） | **ECoM推理** | +21% |
| 准确率 | Spoken MathQA | CoM完整推理轨迹 | **ECoM推理** | +3% |
| 文本token数 | Spoken MathQA | CoM完整推理轨迹（100%） | **ECoM推理（40%）** | -60% |

ECoM推理在口语数学问答基准上相比标准CoM无显式推理提升21%准确率，相比CoM完整推理轨迹提升3%准确率，同时仅使用40%的文本token，验证了压缩推理的有效性和效率优势。

## 🎯 结论与影响

ECoM推理框架通过渐进式压缩将文本推理高效融入SLM，显著提升口语数学问答准确率并降低推理开销。该工作为SLM的推理能力增强提供了新范式，有望推动口语交互系统的智能化。工业上可应用于语音助手、教育辅导等场景。

## ⚠️ 局限与未解决问题

实验仅在口语数学问答任务上验证，泛化性未知；未报告推理延迟或模型参数量；渐进式压缩策略的收敛性分析不足；对比基线未包含最新SLM方法。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
