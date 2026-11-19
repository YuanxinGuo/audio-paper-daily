---
title: "End-to-End Multi-Task Learning for Adjustable Joint Noise Reduction and Hearing Loss Compensation"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "用可微分听觉模型端到端训练单一DNN，同时输出NR与HLC两个TF掩码，可按指数独立调节并支持audiogram个性化。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#听力损失补偿</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#可微分听觉模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.20387</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.20387" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.20387" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用可微分听觉模型端到端训练单一DNN，同时输出NR与HLC两个TF掩码，可按指数独立调节并支持audiogram个性化。
</div>

## 👥 作者与机构

**Philippe Gonzalez** ¹ · Vera Margrethe Frederiksen · Torsten Dau · Tobias May

**机构**：丹麦技术大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合助听器算法、听觉模型与多任务学习方向的研究者与工程团队阅读。建议通读，重点看 §2 可微分听觉模型的设计与 §3 双掩码指数组合的推理调节机制，以及表 2/表 3 中与级联双 DNN 和传统验配公式的对比；消融部分关注单目标 vs 多目标训练的差异。

## 🌍 研究背景

助听器前端通常把语音增强（NR）与听力损失补偿（HLC）分开处理：NR 用 DNN 去噪，HLC 依赖传统验配公式或级联第二个 DNN。近期工作多用听觉模型仿真器构造可微目标，但仿真器本身不可微，只能两阶段训练，且难以按用户听力图个性化、NR 与 HLC 强度无法独立调节。本文要解决的是：用单一 DNN、单一可微目标端到端联合优化 NR 与 HLC，并支持推理时独立调节两者强度与听众个性化。

## 💡 核心创新

1. 提出本身可微的听觉模型，替代不可微仿真器实现端到端训练
2. 单 DNN 输出 NR 与 HLC 两个 TF 掩码，推理时各自指数化后组合
3. audiogram 作为 DNN 输入，实现免重训的听众个性化
4. 为 NR 与 HLC 分别定义独立训练目标做多任务联合优化

## 🏗️ 模型架构

输入为含噪语音的时频特征并拼接听力图（audiogram）条件向量，主干 DNN 预测两个时频掩码：NR 掩码与 HLC 掩码。训练时两掩码组合后经可微分听觉模型（含外周滤波、压缩与内毛细胞/听神经建模）得到可微损失，直接反传端到端优化。推理时对每个掩码取幂（指数 α 控制 NR 强度、β 控制 HLC 强度）后再相乘/组合，从而独立调节两任务强度，无需重训即可适配不同听力损失曲线。摘要未给出参数量。

## 📚 数据集

- 含噪语音与平坦/高频倾斜听力损失曲线组合的评估集（评估，覆盖多种 hearing-loss profile）

## 📊 实验结果

摘要仅给出定性结论：所提方法在客观指标上优于单目标联合优化，也优于分别训练 NR 与 HLC 的两个 DNN 级联，并在 HLC 客观指标上与传统助听器验配公式相当；同时验证了 NR 与 HLC 强度可独立调节。摘要未披露具体指标数值、测试集名称与参数量，故无法列出定量对比表。

## 🎯 结论与影响

最强结论是：一个可微听觉模型即可端到端训练单 DNN 同时完成 NR 与 HLC，并在宽范围听力损失曲线上支持个性化与独立调节。这为助听器联合优化提供了可微建模范式，可能推动后续工作放弃两阶段仿真器训练；工业上利于单模型部署与按用户听力图在线调节，降低重训成本。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟、参数量与模型复杂度，难以评估助听器实时可行性；缺少主观听感（如 HASPI/HASQI 之外的 MOS 类）验证；对比基线数量有限，未与更多 DNN 联合训练方案比较；听力损失曲线覆盖范围与噪声条件的泛化性需更充分消融。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-19/">← 返回 2026-11-19 速递</a></div>
