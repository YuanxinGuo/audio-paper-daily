---
title: "Unsupervised Speech Enhancement via Drifting"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出输入条件化漂移方法，在非配对无监督语音增强中通过锚编码器和键编码器保留输入的语言内容与说话人身份。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#无监督学习</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.34662</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.34662" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.34662" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出输入条件化漂移方法，在非配对无监督语音增强中通过锚编码器和键编码器保留输入的语言内容与说话人身份。
</div>

## 👥 作者与机构

**Diego Caviedes-Nozal** ¹ · Liang Xu · Rasmus Kongsgaard Olsson · W. Bastiaan Kleijn

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究无监督/非配对语音增强及生成模型（漂移、扩散）的研究者阅读。建议通读，重点看 §3 的输入条件化漂移机制（锚编码器与键编码器）以及表 1 的 WER 与说话人相似度对比。可先看 §3.2 与表 2 的消融实验，再关注 §4 在 WSJ0-REVERB 上的迁移结果。

## 🌍 研究背景

非配对语音增强旨在仅用分离的退化与干净语音集合训练，避免配对数据依赖。近期漂移方法（如 Drift 模型）虽支持非配对训练，但目标仅优化干净语音的边缘先验，导致增强器逐渐丢失输入的语言内容和说话人身份。本文要解决的核心问题是：如何在保持干净语料吸引力的同时，将输出重新锚定到退化输入，从而在无标签、无配对数据条件下保留内容与说话人信息。

## 💡 核心创新

1. 提出输入条件化漂移，通过锚编码器提供缺失的似然项，将输出拉向输入特征
2. 引入键编码器对先验进行条件化，通过重加权检索帧来保留输入信息
3. 提出无需训练的编码器选择准则，用于挑选合适的编码器
4. 在 VoiceBank-DEMAND 上实现 WER 从 11.7% 降至 10.1%，说话人相似度从 0.490 恢复至 0.879

## 🏗️ 模型架构

输入为退化语音特征，主干采用漂移生成框架。关键模块包括：锚编码器（anchor encoder）从退化输入提取特征，提供缺失的似然项，将生成输出拉向输入特征；键编码器（key encoder）对先验进行条件化，通过重加权检索帧来保留输入信息。训练目标结合干净语料的漂移先验与输入条件化项，无需标签或配对数据。编码器选择采用无需训练的准则。输出为增强后的语音波形或特征。摘要未给出具体参数量。

## 📚 数据集

- VoiceBank-DEMAND（评估，非配对训练与测试）
- WSJ0-REVERB（评估，去混响迁移）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | VoiceBank-DEMAND | 未处理 11.7% | **10.1%** | -1.6% |
| 说话人相似度 | VoiceBank-DEMAND | 0.490 | **0.879** | +0.389 |

在 VoiceBank-DEMAND 上，WER 从未处理的 11.7% 降至 10.1%，说话人相似度从 0.490 恢复至 0.879。在 WSJ0-REVERB 去混响任务上，内容指标有所改善，但渲染质量未提升。摘要未提供消融实验、效率指标或与其他无监督方法的详细对比。

## 🎯 结论与影响

本文最强结论是：输入条件化漂移能在非配对无监督设置下同时保留语言内容与说话人身份，WER 和说话人相似度均显著优于未处理基线。该工作为无监督语音增强提供了新思路，可能推动后续研究关注生成先验与输入条件化的平衡。工业落地方面，减少对配对数据的依赖可降低数据采集成本，但渲染质量在去混响任务上未提升，需进一步优化。

## ⚠️ 局限与未解决问题

作者承认在 WSJ0-REVERB 上渲染质量未提升。作为审稿人，我认为缺少与现有无监督/自监督语音增强方法的全面对比，未报告推理延迟和模型参数量，消融实验不充分，且仅在两个数据集上评估，泛化性有待验证。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
