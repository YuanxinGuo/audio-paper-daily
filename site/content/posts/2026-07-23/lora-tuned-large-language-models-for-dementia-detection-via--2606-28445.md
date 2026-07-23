---
title: "LoRA-Tuned Large Language Models for Dementia Detection via Multi-View Speech-Derived Features"
date: 2026-07-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#痴呆症检测"]
summary: "提出用LoRA微调LLM，融合ASR转录、停顿标记、话题线索、时间流畅度和音序等多视图语音特征进行痴呆症检测，在ADReSSo上F1达90.14%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#痴呆症检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分析</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#低秩适应</span> <span class="tag-pill tag-pill-soft">#多视图推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.28445</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.28445" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.28445" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出用LoRA微调LLM，融合ASR转录、停顿标记、话题线索、时间流畅度和音序等多视图语音特征进行痴呆症检测，在ADReSSo上F1达90.14%。
</div>

## 👥 作者与机构

**Jonghyeon Park** ¹ · Olivier Jiyoun Jung · Myungwoo Oh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音健康监测和LLM应用研究者阅读。重点看§3多视图提示设计和§4消融实验。可先看表1结果，再读§3.2特征编码细节。

## 🌍 研究背景

痴呆症早期检测对及时干预至关重要。自发语音作为非侵入性筛查手段，传统方法多聚焦单一维度（如声学特征、停顿建模、ASR转录或融合），难以整合异质认知症状。本文提出用LoRA微调LLM，通过统一提示编码ASR转录（含停顿）、话题线索、时间流畅度和音序四个互补视图，实现结构化多视图推理，避免专用编码器或后期融合。

## 💡 核心创新

1. 多视图语音特征统一提示编码
2. LoRA微调LLM实现跨视图推理
3. 无需专用编码器或后期融合
4. 音序特征首次用于痴呆症检测

## 🏗️ 模型架构

输入为四个视图的文本化特征：ASR转录（含停顿标记）、话题线索（LDA主题分布）、时间流畅度统计（语速、停顿时长等）、音序（音素序列）。这些特征拼接成统一提示，输入预训练LLM（如Llama2），通过LoRA低秩适配器微调，输出痴呆症分类结果。模型参数量取决于基座LLM，LoRA仅更新少量参数。

## 📚 数据集

- ADReSSo（评估，包含痴呆症和健康对照自发语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| F1-score | ADReSSo | 未明确给出最佳基线值 | **90.14%** | 未提供 |

在ADReSSo上，最佳模型F1达90.14%。消融实验证实每个视图均有互补贡献，移除任一视图均导致性能下降。未报告与其他SOTA方法的直接对比，但结果具有竞争力。

## 🎯 结论与影响

本文证明LoRA微调LLM可有效融合多视图语音特征用于痴呆症检测，F1达90.14%。该方法简化了传统多模态融合流程，为语音健康筛查提供了新范式。未来可扩展至其他神经退行性疾病检测，并探索更丰富的语音特征。

## ⚠️ 局限与未解决问题

仅在ADReSSo单一数据集上评估，泛化性未知；未与现有SOTA方法（如专用声学模型或融合模型）进行直接对比；未报告推理延迟或计算开销；音序特征的有效性需进一步验证。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-23/">← 返回 2026-07-23 速递</a></div>
