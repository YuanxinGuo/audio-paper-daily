---
title: "ChildVox: A Speech, Audio, and Large Audio-Language Model Benchmark in Understanding and Characterizing Sound across Childhood"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "ChildVox 整合 17 个儿童音频数据集、20+ 子任务，系统评测自监督、ASR 与大音频语言模型在儿童声学信号理解上的表现。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音质量评估</span> <span class="tag-pill tag-pill-soft">#基准测试</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.29257</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/tiantiaf0627/childvox-release" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">tiantiaf0627/childvox-release</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.29257" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.29257" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/tiantiaf0627/childvox-release" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ChildVox 整合 17 个儿童音频数据集、20+ 子任务，系统评测自监督、ASR 与大音频语言模型在儿童声学信号理解上的表现。
</div>

## 👥 作者与机构

**Tiantian Feng** ¹ · Anfeng Xu · Xuan Shi · Aditya Kommineni · Shakhrul Iman Siam · Megan Micheletti · Zhonghao Shi · Helen Tager-Flusberg · … 等 5 人

**机构**：南加州大学 · 波士顿大学 · 密歇根州立大学 · 加州大学洛杉矶分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做儿童语音、低资源 ASR、音频基础模型评测的研究者与产品团队。建议通读 §2 数据集构建与 §3 任务定义，重点看跨语料/跨域对比表与模型排行榜；若只关心 ASR，可先看语音识别与质量评估子任务的结果表，再回看生理声/非语言发声分类的消融。

## 🌍 研究背景

儿童语音识别与声学表征长期受数据稀缺、年龄跨度大、非语言发声与生理声混杂等问题困扰。此前 SOTA 多为成人语料上预训练的 wav2vec2 / Whisper / AST 等模型，直接迁移到儿童语音时 WER 显著升高，且缺乏统一评测协议。本文要解决的是：如何系统刻画从出生到学龄期的多样声学信号，并给出跨语料、跨领域的可复现基准。

## 💡 核心创新

1. 覆盖出生到学龄全发育轨迹的 20+ 子任务基准
2. 整合 17 个儿童中心音频/语音数据集做跨语料对比
3. 统一评测 SSL、ASR 与大音频语言模型三类基础模型
4. 开源基准模型与评测流程，支持语言水平刻画与年龄追踪

## 🏗️ 模型架构

ChildVox 本身是评测基准而非单一网络。输入为儿童音频波形或声学特征，按任务分为生理声分类、非语言发声与规范音节建模、语音质量评估与语音识别四类。评测对象包括自监督模型（如 wav2vec2 / HuBERT 类）、ASR 导向模型（Whisper 类）以及大音频语言模型（LALM）。各任务分别接分类头、CTC/注意力解码器或回归头，输出类别、转写或质量分数，并在统一数据划分下做跨语料比较。

## 📚 数据集

- 17 个儿童中心音频与语音数据集（训练/评测，覆盖生理声、非语言发声、规范音节、口语）
- 公开数据集上的基准模型（评估，已随代码发布）

## 📊 实验结果

摘要未给出具体指标数值，仅说明基准在生理声分类、发声与规范音节建模、语音质量评估与识别等任务上提供了高性能模型套件，并支持刻画儿童语言水平与追踪随年龄变化的语音产出。具体 WER、准确率、MOS 等数值需查阅原文表格。

## 🎯 结论与影响

ChildVox 是目前覆盖儿童发育全阶段、任务最全的儿童音频/语音基准之一，为跨语料比较提供了统一协议。其最强结论是：现有基础模型经适配后可在多类儿童声学任务上达到可用性能。后续研究可基于该基准做儿童专用预训练与年龄条件建模，工业上可用于儿童语言发展筛查与教育类语音产品评测。

## ⚠️ 局限与未解决问题

作为基准论文，方法创新有限，主要是数据集整合与评测协议；摘要未报告推理延迟、参数量与统计显著性检验，跨语料划分是否严格说话人独立也未说明。部分子任务数据量可能不均衡，存在年龄与语料偏差风险，且未与最新儿童专用 ASR 系统做全面对比。

## 🔗 开源资源

- **代码**：<https://github.com/tiantiaf0627/childvox-release>

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-08/">← 返回 2026-10-08 速递</a></div>
