---
title: "Video-to-Music Generation for Gameplay Videos"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "构建217.6小时SNES游戏视频-配乐数据集，用冻结ViViT编码器接MusicGen解码器做视频到音乐生成，客观指标超基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#视频到音乐</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.31810</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.31810" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.31810" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建217.6小时SNES游戏视频-配乐数据集，用冻结ViViT编码器接MusicGen解码器做视频到音乐生成，客观指标超基线。
</div>

## 👥 作者与机构

**Felipe Marra** ¹ · Lucas N. Ferreira

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视频到音乐生成、多模态生成、游戏音频的研究者阅读。建议重点看 §3 数据集构建流程（音频指纹匹配、去音效/人声）与 §4 编码器对比实验，表 2 的冻结 vs 微调结果值得细看。若只关心方法可略读基线部分。

## 🌍 研究背景

视频到音乐生成近年在电影与音乐视频场景进展明显，主流做法是用视频特征条件化音乐生成模型（如 MusicGen、GVMGen）。但游戏场景带来新挑战：画面是渲染图形而非实拍、音乐多为合成音、配乐按关卡循环而非跟随画面事件。现有数据集缺乏干净的游戏配乐与视频对齐数据，导致该场景研究受限。本文要解决游戏视频到音乐的生成问题，并构建配套数据集。

## 💡 核心创新

1. 构建217.6小时SNES游戏视频-配乐数据集，音频指纹对齐
2. 对比T5/ViT/ViViT三种视频编码策略接MusicGen解码器
3. 发现冻结编码器普遍优于微调编码器
4. 冻结ViViT取得最佳客观指标，参数量少18%

## 🏗️ 模型架构

输入为游戏视频帧序列，分别尝试三种编码器：文本描述经T5、独立帧经ViT、时空块经ViViT，将视频特征直接送入MusicGen解码器。编码器分别测试冻结与微调两种设置，解码器始终微调。模型为简单encoder-decoder transformer结构，冻结ViViT编码器整体效果最佳，参数量比基线少最多18%。

## 📚 数据集

- SNES游戏视频-配乐数据集（训练/评估，217.6小时视频+485小时干净配乐）

## 📊 实验结果

摘要未给出具体数值指标，仅说明：冻结编码器在所有指标上匹配或超过微调版本；冻结ViViT整体最佳；参数量最多少18%的情况下客观指标超过所有基线，听测中超过GVMGen，与OSSL相当（N=96）。

## 🎯 结论与影响

本文最强结论是冻结视频编码器接MusicGen解码器即可在游戏视频到音乐生成上超过现有基线，且参数更少。这提示该任务中视频编码器微调可能不必要，对后续多模态音乐生成研究有参考价值。工业上可用于游戏配乐自动生成，降低人工作曲成本。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与生成音乐质量的主观MOS细节；听测仅N=96且只与两个基线比较；数据集限于SNES复古游戏，泛化到现代游戏存疑；未做编码器组合或解码器消融。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
