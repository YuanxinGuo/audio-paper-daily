---
title: "A strongly annotated passive acoustic dataset for tropical bird monitoring"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "PteroSet是一个包含15,372个强标注的哥伦比亚热带鸟鸣数据集，提供COCO格式标注和深度学习基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#被动声学监测</span> <span class="tag-pill tag-pill-soft">#鸟鸣检测</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#热带声景</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.20578</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.20578" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.20578" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PteroSet是一个包含15,372个强标注的哥伦比亚热带鸟鸣数据集，提供COCO格式标注和深度学习基线。
</div>

## 👥 作者与机构

**Daniela Ruiz** ¹ · Juan Sebasti\'an Ulloa · Zhongqi Miao · Nicol\'as Betancourt · Maria Paula Toro-G\'omez · Andr\'es Hern\'andez · Bruno Demuro · Eliana Barona-Cort\'es · … 等 6 人

**机构**：微软研究院 · 哥伦比亚大学 · 洛斯安第斯大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事生物声学、被动声学监测和机器学习数据集构建的研究者。建议重点阅读数据集构建部分（§2）和基线实验（§4），了解标注格式和热带声景挑战。

## 🌍 研究背景

被动声学监测（PAM）通过连续录音实现非侵入式生物多样性评估，但监督学习方法依赖时间分辨率高的标注数据集。现有数据集多来自温带地区，热带声景因物种丰富、声音重叠和域偏移而更具挑战。本文旨在填补热带鸟鸣强标注数据的空白，提供PteroSet数据集和基准。

## 💡 核心创新

1. 提供168种热带鸟类的6,702个物种级标注
2. 采用COCO格式统一音频、分类和标签
3. 数据集涵盖两个不同录音地点的域偏移
4. 提供二元鸟检测的深度学习基线
5. 标注包含声学共现信息

## 🏗️ 模型架构

基线模型采用基于预训练音频嵌入（如BirdNET或CNN）的二元分类器，输入为音频片段，输出为鸟存在概率。具体架构未在摘要中详述，但提及使用深度学习模型进行检测。

## 📚 数据集

- PteroSet（训练/评估，563段录音，73.62小时，15,372个标注）
- 录音地点：Puerto Asís (Putumayo) 和 Pivijay (Magdalena), Colombia

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 检测准确率 | PteroSet | 未提供 | **基线结果（具体值未在摘要中给出）** | N/A |

摘要未提供具体数值结果，仅说明基线实验展示了数据集的可用性和挑战，包括声学共现和域偏移的影响。

## 🎯 结论与影响

PteroSet为热带鸟鸣监测提供了首个大规模强标注数据集，填补了数据稀缺的空白。其COCO格式便于机器学习集成，基线实验揭示了热带声景的独特挑战。该数据集有望推动生物声学领域的监督学习研究，并为生态监测应用提供基准。

## ⚠️ 局限与未解决问题

摘要未明确讨论局限，但可推测：数据集仅覆盖哥伦比亚两个地点，物种多样性有限；基线仅针对二元检测，未涉及多物种分类；未提供模型推理效率或泛化到其他热带地区的评估。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
