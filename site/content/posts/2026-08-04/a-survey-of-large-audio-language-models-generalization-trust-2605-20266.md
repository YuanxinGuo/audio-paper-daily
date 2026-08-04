---
title: "A Survey of Large Audio Language Models: Generalization, Trustworthiness, and Outlook"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频大语言模型综述"]
summary: "全面综述音频大语言模型（LALMs）的架构、对齐算法及可信赖性风险，提出防御路线图。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频大语言模型综述</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#可信赖性</span> <span class="tag-pill tag-pill-soft">#安全</span> <span class="tag-pill tag-pill-soft">#综述</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.20266</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Kwwwww74/Awesome-Trustworthy-AudioLLMs" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Kwwwww74/Awesome-Trustworthy-AudioLLMs</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.20266" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.20266" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Kwwwww74/Awesome-Trustworthy-AudioLLMs" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>全面综述音频大语言模型（LALMs）的架构、对齐算法及可信赖性风险，提出防御路线图。
</div>

## 👥 作者与机构

**Kaiwen Luo** ¹ · Zhenhong Zhou · Leyan Wang · Liang Lin · Tianyu Shao · Yuanhe Zhang · Yang Xiao · Yuxuan Li · … 等 27 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频与多模态大模型研究者、安全领域学者。建议重点阅读第3节（架构与对齐）、第4节（可信赖性分类）及第6节（防御路线图）。可先浏览摘要与图表，再深入相关章节。

## 🌍 研究背景

大语言模型（LLMs）推动了多模态大语言模型（MLLMs）的发展，其中音频大语言模型（LALMs）是实现通用听觉智能的关键。尽管LALMs性能显著，但其能力提升远超可信赖性框架的发展，导致安全风险。现有综述多关注性能，缺乏对LALMs内生机制及可信赖性问题的系统分析。本文旨在填补这一空白，全面梳理LALMs的架构创新、对齐算法，并建立可信赖性分类体系，评估风险。

## 💡 核心创新

1. 首次系统分析LALMs内生机制与可信赖性
2. 建立涵盖六维度的可信赖性分类体系
3. 提出跨模态越狱、声学后门等风险分类
4. 提出Defense-in-Depth防御架构路线图
5. 整合最新LALMs并开源项目资源

## 🏗️ 模型架构

本文为综述，不提出新模型。其分析框架包括：LALMs的架构演进（从模块化到端到端）、对齐算法（如指令微调、RLHF）、以及可信赖性评估体系。具体涵盖语音编码器（如Whisper）、主干网络（如Qwen-Audio）、输出层等。综述通过六支柱（幻觉、鲁棒性、安全性、隐私、公平性、认证）评估LALMs。

## 📊 实验结果

本文为综述，未提供实验数据。但通过分析现有LALMs，指出攻击面成熟而防御不足，强调可信赖性差距。综述总结了当前LALMs在幻觉、鲁棒性等方面的脆弱性，并呼吁加强防御研究。

## 🎯 结论与影响

本文系统梳理了LALMs的架构与可信赖性风险，指出当前攻击与防御的不平衡。提出Defense-in-Depth、因果听觉世界建模等方向，为构建可靠音频智能提供路线图。对后续研究具有重要指导意义，推动LALMs安全落地。

## ⚠️ 局限与未解决问题

作为综述，未提供实证实验。可能受限于文献覆盖范围，对某些新兴风险分析不足。此外，防御路线图缺乏具体实现细节，可操作性有待验证。

## 🔗 开源资源

- **代码**：<https://github.com/Kwwwww74/Awesome-Trustworthy-AudioLLMs>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
