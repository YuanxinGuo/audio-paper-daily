---
title: "HeartMuLa: A Family of Open Sourced Music Foundation Models"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "开源音乐基础模型系列，包含对齐、歌词识别、编解码和可控歌曲生成，首次用学术资源复现商业级系统。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐理解</span> <span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#音频编解码</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.10547</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.10547" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.10547" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>开源音乐基础模型系列，包含对齐、歌词识别、编解码和可控歌曲生成，首次用学术资源复现商业级系统。
</div>

## 👥 作者与机构

**Dongchao Yang** ¹ · Yuxin Xie · Yuguo Yin · Zheyu Wang · Xiaoyu Yi · Gongxi Zhu · Xiaolong Weng · Zihan Xiong · … 等 21 人

**机构**：北京大学 · 字节跳动

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐AI研究者及工业应用开发者。建议通读，重点看§3.3 HeartCodec的低帧率设计（12.5 Hz）和§3.4 HeartMuLa的7B扩展与可控生成。可先看表2的客观指标对比。

## 🌍 研究背景

音乐基础模型领域此前缺乏开源方案，商业系统如Suno、Udio未公开细节。现有工作多聚焦单一任务（如歌词识别或音乐生成），缺乏统一框架。本文旨在构建一个涵盖理解与生成的开源音乐基础模型家族，解决多任务协同与可控生成问题。

## 💡 核心创新

1. HeartCLAP: 音频-文本对齐模型，支持多模态检索
2. HeartTranscriptor: 鲁棒歌词识别，优化真实音乐场景
3. HeartCodec: 12.5 Hz低帧率高保真编解码器，保留长程结构
4. HeartMuLa: 基于LLM的可控歌曲生成，支持细粒度属性控制
5. 首次用学术级数据与GPU复现Suno级商业系统

## 🏗️ 模型架构

框架包含四个组件：HeartCLAP采用对比学习对齐音频与文本；HeartTranscriptor基于编码器-解码器结构，含语音增强前端；HeartCodec使用残差向量量化（RVQ）在12.5 Hz帧率下编码，结合Transformer解码器重建；HeartMuLa基于LLaMA架构，以文本、歌词、参考音频为条件，通过自回归生成Codec token，支持7B参数扩展。

## 📚 数据集

- 内部数据集（训练，包含歌词、风格标注，规模未公开）
- 公开数据集（评估，如MUSDB18、Medley-solos-DB等，具体未列）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FAD | MUSDB18 | MusicGen 3.3B 2.0 | **HeartMuLa 7B 1.2** | -0.8 |
| CLAP Score | 内部测试集 | MusicGen 3.3B 0.32 | **HeartMuLa 7B 0.38** | +0.06 |

HeartMuLa 7B在FAD和CLAP Score上优于MusicGen 3.3B，且歌词识别准确率（WER）在真实场景下达到12.5%，优于公开基线。HeartCodec在12.5 Hz帧率下重建质量接近EnCodec（24 kHz），但码率更低。消融实验验证了各组件贡献。

## 🎯 结论与影响

本文首次用学术资源复现商业级音乐生成系统，开源模型家族为音乐AI研究提供了强基线。HeartCodec的低帧率设计对高效生成有重要启发，HeartMuLa的可控性为工业应用（如短视频配乐）铺平道路。

## ⚠️ 局限与未解决问题

未报告推理延迟与参数量细节；歌词识别仅在中文数据集上评估，泛化性未知；可控生成中细粒度属性控制的效果缺乏主观评测；7B模型训练数据规模未明确，可能依赖内部数据。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-08/">← 返回 2026-07-08 速递</a></div>
