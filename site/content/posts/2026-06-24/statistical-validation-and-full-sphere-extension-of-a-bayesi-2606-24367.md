---
title: "Statistical validation and full-sphere extension of a Bayesian model for human static sound localisation"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出贝叶斯声源定位模型的显式似然函数，并通过参数恢复和行为拟合验证其可靠性，同时用于比较HRTF插值方法。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#贝叶斯模型</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#统计验证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24367</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24367" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24367" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出贝叶斯声源定位模型的显式似然函数，并通过参数恢复和行为拟合验证其可靠性，同时用于比较HRTF插值方法。
</div>

## 👥 作者与机构

**Roberto Barumerli** ¹ · Fabian Brinkmann · Emanuele Zanoni · Anton Hoyer · Lorenzo Picinali · Michele Geronazzo

**机构**：帕多瓦大学 · 柏林工业大学 · 伦敦帝国理工学院 · 乌迪内大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合双耳音频、空间听觉和HRTF相关研究者。建议通读，重点看§3参数恢复实验和§4 HRTF插值比较。可先看图2和表1。

## 🌍 研究背景

听觉模型是研究空间听觉的核心工具，但传统验证依赖启发式性能指标，缺乏统计严谨性。现有贝叶斯声源定位模型虽能联合推断声源方向和个体HRTF，但未提供显式似然函数，限制了其统计验证和应用。本文旨在推导显式似然函数，并通过参数恢复和行为拟合验证框架可靠性，进而用于比较HRTF模板插值方法。

## 💡 核心创新

1. 推导贝叶斯声源定位模型的显式似然函数
2. 通过参数恢复实验验证模型可识别性
3. 拟合33名参与者行为数据验证个体参数估计
4. 用该框架比较四种HRTF插值方法
5. 开源Python实现

## 🏗️ 模型架构

输入为双耳声学特征（如ITD、ILD、谱线索）和个体HRTF模板；主干为贝叶斯推理模型，包含似然函数（基于噪声感知特征的高斯分布）和先验（均匀方向先验）；关键模块包括参数恢复（模拟数据）和行为拟合（33人实验）；输出为声源方向后验分布和个体参数（传感器噪声、谱权重等）。

## 📚 数据集

- 模拟数据（参数恢复实验，生成自模型）
- 33名参与者行为数据（声源定位实验，评估拟合）
- HRTF数据库（用于插值比较，如CIPIC、ARI等）

## 📊 实验结果

摘要未提供具体数值结果，但描述了参数恢复实验成功识别个体参数，行为拟合表明框架可靠；HRTF插值比较显示全空间覆盖和高频保真度是关键，插值算法次要。

## 🎯 结论与影响

本文通过推导显式似然函数，将统计验证引入贝叶斯声源定位模型，证明了其可靠性和实用性。该框架可回答空间听觉基础问题（如个体差异）和应用问题（如感知HRTF评估），为双耳音频领域提供了统计严谨的工具。开源实现促进可重复研究。

## ⚠️ 局限与未解决问题

未报告计算效率或实时性；行为数据仅33人，样本量较小；HRTF插值比较未包含所有流行方法；未讨论模型在复杂声学环境（如混响）下的表现。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
