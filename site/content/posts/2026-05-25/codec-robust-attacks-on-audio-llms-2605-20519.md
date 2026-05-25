---
title: "Codec-Robust Attacks on Audio LLMs"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对抗攻击"]
summary: "提出CodecAttack，在神经音频编解码器潜空间优化扰动，实现对抗音频大模型的高成功率攻击，且对多种有损压缩鲁棒。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对抗攻击</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大模型</span> <span class="tag-pill tag-pill-soft">#对抗鲁棒性</span> <span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#语音安全</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.20519</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.20519" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.20519" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CodecAttack，在神经音频编解码器潜空间优化扰动，实现对抗音频大模型的高成功率攻击，且对多种有损压缩鲁棒。
</div>

## 👥 作者与机构

**Jaechul Roh** ¹ · Jean-Philippe Monteuuis · Jonathan Petit · Amir Houmansadr

**机构**：马萨诸塞大学阿默斯特分校 · 安波福

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、对抗机器学习研究者。建议通读，重点看§3攻击方法、§4.2-4.3实验结果与§5能量分析。可复现其开源代码验证攻击效果。

## 🌍 研究背景

现有针对音频大模型的对抗攻击通过在波形域添加扰动实现，但实际部署中常采用有损编解码压缩作为预处理防御，可有效去除波形扰动。然而，尚无攻击能同时绕过多种编解码压缩。本文旨在设计一种对编解码压缩鲁棒的对抗攻击方法，揭示有损压缩作为防御的不可靠性。

## 💡 核心创新

1. 在神经音频编解码器连续潜空间优化扰动
2. 利用编解码器自身压缩通道传递潜空间扰动
3. 多比特率直通期望变换（EoT）增强鲁棒性
4. 无需修改目标模型即可跨编解码器迁移
5. 揭示潜空间扰动集中在4kHz以下低频区域

## 🏗️ 模型架构

攻击流程：输入音频 → 编码器（如EnCodec）提取连续潜变量 → 在潜空间添加优化扰动 → 解码器重构音频 → 输入目标Audio LLM。扰动优化采用多比特率直通EoT，模拟不同压缩条件。不修改目标模型参数。

## 📚 数据集

- LibriSpeech（用于生成对抗样本的语音数据）
- Common Voice（用于生成对抗样本的语音数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 目标子串攻击成功率（ASR） | 三个部署场景（含Opus压缩） | 波形基线（EoT增强）26% | **CodecAttack 85.5%** | +59.5% |
| ASR | MP3（未见编解码器） | 波形基线（未报告） | **100%** | N/A |
| ASR | AAC-LC（未见编解码器） | 波形基线（未报告） | **84%** | N/A |

CodecAttack在Opus中等码率下平均ASR达85.5%，而波形基线仅26%。攻击可迁移至未见编解码器，MP3达100%，AAC-LC达84%。能量分析表明潜空间扰动集中在4kHz以下，与编解码器比特分配一致，而波形基线扰动扩散至高频被丢弃。

## 🎯 结论与影响

本文证明有损压缩不是对抗音频的可靠防御，CodecAttack在多种编解码器下保持高成功率，对部署的音频大模型构成实际威胁。后续研究需开发更鲁棒的防御机制，如基于潜空间检测或自适应压缩。工业界应警惕此类攻击对语音助手等应用的影响。

## ⚠️ 局限与未解决问题

未评估对更复杂音频大模型（如多模态）的攻击效果；未考虑自适应防御（如对抗训练）；攻击计算开销未报告；仅测试英语语音数据，泛化性待验证。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
