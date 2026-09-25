---
title: "Configurable-Bandwidth Time-Frequency Modeling for Efficient Full-Band Speech Enhancement Across Sampling Rates"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出 TF-Refiner，将深度分析带宽与全带输入输出解耦，用单套参数跨 16/48 kHz 及未见采样率做全带语音增强。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.6</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#多采样率</span> <span class="tag-pill tag-pill-soft">#时频域建模</span> <span class="tag-pill tag-pill-soft">#高效推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29463</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29463" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29463" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 TF-Refiner，将深度分析带宽与全带输入输出解耦，用单套参数跨 16/48 kHz 及未见采样率做全带语音增强。
</div>

## 👥 作者与机构

**Ui-Hyeop Shin** ¹ · Wooseok Kim · Hyung-Min Park ✉

**机构**：韩国崇实大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多采样率/全带语音增强与高效时频建模的研究者与工程团队。建议通读，重点看 §3 的 deep encoder + shallow decoder 解耦设计与随机截止训练策略，以及表 2 跨采样率对比和成本-质量工作点实验；复现时先确认 STFT 配置与高频 query 的实现细节。

## 🌍 研究背景

现有语音增强系统多针对固定采样率设计，而时频模型的计算量随频点数增长，全带（48 kHz）建模代价高。此前 SOTA 如 BSRNN、FRCRN 等在 16 kHz VoiceBank+DEMAND 上表现良好，但难以直接迁移到多采样率场景，且为每个采样率单独训练参数成本高。本文要解决的是：用单套参数覆盖多采样率全带增强，并让分析带宽可按算力预算配置。

## 💡 核心创新

1. 解耦深度分析带宽与全带输入输出，低频深编码、高频浅解码
2. 输入相关的高频 query 机制，配合浅解码器预测局部复数滤波器
3. 随机截止训练，支持推理时无重训选择成本-质量工作点
4. 单参数集跨 16/48 kHz 训练，泛化到未见采样率

## 🏗️ 模型架构

输入为原始含噪 STFT。低于可配置截止频率的频带送入深度编码器提取特征；浅层解码器将该特征与输入相关的高频 query 结合，预测作用于原始含噪 STFT 的局部复数滤波器，从而重建全带输出。模型为采样频率无关设计，单套参数在 16 kHz 与 48 kHz 上联合训练，推理时可通过调整截止频率在成本与质量间取舍，输出带宽保持不变。摘要未给出具体参数量。

## 📚 数据集

- VoiceBank+DEMAND（训练与评估，16 kHz 常用增强基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | 各采样率专用模型 | **通用模型更优** | 优于 rate-specific |
| STOI | VoiceBank+DEMAND | 各采样率专用模型 | **通用模型更优** | 优于 rate-specific |
| log-spectral distance | VoiceBank+DEMAND | 各采样率专用模型 | **通用模型更优** | 优于 rate-specific |

摘要仅给出定性结论：在 VoiceBank+DEMAND 上，通用模型在 PESQ、STOI、log-spectral distance 上均优于各采样率专用模型，且覆盖训练中未见的采样率。随机截止训练可在推理时选择成本-质量工作点而无需重训或改变输出带宽。摘要未提供具体数值、消融细节与推理延迟数据。

## 🎯 结论与影响

最强结论是：可配置分析带宽可作为多采样率全带语音增强的实用设计选择，单套参数即可跨采样率并泛化到未见采样率。这为多采样率部署与算力自适应增强提供了新思路，工业上可减少为不同采样率维护多套模型的成本。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值、参数量、推理延迟与 FLOPs，成本-质量工作点缺少量化曲线；仅在 VoiceBank+DEMAND 上评估，缺少 DNS-Challenge、LibriMix 等更复杂噪声与混响场景；未与近期全带增强方法做充分对比，随机截止训练的消融细节不明。

---

<div class="paper-footer"><span>评分：8.6</span><span>原始：7.6</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
