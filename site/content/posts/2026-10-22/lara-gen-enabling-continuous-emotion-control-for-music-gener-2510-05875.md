---
title: "LARA-Gen: Enabling Continuous Emotion Control for Music Generation Models via Latent Affective Representation Alignment"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "通过潜空间情感表征对齐，为文本到音乐生成模型加入连续 valence-arousal 情感控制，并建立情感可控性评测基准。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#情感控制</span> <span class="tag-pill tag-pill-soft">#表征对齐</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.05875</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://anonymous2232330.github.io/laragen-web/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">anonymous2232330.github.io/laragen-web/</span></span></a><a class="oc-chip oc-chip-demo" href="https://anonymous2232330.github.io/laragen-web/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">anonymous2232330.github.io/laragen-web/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.05875" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.05875" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://anonymous2232330.github.io/laragen-web/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://anonymous2232330.github.io/laragen-web/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>通过潜空间情感表征对齐，为文本到音乐生成模型加入连续 valence-arousal 情感控制，并建立情感可控性评测基准。
</div>

## 👥 作者与机构

**Jiahao Mei** ¹ · Shimeng Li · Xuenan Xu · Leyuan Jin · Yixuan Yuan · Zeyu Xie · Zihao Zheng · Ye Tao · … 等 2 人

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控音乐生成、情感计算与生成模型表征对齐的研究者阅读。建议通读，重点看 §3 的 LARA 对齐损失设计与情感控制模块如何与文本条件解耦，以及 §4 基准构建与 Emotion Predictor 的可靠性验证；表 2/3 的情感贴合度与音乐质量对比是核心证据。

## 🌍 研究背景

文本到音乐生成（MusicGen、AudioLDM 等）已能生成结构连贯的音乐，但情感控制仍依赖文本提示中的形容词，粒度粗、难以连续调节，且情感词与内容描述纠缠。已有工作多通过 prompt engineering 或离散情感标签实现，缺乏连续 valence-arousal 空间上的细粒度控制，也缺少客观评测情感可控性的基准。本文要解决的是：如何在潜空间层面把情感属性从文本内容中解耦，实现连续、可量化的情感控制。

## 💡 核心创新

1. LARA：将生成模型隐状态与音乐理解模型表征对齐
2. 基于连续 valence-arousal 空间的情感控制模块
3. 情感属性与文本内容解耦，绕开文本提示瓶颈
4. 构建含 Emotion Predictor 的情感可控性评测基准

## 🏗️ 模型架构

输入为文本提示与目标 valence-arousal 连续向量；主干沿用预训练文本到音乐生成模型（摘要未指明具体骨干），在生成网络的隐状态上引入 LARA 模块，通过投影层将内部 hidden states 与外部音乐理解模型的情感表征做对齐约束，使潜空间具备情感语义结构。情感控制模块将连续 VA 向量编码后注入生成过程，与文本条件分支解耦。输出为生成音频，训练时联合生成损失与表征对齐损失。摘要未给出参数量。

## 📚 数据集

- 自建情感标注测试集（评估，规模摘要未给出）
- 文本到音乐生成训练数据（训练，摘要未指明具体数据集）

## 📊 实验结果

摘要仅声称在情感贴合度与音乐质量两方面显著优于基线，并给出试听页面，但未披露具体指标数值、基线名称与测试集规模，无法量化比较。基准部分包含精心筛选的测试集与一个 Emotion Predictor 用于客观评测，其可靠性验证细节需查阅正文。

## 🎯 结论与影响

最强结论是潜空间情感表征对齐可在不牺牲音乐质量的前提下实现连续情感控制。该思路对可控生成与情感计算交叉方向有参考价值，表征对齐范式或可迁移到其他条件生成任务。工业上可用于配乐、情绪化 BGM 生成等需要细粒度情绪调节的场景。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果与基线细节，难以判断提升幅度；Emotion Predictor 作为评测核心，其自身偏差会直接影响结论可信度；连续 VA 控制与文本条件的解耦是否彻底缺少消融证据；推理开销与生成质量的主观评测（MOS）未提及。

## 🔗 开源资源

- **项目主页**：<https://anonymous2232330.github.io/laragen-web/>
- **Demo / 试听**：<https://anonymous2232330.github.io/laragen-web/>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
