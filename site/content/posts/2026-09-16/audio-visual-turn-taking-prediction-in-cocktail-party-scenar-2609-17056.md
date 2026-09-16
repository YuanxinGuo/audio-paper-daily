---
title: "Audio-Visual Turn-taking Prediction in Cocktail Party Scenarios"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉说话人轮换预测"]
summary: "评估清洁数据训练的视听轮换预测模型在鸡尾酒会噪声场景下的泛化与微调适应行为。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉说话人轮换预测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#鸡尾酒会问题</span> <span class="tag-pill tag-pill-soft">#语音重叠</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.17056</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.17056" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.17056" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>评估清洁数据训练的视听轮换预测模型在鸡尾酒会噪声场景下的泛化与微调适应行为。
</div>

## 👥 作者与机构

**Long-Vu Hoang** ¹ · Naomi Harte

**机构**：都柏林圣三一大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究对话交互、多模态鲁棒性的读者。建议通读，重点关注域适应实验设计与跨模态对比分析。可先看实验设置与结果表格，再深入讨论部分理解音频与视觉模态的泛化差异。

## 🌍 研究背景

当前预测性轮换模型（PTTM）在受控声学条件和干净音频基准上表现良好，但其在重叠语音与背景干扰对话中的泛化能力尚未充分探索。本文针对这一空白，在基于AVCocktail数据集构建的鸡尾酒会测试台上评估清洁数据训练的视听PTTM，分析其域适应行为，旨在揭示噪声条件下音频与视觉模态的泛化与适应差异。

## 💡 核心创新

1. 构建基于AVCocktail的鸡尾酒会噪声测试台
2. 系统评估清洁训练PTTM在噪声下的跨模态退化
3. 分析微调适应增益与预训练数据量的关系

## 🏗️ 模型架构

摘要未提供具体模型架构细节，仅说明评估的是音频-视觉预测性轮换模型（PTTM），在清洁数据上训练后迁移至鸡尾酒会测试台。未提及主干网络、输入特征或参数量等具体信息。

## 📚 数据集

- AVCocktail（构建鸡尾酒会测试台，用于评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| weighted F1 | AVCocktail鸡尾酒会测试台 | 清洁条件训练模型 | **噪声条件下** | 相对下降最高38% |

实验显示音频与视觉模态在噪声条件下性能一致退化，加权F1相对下降最高达38%。在新域上微调可提升鲁棒性，但增益因模态而异，且依赖可用预训练数据规模。摘要未提供具体数值表格或消融细节。

## 🎯 结论与影响

本文最强结论是清洁数据训练的视听轮换预测模型在鸡尾酒会噪声下泛化显著下降，微调可部分缓解但模态间差异明显。这提示后续研究需发展鲁棒建模策略以适应噪声中的人类交互，对实际对话系统部署有参考意义。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、模型参数量或具体消融实验；仅基于AVCocktail单一数据集，泛化结论有限；未与噪声条件下训练的基线对比，难以判断微调策略的最优性。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
