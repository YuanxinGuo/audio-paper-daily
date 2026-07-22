---
title: "Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态嵌入"]
summary: "提出Fusion Embedding系列，通过轻量连接器将音频嵌入到冻结的视觉-语言嵌入空间中，实现跨模态检索。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态嵌入</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-文本检索</span> <span class="tag-pill tag-pill-soft">#多模态学习</span> <span class="tag-pill tag-pill-soft">#嵌入空间对齐</span> <span class="tag-pill tag-pill-soft">#零样本学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.18666</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.18666" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.18666" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Fusion Embedding系列，通过轻量连接器将音频嵌入到冻结的视觉-语言嵌入空间中，实现跨模态检索。
</div>

## 👥 作者与机构

**Abdul Basit Tonmoy** ¹ · Kazi Fardinul Hoque · Md. Shahrier Islam Arham · Arman Luthra

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态检索、音频-文本对齐方向的研究者。建议重点阅读第3节（方法设计）和第4节（消融实验），尤其是负结果分析部分。可复现其开源代码。

## 🌍 研究背景

当前多模态嵌入模型（如CLIP）在文本、图像、视频检索上表现优异，但缺乏音频模态。音频-文本检索由专用系统主导，无法与其他模态统一。本文旨在将音频嵌入到已有的视觉-语言嵌入空间中，实现单一索引支持所有模态查询，同时利用零样本能力实现音频-图像检索。

## 💡 核心创新

1. 提出Fusion Embedding系列，将音频嵌入到冻结的视觉-语言嵌入空间
2. 设计模态门控深度适配器，确保非音频输入输出与原始模型一致
3. 发现音频-图像检索可通过仅对齐音频-文本零样本涌现
4. 系统映射设计空间，报告多个负结果（如LLM改写字幕降低性能）
5. 单GPU数小时训练，完全开源

## 🏗️ 模型架构

输入音频经冻结的音频塔（如CLAP）提取特征，通过可训练连接器（16.4M参数）映射到冻结的视觉-语言嵌入空间（如SigLIP）。第二代引入模态门控深度适配器（44.2M参数），仅在音频输入时激活，确保文本/图像/视频输入输出与原始模型比特一致。训练时仅对齐音频-文本对，无需音频-图像对。

## 📚 数据集

- AudioCaps（训练/评估，音频-文本对）
- Clotho（训练/评估，音频-文本对）
- Flickr8k（评估，图像-文本对，用于零样本音频-图像检索）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Recall@1 (audio-text) | AudioCaps | CLAP (52.3) | **fusion-embedding-2 (56.1)** | +3.8 |
| Recall@1 (audio-text) | Clotho | CLAP (28.9) | **fusion-embedding-2 (32.4)** | +3.5 |
| Recall@1 (audio-image) | Flickr8k (zero-shot) | CLAP (N/A) | **fusion-embedding-2 (18.7)** | N/A |

在AudioCaps和Clotho上，fusion-embedding-2在音频-文本检索Recall@1上分别比CLAP高3.8和3.5个百分点。零样本音频-图像检索在Flickr8k上达到18.7% Recall@1，证明音频-图像对齐的涌现能力。消融实验显示，LLM改写字幕、替换更强音频塔、加宽连接器均降低性能，表明设计空间敏感。

## 🎯 结论与影响

本文证明通过轻量连接器可将音频嵌入到冻结的视觉-语言空间中，实现统一多模态检索，且音频-图像检索零样本涌现。该工作为多模态嵌入的扩展提供了高效范式，有望推动工业级多模态搜索系统的构建。

## ⚠️ 局限与未解决问题

零样本音频-图像检索性能较低（Recall@1 18.7%），且未在更大规模数据集上验证。未报告推理延迟或参数量对速度的影响。消融实验仅针对特定设计选择，缺乏对音频塔选择更系统的探索。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
