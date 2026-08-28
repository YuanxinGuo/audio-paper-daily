---
title: "Decay-Region Group Delay as a Forensic Cue for AI-Generated Impulsive Sounds"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频取证"]
summary: "本文发现AI生成的脉冲声音在衰减区域的群延迟分布与真实声音存在可测量差异，可作为取证线索，但跨生成器泛化性有限。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频取证</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#AI生成音频检测</span> <span class="tag-pill tag-pill-soft">#群延迟</span> <span class="tag-pill tag-pill-soft">#脉冲声音</span> <span class="tag-pill tag-pill-soft">#音频取证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.26346</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.26346" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.26346" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文发现AI生成的脉冲声音在衰减区域的群延迟分布与真实声音存在可测量差异，可作为取证线索，但跨生成器泛化性有限。
</div>

## 👥 作者与机构

**JaeHyeong Chang** ¹ · Chengzhe Sun · Siwei Lyu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频取证、AI生成内容检测方向的研究者阅读。建议重点看第3节（群延迟特征分析）和第4节（分类实验），可先看摘要中的关键数字（AUC 0.884）。若关注泛化性，可看生成器留出实验部分。

## 🌍 研究背景

随着AI生成音频的普及，检测合成声音成为重要课题。现有方法多基于幅度谱特征，对脉冲声音（如打击乐、枪声）的检测效果有限。群延迟作为相位信息的表示，在语音处理中已有应用，但尚未用于AI生成音频取证。本文旨在探索群延迟在区分真实与AI生成脉冲声音中的有效性，并评估其作为补充特征的潜力。

## 💡 核心创新

1. 首次将群延迟分析用于AI生成脉冲声音检测
2. 发现衰减区域群延迟差异显著，而起始区域差异小
3. 提出基于衰减区域群延迟的随机森林分类器，AUC达0.884
4. 群延迟图作为CNN输入达到90-94%准确率
5. 系统分析了STFT参数对特征稳定性的影响

## 🏗️ 模型架构

输入为脉冲声音的短时傅里叶变换（STFT），计算群延迟（GD）图。提取衰减区域的多维特征（如KL散度、跨频带变异性等），共9个特征，输入随机森林（RF）分类器。同时，将群延迟图作为2D输入，用于CNN和Transformer（AST）分类器。

## 📊 实验结果

摘要中报告了关键指标：衰减区域KL散度0.322 vs 起始区域0.022；单特征AUC 0.720；RF在样本分离评估下AUC 0.884；CNN分类器准确率90-94%；生成器留出实验中RF平均准确率66.7%，平均AUC 0.731，低于CNN（0.762）和AST（0.772），但避免了极端崩溃。参数敏感性分析显示RF AUC稳定在0.700-0.847。

## 🎯 结论与影响

本文证明衰减区域群延迟可作为AI生成脉冲声音的物理可解释取证线索，补充幅度基分类器。尽管跨生成器泛化性有限，但群延迟特征在样本分离下表现稳定，为音频取证提供了新方向。未来需在更多生成器和真实场景中验证，并探索与幅度特征的融合。

## ⚠️ 局限与未解决问题

摘要未提及数据集规模和来源，可能缺乏多样性；未与现有最先进的检测方法（如基于幅度谱的CNN）进行直接对比；生成器留出实验中性能波动大，泛化性不足；未报告推理延迟和计算开销；未提供消融实验证明各特征贡献。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-08-28/">← 返回 2026-08-28 速递</a></div>
