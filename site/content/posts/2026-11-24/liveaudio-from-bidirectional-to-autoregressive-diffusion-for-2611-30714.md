---
title: "LiveAudio: From Bidirectional to Autoregressive Diffusion for Real-Time Streaming Video-to-Audio Generation"
date: 2026-11-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "将双向视频到音频扩散模型经渐进因果微调与蒸馏转为流式自回归生成器，在VGGSound上实现实时同步音频合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音频生成</span> <span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#实时推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.30714</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://streamaudio.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">streamaudio.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://streamaudio.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">streamaudio.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.30714" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.30714" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://streamaudio.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://streamaudio.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将双向视频到音频扩散模型经渐进因果微调与蒸馏转为流式自回归生成器，在VGGSound上实现实时同步音频合成。
</div>

## 👥 作者与机构

**Yuxuan Jiang** ¹ · Zehua Chen · Yusheng Dai · Andong Wang · Weibei Dou · Jun Zhu

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视频到音频生成、流式扩散/自回归生成的研究者与工程落地团队阅读。建议通读，重点看 §3 的渐进因果微调与蒸馏流程、以及实时性指标（RTF、首帧时延）的测量方式；表 2 的同步性对比与消融值得细看。

## 🌍 研究背景

视频到音频生成近年多采用双向扩散或流匹配模型（如 Diff-Foley、Frieren 类），在 VGGSound 上音频质量与同步性已较高，但必须观测完整视频片段后才能出音，无法用于直播、游戏、交互式世界模型等连续输入场景。已有流式模型多从零训练，音频质量与同步性明显落后于双向模型。本文要解决的是：如何在不牺牲音频质量与同步性的前提下，把强双向模型改造成逐块实时生成的流式生成器。

## 💡 核心创新

1. 提出 LiveAudio 流式视频到音频框架，逐块生成且仅依赖已播放视频
2. 用渐进因果微调把双向扩散模型转为因果流式生成器
3. 结合蒸馏使每块仅需少量采样步，降低时延
4. 在 VGGSound 上同步性超过其源双向模型

## 🏗️ 模型架构

输入为已播放视频块的特征（视觉编码器提取），主干沿用源双向视频到音频扩散模型的去噪网络，输出为对应音频块的潜变量再经声码器还原波形。关键改造在于将双向注意力替换/约束为因果形式，通过渐进因果微调逐步引入因果掩码，再用蒸馏把多步采样压缩为每块少步采样，实现块级自回归流式生成。摘要未给出具体参数量。

## 📚 数据集

- VGGSound（训练与评估，视频-音频对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 实时因子 RTF | VGGSound | 现有流式模型（未给具体值） | **0.79** | 实时（<1） |
| 首帧时延 TTFF | VGGSound | 现有流式模型（未给具体值） | **143 ms** | — |

摘要称在 VGGSound 上音频质量与同步性均优于现有流式模型，且同步性超过其源双向模型；单张 A100 上 RTF 0.79、首帧时延 143 ms，达到实时。但摘要未给出 FAD、IS、同步性等具体数值，也未报告与双向基线的音频质量差距及蒸馏步数消融，需看正文表格确认。

## 🎯 结论与影响

最强结论是双向扩散模型可经渐进因果微调与蒸馏转为实时流式生成器，且同步性不降反升。这为视频到音频的交互式落地（直播、游戏、世界模型）提供了可行路径，也提示“双向转流式”可作为通用范式迁移到其他生成任务。

## ⚠️ 局限与未解决问题

摘要未给出音频质量（FAD/IS）与同步性的具体数值及与双向基线的量化差距；缺少蒸馏步数、因果微调策略的消融；仅在 VGGSound 单一数据集验证，跨域泛化未知；未报告显存占用与长视频稳定性。

## 🔗 开源资源

- **项目主页**：<https://streamaudio.github.io>
- **Demo / 试听**：<https://streamaudio.github.io>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-24/">← 返回 2026-11-24 速递</a></div>
