---
title: "Sound Sparks Motion: Audio and Text Tuning for Video Editing"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频编辑"]
summary: "提出无需训练的测试时调优框架，通过调整音频潜变量和文本条件扰动实现视频运动编辑。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#运动编辑</span> <span class="tag-pill tag-pill-soft">#多模态条件调优</span> <span class="tag-pill tag-pill-soft">#音频引导</span> <span class="tag-pill tag-pill-soft">#测试时调优</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.15307</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://amirhossein-razlighi.github.io/Sound_Sparks_Motion/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">amirhossein-razlighi.github.io/Sound_Sparks_M…</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.15307" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.15307" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://amirhossein-razlighi.github.io/Sound_Sparks_Motion/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无需训练的测试时调优框架，通过调整音频潜变量和文本条件扰动实现视频运动编辑。
</div>

## 👥 作者与机构

**AmirHossein Naghi Razlighi** ¹ · Aryan Mikaeili · Ali Mahdavi-Amiri · Daniel Cohen-Or · Yiorgos Chrysanthou

**机构**：西蒙菲莎大学 · 阿尔伯塔大学 · 特拉维夫大学 · 塞浦路斯大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合视频生成与编辑方向的研究者。重点看§3方法部分和§4.2跨视频迁移实验。可先看图3的框架概览。

## 🌍 研究背景

现有视频生成模型擅长外观变化，但难以产生精确的局部动作或状态转换。运动编辑是难点，通常需要大量训练数据或模型微调。本文提出在测试时调优多模态条件信号（音频和文本），无需修改模型权重，实现运动编辑。

## 💡 核心创新

1. 测试时调优音频潜变量和文本残差扰动
2. 利用视觉语言模型提供运动对齐反馈
3. 跨视频迁移学习到的运动编辑方向

## 🏗️ 模型架构

输入源视频及其音频，提取音频潜变量；文本条件添加残差扰动。调优过程中，固定视频生成模型权重，仅优化音频潜变量和文本残差。使用预训练视觉语言模型评估生成视频中运动是否出现，作为监督信号。结合正则化和感知-时间约束保持内容与视觉质量。

## 📊 实验结果

摘要未提供具体定量指标，但定性结果显示运动编辑有效，且调优后的潜变量可跨视频迁移，表明捕获了可复用的运动编辑方向。

## 🎯 结论与影响

多模态条件调优，特别是音频路径，为运动感知视频编辑提供了有前景的方向。测试时调优可作为轻量级探测机制，揭示模型中嵌入的潜在运动控制。

## ⚠️ 局限与未解决问题

缺乏定量指标和与现有方法的对比；依赖视觉语言模型反馈的准确性；调优过程可能耗时；仅验证了特定模型架构。

## 🔗 开源资源

- **项目主页**：<https://amirhossein-razlighi.github.io/Sound_Sparks_Motion/>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
