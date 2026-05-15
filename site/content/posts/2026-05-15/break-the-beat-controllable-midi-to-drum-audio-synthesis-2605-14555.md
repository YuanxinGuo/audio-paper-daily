---
title: "Break-the-Beat! Controllable MIDI-to-Drum Audio Synthesis"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器合成"]
summary: "提出Break-the-Beat!模型，通过微调预训练文生音频模型，实现从MIDI鼓序列到高质量鼓音频的可控合成，支持参考音色控制。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#MIDI-to-Audio</span> <span class="tag-pill tag-pill-soft">#鼓合成</span> <span class="tag-pill tag-pill-soft">#可控生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.14555</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://ik4sumii.github.io/break-the-beat/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">ik4sumii.github.io/break-the-beat/</span></span></a><a class="oc-chip oc-chip-demo" href="https://ik4sumii.github.io/break-the-beat/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ik4sumii.github.io/break-the-beat/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.14555" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.14555" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://ik4sumii.github.io/break-the-beat/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://ik4sumii.github.io/break-the-beat/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Break-the-Beat!模型，通过微调预训练文生音频模型，实现从MIDI鼓序列到高质量鼓音频的可控合成，支持参考音色控制。
</div>

## 👥 作者与机构

**Shuyang Cui** ¹ · Zhi Zhong · Qiyu Wu · Zachary Novack · Woosung Choi · Keisuke Toyama · Kin Wai Cheuk · Junghyun Koo · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、乐器合成方向的研究者。建议重点阅读§3的混合条件机制和§4的消融实验。可先看Demo页面了解效果。

## 🌍 研究背景

数字音乐制作中，鼓循环音频的创建通常依赖单次采样或重采样，需要大量手动调整。现有生成模型虽能生成高质量音频，但缺乏对鼓MIDI序列的精确控制。已有的符号到音频研究多聚焦于单音调乐器，未解决多音打击乐合成问题。本文旨在填补这一空白，实现可控的鼓MIDI到音频合成。

## 💡 核心创新

1. 提出内容编码器提取参考音频的鼓音色特征
2. 设计混合条件机制融合MIDI序列与音色嵌入
3. 构建配对的目标-参考鼓音频数据集
4. 微调预训练文生音频模型实现高分辨率鼓合成

## 🏗️ 模型架构

基于预训练文本到音频扩散模型（如AudioLDM2），冻结大部分参数，引入内容编码器（参考音频的鼓音色嵌入）和条件编码器（MIDI序列的时序嵌入）。通过混合条件机制将两者注入扩散模型的UNet中，输出与MIDI对齐的鼓音频。参数量未明确给出。

## 📚 数据集

- ENST-Drums（训练/评估，鼓音频数据集）
- Groove MIDI Dataset（训练/评估，MIDI鼓序列）
- 自定义配对数据集（训练，从上述数据集中构建目标-参考对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | ENST-Drums测试集 | DiffSound (4.32) | **2.15** | -2.17 |
| KL散度 | ENST-Drums测试集 | DiffSound (1.82) | **0.93** | -0.89 |
| 节奏对齐精度 | ENST-Drums测试集 | DiffSound (78.3%) | **94.1%** | +15.8% |

实验表明，模型在FAD、KL散度和节奏对齐精度上均显著优于DiffSound基线。消融实验验证了内容编码器和混合条件机制的有效性。跨数据集泛化测试显示模型能适应不同鼓风格。

## 🎯 结论与影响

本文提出的Break-the-Beat!模型实现了从MIDI到鼓音频的高质量可控合成，在音频质量和节奏对齐上达到SOTA。该方法为音乐制作提供了新的可控工具，有望推动符号到音频合成在打击乐器方向的发展。

## ⚠️ 局限与未解决问题

模型依赖预训练文生音频模型，可能继承其偏差；参考音色控制仅针对鼓，未扩展到其他乐器；未报告推理速度或参数量；数据集规模有限，可能影响泛化性。

## 🔗 开源资源

- **项目主页**：<https://ik4sumii.github.io/break-the-beat/>
- **Demo / 试听**：<https://ik4sumii.github.io/break-the-beat/>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
