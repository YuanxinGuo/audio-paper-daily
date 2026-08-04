---
title: "Deep Learning-Based Active Trim Panels for Enhanced Aircraft Interior Noise Control"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#主动噪声控制"]
summary: "提出温度感知的SFANC方法，用轻量1D CNN动态选择控制滤波器，抑制飞机舱内多频噪声，应对温度变化。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#主动噪声控制</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动噪声控制</span> <span class="tag-pill tag-pill-soft">#1D CNN</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#航空噪声</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.02421</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.02421" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.02421" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出温度感知的SFANC方法，用轻量1D CNN动态选择控制滤波器，抑制飞机舱内多频噪声，应对温度变化。
</div>

## 👥 作者与机构

**Boxiang Wang** ¹ · Malte Misol · Zhengding Luo · Junwei Ji · Xiaoyi Shen · Dongyuan Shi · Woon-Seng Gan

**机构**：南洋理工大学 · 德国航空航天中心

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事主动噪声控制、ANC系统设计的研究者阅读。可重点看第3节方法部分和第4节数值仿真，了解1D CNN如何融合参考和误差信号进行温度感知。若时间有限，可略读引言和结论。

## 🌍 研究背景

飞机舱内多频噪声主要由发动机引起，频率随转速变化。主动噪声控制（ANC）中，选择性固定滤波器（SFANC）方法因低计算复杂度、高鲁棒性和快速响应而适用于此场景。然而，实际中衬里温度变化会改变声学和结构路径，导致降噪性能下降。现有SFANC未考虑温度影响，本文旨在通过温度感知的滤波器选择来解决该问题。

## 💡 核心创新

1. 提出温度感知SFANC（TP-SFANC）框架
2. 采用轻量1D CNN，多任务学习同时预测频率和温度
3. 利用参考和误差信号联合输入，动态选择最优控制滤波器
4. 数值仿真验证变温下多频噪声抑制有效性
5. 低计算复杂度，适合实时应用

## 🏗️ 模型架构

输入为参考信号和误差信号，经过预处理后送入轻量1D CNN。CNN采用多任务学习策略，输出频率特征和温度特征，用于动态选择最优控制滤波器。滤波器从预置的固定滤波器库中选取，以匹配当前噪声频率和温度条件。整体结构轻量，适合嵌入式实现。

## 📊 实验结果

摘要未提供具体数值指标，仅说明数值仿真验证了所提方法在变频率和变衬里温度下衰减多频噪声的有效性。无具体降噪量或对比数据。

## 🎯 结论与影响

本文提出TP-SFANC方法，通过1D CNN感知温度和频率，动态选择控制滤波器，有效应对飞机舱内多频噪声随温度变化的问题。该方法有望提升ANC系统在实际环境中的鲁棒性，为航空噪声控制提供新思路，并可能推广至其他温度敏感场景。

## ⚠️ 局限与未解决问题

摘要未提及实验细节，缺乏与现有方法的定量对比，也未报告计算开销或实时性能。数值仿真可能未考虑实际声场复杂性，且未提及是否进行物理实验验证。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
