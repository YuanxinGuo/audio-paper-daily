---
title: "Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音编辑检测"]
summary: "提出基于音频大语言模型的统一框架，将语音编辑检测与内容定位重构为结构化文本生成任务，并引入先验增强提示和声学一致性损失。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音编辑检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频大语言模型</span> <span class="tag-pill tag-pill-soft">#语音编辑检测</span> <span class="tag-pill tag-pill-soft">#内容定位</span> <span class="tag-pill tag-pill-soft">#生成式方法</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2601.21463</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/datasets/JunXueTech/AiEdit" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 datasets/JunXueTech/AiEdit</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2601.21463" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2601.21463" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/datasets/JunXueTech/AiEdit" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于音频大语言模型的统一框架，将语音编辑检测与内容定位重构为结构化文本生成任务，并引入先验增强提示和声学一致性损失。
</div>

## 👥 作者与机构

**Jun Xue** ¹ · Yi Chai · Yanzhen Ren · Jinshen He · Zhiqiang Tang · Zhuolin Yi · Yihuan Huang · Yuankun Xie · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音编辑检测、音频取证和音频大语言模型研究者阅读。建议重点读§3方法部分（先验增强提示和声学一致性损失）及§4实验（表1-3对比结果）。可先看§1引言了解问题动机。

## 🌍 研究背景

现有语音编辑检测数据集多依赖手动拼接或有限编辑操作，多样性不足且难以覆盖真实编辑场景。当前方法依赖帧级监督检测可观测声学异常，对删除型编辑（操作内容完全从信号中消失）处理能力有限。本文旨在通过生成式框架统一检测与定位，解决上述问题。

## 💡 核心创新

1. 构建大规模双语数据集AiEdit（约140小时），覆盖增删改操作
2. 将SED重构为结构化文本生成任务，联合推理编辑类型与内容定位
3. 提出先验增强提示策略，注入帧级检测器的词级概率线索
4. 引入声学一致性损失，在隐空间分离正常与异常声学表征

## 🏗️ 模型架构

输入音频特征经Audio LLM编码器提取表征，结合先验增强提示（来自帧级检测器的词级概率）注入LLM解码器，输出结构化文本（编辑类型、位置等）。训练时使用声学一致性损失，在隐空间拉近正常音频表征、推远异常表征。

## 📚 数据集

- AiEdit（训练/评估，约140小时，双语，含增删改操作）
- 现有SED基准数据集（评估，如In-the-Wild等）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 检测F1 | AiEdit测试集 | 基线方法（如帧级分类器）约0.85 | **0.92** | +0.07 |
| 定位IoU | AiEdit测试集 | 基线方法约0.70 | **0.78** | +0.08 |

在AiEdit数据集上，所提方法在检测F1和定位IoU上均优于现有方法，消融实验验证了先验增强提示和声学一致性损失的有效性。跨数据集泛化测试显示方法在真实场景下仍保持优势。

## 🎯 结论与影响

本文通过生成式框架统一语音编辑检测与内容定位，显著提升对删除型编辑的检测能力。AiEdit数据集为后续研究提供更真实的基准。该方法有望推动音频取证领域向更鲁棒的生成式检测方向发展。

## ⚠️ 局限与未解决问题

依赖Audio LLM的推理能力，计算开销较大；未报告推理延迟；AiEdit数据集虽规模大，但编辑操作由特定系统生成，可能仍存在领域偏差；对极短编辑的定位精度有待提升。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/datasets/JunXueTech/AiEdit>
- **数据集**：<https://huggingface.co/datasets/JunXueTech/AiEdit>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-26/">← 返回 2026-05-26 速递</a></div>
