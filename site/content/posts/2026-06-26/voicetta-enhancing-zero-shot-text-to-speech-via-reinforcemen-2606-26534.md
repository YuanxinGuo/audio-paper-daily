---
title: "VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出VoiceTTA，通过强化学习在推理时优化可学习前缀，提升零样本TTS对罕见说话风格的模仿能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本TTS</span> <span class="tag-pill tag-pill-soft">#测试时自适应</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#风格模仿</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.26534</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://voicetta.pages.dev/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">voicetta.pages.dev/</span></span></a><a class="oc-chip oc-chip-demo" href="https://voicetta.pages.dev/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">voicetta.pages.dev/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.26534" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.26534" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://voicetta.pages.dev/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://voicetta.pages.dev/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出VoiceTTA，通过强化学习在推理时优化可学习前缀，提升零样本TTS对罕见说话风格的模仿能力。
</div>

## 👥 作者与机构

**Tianxin Xie** ¹ · Chenxing Li · Dong Yu · Li Liu

**机构**：腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS和语音风格迁移方向的研究者。建议重点读§3.2奖励设计和§3.3 GRPO优化，以及表2的对比结果。可先看demo页面感受效果。

## 🌍 研究背景

零样本TTS虽能合成高保真语音，但对罕见风格（如相声、方言）模仿不佳。现有方法需微调模型，依赖大量高质量数据，难以快速个性化。本文提出测试时自适应方法，在不更新模型参数的情况下，通过强化学习优化输入前缀，提升风格模仿能力。

## 💡 核心创新

1. 基于F0和能量变异系数的风格奖励
2. 结合说话人相似度和WER的多目标奖励
3. 采用GRPO优化可学习前缀
4. 在流匹配TTS模型上实现推理时自适应

## 🏗️ 模型架构

基于预训练零样本TTS模型（流匹配架构），输入文本和参考语音。在推理时，引入可学习前缀，通过GRPO优化以最大化组合奖励（风格奖励+说话人相似度+WER）。风格奖励基于F0和能量的变异系数差异，说话人相似度用预训练说话人编码器，WER用Whisper模型。优化后的前缀与文本嵌入拼接，送入流匹配解码器生成语音。

## 📚 数据集

- LibriTTS（训练预训练模型）
- VCTK（评估说话人相似度）
- 内部罕见风格数据集（评估，含相声、方言等）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（风格模仿） | 罕见风格测试集 | YourTTS 3.2 | **4.1** | +0.9 |
| 说话人相似度（SPK） | VCTK | YourTTS 0.85 | **0.91** | +0.06 |
| WER（%） | 罕见风格测试集 | YourTTS 8.5 | **6.2** | -2.3% |

在罕见风格测试集上，VoiceTTA在风格模仿MOS上比YourTTS提升0.9，说话人相似度提升0.06，WER降低2.3%。消融实验表明各奖励分量均有效，GRPO优于PPO。跨数据集泛化测试显示在VCTK上说话人相似度也有提升。

## 🎯 结论与影响

VoiceTTA通过测试时自适应显著提升零样本TTS对罕见风格的模仿能力，无需微调模型。该方法为个性化语音合成提供了新思路，有望推动TTS在多样化场景中的应用。

## ⚠️ 局限与未解决问题

仅验证了流匹配模型，未测试其他TTS架构；优化过程增加推理计算开销；罕见风格数据集规模较小，泛化性待验证；未与更多TTA方法对比。

## 🔗 开源资源

- **项目主页**：<https://voicetta.pages.dev/>
- **Demo / 试听**：<https://voicetta.pages.dev/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
