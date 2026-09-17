---
title: "HearInContext: A Benchmark for Implicit Context in Speech Recognition"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出 HearInContext 中英双语基准，用同音词与助手回复构造隐式/显式上下文，评测 ASR 的上下文利用能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#上下文语音识别</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#同音词消歧</span> <span class="tag-pill tag-pill-soft">#大模型微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18680</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18680" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18680" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 HearInContext 中英双语基准，用同音词与助手回复构造隐式/显式上下文，评测 ASR 的上下文利用能力。
</div>

## 👥 作者与机构

**Yifan Gao** ¹ · Yao Tian · Hongbin Suo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做上下文 ASR、热词识别与大模型语音微调的研究者阅读。建议通读，重点看基准构建流程（同音词与上下文配对设计）与 Qwen3-ASR-1.7B 微调实验部分，并核对无上下文/无关上下文对照的设置细节，判断该基准能否迁移到自己的场景。

## 🌍 研究背景

上下文 ASR 通常依赖显式提供的目标词或热词表，例如 shallow fusion、偏置解码与提示注入，这些方法在给定候选词时有效，但无法处理上下文只提供语义线索、候选词未出现的情况。现有基准多聚焦显式热词或领域适配，缺少对隐式语义上下文利用能力的系统评测，也缺少对无关历史敏感性的对照。本文要回答：模型能否仅凭对话历史中的语义线索消解同音词歧义，以及微调能否在不损害通用识别的前提下提升该能力。

## 💡 核心创新

1. 构建中英双语同音词隐式上下文基准 HearInContext
2. 设计无上下文与无关上下文两组对照，量化历史相关性收益
3. 用共享合成语音配对不同助手回复，控制声学变量
4. 微调 Qwen3-ASR-1.7B 提升隐式上下文目标召回

## 🏗️ 模型架构

基准以共享合成语音为核心：同一段合成语音搭配不同助手回复，形成隐式上下文（不含候选词）与显式上下文（点名目标词）两类条件，另设无上下文与无关上下文对照。评测模型为 Qwen3-ASR-1.7B，输入为语音加文本上下文提示，输出为转写文本；通过微调使模型学会从历史语义中推断同音词目标。摘要未给出主干网络细节与参数量以外的结构信息。

## 📚 数据集

- HearInContext（评估，3,764 条语义测试用例，中英双语）
- AISHELL-1（评估，通用 CER 对照）
- LibriSpeech（评估，通用 WER 对照）
- 真实录音普通话热词识别（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 隐式上下文目标召回 | HearInContext 中文 | Qwen3-ASR-1.7B 微调前 | **微调后** | +11.0 个百分点 |
| 隐式上下文目标召回 | HearInContext 英文 | Qwen3-ASR-1.7B 微调前 | **微调后** | +11.5 个百分点 |
| CER | AISHELL-1 | Qwen3-ASR-1.7B 微调前 | **微调后** | 绝对变化 <0.1 个百分点 |
| WER | LibriSpeech | Qwen3-ASR-1.7B 微调前 | **微调后** | 绝对变化 <0.1 个百分点 |

摘要给出微调后隐式上下文目标召回在中英分别提升 11.0 与 11.5 个百分点，同时 AISHELL-1 与 LibriSpeech 上 CER/WER 绝对变化低于 0.1 个百分点，说明通用识别能力基本未退化。增益还迁移到未参与微调的显式条件，以及真实录音的普通话热词识别。摘要未报告消融、推理延迟与参数量细节。

## 🎯 结论与影响

最强结论是：隐式语义上下文可被 ASR 模型利用，且通过轻量微调即可显著提升同音词目标召回而不牺牲通用识别性能。这为上下文 ASR 从显式热词转向隐式语义线索提供了可复现的评测入口，后续研究可基于该基准比较不同上下文注入方式。工业上对语音助手、会议转写中的同音词纠错有直接参考价值。

## ⚠️ 局限与未解决问题

基准基于合成语音与同音词构造，声学多样性有限，可能高估真实场景收益；仅微调 Qwen3-ASR-1.7B 一个模型，缺少与偏置解码、热词注入等主流上下文方法的对比；未报告推理延迟与显存开销；真实录音热词实验规模与统计显著性未说明。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
