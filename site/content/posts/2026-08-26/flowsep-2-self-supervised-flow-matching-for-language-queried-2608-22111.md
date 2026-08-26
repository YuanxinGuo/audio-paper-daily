---
title: "FlowSep 2: Self-Supervised Flow Matching for Language-Queried Audio Source Separation"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "FlowSep2 提出基于流匹配的生成式语言查询音频分离模型，利用自监督流匹配范式提升复杂声学场景下的分离性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语言查询音频分离</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#扩散Transformer</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.22111</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.22111" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.22111" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FlowSep2 提出基于流匹配的生成式语言查询音频分离模型，利用自监督流匹配范式提升复杂声学场景下的分离性能。
</div>

## 👥 作者与机构

**Yi Yuan** ¹ · Xubo Liu · Haohe Liu · Xiyuan Kang · Mark D. Plumbley · Wenwu Wang

**机构**：萨里大学 · 伦敦玛丽女王大学 · 香港中文大学（深圳）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频分离、生成模型研究者阅读。建议重点看第3节方法部分（FlowSep2架构与Self-Flow）以及第4节实验对比。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

语言查询音频源分离（LASS）旨在根据自然语言描述从混合音频中提取目标源，提供灵活接口。现有方法多为判别式掩码模型，在复杂声学场景中易过度抑制或分离不彻底。FlowSep2 提出生成式流匹配方法，从噪声生成目标源表示，以改善重叠声音事件的分离效果。

## 💡 核心创新

1. 采用流匹配生成范式替代掩码预测
2. 引入Diffusion Transformer作为主干网络
3. 提出Self-Flow自监督流匹配范式
4. 在潜在空间进行条件生成，结合混合表示与文本查询

## 🏗️ 模型架构

FlowSep2 采用文本条件流匹配生成模型。输入为混合音频的潜在表示和文本查询嵌入，通过Diffusion Transformer主干网络，从高斯噪声逐步生成目标源表示。使用整流流匹配（rectified flow matching）训练，并引入Self-Flow自监督范式增强语义结构。输出为分离的目标源表示，再解码为音频波形。

## 📊 实验结果

摘要未提供具体数值，但声称在多个LASS基准上达到最先进性能，并在重叠声音事件挑战场景中展示增强的分离效果。

## 🎯 结论与影响

FlowSep2 通过生成式流匹配方法显著提升语言查询音频分离性能，尤其在复杂重叠场景。该工作为LASS提供了新范式，可能推动生成模型在音频分离中的应用，对工业界灵活音频编辑有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为审稿人，可能缺少与判别式方法的计算效率对比，未报告推理延迟，且未提供消融实验细节。此外，生成模型可能引入额外推理开销。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
