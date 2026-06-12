---
title: "The Moving Drone: Negotiating Agency Between the Voice and the Virtual"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出一种将传统静态 drone 变为动态虚拟代理的音乐系统，通过实时循环和生成式AI实现人声与虚拟 drone 的协作。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#交互式音乐系统</span> <span class="tag-pill tag-pill-soft">#生成式AI</span> <span class="tag-pill tag-pill-soft">#印度斯坦音乐</span> <span class="tag-pill tag-pill-soft">#实时音频处理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13640</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13640" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13640" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种将传统静态 drone 变为动态虚拟代理的音乐系统，通过实时循环和生成式AI实现人声与虚拟 drone 的协作。
</div>

## 👥 作者与机构

**Nithya Shikarpur** ¹ · Victor Arul · Anna Huang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对交互式音乐系统、生成式AI在音乐中应用感兴趣的读者。建议重点阅读系统设计部分（§3）和讨论部分（§5），了解其技术实现与艺术理念。

## 🌍 研究背景

印度斯坦音乐中，旋律围绕持续音（drone）展开，传统上由 tanpura 提供静态 drone。现有音乐AI追求高保真和逼真度，引发音乐社区对就业替代的焦虑。本文旨在探索低保真生成式AI在传统音乐实践中的角色，将虚拟 drone 从被动伴奏转变为主动、共生的音乐代理。

## 💡 核心创新

1. 使用四个独立循环器实现实时反馈循环
2. 通过变调引入动态旋律变化
3. 集成GaMaDHaNi生成式AI模型进行音色重塑
4. 有意利用低保真生成输出，强调人类诠释的必要性

## 🏗️ 模型架构

系统基于Max/MSP构建，包含四个独立循环器作为虚拟drone。人声即兴演唱时，循环器实时循环填充音频。通过变调处理引入旋律移动，再通过GaMaDHaNi（一种基于条件的音高到语音生成AI模型）对循环音频进行音色重塑，最终输出低保真生成音频。

## 📊 实验结果

摘要未提供定量实验结果，本文为艺术实践作品，主要展示系统设计与创作理念。

## 🎯 结论与影响

本文提出一种将传统音乐实践与生成式AI结合的新范式，通过低保真输出强调人类在音乐创作中的核心作用。对后续研究的影响在于挑战了AI音乐生成中高保真度的主流追求，为交互式音乐系统提供了新思路。工业落地方面，可能启发更多以协作为导向的音乐工具。

## ⚠️ 局限与未解决问题

缺乏定量评估和用户研究，系统性能与稳定性未报告。作为艺术实践，技术细节不够深入，难以复现。未讨论实时延迟、音质等工程问题。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
