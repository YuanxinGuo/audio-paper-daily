---
title: "PASE: Leveraging the Phonological Prior of WavLM for Low-Hallucination Generative Speech Enhancement"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出PASE，利用WavLM的音韵先验进行生成式语音增强，显著降低语言和声学幻觉，提升感知质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生成式语音增强</span> <span class="tag-pill tag-pill-soft">#幻觉抑制</span> <span class="tag-pill tag-pill-soft">#WavLM</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.13300</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.13300" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.13300" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出PASE，利用WavLM的音韵先验进行生成式语音增强，显著降低语言和声学幻觉，提升感知质量。
</div>

## 👥 作者与机构

**Xiaobin Rong** ¹ · Qinwen Hu · Mansur Yesilbursa · Kamil Wojcicki · Jing Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、生成模型和预训练模型应用研究者。建议通读，重点看第3节方法（PASE框架）和第4节实验（表1-3）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

生成式语音增强（SE）在感知质量上优于判别式方法，但现有方法在严重噪声下易产生幻觉，导致内容错误或说话人特征不一致。语言幻觉源于模型未能约束有效音韵结构，而现有方法从噪声损坏表示中学习，污染先验。本文利用预训练WavLM的鲁棒音韵先验，通过表示蒸馏和双流表示训练，缓解幻觉。

## 💡 核心创新

1. 将WavLM适配为去噪专家，通过表示蒸馏清洁最终层特征
2. 利用WavLM内在音韵先验引导去噪，减少语言幻觉
3. 双流表示训练声码器：高层音素表示提供干净语言内容，低层声学表示保留说话人身份和韵律
4. 提出PASE框架，同时降低语言和声学幻觉
5. 在感知质量上超越SOTA判别式模型，并显著优于先前生成模型

## 🏗️ 模型架构

PASE采用生成式SE框架，输入含噪语音，首先通过预训练WavLM提取特征，并适配为去噪专家（通过表示蒸馏清洁最终层特征）。然后，声码器采用双流表示：高层音素表示（来自WavLM）提供干净语言内容，低层声学表示保留说话人身份和韵律。最终输出增强语音。

## 📊 实验结果

摘要未提供具体数值，但声称PASE在感知质量上超越SOTA判别式模型，并显著优于先前生成模型，同时大幅降低语言和声学幻觉。具体指标和数据集未提及。

## 🎯 结论与影响

PASE通过利用WavLM的音韵先验，有效缓解了生成式SE中的幻觉问题，在感知质量上取得领先。该工作为生成式SE提供了新思路，即利用预训练模型的内在结构先验来约束生成过程，对后续研究有重要影响。工业上，可提升助听器和语音通信在噪声环境下的可懂度和自然度。

## ⚠️ 局限与未解决问题

摘要未提供实验细节，如数据集、基线、消融等，无法评估泛化性和计算开销。未报告推理延迟，可能影响实时应用。未讨论对未见噪声类型的鲁棒性。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
