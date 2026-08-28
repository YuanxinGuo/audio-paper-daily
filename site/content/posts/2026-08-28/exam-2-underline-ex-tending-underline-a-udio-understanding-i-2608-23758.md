---
title: "EXAM$^2$: $\\underline{Ex}tending$ $\\underline{A}udio$ $Understanding$ $in$ $\\underline{M}ultilingual$ $and$ $\\underline{M}ultimodal$ $Analysis$"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "提出EXAM^2基准，覆盖六种语言和多种音频模态，评估并微调LALMs，显著提升多语言和多模态音频理解性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#基准测试</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.23758</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.23758" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.23758" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出EXAM^2基准，覆盖六种语言和多种音频模态，评估并微调LALMs，显著提升多语言和多模态音频理解性能。
</div>

## 👥 作者与机构

**Jiawen Wang** ¹ · Xiaoxue Gao · Zi Haur Pang · Nancy F. Chen

**机构**：新加坡科技研究局

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频理解、多模态LLM和跨语言研究的研究者。建议重点阅读第3节（基准设计）和第4节（实验与结果），可先看表1和表2了解基准构成和模型性能。

## 🌍 研究背景

近年来，大型音频语言模型（LALMs）在音频理解方面取得显著进展，但现有评估多局限于英语和单一音频域（语音、声音或音乐），缺乏对跨语言和跨模态泛化能力的系统研究。这限制了LALMs在真实场景中的应用，因为真实场景常涉及多语言和多种音频类型。本文旨在填补这一空白，通过构建多语言、多模态的音频理解基准，系统评估LALMs的泛化能力。

## 💡 核心创新

1. 构建多语言多模态音频理解基准EXAM^2，覆盖6种语言和5种音频模态
2. 引入视觉信息，实现场景感知的音频推理和跨模态理解
3. 提出Gemma3n-EXAM^2融合模型，在多语言和多模态任务上显著提升
4. 评估多种开源和专有LALMs，揭示跨语言和跨模态性能差距

## 🏗️ 模型架构

基准包含5,667道多选题，22,614个图像实例和135,684个多语言翻译。评估模型包括开源和专有LALMs（如Qwen2-Audio、Gemma3n等）以及多模态LLMs。提出的Gemma3n-EXAM^2基于Gemma3n，通过融合音频和视觉特征进行微调，输出答案。

## 📚 数据集

- EXAM^2（训练/评估，包含5,667道题，22,614图像，135,684翻译）
- 多语言音频理解测试集（评估，覆盖6种语言）
- 多模态音频理解测试集（评估，包含视觉信息）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | EXAM^2多语言测试集 | 强基线（未指定具体模型） | **Gemma3n-EXAM^2** | +12.4% |
| 准确率 | EXAM^2多模态测试集 | 强基线（未指定具体模型） | **Gemma3n-EXAM^2** | +21.7% |

实验表明，现有LALMs在多语言和跨模态理解上存在显著性能差距，而Gemma3n-EXAM^2通过微调融合模型，在多语言设置中提升12.4%，在多模态评估中提升21.7%，验证了基准的挑战性和方法的有效性。

## 🎯 结论与影响

EXAM^2作为多语言多模态音频理解基准，揭示了现有LALMs的不足，并展示了融合模型微调的潜力。该基准将推动音频智能研究向多语言和跨模态方向发展，为工业界开发更通用的音频助手提供评估标准。

## ⚠️ 局限与未解决问题

基准仅覆盖6种语言，可能未充分代表全球语言多样性；视觉信息与音频的关联可能受限于图像质量；未报告模型推理效率；对比的基线模型有限，可能未涵盖所有最新LALMs。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-28/">← 返回 2026-08-28 速递</a></div>
