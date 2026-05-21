---
title: "Discriminative-Generative Target Speaker Extraction with Decoder-Only Language Models"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出判别-生成两阶段框架，用解码器语言模型作为生成后端，结合判别前端实现高质量目标说话人提取。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#生成式模型</span> <span class="tag-pill tag-pill-soft">#解码器语言模型</span> <span class="tag-pill tag-pill-soft">#神经音频编解码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.06006</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.06006" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.06006" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出判别-生成两阶段框架，用解码器语言模型作为生成后端，结合判别前端实现高质量目标说话人提取。
</div>

## 👥 作者与机构

**Bang Zeng** ¹ · Beilong Tang · Wang Xiang · Ming Li ✉

**机构**：武汉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TSE和语音增强研究者。重点读§3两阶段框架设计和§4协作策略（前端冻结、联合微调、SI-SDR正则化）。建议先看表1和表2对比结果。

## 🌍 研究背景

目标说话人提取（TSE）和语音增强（SE）主流方法基于判别模型，虽干扰抑制强但感知质量和自然度有限。纯生成式TSE（如LauraTSE）存在幻觉、内容漂移和可控性差问题。本文提出判别-生成两阶段框架，结合判别前端的可控性和生成后端的重建能力。

## 💡 核心创新

1. 提出判别-生成两阶段TSE框架
2. 使用解码器语言模型作为生成后端
3. 探索多种前后端协作策略（冻结、联合微调、SI-SDR正则化）
4. 支持自回归和非自回归推理
5. 在TSE和SE基准上实现感知质量与可懂度平衡

## 🏗️ 模型架构

输入混合语音和注册语音→判别前端（如Conv-TasNet或SepFormer）提取目标相关表示→神经音频编解码器（如EnCodec）将表示编码为离散token→解码器语言模型（如Transformer解码器）自回归或非自回归生成高质量token→解码器重建波形。参数量未提及。

## 📚 数据集

- Libri2Mix（TSE训练/评估）
- WSJ0-2mix（TSE评估）
- DNS-Challenge（SE训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | Libri2Mix (TSE) | SepFormer 17.5 | **18.9** | +1.4 dB |
| PESQ | Libri2Mix (TSE) | SepFormer 3.45 | **3.62** | +0.17 |
| SI-SDR (dB) | WSJ0-2mix (TSE) | Conv-TasNet 15.3 | **16.8** | +1.5 dB |
| PESQ | DNS-Challenge (SE) | DCCRN 3.12 | **3.28** | +0.16 |

在TSE和SE基准上，所提框架相比纯判别或纯生成基线在SI-SDR和PESQ上均有提升。消融实验表明联合微调与SI-SDR正则化效果最佳，非自回归推理在保持质量的同时降低延迟。

## 🎯 结论与影响

判别-生成两阶段框架有效结合了判别模型的干扰抑制和生成模型的感知质量，在TSE和SE任务上均优于纯判别或纯生成方法。该框架为高质量语音提取提供了新范式，有望推动生成式模型在语音处理中的工业应用。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟；生成后端可能仍存在幻觉风险；仅在干净和噪声条件下评估，未见混响场景；协作策略的泛化性未充分验证。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
