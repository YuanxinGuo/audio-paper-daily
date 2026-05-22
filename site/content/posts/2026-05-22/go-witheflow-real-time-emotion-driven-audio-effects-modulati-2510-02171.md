---
title: "Go witheFlow: Real-time Emotion Driven Audio Effects Modulation"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频效果调制"]
summary: "提出witheFlow系统，利用生物信号和音频特征实时调制音频效果，增强音乐表演的人机协作。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频效果调制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#实时系统</span> <span class="tag-pill tag-pill-soft">#生物信号</span> <span class="tag-pill tag-pill-soft">#音乐表演</span> <span class="tag-pill tag-pill-soft">#开源</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.02171</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.02171" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.02171" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出witheFlow系统，利用生物信号和音频特征实时调制音频效果，增强音乐表演的人机协作。
</div>

## 👥 作者与机构

**Edmund Dervakos** ¹ · Spyridon Kantarelis · Vassilis Lyberatos · Jason Liartis · Giorgos Stamou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对实时音频效果调制和人机交互感兴趣的研究者。可重点阅读系统架构部分，但实验评估不足，建议跳过结果部分。

## 🌍 研究背景

音乐表演是人类特有的情感表达活动，机器缺乏情感体验。现有音频效果调制多依赖手动控制或预设，缺乏对表演者状态的实时响应。本文提出witheFlow系统，通过生物信号和音频特征自动调制效果，探索人机协作。

## 💡 核心创新

1. 融合生物信号与音频特征进行效果调制
2. 轻量级实时系统，可本地运行
3. 开源设计，兼容主流DAW和传感器

## 🏗️ 模型架构

系统输入为生物信号（如心率、皮肤电导）和音频信号，通过特征提取模块获取实时特征，送入轻量级神经网络或规则引擎，输出控制参数调制音频效果（如混响、延迟）。系统基于开源框架，兼容VST插件。

## 📊 实验结果

摘要未提供具体实验结果，仅描述系统为概念验证阶段，未报告客观指标或用户研究。

## 🎯 结论与影响

witheFlow系统展示了利用生物信号实时调制音频效果的可行性，为音乐表演人机协作提供了新思路。但当前仅为概念验证，缺乏定量评估，后续需完善实验验证。

## ⚠️ 局限与未解决问题

系统仅处于概念验证阶段，缺乏客观指标和用户研究；未与基线方法对比；生物信号与情感映射的可靠性存疑；实时性能未量化。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-05-22/">← 返回 2026-05-22 速递</a></div>
