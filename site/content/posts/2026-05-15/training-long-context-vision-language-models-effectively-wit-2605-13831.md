---
title: "Training Long-Context Vision-Language Models Effectively with Generalization Beyond 128K Context"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#持续预训练", "#数据混合策略", "#视觉语言模型", "#长上下文建模", "#长上下文视觉语言模型"]
summary: "系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布优于聚焦目标长度，并提出MMProLong模型，仅用5B token训练即可泛化至512K上下文。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#长上下文视觉语言模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#长上下文建模</span> <span class="tag-pill tag-pill-soft">#视觉语言模型</span> <span class="tag-pill tag-pill-soft">#数据混合策略</span> <span class="tag-pill tag-pill-soft">#持续预训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13831</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13831" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13831" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统研究长上下文视觉语言模型的持续预训练策略，发现长文档VQA优于OCR转录，平衡数据分布优于聚焦目标长度，并提出MMProLong模型，仅用5B token训练即可泛化至512K上下文。
</div>

## 👥 作者与机构

**Zhaowei Wang** ¹ · Lishu Luo · Haodong Duan · Weiwei Liu · Sijin Wu · Ji Luo · Shen Yan · Shuai Peng · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事长上下文LVLM训练、多模态文档理解的研究者。建议通读全文，重点看§3的消融实验和§4的泛化结果。可先看表2和表3了解关键发现。

## 🌍 研究背景

长上下文建模是LVLM的核心能力，但训练策略尚未充分探索。现有方法多依赖OCR转录或简单数据混合，缺乏对数据分布、任务平衡的系统研究。本文旨在通过消融实验，揭示长文档VQA、序列长度分布、检索与推理数据比例等关键因素对长上下文能力的影响，并提出高效训练配方。

## 💡 核心创新

1. 发现长文档VQA比OCR转录更有效
2. 平衡序列长度分布优于聚焦目标长度
3. 检索密集型数据混合优于推理密集型
4. 纯长文档VQA可保持短上下文能力
5. 提出MMProLong模型，5B token训练泛化至512K

## 🏗️ 模型架构

基于Qwen2.5-VL-7B，采用ViT视觉编码器+Qwen2.5语言模型。持续预训练阶段使用长文档VQA数据，序列长度从32K扩展至128K。关键模块包括视觉-语言投影层和长上下文注意力机制。模型参数量7B，训练token预算5B。

## 📚 数据集

- 长文档VQA数据集（训练，包含多种文档类型）
- OCR转录数据集（消融对比）
- 短上下文VQA数据集（评估短上下文保持）
- 多模态针检索数据集（评估长上下文泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 长文档VQA准确率 | 内部长文档VQA测试集 | Qwen2.5-VL-7B 32K基线 | **MMProLong 128K** | +7.1% |

MMProLong在128K上下文内长文档VQA提升7.1%，且无需额外训练即可泛化至256K和512K上下文。在网页多模态针检索、长上下文视觉文本压缩、长视频理解等任务上也表现优异，验证了训练策略的通用性。消融实验表明平衡数据分布和检索密集型混合是关键。

## 🎯 结论与影响

本文通过系统消融实验，提出了高效的长上下文LVLM训练配方，证明长文档VQA数据、平衡序列分布和检索密集型混合是核心要素。MMProLong仅用5B token训练即可实现强泛化，为长上下文LVLM的实用化提供了经验基础，对多模态文档理解和视频分析等应用有重要影响。

## ⚠️ 局限与未解决问题

实验仅基于Qwen2.5-VL-7B，未验证在其他架构（如LLaVA）上的可迁移性。训练数据未公开，可能影响复现。未报告推理延迟和显存占用等效率指标。长上下文泛化至512K但未测试更长上下文。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
