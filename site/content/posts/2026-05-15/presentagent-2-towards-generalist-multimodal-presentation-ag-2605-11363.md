---
title: "PresentAgent-2: Towards Generalist Multimodal Presentation Agents"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#交互式演示", "#多模态代理", "#多模态演示生成", "#演示视频生成", "#研究驱动"]
summary: "PresentAgent-2是一个从用户查询生成演示视频的智能体框架，支持单人、多人讨论和交互三种模式。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态演示生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#演示视频生成</span> <span class="tag-pill tag-pill-soft">#多模态代理</span> <span class="tag-pill tag-pill-soft">#交互式演示</span> <span class="tag-pill tag-pill-soft">#研究驱动</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.11363</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.11363" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.11363" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/AIGeeksGroup/PresentAgent-2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://aigeeksgroup.github.io/PresentAgent-2" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>PresentAgent-2是一个从用户查询生成演示视频的智能体框架，支持单人、多人讨论和交互三种模式。
</div>

## 👥 作者与机构

**Wei Wu** ¹ · Ziyang Xu · Zeyu Zhang · Yang Zhao · Hao Tang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态AI、人机交互领域研究者。建议重点阅读§3系统架构和§4实验部分，了解三种模式的设计与评估。可先看Figure 2概览流程。

## 🌍 研究背景

传统演示生成局限于静态幻灯片制作，缺乏端到端视频生成、多模态资源整合和交互能力。现有方法依赖预定义文档，无法从开放查询出发进行深度研究并生成包含文本、图像、GIF、视频的演示视频。本文旨在构建一个统一的智能体框架，支持单人讲解、多人讨论和实时问答三种模式。

## 💡 核心创新

1. 提出统一框架支持三种演示模式
2. 研究驱动的多模态资源收集机制
3. 基于检索的交互式问答模块
4. 构建多模态演示评估基准

## 🏗️ 模型架构

输入用户查询和演示模式 → 查询摘要与深度研究模块（收集文本、图像、GIF、视频）→ 幻灯片构建器 → 模式特定脚本生成器 → 媒体合成器（整合幻灯片、音频、动态媒体）→ 输出完整演示视频。三种模式共享核心组件，但脚本生成和交互模块不同。

## 📚 数据集

- 多模态演示基准（评估，包含单演示、讨论、交互场景）

## 📊 实验结果

摘要未提供具体数值结果，仅描述了基准的评估标准（内容质量、媒体相关性、动态媒体使用、对话自然度、交互基础）。实验部分可能包含消融研究和模式对比，但摘要未给出定量数据。

## 🎯 结论与影响

PresentAgent-2将演示生成从文档依赖的幻灯片制作扩展到查询驱动的、研究支撑的多模态视频生成，支持对话和交互。该工作为智能演示代理的发展提供了新范式，有望应用于教育、会议和内容创作领域。

## ⚠️ 局限与未解决问题

摘要未提及局限性。可能的问题包括：三种模式的实际效果缺乏定量对比；交互模式中问答的准确性依赖检索质量；未报告推理延迟和计算开销；基准的规模和多样性可能有限。

## 🔗 开源资源

- **代码**：<https://github.com/AIGeeksGroup/PresentAgent-2>
- **项目主页**：<https://aigeeksgroup.github.io/PresentAgent-2>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
