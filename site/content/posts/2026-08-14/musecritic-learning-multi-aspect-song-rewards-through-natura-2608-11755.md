---
title: "MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques"
date: 2026-08-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出MUSECRITIC，一种半标量奖励模型，通过生成自然语言审美评论作为中间表示来预测歌曲的连续奖励分数，显著提升评分准确率并有效用于歌曲生成的强化学习对齐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#奖励模型</span> <span class="tag-pill tag-pill-soft">#自然语言评论</span> <span class="tag-pill tag-pill-soft">#歌曲生成</span> <span class="tag-pill tag-pill-soft">#RLHF</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.11755</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/WuqnEl/MuseCritic" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">WuqnEl/MuseCritic</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.11755" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.11755" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/WuqnEl/MuseCritic" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MUSECRITIC，一种半标量奖励模型，通过生成自然语言审美评论作为中间表示来预测歌曲的连续奖励分数，显著提升评分准确率并有效用于歌曲生成的强化学习对齐。
</div>

## 👥 作者与机构

**Jiabao Zhuang** ¹ · Changhao Jiang · Hanchen Wang · Jiahao Chen · Zhixiong Yang · Zhenghao Xiang · Yifei Cao · Jiajun Sun · … 等 6 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音乐生成、音频质量评估、RLHF对齐的研究者。建议重点阅读第3节方法部分（两阶段训练流程）和第4节实验部分（表1、表2及GRPO优化结果）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

长格式歌曲生成模型在时长、结构完整性和声学复杂度上不断进步，但可靠的审美奖励对于对齐人类偏好至关重要。现有奖励模型通常单次前向预测分数，缺乏可解释性，且针对完整歌曲的奖励模型有限。本文旨在解决奖励模型缺乏可解释性和评分误差大的问题，通过引入自然语言评论作为中间表示，提高评分准确性和可解释性。

## 💡 核心创新

1. 提出半标量奖励模型，生成自然语言评论作为中间表示预测分数
2. 两阶段训练：教师模型监督微调，再自生成评论进行奖励学习，缓解分布偏移
3. 覆盖五个审美维度，提供可读解释
4. 在GRPO优化中作为奖励信号，提升生成模型九个审美指标

## 🏗️ 模型架构

MUSECRITIC采用半标量架构，输入歌曲音频特征，通过编码器提取表示，然后生成自然语言评论（覆盖五个审美维度），评论嵌入与音频表示融合，最终通过回归头预测连续奖励分数。训练分两阶段：第一阶段用教师模型生成的高质量评论进行监督微调，第二阶段模型自生成评论用于奖励学习，避免训练推理分布不一致。

## 📚 数据集

- SongEval（训练/评估，200首测试歌曲）
- Music Arena（评估，733个偏好对）
- Audiobox Aesthetics（评估，用于GRPO优化后的指标）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-MSE | SongEval | 0.2875 | **0.2316** | -0.0559 |
| macro-LCC | SongEval | 未给出 | **0.9068** | — |
| macro-SRCC | SongEval | 未给出 | **0.8838** | — |
| macro-Kendall's tau | SongEval | 未给出 | **0.7178** | — |
| Accuracy | Music Arena | 未给出 | **71.35%** | — |

在SongEval测试集上，MUSECRITIC将宏平均MSE从0.2875降至0.2316，LCC、SRCC和Kendall's tau分别达到0.9068、0.8838和0.7178。在Music Arena基准上，准确率最高达71.35%。使用GRPO优化Muse-0.6B后，所有九个审美指标均有提升，表明评论条件奖励模型能有效指导歌曲生成。

## 🎯 结论与影响

MUSECRITIC通过引入自然语言评论作为中间表示，显著降低了歌曲奖励模型的评分误差，并提供了可解释的反馈。该方法在域内和域外数据集上均表现优异，且能作为强化学习信号提升生成模型质量。未来有望成为歌曲生成对齐的标准工具，推动可解释奖励模型的发展。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标；未与其他可解释奖励模型对比；域外测试仅一个基准，泛化性需更多验证；评论质量依赖教师模型，可能引入偏差。

## 🔗 开源资源

- **代码**：<https://github.com/WuqnEl/MuseCritic>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-14/">← 返回 2026-08-14 速递</a></div>
