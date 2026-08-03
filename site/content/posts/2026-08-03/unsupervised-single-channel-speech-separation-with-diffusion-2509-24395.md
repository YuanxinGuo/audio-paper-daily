---
title: "Unsupervised Single-Channel Speech Separation with Diffusion under Speaker-Embedding Guidance"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出无监督单通道语音分离方法，利用扩散模型和说话人嵌入引导，在逆扩散过程中保持说话人一致性并分离不同说话人。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#无监督学习</span> <span class="tag-pill tag-pill-soft">#说话人嵌入</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.24395</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://runwushi.github.io/UnSepDiff_demo" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">runwushi.github.io/UnSepDiff_demo</span></span></a><a class="oc-chip oc-chip-demo" href="https://runwushi.github.io/UnSepDiff_demo" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">runwushi.github.io/UnSepDiff_demo</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.24395" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.24395" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://runwushi.github.io/UnSepDiff_demo" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://runwushi.github.io/UnSepDiff_demo" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无监督单通道语音分离方法，利用扩散模型和说话人嵌入引导，在逆扩散过程中保持说话人一致性并分离不同说话人。
</div>

## 👥 作者与机构

**Runwu Shi** ¹ · Kai Li · Yiyan Wang · Jiang Wang · Chang Li · Ragib Amin Nihal · Sihan Tan · Kazuhiro Nakadai

**机构**：东京工业大学 · 中国科学院 · 北京邮电大学 · 早稻田大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离和生成模型研究者阅读。建议重点阅读第3节方法部分和第4节实验部分，特别是说话人嵌入引导和分离求解器的设计。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

传统语音分离依赖成对混合语音进行监督训练，但合成数据与真实场景存在差距。源模型范式通过仅训练纯净语音的生成模型，将分离视为逆问题，但无条件扩散模型缺乏说话人级条件，导致分离结果中说话人身份不一致。本文旨在解决无监督源模型分离中说话人一致性问题。

## 💡 核心创新

1. 提出说话人嵌入引导，在逆扩散过程中保持说话人一致性
2. 设计分离导向的求解器，适配语音分离任务
3. 实现完全无监督的源模型分离，无需成对混合数据
4. 在多个数据集上验证有效性，并开源代码和音频样本

## 🏗️ 模型架构

输入为混合语音，通过扩散模型进行逆扩散过程。主干为扩散生成模型，训练时仅使用无回声纯净语音。在逆扩散过程中，引入说话人嵌入引导，利用预训练说话人编码器提取嵌入，通过引导项使分离出的每个音轨保持说话人一致性，同时推动不同说话人嵌入分离。此外，提出分离导向的求解器，优化逆扩散步骤。输出为分离后的多个语音流。

## 📚 数据集

- WSJ0-2mix（评估）
- Libri2Mix（评估）
- WSJ0-3mix（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi | WSJ0-2mix | 未提供 | **未提供** | 未提供 |

摘要中未提供具体数值，但声称在无监督源模型分离任务上性能显著提升，并通过大量实验验证。具体指标和对比结果需查阅论文正文。

## 🎯 结论与影响

本文提出了一种无监督语音分离方法，通过说话人嵌入引导和分离导向求解器，有效解决了扩散模型在分离中说话人身份不一致的问题。该方法无需成对混合数据，有望缩小合成数据与真实场景的差距，对无监督语音分离研究有重要推动作用，并可能促进实际应用中的泛化能力。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为无监督方法，可能依赖预训练说话人编码器的质量，且扩散模型推理速度较慢，未报告计算开销。实验仅在合成混合数据上评估，真实场景泛化性未知。

## 🔗 开源资源

- **项目主页**：<https://runwushi.github.io/UnSepDiff_demo>
- **Demo / 试听**：<https://runwushi.github.io/UnSepDiff_demo>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-03/">← 返回 2026-08-03 速递</a></div>
