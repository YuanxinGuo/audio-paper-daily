---
title: "Predicting Turn-Taking Outcomes in Multi-Party Conversation: Interpretable Modelling of Speech and Gaze Dynamics with Interpersonal Closeness"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话分析"]
summary: "本研究利用可解释的语音和凝视特征预测四人自由对话中的话轮转换结果（间隙或重叠），并发现凝视特征在噪声条件下具有鲁棒性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对话分析</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#话轮转换</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#凝视</span> <span class="tag-pill tag-pill-soft">#人际距离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.27988</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.27988" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.27988" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本研究利用可解释的语音和凝视特征预测四人自由对话中的话轮转换结果（间隙或重叠），并发现凝视特征在噪声条件下具有鲁棒性。
</div>

## 👥 作者与机构

**Mark Dourado** ¹ · Karim Haddad · Henrik G. Hassager · Stefania Serafin

**机构**：奥尔堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对话系统、多模态交互和计算社会学研究者阅读。可重点阅读第3节特征工程和第4节实验结果，了解如何从凝视和语音中提取行为学特征。若关注话轮转换预测，可通读全文；若仅关注方法，可先看摘要和结论。

## 🌍 研究背景

流畅的话轮转换是有效对话的基础，依赖于参与者准确预测何时进入对话。在嘈杂、自然的多方对话中，这一过程更为复杂。以往研究多关注语音特征，较少结合凝视和人际距离等非语言线索。本文利用GaMMA语料库，通过可解释的逻辑回归模型，研究凝视、语音和人际亲密感如何共同预示话轮转换结果，旨在提高预测准确性并理解其机制。

## 💡 核心创新

1. 结合凝视转移模式、熵、注视对象身份和相互凝视等特征
2. 引入人际亲密感（IOS）作为预测变量
3. 使用可解释的逻辑回归模型，而非黑盒模型
4. 验证凝视特征在噪声条件下的鲁棒性
5. 特征基于行为学动机，具有可解释性

## 🏗️ 模型架构

输入特征包括凝视特征（转移模式、行为对比、熵、注视对象身份、相互凝视）和语音特征（说话者响度），以及人际亲密感（IOS）。使用逻辑回归模型进行分类，输出为话轮转换结果（间隙或重叠）。模型简单可解释，参数量小。

## 📚 数据集

- GaMMA语料库（训练和评估，四人自由对话）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ROC AUC | GaMMA语料库 | 仅语音特征（未给出具体值） | **0.76 ± 0.04** | 结合凝视和语音特征后提升 |

实验表明，结合凝视和响度特征可达到ROC AUC 0.76，优于仅使用单一模态。响度反映说话者控制力，而凝视分散和注视对象索引了听者准备度和竞争性进入。性能在噪声条件下保持稳定，表明凝视是噪声鲁棒的线索。

## 🎯 结论与影响

本研究证实凝视和语音特征结合能有效预测话轮转换结果，且凝视在噪声下具有鲁棒性。这为构建更自然的人机对话系统提供了依据，并强调了非语言线索在交互建模中的重要性。未来可扩展到更多参与者或真实场景。

## ⚠️ 局限与未解决问题

样本量可能有限（单一语料库），未报告不同噪声水平的详细分析，逻辑回归模型可能无法捕捉复杂非线性关系，且未与其他先进模型（如深度学习）对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
