---
title: "Decomposer: Learning to Decompile Symbolic Music to Programs"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐程序反编译"]
summary: "提出Decomposer框架，将符号音乐（MIDI）反编译为可编辑的Strudel音乐程序，通过合成数据微调与强化学习提升重建保真度和代码可读性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐程序反编译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#程序合成</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#音乐编程语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.01849</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.01849" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.01849" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Decomposer框架，将符号音乐（MIDI）反编译为可编辑的Strudel音乐程序，通过合成数据微调与强化学习提升重建保真度和代码可读性。
</div>

## 👥 作者与机构

**Yewon Kim** ¹ · Apurva Gandhi · David Chung · Graham Neubig · Chris Donahue

**机构**：卡内基梅隆大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、程序合成方向研究者。建议通读，重点看§3合成数据构造与§4强化学习奖励设计。可复现实验部分。

## 🌍 研究背景

音乐演奏可视为执行一组高级音乐指令，但从演奏中恢复这些指令是逆问题。现有方法多依赖启发式转换器或闭源LLM，但前者生成代码可读性差，后者缺乏领域数据。本文提出符号音乐反编译任务，将MIDI转为Strudel程序，面临低资源语言和保真度-可读性权衡两大挑战。

## 💡 核心创新

1. 提出MIDI-to-Strudel反编译任务
2. 构建Strudel-Synth合成语料库
3. 两阶段训练：监督微调+强化学习优化
4. 设计保真度与可读性联合奖励函数

## 🏗️ 模型架构

输入为MIDI事件序列，经编码器（Transformer）处理，解码器自回归生成Strudel程序。第一阶段在Strudel-Synth合成数据上监督微调；第二阶段使用PPO算法在无配对MIDI数据上优化，奖励函数包含MIDI重建保真度（如音符匹配）和代码可读性（如循环结构使用率）。

## 📚 数据集

- Strudel-Synth（合成训练集，含配对Strudel程序与渲染MIDI）
- Lakh MIDI（真实MIDI，用于强化学习阶段）
- MAESTRO（真实MIDI，评估用）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MIDI重建保真度（F1） | MAESTRO | GPT-4o 0.72 | **Decomposer 0.85** | +0.13 |
| 代码可读性（循环使用率） | MAESTRO | Heuristic 0.10 | **Decomposer 0.45** | +0.35 |

在MAESTRO和Lakh MIDI基准上，Decomposer的MIDI重建F1达0.85，显著优于GPT-4o（0.72）和启发式方法（0.60）。代码可读性方面，循环结构使用率45%，远高于启发式方法的10%，且生成程序多样性更高。消融实验验证了强化学习阶段对可读性的关键贡献。

## 🎯 结论与影响

Decomposer首次实现从符号音乐到可读音乐程序的反编译，通过合成数据与强化学习有效解决低资源与保真度-可读性权衡问题。该工作为音乐编辑、教学和创作提供了新工具，有望推动音乐编程语言在音乐信息处理中的应用。

## ⚠️ 局限与未解决问题

依赖Strudel语言，泛化性受限；合成数据与真实音乐分布存在差异；未评估程序执行效率；强化学习奖励设计可能偏向特定风格。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
