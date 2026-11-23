---
title: "Windchime: an Audiovisual Installation with Audio-Language Model implementations"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "一个语音驱动的视听装置，用本地ASR与音频语言模型对406个音频stem做检索，生成声景与交互动画。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">3.0</div>
<div class="score-stars">★★☆☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态检索</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#艺术装置</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.26759</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.26759" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.26759" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>一个语音驱动的视听装置，用本地ASR与音频语言模型对406个音频stem做检索，生成声景与交互动画。
</div>

## 👥 作者与机构

**Trent Eriksen** ¹ · Celeste Betancur Gutierrez

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合数字艺术、HCI与多模态检索交叉方向的研究者或策展人浏览。本文属艺术装置描述，非方法论文，无需通读；若关注ALM用于检索的工程细节，可看系统流程与语料构建部分，但不要期待定量评测。

## 🌍 研究背景

音频-语言模型（ALM）如CLAP已能实现文本到音频的跨模态检索，语音识别也趋于本地化部署。但现有工作多聚焦基准指标，较少探讨这些模型在公共艺术与具身交互中的角色。本文要解决的问题是：如何把语音输入、ALM检索与视听输出组合成一个可交互装置，并讨论作者、模型与观众之间的能动性分配。

## 💡 核心创新

1. 本地ASR+ALM串联的语音检索管线
2. 406个音频stem的艺术家自建语料检索
3. Strudel实时编码片段分层合成声景
4. Three.js动画与monome grid/arc触觉控制联动

## 🏗️ 模型架构

系统输入为观众语音提示，先由本地ASR模型转写为文本，再送入音频-语言模型（ALM）得到嵌入向量，在艺术家自建的406个音频stem语料上做检索，返回匹配音频并叠加实时编码的Strudel片段形成声景输出；同时同一语音输入触发Three.js交互动画场景检索，场景通过monome grid与arc硬件提供触觉控制。摘要未给出网络结构细节与参数量。

## 📚 数据集

- 艺术家自建音频语料（406个音频stem，检索库）

## 📊 实验结果

摘要未报告任何定量实验结果，无SI-SDR、PESQ、WER或检索指标，也未与基线系统对比。本文为装置描述型论文，评价以艺术体验与交互设计为主。

## 🎯 结论与影响

最强结论是语音+ALM检索可支撑一个多模态具身艺术装置，并把能动性分配给作者、模型与观众三方。对后续研究的潜在影响主要在ALM的交互式应用与艺术实践，而非语音信号处理算法本身；工业落地含义有限。

## ⚠️ 局限与未解决问题

缺少任何定量评测与消融，未报告ASR的WER、检索准确率或延迟；语料仅406个stem且为艺术家自建，存在明显偏置；未与现有文本-音频检索方法对比，可复现性信息不足。

---

<div class="paper-footer"><span>评分：3.0</span><span>原始：3.0</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
