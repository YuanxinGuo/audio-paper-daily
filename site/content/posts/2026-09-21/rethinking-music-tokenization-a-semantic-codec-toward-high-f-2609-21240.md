---
title: "Rethinking Music Tokenization: A Semantic Codec toward High-Fidelity LLM Music Generation"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出音乐语义编解码器 MuSeC，将语义与声学内容从混合信号中解耦，产出更利于语言模型建模的离散 token。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐生成</span> <span class="tag-pill tag-pill-soft">#神经音频编解码</span> <span class="tag-pill tag-pill-soft">#离散tokenization</span> <span class="tag-pill tag-pill-soft">#语义表征</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.21240</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://longwaytog0.github.io/MuSeC/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">longwaytog0.github.io/MuSeC/</span></span></a><a class="oc-chip oc-chip-demo" href="https://longwaytog0.github.io/MuSeC/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">longwaytog0.github.io/MuSeC/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.21240" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.21240" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://longwaytog0.github.io/MuSeC/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://longwaytog0.github.io/MuSeC/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出音乐语义编解码器 MuSeC，将语义与声学内容从混合信号中解耦，产出更利于语言模型建模的离散 token。
</div>

## 👥 作者与机构

**Huakang Chen** ¹ · Guobin Ma · Yuepeng Jiang · Dake Guo · Jingbin Hu · Hanke Xie · Wenhao Li · Lingxin Xiong · … 等 5 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐生成、音频 tokenizer、LLM 音频建模的研究者。建议通读，重点看语义/声学解耦模块设计与 token 熵分析部分，以及重建质量与 LM 可预测性的联合评估。可先看方法框架图与重建指标表，再核对是否与 speech 语义 codec（如 SpeechTokenizer）做对比。

## 🌍 研究背景

离散音频 tokenization 是波形与自回归建模之间的关键接口。此前重建导向的 tokenizer（如 SoundStream、EnCodec）把音乐结构与细粒度声学细节混在一起，token 熵高、难被 LM 建模；而语义导向方案多针对语音设计，迁移到音乐会损害重建质量。本文要解决的核心问题是：如何在保持高保真重建的同时，产出更 LM-friendly 的离散单元。

## 💡 核心创新

1. 以 MIR 下游任务定义可度量的音乐语义内容
2. MuSeC 无需源分离即可从混合信号解耦语义与声学
3. 兼顾高保真重建与低熵、可预测的 token 序列

## 🏗️ 模型架构

摘要未给出完整网络细节。整体思路为：输入原始音乐波形 → 编码器提取表征 → 通过语义/声学因子分解模块，在不做源分离的前提下将语义内容与声学细节解耦 → 分别量化得到离散 token → 解码器重建波形。语义分支对齐 MIR 任务所需信息，声学分支保留高保真重建所需细节，最终输出兼顾重建质量与 LM 可建模性的 token 序列。具体主干网络名与参数量摘要未披露。

## 📊 实验结果

摘要仅定性说明 MuSeC 在重建质量上优于现有方案，并产生更可预测的 token 序列，未给出 SI-SDR、PESQ、FAD、token 熵或 MIR 任务准确率等具体数值，也未列出所用数据集与基线名称，因此无法量化对比。

## 🎯 结论与影响

最强结论是：以 MIR 任务定义的语义内容为准则，可在不牺牲重建质量的前提下获得更 LM-friendly 的音乐 token。这为高保真 LLM 音乐生成提供了 tokenizer 层面的新思路，可能推动后续工作重新审视音乐 tokenization 的语义-声学权衡。工业上若成立，可降低音乐生成模型的序列建模难度与推理成本。

## ⚠️ 局限与未解决问题

摘要未给出任何定量结果、数据集、基线或消融，难以判断相对 EnCodec/SoundStream 等重建导向 tokenizer 的实际增益。语义定义依赖 MIR 任务选择，可能存在任务偏置；未报 token 率、推理延迟与参数量，也未说明是否与 speech 语义 codec 公平对比。

## 🔗 开源资源

- **项目主页**：<https://longwaytog0.github.io/MuSeC/>
- **Demo / 试听**：<https://longwaytog0.github.io/MuSeC/>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
