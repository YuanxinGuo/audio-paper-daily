---
title: "Confucius4-R2T2: A Stable-Prefix Streaming ASR Model for Real Real-Time Transcription"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出最长稳定前缀(LSP)概念，通过后训练Qwen3-ASR-1.7B实现不修改历史输出的流式ASR，兼顾精度与低延迟。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式ASR</span> <span class="tag-pill tag-pill-soft">#稳定前缀</span> <span class="tag-pill tag-pill-soft">#大模型微调</span> <span class="tag-pill tag-pill-soft">#低延迟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.06043</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/netease-youdao/Confucius4-R2T2" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">netease-youdao/Confucius4-R2T2</span></span></a><a class="oc-chip oc-chip-hf" href="https://huggingface.co/netease-youdao/Confucius4-R2T2" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 netease-youdao/Confucius4-R2T2</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.06043" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.06043" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/netease-youdao/Confucius4-R2T2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-hf" href="https://huggingface.co/netease-youdao/Confucius4-R2T2" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出最长稳定前缀(LSP)概念，通过后训练Qwen3-ASR-1.7B实现不修改历史输出的流式ASR，兼顾精度与低延迟。
</div>

## 👥 作者与机构

**Daniel Huang** ¹ · Qi He · Shaoxiong Duan · Yingjie Li · Qiao Cheng · Yitao Duan

**机构**：网易有道

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做流式ASR、语音agent、端到端大模型落地的工程与研究读者。值得通读，重点看§3 LSP定义与单调性证明、§4后训练数据构造与冻结编码器策略、以及实验中的发射延迟(emission lag)与稳定性指标。可先看表2与延迟分析图，再回看LSP标签生成算法细节。

## 🌍 研究背景

流式ASR越来越多被机器消费（翻译器、语音agent），逐token触发下游动作。传统流式模型（如RNN-T、Conformer流式）存在输出回改问题，被修订的token导致下游重复计算或错误动作。而全上下文大模型（Whisper、Qwen3-ASR）精度高但非流式。已有chunk-based流式方案仍会在chunk边界回改文本。本文要解决：在不改架构的前提下，把全上下文ASR模型转成永不修改历史输出的稳定流式模型。

## 💡 核心创新

1. 提出最长稳定前缀(LSP)概念并证明其单调性、一致性与极大性
2. 用LSP标签对全上下文模型做后训练，无需架构改动即得流式能力
3. 冻结音频编码器与projector，仅适配语言侧，保留预训练声学表征
4. 在1,500小时中英数据上后训练，稳定性收益可跨语言泛化

## 🏗️ 模型架构

输入为流式音频chunk，经冻结的Qwen3-ASR-1.7B音频编码器与projector得到声学表征，送入LLM解码器。后训练阶段以LSP标签作为监督目标：对每条全音频输出，构造在任意前缀时刻都等于某个完整历史输出的最长稳定标签序列，使模型学会只发射不会被后续修订的token。推理时按chunk增量解码，已发射token锁定不再修改。模型基于Qwen3-ASR-1.7B（约1.7B参数），仅训练语言侧适配参数。

## 📚 数据集

- 1,500小时中英文语音（后训练，训练）
- 中英文流式识别评测集（评估，摘要未具名）

## 📊 实验结果

摘要称R2T2的流式识别质量接近基座模型的全上下文水平，同时输出稳定文本且发射延迟低；稳定性收益可泛化到后训练语言之外。但摘要未给出SI-SDR类以外的具体WER、延迟毫秒数或对比基线数值，缺乏可核对的定量表格，需查阅正文实验部分确认。

## 🎯 结论与影响

最强结论是：仅靠LSP标签后训练即可把全上下文ASR转为稳定前缀流式模型，无需架构改动且精度接近全上下文。这为流式ASR提供了一条低成本迁移路径，对语音agent、同传等逐token消费场景有直接落地价值，也提示稳定性可作为流式ASR的新优化目标。

## ⚠️ 局限与未解决问题

摘要未报告具体WER、发射延迟数值与对比基线，定量证据不足；仅冻结编码器可能限制声学域迁移；1,500小时数据规模与语言覆盖有限，跨语言泛化仅定性描述；缺少与RNN-T、chunk-based流式方案的直接对比与消融。

## 🔗 开源资源

- **代码**：<https://github.com/netease-youdao/Confucius4-R2T2>
- **HuggingFace**：<https://huggingface.co/netease-youdao/Confucius4-R2T2>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
