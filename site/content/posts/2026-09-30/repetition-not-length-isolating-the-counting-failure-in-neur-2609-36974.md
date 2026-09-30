---
title: "Repetition, Not Length: Isolating the Counting Failure in Neural Text-to-Speech"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "通过配对控制实验证明：TTS 在重复文本上的计数失败源于重复性本身而非文本长度，六模型在 k≥6 时准确率从 94.3% 跌至 18.2%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#鲁棒性评估</span> <span class="tag-pill tag-pill-soft">#重复文本</span> <span class="tag-pill tag-pill-soft">#自回归解码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.36974</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.36974" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.36974" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过配对控制实验证明：TTS 在重复文本上的计数失败源于重复性本身而非文本长度，六模型在 k≥6 时准确率从 94.3% 跌至 18.2%。
</div>

## 👥 作者与机构

**Kirill Borodin** ¹ · Vasilii Kudryavtsev · Maxim Maslov · Grach Mkrtchian

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TTS 鲁棒性、长文本合成与解码策略的研究者阅读。建议通读，重点看 §3 的配对控制设计与 §4 的 420 组分析规格稳健性检验，以及非自回归基线的对比小节；若只关心结论，看表 1 与周期性扫描图即可。

## 🌍 研究背景

当前 TTS 系统（自回归与非自回归）在长文本上常出现循环、截断与计数错误，此前多归因于序列长度带来的误差累积，SOTA 方案多靠长度外推或分段合成缓解。但长度与重复性在自然文本中高度耦合，尚无工作将二者解耦。本文要回答：究竟是长度还是重复本身导致失败，并量化失败随周期性的变化规律。

## 💡 核心创新

1. 配对控制设计：重复句与等句数等词数但不含相邻重复的对照句严格配对
2. 证明失败由重复性而非长度驱动，k≥6 时 94.3% vs 18.2%
3. 420 组分析规格 + 四种 ASR + 贪心解码与重复惩罚扫描均不反转结论
4. 周期性扫描显示失败随周期平滑增长，非相邻重复仍保留一半失败

## 🏗️ 模型架构

本文为诊断性研究而非新模型。实验覆盖三种架构共六个 TTS 模型，另加一个留出的第四种架构与两个非自回归基线。输入为构造的重复文本与配对控制文本，输出为合成语音，再由四个独立 ASR 系统转写并统计精确计数正确率。评估维度包括贪心解码、重复惩罚系数扫描、周期性变化以及 420 组分析规格的稳健性检验，未报告参数量。

## 📚 数据集

- 自建重复/控制配对测试集（评估，含不同重复次数 k 与周期）
- 留出第四架构的预测验证集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 精确计数正确率 | 自建重复文本测试集（k≥6） | 配对控制文本 94.3% | **重复文本 18.2%** | -76.1% |

摘要给出核心数字：k≥6 时控制文本 94.3% 精确正确，重复文本仅 18.2%。该差距在贪心解码、重复惩罚扫描、四种 ASR 与 420 组分析规格下均未反转；留出的第四架构落在预测差距一个百分点内，两个非自回归基线中有一个复现同样失败。周期性扫描显示失败随周期平滑增长，即使无相邻重复词仍保留约一半失败。

## 🎯 结论与影响

最强结论是 TTS 的计数失败由文本重复性本身触发，而非长度。这提示后续 TTS 研究需在解码与位置编码层面显式建模重复结构，而非仅做长度外推。工业上，长文朗读、字幕与有声书场景应加入重复文本的专项回归测试。

## ⚠️ 局限与未解决问题

仅评估计数正确率，未报告 MOS、韵律或自然度等感知指标；未给出推理延迟与显存开销；非自回归基线仅两个且只有一个复现失败，覆盖面有限；未提出缓解方法，诊断到干预之间仍有距离。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
