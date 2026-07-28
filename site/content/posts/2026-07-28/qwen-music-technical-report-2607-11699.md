---
title: "Qwen-Music Technical Report"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出Qwen-Music音乐生成模型，结合语义token自回归建模与立体声渲染，在16项客观指标中13项达到SOTA。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音乐生成</span> <span class="tag-pill tag-pill-soft">#翻唱生成</span> <span class="tag-pill tag-pill-soft">#自回归模型</span> <span class="tag-pill tag-pill-soft">#扩散渲染</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.11699</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.11699" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.11699" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Qwen-Music音乐生成模型，结合语义token自回归建模与立体声渲染，在16项客观指标中13项达到SOTA。
</div>

## 👥 作者与机构

**Jin Xu** ¹ · Kangdi Wang · Ruibin Yuan · Shun Lei · Xiong Wang · Xize Cheng · Xueyao Zhang · Yang Zhang · … 等 19 人

**机构**：阿里巴巴达摩院 · 浙江大学 · 西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、音频生成方向的研究者。建议重点阅读§3.2 Melody-CoT机制和§3.3渲染模块，以及§4.2的客观评测结果。可复现性高，代码未开源但技术细节充分。

## 🌍 研究背景

音乐生成领域面临两大挑战：生成高音乐性、高保真度的歌曲，以及支持多样化的控制（如文本、旋律）。现有方法如MusicGen、Stable Audio等采用离散token或扩散模型，但在旋律规划、长程结构连贯性和音频保真度上仍有不足。本文旨在通过语义token自回归建模与渲染模块结合，提升音乐质量和可控性。

## 💡 核心创新

1. Melody-CoT机制：在生成完整歌曲前先规划旋律token序列
2. Qwen-Music-Tokenizer：25Hz单码本语义token，保留旋律信息
3. Qwen-Music-Render：基于扩散的立体声渲染，弥补离散token保真度损失
4. 渐进式后训练：监督初始化+离线DPO+在线GSPO

## 🏗️ 模型架构

输入为文本描述、歌词和音乐属性（如风格、BPM）。Qwen-Music-Tokenizer将音频压缩为25Hz单码本Music Semantic Tokens。Qwen-Music-LLM基于这些token进行自回归建模，关键创新是Melody-CoT：先生成旋律token序列（规划），再生成完整语义token序列。最后Qwen-Music-Render（基于扩散的生成式渲染）将语义token转换为高保真立体声波形。模型在500万小时多语言数据上训练。

## 📚 数据集

- 500万小时多语言音乐数据（训练，涵盖数百种语言）
- 600条中英文提示（评估，用于客观指标和主观评测）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 客观音乐性和音频质量指标（16项） | 600条中英文提示 | 领先专有系统（未具名） | **13/16项SOTA** | 未提供具体数值 |

在600条中英文提示上，Qwen-Music在16项客观指标中13项达到SOTA，包括音乐性、音频质量等。专业评估者偏好Qwen-Music超过领先专有系统。翻唱生成任务中，Qwen-Music比领先专有系统更准确地保留参考旋律。未提供具体数值和消融实验。

## 🎯 结论与影响

Qwen-Music通过语义token自回归建模与渲染模块结合，在音乐生成质量上达到SOTA，尤其Melody-CoT机制提升了旋律规划能力。对工业界音乐生成应用有直接推动作用，但未开源代码可能限制学术复现。

## ⚠️ 局限与未解决问题

未开源代码和模型权重；客观指标未给出具体数值；消融实验缺失（如Melody-CoT贡献度）；仅评估600条提示，规模有限；未与开源模型（如MusicGen）直接对比。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-28/">← 返回 2026-07-28 速递</a></div>
