---
title: "Text-Prompted CLAP: Learning Query-Conditioned Audio Representations via Contrastive Learning"
date: 2026-07-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频表示学习"]
summary: "提出Text-Prompted CLAP，通过交叉注意力融合文本提示到音频特征，在音频问答、检索和零样本分类上提升CLAP性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频表示学习</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#跨模态检索</span> <span class="tag-pill tag-pill-soft">#音频问答</span> <span class="tag-pill tag-pill-soft">#参数高效微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.25085</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.25085" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.25085" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Text-Prompted CLAP，通过交叉注意力融合文本提示到音频特征，在音频问答、检索和零样本分类上提升CLAP性能。
</div>

## 👥 作者与机构

**Mohan Li** ¹ · Rama Doddipatla · Philip C. Woodland ✉

**机构**：剑桥大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频-语言多模态学习、音频检索或音频问答的研究者阅读。建议重点看§3的模型架构和§4的实验结果，尤其是表1-3。可先读§3.2的音频-MCQ框架。

## 🌍 研究背景

CLAP通过对比学习对齐音频和文本表示，但独立编码限制了跨模态语义建模。现有方法如AudioCLIP、Wav2CLIP等也面临类似问题。本文旨在通过引入文本提示的交叉注意力融合，增强音频表示对查询条件的适应性，提升复杂音频理解和检索任务性能。

## 💡 核心创新

1. 交叉注意力融合模块将文本提示注入音频特征
2. 音频多项选择（audio-MCQ）训练框架
3. 参数高效扩展，仅增加少量参数
4. 在音频问答任务上媲美大型音频-LLM

## 🏗️ 模型架构

输入音频经CLAP音频编码器提取特征，文本提示经CLAP文本编码器提取嵌入，然后通过交叉注意力融合模块将文本提示嵌入作为query，音频特征作为key/value，输出查询条件化的音频表示。该表示与候选答案文本嵌入通过对比学习对齐。整体采用预训练CLAP权重初始化，仅训练融合模块和少量适配层。

## 📚 数据集

- Clotho（音频-文本检索评估）
- AudioCaps（音频-文本检索评估）
- VGGSound（零样本分类评估）
- MusicCaps（音乐检索微调评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| R@1 | Clotho (audio→text) | CLAP 17.1 | **TP-CLAP 18.5** | +1.4 |
| R@1 | AudioCaps (audio→text) | CLAP 42.3 | **TP-CLAP 44.1** | +1.8 |
| Accuracy | VGGSound (zero-shot) | CLAP 39.2 | **TP-CLAP 40.5** | +1.3 |

TP-CLAP在音频-文本检索和零样本分类上一致优于CLAP基线。在音频问答任务上，TP-CLAP（仅220M参数）在Clotho-AQA上达到52.3%准确率，接近更大模型（如LTU-AS 53.1%）。音乐检索微调后，TP-CLAP在MusicCaps上R@1达28.7%，优于CLAP的25.9%。

## 🎯 结论与影响

TP-CLAP通过轻量级交叉注意力融合有效提升了CLAP的跨模态语义建模能力，在多个下游任务上取得改进。该方法为参数高效的多模态表示学习提供了新思路，有望推动音频检索和问答系统的实际应用。

## ⚠️ 局限与未解决问题

仅在公开数据集上评估，未在真实场景噪声下测试；音频问答任务仅与部分基线对比，缺乏与更多音频-LLM的公平比较；未报告推理延迟和参数量细节；融合模块设计较简单，可能无法捕捉复杂时序依赖。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-30/">← 返回 2026-07-30 速递</a></div>
