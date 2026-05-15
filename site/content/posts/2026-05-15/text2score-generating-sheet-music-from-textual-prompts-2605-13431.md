---
title: "Text2Score: Generating Sheet Music From Textual Prompts"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#ABC记谱法", "#两阶段框架", "#乐谱生成", "#文本驱动音乐生成", "#符号音乐生成"]
summary: "Text2Score提出两阶段框架，先由LLM将文本提示转为结构化乐谱计划，再由生成模型输出ABC记谱法乐谱，在客观和主观指标上优于纯LLM和端到端基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#符号音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本驱动音乐生成</span> <span class="tag-pill tag-pill-soft">#乐谱生成</span> <span class="tag-pill tag-pill-soft">#两阶段框架</span> <span class="tag-pill tag-pill-soft">#ABC记谱法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13431</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13431" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13431" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Text2Score提出两阶段框架，先由LLM将文本提示转为结构化乐谱计划，再由生成模型输出ABC记谱法乐谱，在客观和主观指标上优于纯LLM和端到端基线。
</div>

## 👥 作者与机构

**Keshav Bhandari** ¹ · Sungkyun Chang · Abhinaba Roy · Francesca Ronchini · Emmanouil Benetos · Dorien Herremans · Simon Colton

**机构**：Queen Mary University of London · Singapore University of Technology and Design

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事符号音乐生成、文本到音乐生成的研究者阅读。建议重点看§3的两阶段框架设计和§4的评估框架，尤其是表1和表2的对比结果。可先浏览项目页面demo再深入论文。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从自然语言描述生成可演奏的乐谱。 |
| **核心创新** | 提出两阶段框架分离规划与执行，避免文本-乐谱对齐问题 · 利用符号XML数据提供监督信号，绕过噪声文本-音乐对 · 设计包含可演奏性、可读性等多维度的评估框架 |
| **模型架构** | 输入自然语言提示 → 规划阶段：LLM orchestrator（如GPT-4）生成结构化measure-wise计划（含乐器、调性、拍号、和声等）→ 执行阶段：基于Transformer的生成模型（如MusicGen变体）以计划为条件生成ABC记谱法序列 → 输出乐谱。参数量未明确给出。 |
| **数据集** | 自建文本-乐谱数据集（训练规划阶段） · 符号XML数据集（训练执行阶段） |
| **关键结果** | 在客观指标上，Text2Score在可演奏性（100% vs 基线最高85%）、乐器利用率（0.92 vs 0.75）等方面显著领先；主观专家评估中，在可读性、结构复杂度、提示遵循度上均优于纯LLM框架和三个端到端基线。具体数值见论文表1和表2。 |

## 🔗 开源资源

- **项目主页**：<https://keshavbhandari.github.io/portfolio/text2score>
- **Demo / 试听**：<https://keshavbhandari.github.io/portfolio/text2score>

## 🎯 与本站重点领域的关联

与本站5个重点领域无直接关联。但两阶段框架（规划+执行）可迁移至语音增强中的条件生成任务，例如先由LLM规划噪声类型和增强策略，再由声学模型执行。

## ⚠️ 局限与未解决问题

执行阶段生成模型基于ABC记谱法，未直接输出标准五线谱；评估数据集规模较小（约100条提示）；未报告推理延迟；LLM规划阶段依赖外部API（如GPT-4），可能引入成本和不稳定性。

## 📋 引用

```bibtex
@article{bhandari20262605,
  title  = {Text2Score: Generating Sheet Music From Textual Prompts},
  author = {Keshav Bhandari and  Sungkyun Chang and  Abhinaba Roy and  Francesca Ronchini and  Emmanouil Benetos and  Dorien Herremans and  Simon Colton},
  journal = {arXiv preprint arXiv:2605.13431},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
