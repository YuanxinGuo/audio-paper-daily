---
title: "MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech"
date: 2026-08-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "MINT-Bench 是一个多语言指令跟随 TTS 的综合基准，通过分层多轴分类和混合评估协议，系统评估内容一致性、指令遵循和感知质量。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#指令跟随TTS</span> <span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#评估协议</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.17958</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://aslp-lab.github.io/MINT-Bench-Demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">aslp-lab.github.io/MINT-Bench-Demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://aslp-lab.github.io/MINT-Bench-Demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">aslp-lab.github.io/MINT-Bench-Demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.17958" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.17958" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://aslp-lab.github.io/MINT-Bench-Demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://aslp-lab.github.io/MINT-Bench-Demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MINT-Bench 是一个多语言指令跟随 TTS 的综合基准，通过分层多轴分类和混合评估协议，系统评估内容一致性、指令遵循和感知质量。
</div>

## 👥 作者与机构

**Huakang Chen** ¹ · Jingbin Hu · Liumeng Xue · Qirui Zhan · Wenhao Li · Guobin Ma · Hanke Xie · Dake Guo · … 等 7 人

**机构**：西北工业大学 · 阿里巴巴达摩院 · 腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合 TTS 研究者、评估方法学者及工业界 TTS 开发者。建议通读，重点看 §3 数据构建和 §4 评估协议，以及 §5 实验结果。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

指令跟随 TTS 旨在根据自然语言指令生成可控、表现力丰富的语音，但现有评估存在覆盖有限、诊断粒度弱、多语言支持不足等问题。此前缺乏系统性的基准，导致不同模型难以公平比较，也无法定位具体能力短板。MINT-Bench 旨在填补这一空白，提供全面的多语言评估框架。

## 💡 核心创新

1. 提出分层多轴分类法，覆盖内容、指令、质量多维度
2. 构建可扩展的多阶段数据构建流程，支持多语言
3. 设计分层混合评估协议，联合评估内容一致性、指令遵循和感知质量
4. 在十种语言上系统评估商业和开源模型，揭示性能差距
5. 发布基准和工具包，支持可控、多语言、诊断性 TTS 评估

## 🏗️ 模型架构

MINT-Bench 是一个评估基准，而非单一模型。其架构包括：分层多轴分类法定义评估维度；多阶段数据构建流程生成测试样本；分层混合评估协议结合自动指标和人工评估，从内容一致性、指令遵循和感知质量三个层面打分。

## 📚 数据集

- MINT-Bench（评估，十种语言，具体规模未提及）

## 📊 实验结果

摘要指出在十种语言上的实验显示当前系统远未解决：前沿商业系统整体领先，但领先开源模型在中文等本地化场景中极具竞争力甚至超越商业模型。更难的组合性和副语言控制仍是主要瓶颈。具体指标数值未在摘要中给出。

## 🎯 结论与影响

MINT-Bench 提供了全面的多语言指令跟随 TTS 评估框架，揭示了当前系统的能力边界和瓶颈，特别是组合性和副语言控制。该基准有望推动可控、多语言 TTS 评估的标准化，对工业界模型选型和改进具有指导意义。

## ⚠️ 局限与未解决问题

摘要未提及具体局限。作为基准，可能受限于测试集覆盖范围、人工评估成本、以及自动评估指标与主观感知的相关性。此外，语言覆盖虽广，但可能未涵盖所有方言或低资源语言。

## 🔗 开源资源

- **项目主页**：<https://aslp-lab.github.io/MINT-Bench-Demo/>
- **Demo / 试听**：<https://aslp-lab.github.io/MINT-Bench-Demo/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-22/">← 返回 2026-08-22 速递</a></div>
