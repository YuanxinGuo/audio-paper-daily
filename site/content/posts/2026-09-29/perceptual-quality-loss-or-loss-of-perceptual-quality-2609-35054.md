---
title: "Perceptual Quality Loss or Loss of Perceptual Quality?"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "系统检验 PESQ 辅助损失对语音增强模型的影响，发现其虽提升 PESQ 分数，却降低主观听感偏好，并揭示 CSIG/CBAK/COVL 被 PESQ 主导。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#感知指标</span> <span class="tag-pill tag-pill-soft">#PESQ</span> <span class="tag-pill tag-pill-soft">#主观评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.35054</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.35054" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.35054" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统检验 PESQ 辅助损失对语音增强模型的影响，发现其虽提升 PESQ 分数，却降低主观听感偏好，并揭示 CSIG/CBAK/COVL 被 PESQ 主导。
</div>

## 👥 作者与机构

**Danilo de Oliveira** ¹ · Tal Peer · Maurício do V. M. da Costa · Timo Gerkmann

**机构**：不来梅大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强损失设计、感知指标研究与主观评测的研究者与工程团队阅读。建议通读，重点看主观听验设计与 CSIG/CBAK/COVL 相关性分析两节；若只关心结论，可先看摘要与结论表，再回看失配数据实验部分。

## 🌍 研究背景

语音增强领域长期以 PESQ 等感知指标作为优化目标与评价标准，许多工作将 PESQ 作为辅助损失以提升感知质量。然而 PESQ 与真实听感的相关性有限，且 CSIG、CBAK、COVL 等复合指标本身可能被 PESQ 主导。本文要回答：加入 PESQ 损失究竟改善还是损害感知质量，以及这些复合指标是否可靠。

## 💡 核心创新

1. 对比两种 PESQ 辅助损失训练的 SE 模型
2. 在失配数据上检验 PESQ 损失的泛化性
3. 形式化主观听验比较有无 PESQ 损失
4. 量化 PESQ 在 CSIG/CBAK/COVL 中的主导性

## 🏗️ 模型架构

论文并非提出新网络，而是以现有深度语音增强模型为对象，在训练损失中加入两类 PESQ 辅助项：一类为可微 PESQ 近似，另一类为基于 PESQ 的复合目标。模型输入为含噪语音的幅度谱或波形，主干沿用常规 SE 结构，输出增强语音。评估端使用标准客观指标套件与形式化主观听验，并分析 CSIG、CBAK、COVL 与 PESQ 的相关结构。

## 📚 数据集

- 标准语音增强测试集（评估，含匹配与失配条件）
- 主观听验所用语音样本（评估）

## 📊 实验结果

摘要未给出具体数值。数值评估显示，PESQ 优化模型在测试集上 PESQ 更高，但多数其他指标无显著变化，失配数据上 PESQ 甚至更差；主观听验中无 PESQ 损失模型在所有设置下更受偏好；CSIG、CBAK、COVL 均被 PESQ 主导。

## 🎯 结论与影响

最强结论是：优化 PESQ 并不等于提升听感，甚至可能损害主观质量。该工作提醒后续研究不要过度依赖 PESQ 与由其主导的复合指标，应建立更完整的评估流程。对工业落地而言，仅以 PESQ 选型或调参可能误导产品体验。

## ⚠️ 局限与未解决问题

论文未提出替代指标或新损失，主观听验规模与统计细节在摘要中未披露；失配条件定义较模糊，缺少推理延迟与模型规模对比；未覆盖更多感知指标如 SI-SDR、MOS 的联合分析。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
