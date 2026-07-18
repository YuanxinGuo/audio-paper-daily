---
title: "Towards Out-of-Distribution Detection in Vocoder Recognition via Latent Feature Reconstruction"
date: 2026-07-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#深度伪造检测"]
summary: "提出基于自编码器重构的声码器识别中OOD检测方法，利用WavLM特征和对比学习提升检测精度。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声码器识别</span> <span class="tag-pill tag-pill-soft">#异常检测</span> <span class="tag-pill tag-pill-soft">#自编码器</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2406.02233</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2406.02233" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2406.02233" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于自编码器重构的声码器识别中OOD检测方法，利用WavLM特征和对比学习提升检测精度。
</div>

## 👥 作者与机构

**Renmingyue Du** ¹ · Jixun Yao · Qiuqiang Kong · Yin Cao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频深度伪造检测、OOD检测的研究者阅读。建议重点看§3方法部分和§4实验部分，尤其是对比约束和辅助分类器的消融实验。可先看表1和表2了解性能提升。

## 🌍 研究背景

合成语音技术的进步带来了冒充威胁，深度伪造算法识别变得重要。其中，分布外（OOD）检测是关键环节，但现有方法多基于概率分数或分类距离，在阈值边缘样本上精度有限。本文旨在通过重构方法提高OOD检测的准确性。

## 💡 核心创新

1. 采用自编码器架构重构WavLM声学特征
2. 每个声码器类别对应独立解码器，仅重构本类特征
3. 引入对比学习增强解码器重构特征的区分性
4. 添加辅助分类器进一步约束重构特征
5. 在评估集上相对基线提升10%

## 🏗️ 模型架构

输入为预训练WavLM模型提取的声学特征，送入自编码器。编码器压缩特征，多个解码器分别对应不同声码器类别，每个解码器仅重构属于其类别的特征。若所有解码器均无法满意重构，则判定为OOD样本。训练中引入对比损失和辅助分类损失以增强特征区分性。

## 📚 数据集

- 评估数据集（未具名，用于评估OOD检测性能）

## 📊 实验结果

实验表明，所提方法在评估数据集上相对基线系统有10%的相对提升。消融研究验证了对比约束和辅助分类器的有效性。摘要未提供具体指标数值。

## 🎯 结论与影响

本文提出的基于重构的OOD检测方法在声码器识别中有效，通过自编码器和对比学习提升了检测精度。该方法为深度伪造检测提供了新思路，有望应用于实际语音安全系统。

## ⚠️ 局限与未解决问题

摘要未提及具体数据集名称和规模，缺乏与更多基线方法的对比，未报告推理延迟或计算开销。此外，方法依赖预训练WavLM模型，可能引入领域偏差。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-07-18/">← 返回 2026-07-18 速递</a></div>
