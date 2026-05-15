---
title: "PresentAgent-2: Towards Generalist Multimodal Presentation Agents"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#基准测试", "#多模态智能体", "#多模态演示生成", "#对话系统", "#演示视频生成"]
summary: "提出一个智能体框架，从用户查询出发，自动研究、收集多模态资源并生成带对话和交互的演示视频。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#演示视频生成</span> <span class="tag-pill tag-pill-soft">#多模态智能体</span> <span class="tag-pill tag-pill-soft">#对话系统</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.11363</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/AIGeeksGroup/PresentAgent-2" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">AIGeeksGroup/PresentAgent-2</span></span></a><a class="oc-chip oc-chip-proj" href="https://aigeeksgroup.github.io/PresentAgent-2" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">aigeeksgroup.github.io/PresentAgent-2</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.11363" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.11363" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/AIGeeksGroup/PresentAgent-2" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://aigeeksgroup.github.io/PresentAgent-2" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一个智能体框架，从用户查询出发，自动研究、收集多模态资源并生成带对话和交互的演示视频。
</div>

## 👥 作者与机构

**Wei Wu** ¹ · Ziyang Xu · Zeyu Zhang · Yang Zhao · Hao Tang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态生成、智能体系统研究者。建议重点阅读第3节框架设计和第4节基准构建，可先看图1系统概览。

## 🌍 研究背景

演示生成领域从静态幻灯片制作向端到端演示视频生成发展，现有方法依赖预定义文档，缺乏对开放域查询的支持和多模态资源整合能力。本文旨在解决从用户查询到完整演示视频的自动化生成问题，支持单讲、讨论和交互三种模式。

## 💡 核心创新

1. 统一框架支持三种演示模式
2. 基于智能体的多模态资源收集与整合
3. 构建多模态演示基准及评估标准

## 🏗️ 模型架构

输入用户查询和演示模式，首先通过LLM总结主题并进行深度研究，收集文本、图像、GIF和视频等资源；然后构建幻灯片，生成模式特定脚本；最后合成幻灯片、音频和动态媒体为完整视频。支持单讲、讨论（多角色）和交互（问答）三种模式。

## 📚 数据集

- 自建多模态演示基准（评估，包含单讲、讨论、交互场景）

## 📊 实验结果

摘要未提供具体数值结果，但构建了包含三种场景的基准，并制定了内容质量、媒体相关性、动态媒体使用、对话自然性和交互接地等评估标准。

## 🎯 结论与影响

PresentAgent-2将演示生成从文档依赖的幻灯片创建扩展到查询驱动的、研究支撑的多模态演示视频生成，支持对话和交互。对智能体驱动的多模态内容生成方向有推动作用，工业上可用于自动制作教学或产品演示视频。

## ⚠️ 局限与未解决问题

未报告定量实验结果，缺乏与现有方法的对比；依赖外部LLM和检索工具，可能引入延迟和错误；基准规模未说明，评估标准的主观性可能影响可复现性。

## 🔗 开源资源

- **代码**：<https://github.com/AIGeeksGroup/PresentAgent-2>
- **项目主页**：<https://aigeeksgroup.github.io/PresentAgent-2>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
