---
title: "MambaVoice: Lightweight Audiovisual Singing Voice Separation Via A Hybrid Mamba-Transformer Model"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "MambaVoice 用 Mamba-Transformer 混合骨干加视听融合，轻量地做目标歌声分离，16.2M 参数在 Acappella 上达 14.18 dB SDR。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.26635</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.26635" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.26635" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MambaVoice 用 Mamba-Transformer 混合骨干加视听融合，轻量地做目标歌声分离，16.2M 参数在 Acappella 上达 14.18 dB SDR。
</div>

## 👥 作者与机构

**Adithi Shankar** ¹ · Gopika Krishnan · Gloria Haro · Xavier Serra · Mart\'in Rocamora

**机构**：庞培法布拉大学 · 巴塞罗那音乐科技集团

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐源分离、视听多模态分离的研究者与工程落地团队阅读。建议重点看 §3 的 band-split 音频编码器、ST-GCN 视觉分支与乘法门控融合，以及 §4 表 2 的 Acappella/URSing 跨数据集结果与参数量对比；消融与感知实验部分可快速浏览。

## 🌍 研究背景

从音乐视频中分离目标歌声在多人演唱与密集伴奏下仍困难。此前 SOTA 多为纯音频的 BSRNN、Demucs 类大模型，或视听方法如使用 U-Net 视觉分支的模型，参数量大、长时建模代价高。纯音频方法无法利用唇动/面部运动线索区分同曲多歌手，而现有视听方法又偏重、推理成本高。本文要解决的是：在保持轻量的前提下，用视听线索做目标歌声分离，并验证 SSM+注意力混合骨干的有效性。

## 💡 核心创新

1. 提出 Mamba-Transformer 混合骨干，用 Selective SSM 做线性复杂度长时建模
2. band-split 音频编码器 + ST-GCN 面部运动特征的双流视听编码
3. 乘法门控融合，让视觉线索选择性调制音频表征
4. 16.2M 参数下在 Acappella 达 14.18 dB SDR，跨数据集泛化到 URSing

## 🏗️ 模型架构

输入为混合音频与对应视频。音频经 attention-based band-split 编码器得到子带表征；视觉流用 ST-GCN 从人脸区域提取时空面部运动特征。两模态通过乘法门控融合，视觉特征对音频表征做选择性调制。融合特征送入混合骨干：Transformer 自注意力与 Selective State Space Model 交替堆叠，兼顾局部注意力与线性复杂度长时建模，最终输出目标歌声的掩蔽/波形。模型总参数量 16.2M，定位为轻量组件。

## 📚 数据集

- Acappella（训练与评估，含干扰歌手的困难混合）
- URSing（跨数据集评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR | Acappella | 更大规模基线模型（摘要未给具体值） | **14.18 dB** | 摘要未给具体差值 |

摘要仅给出 Acappella 上 14.18 dB SDR 与 16.2M 参数量，并称在 URSing 上跨数据集表现良好、与更大模型相当。作者还做了感知研究支持客观指标提升。但摘要未列出具体基线数值、消融结果、推理延迟与各数据集完整对比，难以判断增益幅度。

## 🎯 结论与影响

最强结论是：混合 SSM-注意力骨干可在 16.2M 参数下取得与更大模型相当的视听歌声分离性能。这为轻量、可扩展的视听源分离提供了可行路线，也提示其可作为大型流水线中的前端组件。工业上对移动端/实时音乐处理有潜在价值，但需补充效率与延迟数据。

## ⚠️ 局限与未解决问题

摘要未给出与具体基线的数值对比、缺少消融验证各模块贡献，也未报告推理延迟与显存占用；Acappella 与 URSing 的歌手/语言分布可能带来 bias，跨数据集提升幅度未量化；感知研究细节与听测规模未说明。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
