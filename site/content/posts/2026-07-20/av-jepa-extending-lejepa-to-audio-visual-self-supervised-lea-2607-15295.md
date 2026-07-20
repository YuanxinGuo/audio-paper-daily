---
title: "AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#自监督学习"]
summary: "提出AV-JEPA，将LeJEPA扩展到音视频自监督学习，采用早期融合ViT和模态丢弃，无需解码器或负样本，在VGGSound和AudioSet上取得有竞争力的分类与检索性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#自监督学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态学习</span> <span class="tag-pill tag-pill-soft">#音频-视觉</span> <span class="tag-pill tag-pill-soft">#表示学习</span> <span class="tag-pill tag-pill-soft">#联合嵌入</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.15295</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.15295" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.15295" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AV-JEPA，将LeJEPA扩展到音视频自监督学习，采用早期融合ViT和模态丢弃，无需解码器或负样本，在VGGSound和AudioSet上取得有竞争力的分类与检索性能。
</div>

## 👥 作者与机构

**Benjamin Robson** ¹ · Santeri Mentu · Wenshuai Zhao · Arno Solin

**机构**：阿尔托大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对自监督多模态表示学习感兴趣的读者。建议重点阅读第3节方法部分和第4节实验，尤其是消融研究。可先看图1架构概览。

## 🌍 研究背景

自监督学习在单模态（如音频、视觉）上取得了显著进展，但多模态联合学习仍面临挑战。现有方法如CLIP依赖对比学习和大批量负样本，而MAE-style方法需要解码器重建。LeJEPA在图像上通过SIGReg目标实现无解码器、无负样本的表示学习。本文将其扩展到音视频领域，解决跨模态对齐问题，提出AV-JEPA。

## 💡 核心创新

1. 早期融合Vision Transformer处理音视频输入
2. 模态丢弃（modality dropout）作为掩蔽策略
3. SIGReg目标实现跨模态对齐
4. 无需解码器、EMA教师、对比负样本的简洁架构

## 🏗️ 模型架构

输入为音频频谱图和视频帧，经线性投影后拼接成token序列，送入早期融合Vision Transformer（ViT）。训练时随机丢弃整个模态的token（模态丢弃），剩余token经ViT编码后，对全局视图和局部视图（每个模态分别）应用SIGReg损失，鼓励嵌入分布对齐。推理时直接使用编码器输出。无解码器、无EMA教师。

## 📚 数据集

- VGGSound（训练/评估，约300类）
- AudioSet（训练/评估，约527类）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Top-1 Accuracy | VGGSound | AV-MAE 56.2% | **57.1%** | +0.9% |
| mAP | AudioSet | AV-MAE 32.0 | **32.7** | +0.7 |

在VGGSound上top-1准确率57.1%，AudioSet上mAP 32.7，均优于AV-MAE。零样本音视频检索性能与对比学习方法相当，但无需负样本。消融实验验证了模态丢弃和SIGReg的有效性。

## 🎯 结论与影响

AV-JEPA以简洁架构实现有竞争力的音视频自监督学习，无需解码器或负样本，为多模态表示学习提供了新范式。未来可扩展到更多模态和下游任务，对工业界高效预训练有潜在价值。

## ⚠️ 局限与未解决问题

仅在分类和检索任务上评估，未在细粒度任务（如音视频分割）上验证。模态丢弃策略可能丢失信息，未与随机掩蔽对比。未报告推理速度或参数量。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-20/">← 返回 2026-07-20 速递</a></div>
