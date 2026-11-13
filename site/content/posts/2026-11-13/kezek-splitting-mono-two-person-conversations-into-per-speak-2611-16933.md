---
title: "Kezek: Splitting Mono Two-Person Conversations into Per-Speaker Tracks for Full-Duplex Dialogue Data"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "Kezek 将单声道双人对话拆成每人一条等长音轨，两阶段：指纹引导的双声活动检测定决策，条件时域分离器执行，输出严格可加。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#双说话人对话</span> <span class="tag-pill tag-pill-soft">#全双工对话数据</span> <span class="tag-pill tag-pill-soft">#说话人日志</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.16933</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.16933" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.16933" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Kezek 将单声道双人对话拆成每人一条等长音轨，两阶段：指纹引导的双声活动检测定决策，条件时域分离器执行，输出严格可加。
</div>

## 👥 作者与机构

**Bagzhan Karl** ¹ · Alizhan Karl

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工对话数据、双人分离与对话数据清洗的研究者与工程团队阅读。建议通读，重点看 §3 两阶段设计与 §4 自定义指标（短回复保留率、泄漏、通道互换、覆盖率），并核对表 2 与 CallHome 泛化结果；负结果与理想掩码上限部分值得细读以判断剩余差距。

## 🌍 研究背景

全双工语音对话模型依赖每人一通道的对话录音来学习轮次转换、重叠与反馈语，但公开对话音频多为单声道混音。传统做法是 pyannote 说话人日志接 DialogueSidon 等分离器，但该流水线会丢弃部分录音、短回复保留差、通道互换多、速度慢。本文要解决的是：在恰好两人的单声道录音上，稳定产出与原录音等长、时序对齐的每人音轨，并保留重叠与短回复。

## 💡 核心创新

1. 两阶段解耦：先由双声活动模型加说话人指纹做全局“谁在何时说、谁是谁”的决策
2. 指纹训练对相位不敏感，提升说话人归属鲁棒性
3. 条件时域分离器只执行决策，输出严格求和等于输入
4. 面向对话数据提出短回复保留率、泄漏、通道互换、覆盖率等指标

## 🏗️ 模型架构

输入为单声道双人对话波形。第一阶段用双声活动模型（two-voice activity）结合说话人指纹，对整段录音一次性判定两路活动与说话人身份映射，指纹经训练对相位不敏感。第二阶段为条件时域分离器，以第一阶段决策为条件，在时域直接估计两路波形，输出被约束为逐样本求和等于输入混合，从而保证无残留、无新增成分。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- Open Yap（评估，双人对话测试集）
- CallHome English（评估，未见电话语音泛化）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 短回复保留率 | Open Yap test | pyannote→DialogueSidon 0.69 | **0.83** | +0.14 |
| 短回复保留率（对方语音上） | CallHome English | pyannote→DialogueSidon 0.71 | **0.80** | +0.09 |
| 短回复保留率（两者均返回的音频） | Open Yap | 0.865 | **0.859** | -0.006 |
| 推理速度（每小时 GPU 处理音频时长） | — | 外部流水线 | **约 230 小时/GPU 小时** | 快 4-5 倍 |

在 Open Yap 与未见电话语音 CallHome English 上，Kezek 的短回复保留率均高于 pyannote→DialogueSidon，主要收益来自返回整段录音而外部流水线丢弃部分音频；在两者都返回的音频上保留率基本持平（0.859 vs 0.865）。此外泄漏更少、通道互换更少、速度快 4-5 倍。作者还报告负结果与理想掩码上限，指出剩余差距集中在“较响声音下的轻声回复”。

## 🎯 结论与影响

最强结论是：把“谁在何时说、谁是谁”的全局决策与波形分离解耦，可在单声道双人对话上稳定保留短回复与重叠，并显著提速。这为全双工对话数据构建提供了可复现的替代流水线，对工业界清洗真实对话录音有直接价值。

## ⚠️ 局限与未解决问题

仅支持恰好两人的单声道录音，多人或单说话人场景未覆盖；自定义指标与外部流水线不完全可比（返回音频范围不同）；未报告 SI-SDR 等标准分离指标与推理延迟细节；轻声回复在较响声音下仍是主要失败模式，理想掩码上限表明仍有提升空间。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
