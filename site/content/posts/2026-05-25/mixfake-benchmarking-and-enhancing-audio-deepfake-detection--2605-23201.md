---
title: "MixFake: Benchmarking and Enhancing Audio Deepfake Detection in Diverse Real-world Mixed Audio"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出MixFake基准数据集和多流提示微调框架，在混合音频深度伪造检测中显著提升复杂背景下的性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#多流提示微调</span> <span class="tag-pill tag-pill-soft">#混合音频</span> <span class="tag-pill tag-pill-soft">#基准数据集</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23201</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/saltfish233/MixFake" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">saltfish233/MixFake</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23201" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23201" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/saltfish233/MixFake" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MixFake基准数据集和多流提示微调框架，在混合音频深度伪造检测中显著提升复杂背景下的性能。
</div>

## 👥 作者与机构

**Qingcao Li** ¹ · Yipeng Lin · Weichen Lian · Zhongjie Ba · Peng Cheng · Zhichao Lian

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频伪造检测、自监督学习领域的研究者。建议重点阅读第3节（MixFake数据集构建）和第4节（多流提示微调框架），以及表1-3的实验结果。可先看§4.2的模型架构图。

## 🌍 研究背景

当前语音深度伪造检测在干净环境下表现优异，但真实场景中语音常与背景音乐或噪声混合，现有基于自监督学习（SSL）语义特征的方法在处理非语音或混合源音频时失效。本文旨在解决这一痛点，通过构建大规模混合音频基准数据集MixFake，并提出注入信号级先验的多流提示微调框架，提升复杂环境下的检测鲁棒性。

## 💡 核心创新

1. 构建MixFake大规模混合音频基准数据集
2. 提出多流提示微调框架注入信号级先验
3. 设计基、频率、纹理三流深度提示注入
4. 在复杂背景检测中实现7.72%绝对EER提升

## 🏗️ 模型架构

输入为混合音频的log-mel谱图。主干网络采用预训练SSL模型（如WavLM），通过多流提示微调框架注入信号级先验：基流（base stream）保留原始SSL特征，频率流（frequency stream）提取频域伪影，纹理流（texture stream）捕捉时频纹理。三流通过深度提示注入（deep prompt injection）融合，最终输出二分类（真/假）结果。模型参数量未提及。

## 📚 数据集

- MixFake（训练/评估，大规模混合音频，含不同SNR和混合成分）
- ASVspoof2019（评估，用于对比）
- In-the-Wild（评估，用于对比）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER (%) | MixFake前景检测 | WavLM+Linear 1.23 | **0.95** | -0.28% |
| EER (%) | MixFake复杂背景检测 | WavLM+Linear 16.85 | **9.13** | -7.72% |

在MixFake基准上，所提方法在前景检测中EER为0.95%，优于基线WavLM+Linear的1.23%；在复杂背景检测中EER为9.13%，相比基线16.85%绝对提升7.72%。在ASVspoof2019和In-the-Wild等标准数据集上也取得一致改进，消融实验验证了三流融合的有效性。

## 🎯 结论与影响

本文通过MixFake数据集和多流提示微调框架，显著提升了混合音频场景下的深度伪造检测性能，尤其复杂背景检测。该工作为真实世界音频伪造检测提供了新基准和有效方法，有望推动工业级部署，如语音助手和声纹认证系统的鲁棒性增强。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理延迟，可能影响实时部署评估；MixFake数据集仅包含音乐和噪声混合，未涵盖其他干扰（如混响、多人语音）；实验仅在EER指标上对比，缺乏其他指标（如t-DCF）的验证；未与最新端到端方法（如AASIST）在标准集上对比。

## 🔗 开源资源

- **代码**：<https://github.com/saltfish233/MixFake>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
