---
title: "Domain-Incremental Learning for Generative Speech Enhancement"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出基于语言模型生成式语音增强骨干的域增量学习框架，用轻量 LoRA 适配新声学域，缓解灾难性遗忘。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#持续学习</span> <span class="tag-pill tag-pill-soft">#生成模型</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.34901</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.34901" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.34901" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于语言模型生成式语音增强骨干的域增量学习框架，用轻量 LoRA 适配新声学域，缓解灾难性遗忘。
</div>

## 👥 作者与机构

**Manjunath Mulimani** ¹ · Annamaria Mesaros · Minje Kim · Jesper Rindom Jensen

**机构**：坦佩雷大学 · 印第安纳大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强落地与持续学习的研究者。建议通读，重点看 §3 的生成式 SE 骨干设计与 LoRA 域适配机制，以及四个异构数据集上的遗忘-适应权衡实验表。若关注参数高效微调，可先看 LoRA 插入位置与秩的消融。

## 🌍 研究背景

语音增强在匹配域上已由判别式与生成式方法（如基于扩散、语言模型先验的 SE）取得较好效果，但真实部署中声学域持续变化。直接微调预训练模型会导致对旧域的灾难性遗忘，零样本泛化又难以适配新域。本文要解决的是：在连续到来的异构声学域上增量学习增强能力，同时不遗忘已学域。

## 💡 核心创新

1. 提出基于语言模型的生成式 SE 骨干作为预训练模型
2. 用域特定 LoRA 做轻量增量适配，冻结主干
3. 面向声学失配域的域增量学习框架，兼顾新域适应与旧域保持

## 🏗️ 模型架构

输入为含噪语音特征，主干为语言模型式生成式语音增强网络（摘要未给出具体层数与参数量），以预训练权重初始化并冻结。每个新域仅训练一组轻量域特定 Low-Rank Adaptation 参数，插入主干线性层，实现低秩增量更新。推理时按域选择对应 LoRA，输出增强语音。整体为生成式建模，未披露具体 tokenizer 或解码细节。

## 📚 数据集

- 四个异构语音数据集（训练与增量学习，具体名称摘要未给出）
- 四个异构语音数据集（评估域适应与遗忘，具体名称摘要未给出）

## 📊 实验结果

摘要仅说明在四个异构语音数据集上评估，方法能有效适应新域且不遗忘旧域，未给出 SI-SDR、PESQ 等具体数值，也未报告参数量、推理延迟或与持续学习基线的定量对比。

## 🎯 结论与影响

最强结论是：域特定 LoRA 加冻结生成式 SE 骨干可在多域序列上实现无遗忘的增量增强。这为语音增强的持续部署提供了参数高效路径，后续可探索域自动识别与 LoRA 合并。工业上利于边缘端按域切换小适配器，降低重训成本。

## ⚠️ 局限与未解决问题

摘要未给出任何定量指标、基线对比与消融，无法判断相对零样本与全量微调的增益幅度；域数量仅四个，域边界与域 ID 是否已知未说明；未报告推理延迟与 LoRA 存储开销。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
