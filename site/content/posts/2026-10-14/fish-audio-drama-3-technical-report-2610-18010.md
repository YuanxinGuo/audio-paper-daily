---
title: "Fish Audio Drama 3 Technical Report"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "开源35B MoE语音生成模型，支持多轮修订、场景配音、infilling编辑与流式合成，单H200解码271帧/秒。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#多说话人</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.18010</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/fishaudio/fish-speech" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">fishaudio/fish-speech</span></span></a><a class="oc-chip oc-chip-hf" href="https://huggingface.co/fishaudio/drama-3" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 fishaudio/drama-3</span></span></a><a class="oc-chip oc-chip-demo" href="https://fish.audio" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">fish.audio</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.18010" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.18010" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/fishaudio/fish-speech" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-hf" href="https://huggingface.co/fishaudio/drama-3" target="_blank" rel="noopener">🤗 HuggingFace</a><a class="rsrc rsrc-demo" href="https://fish.audio" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>开源35B MoE语音生成模型，支持多轮修订、场景配音、infilling编辑与流式合成，单H200解码271帧/秒。
</div>

## 👥 作者与机构

**Dawei Han** ¹ · Shidong Li · Shijia Liao · Jiahua Liu · Songting Liu · Qingzheng Wang · Yuxuan Wang · Xin Chen · … 等 8 人

**机构**：Fish Audio

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS系统、语音编辑与流式推理的工程与研究人员阅读。建议重点看§3的codebook multi-token-prediction解码器与三阶段预训练配方，以及§4的大批量RL与人类偏好奖励设计；效率对比表值得单独核对。若只关心语音增强/分离，可跳过。

## 🌍 研究背景

此前开源TTS多以自回归或扩散模型为主，如Fish Audio S2、CosyVoice、F5-TTS等，参数规模多在数亿到十亿级，功能上通常只支持单轮文本到语音，缺乏多轮修订、场景配音与流式输入的统一建模。痛点在于：多角色场景需拼接多个模型，编辑已有语音需外挂工具，长音频与流式难以兼顾，且RLHF在语音生成中应用有限。本文要在一个模型内统一这些能力，并保持高吞吐推理。

## 💡 核心创新

1. 35B MoE主干，每token仅激活3B，混合线性注意力
2. codebook multi-token-prediction音频解码器，逐帧分层预测声学码本
3. 三阶段预训练+指令微调+大批量RL，奖励为单一人类偏好模型
4. 单模型统一多轮修订、场景配音、infilling编辑与流式合成

## 🏗️ 模型架构

输入为文本与多参考语音，主干为35B参数MoE，每token激活3B，采用混合线性注意力以降低长序列开销。音频侧使用新的codebook multi-token-prediction解码器：每一帧的多个声学码本由专用层预测，这些层对整个序列做注意力，从而在帧内并行、帧间保持全局依赖。输出为声学码本序列，再经声码器还原波形。训练分三阶段预训练、指令微调与大批量强化学习，奖励来自单一学习到的人类偏好模型。推理经SGLang-Omni，单H200达271帧/秒。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 解码帧率 (frames/s) | 单张H200推理 | Fish Audio S2 177 | **271** | +94 |

摘要仅给出推理吞吐对比：Drama 3在单张H200上达271帧/秒，Fish Audio S2为177帧/秒，而Drama 3参数量是S2的七倍以上。未报告MOS、WER、说话人相似度等主观或客观指标，也未给出多轮修订、场景配音、infilling编辑的具体评测数据，实验部分信息明显不足。

## 🎯 结论与影响

最强结论是：在参数量扩大七倍的情况下，通过MoE与线性注意力仍把解码吞吐提升约53%，并把多轮修订、场景配音、编辑与流式统一进单一模型。若其能力可复现，将推动开源TTS从单轮合成走向可交互的“导演式”语音生成，对配音、有声书与实时语音Agent落地有直接价值。

## ⚠️ 局限与未解决问题

摘要未给出任何MOS、WER、相似度或编辑保真度指标，无法判断生成质量是否随规模提升；缺少与CosyVoice、F5-TTS等强基线的对比；RL仅用单一偏好奖励，可能过优化；271帧/秒的吞吐未说明批大小与延迟；多轮修订与infilling的失败模式未讨论。

## 🔗 开源资源

- **代码**：<https://github.com/fishaudio/fish-speech>
- **HuggingFace**：<https://huggingface.co/fishaudio/drama-3>
- **Demo / 试听**：<https://fish.audio>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
