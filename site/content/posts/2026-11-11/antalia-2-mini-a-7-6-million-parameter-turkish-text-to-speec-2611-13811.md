---
title: "Antalia-2 Mini: A 7.6-million-parameter Turkish text-to-speech model trained entirely on synthetic speech"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "7.6M 参数土耳其单说话人 TTS，全部用 VoxCPM2 合成语音蒸馏训练，48kHz 输出，WER 1.09%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#声码器</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.13811</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.13811" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.13811" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>7.6M 参数土耳其单说话人 TTS，全部用 VoxCPM2 合成语音蒸馏训练，48kHz 输出，WER 1.09%。
</div>

## 👥 作者与机构

**Sezgin Saygili** ¹ · Emre Kaplaner · Oncel Ozgul · Fikri San Koktas

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做轻量 TTS 部署、合成数据蒸馏、土耳其语/低资源语言 TTS 的工程读者。方法新颖度有限，但工程细节（vocoder 用声学模型自身 mel 微调、教师伪影被学生继承并靠前缀裁剪掩盖）值得一读。建议重点看 §vocoder 微调与 WER 对比表、Freya-TR-Eval 评测协议，以及作者对无人工听测的坦诚说明。

## 🌍 研究背景

土耳其语 TTS 的公开强基线很少，EMA Lightning（8.6M）是少数可比的轻量模型；主流做法依赖真实录音训练声学模型+声码器。痛点在于：真实多说话人语料稀缺、录制成本高，而大模型教师（如 VoxCPM2）合成语音虽易得却带有系统性伪影。本文要解决的问题是：能否仅用教师合成语音，蒸馏出一个 7.6M 参数、可在笔记本 CPU 实时推理的土耳其单说话人 TTS，并量化其与真实数据训练模型的差距。

## 💡 核心创新

1. 全合成语音蒸馏：仅用 VoxCPM2 生成约 1790h 数据训练学生模型
2. 用声学模型自身 mel 微调声码器，WER 从 3.89% 降至 1.75%
3. 发现并处理教师首词为 'o 时的起始失真，用裁剪前缀掩盖
4. 7.6M 参数在 Apple M5 CPU 双线程达 41 倍实时，输出 48kHz

## 🏗️ 模型架构

输入为字符序列，经轻量声学模型（摘要未给主干网络名）预测 mel 频谱，再由声码器还原 48kHz 波形；声码器在声学模型自产 mel 上二次微调以对齐训练/推理分布。整体参数量 7,620,931，单说话人、单音色。训练数据全部来自教师 VoxCPM2 克隆一条合成片段后批量生成，经自动检查保留约 1790 小时。推理在 Apple M5 笔记本 CPU 双线程上达 41 倍实时。

## 📚 数据集

- VoxCPM2 合成语音（训练，约 1790 小时，经自动筛选）
- Freya-TR-Eval（评估，495 句土耳其语）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Freya-TR-Eval | 相邻预发布检查点 3.89% | **1.75%** | -2.14% |
| WER | Freya-TR-Eval | EMA Lightning（8.6M，配对 bootstrap 无显著差异） | **1.09%** | 统计不可区分 |
| CER | Freya-TR-Eval | 未给 | **0.22%** | — |

声码器用声学模型自身 mel 微调后，Whisper 转写 WER 从均值 3.89% 降到 1.75%。在自建 495 句 Freya-TR-Eval 上，v1.0.1 达 WER 1.09%、CER 0.22%，但与 EMA Lightning 的差异经配对 bootstrap 不显著；后者在全频带 UTMOS（英语训练的质量代理）上更高。作者明确说明无人工听测，且评测集上做过参数调优。

## 🎯 结论与影响

最强结论是：纯合成语音蒸馏可训练出 7.6M 参数、CPU 实时的土耳其 TTS，字错率接近同量级真实数据模型。对低资源语言 TTS 与合成数据蒸馏方向有参考价值，说明教师伪影可被识别并部分规避。工业上适合端侧/离线轻量部署，但质量上限受教师与无听测所限。

## ⚠️ 局限与未解决问题

无任何人工主观听测，UTMOS 为英语训练代理，对土耳其语质量判断存疑；评测集上调过参数，存在过拟合风险；与 EMA Lightning 差异统计不显著，优势不明确；未报推理延迟分布与内存占用；训练代码与数据未公开，复现受限；教师起始失真靠裁剪掩盖而非修复。

---

<div class="paper-footer"><span>评分：5.8</span><span>原始：5.8</span><a href="/audio-paper-daily/posts/2026-11-11/">← 返回 2026-11-11 速递</a></div>
