---
title: "Few-Shot Synthetic Accented Speech for ASR Fine-Tuning: What Helps and When?"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "探究合成口音语音对ASR微调的有效性，发现随机音素扰动即可获得大部分收益，真实口音音素和韵律增益有限。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#口音语音合成</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#少样本学习</span> <span class="tag-pill tag-pill-soft">#ASR微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.27273</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.27273" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.27273" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>探究合成口音语音对ASR微调的有效性，发现随机音素扰动即可获得大部分收益，真实口音音素和韵律增益有限。
</div>

## 👥 作者与机构

**Yurii Halychanskyi** ¹ · Nimet Beyza Bozdag · Mark Hasegawa-Johnson · Dilek Hakkani-T\"ur · Volodymyr Kindratenko

**机构**：伊利诺伊大学厄巴纳-香槟分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事ASR数据增强、口音识别的研究者阅读。重点看§3实验设置和§4结果分析，特别是表1和表2的对比。可跳过§2相关工作。

## 🌍 研究背景

真实口音语音数据稀缺是ASR系统面临的主要挑战之一。合成口音语音作为一种数据增强手段被广泛研究，但其有效性的来源尚不明确。现有方法通常使用LLM生成目标口音的音素编辑，但缺乏与随机扰动、真实口音音素和韵律的对比分析。本文旨在系统性地解耦这些因素，探究合成口音数据中哪些成分真正有助于ASR微调。

## 💡 核心创新

1. 对比LLM生成口音编辑与随机音素替换的效果
2. 引入真实口音音素和韵律作为oracle控制
3. 分析合成数据与真实数据混合时的比例效应

## 🏗️ 模型架构

采用少样本TTS流水线：输入文本→LLM生成目标口音音素序列（或随机替换）→TTS合成语音。使用预训练TTS模型（如VITS）生成语音，然后用于微调ASR模型（如Whisper）。实验控制变量包括音素编辑类型（LLM生成、随机替换、真实口音）、是否加入真实口音韵律。

## 📚 数据集

- Common Voice（真实口音语音，用于微调和评估）
- LibriTTS（中性语音，用于TTS训练）
- LJSpeech（中性语音，用于TTS训练）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | Common Voice（口音测试集） | 无合成数据 25.0 | **随机替换 18.5** | -6.5% |
| WER | Common Voice（口音测试集） | LLM口音编辑 17.8 | **随机替换 18.5** | +0.7% |

随机音素替换在ASR微调中恢复了大部分收益（WER从25.0降至18.5），LLM生成的口音编辑仅额外降低0.7%。真实口音音素与随机基线接近，加入真实口音韵律仅带来微小改进。混合合成与真实口音数据可稳定低资源微调，但固定合成预算会稀释真实数据信息。

## 🎯 结论与影响

合成口音语音对ASR微调的主要收益来自音素空间的随机扰动，而非精确的口音编辑。这提示未来数据增强可简化生成流程，无需复杂口音建模。工业应用中，应谨慎控制合成与真实数据的比例，避免稀释真实信息。

## ⚠️ 局限与未解决问题

仅使用单一TTS模型和ASR模型（Whisper），泛化性未知。未评估不同口音类型和严重程度的影响。缺乏对合成语音自然度的客观度量（如MOS）。未报告推理延迟和计算成本。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
