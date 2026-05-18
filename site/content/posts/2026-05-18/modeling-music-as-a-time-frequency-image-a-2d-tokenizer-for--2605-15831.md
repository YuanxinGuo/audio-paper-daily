---
title: "Modeling Music as a Time-Frequency Image: A 2D Tokenizer for Music Generation"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出BandTok，一种面向音乐生成的2D梅尔频谱分词器，用单一码本表示频带token，简化自回归建模。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频分词器</span> <span class="tag-pill tag-pill-soft">#自回归生成</span> <span class="tag-pill tag-pill-soft">#梅尔频谱</span> <span class="tag-pill tag-pill-soft">#2D位置编码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.15831</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.15831" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.15831" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出BandTok，一种面向音乐生成的2D梅尔频谱分词器，用单一码本表示频带token，简化自回归建模。
</div>

## 👥 作者与机构

**Yuqing Cheng** ¹ · Xingyu Ma · Guochen Yu · Xiaotao Gu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成和音频分词方向的研究者。建议重点读§3的BandTok设计及§4的2D RoPE部分，对比实验见表2。可先看§3.2的PatchGAN和EMA更新细节。

## 🌍 研究背景

自回归音乐生成依赖高质量音频分词器。现有高保真编解码器多采用残差多码本量化，虽重建质量好，但序列展平后残差层次引入强依赖，易累积误差。本文旨在设计一种生成友好的分词器，简化token结构以提升自回归建模效果。

## 💡 核心创新

1. 提出BandTok：2D梅尔频谱分词器，每帧用单一码本的频带token表示
2. 引入多尺度PatchGAN损失和EMA码本更新提升重建质量
3. 设计2D旋转位置编码（2D RoPE）保持时频结构
4. 在数据受限场景下取得优于残差码本分词器的结果

## 🏗️ 模型架构

输入音频经短时傅里叶变换得到梅尔频谱图，BandTok编码器将频谱图映射为2D token网格（时间帧×频带），每个token来自单一共享码本。解码器基于PatchGAN和EMA更新重建频谱。自回归语言模型采用2D RoPE，在生成时同时建模时间和频率维度。

## 📚 数据集

- MusicCaps（评估，约5.5k样本）
- 内部数据集（训练，数据受限设置）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | MusicCaps | EnCodec (4.5) | **3.8** | -0.7 |
| KL散度 | MusicCaps | EnCodec (1.2) | **1.0** | -0.2 |

在MusicCaps上，BandTok的FAD为3.8，KL散度为1.0，优于EnCodec基线。消融实验验证了PatchGAN和EMA更新的有效性。在数据受限条件下，BandTok仍保持竞争力，表明其token结构对自回归建模更友好。

## 🎯 结论与影响

BandTok通过2D梅尔频谱分词器简化了token结构，在数据受限场景下优于残差码本方法。该工作为生成导向的音频分词提供了新思路，可能推动低资源音乐生成的发展。工业上可降低对大规模数据的依赖。

## ⚠️ 局限与未解决问题

仅在数据受限设置下验证，未在更大规模数据上对比；未报告推理速度或参数量；与最新编解码器（如DAC）的对比缺失；主观评测（MOS）未提供。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-18/">← 返回 2026-05-18 速递</a></div>
