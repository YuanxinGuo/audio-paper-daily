---
title: "VocalRender: Score-Native Singing Voice Synthesis for Real-World Composition"
date: 2026-07-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#歌声合成"]
summary: "VocalRender提出乐谱原生歌声合成系统，直接由歌词、音高、音符值和速度生成歌声，无需显式时长预测，在自然度上超越最强基线0.42 CMOS。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#歌声合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#歌声合成</span> <span class="tag-pill tag-pill-soft">#自回归扩散模型</span> <span class="tag-pill tag-pill-soft">#乐谱驱动</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.27768</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.27768" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.27768" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VocalRender提出乐谱原生歌声合成系统，直接由歌词、音高、音符值和速度生成歌声，无需显式时长预测，在自然度上超越最强基线0.42 CMOS。
</div>

## 👥 作者与机构

**Yukun Chen** ¹ · Tianrui Wang · Zhaoxi Mu · Xinyu Yang · EngSiong Chng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合歌声合成、语音合成及音乐技术研究者阅读。建议重点阅读第3节模型架构和第4节实验部分，特别是与基线的对比表。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

现有歌声合成系统通常需要预定义时长、显式时长预测或时间对齐的声学引导，限制了在实际作曲工作流中的兼容性。这些方法依赖额外对齐信息，增加了使用复杂度。本文旨在提出一种乐谱原生系统，直接从乐谱信息合成歌声，无需显式时长预测，以更好地适配实际作曲场景。

## 💡 核心创新

1. 提出乐谱原生表示，交错歌词-音符编码
2. 采用自回归扩散模型生成连续声学潜变量并预测输出长度
3. 消除显式时长预测，简化合成流程
4. 在2300小时歌唱数据上训练，实现强可懂度和旋律控制
5. 跨域基准上展现高说话人相似度

## 🏗️ 模型架构

VocalRender输入歌词、音高、符号音符值和速度，通过交错歌词-音符表示编码。主干为自回归扩散模型，生成连续声学潜变量，同时预测输出长度。模型无需显式时长预测，直接输出声学特征，再经声码器合成波形。

## 📚 数据集

- 2300小时歌唱数据集（训练）
- 域内基准（评估）
- 域外基准（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 自然度CMOS | 域内/域外基准 | 最强基线 | **比基线高0.42** | +0.42 |

实验表明，VocalRender在可懂度、旋律控制和说话人相似度上均表现优异，域内和域外基准均验证了其泛化能力。自然度CMOS比最强基线高0.42，证明了乐谱原生架构的有效性。

## 🎯 结论与影响

VocalRender通过乐谱原生设计，实现了无需显式时长预测的歌声合成，显著提升了自然度，为实际作曲工作流提供了更便捷的工具。其自回归扩散模型和交错表示有望启发后续研究，推动歌声合成向更灵活、更易用的方向发展。

## ⚠️ 局限与未解决问题

摘要未提及推理速度、模型参数量等效率指标，也未报告消融实验。此外，训练数据规模虽大，但未说明数据多样性，可能影响跨语言或风格泛化。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-31/">← 返回 2026-07-31 速递</a></div>
