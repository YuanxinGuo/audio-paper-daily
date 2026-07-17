---
title: "Large Audio Language Models for Spoofing-Aware Speaker Verification"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#说话人验证"]
summary: "系统评估大音频语言模型在欺骗感知说话人验证任务上的表现，发现零样本性能接近随机，但任务特定微调可缩小差距。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#说话人验证</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#欺骗检测</span> <span class="tag-pill tag-pill-soft">#反欺骗</span> <span class="tag-pill tag-pill-soft">#说话人验证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14753</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14753" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14753" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估大音频语言模型在欺骗感知说话人验证任务上的表现，发现零样本性能接近随机，但任务特定微调可缩小差距。
</div>

## 👥 作者与机构

**Sofya Savelyeva** ¹ · Mariia Perunova · Evgeny Kushnir · Artem Dvirniak · Dmitrii Korzh · Oleg Y. Rogov

**机构**：莫斯科物理技术学院 · Sber AI

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事说话人验证、反欺骗及大音频语言模型应用的研究者阅读。建议重点看第4节实验设置与第5节结果分析，尤其是表1-3的对比结果。可先看摘要与结论，再决定是否通读。

## 🌍 研究背景

文本转语音和语音克隆技术的进步使得高质量欺骗攻击变得廉价且可扩展，威胁自动说话人验证系统。现有防御主要通过二元反欺骗检测或欺骗感知说话人验证（SASV）来应对，当前系统以模块化ASV-CM融合和级联流水线为主。大音频语言模型（LALM）在相关音频任务上展现出潜力，但尚未被用于SASV。本文旨在系统评估LALM在SASV中的表现，探索其作为统一可审计基础的可能性。

## 💡 核心创新

1. 首次系统评估LALM用于SASV
2. 探索零样本、监督微调、推理训练和强化学习优化四种范式
3. 发现LALM零样本性能接近随机，但微调可缩小差距
4. 揭示多种竞争性SASV实现路径

## 🏗️ 模型架构

本文评估多种预训练LALM（如Qwen2-Audio、SALMONN等）用于SASV。输入为语音对（注册语音与测试语音），输出为自然语言判断（是否同一说话人及是否欺骗）。采用四种范式：零样本提示、监督微调（全参数或LoRA）、推理导向训练（思维链）、强化学习优化（基于偏好）。未给出参数量。

## 📚 数据集

- ASVspoof 2021 SASV（训练/评估，包含真实与欺骗语音对）
- VoxCeleb1（辅助训练，用于说话人识别预训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SASV-EER | ASVspoof 2021 SASV | 级联ASV-CM融合 2.5% | **微调LALM 3.1%** | +0.6% |
| min t-DCF | ASVspoof 2021 SASV | 级联ASV-CM融合 0.12 | **微调LALM 0.15** | +0.03 |

零样本LALM在SASV上接近随机（EER约50%），但通过监督微调（LoRA）可将EER降至3.1%，接近级联基线（2.5%）。推理训练和强化学习进一步改善，但未超越级联系统。消融实验显示，音频编码器质量对性能影响最大。

## 🎯 结论与影响

本文表明，尽管LALM在零样本SASV中表现不佳，但任务特定微调可使其达到接近级联系统的性能，且具备自然语言可解释性优势。这为统一可审计的SASV系统提供了新方向，但级联系统在精度上仍领先。对工业落地而言，LALM的推理延迟和计算成本需进一步优化。

## ⚠️ 局限与未解决问题

仅评估了有限几种LALM，未涵盖最新模型；实验仅在ASVspoof 2021数据集上进行，泛化性未知；未报告推理延迟和计算开销；级联基线未使用最先进的反欺骗模型；缺乏对LALM生成理由的定量评估。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
