---
title: "CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "CookVoice提出统一框架，将人声分解为内容、韵律和风格三因子，实现语音与歌声生成、风格控制、声音模仿、转换和编辑等多种任务，仅43.51M参数且支持4步ODE高效推理。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音生成</span> <span class="tag-pill tag-pill-soft">#歌声生成</span> <span class="tag-pill tag-pill-soft">#风格控制</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11590</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://haoweilou.github.io/CookVoice/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">haoweilou.github.io/CookVoice/</span></span></a><a class="oc-chip oc-chip-demo" href="https://haoweilou.github.io/CookVoice/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">haoweilou.github.io/CookVoice/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11590" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11590" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://haoweilou.github.io/CookVoice/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://haoweilou.github.io/CookVoice/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>CookVoice提出统一框架，将人声分解为内容、韵律和风格三因子，实现语音与歌声生成、风格控制、声音模仿、转换和编辑等多种任务，仅43.51M参数且支持4步ODE高效推理。
</div>

## 👥 作者与机构

**Haowei Lou** ¹ · Hye-Young Paik · Dai Jia · Kai Li · Lina Yao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成、歌声合成、多模态生成方向的研究者。建议重点阅读第3节（方法）中的因子分解与对齐策略，以及第4节（实验）中的可控性评估。可先看摘要中的Demo页面直观感受效果，再深入模型细节。

## 🌍 研究背景

人声生成领域已发展出语音合成、歌声合成、声音克隆和编辑等独立任务，但现有系统多为特定任务设计，依赖任务相关的架构、控制信号或自回归解码，限制了细粒度控制和推理效率。本文提出统一框架CookVoice，通过将人声分解为内容、韵律和风格三个因子，实现多任务、多风格、多模态的人声生成，旨在解决现有方法的碎片化和低效问题。

## 💡 核心创新

1. 提出三因子分解（内容、韵律、风格）统一人声表示
2. 设计灵活对齐策略，将文本、风格、韵律控制信号映射到频谱帧级
3. 支持多种任务（TTS、歌声合成、风格控制、模仿、转换、编辑）
4. 仅43.51M参数，支持4步ODE高效推理
5. 统一模型实现语音与歌声生成，无需任务特定架构

## 🏗️ 模型架构

CookVoice采用统一框架，输入为文本、风格和韵律控制信号，通过编码器提取内容、韵律和风格因子，并设计对齐策略将这些控制信号映射到频谱的帧级。主干网络可能基于扩散模型或流匹配，使用ODE求解器进行推理，支持4步采样。输出为梅尔频谱，可进一步合成波形。具体网络结构未在摘要中详述，但参数量为43.51M。

## 📊 实验结果

摘要中未提供具体数值指标，仅提及生成质量与现有TTS和歌声合成基线相当，但风格和韵律可控性更强。与大规模基线相比，CookVoice以43.51M参数和4步ODE推理达到可比性能，表明其高效性。具体实验数据需查阅论文。

## 🎯 结论与影响

CookVoice通过统一框架实现了多任务、多风格的人声生成，以较小模型和高效推理达到与大规模基线相当的质量，同时提供更强的可控性。该工作有望推动人声生成领域的统一建模，减少任务特定系统的冗余，并为实时应用提供可能。

## ⚠️ 局限与未解决问题

摘要未提及明显局限，但作为审稿人可看出：缺乏与最新SOTA的详细对比，未报告主观MOS等指标，未讨论多任务联合训练可能带来的任务干扰，以及风格控制的具体粒度未量化。此外，仅43.51M参数可能限制复杂风格建模。

## 🔗 开源资源

- **项目主页**：<https://haoweilou.github.io/CookVoice/>
- **Demo / 试听**：<https://haoweilou.github.io/CookVoice/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-15/">← 返回 2026-08-15 速递</a></div>
