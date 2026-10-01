---
title: "Improving Predicted MOS Scores, Not Perceived Quality: Multi-Predictor Test-Time Optimization of Enhanced Speech"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "首次系统分析语音增强的测试时MOS优化：多预测器分数被抬高，但MUSHRA主观听感无改善。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#评测方法</span> <span class="tag-pill tag-pill-soft">#MOS预测</span> <span class="tag-pill tag-pill-soft">#对抗性优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.39028</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.39028" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.39028" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次系统分析语音增强的测试时MOS优化：多预测器分数被抬高，但MUSHRA主观听感无改善。
</div>

## 👥 作者与机构

**Tsubasa Ochiai** ¹ · Marc Delcroix · Nahomi Kusunoki · Rintaro Ikeshita · Naohiro Tawara · Naoyuki Kamo · Tetsuji Ogawa · Shoko Araki

**机构**：日本电信电话公司（NTT）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强评测、MOS预测器、Challenge组织的读者。建议通读，重点看多预测器平均优化的目标函数定义、七套URGENT 2026系统的实验设置，以及MUSHRA听测与预测分数脱节的对比分析。若只关心建模方法可略读。

## 🌍 研究背景

非侵入式MOS预测器（如DNSMOS、UTMOS）已广泛替代主观听测来评估和排序语音增强系统，学界默认其分数与感知质量正相关。然而这一假设缺乏严格验证：若直接对增强信号做测试时优化以抬高预测分数，是否真能提升听感？此前无人系统研究该问题，本文针对URGENT 2026挑战的七套SE系统，考察多预测器分数优化对客观指标与主观听感的影响。

## 💡 核心创新

1. 首次系统分析SE任务的测试时MOS优化
2. 多MOS预测器平均分数作为优化目标
3. 揭示优化分数上升但MUSHRA听感无改善
4. 指出未参与优化的预测器分数不上升

## 🏗️ 模型架构

方法不涉及新的增强网络，而是对已有SE系统输出的增强波形做测试时优化：以多个非侵入式MOS预测器（如DNSMOS、UTMOS类）分数的平均值为目标函数，直接迭代修改增强信号本身（波形域或特征域扰动），使预测分数最大化。实验在URGENT 2026挑战的七套系统上进行，对比优化前后参考型指标（如SI-SDR、PESQ）与未参与优化的MOS预测器分数，并组织MUSHRA主观听测验证感知质量变化。

## 📚 数据集

- URGENT 2026挑战七套SE系统输出（评估）
- MUSHRA主观听测（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 多预测器平均MOS | URGENT 2026七系统 | 优化前原始分数 | **优化后分数上升** | 上升（摘要未给具体值） |
| 参考型指标（如SI-SDR/PESQ） | URGENT 2026七系统 | 优化前 | **基本不变** | ≈0 |
| 未优化MOS预测器分数 | URGENT 2026七系统 | 优化前 | **不上升** | ≈0 |
| MUSHRA主观质量 | 听测 | 优化前 | **无改善** | ≈0 |

摘要未给出具体数值，仅报告趋势：在七套URGENT 2026系统上，优化后所有被优化的预测分数均上升，参考型指标几乎不变，未参与优化的预测器分数不上升，MUSHRA听测显示感知质量无提升。说明优化仅针对特定预测器，未迁移到真实听感或其他预测器，缺乏消融与效率数据。

## 🎯 结论与影响

最强结论是：抬高MOS预测分数不等于提升感知质量，测试时优化会扭曲SE系统评测。该发现提示用于优化的预测器不应再用于评估，挑战赛应隐藏排序所用预测器。对工业界意味着不能以MOS预测器分数作为唯一优化目标，否则可能过拟合评测指标而损害真实用户体验。

## ⚠️ 局限与未解决问题

仅覆盖URGENT 2026的七套系统，预测器种类与优化强度未充分消融；未报告优化计算开销与推理延迟；MUSHRA听测规模与统计显著性未在摘要说明；未讨论防御或检测该优化的方法。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
