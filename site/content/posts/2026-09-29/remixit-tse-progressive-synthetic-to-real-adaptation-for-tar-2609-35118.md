---
title: "RemixIT-TSE: Progressive Synthetic-to-Real Adaptation for Target Speech Extraction via Target-Aware Supervision and Remixing"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "将 RemixIT 从语音增强扩展到目标说话人提取，用两阶段渐进式合成到真实域适应，在 REAL-TSE 挑战赛上显著提升。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.3</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#域适应</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.35118</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/YuWang-Speech/RemixIT-TSE" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">YuWang-Speech/RemixIT-TSE</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.35118" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.35118" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/YuWang-Speech/RemixIT-TSE" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将 RemixIT 从语音增强扩展到目标说话人提取，用两阶段渐进式合成到真实域适应，在 REAL-TSE 挑战赛上显著提升。
</div>

## 👥 作者与机构

**Yu Wang** ¹ · Haixin Guan · Shuang Wei · Yanhua Long

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TSE、域适应、半监督语音增强的研究者与工程团队阅读。建议重点看 §3 两阶段微调框架与目标感知监督设计，以及表 2 的消融实验。若关注落地，可先看 EVAL-2 上的 TER 与说话人相似度结果，再回看第一阶段弱监督约束的实现细节。

## 🌍 研究背景

真实对话场景下的目标说话人提取因合成训练数据与复杂声学环境之间的域差距而性能严重下降，且真实数据通常缺乏信号级 ground truth。此前 TSE 主流方法依赖模拟混合数据训练，如基于 Conformer/DPRNN 的提取网络，在真实场景泛化差。RemixIT 在语音增强中已验证可利用真实无标签数据自训练，但尚未扩展到 TSE。本文要解决的是：如何在无信号级标注的真实数据上，渐进地把合成域模型适应到真实域。

## 💡 核心创新

1. 首次将 RemixIT 从语音增强扩展到 TSE，提出两阶段渐进式合成到真实域适应框架
2. 第一阶段用区域级说话人相似度与静音约束做目标感知弱监督联合优化
3. 第二阶段用质量过滤的教师伪目标提供 SI-SNR 信号级监督训练学生

## 🏗️ 模型架构

输入为混合语音与目标说话人线索（如 enrollment embedding）。主干为 TSE 提取网络，输出目标说话人估计。第一阶段在目标感知适应框架下，对合成数据与真实弱监督数据联合优化，损失包含区域级说话人相似度与静音约束，保留合成域能力同时注入真实特性。第二阶段仅用真实数据，教师模型生成伪目标，经质量过滤后以 SI-SNR loss 监督学生模型，实现 RemixIT-TSE 自训练。摘要未给出具体参数量与网络名。

## 📚 数据集

- SLT 2026 REAL-TSE Challenge EVAL-2（真实对话评估集，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| TER | EVAL-2 | 源域基线 | **相对降低 6.53%** | -6.53% |
| Speaker Similarity | EVAL-2 | 源域基线 | **相对提升 21.84%** | +21.84% |
| DNSMOS-P808 | EVAL-2 | 源域基线 | **相对提升 9.89%** | +9.89% |
| Target-activity F1 | EVAL-2 | 源域基线 | **相对提升 4.10%** | +4.10% |

在 SLT 2026 REAL-TSE Challenge 的 EVAL-2 真实对话评估集上，相比源域基线，TER 相对降低 6.53%，说话人相似度相对提升 21.84%，DNSMOS-P808 相对提升 9.89%，目标活动 F1 相对提升 4.10%。摘要未提供消融实验、推理效率或跨数据集泛化结果，也未给出各阶段单独贡献的量化分析。

## 🎯 结论与影响

本文最强结论是：通过两阶段渐进式合成到真实域适应，可在无信号级真实标注下显著提升真实场景 TSE 性能。该工作为 TSE 域适应提供了可复用的弱监督加自训练范式，后续研究可在此基础上探索更鲁棒的伪标签过滤与教师更新策略。工业落地方面，对缺乏真实标注的对话式 TSE 产品有直接参考价值。

## ⚠️ 局限与未解决问题

摘要仅报告相对提升，未给出绝对指标与基线具体数值；缺少消融实验验证两阶段各自贡献；未报告推理延迟与模型复杂度；仅在单一挑战赛评估集上验证，跨数据集泛化未知；伪标签质量过滤策略细节未在摘要中说明。

## 🔗 开源资源

- **代码**：<https://github.com/YuWang-Speech/RemixIT-TSE>

---

<div class="paper-footer"><span>评分：8.3</span><span>原始：7.3</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
