---
title: "MindMelody: A Closed-Loop EEG-Driven System for Personalized Music Intervention"
date: 2026-05-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出MindMelody，一个基于EEG的闭环实时系统，通过情感介导语义桥实现个性化音乐干预。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脑电信号</span> <span class="tag-pill tag-pill-soft">#情感计算</span> <span class="tag-pill tag-pill-soft">#闭环系统</span> <span class="tag-pill tag-pill-soft">#个性化音乐干预</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.01235</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.01235" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.01235" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MindMelody，一个基于EEG的闭环实时系统，通过情感介导语义桥实现个性化音乐干预。
</div>

## 👥 作者与机构

**Yimeng Zhang** ¹ · Yueru Sun · Haoyu Gu · Zhanpeng Jin

**机构**：纽约州立大学布法罗分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合脑机接口、音乐生成、情感计算领域研究者。建议重点阅读§3系统架构和§4实验部分，尤其是情感对齐和反馈机制。可先看Fig.2系统流程图。

## 🌍 研究背景

音乐干预作为非侵入式情绪调节手段受到关注，但现有数字音乐服务依赖静态偏好，无法适应实时心理状态。直接映射EEG到音乐生成面临配对数据稀缺和可解释性差的问题。本文旨在构建一个闭环系统，通过EEG解码情感状态并驱动音乐生成，实现个性化干预。

## 💡 核心创新

1. 提出情感介导语义桥，将EEG解码为Valence-Arousal状态
2. 混合Transformer-GNN解码实时EEG信号
3. RAG增强的LLM生成结构化干预计划
4. 层次化EEG控制器注入全局和局部情感引导
5. 连续反馈循环动态更新生成参数

## 🏗️ 模型架构

输入为实时EEG信号，经混合Transformer-GNN解码为全局Valence-Arousal状态和局部时间情感轨迹。这些状态输入RAG增强的LLM生成结构化干预计划。然后，层次化EEG控制器将全局情感前缀和局部时间引导注入预训练音乐骨干网络（如MusicGen），实现可控音频合成。系统包含连续反馈循环，根据用户EEG动态更新生成参数。

## 📚 数据集

- DEAP（训练EEG解码器）
- 自建EEG-音乐配对数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 情感对齐准确率 | 自建测试集 | 无控制基线 0.52 | **0.78** | +0.26 |
| 感知帮助度评分 | 用户研究 | 静态音乐 3.2/5 | **4.1/5** | +0.9 |

实验表明，MindMelody在情感对齐和用户感知帮助度上显著优于静态音乐基线。消融研究验证了各模块的有效性，反馈循环进一步提升了实时适应性。但缺乏与现有EEG驱动音乐生成方法的直接对比。

## 🎯 结论与影响

MindMelody通过闭环EEG驱动实现了实时个性化音乐干预，在情感对齐和用户满意度上表现优异。该工作为情感感知音乐生成提供了新范式，有望推动数字心理健康干预的发展。

## ⚠️ 局限与未解决问题

实验仅在短期聆听场景下评估，长期效果未知；用户研究样本量较小；未报告系统延迟和计算开销；缺乏与现有EEG-to-music方法的定量对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-19/">← 返回 2026-05-19 速递</a></div>
