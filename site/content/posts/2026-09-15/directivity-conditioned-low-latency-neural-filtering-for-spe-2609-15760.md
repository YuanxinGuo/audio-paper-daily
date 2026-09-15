---
title: "Directivity-Conditioned Low-Latency Neural Filtering for Speech Enhancement in Hearing Aids"
date: 2026-09-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "面向助听器的10ms低延迟DNN，用FiLM在推理时调节指向性模式，并设计保持跨通道频谱关系的损失函数。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#助听器</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.15760</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.15760" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.15760" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向助听器的10ms低延迟DNN，用FiLM在推理时调节指向性模式，并设计保持跨通道频谱关系的损失函数。
</div>

## 👥 作者与机构

**Lennart Uphaus** ¹ · Andr\'e Merboldt · Markus Hofbauer · Timo Gerkmann

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做助听器/低延迟语音增强与指向性滤波的研究者与工程团队阅读。建议通读，重点看 §3 的 FiLM 调制机制与所提跨通道频谱一致性损失，以及表 2 中与放宽延迟约束方法的对比；若关注落地，再核对延迟与算力开销的实测细节。

## 🌍 研究背景

神经指向性滤波近期可在推理阶段自适应调整指向性图的方向与形状，代表性工作多基于 FiLM 调制。但既有方法普遍忽略助听器真实约束：场景高度动态、麦克风位置随头径与佩戴方式变化、存在头影效应，且延迟预算极严（通常 10 ms 量级）。本文针对这些被忽视的约束，提出低延迟网络并保持指向性图可控。

## 💡 核心创新

1. 10 ms 低延迟 DNN 指向性滤波框架
2. FiLM 在推理阶段调制指向性图方向与形状
3. 保持跨通道频谱关系的损失函数
4. 显式建模头径/佩戴变化与头影效应

## 🏗️ 模型架构

输入为多麦克风含噪语音特征，主干为低延迟 DNN（摘要未给出具体网络名与参数量），通过 FiLM 层在推理阶段注入指向性控制条件以调节指向性图的方向与形状。训练时除增强损失外，加入一项维持跨通道频谱关系的损失，防止调制破坏目标指向性模式。输出为增强后的单通道/参考通道语音，整体算法延迟约 10 ms。

## 📊 实验结果

摘要未给出具体指标数值与数据集名称，仅声称在 10 ms 低延迟约束下可达到与放宽延迟约束方法相近的结果，说明低延迟并未带来明显性能损失。缺少 SI-SDR、PESQ 等量化对比与消融细节，需查阅正文确认。

## 🎯 结论与影响

最强结论是：在 10 ms 严格延迟下仍能取得与放宽延迟方法相当的指向性滤波增强效果。这为助听器场景的低延迟神经指向性滤波提供了可行路径，后续研究可围绕更动态场景与个性化头影建模展开；工业上对助听器芯片的实时部署有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告具体指标、数据集与消融，无法判断跨头径/佩戴变化的泛化性；未给出推理延迟与算力实测、模型参数量；与放宽延迟基线的对比缺少统计显著性；头影效应建模是否充分仍需验证。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-15/">← 返回 2026-09-15 速递</a></div>
