---
title: "Towards Unified Song Generation and Singing Voice Conversion with Accompaniment Co-Generation"
date: 2026-06-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出UniSinger，首个统一歌声生成与伴奏协同生成SVC的端到端框架，实现零样本说话人克隆与跨任务音色控制。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#歌唱声音转换</span> <span class="tag-pill tag-pill-soft">#歌声生成</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span> <span class="tag-pill tag-pill-soft">#多任务学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07015</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07015" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07015" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出UniSinger，首个统一歌声生成与伴奏协同生成SVC的端到端框架，实现零样本说话人克隆与跨任务音色控制。
</div>

## 👥 作者与机构

**Ziyu Zhang** ¹ · Chunyu Qiang · Xiaopeng Wang · Yuxin Guo · Kang Yin · Wenjie Tian · Jingbin Hu · Tianlun Zuo · … 等 5 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成与SVC方向的研究者。建议通读，重点看§3.2统一说话人嵌入空间和§3.3课程学习策略。可复现实验部分对比结果。

## 🌍 研究背景

歌声生成和歌唱声音转换（SVC）长期独立发展：歌声生成缺乏零样本说话人克隆能力，而SVC忽略人声与伴奏的协同生成。现有方法多针对单一任务，无法同时实现高质量歌声合成与音色迁移。本文旨在构建统一框架，同时解决零样本克隆与伴奏协同生成问题。

## 💡 核心创新

1. 基于多模态扩散Transformer构建统一框架
2. 统一说话人嵌入空间实现跨任务音色控制
3. 课程学习策略缓解多任务优化冲突
4. 任务特定模态掩码引导生成机制

## 🏗️ 模型架构

输入为文本/参考音频/说话人嵌入等多模态条件，主干采用多模态扩散Transformer。关键模块包括：统一说话人嵌入空间（将SVC说话人表示迁移至歌声生成）、任务特定模态掩码（控制语义、音色、伴奏的生成）。输出为歌声波形或转换后的歌声。参数量未提及。

## 📚 数据集

- 训练数据集未明确提及（推测为内部数据集）
- 评估数据集未明确提及

## 📊 实验结果

摘要未提供具体数值指标，仅声称在两个任务上达到SOTA并实现互补优势。缺乏定量结果，需参考全文实验部分。

## 🎯 结论与影响

UniSinger首次统一歌声生成与伴奏协同生成SVC，通过共享嵌入空间和课程学习实现跨任务音色控制与性能提升。该工作为智能音乐制作提供了新范式，有望推动歌声合成与转换的融合。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：缺乏公开数据集和客观指标对比；多任务优化冲突的缓解策略可能依赖特定数据分布；零样本克隆的泛化能力未充分验证。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-16/">← 返回 2026-06-16 速递</a></div>
