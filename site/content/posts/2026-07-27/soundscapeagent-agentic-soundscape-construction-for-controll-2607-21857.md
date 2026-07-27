---
title: "SoundscapeAgent: Agentic Soundscape Construction for Controllable Synthesis and Scalable Audio-Language Supervision"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出基于LLM代理的声景构建框架，将文本到音频生成分解为场景规划、源选择、时间布局和渲染步骤，实现可控合成和可扩展的音频-语言数据构建。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可控音频生成</span> <span class="tag-pill tag-pill-soft">#声景合成</span> <span class="tag-pill tag-pill-soft">#LLM代理</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.21857</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://haozhang6720.github.io/SoundscapeAgentDemoPage/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">haozhang6720.github.io/SoundscapeAgentDemoPage/</span></span></a><a class="oc-chip oc-chip-demo" href="https://haozhang6720.github.io/SoundscapeAgentDemoPage/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">haozhang6720.github.io/SoundscapeAgentDemoPage/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.21857" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.21857" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://haozhang6720.github.io/SoundscapeAgentDemoPage/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://haozhang6720.github.io/SoundscapeAgentDemoPage/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LLM代理的声景构建框架，将文本到音频生成分解为场景规划、源选择、时间布局和渲染步骤，实现可控合成和可扩展的音频-语言数据构建。
</div>

## 👥 作者与机构

**Hao Zhang** ¹ · Yiwen Zhao · Yixuan Zhang · Yiwen Shao · Steve Yves

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、可控合成及数据增强方向的研究者。建议重点阅读§3框架设计及§4实验部分，特别是表2和表3的对比结果。可先看demo页面了解生成效果。

## 🌍 研究背景

现有文本到音频生成模型通常以端到端方式隐式处理场景规划、源选择和布局，缺乏可解释性和可控性。同时，高质量音频-语言配对数据稀缺，限制了模型在下游任务中的性能。本文提出将声景构建分解为显式步骤，利用LLM代理实现可控合成，并自动生成带标注的多事件混合数据，以缓解数据瓶颈。

## 💡 核心创新

1. LLM代理驱动的场景规划与资产获取
2. 显式的时间布局与可控渲染模块
3. 支持人机交互的可编辑场景计划
4. 利用代理生成数据训练下游模型

## 🏗️ 模型架构

输入用户意图文本，由LLM代理解析为场景计划，包含事件列表、时间布局和空间属性。通过检索或按需生成获取音频资产（如单源声音），然后经渲染模块混合为多事件声景，并输出对齐的场景元数据（事件时间戳、类别等）。框架支持用户通过工具选择和编辑计划进行交互。

## 📚 数据集

- AudioCaps（评估文本到音频生成）
- SoundScene（评估下游音频推理，由代理生成）
- ESC-50（评估音频分类，代理生成数据训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | AudioCaps | AudioLDM2 2.0 | **1.8** | -0.2 |
| CLAP Score | AudioCaps | AudioLDM2 0.31 | **0.33** | +0.02 |
| Accuracy | ESC-50 (代理数据训练) | 真实数据 85.0% | **87.5%** | +2.5% |

在AudioCaps上，所提框架的FAD和CLAP分数与强基线AudioLDM2相当或略优。在ESC-50分类任务中，使用代理生成数据训练的模型准确率达87.5%，优于仅用真实数据的85.0%。消融实验验证了各模块的有效性，且用户研究表明生成声景的自然度和可控性获得较高评分。

## 🎯 结论与影响

本文提出的SoundscapeAgent通过显式分解声景构建步骤，实现了可控且可解释的音频生成，同时为数据稀缺问题提供了可扩展的解决方案。该方法有望推动音频生成从黑盒向模块化、可交互方向发展，并为下游音频-语言任务提供高质量训练数据。

## ⚠️ 局限与未解决问题

依赖LLM的规划质量，可能产生不合理场景；音频资产库规模有限，影响多样性；渲染模块未考虑空间音频效果；未报告推理延迟和计算开销；与端到端模型的公平对比需进一步标准化。

## 🔗 开源资源

- **项目主页**：<https://haozhang6720.github.io/SoundscapeAgentDemoPage/>
- **Demo / 试听**：<https://haozhang6720.github.io/SoundscapeAgentDemoPage/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-27/">← 返回 2026-07-27 速递</a></div>
