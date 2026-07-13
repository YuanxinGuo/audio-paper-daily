---
title: "Event-Based Token Sequences for Audio-Conditioned Music-Game Level Modeling"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐游戏关卡生成"]
summary: "提出基于事件令牌的序列建模方法，将音乐游戏关卡生成转化为多模态序列到序列问题，优于帧级基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐游戏关卡生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#事件序列建模</span> <span class="tag-pill tag-pill-soft">#序列到序列</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#程序化生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.09095</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.09095" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.09095" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于事件令牌的序列建模方法，将音乐游戏关卡生成转化为多模态序列到序列问题，优于帧级基线。
</div>

## 👥 作者与机构

**Ke Zhang** ¹ · Chu-Hsuan Hsueh · Kokolo Ikeda

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合游戏AI、程序化内容生成及音乐信息检索研究者。可重点阅读第3节方法（令牌序列公式化）和第4节实验（事件级评估）。建议对比其与帧级基线的具体差异。

## 🌍 研究背景

音乐游戏关卡需将音乐结构转化为交互式事件序列，现有方法多采用帧级表示，将音频均匀分帧并预测每帧事件，导致事件时序关系隐式且难以建模长程结构。本文受事件级符号音乐建模启发，提出令牌级序列公式，将关卡生成视为多模态序列到序列问题，旨在显式建模动作及其相对节拍时序。

## 💡 核心创新

1. 提出事件令牌与节拍偏移令牌交替的序列公式
2. 将关卡生成建模为多模态序列到序列问题
3. 显式建模动作在节拍空间中的相对时序
4. 基于Transformer实现端到端生成

## 🏗️ 模型架构

输入为音频特征（如梅尔谱）和关卡元数据（如难度、速度），通过编码器提取表示；解码器基于Transformer自回归生成令牌序列，令牌类型包括游戏事件令牌（如音符、滑条）和节拍偏移令牌（表示距上一事件或节拍的相对时间）。输出序列可直接映射为游戏关卡。

## 📚 数据集

- 自建数据集（训练/评估，包含音乐片段与对应人工关卡）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 事件级F1 | 自建测试集 | 帧级基线（未指名具体方法） | **显著优于基线** | 具体数值未给出 |

实验表明，所提令牌级方法在事件级评估指标上优于代表性帧级基线，并能系统分析音频如何辅助节拍对齐的事件预测，超越仅依赖元数据的条件。但摘要未提供具体数值，仅定性描述。

## 🎯 结论与影响

本文提出的令牌级序列公式为音乐游戏关卡生成提供了更自然的表示，显式建模事件时序关系，优于帧级方法。该工作可能推动程序化内容生成中事件级建模的研究，并为音乐与交互序列对齐提供新思路。工业上可用于自动化关卡设计。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理速度等效率指标；仅与帧级基线对比，缺乏与最新序列生成方法（如扩散模型）的比较；数据集未公开，可复现性存疑；未讨论生成关卡的可玩性评估。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
