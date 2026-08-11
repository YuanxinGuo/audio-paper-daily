---
title: "Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑"]
summary: "提出SIEDD，一种基于分层编解码器离散扩散的文本引导语音修复与编辑框架，在RealEdit基准上达到最优编辑性能，并优于自回归基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音修复</span> <span class="tag-pill tag-pill-soft">#离散扩散</span> <span class="tag-pill tag-pill-soft">#编解码器</span> <span class="tag-pill tag-pill-soft">#文本引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.06424</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/iftachShoham/SIEDD" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">iftachShoham/SIEDD</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.06424" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.06424" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/iftachShoham/SIEDD" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SIEDD，一种基于分层编解码器离散扩散的文本引导语音修复与编辑框架，在RealEdit基准上达到最优编辑性能，并优于自回归基线。
</div>

## 👥 作者与机构

**Iftach Shoham** ¹ · Tali Dror · Oren Gal · Haim Permuter · Gilad Katz · Eliya Nachmani

**机构**：本古里安大学 · 谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成、编辑与修复方向的研究者。建议重点阅读第3节（HiCoDD架构）与第4节（实验设置与结果），可先看表1与表2对比。若对扩散模型在音频中的应用感兴趣，可通读全文。

## 🌍 研究背景

语音录音常包含缺失、损坏或错误区域，需要在不重新合成整个话语的情况下进行修复或编辑。语音修复恢复缺失片段，语音编辑根据编辑后的文本替换内容。现有方法多基于自回归模型或单码本扩散，难以同时保持说话人身份、韵律、时序和录音条件的一致性。离散扩散模型因能迭代细化掩码token并联合左右上下文而适合此任务，但如何有效利用RVQ层级结构仍待探索。本文提出SIEDD，通过分层条件扩散解决该问题。

## 💡 核心创新

1. 提出HiCoDD架构，按RVQ生成顺序将已生成码本作为干净上下文，仅对当前码本扩散，实现无泄漏联合训练
2. 结合音素级条件、跨度局部化无分类器引导和时长预测，支持固定时长修复与可变时长编辑
3. 在RealEdit基准上达到最优编辑性能，并在多种修复场景下优于自回归基线
4. 开源代码，便于复现与后续研究

## 🏗️ 模型架构

SIEDD采用离散扩散框架，输入为文本转录和音频的RVQ码本序列。主干网络为HiCoDD，它按RVQ层级顺序处理：对于每个码本级，将之前生成的码本作为干净、已承诺的声学上下文，仅对当前码本应用扩散过程。模型结合音素级条件（通过文本编码器提取）、跨度局部化无分类器引导（用于增强编辑区域的保真度）和时长预测模块（用于可变时长编辑）。输出为修复或编辑后的音频码本，经解码器合成波形。

## 📚 数据集

- RealEdit（评估，用于语音编辑和修复基准）
- 可能使用LibriTTS或VCTK（训练，摘要未明确，但通常此类任务使用）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 编辑性能（具体指标未给出） | RealEdit | 未给出具体值 | **最佳整体性能** | 未给出具体数值 |
| 修复性能（具体指标未给出） | RealEdit（单/多缺口） | 自回归基线 | **优于所有自回归基线** | 未给出具体数值 |

摘要指出SIEDD在RealEdit基准上达到最佳整体语音编辑性能，并在所有语音修复设置（单缺口和多缺口）中优于评估的自回归基线。但未提供具体指标数值，如PESQ、WER等。实验表明显式建模码本层级显著改善了上下文保留的语音重建和编辑。

## 🎯 结论与影响

SIEDD通过显式建模RVQ码本层级，在文本引导的语音修复和编辑任务中取得了最优性能，证明了分层离散扩散的有效性。该工作为语音编辑领域提供了新思路，有望推动基于扩散的生成模型在音频编辑中的应用。对于工业界，该模型可应用于语音内容修正、配音等场景，提高编辑效率和质量。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为审稿人可看出：缺乏与更多基线（如基于GAN或Flow的方法）的对比；未报告推理延迟或计算成本；未讨论对未见说话人/噪声环境的泛化能力；未提供主观听感评估（如MOS）。

## 🔗 开源资源

- **代码**：<https://github.com/iftachShoham/SIEDD>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
