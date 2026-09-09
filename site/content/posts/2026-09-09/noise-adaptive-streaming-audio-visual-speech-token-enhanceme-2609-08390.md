---
title: "Noise Adaptive Streaming Audio-Visual Speech Token Enhancement for Robust Full-Duplex Spoken Dialogue Models"
date: 2026-09-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出模块化流式音视频前端AV-STE，在噪声和重叠语音下恢复语义语音token，冻结下游对话模型，提升响应连贯性。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#音视频融合</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#对话系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.08390</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.08390" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.08390" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出模块化流式音视频前端AV-STE，在噪声和重叠语音下恢复语义语音token，冻结下游对话模型，提升响应连贯性。
</div>

## 👥 作者与机构

**Bella Godiva** ¹ · Yeonju Kim · Yong Man Ro

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、多模态对话系统研究者。值得通读，重点看方法部分（AV-STE架构）和实验部分（表1、表2）。可先看§3.2和表2了解核心设计。

## 🌍 研究背景

全双工对话系统需同时听和说，但纯音频感知在噪声和重叠语音下易失败。现有音视频对话方法通过微调大型语音对话模型以融合视觉信息，成本高且可能损害预训练能力。本文提出模块化前端AV-STE，在语音token进入LLM前进行增强，保持对话模型冻结，解决鲁棒性和训练成本问题。

## 💡 核心创新

1. 模块化前端设计，冻结下游对话模型，避免多模态训练成本
2. 流式音视频融合，利用唇部运动辅助语音token增强
3. 噪声自适应机制，根据噪声水平动态调整融合权重
4. 在真实对话场景下验证，提升响应连贯性并保持轮转行为
5. 跨域泛化到Seamless Interaction，显示通用性

## 🏗️ 模型架构

AV-STE作为前端，输入为带噪音频和同步唇部视频。音频经编码器提取语义token，视频经视觉编码器提取唇部特征。通过跨模态注意力融合，并采用噪声自适应门控机制调整融合强度。增强后的token流式输入冻结的语音LLM（如Moshi）进行对话生成。

## 📊 实验结果

摘要未提供具体指标数值，仅提及在相同数据集干扰下，GPT-4o评估的响应连贯性从1.42提升至1.91，且保持轮转行为，并泛化到Seamless Interaction。

## 🎯 结论与影响

AV-STE通过模块化前端增强语音token，显著提升全双工对话系统在噪声下的鲁棒性，且无需微调对话模型。该工作为多模态对话系统提供轻量级增强方案，可能推动实际部署。

## ⚠️ 局限与未解决问题

摘要未提及计算开销、延迟等效率指标；实验仅评估了单一干扰场景，缺乏多种噪声类型和信噪比分析；未与端到端多模态训练方法进行对比；未报告主观MOS或客观语音质量指标。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-09/">← 返回 2026-09-09 速递</a></div>
