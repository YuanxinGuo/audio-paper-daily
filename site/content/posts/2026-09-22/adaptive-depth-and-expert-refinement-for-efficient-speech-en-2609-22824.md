---
title: "Adaptive Depth and Expert Refinement for Efficient Speech Enhancement"
date: 2026-09-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出 ADER，用自适应深度控制器与条件专家路由实现输入相关的渐进式语音增强，在 VCTK-DEMAND 上大幅削减参数量与计算量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#动态计算</span> <span class="tag-pill tag-pill-soft">#模型压缩</span> <span class="tag-pill tag-pill-soft">#条件计算</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.22824</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.22824" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.22824" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 ADER，用自适应深度控制器与条件专家路由实现输入相关的渐进式语音增强，在 VCTK-DEMAND 上大幅削减参数量与计算量。
</div>

## 👥 作者与机构

**Xikun Lu** ¹ · Yujian Ma · Yunda Chen · Xianquan Jiang · Jinqiu Sang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做高效语音增强、动态网络与条件计算的读者。建议通读，重点看 §3 中 ADC 的早退判据、CER 的专家选择机制与 EIS 的监督设计，以及表 2 的 PESQ 与计算量对比。可先看方法图与消融，再核对与 MP-SENet 的公平性设置。

## 🌍 研究背景

当前主流语音增强系统（如 MP-SENet、CMGAN 等基于 Conformer/Transformer 的生成式模型）对所有输入采用固定处理深度，简单噪声片段也被迫走完全部 refinement 迭代，造成推理算力浪费。已有动态深度工作多用于分类或 ASR，语音增强中如何在参数共享的渐进框架内做输入相关早退、并保证中间输出质量，仍缺少系统方案。本文针对该冗余计算问题提出 ADER。

## 💡 核心创新

1. Adaptive Depth Controller 实现硬早退，按输入决定迭代次数
2. Conditional Expert Router 每步选一个轻量残差适配器
3. Exit-aware Intermediate Supervision 直接优化候选中间输出
4. 参数共享的渐进增强框架，显著降低参数量与平均计算

## 🏗️ 模型架构

输入为含噪语音的幅度谱或波形特征，主干沿用 MP-SENet 式参数共享渐进增强结构，多次 refinement 迭代复用同一组权重。每次迭代前由 Adaptive Depth Controller 判断是否硬早退；若继续，Conditional Expert Router 从若干轻量残差适配器中选一个作用于当前特征。Exit-aware Intermediate Supervision 对每个候选退出点的中间输出施加监督，使早退输出可直接使用。输出为增强后的语音波形/谱。相比 MP-SENet 参数量减少 70.4%，平均计算减少 51.3%。

## 📚 数据集

- VCTK-DEMAND（训练与评估，语音增强标准集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WB-PESQ | VCTK-DEMAND | MP-SENet（摘要未给具体值） | **3.37** | 摘要未给基线具体值，无法计算 |
| 参数量 | VCTK-DEMAND | MP-SENet 100% | **减少 70.4%** | -70.4% |
| 平均计算量 | VCTK-DEMAND | MP-SENet 100% | **减少 51.3%** | -51.3% |

摘要仅报告 VCTK-DEMAND 上 WB-PESQ 3.37，以及相对 MP-SENet 参数量降 70.4%、平均计算降 51.3%。未给出 SI-SDR、PESQ 对比基线具体数值，也未提供消融、推理延迟或跨数据集泛化结果，实验信息偏少，需正文补充。

## 🎯 结论与影响

ADER 证明在语音增强中引入输入相关的自适应深度与专家路由，可在基本保持增强质量的同时大幅压缩参数与平均计算。该思路对高效生成式增强、动态推理调度有参考价值，工业上有利于在边缘设备按输入难度分配算力。

## ⚠️ 局限与未解决问题

摘要未报告与 MP-SENet 的 PESQ 直接对比数值，也未给出 SI-SDR、推理延迟、消融实验与跨数据集结果；早退阈值与专家数量等超参敏感性未知；仅在 VCTK-DEMAND 单一仿真集验证，真实噪声与混响场景泛化性存疑。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-22/">← 返回 2026-09-22 速递</a></div>
