---
title: "The Alignment Curse: Modality Alignment Supercharges Audio Attacks via Text Transfer"
date: 2026-11-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频安全"]
summary: "提出“对齐诅咒”原则：文本-音频模态对齐越强，文本越狱攻击越易迁移到音频，对Qwen2.5-Omni等全模态模型做黑盒评估验证。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态对齐</span> <span class="tag-pill tag-pill-soft">#对抗攻击迁移</span> <span class="tag-pill tag-pill-soft">#全模态模型</span> <span class="tag-pill tag-pill-soft">#越狱攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.02557</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.02557" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.02557" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出“对齐诅咒”原则：文本-音频模态对齐越强，文本越狱攻击越易迁移到音频，对Qwen2.5-Omni等全模态模型做黑盒评估验证。
</div>

## 👥 作者与机构

**Yupeng Chen** ¹ · Junchi Yu · Aoxi Liu · Baoyuan Wu · Philip Torr · Adel Bibi

**机构**：牛津大学 · 香港中文大学（深圳）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态安全、全模态模型红队、语音交互系统风险评估的研究者阅读。值得通读：重点看对齐强度的形式化定义与§4攻击迁移实验设计，以及跨模型（Qwen2.5-Omni vs Qwen3-Omni）的对齐-迁移相关性分析。若只关心语音增强/分离可跳过。

## 🌍 研究背景

端到端全模态模型通过强化文本-音频对齐显著提升音频能力，但文本越狱攻击远比音频攻击成熟。若文本漏洞能系统性迁移到音频，现有音频安全评估会低估来自文本模态的风险。此前工作多分别评估文本或音频攻击，缺少对跨模态迁移与对齐强度关系的刻画，本文要回答对齐是否反而放大安全风险这一具体问题。

## 💡 核心创新

1. 形式化刻画“对齐诅咒”：对齐强度与跨模态攻击迁移正相关
2. 构建文本攻击、文本迁移音频攻击、音频攻击三类黑盒评估协议
3. 在Qwen2.5/3-Omni上验证文本迁移攻击常优于纯音频攻击
4. 分析对齐强度与迁移效果跨方法、跨模型的一致性关系

## 🏗️ 模型架构

本文为评估性研究而非新网络。流程为：以文本越狱提示为源攻击，经全模态模型的文本-音频对齐通道转换为音频对抗输入，再在黑盒设定下查询Qwen2.5-Omni、Qwen3-Omni等模型；对比三类攻击（纯文本、文本迁移音频、纯音频）的攻击成功率，并以模态对齐度量（如嵌入相似度/对齐训练强度）为自变量做相关性分析，输出对齐-迁移关系曲线。

## 📚 数据集

- 自建文本越狱提示集（攻击源，规模摘要未给出）
- 音频对抗样本集（由文本攻击迁移生成，评估用）
- Qwen2.5-Omni / Qwen3-Omni 黑盒评估（模型侧，非数据集）

## 📊 实验结果

摘要未给出具体攻击成功率数值，仅定性报告：文本迁移音频攻击与纯音频攻击表现相当，且常更优，在仅音频访问条件下优势明显；跨攻击方法与跨模型分析一致支持对齐越强迁移越有效的结论。缺少量化表格与置信区间。

## 🎯 结论与影响

最强结论是模态对齐在提升能力的同时系统性放大文本到音频的漏洞迁移，构成能力与安全的根本张力。这提示后续全模态安全研究需把文本侧风险纳入音频评估，工业上部署语音交互全模态模型时应联合红队文本与音频通道。

## ⚠️ 局限与未解决问题

以评估为主，缺防御方法与缓解实验；对齐强度度量较粗，未控制训练数据重叠等混淆因素；攻击成功率数值与置信区间未在摘要呈现；仅覆盖Qwen系列，跨厂商模型泛化性待验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-16/">← 返回 2026-11-16 速递</a></div>
