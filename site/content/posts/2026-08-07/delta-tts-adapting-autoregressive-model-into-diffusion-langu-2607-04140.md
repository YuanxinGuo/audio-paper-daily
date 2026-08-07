---
title: "DELTA-TTS: Adapting Autoregressive Model into Diffusion Language Model for Text-to-Speech"
date: 2026-08-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "DELTA-TTS通过LoRA将自回归TTS转为扩散语言模型，实现置信度排序解码，提升速度与鲁棒性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散语言模型</span> <span class="tag-pill tag-pill-soft">#自回归模型</span> <span class="tag-pill tag-pill-soft">#LoRA</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.04140</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.04140" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.04140" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>DELTA-TTS通过LoRA将自回归TTS转为扩散语言模型，实现置信度排序解码，提升速度与鲁棒性。
</div>

## 👥 作者与机构

**Junwon Moon** ¹ · Yejin Lee · Seungbeom Kim · Hoseong Ahn · Sewoong Park · Heeseung Kim · Kyuhong Shim

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS研究者，重点看方法部分（§3）和实验（§4），可复现其LoRA适配与推理调度。

## 🌍 研究背景

自回归TTS模型顺序生成离散语音token，推理慢且错误传播导致幻觉。尽管TTS可获取完整文本，但AR模型仍受限于从左到右的生成顺序。本文旨在通过将预训练AR模型转换为离散扩散语言模型，实现非顺序、置信度排序的解码，以提升速度与鲁棒性。

## 💡 核心创新

1. LoRA适配将AR模型转为扩散语言模型
2. 卷积模块注入局部声学上下文
3. 1/t加权训练目标
4. 时间偏移推理调度延迟低置信度位置
5. 置信度排序解码缓解幻觉

## 🏗️ 模型架构

输入文本编码后，通过LoRA适配的预训练AR模型作为扩散语言模型，在离散token空间进行扩散过程。主干为预训练AR模型（如Seed-TTS），加入卷积模块捕捉局部声学结构。训练采用1/t加权目标，推理使用时间偏移调度，按置信度排序生成token。

## 📚 数据集

- LibriTTS（训练，585小时）
- Seed-TTS test-en（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Seed-TTS test-en | AR backbone（未给出具体值） | **1.75%** | 优于AR backbone |
| 推理速度 | Seed-TTS test-en | AR backbone（未给出具体值） | **3.3x faster** | +3.3x |

DELTA-TTS在Seed-TTS test-en上达到1.75% WER，优于其AR骨干，同时生成速度快3.3倍。进一步分析显示，DELTA-TTS产生更清晰的文本-语音对齐，提高整体解码置信度，并减少AR生成中观察到的幻觉。

## 🎯 结论与影响

DELTA-TTS通过LoRA将AR TTS转换为扩散语言模型，实现置信度排序解码，显著提升推理速度并改善鲁棒性。该方法为TTS提供新范式，有望推动非自回归TTS发展，并可能降低部署成本。

## ⚠️ 局限与未解决问题

仅基于585小时LibriTTS训练，未在更大规模数据上验证；未报告MOS等主观指标；未与其他非自回归TTS（如VALL-E）对比；未讨论模型参数量增加情况。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-07/">← 返回 2026-08-07 速递</a></div>
