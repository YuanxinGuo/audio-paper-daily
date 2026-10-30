---
title: "Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis"
date: 2026-10-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用CTC假名识别器对日语金融TTS中多音汉字做读音级校验，替代不可靠的ASR转写门控。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#发音验证</span> <span class="tag-pill tag-pill-soft">#CTC</span> <span class="tag-pill tag-pill-soft">#日语TTS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.39168</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.39168" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.39168" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用CTC假名识别器对日语金融TTS中多音汉字做读音级校验，替代不可靠的ASR转写门控。
</div>

## 👥 作者与机构

**Cheng Zhang** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做日语TTS前端、发音词典与TTS质量门控的工程与研究同学阅读。值得通读，重点看§3的CTC假名打分与混淆读音候选构造，以及表2的检测率/误报率对比；若只关心落地，可先看自然输入下重生成率38.9%→6.1%的实验。

## 🌍 研究背景

少样本语音克隆使批量生成日语金融播报变得廉价，但多音汉字（如「市場」shijo/ichiba、「大勢」taisei/oze）仍常被误读。常见质量门控是ASR转写后与输入转假名比对、不一致则重生成。该门控双向失效：音频误读时ASR语言模型会把期望汉字“写回”掩盖错误；音频正确时普通识别错误又触发无谓重生成。本文要解决的是可靠检测读音错误、同时压低误报。

## 💡 核心创新

1. 用CTC平假名识别器对期望读音与混淆读音分别打分
2. 以“替代读音更能解释音频”作为误读判据，绕开ASR语言模型纠错
3. 针对金融术语构造混淆读音候选集
4. 在受控注入误读条件下系统评估门控双向失效

## 🏗️ 模型架构

输入为合成语音波形，前端提取声学特征后送入CTC平假名识别器（摘要未给出具体主干网络名与参数量）。对每个待检词，将期望读音及其混淆替代读音分别作为CTC目标序列计算得分（如对数后验），比较期望读音与最佳替代读音的得分差，当替代读音解释音频更好时将该词标记为疑似误读并触发重生成。整体是TTS流水线后的读音级校验模块，而非端到端重训TTS。

## 📚 数据集

- 540条合成语音（三个语音克隆生产音色、30个金融术语，评估，误读受控注入）
- 自然汉字输入句子（评估，统计重生成请求比例）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 误读检测率 | 540条受控注入误读语音 | ASR转写门控 78.9% | **91.7%** | +12.8% |
| 误报率 | 540条受控注入误读语音 | ASR转写门控 44.4% | **5.0%** | -39.4% |
| AUC | 540条受控注入误读语音 | 未报告 | **0.990** | — |
| 重生成请求比例 | 自然汉字输入 | ASR转写门控 38.9% | **6.1%** | -32.8% |

在540条受控注入误读语音上，所提读音级校验以91.7%检测率、5.0%误报率显著优于转写门控的78.9%/44.4%，AUC达0.990。自然汉字输入下重生成请求从38.9%降至6.1%，并捕获了转写门控对某一音色漏掉的前端错误。摘要未给出消融、推理延迟与跨领域泛化结果。

## 🎯 结论与影响

最强结论是：直接对读音而非转写做声学打分，可同时大幅提升误读检出并压低误报。这为TTS前端读音校验提供了可复用范式，对批量金融播报等低成本语音克隆生产线的质量门控有直接落地价值。

## ⚠️ 局限与未解决问题

评估仅限三个克隆音色、30个金融术语与540条语音，规模偏小且领域狭窄；混淆读音候选集如何构造、是否覆盖未登录词未说明；未报告CTC识别器推理开销与延迟；缺少与更强发音评估模型（如GOP、强制对齐）的对比与消融。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-30/">← 返回 2026-10-30 速递</a></div>
