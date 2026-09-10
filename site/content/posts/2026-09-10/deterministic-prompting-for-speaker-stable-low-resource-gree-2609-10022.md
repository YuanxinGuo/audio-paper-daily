---
title: "Deterministic Prompting for Speaker-Stable Low-Resource Greek TTS"
date: 2026-09-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用确定性提示替代LLM生成提示，配合3.5小时单说话人LoRA微调Parler-TTS，实现稳定的低资源希腊语TTS。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#低资源TTS</span> <span class="tag-pill tag-pill-soft">#LoRA微调</span> <span class="tag-pill tag-pill-soft">#提示工程</span> <span class="tag-pill tag-pill-soft">#数据筛选</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.10022</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.10022" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.10022" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用确定性提示替代LLM生成提示，配合3.5小时单说话人LoRA微调Parler-TTS，实现稳定的低资源希腊语TTS。
</div>

## 👥 作者与机构

**Georgios Syllas** ¹ · Efthymios Georgiou · Kosmas Kritsis · Alexandros Potamianos

**机构**：雅典国立技术大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做低资源TTS与多语言适配的工程研究者阅读。建议重点看数据筛选流程与确定性提示的消融部分，以及LoRA配置（约5%参数）的细节。若只关心建模创新可略读，本文主要贡献在数据与提示工程而非新架构。

## 🌍 研究背景

现代TTS在高资源语言上已接近人类水平，但希腊语等低资源语言缺乏精调语料，直接微调易出现质量下降与说话人漂移。此前基于提示的多语言模型（如Parler-TTS）依赖LLM生成风格提示，推理时提示随机性会导致音色不稳定。本文要解决的是：在仅有少量单说话人数据条件下，如何获得说话人一致且可懂度高的希腊语TTS。

## 💡 核心创新

1. 用WhisperX对齐+过滤将有声书转为TTS可用数据
2. 发现LLM生成风格提示导致说话人漂移，改用确定性提示
3. 单说话人LoRA仅更新约5%参数锚定音色
4. 在880M Parler-TTS上验证低资源希腊语迁移

## 🏗️ 模型架构

输入为文本与确定性风格提示，主干为880M参数的Parler-TTS（基于提示的多语言自回归TTS）。流程分两阶段：先用WhisperX对有声书做强制对齐与质量过滤，构建TTS训练数据；再在预训练模型上做说话人特定LoRA微调，仅更新约5%参数以锚定单说话人身份。推理时使用固定确定性提示替代LLM生成提示，输出为单说话人希腊语语音。

## 📚 数据集

- 有声书录音（数据来源，经WhisperX对齐与过滤）
- 3.5小时单说话人数据（LoRA微调）
- 希腊语评估集（评估，含ASR floor对比）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | 希腊语评估集 | ASR floor 7.8% | **10.7%** | +2.9% |
| MOS-I | 希腊语评估集 | 人类语音 4.36 | **4.00** | -0.36 |
| MOS-C | 希腊语评估集 | 人类语音 4.30 | **4.24** | -0.06 |

摘要给出WER 10.7%（高于ASR下限2.9）、MOS-I 4.00（人类4.36）、MOS-C 4.24（人类4.30）。说话人一致性接近人类，可懂度与自然度仍有差距。未提供消融实验、推理延迟或与其他低资源TTS基线的系统对比，确定性提示与LoRA各自的贡献缺乏量化拆分。

## 🎯 结论与影响

最强结论是：在仅3.5小时单说话人数据下，确定性提示加LoRA即可获得接近人类的说话人一致性与可接受的希腊语可懂度。这为低资源语言的提示式TTS适配提供了可复现的数据与提示工程范式，对工业界快速上线小语种语音合成有参考价值。

## ⚠️ 局限与未解决问题

仅单说话人、单语言验证，泛化性未知；未报告推理延迟与参数量开销；缺少确定性提示与LLM提示的定量消融；MOS样本量与评估协议未说明；与主流低资源TTS基线（如VITS微调）缺乏对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-10/">← 返回 2026-09-10 速递</a></div>
