---
title: "TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection"
date: 2026-09-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频诈骗检测"]
summary: "构建可月度冻结更新的电信诈骗音频基准，用近域负样本暴露分类器捷径与预测崩溃问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频诈骗检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分类</span> <span class="tag-pill tag-pill-soft">#基准数据集</span> <span class="tag-pill tag-pill-soft">#数据生成</span> <span class="tag-pill tag-pill-soft">#ASR+LLM</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.18748</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://anonymous.4open.science/r/TeleAntiFraud-2_0-EEB2/" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">anonymous.4open.science/r/TeleAntiFraud-2_0-E…</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.18748" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.18748" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://anonymous.4open.science/r/TeleAntiFraud-2_0-EEB2/" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建可月度冻结更新的电信诈骗音频基准，用近域负样本暴露分类器捷径与预测崩溃问题。
</div>

## 👥 作者与机构

**Huiyuan Liu** ¹ · Zhiming Ma · Yanxing Liu · Shun Zhang · Qifan Wang · Di Liu · Yifan Wang · Yuyang Deng · … 等 6 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音反诈、音频分类基准与数据合成的研究者。建议通读，重点看 §3 的 Mixed-Tree 生成管线与月度冻结协议，以及近域负样本实验（表 2/3）。可执行动作：先看近域 vs 普通负样本的 Macro-F1 对比，再核对冻结清单与 provenance 记录设计。

## 🌍 研究背景

电信诈骗话术演化快且刻意模仿正常客服对话，现有音频反诈评测多依赖话题分离的负样本，模型易学到类别先验而非真实判别能力。此前基准多为静态、一次性发布，无法纳入新骗术又不覆盖旧测试集。本文要解决两个问题：基准需可增量刷新且不覆盖历史测试集；负样本需为近域合法通话，以检验模型在真实易混条件下的鲁棒性。

## 💡 核心创新

1. Mixed-Tree 反诈生成管线，从案件摘要生成 profile-grounded 场景
2. 共享上下文下同时生成诈骗与非诈骗对话路径
3. 月度冻结评测协议，固定音频/标签/prompt/manifest/provenance
4. 引入近域兄弟负样本，暴露分类器类别先验捷径

## 🏗️ 模型架构

输入为在线诈骗案件摘要文本，经 Mixed-Tree Anti-Fraud Generation Pipeline 转为 profile-grounded 场景，再以混合树扩展生成诈骗与非诈骗对话路径，共享同一上下文；验证后的对话经角色匹配 TTS 渲染为语音。每个冻结集含 900 通中文电话（600 诈骗 / 300 近域非诈骗），冻结音频、标签、prompt、manifest 与 provenance。评测侧使用文本分类器与 ASR+LLM 流水线，未涉及特定声学主干网络。

## 📚 数据集

- TeleAntiFraud 2.0（自建，每月冻结 900 通中文电话，600 诈骗 / 300 近域非诈骗，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Macro-F1 | TeleAntiFraud 2.0 文本对照 | 无关/普通负样本 1.00 | **近域兄弟负样本 0.65-0.68** | -0.32~-0.35 |

受控文本实验显示，三个分类器在无关或普通负样本上达到完美 Macro-F1（1.00），但换成近域兄弟负样本后降至 0.65-0.68。全量音频与 ASR+LLM 评测进一步暴露类别先验捷径、预测崩溃与快照敏感性问题。摘要未给出音频端具体指标数值与消融细节。

## 🎯 结论与影响

最强结论是：近域构造与 collapse-aware 报告应成为音频反诈评测的核心要求，否则高分可能来自类别先验而非真实判别。该工作为可刷新、可追溯的反诈基准提供了协议模板，后续研究可据此设计更鲁棒的判别模型。工业落地意味着反诈系统上线前需用近域负样本与月度冻结集做回归测试。

## ⚠️ 局限与未解决问题

仅中文电话、单一 TTS 渲染，声学多样性有限；未报告推理延迟与模型规模；音频端具体指标与消融不充分；近域负样本构造依赖生成管线，可能引入自身偏差；匿名仓库链接不利于长期可复现。

## 🔗 开源资源

- **代码**：<https://anonymous.4open.science/r/TeleAntiFraud-2_0-EEB2/>
- **数据集**：<https://anonymous.4open.science/r/TeleAntiFraud-2_0-EEB2/>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-18/">← 返回 2026-09-18 速递</a></div>
