---
title: "Do Text-to-Music Models Really Follow Instructions? A Counterfactual Evaluation of Key and Beat Grouping"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出匹配反事实评估框架，分离文本到音乐模型中指令控制与输出先验，发现现有模型在节拍分组上的控制力被高估。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音乐</span> <span class="tag-pill tag-pill-soft">#可控性评估</span> <span class="tag-pill tag-pill-soft">#反事实评估</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11899</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11899" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11899" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出匹配反事实评估框架，分离文本到音乐模型中指令控制与输出先验，发现现有模型在节拍分组上的控制力被高估。
</div>

## 👥 作者与机构

**Yining Wang** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究文本到音乐生成、可控生成评估的研究者。建议重点阅读第3节方法部分和第4节实验结果，特别是表2和表3。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

文本到音乐模型的可控性通常通过提示属性一致性来评估，但属性出现可能源于模型输出分布中的先验，而非指令控制。现有评估方法未区分这两者，导致对模型控制力的高估。本文旨在通过匹配反事实设计，分离目标出现与指令归因的控制，提供更可靠的评估方法。

## 💡 核心创新

1. 提出匹配反事实评估框架，包含中性输入和目标交换输入
2. 使用冻结原生接口适配器和共享种子确保公平比较
3. 引入安慰剂、外部识别器验证和盲审专家标注增强归因
4. 揭示节拍分组中四拍一致性主要继承自中性输出
5. 提供多种子哨兵测试增强统计可靠性

## 🏗️ 模型架构

评估框架：每个家族包含中性输入（省略评分属性）和两个匹配输入（交换目标属性），通过冻结的原生接口适配器渲染，使用共享种子。应用于三个开源系统：ACE-Step 1.5、Stable Audio 3 Medium和LeVo2。评估全局调性和节拍分组，使用外部识别器验证和盲审专家标注。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 四拍分组一致性 | 中性输入 | Stable Audio 3 0.97 | **Stable Audio 3 0.56** | -0.41 |

实验表明，ACE-Step 1.5和Stable Audio 3 Medium在调性控制上表现显著，而LeVo2无显著控制。对于节拍分组，模型能转向罕见的三拍目标，但四拍一致性主要继承自中性输出：Stable Audio 3在中性输入下四拍分组一致性为0.97，但在明确四拍处理下仅为0.56。外部识别器验证和盲审专家标注支持归因。

## 🎯 结论与影响

本文提出的匹配反事实评估框架能有效区分指令控制与输出先验，揭示了现有模型在节拍分组控制上的局限性。该评估方法可推广至其他可控生成任务，为更严谨的可控性评估提供范式。对工业界而言，有助于开发者准确了解模型能力，避免过度宣传。

## ⚠️ 局限与未解决问题

评估仅针对三个开源系统，可能不具广泛代表性。未涉及其他属性（如乐器、风格）和更复杂的音乐结构。未报告计算开销和推理延迟。未提供代码或数据，可复现性存疑。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
