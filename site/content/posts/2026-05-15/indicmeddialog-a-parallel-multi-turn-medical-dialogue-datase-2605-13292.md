---
title: "IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#低资源语言", "#医疗对话", "#参数高效微调", "#多语言数据集"]
summary: "构建了一个涵盖英语和9种印度语言的并行多轮医疗对话数据集，并基于量化小语言模型微调了IndicMedLM，实现多轮症状询问。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#医疗对话</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言数据集</span> <span class="tag-pill tag-pill-soft">#医疗对话</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13292</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13292" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13292" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建了一个涵盖英语和9种印度语言的并行多轮医疗对话数据集，并基于量化小语言模型微调了IndicMedLM，实现多轮症状询问。
</div>

## 👥 作者与机构

**Shubham Kumar Nigam** ¹ · Suparnojit Sarkar · Piyush Patel

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言NLP、医疗对话系统或低资源语言研究的读者。建议重点阅读§3数据集构建和§4模型微调部分，特别是翻译后处理流水线和参数高效微调方法。可先看表1和表2了解数据规模和语言覆盖。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 多语言医疗对话系统，支持多轮症状询问和个性化对话。 |
| **核心创新** | 构建了首个多语言多轮医疗对话数据集 · 使用LLM生成合成对话并翻译后经母语者验证 · 采用参数高效微调量化小语言模型 |
| **模型架构** | 输入为患者主诉和可选预上下文，使用量化后的Gemma-2B作为主干，通过LoRA进行参数高效微调，输出多轮症状询问和诊断建议。模型参数量约2B（量化后）。 |
| **数据集** | MDDial（基础数据集） · IndicMedDialog（构建的多语言数据集） |
| **关键结果** | 在零样本多语言基线上，IndicMedLM在BLEU、ROUGE-L等指标上平均提升5-10%，具体数值因语言而异。专家评估表明临床合理性达到可接受水平。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但数据集构建方法（LLM生成+翻译+后处理）可迁移至语音领域的多语言数据增强，例如多语言语音识别或语音翻译任务。

## ⚠️ 局限与未解决问题

数据集依赖机器翻译，虽经母语者验证但可能仍存在文化或医学术语偏差；模型仅2B参数量，复杂病例推理能力有限；未报告推理延迟和实际部署可行性。

## 📋 引用

```bibtex
@article{nigam20262605,
  title  = {IndicMedDialog: A Parallel Multi-Turn Medical Dialogue Dataset for Accessible Healthcare in Indic Languages},
  author = {Shubham Kumar Nigam and  Suparnojit Sarkar and  Piyush Patel},
  journal = {arXiv preprint arXiv:2605.13292},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
