---
title: "CARE: A Multimodal Corpus for Studying Speech and Non-Verbal Communication Across Multiple Medical Conditions"
date: 2026-07-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态语料库"]
summary: "CARE v1.0是一个包含12种医学条件和对照组的144小时多模态视频访谈语料库，提供丰富的临床元数据，支持疾病检测和语音行为分析。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态语料库</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分析</span> <span class="tag-pill tag-pill-soft">#非语言交流</span> <span class="tag-pill tag-pill-soft">#医学条件</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25903</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25903" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25903" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>CARE v1.0是一个包含12种医学条件和对照组的144小时多模态视频访谈语料库，提供丰富的临床元数据，支持疾病检测和语音行为分析。
</div>

## 👥 作者与机构

David Gimeno-G\'omez · Catarina Botelho · Carlos-D. Mart\'inez-Hinarejos · Isabel Trancoso · Alberto Abad

**机构**：瓦伦西亚理工大学 · 里斯本大学 · INESC-ID

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态语音分析、计算精神病学或临床语音研究的读者。建议重点阅读第3节（语料库设计）和第4节（元数据与标注），以了解数据规模和可用特征。若关注应用，可看第5节（示例任务）。

## 🌍 研究背景

多模态语音分析在检测神经、精神和呼吸系统疾病方面潜力巨大，但现有公开数据集规模小、疾病单一、缺乏关键混杂变量（如教育、用药、情绪）的文档，限制了可靠性和可解释性。本文旨在构建一个大规模、多疾病、元数据丰富的语料库，以推动该领域发展。

## 💡 核心创新

1. 覆盖12种医学条件加对照组，规模达144小时
2. 提供结构化元数据包括用药、生活影响、情绪等
3. 包含多模态描述符（语音、面部、身体）
4. 支持疾病检测、症状建模和轨迹研究

## 🏗️ 模型架构

CARE v1.0是一个语料库，非模型架构。数据来自612名个体的短时视频访谈，每个视频提供多模态描述符（如声学特征、面部动作单元、身体姿态）和结构化元数据（疾病类型、用药、情绪等）。总时长约144小时，涵盖12种医学条件（如帕金森、抑郁症、COVID-19等）和健康对照组。

## 📚 数据集

- CARE v1.0（训练/评估，144小时，612人，12种疾病+对照）

## 📊 实验结果

摘要未提供具体实验结果，仅描述了语料库的规模和内容。该语料库可用于多种下游任务，但本文未报告基线模型性能。

## 🎯 结论与影响

CARE v1.0是一个大规模、多疾病、多模态语料库，填补了现有数据集在规模和元数据丰富性上的空白。它将促进疾病检测、症状建模和语音行为分析的研究，并为临床决策支持系统提供数据基础。

## ⚠️ 局限与未解决问题

语料库仅包含英语访谈，可能限制跨语言泛化；未提供标注者间一致性指标；元数据完整性依赖于自我报告，可能存在偏差；未公开基线模型结果，难以直接评估数据效用。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-30/">← 返回 2026-07-30 速递</a></div>
