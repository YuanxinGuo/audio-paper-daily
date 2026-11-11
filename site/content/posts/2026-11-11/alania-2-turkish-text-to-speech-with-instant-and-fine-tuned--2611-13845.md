---
title: "Alania-2: Turkish text-to-speech with instant and fine-tuned voice cloning"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "Alania-2 是 488M 参数的土耳其语 TTS 系统，基于 VoxCPM 架构，支持文本描述音色设计与两种声音克隆，并开源评测工具与三个数据集。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#声音克隆</span> <span class="tag-pill tag-pill-soft">#土耳其语</span> <span class="tag-pill tag-pill-soft">#低秩适配</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.13845</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.13845" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.13845" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Alania-2 是 488M 参数的土耳其语 TTS 系统，基于 VoxCPM 架构，支持文本描述音色设计与两种声音克隆，并开源评测工具与三个数据集。
</div>

## 👥 作者与机构

**Sezgin Saygili** ¹ · Emre Kaplaner · Oncel Ozgul · Fikri San Koktas

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多语种 TTS、声音克隆落地与数据合成管线的工程与研究同学。建议通读：重点看 §3 数据合成与过滤流程、§4 文本正则化对数字/日期可懂度的影响、§5 克隆条件方式对比（21.9%→1.7% 跳词）与 LoRA 微调实验；推理引擎 32 ms 首包部分可按需看。

## 🌍 研究背景

土耳其语 TTS 的公开资源与评测基准都很少，此前系统多为小规模单说话人模型，可懂度与克隆稳定性不足；同时大模型 TTS 依赖海量标注语音，低资源语种难以直接复制。本文要解决三个具体问题：如何在有限真实数据下用教师模型合成数据扩充训练集、如何保证数字/缩写/外来词在合成后仍可被 ASR 正确识别、以及即时克隆与微调克隆的工程取舍。

## 💡 核心创新

1. 用 488M VoxCPM 架构（LM 主干 + 扩散头生成连续音频 latent）从零训练土耳其语 TTS
2. 90% 合成语音 + 自动过滤的 18,195 小时数据配方，验证数据量比模型规模更影响可懂度
3. 文本正则化将数字/缩写/外来名改写为口语词，显著提升关键信息保留率
4. 克隆改为仅以参考音频为条件而非续写，跳词率从 21.9% 降至 1.7%
5. 约两分钟训练的 LoRA 适配器显著提升说话人相似度

## 🏗️ 模型架构

输入为文本（经文本正则化器处理数字、缩写、外来名）与可选参考音频/文本描述；主干为 VoxCPM 架构的语言模型 backbone，在其上接扩散头生成连续音频 latent，再由声码器还原波形。模型共 488M 参数，内置两个音色，支持文本描述的音色设计与即时/微调两种克隆；微调路径使用低秩适配器（LoRA）。推理引擎做了流式优化，单流首包音频延迟 32 ms。

## 📚 数据集

- 18,195 小时土耳其语语音（训练，其中 90% 为教师模型合成并自动过滤）
- Freya-TR-Eval（评估，495 条土耳其语句子，ASR 打分）
- 96 条含数字测试句（评估文本正则化）
- 作者开源的三个土耳其语语音与文本数据集（用途见原文）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Freya-TR-Eval | 前代系统 5.99% | **1.44%** | -4.55% |
| 关键信息全保留句数（96 句含数字） | 内部数字测试集 | 无文本正则化 0/96 | **有文本正则化 86/96** | +86 句 |
| 跳词率 | 克隆评测 | 续写参考音频 21.9% | **仅条件化 1.7%** | -20.2% |
| CER | 内置音色评测 | 2.3B 参数模型（差距半百分点内） | **488M 模型，差距 <0.5 点** | 接近 |
| 首包音频延迟 | 推理引擎 | 未给出 | **32 ms（单流）** | — |

Freya-TR-Eval 上 WER 从 5.99% 降至 1.44%；内置音色 CER 与 2.3B 参数模型差距在半点内，而 7.6M 单说话人模型用同一配方即可达到同等可懂度，说明数据比模型规模更关键。克隆实验给出经验结论：20–30 秒参考音频最佳，LoRA 微调约两分钟即可明显提升相似度。摘要未给出相似度具体数值与消融细节。

## 🎯 结论与影响

最强结论是：在土耳其语这类低资源语种上，合成数据配方与文本正则化对可懂度的贡献大于模型规模，488M 模型可逼近 2.3B 系统。这为低资源 TTS 的数据中心化路线提供了可复现证据，也提示工业落地可优先投入数据管线与推理引擎优化，而非一味堆参数。

## ⚠️ 局限与未解决问题

评测以 ASR 的 WER/CER 为主，缺少 MOS 等主观自然度与说话人相似度的具体数值；合成数据占 90%，教师模型偏差可能被继承；克隆对比基线不全，未报推理显存与吞吐；文本正则化仅用 96 句内部测试，规模偏小。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-11/">← 返回 2026-11-11 速递</a></div>
