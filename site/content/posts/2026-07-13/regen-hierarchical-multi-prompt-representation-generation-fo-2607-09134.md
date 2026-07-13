---
title: "ReGen: Hierarchical Multi-Prompt Representation Generation for Efficient Waveform Diffusion Models"
date: 2026-07-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "提出ReGen，一种层次化多提示表示生成框架，通过联合估计表示和数据的向量场，提升波形扩散模型的生成质量和效率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#波形生成</span> <span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#表示学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.09134</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://regenvoice.github.io/demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">regenvoice.github.io/demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.09134" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.09134" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://regenvoice.github.io/demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ReGen，一种层次化多提示表示生成框架，通过联合估计表示和数据的向量场，提升波形扩散模型的生成质量和效率。
</div>

## 👥 作者与机构

**Sang-Hoon Lee** ¹ · Ha-Yeong Choi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成、扩散模型方向的研究者。建议重点阅读§3的ReGen框架和§4的GFM公式，以及§5.2的ReGenVoice实验。可先看表1和表2对比结果。

## 🌍 研究背景

扩散模型在语音生成中取得显著进展，但训练速度慢。表示对齐（REPA）方法通过正则化中间表示加速训练，但可能隐式纠缠潜在变量，限制生成能力。本文旨在解决这一问题，提出层次化多提示表示生成框架ReGen，在单个扩散模型中联合估计表示和数据的多个向量场，并引入广义流匹配（GFM）提升泛化能力。

## 💡 核心创新

1. 提出层次化多提示表示生成框架ReGen，联合估计表示和数据的向量场
2. 引入广义流匹配（GFM）改进条件流匹配的泛化性
3. 在12.5Hz高度压缩潜在表示上显著提升波形生成质量
4. 实现6.25Hz潜在扩散模型，训练仅需4GPU 1天，RTF达0.08

## 🏗️ 模型架构

ReGen基于扩散Transformer（DiT）架构。输入为高度压缩的潜在表示（12.5Hz），通过层次化多提示机制生成多个表示向量场，并与数据向量场联合估计。采用广义流匹配（GFM）训练。ReGenVoice使用两阶段：语义编码器提取语义潜在，声学编码器提取声学潜在，在6.25Hz上运行LDM。模型参数量未明确给出。

## 📚 数据集

- LibriTTS（训练ReGenVoice，小数据集）
- VCTK（可能用于评估，摘要未明确）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriTTS测试集 | 未明确基线 | **强语音可懂度（具体值未给出）** | 未给出 |
| SIM | LibriTTS测试集 | 未明确基线 | **高说话人相似度（具体值未给出）** | 未给出 |
| RTF | 推理速度 | 未明确基线 | **0.08** | 未给出 |

摘要未提供具体数值指标，仅定性描述ReGen显著提升波形生成质量，ReGenVoice在WER和SIM上表现强，且训练高效（4GPU 1天），推理RTF为0.08。缺乏与SOTA的定量对比。

## 🎯 结论与影响

ReGen通过层次化多提示表示生成和广义流匹配，有效提升了波形扩散模型的生成质量和训练效率。ReGenVoice在6.25Hz低帧率下实现高语音可懂度和说话人相似度，展示了在资源受限场景下的潜力。该工作为高效语音生成提供了新思路。

## ⚠️ 局限与未解决问题

摘要未提供与现有方法的定量对比，缺乏消融实验验证各组件贡献。仅在小数据集上验证ReGenVoice，泛化性未知。未报告模型参数量和计算复杂度。GFM的理论分析不足。

## 🔗 开源资源

- **Demo / 试听**：<https://regenvoice.github.io/demo/>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-13/">← 返回 2026-07-13 速递</a></div>
