---
title: "Genre Bias or Aesthetic Perception? Identifying and Mitigating Shortcut Learning in Music Evaluation"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐评估"]
summary: "发现音乐评估模型存在基于体裁的捷径学习，提出联合重加权与正则化训练目标以缓解偏差，提升与人类偏好的一致性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐美学评分</span> <span class="tag-pill tag-pill-soft">#捷径学习</span> <span class="tag-pill tag-pill-soft">#去偏方法</span> <span class="tag-pill tag-pill-soft">#音乐生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.13903</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.13903" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.13903" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发现音乐评估模型存在基于体裁的捷径学习，提出联合重加权与正则化训练目标以缓解偏差，提升与人类偏好的一致性。
</div>

## 👥 作者与机构

**Yizhou Zhang** ¹ · Wangjin Zhou · Yi Zhao · Wei Tan · Keisuke Imoto · Zhi Gong

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、生成模型评估方向的研究者。建议重点阅读第3节（偏差分析）和第4节（方法）。可先看表1和表2了解效果。

## 🌍 研究背景

音乐美学评分在数据集筛选、生成模型评估和奖励建模中至关重要。现有方法使用深度神经网络学习人类标注评分，但可能利用虚假相关而非感知上有意义的特征。本文识别出一种此前未被充分探索的失败模式：体裁诱导的捷径学习。通过系统分析SongEval，发现训练数据偏差导致体裁相关特征与预测分数强相关，模型将其作为美学代理，导致对流行音乐高估、对其他体裁优质样本低估，预测与人类偏好不一致。

## 💡 核心创新

1. 识别音乐评估中体裁捷径学习问题
2. 提出联合重加权与组级正则化训练目标
3. 实现体裁不变的音乐性表征学习
4. 在跨体裁和体裁内偏好对齐上取得提升

## 🏗️ 模型架构

基于SongEval模型（具体架构未详述，推测为深度神经网络），输入音乐特征，主干网络提取表征，输出美学评分。改进方法在训练时引入联合损失：重加权难样本（hard sample reweighting）和组级正则化（group-level regularization），鼓励模型学习体裁不变表征。

## 📚 数据集

- SongEval（训练与评估，含多体裁音乐及人类评分）

## 📊 实验结果

摘要未提供具体数值结果，但声称方法减少了体裁相关偏差，并在跨体裁和体裁内偏好对齐上取得提升。建议读者查阅论文全文获取详细实验数据。

## 🎯 结论与影响

本文揭示了音乐评估模型中体裁捷径学习问题，并提出有效的去偏训练方法。该工作对音乐生成模型的奖励建模和数据集筛选具有指导意义，有助于构建更公平、与人类偏好更一致的评估系统。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：仅基于SongEval数据集，泛化性待验证；未与其他去偏方法对比；未分析模型复杂度或推理效率；未讨论体裁定义的主观性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-16/">← 返回 2026-07-16 速递</a></div>
