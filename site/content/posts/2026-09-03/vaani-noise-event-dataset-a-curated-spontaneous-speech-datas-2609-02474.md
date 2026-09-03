---
title: "VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#噪声事件检测"]
summary: "VAANI噪声事件数据集为105种印度语言的野外自发语音提供细粒度时间戳噪声标注，支持噪声鲁棒ASR、SED和语音增强研究。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#噪声事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#自动语音识别</span> <span class="tag-pill tag-pill-soft">#声音事件检测</span> <span class="tag-pill tag-pill-soft">#多语言语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.02474</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.02474" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.02474" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>VAANI噪声事件数据集为105种印度语言的野外自发语音提供细粒度时间戳噪声标注，支持噪声鲁棒ASR、SED和语音增强研究。
</div>

## 👥 作者与机构

**Pavan Kumar J** ¹ · Agneedh Basu · Pranav Bhat · Sujith Pulikodan · Suryansh Shukla · Nihar Desai Prasanta K. Ghosh

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强、ASR鲁棒性、声音事件检测研究者阅读。建议重点看第3节（数据集构建与标注协议）和第4节（与现有数据集的对比分析）。若关注多语言场景，可先看第2节（VAANI项目背景）。

## 🌍 研究背景

现有公共声音事件语料库多针对通用音频标记或干净语音分离，缺乏在真实自发语音上叠加的带时间戳噪声标注。合成混合语料（如WHAM!）无法捕捉真实场景中语音与噪声的同时性和重叠性。VAANI数据集填补了这一空白，提供105种印度语言、165个地区的真实野外录音，并带有细粒度噪声事件标注，支持噪声鲁棒ASR、SED和语音增强等任务。

## 💡 核心创新

1. 真实场景中语音与噪声同时采集，非合成混合
2. 细粒度开始/结束时间戳标注重叠噪声事件
3. 七类语义噪声分类法（动物、交通、婴儿/儿童等）
4. 覆盖105种印度语言，跨165个地区，多语言多样性
5. 与九个现有语料库的全面对比分析

## 🏗️ 模型架构

该论文不提出模型架构，而是介绍数据集构建流程。数据来源于Project VAANI的野外录音，包含自发语音和环境噪声。标注流程包括：音频分割、噪声事件检测、时间戳标注、七类语义分类。质量控制程序确保标注一致性。数据集提供音频文件和对应的JSON标注文件。

## 📚 数据集

- VAANI Noise Event Dataset（训练/评估，105种语言，165个地区）
- WHAM!（对比）
- AVA-Speech（对比）
- MUSAN（对比）

## 📊 实验结果

摘要未提供具体实验数值，但论文将VAANI与WHAM!、AVA-Speech、MUSAN、FSD50K、CHiME-6、AudioSet、DESED、iNoise和Kathbath-Noisy等九个语料库进行对比，强调VAANI在真实场景、多语言覆盖和重叠噪声标注方面的独特性。

## 🎯 结论与影响

VAANI数据集为噪声鲁棒语音处理提供了宝贵的真实世界资源，其多语言、真实声学环境和细粒度标注特性有望推动ASR、SED和语音增强在印度等低资源多语言场景的研究。该数据集可作为训练和评估基准，促进跨语言泛化研究。

## ⚠️ 局限与未解决问题

摘要未提及标注规模（如总时长、事件数量），也未提供基线实验验证数据集效用。作为数据集论文，缺乏下游任务（如ASR增强）的基准测试，可能限制其直接可用性。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-03/">← 返回 2026-09-03 速递</a></div>
