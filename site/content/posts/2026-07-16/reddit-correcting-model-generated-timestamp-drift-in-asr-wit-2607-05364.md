---
title: "REDDIT: Correcting Model-Generated Timestamp Drift in ASR without Forgetting via Replay-Based Distribution Editing"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出REDDIT框架，通过重放式分布编辑纠正ASR模型生成的时间戳漂移，避免灾难性遗忘。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#时间戳漂移</span> <span class="tag-pill tag-pill-soft">#遗忘问题</span> <span class="tag-pill tag-pill-soft">#重放编辑</span> <span class="tag-pill tag-pill-soft">#语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.05364</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.05364" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.05364" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出REDDIT框架，通过重放式分布编辑纠正ASR模型生成的时间戳漂移，避免灾难性遗忘。
</div>

## 👥 作者与机构

**Cheng-Kang Chou** ¹ · Ming-To Chuang · Ke-Han Lu · Chan-Jan Hsu · Hung-yi Lee

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR时间戳相关研究者。建议重点阅读§3方法部分和§4实验，特别是表2和表3。可先看§3.2的编辑阶段和§3.3的微调阶段。

## 🌍 研究背景

现代自回归ASR系统可直接解码时间戳，但长非语音段会导致时间戳漂移，转录看似合理但时间轴偏离音频。现有微调方法虽能改善对齐，但会严重退化非目标ASR行为，引发遗忘问题。本文旨在纠正时间戳漂移同时避免灾难性遗忘。

## 💡 核心创新

1. 提出REDDIT两阶段后训练框架
2. 利用重放解码上下文编辑时间戳目标
3. 结合VAD和已知拼接偏移构造纠正监督
4. 仅更新1.6%参数，高效纠正漂移

## 🏗️ 模型架构

输入音频特征→Whisper-tiny自回归解码器→REDDIT框架：第一阶段编辑时间戳目标，在模型自身重放解码上下文中匹配冻结基分布的非时间戳token；第二阶段短编辑前缀微调。仅更新解码器部分参数（1.6%）。

## 📚 数据集

- 自建gap基准（训练/评估，含非语音间隔）
- 自建long-gap基准（评估，长非语音段）
- CV-en（评估，通用语音识别）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| mIoU | long-gap基准 | 原始Whisper-tiny 38.7% | **95.0%** | +56.3% |
| AAS | 混合gap域外 | 原始Whisper-tiny 2752 ms | **223 ms** | -2529 ms |
| MER | CV-en | 原始Whisper-tiny 41.3% | **41.3%** | 0% |

在Whisper-tiny上，REDDIT使用34.9小时纠正音频，仅更新1.6%参数，将长间隙mIoU从38.7%提升至95.0%，混合间隙域外AAS从2752ms降至223ms，同时保持CV-en MER为41.3%（普通SFT解码器调优导致MER升至524.2%）。

## 🎯 结论与影响

REDDIT有效纠正ASR时间戳漂移且不牺牲识别性能，仅需少量参数更新。该方法为时间戳后处理提供了轻量级解决方案，有望推广至其他自回归ASR系统，对工业实时转录场景有实用价值。

## ⚠️ 局限与未解决问题

仅在Whisper-tiny上验证，未测试更大模型；纠正监督依赖VAD和拼接偏移，可能引入额外误差；未报告推理延迟；缺乏与其他后处理方法（如CTC对齐）的对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-16/">← 返回 2026-07-16 速递</a></div>
