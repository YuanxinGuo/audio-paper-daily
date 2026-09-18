---
title: "CoRELoop: Parameter-Efficient Controlled Recurrent Refinement for Audio Deepfake Detection"
date: 2026-09-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "在冻结的SSL音频深伪检测器上，用轻量循环精炼模块与低秩适配器迭代修正预测，跨域EER从4.85%降至3.74%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音伪造检测</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#循环精炼</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.19818</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.19818" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.19818" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在冻结的SSL音频深伪检测器上，用轻量循环精炼模块与低秩适配器迭代修正预测，跨域EER从4.85%降至3.74%。
</div>

## 👥 作者与机构

**Kunyu Feng** ¹ · Yuxiang Wang · Li Wang · Wan Lin · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频深伪检测、参数高效微调与循环/迭代推理的研究者阅读。建议通读，重点看 §3 中循环输入适配、状态更新控制与分类器对齐三个模块的设计，以及表 2 的 14 个跨域测试集结果和 halting head 的 pass 数-性能权衡分析。

## 🌍 研究背景

音频深伪检测在跨域、未见攻击上泛化差，而收集覆盖所有攻击类型的训练数据不现实。此前 SOTA 多基于 SSL 前端（如 WavLM、XLS-R）加后端分类器，靠大规模数据或数据增强提升泛化，但推理时只做一次前向，未利用迭代修正的潜力。直接复用编码器输出作为下一轮输入会因分布不匹配导致性能下降，本文要解决如何在不改原参数、不加数据的前提下让循环精炼真正有效。

## 💡 核心创新

1. 冻结 SSL 检测器上做循环精炼，仅训练轻量模块与 loop-specific LoRA
2. 适配循环输入到冻结编码器，缓解分布不匹配导致的退化
3. 受控状态更新 + 与冻结分类器对齐，保留首轮预测
4. 可选 halting head 按句自适应选择精炼深度

## 🏗️ 模型架构

输入为原始波形，经冻结的 24 层 SSL 编码器（约 598M 参数）提取表征，送入冻结分类器得到首轮预测。CoRELoop 在其上叠加轻量精炼模块：先将上一轮输出适配回冻结编码器的输入空间，再通过受控门控更新循环状态，最后用对齐模块使精炼输出与冻结分类器的决策边界一致。每个循环配独立的低秩适配器（LoRA）。可训练参数约 10M，占总参数 1.7%。可选 halting head 逐句预测所需 pass 数，输出最终检测分数。

## 📚 数据集

- 14 个跨域测试集（评估，具体名称摘要未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| pooled EER | 14 个跨域测试集 | 冻结 SSL 检测器首轮 4.85% | **3.74%（两轮）** | -1.11% |
| pooled EER | 14 个跨域测试集 | 固定两轮 3.74% | **3.73%（halting head，平均 1.18 pass）** | -0.01% |

摘要给出两轮精炼将 pooled EER 从 4.85% 降至 3.74%，可训练参数约 10M/598M。加入 halting head 后以平均 1.18 次前向达到 3.73%，说明多数样本只需一轮即可，精炼主要对困难样本生效。摘要未提供各测试集细分、消融实验、推理延迟与不同 SSL 前端的对比。

## 🎯 结论与影响

在完全冻结的 SSL 深伪检测器上，轻量循环精炼即可显著提升跨域泛化，且不牺牲首轮预测。这为参数高效、可插拔的检测器后处理提供了新思路，后续可探索将该循环机制迁移到其他音频分类任务。工业上意味着可用极低训练成本对已部署检测器做在线增强。

## ⚠️ 局限与未解决问题

摘要未给出 14 个测试集的具体构成与攻击类型分布，缺少与现有参数高效微调方法（如 LoRA、Adapter）的对比，也未报告推理延迟与显存开销。halting head 的训练目标与阈值选择未说明，平均 1.18 pass 的方差与最坏情况 pass 数未知。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-18/">← 返回 2026-09-18 速递</a></div>
