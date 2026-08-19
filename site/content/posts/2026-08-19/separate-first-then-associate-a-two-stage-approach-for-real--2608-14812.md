---
title: "Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出分离-关联两阶段方法，先用音频-only模型分离多说话人混合，再用音频-视觉CLIP匹配目标人脸视频，提升真实场景AVSE性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-视觉语音增强</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#跨模态匹配</span> <span class="tag-pill tag-pill-soft">#真实场景</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.14812</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.14812" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.14812" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出分离-关联两阶段方法，先用音频-only模型分离多说话人混合，再用音频-视觉CLIP匹配目标人脸视频，提升真实场景AVSE性能。
</div>

## 👥 作者与机构

**Tongtao Ling** ¹ · Zhong-Qiu Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、多模态学习的研究者。建议重点阅读方法部分（两阶段框架）和实验部分（挑战赛结果）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

音频-视觉语音增强（AVSE）利用视觉线索从多说话人混合中提取目标语音。现有方法在模拟数据集上表现良好，但在真实场景中性能下降，因为真实环境存在说话人重叠、声学干扰、混响和视觉退化。ISCSLP 2026真实世界AVSE挑战赛旨在推动实用解决方案。本文提出解耦的分离-关联方法，以应对真实条件。

## 💡 核心创新

1. 两阶段解耦：分离与关联分离，降低联合优化难度
2. 利用音频-only分离模型，不依赖视觉线索，增强泛化性
3. 使用音频-视觉CLIP进行跨模态相似度匹配，关联目标说话人
4. 针对真实场景设计，处理重叠、混响和视觉退化

## 🏗️ 模型架构

输入多说话人混合音频和多个说话人的面部视频。第一阶段：使用预训练的音频-only分离模型（如SepFormer或Conv-TasNet）将混合音频分离为多个单说话人信号。第二阶段：使用音频-视觉CLIP模型，将每个分离信号与目标说话人的面部视频进行跨模态相似度匹配，选择相似度最高的信号作为增强结果。

## 📚 数据集

- 挑战赛数据集（评估）

## 📊 实验结果

摘要未提供具体数值，但提到在挑战赛数据集上评估，证明了方法的有效性。具体指标（如PESQ、SI-SDR）未给出。

## 🎯 结论与影响

本文提出的分离-关联两阶段方法在真实世界AVSE挑战赛中有效，通过解耦分离和关联，利用音频-only模型和跨模态匹配，提升了真实场景下的增强性能。该方法为AVSE提供了新思路，可能推动实际应用，如助听器和远程通信。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：两阶段方法误差累积，分离阶段错误影响关联；依赖预训练模型，可能不适用于未见过的说话人；未提供与其他方法的详细对比或消融实验。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-19/">← 返回 2026-08-19 速递</a></div>
