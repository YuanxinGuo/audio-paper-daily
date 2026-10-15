---
title: "MUSEBENCH: A Benchmark for AI-Generated Music Detection and Artifact Analysis"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频取证与生成检测"]
summary: "构建36.1万首曲目的AI生成音乐检测基准MUSEBENCH，含10个生成模型产物与对抗扰动变体，评测11个检测器并分析声学伪影。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频取证与生成检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#AI生成音乐检测</span> <span class="tag-pill tag-pill-soft">#基准数据集</span> <span class="tag-pill tag-pill-soft">#音频取证</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.20310</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.20310" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.20310" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建36.1万首曲目的AI生成音乐检测基准MUSEBENCH，含10个生成模型产物与对抗扰动变体，评测11个检测器并分析声学伪影。
</div>

## 👥 作者与机构

**Yi Chen Liu** ¹ · Syed Irfan Ali Meerza · Jiawei Yu · Xi Guo · Samuel Bright · Jian Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频取证、生成内容检测、AIGC溯源的研究者与平台风控工程师阅读。建议重点看数据集构建（§3）与跨域/扰动鲁棒性实验（表2、表3），以及伪影分析一节；检测器架构细节可略读。可执行动作：先看表2的跨域泛化结果，再对照伪影分析验证检测器是否依赖特定伪影。

## 🌍 研究背景

生成式音乐模型（Suno、Udio等）已能产出与人类作品难以区分的音频，AI音乐检测成为内容溯源与版权治理的关键问题。此前检测工作多基于小规模数据集，且生成模型单一，缺乏对跨模型泛化、对抗扰动与压缩后处理的系统评测。现有检测器在真实场景下的鲁棒性与失效边界尚不清楚，本文旨在通过大规模多源基准填补这一空白。

## 💡 核心创新

1. 构建36.1万曲目基准，覆盖10个开源与商业生成模型
2. 纳入人机共创、对抗扰动、压缩与声学后处理变体
3. 系统评测11个检测器在默认/跨域/变换三种设定下的表现
4. 通过声学特征检查归纳生成音乐的可复用伪影签名

## 🏗️ 模型架构

本文为基准与评测工作，非单一模型。数据侧：采集人类作曲、10个生成模型（含Suno、Udio）输出、人机共创及经对抗扰动、压缩、声学后处理的变体，共36.1万曲目。评测侧：统一11个自动检测器（含基于声学特征与深度表征的方法），在默认、out-of-domain、transformed-variant三种实验设定下比较准确率、泛化性与鲁棒性。分析侧：对音频做声学特征检查，识别非惯用和声进行、上采样引起的频谱周期性、违反物理演奏约束等伪影。

## 📚 数据集

- MUSEBENCH（自建基准，36.1万曲目，含人类作曲与10个生成模型输出，用于训练/评测）

## 📊 实验结果

摘要未给出具体数值指标，仅说明对11个检测器在默认、跨域与变换变体三种设定下评测了准确率、泛化性与鲁棒性。定性结论为：现有检测器在默认设定下表现尚可，但跨域与扰动/压缩变体下性能下降，暴露其脆弱性；伪影分析发现非惯用和声、上采样频谱周期性与物理演奏约束违背等可复用签名。

## 🎯 结论与影响

最强结论是：现有AI音乐检测器在跨模型与后处理扰动下泛化不足，单一伪影特征难以支撑可靠检测。该基准为后续研究提供了统一评测协议与失效分析视角，有望推动更鲁棒的检测方法。工业上对音乐平台的内容审核、版权归属与AIGC标注具有直接参考价值，但需注意检测器在真实压缩链路下的可靠性。

## ⚠️ 局限与未解决问题

作为基准论文，未提出新的检测方法，仅评测现有检测器，方法贡献有限；摘要未报告推理延迟、参数量等效率指标；对抗扰动与后处理的具体强度、生成模型版本未在摘要说明，可能影响可复现性；伪影分析偏定性，缺乏与检测性能的定量关联。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-15/">← 返回 2026-10-15 速递</a></div>
