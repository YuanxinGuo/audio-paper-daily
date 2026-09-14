---
title: "DiffSynth-Music: Audio-Conditioned KV-Cache Adapters for Controllable Music Generation"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "用逐层KV注入为音乐扩散Transformer加入节拍、人声、伴奏、韵律与参考音频五类可控条件。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#可控生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#KV-Cache适配器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.12774</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.12774" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.12774" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用逐层KV注入为音乐扩散Transformer加入节拍、人声、伴奏、韵律与参考音频五类可控条件。
</div>

## 👥 作者与机构

**Zhongjie Duan** ¹ · Shengchuan Gao · Hong Zhang · Yingda Chen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控音乐生成、扩散/流匹配条件注入的研究者与工程团队阅读。建议先看 §3 的 KV-cache 注入机制与模板模型设计，再看表 2 的五类单条件评测；若关注训练数据构造，重点看节拍提取与源分离配对流程。

## 🌍 研究背景

文本与歌词条件只能约束音乐的整体风格与唱词，对节拍对齐、旋律走向和参考风格的控制力有限。已有可控音乐生成多依赖额外条件分支或重训练主干，条件组合困难且采样开销大。本文希望在冻结/复用扩散 Transformer 主干的前提下，以可组合的音频条件实现细粒度时序与音色控制。

## 💡 核心创新

1. 逐层 KV-cache 注入实现可组合音频条件
2. Control/Prosody/Reference 三个模板模型共享 VAE 隐空间
3. 模板时间步固定在干净数据端点，控制缓存一次计算全程复用
4. 由节拍提取、源分离、人声重合成自动构造训练配对

## 🏗️ 模型架构

输入为条件波形与文本/歌词，共享变分自编码器将节拍、人声、伴奏、韵律、参考音频统一映射到公共隐空间。主干为扩散 Transformer，三个模板模型由主干初始化并用条件流匹配训练。推理时在每一层以 key-value 形式注入条件注意力记忆，多个控制缓存可相加组合；模板时间步固定在干净数据端点，使每个控制缓存只需计算一次并在整个采样过程中复用。

## 📚 数据集

- Mandarin 与 English 歌曲（训练配对构造与单条件评估）

## 📊 实验结果

摘要仅给出定性结论：五类单条件在普通话与英文歌曲上依从性均优于主干，人声条件下歌词保真度提升；自动音乐质量与指令跟随分数与所评估基座模型大体相当，存在指标间取舍。未给出 SI-SDR、FAD、CLAP 等具体数值，也无消融与推理延迟数据。

## 🎯 结论与影响

最强结论是逐层 KV-cache 注入可在不重训主干的情况下为音乐扩散模型提供五类可组合音频控制。该思路对可控音乐生成的条件组合与推理复用有参考价值，工业上利于在已有基座上快速叠加节拍对齐与参考风格能力。

## ⚠️ 局限与未解决问题

缺少与主流可控音乐生成方法的定量对比，仅与自身主干比较；未报告推理延迟与缓存复用带来的实际加速；条件组合（多控制同时开启）未做系统评测；训练配对依赖源分离与重合成，可能引入伪影偏差。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
