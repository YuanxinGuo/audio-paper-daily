---
title: "InstructFX2FX: A Multi-turn Text-to-Preset Demo for Iterative Audio Effect Refinement"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频效果控制"]
summary: "提出多轮文本引导音频效果调整系统，结合LLM规划与CLAP优化，实现迭代式音色精调。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频效果控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到预设</span> <span class="tag-pill tag-pill-soft">#CLAP</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#交互式演示</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22005</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22005" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22005" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多轮文本引导音频效果调整系统，结合LLM规划与CLAP优化，实现迭代式音色精调。
</div>

## 👥 作者与机构

**Song-Ze Yu** ¹ · Milan Liessens Dujardin · Yuxuan Cai · Wantong Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频效果处理与交互式系统研究者。重点看§3混合架构与§4实验部分。可先看图1了解系统流程，再读表1的定量结果。

## 🌍 研究背景

现有文本到预设系统多为单轮映射，无法支持音频工程师的迭代式调整需求。用户常需通过连续指令（如“更温暖”“太刺耳，柔和些”）逐步优化效果链。单轮系统缺乏状态记忆，每次重新生成会丢失先前调整。本文提出多轮交互框架，结合LLM的高层规划与CLAP引导的优化，实现状态感知的迭代精调。

## 💡 核心创新

1. LLM作为高层规划器选择效果器并初始化参数
2. CLAP引导优化避免LLM重提示导致的参数漂移
3. 用户可试听优化检查点并选择应用强度
4. 在SocialFX数据集上验证9/10描述符对MMD降低

## 🏗️ 模型架构

输入为干录音与自然语言指令序列。系统包含两个模块：1) LLM（如GPT-4）作为规划器，根据当前效果参数和新指令选择效果器、排序信号链并初始化参数；2) CLAP引导优化器，从LLM初始状态出发，通过最小化CLAP嵌入距离与DSP特征MMD来精调参数。用户循环中可试听保存的优化检查点并选择应用强度，然后发出下一条指令。

## 📚 数据集

- SocialFX（描述符转换评估，包含10对定向描述符）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 目标导向DSP特征MMD | SocialFX描述符转换 | LLM-only重提示基线（未报告具体值） | **9/10描述符对MMD降低** | 优于基线 |

在SocialFX数据集上，CLAP引导优化在9/10的定向描述符对上降低了目标导向DSP特征MMD，且大多数优化轨迹趋向目标。未提供具体数值，但定性展示了多轮交互的有效性。

## 🎯 结论与影响

本文证明结合LLM规划与CLAP优化可有效实现多轮文本引导音频效果精调，优于纯LLM重提示基线。该工作为交互式音频制作工具提供了新范式，有望推动文本控制音频效果在DAW中的实际应用。

## ⚠️ 局限与未解决问题

仅基于SocialFX数据集评估，缺乏真实用户实验；未报告推理延迟或计算开销；未与更多基线（如纯CLAP优化）对比；用户循环中检查点选择机制可能引入主观偏差。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-25/">← 返回 2026-06-25 速递</a></div>
