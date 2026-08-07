---
title: "Teaching Nemotron Greek: Mining a Corpus, Adapting Retrieval, and Grounding Generation for Modern Greek across Specialist Domains"
date: 2026-08-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#检索增强生成"]
summary: "针对现代希腊语，端到端适配Nemotron检索栈，构建HERA基准，显著提升检索与生成质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#检索增强生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#希腊语</span> <span class="tag-pill tag-pill-soft">#检索模型</span> <span class="tag-pill tag-pill-soft">#重排序</span> <span class="tag-pill tag-pill-soft">#生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05138</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05138" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05138" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对现代希腊语，端到端适配Nemotron检索栈，构建HERA基准，显著提升检索与生成质量。
</div>

## 👥 作者与机构

**Ayoub Kirouane** ¹ · Christos Petrocheilos

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多语言RAG、信息检索和低资源语言处理的读者。建议重点阅读第3节（语料挖掘与训练数据构建）和第4节（检索与重排序实验），以及第5节（生成实验）。可先看摘要中的关键结果表，再深入方法细节。

## 🌍 研究背景

现代希腊语在NVIDIA的Nemotron检索模型和主流多语言检索基准中缺失，但法律、能源、金融和医疗等领域对RAG有重要需求。现有密集检索模型在专业希腊语语料上表现不佳，甚至不如BM25基线。本文旨在通过端到端适配Nemotron检索栈，包括语料挖掘、合成监督、检索模型训练、重排序器适配和读者微调，填补这一空白，并引入首个大规模希腊语RAG基准HERA。

## 💡 核心创新

1. 构建HERA基准，首个大规模希腊语RAG基准
2. 挖掘专业领域希腊语语料，生成65,773个检索训练对
3. 微调Nemotron 1B嵌入器，nDCG@10从0.362提升至0.835
4. 适配交叉编码器重排序器，跨领域一致改进
5. LoRA微调Nemotron 30B-A3B MoE读者，答案正确率从29.4%提升至66.9%

## 🏗️ 模型架构

输入为查询和文档对，使用BM25作为基线。检索模型采用Nemotron 1B嵌入器，通过对比学习微调。重排序器为交叉编码器，基于微调后的嵌入器输出进行排序。生成部分使用Nemotron 30B-A3B MoE模型，通过LoRA微调进行接地生成。整体流程：语料挖掘→合成监督→检索模型训练→重排序器适配→读者微调。

## 📚 数据集

- HERA（评估基准，涵盖法律、能源、金融、医疗领域）
- 专业希腊语语料（训练，65,773个检索对）
- 通用领域希腊语语料（评估泛化性）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| nDCG@10 | HERA | 未适配Nemotron 1B 0.362 | **适配后0.835** | +0.473 |
| 答案正确率 | HERA | 未微调读者 29.4% | **LoRA微调后66.9%** | +37.5% |

实验表明，BM25基线在专业希腊语语料上优于多个现成的多语言密集检索模型。微调后的Nemotron 1B嵌入器在HERA上nDCG@10从0.362提升至0.835，显著优于未适配版本。学习到的语言能力可迁移至通用领域希腊语，但相对BM25的优势仍依赖领域。重排序器适配带来一致改进。LoRA微调的读者模型将答案正确率从29.4%提升至66.9%，同时显著提高忠实度和引用质量。

## 🎯 结论与影响

本文通过端到端适配Nemotron检索栈，成功填补了现代希腊语在RAG中的空白，HERA基准和开源模型为后续研究提供了基础。最强结论是微调后的检索模型和读者模型在专业领域取得显著提升，展示了低资源语言适配的可行性。对工业界，该方法可推广至其他低资源语言，支持多语言RAG系统落地。

## ⚠️ 局限与未解决问题

作者未明确讨论局限，但可看出：优势相对BM25依赖领域，通用领域提升有限；未报告推理延迟和计算成本；未与更多最新多语言模型对比；HERA基准规模虽大但覆盖领域有限，可能引入领域偏差。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-07/">← 返回 2026-08-07 速递</a></div>
