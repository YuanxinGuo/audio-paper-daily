---
title: "SymphonyGen: 3D Hierarchical Orchestral Generation with Controllable Harmony Skeleton"
date: 2026-08-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出3D分层框架SymphonyGen，通过级联解码器分解小节、音轨和事件轴，实现可控的交响乐生成，并用强化学习优化声学奖励。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#交响乐生成</span> <span class="tag-pill tag-pill-soft">#分层生成</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#和声控制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.25498</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.25498" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.25498" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出3D分层框架SymphonyGen，通过级联解码器分解小节、音轨和事件轴，实现可控的交响乐生成，并用强化学习优化声学奖励。
</div>

## 👥 作者与机构

**Xuzheng He** ¹ · Nan Nan · Zhilin Wang · Ziyue Kang · Zhuoru Mo · Ao Li · Yu Pan · Xiaobing Li · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、符号音乐建模研究者阅读。建议重点阅读第3节（3D分层框架）和第4节（强化学习与采样算法），可先看图1和表2了解整体效果。

## 🌍 研究背景

交响乐生成需同时管理高层结构和密集多轨配器，现有符号模型在可扩展性和可控性之间存在矛盾。此前方法多采用扁平token流，难以处理长序列和复杂结构，且缺乏用户控制。SymphonyGen旨在通过3D分层解码和和声骨架条件解决此问题。

## 💡 核心创新

1. 3D分层解码器分解bar/track/event轴，降低内存
2. 节拍量化多音高和声骨架提供短谱条件
3. 基于CLaMP 3音频嵌入的跨模态声学奖励强化学习
4. 避免不和谐音的采样算法抑制音调冲突

## 🏗️ 模型架构

输入为符号音乐序列，首先提取节拍量化的多音高和声骨架作为条件。主干为级联解码器，分别沿bar、track、event三个轴生成，每个解码器可能基于Transformer或类似结构。解码顺序为bar→track→event，每个层级可接受条件。输出为符号音乐序列。强化学习阶段使用CLaMP 3音频嵌入计算奖励，推理时采用不和谐规避采样。

## 📊 实验结果

摘要未提供具体数值指标，但提到客观评估显示两种后训练机制（强化学习和采样算法）在保持旋律独立性的同时降低不和谐度，主观测试中SymphonyGen在质量和偏好上优于基线，尤其在普通听众中显著。

## 🎯 结论与影响

SymphonyGen通过3D分层框架和和声骨架控制，有效平衡了交响乐生成的可扩展性和可控性，强化学习和采样算法进一步提升了输出质量。该工作为复杂音乐生成提供了新思路，可能推动可控音乐生成工具的发展，对音乐创作辅助有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：依赖和声骨架条件，用户需提供或自动分析；强化学习奖励可能偏向特定风格；未报告推理延迟和参数量；对比基线可能有限。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-04/">← 返回 2026-08-04 速递</a></div>
