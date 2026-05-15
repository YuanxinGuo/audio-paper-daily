---
title: "Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#持续预训练", "#数据混合", "#视觉语言模型", "#长上下文建模", "#长上下文视觉语言模型"]
summary: "系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布和检索优先是关键，仅用5B token将7B模型从32K扩展到128K上下文，并泛化至256K和512K。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#长上下文视觉语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#长上下文建模</span> <span class="tag-pill tag-pill-soft">#视觉语言模型</span> <span class="tag-pill tag-pill-soft">#持续预训练</span> <span class="tag-pill tag-pill-soft">#数据混合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13831</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13831" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13831" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布和检索优先是关键，仅用5B token将7B模型从32K扩展到128K上下文，并泛化至256K和512K。
</div>

## 👥 作者与机构

**Zhaowei Wang** ¹ · Lishu Luo · Haodong Duan · Weiwei Liu · Sijin Wu · Ji Luo · Shen Yan · Shuai Peng · … 等 4 人

**机构**：香港科技大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态大模型长上下文训练的研究者。建议通读，重点看§3的消融实验和§4的MMProLong结果，尤其是数据混合策略和泛化实验。可复现其数据配比方法。

## 🌍 研究背景

长上下文建模是现代大型视觉语言模型（LVLM）的核心能力，支持长文档理解、视频分析、多轮工具使用等场景。然而，实用的训练策略，特别是长上下文数据混合的设计与平衡，尚未充分探索。现有工作多依赖OCR转录数据或简单拼接，缺乏系统消融。本文旨在通过系统研究，提出有效的长上下文持续预训练方案。

## 💡 核心创新

1. 发现长文档VQA比OCR转录更有效
2. 提出平衡序列长度分布优于聚焦目标长度
3. 揭示检索是主要瓶颈，检索重混合优于推理重混合
4. 纯长文档VQA可保持短上下文能力，减少短数据混合需求
5. 仅5B token预算实现128K上下文训练，泛化至512K

## 🏗️ 模型架构

基于Qwen2.5-VL-7B模型进行长上下文持续预训练。输入为图像和文本，主干为视觉编码器+语言模型（Transformer架构）。关键模块：在预训练阶段使用长文档VQA数据，采用平衡的序列长度分布（均匀采样32K-128K），数据混合以检索任务为主（如Needle-in-a-Haystack），辅以少量推理任务。输出为文本响应。模型参数量7B，训练token预算5B。

## 📚 数据集

- 长文档VQA数据集（训练，包含多种文档类型，规模未明确）
- OCR转录数据集（训练，用于对比消融）
- 短上下文VQA数据集（评估，用于检测能力保持）
- 多模态Needle-in-a-Haystack（评估，网页版）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 长文档VQA准确率 | 内部长文档VQA测试集 | Qwen2.5-VL-7B (32K) 未明确具体值 | **MMProLong 提升7.1%** | +7.1% |

MMProLong在长文档VQA上提升7.1%，且无需额外训练即可泛化至256K和512K上下文。在网页多模态Needle检索、长上下文视觉文本压缩、长视频理解等任务上也表现出色，无需任务特定监督。消融实验表明平衡序列长度分布优于聚焦128K，检索重混合优于推理重混合，纯长文档VQA训练保持短上下文能力。

## 🎯 结论与影响

本文系统研究了长上下文LVLM的持续预训练策略，提出MMProLong，仅用5B token将7B模型从32K扩展到128K上下文，并泛化至更长序列。关键发现包括长文档VQA优于OCR、平衡数据分布和检索优先。该工作为长上下文多模态模型训练提供了实用配方，对工业界部署长上下文应用具有指导意义。

## ⚠️ 局限与未解决问题

实验仅基于Qwen2.5-VL-7B，未验证在其他架构（如LLaVA）上的泛化性。长文档VQA数据集未公开，可能影响可复现性。未报告推理延迟或显存占用。泛化至512K的评估可能不够全面，仅展示部分任务。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
