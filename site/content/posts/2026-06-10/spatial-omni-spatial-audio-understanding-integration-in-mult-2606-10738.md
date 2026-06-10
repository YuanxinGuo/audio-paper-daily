---
title: "Spatial-Omni: Spatial Audio Understanding Integration in Multimodal LLMs via FOA Encoding"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出Spatial-Omni，通过SO-Encoder将一阶Ambisonics空间音频注入多模态大语言模型，实现空间音频理解，无需修改原音频编码器。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频理解</span> <span class="tag-pill tag-pill-soft">#多模态大语言模型</span> <span class="tag-pill tag-pill-soft">#一阶Ambisonics</span> <span class="tag-pill tag-pill-soft">#空间问答</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10738</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/dieKarotte/Spatial-Omni" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">dieKarotte/Spatial-Omni</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10738" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10738" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/dieKarotte/Spatial-Omni" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Spatial-Omni，通过SO-Encoder将一阶Ambisonics空间音频注入多模态大语言模型，实现空间音频理解，无需修改原音频编码器。
</div>

## 👥 作者与机构

**Zhiyuan Zhu** ¹ · Yixuan Chen · Yiwen Shao · Wenxiang Guo · Changhao Pan · Yu Zhang · Yuxiang Wang · Wei Liu · … 等 8 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事多模态LLM、空间音频理解的研究者阅读。建议重点看§3的SO-Encoder设计和§4的SO-Bench构建与实验结果。可先看表1和表2了解性能提升。

## 🌍 研究背景

现有的大语言模型主要处理单声道音频，忽略了空间音频中的声源定位、空间关系推理等空间线索。尽管已有一些工作尝试将空间音频引入LLM，但通常需要修改原始音频编码器或增加大量计算开销。本文旨在以轻量级方式将FOA空间音频作为独立模态注入现有Omni LLM，同时保持通用音频理解能力。

## 💡 核心创新

1. 提出SO-Encoder，将FOA空间音频编码为空间token，不修改原音频编码器
2. 构建SO-Dataset，包含400K FOA音频和2.1M空间问答对
3. 设计SO-Bench，覆盖16个空间音频理解子任务
4. 采用高效分阶段训练策略，提升空间音频理解性能

## 🏗️ 模型架构

输入为四通道FOA空间音频，首先通过SO-Encoder提取空间特征，SO-Encoder由卷积层和Transformer组成，输出空间token序列。这些空间token与原始单声道音频token（由原音频编码器提取）拼接，送入Omni LLM的跨模态融合层。整体参数量未明确给出，但声称轻量级。

## 📚 数据集

- SO-Dataset（训练，400K FOA音频片段，来自开源数据、真实录音和仿真）
- SO-QA（训练，2.1M空间问答对）
- SO-Bench（评估，16个子任务，包括检测、定位、关系推理等）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 空间音频理解准确率 | SO-Bench | Qwen2-Audio (7B) 约40% | **Spatial-Omni 约65%** | +25% |

在SO-Bench的16个子任务上，Spatial-Omni显著优于现有开源LALM和Omni LLM模型，如Qwen2-Audio和Mini-Omni，在空间定位和关系推理任务上提升尤为明显。同时，在通用音频理解任务（如AudioSet）上性能保持合理水平，未出现明显下降。

## 🎯 结论与影响

Spatial-Omni以轻量级方式成功将空间音频理解能力注入多模态LLM，证明了FOA编码作为独立模态的有效性。该工作为空间音频与LLM的融合提供了新范式，有望推动具身智能、虚拟现实等应用中的空间场景理解。

## ⚠️ 局限与未解决问题

实验仅在SO-Bench上评估，缺乏在真实复杂场景下的泛化性验证；未报告推理延迟和参数量；SO-Encoder的设计可能对高阶Ambisonics支持有限；未与端到端训练的空间音频LLM进行对比。

## 🔗 开源资源

- **代码**：<https://github.com/dieKarotte/Spatial-Omni>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
