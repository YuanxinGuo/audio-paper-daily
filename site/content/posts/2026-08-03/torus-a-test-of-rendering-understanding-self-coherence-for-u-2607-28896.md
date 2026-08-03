---
title: "TORUS: A Test of Rendering-Understanding Self-Coherence for Unified Audio Models"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解与生成一致性评估"]
summary: "提出首个统一音频模型自一致性测试基准TORUS，包含48个三阶段测试和432个六选一问题，评估模型理解自身生成内容的能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解与生成一致性评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#统一音频模型</span> <span class="tag-pill tag-pill-soft">#自一致性</span> <span class="tag-pill tag-pill-soft">#评估基准</span> <span class="tag-pill tag-pill-soft">#音频编辑</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.28896</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.28896" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.28896" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个统一音频模型自一致性测试基准TORUS，包含48个三阶段测试和432个六选一问题，评估模型理解自身生成内容的能力。
</div>

## 👥 作者与机构

**Aryan Vijay Bhosale** ¹ · Harshit Rajgarhia · Abhishek Mukherji · Dinesh Manocha

**机构**：马里兰大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频模型研究者、评估基准构建者阅读。值得通读，重点看第3节（TORUS设计）和第4节（实验结果）。可先看表1和表2了解任务分布和模型表现。

## 🌍 研究背景

统一音频模型（如AudioLDM、AudioGen）同时具备理解、生成和编辑能力，但现有评估仅单独测试各能力，未检验模型是否理解自身生成的内容。这导致模型可能生成与理解不一致的音频，影响实际应用可靠性。本文旨在填补这一空白，提出自一致性测试，评估模型对自身输出的理解程度。

## 💡 核心创新

1. 提出首个自一致性测试基准TORUS
2. 设计三阶段测试流程（生成-编辑-理解）
3. 覆盖语音、声音、音乐五大任务族
4. 引入级联基线对比统一模型
5. 揭示统一模型在音频编辑上的不足

## 🏗️ 模型架构

TORUS为评估基准，非模型。测试流程：阶段1生成音频，阶段2编辑音频，阶段3理解音频并回答问题。评估五个开源统一模型（如AudioLDM、AudioGen等）和级联基线（结合专用生成、编辑、理解模型）。问题为六选一，共432题。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | TORUS | 级联基线 63.2% | **最佳统一模型 50.5%** | -12.7% |

最佳统一模型在TORUS上准确率50.5%，低于级联基线63.2%，但高于随机猜测16.7%。模型在音频编辑任务上表现尤其困难。所有评估模型（专用和统一）均表现出有限的自一致性，表明自一致性是未来音频系统的重要测试维度。

## 🎯 结论与影响

TORUS首次系统评估统一音频模型的自一致性，发现现有模型普遍缺乏对自身生成内容的理解能力，尤其在音频编辑上。这为未来音频模型设计提出新要求：需增强生成与理解模块的协同。对工业界，自一致性测试可作为模型发布前的质量门禁。

## ⚠️ 局限与未解决问题

基准规模有限（48测试，432题），可能未覆盖所有音频场景。评估模型数量有限，未包含最新模型。未提供模型在自一致性失败时的具体错误类型分析。未讨论测试问题设计的主观性。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
