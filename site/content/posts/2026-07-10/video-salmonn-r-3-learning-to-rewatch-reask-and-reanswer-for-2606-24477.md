---
title: "video-SALMONN-R$^3$: Learning to ReWatch, ReAsk, and ReAnswer for Efficient Video Understanding"
date: 2026-07-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频理解"]
summary: "提出首个端到端视频LLM，通过强化学习实现重看机制，无需链式思维冷启动，提升视频问答准确性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频大语言模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#重看机制</span> <span class="tag-pill tag-pill-soft">#问答</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24477</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24477" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24477" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个端到端视频LLM，通过强化学习实现重看机制，无需链式思维冷启动，提升视频问答准确性。
</div>

## 👥 作者与机构

**Yixuan Li** ¹ · Guangzhi Sun · Yudong Yang · Chao Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合视频理解与多模态LLM研究者。建议通读，重点看§3的ReWatch、ReAsk、ReAnswer策略及§4的实验结果。可先看表1与图2了解性能提升。

## 🌍 研究背景

视频大语言模型受限于计算和内存，通常使用低帧率和低分辨率，可能遗漏关键信息。现有方法采用两阶段范式：先粗理解定位相关片段，再高保真重看。但依赖链式思维冷启动和昂贵标注。本文旨在设计端到端视频LLM，通过强化学习实现重看，避免CoT退化。

## 💡 核心创新

1. 提出ReWatch机制，通过强化学习学习何时重看
2. 提出ReAnswer策略，先直接回答再精炼
3. 提出ReAsk机制，重看时重新注入查询
4. 无需CoT冷启动和SFT，保持预训练能力

## 🏗️ 模型架构

基于视频-SALMONN架构，输入视频帧和音频特征，主干为预训练视频LLM。ReWatch模块通过强化学习策略网络决定是否重看特定片段；ReAnswer模块在首次观看后生成初步答案，重看后更新；ReAsk模块在重看时重新注入原始问题。整体端到端训练。

## 📚 数据集

- VideoQA数据集（训练与评估，具体名称未提及）
- NExT-QA（评估）
- ActivityNet-QA（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | NExT-QA | 基线模型（未重看） | **video-SALMONN-R³** | 提升约3% |
| 准确率 | ActivityNet-QA | 基线模型（未重看） | **video-SALMONN-R³** | 提升约2% |

实验表明，video-SALMONN-R³在NExT-QA和ActivityNet-QA上一致优于基线和QA-SFT基线，且超越先前基于重看的方法，计算成本显著降低。消融实验验证了ReWatch、ReAnswer、ReAsk各模块的有效性。

## 🎯 结论与影响

本文提出首个端到端视频LLM重看框架，通过强化学习实现高效重看，无需CoT冷启动。该方法在视频问答任务上取得一致提升，为视频理解提供新范式，有望推动工业级视频分析应用。

## ⚠️ 局限与未解决问题

未报告推理延迟和参数量；重看策略可能对长视频效率仍有挑战；仅在两个数据集评估，泛化性待验证；未与最新视频LLM（如VideoChat2）对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-10/">← 返回 2026-07-10 速递</a></div>
