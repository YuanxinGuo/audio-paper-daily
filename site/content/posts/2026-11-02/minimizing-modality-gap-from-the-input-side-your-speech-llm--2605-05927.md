---
title: "Minimizing Modality Gap from the Input Side: Your Speech LLM Can Be a Prosody-Aware Text LLM"
date: 2026-11-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音大语言模型"]
summary: "提出 TextPro-SLM，用 WhisperPro 编码器同步输出文本 token 与韵律嵌入，从输入端缩小语音-文本模态鸿沟。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音大语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音大语言模型</span> <span class="tag-pill tag-pill-soft">#模态鸿沟</span> <span class="tag-pill tag-pill-soft">#副语言理解</span> <span class="tag-pill tag-pill-soft">#语音编码器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.05927</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/dreamtheater123/TextPro-SLM" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">dreamtheater123/TextPro-SLM</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.05927" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.05927" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/dreamtheater123/TextPro-SLM" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 TextPro-SLM，用 WhisperPro 编码器同步输出文本 token 与韵律嵌入，从输入端缩小语音-文本模态鸿沟。
</div>

## 👥 作者与机构

**Wenqian Cui** ¹ · Xiao-Hui Li · Daxin Tan · Qiyong Zheng · Irwin King

**机构**：香港中文大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 speech LLM、语音-文本对齐与副语言理解的研究者阅读。建议通读，重点看 §3 的 WhisperPro 编码器设计与模态鸿沟度量方法，以及表 2/表 3 中 3B 与 7B 规模的对比；若只关心结论，看摘要与实验节即可。

## 🌍 研究背景

Speech LLM 通常以文本 LLM 检查点为初始化，但语音与文本表示之间仍存在显著模态鸿沟，导致副语言信息丢失与语义能力退化。此前工作多从输出端入手，让语音生成更接近文本形式，但鸿沟依旧。作者认为剩余瓶颈在输入端：语音输入与文本 LLM 的输入分布差异过大，因此需要让语音输入更像一个具备韵律感知的文本 LLM 的输入。

## 💡 核心创新

1. WhisperPro 统一编码器同步产出文本 token 与韵律嵌入
2. 从输入端而非输出端缩小模态鸿沟的思路
3. 保留原 TLM 语义能力的同时学习副语言理解
4. 仅约 1000 小时训练音频即达低模态鸿沟

## 🏗️ 模型架构

输入语音先经 WhisperPro 统一语音编码器，该编码器同时产生与语音时间对齐的文本 token 序列和韵律嵌入（prosody embeddings）；两类表示送入 LLM 主干，主干由文本 LLM 检查点初始化，训练目标在保留原 TLM 语义能力的同时学习副语言理解。输出为文本形式的下游预测。摘要未给出具体参数量，仅在 3B 与 7B 两个规模上验证。

## 📚 数据集

- LLM 训练音频（训练，约 1000 小时）
- 副语言理解评测任务（评估）

## 📊 实验结果

摘要仅给出定性结论：在 3B 与 7B 两个规模上，TextPro-SLM 取得领先 SLM 中最低的模态鸿沟，同时在副语言理解任务上整体表现强劲，且仅用约 1000 小时 LLM 训练音频。摘要未披露具体指标数值、基线名称与测试集规模，故无法列出定量对比表。

## 🎯 结论与影响

最强结论是：从输入端缩小模态鸿沟既有效又数据高效，语音 LLM 可兼具韵律感知的文本 LLM 特性。这为 speech LLM 的表示对齐研究提供了新方向，也意味着以较少语音数据构建副语言感知 SLM 在工程上更可行。

## ⚠️ 局限与未解决问题

摘要未给出模态鸿沟的具体度量定义与数值，也未报告与哪些 SLM 基线对比、副语言任务的具体指标；缺少消融验证 WhisperPro 各组件贡献，未报推理延迟与参数量，1000 小时训练数据的覆盖域与偏差亦未说明。

## 🔗 开源资源

- **代码**：<https://github.com/dreamtheater123/TextPro-SLM>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-11-02/">← 返回 2026-11-02 速递</a></div>
