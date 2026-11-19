---
title: "Harmonic Circuit: Chord Progression Lies in a Sparse Principal Information Flow in Symbolic Music Models"
date: 2026-11-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "用 Auto-Emergence 算法在 ChatMusician 与 MuPT 两个符号音乐模型中提取稀疏子网络，发现其对应 I…V→I 终止主音预测的音乐功能电路。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可解释性</span> <span class="tag-pill tag-pill-soft">#符号音乐</span> <span class="tag-pill tag-pill-soft">#电路发现</span> <span class="tag-pill tag-pill-soft">#稀疏子网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.24453</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-demo" href="https://ukiyo23rui.github.io/auto-emergence-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">ukiyo23rui.github.io/auto-emergence-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.24453" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.24453" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-demo" href="https://ukiyo23rui.github.io/auto-emergence-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用 Auto-Emergence 算法在 ChatMusician 与 MuPT 两个符号音乐模型中提取稀疏子网络，发现其对应 I…V→I 终止主音预测的音乐功能电路。
</div>

## 👥 作者与机构

**Ruiji Yu** ¹ · Gus Xia

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐生成可解释性、机制可解释性（MI）与符号音乐建模的研究者阅读。值得通读，重点看 §3 的 Auto-Emergence 提取流程与 §4 的因果干预验证实验；若只关心音乐生成质量可略读。建议先看因果干预的表与 demo 页音频样例，再回看电路稀疏度设定。

## 🌍 研究背景

机制可解释性（MI）在 NLP 中已通过电路发现（circuit discovery）解析 Transformer 内部计算，但音乐模型内部的可解释电路几乎空白。此前符号音乐生成（如 ChatMusician、MuPT）只关注生成质量与和弦遵循度，缺乏对和声功能如何被内部表征的机制级分析。本文要解决的具体问题是：在符号音乐生成模型中是否存在可被稀疏子网络刻画的和声进行（I…V→I）功能电路，并用因果干预证明其为主驱动。

## 💡 核心创新

1. 首次将 circuit discovery 系统引入音乐模型
2. 用 Auto-Emergence 提取稀疏主信息流子网络
3. 以 I…V→I 终止主音预测作为音乐功能探针
4. 因果干预验证电路为和声行为主驱动

## 🏗️ 模型架构

输入为符号音乐 token 序列（和弦/音符事件），主干为 ChatMusician 与 MuPT 两个自回归符号音乐生成模型（Transformer 类）。方法侧不训练新网络，而是对已训练模型做电路发现：以 I…V→I 终止主音预测为任务，用 Auto-Emergence 算法在注意力头/MLP 子模块构成的計算图上迭代搜索，得到稀疏主信息流子网络作为候选电路；再通过因果干预（激活替换/消融）验证该子网络对目标预测的因果贡献。摘要未给出参数量。

## 📚 数据集

- 符号音乐和弦进行数据（训练/评估模型与电路发现，具体规模摘要未给出）

## 📊 实验结果

摘要未给出具体量化指标（如电路稀疏度、干预后主音预测准确率下降幅度、与随机子网络对比的数值），仅以因果干预定性说明所提取电路是模型和声进行行为的主要驱动。缺少与随机子网络/稠密网络的定量对照表，实验细节需查阅正文。

## 🎯 结论与影响

最强结论是：符号音乐生成模型内部存在可被稀疏子网络刻画的、对应 I…V→I 和声功能的电路，且因果干预证明其为主驱动。这为音乐模型可解释性提供了首个系统性电路发现范式，后续可用于可控生成、模型编辑与和声约束注入；工业上或有助于诊断生成模型的和声错误来源。

## ⚠️ 局限与未解决问题

仅覆盖两个符号音乐模型与单一和声模式（I…V→I），泛化性未知；摘要未报告电路稀疏度、干预强度与定量对比，缺少与随机子网络的统计显著性检验；未涉及音频域模型，对语音/音频 5 大重点方向无直接贡献。

## 🔗 开源资源

- **Demo / 试听**：<https://ukiyo23rui.github.io/auto-emergence-demo/>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-19/">← 返回 2026-11-19 速递</a></div>
