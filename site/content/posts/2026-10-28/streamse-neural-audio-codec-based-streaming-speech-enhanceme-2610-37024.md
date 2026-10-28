---
title: "StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "在冻结神经音频编解码器的连续潜空间做逐帧回归，实现20M参数、无前瞻、单次前向的流式语音增强，可在手机单核实时运行。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#神经音频编解码器</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#端侧部署</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.37024</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.37024" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.37024" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在冻结神经音频编解码器的连续潜空间做逐帧回归，实现20M参数、无前瞻、单次前向的流式语音增强，可在手机单核实时运行。
</div>

## 👥 作者与机构

**Hyunjin Choi** ¹ · Zinu Kim · Junwon Moon · Jeongyun Chae · Seungbeom Kim · Kyuhong Shim

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做端侧/流式语音增强与生成式模型落地的工程与研究读者。值得通读：重点看 §3 的潜空间回归与 RVQ 截断设计、以及实时性与主观听感对比表；若关注部署，先看手机 CPU 单核实测与延迟分解部分。

## 🌍 研究背景

生成式语音增强（如基于扩散/流匹配的方法）在 PESQ、MOS 等感知指标上已明显优于传统掩蔽式方法，但普遍依赖非因果处理、多步迭代采样与较大算力，难以满足流式与端侧约束。此前 SOTA 多为离线生成模型，推理需前瞻与多次前向。本文要解决的是：在完全因果、单次前向、低参数量条件下，如何保留生成式增强的感知质量。

## 💡 核心创新

1. 在冻结神经音频编解码器连续潜空间做逐帧干净潜变量回归
2. 以自回归方式条件于前帧预测，无需迭代采样与前瞻
3. 截断 RVQ 至粗粒度层，token 数减半并提升混响鲁棒性
4. 20M 参数全流程在手机单 CPU 核实时运行

## 🏗️ 模型架构

输入含噪语音先经冻结的预训练神经音频编解码器编码器得到连续潜表示；主干为因果流式网络，逐帧接收含噪连续潜，并以上一帧自身预测的干净潜作为条件，直接回归当前帧干净连续潜；输出潜经解码器重建增强语音。关键设计是截断 codec 的 RVQ 至粗粒度层，使每帧 token 数减半，降低序列建模负担并增强对混响的鲁棒性。整体约 20M 参数，每帧仅一次前向，无迭代采样、无 look-ahead。

## 📚 数据集

- DNS-Challenge 类含噪语音数据（训练/评估，摘要未明确）

## 📊 实验结果

摘要未给出具体指标数值，仅定性说明：StreamSE 是对比中唯一的流式生成模型，其感知质量（主观听感）达到或超过离线生成式基线；完整流程在单颗智能手机 CPU 核上实时运行。RVQ 截断被报告可减半每帧 token 并提升混响鲁棒性，但缺少量化消融数据。

## 🎯 结论与影响

最强结论是连续潜空间回归可在完全因果、端侧流式约束下实现生成式级感知质量。这为生成式语音增强的实时落地提供了可行路线，可能推动后续研究从迭代采样转向潜空间直接回归，并对耳机、助听与通话降噪等端侧产品有直接意义。

## ⚠️ 局限与未解决问题

摘要未报告 PESQ/SI-SDR 等客观指标与具体数据集，主观评测细节不明；缺少 RVQ 截断层数的消融与延迟/功耗分解；对比基线未列全，且未说明与轻量非生成式流式方法的差距；混响鲁棒性提升缺乏量化证据。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-28/">← 返回 2026-10-28 速递</a></div>
