---
title: "Constructing Dynamic Conversations with Neural Back-channel Generation and Voice-line Scheduling"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "用神经调度器把两条独立录制的对白音轨拼接成带副声道与话轮交叠的动态对话。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对话语音合成</span> <span class="tag-pill tag-pill-soft">#副声道生成</span> <span class="tag-pill tag-pill-soft">#语音编辑</span> <span class="tag-pill tag-pill-soft">#回合转换</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.24086</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.24086" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.24086" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用神经调度器把两条独立录制的对白音轨拼接成带副声道与话轮交叠的动态对话。
</div>

## 👥 作者与机构

**Yifang Pan** ¹ · Chris Landreth · Karan Singh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做游戏语音、对话式 TTS、语音编辑的研究者与音频工程师阅读。建议通读，重点看 §3 调度器与副声道预测器的接口设计，以及感知实验部分；若只关心副声道建模，可先看副声道预测器一节与主观评测表。

## 🌍 研究背景

游戏与动画配音中，双人对白通常分轨独立录制或合成，缺少真实对话中的停顿调整、话轮交叠与副声道（back-channel）。传统做法靠人工剪辑或简单拼接，难以规模化且缺乏可控性；已有对话语音生成工作多聚焦单轨 TTS 或端到端对话合成，对已有双轨素材的后期重组关注不足。本文要解决的是：给定两条不同步的对白音轨，自动生成具有可控副声道与话轮动态的统一对话。

## 💡 核心创新

1. 神经调度器对双轨插入/删除停顿并引入交叠
2. 基于音频与文本内容的副声道机会预测器
3. 调度器与预测器联合生成动态对话
4. 支持动画师对副声道多样性/程度/性质的控制

## 🏗️ 模型架构

输入为两条独立对白音轨（及其文本内容），先由副声道预测器判断给定话轮音频与内容中可插入副声道的机会点；随后神经调度器在时间轴上对两轨进行排序，通过插入或删除静音段、引入语音交叠来生成统一对话流，输出为单条混合对话音频及对应时间对齐。摘要未给出具体主干网络名与参数量。

## 📚 数据集

- 自建双人对白语音数据集（训练/评估，规模未披露）

## 📊 实验结果

摘要仅说明进行了多项定量比较、与先前工作及朴素基线的定性/感知对比，并展示了动画师对副声道多样性、程度与性质的可控性，但未给出 SI-SDR、PESQ、MOS 等具体数值，无法列表比较。

## 🎯 结论与影响

最强结论是：对已有双轨对白做神经调度即可生成带可控副声道与话轮动态的自然对话，无需重新录制。这为游戏/动画配音后期提供了可规模化、可交互控制的工具链，也可能影响对话式语音合成与语音编辑的研究路线。

## ⚠️ 局限与未解决问题

摘要未披露数据集规模、客观指标与推理延迟，感知实验细节不足；副声道预测器依赖内容与音频特征，跨语言/跨风格泛化未知；与端到端对话生成方法的对比缺失，可控性评估偏主观。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-19/">← 返回 2026-11-19 速递</a></div>
