---
title: "Toward Interpretable Speech Deepfake Detection using Artifact-Specific Experts and Calibrated Detection Scores"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音深度伪造检测"]
summary: "提出基于伪影特定专家的可解释语音深度伪造检测框架，通过校准的似然比提供可理解证据。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释AI</span> <span class="tag-pill tag-pill-soft">#伪影检测</span> <span class="tag-pill tag-pill-soft">#集成学习</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.21127</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.21127" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.21127" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于伪影特定专家的可解释语音深度伪造检测框架，通过校准的似然比提供可理解证据。
</div>

## 👥 作者与机构

**Viola Negroni** ¹ · Xin Wang · Wanying Ge · Paolo Bestagini · Junichi Yamagishi · Stefano Tubaro

**机构**：米兰理工大学 · 国立信息学研究所 · 索尼公司

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音安全、可解释AI方向研究者。建议重点阅读§3专家训练与校准方法及§4.2证据分析。可先看表1了解各专家检测的伪影类型。

## 🌍 研究背景

语音深度伪造检测对高安全性场景至关重要，但现有黑盒模型缺乏可解释性。此前工作多关注整体分类性能，未提供人类可理解的决策依据。本文旨在设计一个框架，通过多个伪影特定专家分别检测不同合成伪影，并输出校准后的证据分数，实现可解释的伪造检测。

## 💡 核心创新

1. 提出伪影特定专家框架，每个专家检测单一伪影
2. 使用校准对数似然比作为可解释证据分数
3. 集成专家输出实现最终分类并保持可解释性

## 🏗️ 模型架构

输入语音特征（如频谱）→ 五个伪影特定专家模型（每个专家针对一种合成伪影，如重采样、编码等）→ 每个专家输出校准后的对数似然比作为证据分数 → 集成模块聚合所有专家分数，通过阈值或分类器得到最终真/假判决。同时输出每个专家的支持/反对强度，提供可解释性。

## 📚 数据集

- ASVspoof 2019（训练/评估，包含多种合成语音）
- In-the-wild 数据集（评估，真实场景伪造语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | ASVspoof 2019 LA | 基线系统 1.0% | **0.8%** | -0.2% |
| t-DCF | ASVspoof 2019 LA | 基线系统 0.05 | **0.04** | -0.01 |

在ASVspoof 2019 LA上，所提框架在EER和t-DCF上均优于基线，且通过校准的专家证据分数提供了可解释性。跨数据集评估显示专家能泛化到未见过的伪造类型。消融实验验证了每个专家的贡献。

## 🎯 结论与影响

本文提出的伪影特定专家框架在保持高检测性能的同时提供了可解释证据，对语音安全领域有重要价值。未来可扩展更多伪影类型，并探索在真实场景中的部署。

## ⚠️ 局限与未解决问题

专家数量有限（仅五种伪影），可能无法覆盖所有合成方法；未报告推理延迟；专家训练依赖特定伪影标签，获取成本高；跨数据集泛化测试有限。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-24/">← 返回 2026-07-24 速递</a></div>
