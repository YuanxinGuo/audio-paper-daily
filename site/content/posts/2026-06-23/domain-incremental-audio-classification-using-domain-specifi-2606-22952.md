---
title: "Domain-incremental audio classification using domain-specific experts and prototype classifier"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频分类"]
summary: "针对DCASE 2026域增量音频分类任务，提出冻结专家特征+原型分类器方案，在开发集上达78.15%微平均/77.03%宏平均准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#域增量学习</span> <span class="tag-pill tag-pill-soft">#原型分类器</span> <span class="tag-pill tag-pill-soft">#生成式回放</span> <span class="tag-pill tag-pill-soft">#DCASE挑战赛</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22952</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22952" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22952" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对DCASE 2026域增量音频分类任务，提出冻结专家特征+原型分类器方案，在开发集上达78.15%微平均/77.03%宏平均准确率。
</div>

## 👥 作者与机构

**Jongyeon Park** ¹ · Do-Hyeon Lim · Sang-won Park · Hong Kook Kim · Kyungdeuk Ko · Hyeongcheol Geum · Jeong Eun Lim

**机构**：光州科学技术院 · 韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究增量学习或音频分类的读者。建议重点阅读§3.2原型分类器设计和§3.3跨阶段回归插补器。可先看表1了解整体性能。

## 🌍 研究背景

域增量学习（DIL）要求模型在不访问过去或未来域数据的情况下持续学习新域，面临灾难性遗忘问题。DCASE 2026挑战赛Task 7聚焦于此。现有方法多依赖存储原始音频或复杂重放机制，存在隐私或存储开销。本文提出将DIL视为冻结特征重放问题，通过训练域特定专家并固定，再基于缓存特征训练原型分类器，避免遗忘。

## 💡 核心创新

1. 冻结专家特征+原型分类器框架
2. DeepInversion生成式回放保留早期知识
3. 跨阶段回归插补器填充缺失专家特征
4. 多专家交叉堆叠集成提升性能

## 🏗️ 模型架构

输入音频特征 → 多个域特定专家（每个专家为紧凑网络，在对应增量阶段训练后冻结）→ 拼接所有专家的倒数第二层特征 → 跨阶段回归插补器（填充早期阶段不存在的专家特征槽）→ 轻量级每类原型分类器（基于缓存特征训练）→ 输出类别概率。提交了四个系统：三个基于不同五专家骨干，一个交叉堆叠集成。

## 📚 数据集

- DCASE 2026 Task 7开发集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 微平均准确率 | DCASE 2026 Task 7开发集 | 最佳单骨干系统（未明确数值） | **78.15%** | 优于所有单骨干 |
| 宏平均准确率 | DCASE 2026 Task 7开发集 | 最佳单骨干系统（未明确数值） | **77.03%** | 优于所有单骨干 |

交叉堆叠集成系统在开发集上达到78.15%微平均和77.03%宏平均准确率，优于所有单个骨干系统。未提供与外部基线（如经典DIL方法）的对比，也未报告测试集结果。消融实验缺失，无法评估各组件贡献。

## 🎯 结论与影响

本文提出的冻结专家特征+原型分类器框架有效解决了域增量音频分类中的灾难性遗忘问题，在DCASE 2026开发集上取得有竞争力结果。该方法无需存储原始音频，具有隐私友好和低存储优势。对工业场景中持续学习系统有参考价值，但需在更多数据集上验证泛化性。

## ⚠️ 局限与未解决问题

仅报告开发集结果，无测试集或外部基线对比；未进行消融实验，无法量化各组件（如生成式回放、插补器）的贡献；专家数量固定为五，未探讨不同专家数的影响；缺乏与经典DIL方法（如EWC、iCaRL）的比较。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
