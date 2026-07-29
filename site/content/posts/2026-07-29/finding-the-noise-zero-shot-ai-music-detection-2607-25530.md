---
title: "Finding the noise: Zero-shot AI Music Detection"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#AI音乐检测"]
summary: "提出一种零样本AI音乐检测方法，结合伪影提取与非负矩阵分解，在未知生成模型场景下实现高精度检测与聚类。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#AI音乐检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本检测</span> <span class="tag-pill tag-pill-soft">#无监督学习</span> <span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#伪影提取</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25530</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25530" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25530" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种零样本AI音乐检测方法，结合伪影提取与非负矩阵分解，在未知生成模型场景下实现高精度检测与聚类。
</div>

## 👥 作者与机构

**Darius Afchar** ¹ · Romain Hennequin

**机构**：Deezer

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、音乐信息检索领域研究者。重点读§3方法部分和§4实验，尤其是零样本多类识别任务的设计。可先看表1和表2了解性能。

## 🌍 研究背景

自2023年起，Suno、Udio等AI音乐生成服务快速迭代，传统监督检测方法难以适应新模型。现有研究多聚焦语音或通用音频，音乐领域的零样本检测尚属空白。本文旨在解决未知生成模型场景下的AI音乐检测问题，提出无监督方案。

## 💡 核心创新

1. 伪影提取+非负矩阵分解(NMF)的零样本检测框架
2. 首次定义零样本多类识别任务（无监督聚类）
3. 在真实与合成音乐混合数据上实现高纯度聚类

## 🏗️ 模型架构

输入音频经预训练模型提取伪影特征，然后应用非负矩阵分解(NMF)降维，最后使用简单分类器（如SVM）或聚类算法（如K-means）完成检测或聚类。整体流程无需目标生成模型训练数据。

## 📚 数据集

- 内部数据集（包含真实音乐与Suno、Udio等生成音乐，用于训练/评估）

## 📊 实验结果

摘要未提供具体数值，但声称在判别和聚类任务上均取得优异性能。方法可扩展至大规模目录监控。

## 🎯 结论与影响

本文提出的零样本AI音乐检测方法在未知生成模型场景下有效，结合伪影提取与NMF实现高精度。对音乐平台内容审核有直接应用价值，并推动无监督音频伪造检测研究。

## ⚠️ 局限与未解决问题

未报告具体指标和数据集规模，缺乏与监督方法的对比。伪影提取模块依赖预训练模型，泛化性未充分验证。未讨论计算效率。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-29/">← 返回 2026-07-29 速递</a></div>
