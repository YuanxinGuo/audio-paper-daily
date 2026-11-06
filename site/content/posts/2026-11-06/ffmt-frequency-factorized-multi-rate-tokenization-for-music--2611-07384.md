---
title: "FFMT: Frequency-Factorized Multi-Rate Tokenization for Music-to-Dance Generation"
date: 2026-11-06T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "将舞蹈运动按频率分解为低频编排骨架与高频细节残差，用非对称码本与token率做离散化，并据此设计先规划后细化的自回归生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐驱动舞蹈生成</span> <span class="tag-pill tag-pill-soft">#运动离散表征</span> <span class="tag-pill tag-pill-soft">#多速率Tokenization</span> <span class="tag-pill tag-pill-soft">#自回归生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.07384</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-06</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.07384" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.07384" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将舞蹈运动按频率分解为低频编排骨架与高频细节残差，用非对称码本与token率做离散化，并据此设计先规划后细化的自回归生成。
</div>

## 👥 作者与机构

**Qirong Guo** ¹ · Ruijie Li · Zeyan Li · Sicheng Shu · Guanzhi Ding · Weihang Ding

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐驱动动作生成、运动离散表征（VQ tokenizer）的研究者阅读。值得通读，重点看 §3 的频率分解 tokenizer 设计与非对称码本/token率配置，以及 §4 的 plan-then-articulate 自回归分解和消融表。若只关心音频侧方法可略读。

## 🌍 研究背景

音乐驱动舞蹈生成此前主流做法是把整段运动用单一 VQ-VAE 离散化为等速率 token 序列，再由自回归或扩散模型在音乐条件下生成。这类统一表征忽略了舞蹈运动本身的多尺度特性：躯干编排变化缓慢，而四肢局部动作变化快，单一 token 率与码本容量难以同时兼顾粗粒度结构与细粒度细节，导致生成动作要么僵硬要么抖动。本文要解决的是如何用显式时频分解来分别配置时间分辨率与码本容量，并让生成过程与这种分解对齐。

## 💡 核心创新

1. 按频率将根相对运动分解为低频编排骨架与高频残差两支
2. 低频用小码本低token率、高频用大码本高token率的非对称配置
3. 由表征诱导 plan-then-articulate 两阶段自回归分解
4. 高频token以低频plan与音乐为条件做低到高条件生成

## 🏗️ 模型架构

输入为根节点相对的运动序列，先经频率分解得到低频编排分量与高频残差分量。两支分别送入各自的 VQ 编码器做离散化：低频支采用较低 token 率与较小码本，高频支采用较高 token 率与较大码本，形成非对称多速率离散表征。生成阶段采用自回归模型，先根据音乐条件生成低频 token 序列作为粗粒度编排 plan，再以该 plan 与音乐为条件生成高频 token 实现局部动作细化，最后解码回连续运动。摘要未给出参数量。

## 📚 数据集

- AIST++（训练与评估，音乐-舞蹈配对数据）
- FineDance（训练与评估，细粒度舞蹈数据）

## 📊 实验结果

摘要仅定性说明在 AIST++ 与 FineDance 上取得较强的分布保真度，同时保持合理的多样性与音乐-动作同步性，未给出 FID、多样性、Beat Alignment 等具体数值。消融实验一致支持频率分解、非对称时间分配以及低到高条件三项设计，但缺少量化表格与推理效率报告。

## 🎯 结论与影响

最强结论是：显式时频分解可同时决定运动离散表征的时间分辨率与码本容量，并自然导出先规划后细化的生成范式。这为运动 tokenizer 设计提供了新视角，可能影响后续音乐驱动动作生成与通用运动离散化研究；工业上对虚拟人、舞蹈动画生成的可控性有潜在价值。

## ⚠️ 局限与未解决问题

摘要未报告 FID、多样性、Beat Alignment 等定量指标，也无与强基线（如 Bailando、FineDance 相关方法）的数值对比；缺少推理延迟与 token 序列长度开销分析；频率分解的截止频率与两支码本大小如何选取未见敏感性分析；仅在两个舞蹈数据集验证，泛化性未知。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-06/">← 返回 2026-11-06 速递</a></div>
