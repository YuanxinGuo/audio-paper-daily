---
title: "Cross-modal characterization of infant cry: validation of a chest-surface accelerometer in extracting acoustic vocal function measures"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "验证胸戴加速计在婴儿哭声分析中提取声学特征的有效性，与麦克风对比显示基频和抖动指标一致性高。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#婴儿哭声分析</span> <span class="tag-pill tag-pill-soft">#加速计</span> <span class="tag-pill tag-pill-soft">#声学特征提取</span> <span class="tag-pill tag-pill-soft">#交叉模态验证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28687</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28687" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28687" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>验证胸戴加速计在婴儿哭声分析中提取声学特征的有效性，与麦克风对比显示基频和抖动指标一致性高。
</div>

## 👥 作者与机构

**Winko W. An** ¹ · Saketh Sundar · Lisa Yankowitz · Daryush D. Mehta · Carol L. Wilkinson

**机构**：麻省理工 · 哈佛大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生物声学、临床语音分析研究者阅读。重点看方法部分（特征提取与ICC分析）和结果表。若关注噪声鲁棒性，可通读全文。

## 🌍 研究背景

婴儿哭声声学特征可作为神经发育障碍的生物标志物，但传统麦克风录音易受环境噪声干扰且存在隐私问题。胸戴加速计通过直接采集喉部振动提供替代方案，但其在婴儿哭声分析中的有效性尚未系统验证。本文旨在评估加速计与麦克风在提取七种声学特征上的一致性。

## 💡 核心创新

1. 首次系统验证加速计在婴儿哭声分析中的有效性
2. 采用ICC评估跨模态声学特征一致性
3. 涵盖4个月和12个月婴儿的多样化样本
4. 提出噪声鲁棒且隐私保护的哭声采集方案

## 🏗️ 模型架构

使用胸戴加速计（ACC）和麦克风（MIC）同时采集婴儿哭声信号。从两种模态中提取七种声学特征：基频（F0）、抖动、闪烁、倒谱峰值突出度（CPP）、谐波噪声比（HNR）等。通过组内相关系数（ICC）评估ACC与MIC之间特征的一致性和绝对一致性。

## 📚 数据集

- 85名婴儿（41名4个月，44名12个月）的哭声录音（训练/评估，来自常规疫苗接种访问）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ICC（F0） | 婴儿哭声数据集 | N/A | **>0.94** | N/A |
| ICC（抖动） | 婴儿哭声数据集 | N/A | **良好至优秀** | N/A |
| ICC（CPP） | 婴儿哭声数据集 | N/A | **中等** | N/A |

F0在ACC和MIC之间表现出极好的一致性（ICC>0.94），抖动指标也显示良好至优秀的一致性，而CPP一致性中等。闪烁和HNR的绝对一致性较低，存在系统偏差，可能源于信号传输和噪声敏感性的差异。

## 🎯 结论与影响

胸戴加速计能可靠捕获婴儿哭声的基频和抖动等时间声学特征，为麦克风录音提供了噪声鲁棒且保护隐私的替代方案，有望用于可扩展的临床和发展研究。

## ⚠️ 局限与未解决问题

样本量有限（85名），未评估加速计在不同噪声环境下的鲁棒性，未报告推理延迟或计算成本，且仅验证了部分声学特征（闪烁和HNR一致性差）。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
