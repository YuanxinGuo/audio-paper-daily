---
title: "Tap2Listen: Instant Target Switching for Streaming Audio-Visual Speaker Extraction"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出流式音视频目标说话人提取模型 Tap2Listen，将目标无关音频编码与目标相关视觉条件解耦，实现 0.12ms 目标切换与首帧满质量输出。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#音视频语音分离</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#实时系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.36643</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.36643" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.36643" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出流式音视频目标说话人提取模型 Tap2Listen，将目标无关音频编码与目标相关视觉条件解耦，实现 0.12ms 目标切换与首帧满质量输出。
</div>

## 👥 作者与机构

**Hansol Park** ¹ · Minkyung Song · Zinu Kim · Yujun Lee · Hoseong Ahn · Hyunjin Choi · Kyuhong Shim

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 AV-TSE、流式语音分离与实时部署的研究者与工程师阅读。建议通读，重点看 §3 的模态分离架构（音频编码器 / 视觉条件解码器）与切换延迟分析，以及表 2 的 SI-SNRi 对比和切换恢复曲线；工程侧关注单核 CPU 实时性数据。

## 🌍 研究背景

流式 AV-TSE 已有工作（如基于 AV-Conformer、DPRNN 的因果模型）通常在整个片段内固定目标说话人，用视觉线索持续调制整条分离网络。真实对话中目标频繁切换，这类系统在切换后需重新积累上下文，恢复期约 1 秒，且切换需重跑整网。本文要解决的是：如何在流式条件下让目标切换即时生效、且不损失分离质量。

## 💡 核心创新

1. 目标无关音频编码器与目标相关视觉条件解码器解耦
2. 切换仅需 0.12ms 视觉重投影，首帧即满质量
3. 编码器预测损失 + 解码器监督提取损失的分组件训练策略
4. 单 CPU 核实时流式推理

## 🏗️ 模型架构

输入为混合语音波形与目标说话人面部帧。目标无关音频编码器仅处理混合音频，输出与说话人无关的中间表示；目标相关分支将所选人脸经视觉前端编码后，仅作为条件注入解码器（类似 FiLM 式调制），解码器据此重建目标语音。切换目标时只需对新脸做一次重投影（0.12ms），无需重跑音频编码器。训练采用分组件损失：编码器用预测损失，解码器用监督提取损失。摘要未给出具体参数量，仅称与基线参数量相当。

## 📚 数据集

- LRS3-2mix（评估，标准测试集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SNRi | LRS3-2mix | 基线流式 AV-TSE 8.85 dB | **9.68 dB** | +0.83 dB |

在 LRS3-2mix 测试集上，参数量相当条件下 SI-SNRi 由 8.85 提升至 9.68 dB。切换评估显示：切换到已知人脸后本文模型首帧即输出满质量，基线需约 1 秒恢复。模型可在单个 CPU 核上实时运行。摘要未给出消融细节与更多指标（如 PESQ、WER）。

## 🎯 结论与影响

最强结论是模态解耦使目标切换近乎零成本且首帧满质量，同时 SI-SNRi 优于同规模基线。这为流式 AV-TSE 的交互式场景（多人对话、助听设备）提供了可行范式，后续研究可沿“目标无关编码 + 轻量条件注入”思路扩展。工业上单核 CPU 实时性利于端侧部署。

## ⚠️ 局限与未解决问题

仅报告 SI-SNRi，缺 PESQ、WER 等感知与识别指标；切换恢复仅对比一个基线，未与多种流式方案比较；未说明视觉前端在遮挡、侧脸下的鲁棒性；分组件损失的消融细节与推理延迟分解未在摘要中给出。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
