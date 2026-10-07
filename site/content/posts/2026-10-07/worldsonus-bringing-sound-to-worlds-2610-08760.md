---
title: "WorldSonus: Bringing Sound to Worlds"
date: 2026-10-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "面向世界模型的交互式视频到音频框架，用流式因果自回归扩散实现低延迟立体声合成，支持流中提示控制。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音频</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#实时生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.08760</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://noizai.github.io/WorldSonus/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">noizai.github.io/WorldSonus/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.08760" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.08760" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://noizai.github.io/WorldSonus/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向世界模型的交互式视频到音频框架，用流式因果自回归扩散实现低延迟立体声合成，支持流中提示控制。
</div>

## 👥 作者与机构

**Pengjun Fang** ¹ · Jingyi Fa · Kam Man Wu · Jiaming Wang · Haoyuan Huang · Yaguang Wu · Xiangjun Huang · Ziyang Ma · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视频到音频生成、世界模型多模态补全、实时扩散推理的研究者与工程团队。建议通读，重点看 §3 的流式因果自回归扩散设计与 chunk-indexed prompt scheduling 机制，以及立体声监督数据构造部分；实验表关注 RTF 与空间对齐指标的权衡。

## 🌍 研究背景

世界模型已能生成较逼真的视频，但生成环境基本无声。现有视频到音频（V2A）方法多为双向非因果模型，需完整视频输入，无法跟上交互式视频流；同时缺乏对生成中声音事件的动态控制，且多数只输出单声道，难以反映场景几何与相机运动。本文要解决实时性、交互可控性、空间立体声对齐三个具体问题。

## 💡 核心创新

1. 流式因果自回归扩散架构，分块合成音频，RTF 低至 0.41
2. 以音频为中心的 captioning 流水线 + chunk-indexed prompt scheduling 实现流中控制
3. 从立体声与 ambisonic 数据整理高质量立体声监督，提升空间对齐

## 🏗️ 模型架构

输入为交互式视频流，经视觉编码后作为条件；主干为流式因果自回归扩散模型，按 chunk 逐块生成音频潜变量，保证因果性与低延迟。音频侧引入以音频为中心的 captioning 流水线，将文本提示按 chunk 索引调度，实现生成过程中的动态声音事件操控。空间对齐依赖从立体声与 ambisonic 数据整理的高质量立体声监督训练。输出为与视频流同步的立体声波形。摘要未给出参数量。

## 📚 数据集

- 立体声与 ambisonic 整理数据（训练，用于空间对齐监督）
- 开放域视频到音频基准（评估，验证泛化性）

## 📊 实验结果

摘要仅给出实时因子 RTF=0.41，未列出 SI-SDR、PESQ、FD 等具体数值。作者称在开放域 V2A 基准上，声学质量与空间对齐可匹配或超过当前双向 SOTA 模型，但缺少可核对的量化对比与消融细节。

## 🎯 结论与影响

最强结论是流式因果自回归扩散可在 RTF 0.41 下生成空间对齐的交互式视频音轨，并泛化到开放域 V2A 任务。若成立，将推动世界模型从无声走向可交互有声环境，对游戏、VR、具身仿真等实时音效生成落地有直接意义。

## ⚠️ 局限与未解决问题

摘要未报告任何客观指标数值，缺少与双向 SOTA 的量化对比表；立体声监督数据来源与规模未说明，可能存在数据 bias；未给出推理延迟、显存占用与长视频稳定性分析；交互控制的用户研究或主观 MOS 缺失。

## 🔗 开源资源

- **项目主页**：<https://noizai.github.io/WorldSonus/>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-07/">← 返回 2026-10-07 速递</a></div>
