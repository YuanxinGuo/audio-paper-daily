---
title: "A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出两种双耳线索保持损失，直接惩罚掩蔽引起的左右频谱关系失真，联合建模ILD和IPD，在保持降噪性能的同时减少失真并改善ILD保持。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#损失函数</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.16299</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.16299" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.16299" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两种双耳线索保持损失，直接惩罚掩蔽引起的左右频谱关系失真，联合建模ILD和IPD，在保持降噪性能的同时减少失真并改善ILD保持。
</div>

## 👥 作者与机构

**Jayteerth Amble** ¹ · Thomas Haubner · Hendrik Schr\"oter · Christoph Hoog Antink · Henning Puder

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳语音增强或助听器算法研究的读者。建议重点阅读第3节损失函数设计和第4节实验对比，尤其是表2和表3。可先看摘要和结论，再深入方法部分。

## 🌍 研究背景

双耳语音增强旨在降噪的同时保持空间定位所需的耳间线索。现有DNN方法虽降噪强，但常扭曲左右信号关系。先前工作分别优化ILD和IPD误差，但未直接建模双耳一致性。本文提出直接惩罚掩蔽引起的左右频谱关系失真的损失，并联合建模ILD和IPD，以更好保持双耳结构。

## 💡 核心创新

1. 提出双耳重建误差损失，直接惩罚左右频谱关系失真
2. 提出联合双耳线索损失，同时建模ILD和IPD
3. 在保持降噪性能的同时减少掩蔽引起的失真
4. 联合损失在ILD保持上优于基线
5. 实验验证了两种损失的有效性

## 🏗️ 模型架构

输入为左右耳含噪语音的短时傅里叶变换（STFT）幅度谱，通过DNN（如U-Net或Conformer）估计左右耳各自的掩蔽，应用于含噪谱得到增强谱。训练时，在传统损失基础上加入提出的双耳重建误差损失或联合双耳线索损失。输出为增强后的左右耳时域信号。

## 📊 实验结果

摘要未提供具体数值，但实验表明两种损失均保持强降噪性能，并减少掩蔽引起的失真，联合损失在ILD保持上优于基线。具体指标和数据集未提及。

## 🎯 结论与影响

本文提出的双耳线索保持损失能有效减少掩蔽引起的双耳失真，同时保持降噪性能，联合建模ILD和IPD进一步改善ILD保持。对助听器双耳增强算法有实际意义，为后续研究提供了新的损失设计思路。

## ⚠️ 局限与未解决问题

摘要未提供具体实验细节，如数据集、基线、指标数值，缺乏可复现性。未讨论计算开销或实时性。未提及对IPD保持的详细结果，可能联合损失在IPD上无显著优势。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
