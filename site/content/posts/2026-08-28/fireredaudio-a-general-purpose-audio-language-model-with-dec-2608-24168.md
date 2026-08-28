---
title: "FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解与生成"]
summary: "FireRedAudio 提出解耦连续表示，用共享 9B LLM 统一音频理解与生成，支持 ASR、长音频理解、零样本 TTS 和语音编辑。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解与生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#音频理解</span> <span class="tag-pill tag-pill-soft">#语音编辑</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.24168</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/FireRedTeam/FireRedAudio" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">FireRedTeam/FireRedAudio</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.24168" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.24168" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/FireRedTeam/FireRedAudio" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>FireRedAudio 提出解耦连续表示，用共享 9B LLM 统一音频理解与生成，支持 ASR、长音频理解、零样本 TTS 和语音编辑。
</div>

## 👥 作者与机构

**Feiyu Shen** ¹ · Fenglong Xie · Junjie Li · Kun Xie · Lei Xie · Xu Tang · Xuelong Geng · Yan Jia · … 等 8 人

**机构**：阿里巴巴 · 浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频多模态、语音合成与理解方向的研究者。建议重点阅读第 3 节模型架构和第 4 节渐进式多任务训练，以及第 5 节实验对比。可先看摘要中的架构图和表 1 以快速把握整体。

## 🌍 研究背景

统一音频模型需同时处理理解与生成，但两者对表示要求不同：理解需紧凑特征以支持长上下文，生成需可重构特征保留细节。现有模型多采用离散表示或单一连续表示，难以兼顾。FireRedAudio 提出解耦连续输入表示，分别用于理解和生成，在单一自回归 LLM 中实现统一。

## 💡 核心创新

1. 解耦连续输入表示：理解用 Audio Encoder，生成用 RedAE 路径
2. 共享 9B 参数 LLM 直接生成文本或条件 flow-matching DiT
3. 渐进式多任务训练策略，支持 ASR、长音频理解、TTS 和编辑
4. 长音频结构化组织实现秒级时间戳精度

## 🏗️ 模型架构

输入音频分两路：理解路径用 Audio Encoder 提取紧凑特征，生成路径用 RedAE 编码连续声学特征。共享 9B 参数 LLM 作为主干，理解时输出文本，生成时输出条件给 flow-matching DiT，DiT 生成连续声学潜变量，再经 RedAE 解码为波形。支持 ASR、音频理解（长达 1 小时）、零样本 TTS、指令 TTS 和语义/声学编辑。

## 📚 数据集

- 多语种 ASR 数据集（训练，未具体说明）
- 音频理解数据集（训练，含长音频）
- TTS 数据集（训练，用于零样本和指令 TTS）
- 语音编辑数据集（训练，用于语义和声学编辑）

## 📊 实验结果

摘要未给出具体数值，但声称在音频理解和多语种 ASR 上达到竞争或领先性能，零样本 TTS 在内容准确性和说话人保持上表现强，指令 TTS 指令跟随领先，语音编辑相比 Ming-UniAudio-Edit 有显著提升。

## 🎯 结论与影响

FireRedAudio 验证了解耦连续输入表示在统一音频理解与生成中的可行性，以中等规模模型实现多任务领先性能。对后续研究提供了新架构思路，有望推动音频基础模型发展，并可能简化工业部署中的多模型集成。

## ⚠️ 局限与未解决问题

摘要未提及具体局限，但可能包括：未报告推理延迟和计算成本，长音频理解可能受限于上下文长度，语音编辑的客观指标未给出，对比基线有限。

## 🔗 开源资源

- **代码**：<https://github.com/FireRedTeam/FireRedAudio>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-08-28/">← 返回 2026-08-28 速递</a></div>
