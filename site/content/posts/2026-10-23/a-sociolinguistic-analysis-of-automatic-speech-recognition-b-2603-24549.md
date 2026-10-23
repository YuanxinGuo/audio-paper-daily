---
title: "A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "用社会语言学方法分析商用ASR在纽卡斯尔英语上的3000余条转写错误，发现错误按社会群体呈系统性分布。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#ASR公平性</span> <span class="tag-pill tag-pill-soft">#方言语音</span> <span class="tag-pill tag-pill-soft">#社会语言学</span> <span class="tag-pill tag-pill-soft">#错误分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.24549</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.24549" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.24549" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用社会语言学方法分析商用ASR在纽卡斯尔英语上的3000余条转写错误，发现错误按社会群体呈系统性分布。
</div>

## 👥 作者与机构

**Dana Serditova** ¹ · Kevin Tang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做ASR鲁棒性、方言/口音公平性、语料构建的研究者与产品评测人员阅读。本文是分析型工作而非建模工作，无需通读方法细节；建议重点看错误分类体系（按语言域）与按性别/年龄/社会经济地位的分层统计表，以及元音声学个案分析一节，可作为构建方言测试集与公平性评测协议的参考。

## 💡 核心创新

1. 以社会语言学框架系统归类ASR转写错误
2. 将错误率与性别/年龄/社会经济地位交叉分析
3. 对元音音质与喉塞化等方言特征做声学个案归因
4. 指出错误呈社会性模式而非随机分布

## 🏗️ 模型架构

本文不提出新模型。流程为：以 DECTE 中 Tyneside 英语自发语音为输入，调用一套最先进商用 ASR 系统（摘要未指明具体系统）获得转写输出，与人工转写对齐后抽取 3000 余条错误；随后按语言域（音系、词汇、语法等）分类，并与性别、年龄、社会经济地位等社会变量交叉统计；最后对若干元音特征做声学个案分析，考察渐变语音变异与误识别的对应关系。

## 📚 数据集

- DECTE（Diachronic Electronic Corpus of Tyneside English，评估用，自发语音）

## 📊 实验结果

摘要仅给出定性结论：音系变异占错误多数，反复出现的失败集中在元音音质、喉塞化、本地词汇与非标准语法形式；男性及年龄谱两端的说话人错误率更高。摘要未报告 WER 具体数值、基线系统名称或统计显著性检验结果，故无法列表量化对比。

## 🎯 结论与影响

最强结论是ASR错误在社会语言学意义上是可解释、可预测的，而非随机噪声。这为方言公平性评测提供了分析范式，提示后续工作应把社会变量纳入评测协议；对工业落地而言，意味着单一主流口音训练的系统在区域变体上存在系统性服务不均。

## ⚠️ 局限与未解决问题

仅评测一套商用系统，缺少多系统横向对比；未报告整体 WER 与置信区间，社会群体差异的统计显著性不明；错误归因依赖人工标注，标注者一致性未说明；未提出缓解方法或再训练实验，结论的因果强度有限。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
