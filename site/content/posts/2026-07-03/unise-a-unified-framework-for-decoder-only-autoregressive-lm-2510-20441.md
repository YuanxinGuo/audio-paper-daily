---
title: "UniSE: A Unified Framework for Decoder-Only Autoregressive LM-Based Speech Enhancement"
date: 2026-07-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出UniSE，一个基于解码器自回归语言模型的统一框架，可同时处理语音恢复、目标说话人提取和语音分离任务。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#自回归语言模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.20441</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/alibaba/unified-audio/tree/main/QuarkAudio-UniSE" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">alibaba/unified-audio/tree/main/QuarkAudio-UniSE</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.20441" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.20441" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/alibaba/unified-audio/tree/main/QuarkAudio-UniSE" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出UniSE，一个基于解码器自回归语言模型的统一框架，可同时处理语音恢复、目标说话人提取和语音分离任务。
</div>

## 👥 作者与机构

**Haoyin Yan** ¹ · Chengwei Liu · Shaofei Xue · Xiaotao Liang · Yinghao Liu · Yuxiang Kong · Zheng Xue

**机构**：阿里巴巴

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和语音分离领域的研究者阅读。建议重点看§3的模型架构和§4的渐进式强化学习策略。可先看表1和表2的实验结果，再决定是否深入方法细节。

## 🌍 研究背景

神经音频编解码器推动了语言模型在语音应用中的发展，但自回归LM在统一语音增强任务上的有效性尚未充分探索。现有方法多为判别式或生成式模型，针对单一任务设计，缺乏统一框架。本文旨在利用解码器自回归LM处理多种语音增强任务，包括语音恢复、目标说话人提取和语音分离。

## 💡 核心创新

1. 提出UniSE统一框架，用解码器自回归LM处理多种SE任务
2. 渐进式强化学习策略，结合多个评估标准优化语音质量
3. 条件输入语音特征，自回归生成目标离散token

## 🏗️ 模型架构

UniSE采用解码器自回归LM架构。输入为语音特征（如Mel谱或编码器输出），通过条件编码器提取特征，然后输入到Transformer解码器，自回归地生成目标离散token（来自预训练神经音频编解码器的码本）。输出token经解码器恢复为波形。支持多任务通过任务特定条件实现。

## 📚 数据集

- DNS-Challenge（训练/评估，语音恢复）
- Libri2Mix（训练/评估，语音分离）
- WSJ0-2mix（训练/评估，语音分离）
- VCTK（训练/评估，目标说话人提取）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | DNS-Challenge | DEMUCS 3.07 | **3.15** | +0.08 |
| SI-SDR (dB) | Libri2Mix | SepFormer 17.5 | **18.2** | +0.7 |
| SI-SDR (dB) | WSJ0-2mix | SepFormer 22.3 | **22.9** | +0.6 |

UniSE在多个基准上取得有竞争力的性能：在DNS-Challenge上PESQ达3.15，优于DEMUCS；在Libri2Mix和WSJ0-2mix上SI-SDR分别达18.2 dB和22.9 dB，接近SepFormer。渐进式强化学习进一步提升了语音质量。

## 🎯 结论与影响

UniSE证明了自回归语言模型在统一语音增强任务上的潜力，通过单一框架处理语音恢复、目标说话人提取和语音分离，性能接近专用模型。该工作为基于LM的通用语音处理系统提供了新思路，有望推动工业界多任务模型的简化部署。

## ⚠️ 局限与未解决问题

未报告推理延迟和参数量，与轻量级模型对比不足。强化学习策略的收敛稳定性未详细分析。在目标说话人提取任务上仅测试了VCTK，泛化性待验证。

## 🔗 开源资源

- **代码**：<https://github.com/alibaba/unified-audio/tree/main/QuarkAudio-UniSE>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-03/">← 返回 2026-07-03 速递</a></div>
