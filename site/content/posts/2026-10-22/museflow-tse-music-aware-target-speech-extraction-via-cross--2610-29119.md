---
title: "MuseFlow-TSE: Music-Aware Target Speech Extraction via Cross-Source Band-Splitting and Data-to-Data Flow Matching"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出判别式删除+生成式插入两阶段框架，在含音乐场景下用跨源频带分割与数据到数据流匹配精修目标说话人。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#音乐感知</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29119</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29119" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29119" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出判别式删除+生成式插入两阶段框架，在含音乐场景下用跨源频带分割与数据到数据流匹配精修目标说话人。
</div>

## 👥 作者与机构

**Lu Ma** ¹ · Yongliang Wang · Zhewen Su · Xin Tian

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TSE、音乐混叠语音分离与生成式语音增强的研究者。建议通读，重点看 §3 的两阶段设计与 Stage-1 的守恒/音乐泄漏约束、Stage-2 的负条件流匹配，以及表 2 中 1–4 步自适应 Euler 的步数-质量权衡；若只关心工程落地，可先看 Stage-1 单独结果与推理步数开销。

## 🌍 研究背景

TSE 在给定注册语音条件下从混合中提取目标说话人，现有工作几乎都在无音乐数据上验证。判别式方法（如基于掩码的 BSRNN/Conformer 提取器）内容忠实但受掩码上界限制，音乐能量易残留；生成式方法（扩散/流匹配）自然度更好，却可能幻觉、说话人身份漂移且需多步采样。本文针对含音乐场景，试图兼顾内容保真与生成自然度，并控制采样步数。

## 💡 核心创新

1. Stage-1 跨源频带分割提取器，同时估计目标、干扰说话人、音乐与噪声四类源
2. 引入守恒约束与音乐泄漏约束，抑制音乐残留到目标估计
3. Stage-2 数据到数据流匹配精修器，以判别式估计为初始化而非纯噪声
4. 以干扰源为负条件，并用 1–4 步难度自适应 Euler 采样
5. 端到端保真度目标联合训练两阶段

## 🏗️ 模型架构

输入为混合语音的复数谱（频带分割后的子带特征）与注册说话人嵌入。Stage-1 为音乐感知跨源频带分割提取器，按子带建模并输出目标语音、干扰说话人、音乐、噪声四路估计，训练时施加源间守恒与音乐泄漏约束。Stage-2 为数据到数据流匹配精修器：以 Stage-1 判别式估计作为流匹配起点，条件包含注册嵌入与 Stage-1 各源估计，并对干扰源做负条件，用难度自适应 Euler 积分 1–4 步输出最终目标语音，整体以端到端保真度目标优化。摘要未给出参数量。

## 📚 数据集

- 含音乐混合的 TSE 评测集（评估，摘要未具名）
- 注册语音条件下的目标说话人数据（训练，摘要未具名）

## 📊 实验结果

摘要未给出任何具体指标数值、数据集名称或与基线的定量对比，仅定性声称 Stage-1 在守恒与音乐泄漏约束下给出内容忠实的初始估计，Stage-2 以 1–4 步自适应 Euler 提升自然度并缓解幻觉与身份漂移。定量结论需查阅正文实验部分。

## 🎯 结论与影响

最强结论是将 TSE 从无音乐设定推进到含音乐场景，并用“判别式删除+生成式插入”的两阶段设计在保真与自然度间取得折中。若定量结果成立，将推动音乐混叠下的 TSE 与少步流匹配精修研究；工业上对音乐背景下的会议/直播人声提取有直接价值，且 1–4 步采样利于低延迟部署。

## ⚠️ 局限与未解决问题

摘要未报告任何定量结果、参数量与推理延迟，难以判断相对强基线（如 BSRNN、SEPFormer 类 TSE 系统）的实际增益；含音乐 TSE 数据集的构建方式与规模未说明，存在数据偏置风险；两阶段联合训练与负条件设计的消融是否充分未知；难度自适应步数选择机制缺乏细节。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
