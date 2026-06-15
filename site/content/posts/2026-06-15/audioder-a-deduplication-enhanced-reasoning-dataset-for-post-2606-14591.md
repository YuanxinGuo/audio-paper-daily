---
title: "AudioDER: A Deduplication-Enhanced Reasoning Dataset for Post-Training Large Audio-Language Models"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频推理"]
summary: "提出去重增强的音频推理数据集AudioDER，通过声学相似性去重和思维链生成提升LALM后训练效果。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#后训练</span> <span class="tag-pill tag-pill-soft">#数据去重</span> <span class="tag-pill tag-pill-soft">#思维链</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.14591</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.14591" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.14591" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出去重增强的音频推理数据集AudioDER，通过声学相似性去重和思维链生成提升LALM后训练效果。
</div>

## 👥 作者与机构

**Hui Geng** ¹ · Yi Su · Han Yin · Tianjiao Wan · Qisheng Xu · Jiaxin Chen · Zijian Gao · Hengzhu Liu · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频-语言模型训练、数据构建的研究者阅读。建议重点看§3数据构建流水线和§4实验部分，了解去重策略和CoT生成细节。若对后训练数据质量感兴趣，值得通读。

## 🌍 研究背景

大型音频语言模型在复杂音频推理任务上表现不足，后训练是提升能力的有效途径，但其效果受限于训练数据的质量和多样性。现有音频-语言数据集存在大量冗余样本，声学内容高度相似导致监督信号重叠，不仅增加标注成本，还限制语料多样性，降低后训练效率。本文旨在通过构建去重增强的推理导向数据集来解决这一问题。

## 💡 核心创新

1. 基于声学相似性的跨数据集去重流水线
2. 统一多选格式整合音频描述与问答对
3. 利用Qwen3-30B生成思维链推理监督
4. 构建约191k样本的推理导向后训练数据集AudioDER

## 🏗️ 模型架构

输入音频特征 → 声学相似性去重（基于嵌入距离）→ 统一多选格式（音频描述+问答对）→ Qwen3-30B生成CoT rationale → 输出训练样本（音频、多选问题、候选答案、音频描述、CoT）。数据集包含声音、语音、音乐三类音频，共191k样本。

## 📚 数据集

- AudioDER（训练/评估，191k样本，含声音、语音、音乐）
- MMAU-mini（评估音频推理）
- MMSU（评估音频推理）
- MMAR（评估音频推理）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MMAU-mini准确率 | MMAU-mini | Qwen2-Audio-7B-Instruct（未后训练） | **后训练AudioDER后** | 提升（具体数值未给出） |
| MMSU准确率 | MMSU | Qwen2-Audio-7B-Instruct | **后训练AudioDER后** | 提升（具体数值未给出） |
| MMAR准确率 | MMAR | Qwen2-Audio-7B-Instruct | **后训练AudioDER后** | 提升（具体数值未给出） |

实验表明，在AudioDER上后训练Qwen2-Audio-7B-Instruct后，在MMAU-mini、MMSU和MMAR三个音频推理基准上均取得一致性能提升，验证了数据去重和CoT生成的有效性。但摘要未给出具体数值，仅定性描述。

## 🎯 结论与影响

本文构建的AudioDER数据集通过去重和思维链生成显著提升了LALM的音频推理能力，为后训练数据构建提供了新范式。该工作有望推动音频推理研究，并为工业界开发更强大的音频助手提供高质量数据资源。

## ⚠️ 局限与未解决问题

摘要未报告具体提升数值，缺乏定量对比；仅测试了Qwen2-Audio-7B-Instruct一个模型，泛化性未知；未分析去重阈值对性能的影响；未提供推理延迟或计算开销。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-15/">← 返回 2026-06-15 速递</a></div>
