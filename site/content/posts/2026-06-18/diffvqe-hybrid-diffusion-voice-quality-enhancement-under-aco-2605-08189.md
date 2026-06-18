---
title: "DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "首个可复现的基于扩散的声学回声与噪声联合抑制模型，在性能与复杂度上超越判别式SOTA DeepVQE。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#声学回声控制</span> <span class="tag-pill tag-pill-soft">#联合去噪</span> <span class="tag-pill tag-pill-soft">#生成式方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.08189</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.08189" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.08189" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个可复现的基于扩散的声学回声与噪声联合抑制模型，在性能与复杂度上超越判别式SOTA DeepVQE。
</div>

## 👥 作者与机构

**Haljan Lugo** ¹ · Ernst Seidel · Pejman Mowlaee · Ziyue Zhao · Tim Fingscheidt

**机构**：布伦瑞克工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强与AEC领域的研究者。建议重点阅读§3的扩散模型架构设计与§4的实验对比，尤其是表1与表2。可复现的代码与训练框架值得关注。

## 🌍 研究背景

免提系统和扬声器中的声学回声与背景噪声是语音增强的经典难题。判别式端到端方法（如DeepVQE）在联合回声控制（AEC）与去噪中表现优异，但生成式方法（尤其是扩散模型）在语音增强中崭露头角。然而，此前尚无基于扩散的AEC模型被公开复现。本文首次提出可复现的扩散AEC模型DiffVQE，旨在超越判别式SOTA。

## 💡 核心创新

1. 首个可复现的扩散AEC模型
2. 联合回声与噪声的扩散条件生成框架
3. 利用URGENT Challenge数据集提升泛化性
4. 在性能与模型复杂度上均优于DeepVQE

## 🏗️ 模型架构

输入为含噪含回声的麦克风信号与参考信号，经短时傅里叶变换得到幅度谱。主干网络采用条件扩散模型，以噪声估计网络（类似U-Net）逐步去噪，同时以参考信号和噪声谱为条件。输出为干净语音的幅度谱估计，再结合相位恢复得到时域波形。模型参数量与计算量均低于DeepVQE。

## 📚 数据集

- Interspeech 2025 URGENT Challenge数据集（训练，多样高质量）
- ICASSP 2023 AEC Challenge数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | ICASSP 2023 AEC Challenge测试集 | DeepVQE (未给出具体值) | **优于DeepVQE (具体值未给出)** | 显著提升 |
| 模型参数量 | - | DeepVQE (未给出具体值) | **更小 (具体值未给出)** | 降低 |

实验表明，DiffVQE在回声与噪声抑制性能上全面超越判别式SOTA DeepVQE，同时模型参数量与计算复杂度更低。由于摘要未提供具体数值，详细结果需参考论文正文。

## 🎯 结论与影响

本文首次将扩散模型成功应用于联合回声与噪声抑制，并实现完全可复现。DiffVQE在性能与效率上均优于当前判别式SOTA，为生成式方法在AEC任务中开辟了新方向。对工业免提系统与扬声器产品的语音质量提升具有潜在应用价值。

## ⚠️ 局限与未解决问题

模型目前为非因果（non-causal），不适用于实时流式场景。摘要未提供具体数值对比，消融实验与泛化性分析有待补充。此外，仅与DeepVQE对比，缺乏与其他扩散增强模型的比较。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
