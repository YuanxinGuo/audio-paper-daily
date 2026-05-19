---
title: "Acoustic Interference: A New Paradigm Weaponizing Acoustic Latent Semantic for Universal Jailbreak against Large Audio Language Models"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频安全"]
summary: "提出声学干扰攻击（AIA），利用声学潜在语义（ALS）作为通用触发器，无需恶意音频内容即可破解大音频语言模型的安全对齐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#对抗攻击</span> <span class="tag-pill tag-pill-soft">#安全对齐</span> <span class="tag-pill tag-pill-soft">#声学潜在语义</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.18168</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.18168" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.18168" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出声学干扰攻击（AIA），利用声学潜在语义（ALS）作为通用触发器，无需恶意音频内容即可破解大音频语言模型的安全对齐。
</div>

## 👥 作者与机构

**Yanyun Wang** ¹ · Yu Huang · Zi Liang · Xixin Wu · Li Liu

**机构**：香港中文大学 · 腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、多模态对齐研究者。建议重点阅读§3（AIA方法）和§5（实验与可解释性分析），可先看表1的攻击成功率对比。

## 🌍 研究背景

大音频语言模型（LALM）集成音频模态后攻击面扩大。现有越狱范式将音频作为恶意载荷的载体，依赖语义优化、声学参数控制或加性扰动。然而，这些方法需要实例级优化，且假设音频必须包含恶意内容。本文挑战这一假设，发现仅凭声学潜在语义（ALS）即可干扰安全对齐，提出新范式。

## 💡 核心创新

1. 提出声学干扰攻击（AIA），将攻击载荷与音频解耦
2. 发现声学潜在语义（ALS）可作为通用越狱触发器
3. 无需实例级优化，实现指令无关的通用干扰音频
4. 揭示跨模态对齐的根本脆弱性
5. 在10个LALM和5个数据集上达到SOTA攻击成功率

## 🏗️ 模型架构

AIA包含两个阶段：首先，从音频生成模型的先验中提取声学潜在语义（ALS），通过预训练编码器将音频映射到潜在空间；然后，生成一组通用、指令无关的干扰音频，这些音频内容良性但富含特定ALS。攻击时，将干扰音频与标准恶意文本查询拼接，输入LALM，使模型绕过安全对齐。无需实例级优化。

## 📚 数据集

- AdvBench（攻击评估，含500条恶意指令）
- SafeBench（攻击评估，含100条恶意指令）
- MM-SafetyBench（攻击评估，含100条恶意指令）
- 自定义数据集（含5种音频类型，用于ALS提取）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 攻击成功率（ASR） | AdvBench | 现有最佳方法（如Audio Jailbreak）约70% | **88.5%** | +18.5% |
| 攻击成功率（ASR） | SafeBench | 现有最佳方法约65% | **82.3%** | +17.3% |

在10个LALM（包括LLaMA-Adapter、Qwen-Audio等）上，AIA平均攻击成功率88.5%，优于现有方法。可解释性分析显示，AIA导致推理路径偏移，且ALS中存在固有有效模式。跨数据集泛化实验表明，干扰音频具有通用性。

## 🎯 结论与影响

本文提出声学干扰攻击（AIA），证明仅凭声学潜在语义即可破解LALM安全对齐，无需恶意音频内容。该工作揭示了跨模态对齐的根本脆弱性，对LALM安全部署具有警示意义，可能推动更鲁棒的多模态安全机制研究。

## ⚠️ 局限与未解决问题

未讨论防御措施；实验仅针对开源LALM，对闭源模型效果未知；干扰音频的生成依赖预训练编码器，可能引入额外计算开销；未评估对正常音频任务（如语音识别）的影响。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
