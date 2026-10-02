---
title: "Soundwich: Video Generation with Layered and Controllable Audio"
date: 2026-10-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "Soundwich 无需训练，把冻结的音视频流匹配模型改造成可生成多条同步、可独立编辑音频轨（人声/音乐/音效/环境）的框架。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频生成</span> <span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.00691</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/CodyNing/Soundwich" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">CodyNing/Soundwich</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.00691" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.00691" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CodyNing/Soundwich" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Soundwich 无需训练，把冻结的音视频流匹配模型改造成可生成多条同步、可独立编辑音频轨（人声/音乐/音效/环境）的框架。
</div>

## 👥 作者与机构

**Zhuo Ning** ¹ · AmirHossein Naghi Razlighi · Sagi Polaczek · Daniel Cohen-Or · Ali Mahdavi-Amiri

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频联合生成、可控音频生成、多轨编辑的研究者与工程团队。建议通读，重点看 §3 的 shared scene representation 与跨模态路由设计，以及实验中的时间控制与分离度指标；先看方法图与消融表，再对照 human evaluation 结果判断可控性收益。

## 🌍 研究背景

此前音视频联合生成（如 MM-Diffusion、AVDiffusion 类工作）能合成同步声音，但音频通常输出为单一混合轨，无法按源级编辑，与影视/游戏后期中 speech、music、SFX、ambience 分轨的工作流不匹配。已有音频分离模型可事后拆轨，但分离误差与不同步问题会累积，且无法在生成阶段控制各源时间活动。本文要在不重新训练的前提下，让冻结的音视频流匹配模型直接产出多条同步且可独立编辑的音频 stem。

## 💡 核心创新

1. 训练-free 改造冻结音视频 flow-matching 模型为多 stem 生成器
2. shared scene representation 跨 stem 传递全局音视频上下文
3. 每条 stem 与对应视觉源做跨模态路由以提升一致性
4. 显式时间活动控制，支持独立 retime / mute / replace / remix

## 🏗️ 模型架构

输入为视频条件与各音频 stem 的文本/类别提示，主干沿用冻结的音视频 flow-matching 模型（含视觉分支与音频分支）。关键改动有三：一是为每个 stem 维护独立的音频 latent 流，实现源级分离；二是引入 shared scene representation，将全局音视频上下文注入各 stem 以保持整体连贯；三是跨模态路由模块，把每条 stem 与其对应视觉源（如说话人区域、乐器区域）做注意力交互。输出为多条与视频时间对齐的音频 stem，可分别重定时、静音、替换或重混。摘要未给出参数量。

## 📊 实验结果

摘要仅称实验与人类评估显示在时间控制、源分离与自然度上均有提升，并支持源级编辑，但未给出 SI-SDR、PESQ、FAD 或 MOS 等具体数值，也未列出所用数据集与基线名称，无法量化对比。

## 🎯 结论与影响

最强结论是：无需训练即可把单轨音视频生成模型升级为多轨可控生成器，且各 stem 保持同步与可编辑。这为音视频生成的可控性与后期工作流衔接提供了新范式，后续研究可沿 shared scene representation 与跨模态路由继续优化分离度与一致性。工业上对影视、游戏、短视频的自动分轨配音有直接价值。

## ⚠️ 局限与未解决问题

摘要未报告定量指标、数据集、基线对比与推理开销，训练-free 方案可能带来额外采样成本；多 stem 分离度与自然度的权衡缺乏消融；跨模态路由对无对应视觉源的音效（如环境声）如何生效未说明；人类评估细节与规模缺失。

## 🔗 开源资源

- **代码**：<https://github.com/CodyNing/Soundwich>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-02/">← 返回 2026-10-02 速递</a></div>
