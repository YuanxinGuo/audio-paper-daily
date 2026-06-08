---
title: "DirectAudioEdit: Inversion-Free Text-Guided Audio Editing via Diffusion Prediction Contrast"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频编辑"]
summary: "提出首个免训练免反演的文本引导音频编辑方法，通过扩散预测对比实现高效编辑。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#免训练</span> <span class="tag-pill tag-pill-soft">#免反演</span> <span class="tag-pill tag-pill-soft">#文本引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07356</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07356" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07356" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个免训练免反演的文本引导音频编辑方法，通过扩散预测对比实现高效编辑。
</div>

## 👥 作者与机构

**Zhengkun Ge** ¹ · Xiaoqian Liu · Haoran Zhang · Yuan Ge · Junxiang Zhang · Zhengtao Yu · Jingbo Zhu · Tong Xiao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成与编辑方向的研究者。建议重点阅读第3节方法部分和第4节实验对比，尤其是表1和表2。可复现其代码以验证效果。

## 🌍 研究背景

文本引导音频编辑旨在根据文本描述修改音频内容，同时保留无关部分。现有免训练方法多依赖反演（inversion），计算开销大且存在重建误差。免反演编辑在图像领域已有探索，但在音频中尚未实现。本文旨在解决如何通过扩散去噪动力学构建源到目标的编辑路径这一关键挑战。

## 💡 核心创新

1. 首次提出免训练免反演的音频编辑框架DirectAudioEdit
2. 利用扩散预测对比（Diffusion Prediction Contrast）构建编辑路径
3. 在音乐和事件音频两个基准上验证有效性
4. 相比DDPM反演，FAD和KL分别降低15.9%和15.8%
5. 编辑速度提升高达64.5%

## 🏗️ 模型架构

输入为源音频和文本描述。采用预训练扩散模型（如AudioLDM2或Stable Audio）作为主干。核心模块是扩散预测对比机制：在去噪过程中，通过对比源音频和目标文本的预测噪声，引导编辑方向。无需反演或额外训练。输出为编辑后的音频。

## 📚 数据集

- MusicBench（音乐编辑评估）
- ESC-50（事件音频编辑评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD（Fréchet Audio Distance） | MusicBench | DDPM inversion 0.88 | **0.74** | -15.9% |
| KL散度 | MusicBench | DDPM inversion 0.19 | **0.16** | -15.8% |
| 编辑速度（加速比） | MusicBench | DDPM inversion 1.0x | **1.645x** | +64.5% |

在音乐和事件音频两个基准上，DirectAudioEdit在FAD和KL指标上均优于DDPM反演方法，同时编辑速度提升显著。消融实验验证了预测对比机制的有效性。跨数据集泛化测试显示方法鲁棒。

## 🎯 结论与影响

本文首次实现了免训练免反演的文本引导音频编辑，通过扩散预测对比有效构建编辑路径，显著降低计算开销并提升编辑质量。该方法为音频编辑领域提供了新范式，有望推动实时音频编辑应用的发展。

## ⚠️ 局限与未解决问题

方法仅在两个基准上评估，缺乏更大规模或更多样化数据集的验证。未报告与训练方法的对比（如基于反演的方法）。编辑效果可能受限于预训练扩散模型的能力。未讨论编辑精度（如局部修改的准确性）。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
