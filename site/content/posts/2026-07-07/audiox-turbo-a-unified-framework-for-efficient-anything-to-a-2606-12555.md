---
title: "AudioX-Turbo: A Unified Framework for Efficient Anything-to-Audio Generation"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出统一高效的多模态到音频生成框架AudioX-Turbo，通过教师-学生蒸馏实现4步采样，性能优于多步基线。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音频</span> <span class="tag-pill tag-pill-soft">#文本到音乐</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.12555</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://zeyuet.github.io/AudioX-Turbo/" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">zeyuet.github.io/AudioX-Turbo/</span></span></a><a class="oc-chip oc-chip-proj" href="https://zeyuet.github.io/AudioX-Turbo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">zeyuet.github.io/AudioX-Turbo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.12555" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.12555" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://zeyuet.github.io/AudioX-Turbo/" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://zeyuet.github.io/AudioX-Turbo/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一高效的多模态到音频生成框架AudioX-Turbo，通过教师-学生蒸馏实现4步采样，性能优于多步基线。
</div>

## 👥 作者与机构

**Zeyue Tian** ¹ · Lei Ke · Zhaoyang Liu · Ruibin Yuan · Liumeng Xue · Yujiu Yang · Weijia Chen · Xu Tan · … 等 3 人

**机构**：清华大学 · 香港科技大学 · 微软研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、扩散模型蒸馏方向的研究者。建议重点阅读§3.2多模态自适应融合模块和§3.3分布匹配蒸馏部分，以及表1-3的实验结果。可先看§4.2的NFE对比。

## 🌍 研究背景

音频生成领域面临三大挑战：缺乏统一的多模态建模框架、大规模高质量训练数据不足、多步扩散推理成本高。现有方法如AudioLDM、Make-An-Audio等通常针对单一模态条件，且需要数十步采样。本文旨在构建一个统一的高效框架，支持文本、视频、音频等多种条件输入，同时大幅降低推理步数。

## 💡 核心创新

1. 多模态自适应融合模块对齐文本/视频/音频输入
2. 基于分布匹配蒸馏的流匹配蒸馏方法
3. 扩散判别器辅助少步生成质量
4. 构建9.2M样本的高质量数据集IF-caps-Pro

## 🏗️ 模型架构

输入：文本/视频/音频经各自编码器提取特征；主干：多模态扩散Transformer（MDT），包含多模态自适应融合模块（MAF）对齐不同模态嵌入；关键模块：教师模型AudioX-Base采用MDT，学生模型AudioX-Turbo通过分布匹配蒸馏（DMD）适配流匹配，并加入扩散判别器；输出：生成音频的mel谱图。模型参数量未提及。

## 📚 数据集

- IF-caps-Pro（训练，9.2M样本，含文本-音频/视频-音频/音频-音频对）
- AudioCaps（评估文本到音频）
- MusicCaps（评估文本到音乐）
- VAS（评估视频到音频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | AudioCaps | AudioLDM 2.32 | **1.85** | -0.47 |
| CLAP score | AudioCaps | AudioLDM 0.31 | **0.35** | +0.04 |
| FAD | MusicCaps | MusicGen 2.10 | **1.72** | -0.38 |
| NFE | 通用 | 多步基线 200 | **4** | -196 (25x减少) |

AudioX-Turbo在文本到音频和文本到音乐任务上均取得最优FAD和CLAP分数，仅需4步采样，NFE减少约25倍。消融实验验证了MAF模块和DMD蒸馏的有效性。跨数据集泛化测试显示模型对未见条件具有鲁棒性。

## 🎯 结论与影响

本文提出的AudioX-Turbo实现了统一高效的多模态到音频生成，4步采样即可达到甚至超越多步基线质量。该工作为实时音频生成应用铺平道路，其蒸馏框架可推广至其他生成任务。工业上可用于内容创作、辅助工具等场景。

## ⚠️ 局限与未解决问题

未报告推理延迟（秒级）和模型参数量；仅评估了FAD和CLAP分数，缺乏主观MOS测试；数据集IF-caps-Pro未开源（声称将开源）；视频到音频任务仅在一个数据集上评估，泛化性待验证。

## 🔗 开源资源

- **代码**：<https://zeyuet.github.io/AudioX-Turbo/>
- **项目主页**：<https://zeyuet.github.io/AudioX-Turbo/>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-07/">← 返回 2026-07-07 速递</a></div>
