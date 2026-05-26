---
title: "Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频对抗攻击"]
summary: "提出Token-Aware Gradient Optimization (TAGO)，通过保留高梯度能量的音频token对应波形梯度，实现稀疏越狱攻击，证明密集波形更新冗余。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频对抗攻击</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#越狱攻击</span> <span class="tag-pill tag-pill-soft">#梯度优化</span> <span class="tag-pill tag-pill-soft">#稀疏优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.04700</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.04700" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.04700" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Token-Aware Gradient Optimization (TAGO)，通过保留高梯度能量的音频token对应波形梯度，实现稀疏越狱攻击，证明密集波形更新冗余。
</div>

## 👥 作者与机构

**Zheng Fang** ¹ · Xiaosen Wang · Shenyi Zhang · Shaokang Wang · Zhijin Ge

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、对抗攻击方向研究者。建议重点读§3（梯度分析）和§4（方法），表1展示稀疏化后攻击成功率保持情况。可复现代码验证token保留比例与攻击效果关系。

## 🌍 研究背景

音频语言模型（ALM）越狱攻击通过优化音频扰动诱导不安全生成，现有方法密集更新整个波形。但token对齐梯度能量分布高度非均匀，暗示仅少数token主导优化信号。本文旨在利用这一结构实现稀疏优化。

## 💡 核心创新

1. 发现token对齐梯度能量非均匀分布
2. 提出TAGO：保留高梯度能量token的波形梯度
3. 在Qwen3-Omni等模型上以25% token保留率维持86% ASR
4. 证明密集波形更新冗余，推动稀疏安全对齐研究

## 🏗️ 模型架构

输入音频波形 → 提取音频token（如HuBERT编码）→ 计算token对齐梯度能量 → 按能量排序保留top-k token的梯度（其余掩码）→ 使用保留梯度更新扰动 → 迭代优化。主干为任意ALM（如Qwen3-Omni），TAGO作为优化器插件。

## 📚 数据集

- 未明确指定数据集（攻击测试在Qwen3-Omni等模型上进行）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| ASR_l | Qwen3-Omni | Full token retention 87% | **Token retention ratio 0.25: 86%** | -1% |

在Qwen3-Omni、Salmonn、Qwen2-Audio上，TAGO以0.25 token保留率保持接近全token的攻击成功率（86% vs 87%），且显著减少优化参数。梯度能量分析显示前10% token贡献大部分梯度能量。

## 🎯 结论与影响

本文揭示ALM越狱攻击中梯度能量集中于少数token，提出TAGO实现高效稀疏攻击。未来安全对齐研究应关注token级梯度结构，设计针对性防御。对工业部署，可降低攻击计算成本。

## ⚠️ 局限与未解决问题

未在更多ALM（如AudioGPT）上验证；未讨论防御方法；token保留比例选择依赖启发式；未分析稀疏化对攻击隐蔽性的影响。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
