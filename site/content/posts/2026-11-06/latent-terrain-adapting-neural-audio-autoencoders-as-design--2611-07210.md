---
title: "Latent Terrain: Adapting Neural Audio Autoencoders as Design Materials in NIME"
date: 2026-11-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "将神经音频自编码器的潜空间作为生成式声音空间，做成 Max/MSP 工具包供 NIME 创作者使用。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经音频自编码器</span> <span class="tag-pill tag-pill-soft">#潜空间导航</span> <span class="tag-pill tag-pill-soft">#NIME</span> <span class="tag-pill tag-pill-soft">#音乐交互设计</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.07210</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.07210" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.07210" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将神经音频自编码器的潜空间作为生成式声音空间，做成 Max/MSP 工具包供 NIME 创作者使用。
</div>

## 👥 作者与机构

**Shuoyang Jasper Zheng** ¹ · Keigo Yoshida · Nico Garc\'ia-Peguinho · Jiatong Liu · Dan Hearn · Anna Xamb\'o Sed\'o · Nick Bryan-Kinns

**机构**：伦敦玛丽女王大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合 NIME / 音乐交互设计与生成式音频工具研究者阅读。若关注声学信号处理指标（SI-SDR、PESQ）则价值有限。建议重点看工具设计理据与四名创作者的合作作品集部分，跳过纯艺术反思段落。

## 🌍 研究背景

神经音频自编码器（如 RAVE、SoundStream 类模型）已被用于实时声音合成，NIME 社区开始将其潜空间视为可导航的生成式声音空间。但现有实践多为一次性艺术项目，缺乏面向创作者的可复用工具与设计方法论，潜空间如何被“雕刻”为基于语料的声音空间尚缺系统描述。本文试图把自编码器潜空间确立为 NIME 的设计材料，并给出工具化实现。

## 💡 核心创新

1. 将自编码器潜空间定位为 NIME 设计材料
2. Latent Terrain：Max/MSP 潜空间导航工具包
3. 基于语料的潜空间定制流程
4. 与四位 NIME 创作者的合作作品集方法

## 🏗️ 模型架构

论文为实践型工具论文，未给出统一网络结构。Latent Terrain 以预训练神经音频自编码器为后端，将音频编码为潜向量，在 Max/MSP 中提供潜空间导航、插值与语料映射接口，使用户可将潜空间裁剪、组织为基于语料的声音空间。摘要未披露具体自编码器骨干（如 RAVE / SoundStream）、参数量或训练细节。

## 📊 实验结果

摘要未报告任何定量指标（无 SI-SDR / PESQ / MOS / 主观评分），也未给出数据集规模。评估形式为与四位 NIME 创作者合作产生的注释作品集（annotated portfolio），属质性设计评估，而非受控实验对比。

## 🎯 结论与影响

最强结论是神经音频自编码器潜空间可作为 NIME 的可操作设计材料，并通过工具包落地。对 AI 增强 NIME 的工具化与设计方法论有推动作用，提示工业侧可将潜空间导航封装为创作者友好的交互界面。

## ⚠️ 局限与未解决问题

缺乏定量评估与基线对比，作品集样本仅四人，主观性强；未报告工具延迟、实时性与模型推理开销，这对 NIME 现场演出至关重要；也未讨论潜空间可控性与可复现性问题。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-11-06/">← 返回 2026-11-06 速递</a></div>
