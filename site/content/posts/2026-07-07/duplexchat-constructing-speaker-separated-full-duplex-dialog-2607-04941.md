---
title: "DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出DuplexChat语料库及构建流水线，从播客生成双通道全双工对话语音，用于口语对话语言模型训练。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#语料库构建</span> <span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.04941</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.04941" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.04941" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DuplexChat语料库及构建流水线，从播客生成双通道全双工对话语音，用于口语对话语言模型训练。
</div>

## 👥 作者与机构

**Wataru Nakata** ¹ · Yuki Saito · Hiroshi Saruwatari

**机构**：东京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事口语对话建模、语音分离及数据增强的研究者。建议重点阅读§3流水线设计及§4语料库分析，了解数据构建细节与统计特性。

## 🌍 研究背景

全双工口语对话模型需要每个说话人独立音频流训练，但现有大规模公开语音语料多为单声道，不适用于SDLM训练。传统方法依赖人工录制或合成数据，规模有限且缺乏自然对话动态。本文旨在从公开播客源自动构建大规模、说话人分离的全双工对话语音语料库。

## 💡 核心创新

1. 提出DuplexChat-Pipe流水线，集成播客过滤、语音分离与后处理
2. 构建282k小时英语和132k小时日语的双通道对话语料
3. 验证语料包含自然对话中的话轮转换动态

## 🏗️ 模型架构

DuplexChat-Pipe流水线：输入播客RSS源 → 语言过滤（英语/日语）→ 下载并清理音频 → 说话人日志提取双说话人片段 → 语音分离（使用预训练模型）→ 语音修复（降噪、去混响）→ 输出每说话人单通道音频。分离模型采用基于神经网络的掩蔽方法，修复模块包括噪声抑制和混响去除。

## 📚 数据集

- DuplexChat（英语282,634小时，日语132,723小时，训练/评估）

## 📊 实验结果

摘要未提供具体分离或下游任务指标，但通过分析语料库统计特性（如话轮长度、重叠比例）验证了其包含自然对话动态。未报告语音分离或下游SDLM的定量结果。

## 🎯 结论与影响

DuplexChat提供了首个大规模开源全双工对话语音语料库，填补了SDLM训练数据的空白。其流水线可扩展至其他语言，有望推动全双工口语对话模型的发展。工业上可用于构建更自然的语音助手。

## ⚠️ 局限与未解决问题

未报告语音分离的客观指标（如SI-SDR），也未验证语料在下游SDLM任务上的效果。依赖播客数据，可能存在领域偏差。未讨论分离错误对下游模型的影响。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
