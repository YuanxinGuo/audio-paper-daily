---
title: "Robust Workflow Generation via Adversarial Learning for Audio Deepfake Detection"
date: 2026-09-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "提出 ROGUE 双智能体框架，用扰动智能体与策略智能体对抗学习，动态编排多个检测工具以提升音频深伪检测的鲁棒性与泛化性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对抗学习</span> <span class="tag-pill tag-pill-soft">#语音合成检测</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#工作流编排</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.20063</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.20063" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.20063" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 ROGUE 双智能体框架，用扰动智能体与策略智能体对抗学习，动态编排多个检测工具以提升音频深伪检测的鲁棒性与泛化性。
</div>

## 👥 作者与机构

**Xiang Li** ¹ · Pin-Yu Chen · Wenqi Wei

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频深伪检测与鲁棒性研究的读者。建议重点看双智能体对抗训练机制与工作流生成的形式化定义（方法节），以及跨数据集与真实损坏的实验表。若关注工程落地，可先看自适应工具选择策略部分；若关注方法创新，需确认扰动智能体是否仅覆盖信号级扰动。

## 🌍 研究背景

语音合成与声音转换技术使音频深伪愈发逼真，带来安全风险。现有检测方法在受控条件下表现良好，但面对真实世界的扰动与损坏时泛化性差。已有工作多依赖单一检测模型或固定集成，缺乏对扰动条件的自适应能力。本文要解决的核心问题是：如何在分布偏移与信号损坏下，动态构建鲁棒的检测流程，从而提升检测系统的可靠性与泛化能力。

## 💡 核心创新

1. 将检测工作流生成建模为序贯决策问题
2. 提出扰动智能体与策略智能体双智能体对抗范式
3. 实现扰动感知的工具选择与自适应执行策略
4. 通过对抗学习提升对分布偏移的鲁棒性

## 🏗️ 模型架构

ROGUE 将音频深伪检测流程生成形式化为序贯决策问题。输入为待检测音频，扰动智能体生成音频扰动以模拟真实损坏，策略智能体在扰动条件下学习选择并执行多个检测工具，形成动态工作流。两个智能体通过对抗学习交替优化，使策略智能体逐步获得扰动感知的工具选择与自适应执行能力。输出为检测工具序列及其判定结果。摘要未给出具体主干网络名称与参数量。

## 📚 数据集

- 多个音频深伪检测数据集（训练与评估，具体名称摘要未给出）
- 真实世界损坏条件（评估鲁棒性）

## 📊 实验结果

摘要仅声称在多个数据集与真实世界损坏条件下，ROGUE 在鲁棒性与泛化性上持续优于强基线，但未给出任何具体指标数值、数据集名称或对比方法名称，因此无法量化其提升幅度。消融实验、效率指标与跨数据集泛化细节均未在摘要中披露。

## 🎯 结论与影响

本文最强结论是：对抗式优化的工作流生成能有效提升音频深伪检测在真实扰动下的鲁棒性与泛化性。该思路提示后续研究可从固定检测器转向动态工具编排，对工业界构建可部署的深伪检测系统具有参考价值，但需更多可复现实验支撑。

## ⚠️ 局限与未解决问题

摘要未给出任何具体指标、数据集名称与基线数值，实验可信度难以评估；扰动智能体是否覆盖真实声学损坏（混响、编解码、压缩）不明确；缺少推理延迟与工具调用开销分析；对抗训练稳定性与收敛性未讨论；与现有集成/路由方法的对比不清晰。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-18/">← 返回 2026-09-18 速递</a></div>
