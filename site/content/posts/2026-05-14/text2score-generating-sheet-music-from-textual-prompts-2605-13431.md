---
title: "Text2Score: Generating Sheet Music From Textual Prompts"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#ABC记谱法", "#LLM规划", "#乐谱生成", "#文本驱动音乐生成", "#符号音乐生成"]
summary: "Text2Score提出两阶段框架，先由LLM将文本提示转为结构化乐谱规划，再由生成模型输出ABC记谱法，无需文本-乐谱对齐数据，在客观和主观指标上优于纯LLM和端到端基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#符号音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本驱动音乐生成</span> <span class="tag-pill tag-pill-soft">#乐谱生成</span> <span class="tag-pill tag-pill-soft">#LLM规划</span> <span class="tag-pill tag-pill-soft">#ABC记谱法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13431</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13431" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13431" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://keshavbhandari.github.io/portfolio/text2score" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Text2Score提出两阶段框架，先由LLM将文本提示转为结构化乐谱规划，再由生成模型输出ABC记谱法，无需文本-乐谱对齐数据，在客观和主观指标上优于纯LLM和端到端基线。
</div>

## 👥 作者与机构

**Keshav Bhandari** ¹ · Sungkyun Chang · Abhinaba Roy · Francesca Ronchini · Emmanouil Benetos · Dorien Herremans · Simon Colton

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事符号音乐生成、文本到音乐生成的研究者。建议重点阅读§3（两阶段框架）和§4（评估框架），尤其是表2和表3的对比结果。可跳过§2相关工作。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从自然语言描述生成可演奏的乐谱。 |
| **核心创新** | 提出两阶段规划-执行框架，避免文本-乐谱对齐数据需求 · 利用LLM将文本转为结构化节拍级规划，约束生成过程 · 引入包含可演奏性、可读性等多维度的评估框架 |
| **模型架构** | 输入自然语言提示 → LLM规划器（如GPT-4）生成节拍级规划（包含乐器、调号、拍号、和声等） → 执行阶段生成模型（基于Transformer）以规划为条件生成ABC记谱法 → 输出乐谱。参数量未明确给出。 |
| **数据集** | 自建数据集（训练，包含ABC乐谱及对应规划） · 评估集（专家标注，用于主观评估） |
| **关键结果** | 在客观指标（如可演奏性、提示遵循度）和主观专家评分上，Text2Score优于纯LLM基线（GPT-4直接生成）和三个端到端基线（如MusicGen、MuseNet）。具体数值摘要未给出，但声称一致超越。 |

## 🔗 开源资源

- **项目主页**：<https://keshavbhandari.github.io/portfolio/text2score>
- **Demo / 试听**：<https://keshavbhandari.github.io/portfolio/text2score>

## 🎯 与本站重点领域的关联

与本站五个重点领域无直接关联。但两阶段规划-执行框架可迁移至语音增强或分离任务，例如用LLM规划噪声类型或说话人属性，再指导生成模型。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟和模型参数量；执行阶段生成模型可能受限于ABC记谱法的表现力；评估集规模较小且依赖专家主观评分，客观指标可能不够全面。

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

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
