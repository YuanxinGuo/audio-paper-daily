---
title: "GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频大模型安全"]
summary: "提出基于梯度比掩码的频带选择性越狱攻击框架GRM，在保持高越狱成功率的同时显著降低对正常任务的效用损失。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频大模型安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#音频大模型</span> <span class="tag-pill tag-pill-soft">#越狱攻击</span> <span class="tag-pill tag-pill-soft">#频率选择</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.09222</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/159753Fetter/GRM" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">159753Fetter/GRM</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.09222" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.09222" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/159753Fetter/GRM" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于梯度比掩码的频带选择性越狱攻击框架GRM，在保持高越狱成功率的同时显著降低对正常任务的效用损失。
</div>

## 👥 作者与机构

**Yunqiang Wang** ¹ · Hengyuan Na · Di Wu · Miao Hu · Guocong Quan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频大模型安全、对抗攻击方向的研究者阅读。建议重点阅读第3节方法部分和第4节实验部分，尤其是GRM的频带选择机制和效用保持策略。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

音频大语言模型（ALLMs）支持语音交互，但引入了新的越狱漏洞。现有基于扰动的越狱方法未显式控制扰动频带，通用扰动虽能引发不安全响应，但会降低正常任务效用，留下行为足迹，暴露攻击。本文旨在解决全频带扰动导致效用下降的问题，探索频带选择性扰动能否在保持攻击效果的同时减少效用损失。

## 💡 核心创新

1. 提出梯度比掩码（GRM）框架，按越狱贡献与转录敏感度之比排序Mel频带
2. 将通用扰动限制在选定频带，并正则化偏离预期请求语义
3. 发现越狱成功率随频带覆盖非单调变化，效用损失随覆盖增加，支持频带选择性攻击
4. 在四个ALLM上验证，平均JSR达88.46%，效用损失显著低于基线
5. 开源代码，便于复现和后续研究

## 🏗️ 模型架构

GRM框架：输入音频经特征提取得到Mel频谱，计算每个频带的梯度比（越狱贡献/转录敏感度），选择Top-K频带，生成通用扰动并仅添加到这些频带，同时添加语义正则化项约束扰动不偏离原始请求。扰动通过迭代优化生成，最终输入ALLM触发不安全响应。

## 📊 实验结果

摘要未提供具体实验数据，仅提及在四个ALLM上平均JSR为88.46%，效用损失显著低于基线。未给出具体指标数值，无法进行详细对比。

## 🎯 结论与影响

GRM通过频带选择性扰动在保持高越狱成功率的同时显著降低效用损失，证明了全频带扰动并非必要。该工作为音频大模型安全提供了新视角，可能推动更隐蔽、更高效的攻击与防御研究，对工业界部署ALLM的安全评估有参考价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可推测：实验仅在四个ALLM上验证，泛化性未知；未讨论防御方法；未报告计算开销；频带选择机制可能依赖特定模型，迁移性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/159753Fetter/GRM>

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-11/">← 返回 2026-08-11 速递</a></div>
