---
title: "Sona: Personalized Soundscape Mediation to Support People with Sound Sensitivity"
date: 2026-09-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "Sona 是一个移动端个性化声景调节系统，可实时选择性衰减用户指定的多种重叠声音，并支持免重训练的自定义目标添加。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#个性化音频</span> <span class="tag-pill tag-pill-soft">#声音敏感性</span> <span class="tag-pill tag-pill-soft">#目标声音抑制</span> <span class="tag-pill tag-pill-soft">#人机交互</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.00447</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.00447" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.00447" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Sona 是一个移动端个性化声景调节系统，可实时选择性衰减用户指定的多种重叠声音，并支持免重训练的自定义目标添加。
</div>

## 👥 作者与机构

**Jeremy Zhengqi Huang** ¹ · Emani Hicks · Sidharth · Gillian R. Hayes · Dhruv Jain

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合 HCI 与辅助技术方向研究者阅读，尤其是关注声音敏感人群与个性化音频交互的读者。建议重点看系统设计与在-situ 评估部分（§3 与用户研究章节），了解免重训练目标添加机制与用户反馈。若关注信号处理细节，本文技术深度有限，可略读。

## 🌍 研究背景

声音敏感人群（PWSS）目前主要依赖耳塞与降噪耳机，这类方案会无差别抑制整个声景，导致有用听觉线索（如谈话、警报）一并丢失。已有的选择性声音抑制研究多针对单一声音类别，缺乏对多重叠声音、可调强度与个性化目标的实时支持。本文旨在构建一个移动端系统，让用户能实时选择并调节需要衰减的声音目标，同时保留其余声景。

## 💡 核心创新

1. 支持多重叠用户选定声音的实时选择性衰减，强度可调
2. 基于环境声音识别自动建议衰减目标
3. 用户可通过短录音添加自定义目标，无需重训练模型

## 🏗️ 模型架构

Sona 为移动端系统，输入为设备麦克风采集的实时环境音频。系统先进行环境声音识别以生成候选衰减目标，用户选定后对多个重叠目标声音按可调强度进行选择性衰减，输出为处理后的残余声景。自定义目标通过短录音注册，无需模型重训练。摘要未披露具体网络结构、参数量或信号处理算法细节。

## 📊 实验结果

摘要未给出 SI-SDR、PESQ 等客观指标或定量对比。作者对 10 名 PWSS 进行了 in-situ 评估，参与者报告 Sona 使声景更易管理。研究还发现不同声音类型与语境下衰减效果不均、管理滤波器与参与当前活动之间存在张力、个性化结果难以解读等问题。

## 🎯 结论与影响

Sona 表明个性化实时声景调节可帮助声音敏感人群更好地管理环境声音，同时保留有用听觉线索。其最强结论是选择性衰减比全局降噪更符合 PWSS 需求。该工作提示后续研究应关注残余声景质量、用户控制与交互负担的平衡，以及可解释的个性化。对工业落地而言，为助听器、耳机与移动音频应用提供了个性化声景调节的设计方向。

## ⚠️ 局限与未解决问题

摘要未报告客观声学指标、推理延迟或与降噪基线的定量对比，评估仅 10 名参与者，样本量小。系统对不同声音类型的衰减不均，个性化结果可解释性差。作为 HCI 系统论文，信号处理细节与可复现性信息不足，缺少消融与跨场景泛化验证。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：5.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-24/">← 返回 2026-09-24 速递</a></div>
