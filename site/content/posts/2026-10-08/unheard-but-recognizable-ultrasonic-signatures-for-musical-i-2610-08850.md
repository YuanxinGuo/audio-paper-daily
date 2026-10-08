---
title: "Unheard but Recognizable: Ultrasonic Signatures for Musical Instrument Recognition"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "利用96kSPS录音中的超声频段成分，验证其对单音与复音乐器识别的增益。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器识别</span> <span class="tag-pill tag-pill-soft">#超声频段</span> <span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#多音混合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.08850</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.08850" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.08850" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用96kSPS录音中的超声频段成分，验证其对单音与复音乐器识别的增益。
</div>

## 👥 作者与机构

Izhak Kapash (Tel Aviv University) · Uri Rom (Tel Aviv University) · Ram Zamir (Tel Aviv University)

**机构**：特拉维夫大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做MIR、乐器识别与高采样率音频表征的研究者阅读。建议重点看数据集构建与全频/低通/超声三组对照实验设计，以及复音混合下的分类结果表。若只关心语音增强或分离，可略读。

## 🌍 研究背景

乐器识别是MIR的基础任务，支撑转录、源分离与音频理解。现有方法多在44.1/48kSPS下工作，受Nyquist限制无法表征20kHz以上成分，对音色相近乐器及复音混合场景识别仍有提升空间。本文提出利用96kSPS录音中的超声频段与宽带瞬态信息，检验其是否携带乐器特异性线索，并系统比较全频、低通与仅超声输入下的识别性能。

## 💡 核心创新

1. 首次系统评估超声频段对乐器识别的贡献
2. 构建96kSPS多轨15类乐器语料库
3. 对比全频/低通/仅超声三种输入设置
4. 覆盖单音与复音混合两种识别场景

## 🏗️ 模型架构

输入为96kSPS高采样率音频，分别构造全频带、低通（0-20kHz）与仅超声（>20kHz）三种特征表示。采用经典机器学习分类器与深度学习分类器两套基线进行对比，输出15类乐器的类别预测。摘要未给出具体网络名、参数量或特征提取细节，仅说明通过多类分类器比较不同频带输入的识别准确率。

## 📚 数据集

- 96kSPS多轨乐器语料库（训练与评估，15类，覆盖演奏者/乐器/录音室/场次）

## 📊 实验结果

摘要未给出具体数值指标，仅定性说明：源相关的超声扩展与宽带瞬态包含乐器特异性信息，可显著提升单音与复音识别性能。未报告准确率、F1或与具体基线的数值对比，也未提供消融或效率数据。

## 🎯 结论与影响

超声频段与宽带瞬态确实携带乐器识别所需的判别信息，支持在MIR任务中使用更宽带宽录音。该结论可能推动后续研究重新审视采样率与频带选择对识别、分离等任务的影响，并对高保真音乐采集与处理管线设计有参考意义。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果与统计显著性检验，缺少与主流乐器识别SOTA的数值对比；仅15类、单一语料库，泛化性存疑；未报告推理开销与超声成分在真实压缩/传输场景下的鲁棒性。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-08/">← 返回 2026-10-08 速递</a></div>
