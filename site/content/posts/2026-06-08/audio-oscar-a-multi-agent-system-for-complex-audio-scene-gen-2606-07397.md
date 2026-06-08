---
title: "Audio-Oscar: A Multi-Agent System for Complex Audio Scene Generation, Orchestration, and Refinement"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出多智能体框架Audio-Oscar，通过协作专家代理实现复杂音频场景的生成、编排与优化。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多智能体系统</span> <span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#音频场景生成</span> <span class="tag-pill tag-pill-soft">#反馈驱动优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07397</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/ziye26/Audio-Oscar" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">ziye26/Audio-Oscar</span></span></a><a class="oc-chip oc-chip-proj" href="https://audiooscar.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">audiooscar.github.io/</span></span></a><a class="oc-chip oc-chip-demo" href="https://audiooscar.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">audiooscar.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07397" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07397" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/ziye26/Audio-Oscar" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://audiooscar.github.io/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://audiooscar.github.io/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多智能体框架Audio-Oscar，通过协作专家代理实现复杂音频场景的生成、编排与优化。
</div>

## 👥 作者与机构

**Yifan Duan** ¹ · Qixiang Xu · Hengtao Wu · Zhanxun Liu · Wenhao Guan · Junxi Liu · Ziyang Ma · Kelu Xu · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、多智能体系统研究者。建议通读，重点看§3系统架构与§4实验设计，可先浏览demo页面了解生成效果。

## 🌍 研究背景

当前文本到音频生成在简单场景表现良好，但复杂音频场景（含语音、音效、音乐、时间结构等）的生成仍具挑战。现有方法缺乏对多元素协调、时间线规划及后期制作的系统支持。本文提出多智能体框架，通过分工协作解决该问题。

## 💡 核心创新

1. 多智能体协作框架，各代理负责不同音频要素
2. 细粒度时间线规划代理实现时序控制
3. 反馈驱动的迭代优化机制
4. 构建ASG-Bench基准，含场景描述与参考音频
5. 集成角色建模与语音设计代理

## 🏗️ 模型架构

输入复杂场景描述文本，由主控制器解析并分派至各专家代理：角色建模与语音设计代理、语音生成代理、时间线规划代理、模型选择代理、非语音生成代理、音频后期制作代理。各代理调用现有TTS/TTA/TTM模型，最终通过反馈优化模块迭代改进。整体为模块化流水线架构。

## 📚 数据集

- ASG-Bench（评估，含场景描述与参考音频对及纯文本描述）

## 📊 实验结果

摘要未提供具体量化指标，仅定性说明Audio-Oscar能有效生成匹配复杂场景描述的音频。实验部分可能包含用户调研或自动指标，但未在摘要中给出。

## 🎯 结论与影响

Audio-Oscar通过多智能体协作有效解决了复杂音频场景生成难题，展示了模块化设计的潜力。该工作为音频生成领域提供了新范式，有望推动可控、长时音频生成的发展，对影视、游戏等工业应用具有参考价值。

## ⚠️ 局限与未解决问题

摘要未提及局限性，可能包括：依赖现有生成模型质量、代理间协调开销、时间线规划精度有限、缺乏客观评估指标。此外，ASG-Bench规模未知，泛化性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/ziye26/Audio-Oscar>
- **项目主页**：<https://audiooscar.github.io/>
- **Demo / 试听**：<https://audiooscar.github.io/>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
