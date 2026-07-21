---
title: "UniPASE: A Generative Model for Universal Speech Enhancement with High Fidelity and Low Hallucinations"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "UniPASE 基于低幻觉 PASE 框架，通过 DeWavLM-Omni 模块和 Adapter+Vocoder 结构实现多采样率通用语音增强，在 URGENT 2026 挑战赛客观评测中获第一。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#通用语音增强</span> <span class="tag-pill tag-pill-soft">#表示学习</span> <span class="tag-pill tag-pill-soft">#知识蒸馏</span> <span class="tag-pill tag-pill-soft">#多采样率</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.14606</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/xiaobin-rong/unipase/" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">xiaobin-rong/unipase/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.14606" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.14606" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/xiaobin-rong/unipase/" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>UniPASE 基于低幻觉 PASE 框架，通过 DeWavLM-Omni 模块和 Adapter+Vocoder 结构实现多采样率通用语音增强，在 URGENT 2026 挑战赛客观评测中获第一。
</div>

## 👥 作者与机构

**Xiaobin Rong** ¹ · Zheng Wang · Yushi Wang · Jun Gao · Jing Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和表示学习方向的研究者。建议通读，重点看 §3 的 DeWavLM-Omni 知识蒸馏设计和 §4 的 Adapter+Vocoder 结构。可先看表 1 和表 2 了解性能提升。

## 🌍 研究背景

通用语音增强（USE）旨在从多种失真中恢复语音，并支持多采样率。现有方法如 DEMUCS、FullSubNet 等在特定场景表现好，但难以统一处理多种失真和采样率。此外，增强模型常引入语言幻觉（linguistic hallucination），即生成不存在的音素。PASE 框架通过表示级增强减少幻觉，但仅支持单采样率。本文扩展 PASE 到 USE，提出 UniPASE，解决多采样率、高保真度和低幻觉的平衡问题。

## 💡 核心创新

1. DeWavLM-Omni：从 WavLM 知识蒸馏的统一表示增强模块
2. Adapter 模块将增强的语音表示转换为含丰富声学细节的声学表示
3. PostNet 将 16kHz 波形上采样至 48kHz 再重采样回原始采样率
4. 多采样率输入输出无缝处理

## 🏗️ 模型架构

输入波形经 DeWavLM-Omni 模块（基于 WavLM 知识蒸馏）转换为干净的语言学表示；Adapter 模块将该表示转换为声学表示；神经声码器（Vocoder）从声学表示重建 16kHz 波形；PostNet 将波形上采样至 48kHz 再重采样回原始采样率，支持多采样率输出。整体为级联结构：DeWavLM-Omni → Adapter → Vocoder → PostNet。

## 📚 数据集

- 大规模监督多失真数据集（训练，未说明具体名称）
- URGENT 2026 挑战赛评估集（评估，包含子任务和全任务）

## 📊 实验结果

摘要未提供具体指标数值，仅称在多个评估数据集上达到或超越现有 SOTA，并在 URGENT 2026 挑战赛客观评测中获第一名。具体性能需查阅论文正文。

## 🎯 结论与影响

UniPASE 通过表示级增强和知识蒸馏实现了高保真、低幻觉的通用语音增强，支持多采样率。其 DeWavLM-Omni 模块有效减少语言幻觉，Adapter+Vocoder 结构保证声学细节。该工作为 USE 提供了新范式，有望推动工业级多场景语音增强系统的落地。

## ⚠️ 局限与未解决问题

摘要未提及推理延迟和参数量；PostNet 上采样至 48kHz 再重采样可能引入额外计算开销；仅在 URGENT 2026 数据集上评估，泛化性需更多验证；未与最新扩散模型（如 DiffWave）对比。

## 🔗 开源资源

- **代码**：<https://github.com/xiaobin-rong/unipase/>

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
