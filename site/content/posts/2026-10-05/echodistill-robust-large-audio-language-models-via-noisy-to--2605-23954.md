---
title: "EchoDistill: Robust Large Audio Language Models via Noisy-to-Clean Self-Distillation"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "EchoDistill 用干净音频作特权信息做噪声到干净自蒸馏，提升 LALM 在 -10dB 加性噪声下的任务准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自蒸馏</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23954</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23954" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23954" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>EchoDistill 用干净音频作特权信息做噪声到干净自蒸馏，提升 LALM 在 -10dB 加性噪声下的任务准确率。
</div>

## 👥 作者与机构

**Kaiwen Luo** ¹ · Chunxi Luo · Liang Lin · Yuxuan Li · Zhenhong Zhou · Junhao Dong · Yingjie Zhou · Zhendong Chu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大音频语言模型鲁棒性、语音前端与 LALM 结合的研究者阅读。建议重点看 §3 的 masked response-token distillation 与 task-gated consistency shaping 设计，以及表 2 的 -10dB 三域结果和随机/静音替换消融。若关注推理成本，可先看其“仅保留 student”的部署说明。

## 🌍 研究背景

大音频语言模型（LALM）在音频理解任务上进展迅速，但现有模型对加性噪声敏感，噪声会掩盖任务相关声学证据，导致回答不可靠。此前工作多依赖数据增强或前端语音增强级联，前者难以覆盖真实噪声分布，后者会引入额外推理开销与信息损失。本文关注如何在训练后阶段利用干净音频作为特权信息，在不增加推理成本的前提下提升噪声输入下的鲁棒性。

## 💡 核心创新

1. 噪声输入 student 与冻结干净音频 teacher 的同骨干自蒸馏
2. masked response-token distillation 对齐噪声与干净语义
3. task-gated consistency shaping 按任务门控一致性
4. teacher-referenced group-relative optimization 优化生成

## 🏗️ 模型架构

输入为同一段音频的含噪版本与干净版本，分别送入同一 LALM 骨干：student 处理含噪音频并采样候选回答，teacher 为冻结副本处理干净音频。训练目标由三部分组成：对回答 token 做掩码蒸馏、按任务类型门控的一致性塑形、以及以 teacher 为参考的组相对优化。推理时仅保留 student，不引入额外计算。摘要未给出参数量，实验覆盖三个 LALM 骨干与三个音频域。

## 📚 数据集

- 三个音频域数据集（训练与评估，摘要未具名）
- 外部基准（评估，摘要未具名）
- held-out 加性噪声（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 噪声输入准确率 | 三个音频域平均（-10dB） | 最强基线 | **+1.63 个百分点** | +1.63 |
| 噪声输入准确率 | Qwen2.5-Omni | 59.33% | **62.94%** | +3.61 |
| 干净音频准确率 | Qwen2.5-Omni | 76.56% | **77.56%** | +1.00 |
| 准确率下降 | 随机/打乱/静音替换音频 | 匹配音频 | **下降 3.08-6.42 点** | -3.08~-6.42 |

在三个 LALM 骨干、三个音频域、-10dB 加性噪声下，EchoDistill 平均噪声输入准确率比最强基线高 1.63 个百分点；Qwen2.5-Omni 上从 59.33% 提升到 62.94%，干净音频准确率也从 76.56% 升到 77.56%。将匹配音频替换为随机、打乱或静音输入会掉 3.08-6.42 点，说明模型确实依赖匹配声学证据。在 held-out 加性噪声与外部基准上也有提升，但非加性失真上增益不可靠。

## 🎯 结论与影响

本文最强结论是：以干净音频为特权信息的噪声到干净自蒸馏，可在不增加推理成本的情况下显著提升 LALM 在严重加性噪声下的任务准确率，且不牺牲干净音频能力。这为 LALM 鲁棒后训练提供了可复用范式，后续可探索非加性失真与更多音频域。工业上意味着无需改推理栈即可部署更抗噪的音频大模型。

## ⚠️ 局限与未解决问题

摘要承认增益不能可靠迁移到非加性失真；未报告推理延迟、显存与训练成本；未给出具体数据集名称与参数量，复现细节不足；对比基线仅称“最强基线”，缺少与前端语音增强级联方案的直接比较；三个音频域的具体构成与噪声类型未说明，存在域偏置风险。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-05/">← 返回 2026-10-05 速递</a></div>
