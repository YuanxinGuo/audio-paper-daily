---
title: "Motion-Aware Reasoning from Speech to Mask Tracks: Runner-up Solution for the MeViS-Audio Track of the 8th LSVOS Challenge 2026"
date: 2026-08-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频目标分割"]
summary: "提出Speech2MaskTrack，结合语音识别、运动感知时间定位与SAM3.1跟踪，在LSVOS挑战赛MeViS-Audio赛道获第二名。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频目标分割</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音引导</span> <span class="tag-pill tag-pill-soft">#视频目标分割</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#挑战赛方案</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.22337</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.22337" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.22337" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Speech2MaskTrack，结合语音识别、运动感知时间定位与SAM3.1跟踪，在LSVOS挑战赛MeViS-Audio赛道获第二名。
</div>

## 👥 作者与机构

**Jinxing Zhou** ¹ · Suiyi Zhao · Yanghao Zhou · Ruohao Guo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事视频目标分割、多模态推理的研究者阅读。可重点看其系统架构（图1）和消融实验（表2），了解如何将语音指令转化为结构化约束并集成多个模型。建议通读全文，但可略过挑战赛细节。

## 🌍 研究背景

语音引导的指代视频目标分割旨在根据口语描述恢复目标物体的掩码轨迹。与基于声学线索的语音分离不同，这里语音是语言指令，需连接语音识别、运动中心的时间定位、掩码跟踪和显式无目标处理。现有方法多依赖文本查询，而语音引入ASR误差和口语歧义。挑战赛要求处理运动描述，需同时考虑类别、数量、方向、交互角色和时间阶段。

## 💡 核心创新

1. 将语音查询转写并编译为结构化约束（类别、数量、方向等）
2. 利用SAM3.1枚举多实例轨迹，TRACE基于完整轨迹运动与关系排序
3. 引入冻结词汇存在门控，抑制无目标时的基础预测
4. GPT辅助恢复流程，结合查询级和掩码级验证
5. 集成SaSaSa2VA全表达式条件跟踪，提升精度

## 🏗️ 模型架构

输入为语音查询和视频帧。首先ASR转写语音，并编译为结构化约束（类别、数量、方向、交互角色、时间阶段）。SAM3.1生成多个实例轨迹，TRACE根据完整轨迹的运动和关系证据对轨迹排序。冻结的词汇存在门控判断目标是否存在，若存在则使用SaSaSa2VA的跟踪结果替换SAM3.1掩码。若输出为空，则进入GPT辅助恢复，再次调用SaSaSa2VA并进行查询和掩码级验证。

## 📚 数据集

- MeViS-Audio（训练/验证/测试，挑战赛数据集）

## 📊 实验结果

摘要未提供具体数值指标，仅说明在官方挑战赛排名第二。未提及消融实验或跨数据集泛化结果。

## 🎯 结论与影响

Speech2MaskTrack通过结合语音识别、运动感知时间定位和多个分割模型，有效解决了语音引导的视频目标分割任务，在挑战赛中取得第二名。该方法展示了多模态融合和结构化约束的潜力，对后续研究具有参考价值，并可能推动视频编辑、人机交互等应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。作为审稿人，可能存在的问题包括：依赖ASR准确性，错误传播；多个模型集成导致计算开销大；未提供详细消融和效率分析；挑战赛方案可能针对特定数据集过拟合。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-26/">← 返回 2026-08-26 速递</a></div>
