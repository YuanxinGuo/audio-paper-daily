---
title: "Local Chord Corruption Is Not Recognizer Replay: Chord-Condition Propagation in MIDI-SAG"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "本文比较局部和弦损坏与完整自动和弦识别回放在MIDI-SAG生成器中的条件传播差异，发现局部损坏测试机制而完整回放评估部署传播。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.2</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#MIDI-SAG</span> <span class="tag-pill tag-pill-soft">#和弦条件传播</span> <span class="tag-pill tag-pill-soft">#自动和弦识别</span> <span class="tag-pill tag-pill-soft">#歌唱伴奏生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.03584</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.03584" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.03584" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文比较局部和弦损坏与完整自动和弦识别回放在MIDI-SAG生成器中的条件传播差异，发现局部损坏测试机制而完整回放评估部署传播。
</div>

## 👥 作者与机构

**Weiwen Huang** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究歌唱伴奏生成或和弦条件控制的研究者。可重点阅读实验设计与结果分析部分，了解不同条件注入方式的影响。建议先看摘要与结论，再深入方法细节。

## 🌍 研究背景

歌唱伴奏生成（SAG）依赖和弦条件，但条件传递方式对生成质量影响未知。已有研究使用合成和弦损坏或自动和弦识别（ACR）回放来测试系统，但两者差异未明。本文旨在通过固定生成器，对比局部损坏与完整ACR回放对生成输出的影响，以理解条件传播机制。

## 💡 核心创新

1. 对比局部和弦损坏与ACR回放的条件传播差异
2. 引入匹配回放支持与关系组合减少失配
3. 发现相对根音替换比同根音质量翻转影响更大
4. 提出联合匹配降低回放距离
5. 区分机制测试与部署评估的条件注入方式

## 🏗️ 模型架构

使用固定的MIDI-SAG生成器，输入为MIDI序列与和弦条件。条件通过两种方式注入：局部损坏（中央四秒三全音）或ACR回放（CNN-CRF或DeepChroma+CRF预测）。生成器输出音频，通过STFT、CQT、CENS特征比较输出差异。未提及具体网络结构。

## 📊 实验结果

摘要未提供具体数值表格，但提及在30对音轨和三个种子上，中央四秒三全音在STFT、CQT、CENS上产生比CNN-CRF回放更大的目标变化和内部效应；CENS目标差距在29/30音轨为正（平均0.462）。匹配回放支持与关系组合减少失配，联合匹配给出最低回放距离。相对根音替换产生2.88倍更大的CENS全窗口输出变化。

## 🎯 结论与影响

本文表明局部和弦损坏测试生成器机制，而完整ACR回放评估部署条件下的和弦传播。这提示在SAG系统评估中，应根据目的选择条件注入方式。对后续研究，需区分测试与部署场景，并考虑条件表示的影响。工业上，部署时需关注ACR误差传播。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能缺乏对生成音频的主观评估，且仅使用单一生成器，泛化性未知。未报告计算开销或实时性。对比条件有限，未包含其他ACR模型。

---

<div class="paper-footer"><span>评分：6.2</span><span>原始：6.2</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
