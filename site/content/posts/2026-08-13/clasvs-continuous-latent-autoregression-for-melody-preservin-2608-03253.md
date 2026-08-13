---
title: "CLASVS: Continuous-Latent Autoregression for Melody-Preserving Lyric Editing in Singing Voice Synthesis"
date: 2026-08-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#歌声合成"]
summary: "提出CLASVS，用连续潜自回归与状态控制转移实现保持旋律的歌词编辑，在中文基准上显著降低音素错误率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#歌声合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#歌声合成</span> <span class="tag-pill tag-pill-soft">#自回归</span> <span class="tag-pill tag-pill-soft">#歌词编辑</span> <span class="tag-pill tag-pill-soft">#连续潜变量</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.03253</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://piedpiperg.github.io/clasvs-demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">piedpiperg.github.io/clasvs-demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://piedpiperg.github.io/clasvs-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">piedpiperg.github.io/clasvs-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.03253" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.03253" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://piedpiperg.github.io/clasvs-demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://piedpiperg.github.io/clasvs-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CLASVS，用连续潜自回归与状态控制转移实现保持旋律的歌词编辑，在中文基准上显著降低音素错误率。
</div>

## 👥 作者与机构

**Yizhong Geng** ¹ · Tian-Hao Zhang · Chunfeng Wang · Wenxin Fu · Yingming Gao · Ruimin Wang · Zhou Pan · Kun Zhan · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合歌声合成、语音编辑方向的研究者。建议重点阅读第3节的SCT路由与PSCG训练策略，以及第4节的实验对比。可先看摘要与图1了解整体框架，再深入方法部分。

## 🌍 研究背景

歌词编辑任务需在保持旋律、音色和自然度的同时替换歌词。现有方法多基于离散码本的自回归模型，如Vevo2，但离散码本限制生成质量。此外，训练与推理存在不一致：训练时参考线索与原始歌词匹配，推理时需覆盖源歌词相关线索，导致模型可能跟随源内容。本文旨在解决这些挑战，提出连续潜自回归方法。

## 💡 核心创新

1. 提出State-Control-Transition (SCT)路由，分离目标歌词与参考旋律控制
2. 引入Progressive State-Control Grounding (PSCG)训练策略，无需配对编辑数据
3. 采用连续潜自回归，避免离散码本，支持逐步生成与学习停止
4. 在中文基准上显著降低音素错误率，同时保持旋律与音色
5. 提供无分数标注的歌词编辑方案，扩展逐步控制应用

## 🏗️ 模型架构

CLASVS采用连续潜自回归架构。输入为参考音频与目标歌词，通过编码器提取参考旋律与音色特征。主干为自回归Transformer，其状态由SCT路由控制：目标歌词控制与参考旋律控制持久化，语义反馈返回给因果规划器，前一步潜变量仅影响局部Transition。训练时使用PSCG，通过内容一致的语音重建学习状态转移。输出为连续潜变量，经解码器生成编辑后的歌声。

## 📚 数据集

- 中文基准数据集（训练与评估，具体名称未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-PER | 中文基准 | Vevo2 (离散AR) | **未给出具体值** | -46.2% |

在中文基准上，CLASVS在四种操作（替换、插入、删除、保留）上均优于离散AR基线Vevo2，宏观音素错误率降低46.2%，同时保持旋律、歌手相似度和感知质量。摘要未提供具体数值，但强调所有指标均提升。

## 🎯 结论与影响

CLASVS建立了连续自回归在歌词编辑中的有效操作点，通过SCT路由和PSCG训练解决了训练-推理不一致问题，显著提升编辑准确性。该工作为无分数标注的歌词编辑提供了新思路，并可能推动逐步控制生成在歌声合成中的应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题：仅在中文基准上评估，泛化性未知；未报告推理延迟或计算开销；与Vevo2对比但未与其他连续自回归方法比较；未提供消融实验验证各组件贡献。

## 🔗 开源资源

- **项目主页**：<https://piedpiperg.github.io/clasvs-demo/>
- **Demo / 试听**：<https://piedpiperg.github.io/clasvs-demo/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-13/">← 返回 2026-08-13 速递</a></div>
