---
title: "ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频字幕生成"]
summary: "提出ACE-Cap框架，将长段落细粒度音频字幕生成建模为主动证据获取过程，通过Composer与Instruct模型的多轮交互和LOOP-GRPO训练，实现自适应查询与终止。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频字幕生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频字幕生成</span> <span class="tag-pill tag-pill-soft">#主动证据获取</span> <span class="tag-pill tag-pill-soft">#多轮交互</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.16162</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.16162" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.16162" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出ACE-Cap框架，将长段落细粒度音频字幕生成建模为主动证据获取过程，通过Composer与Instruct模型的多轮交互和LOOP-GRPO训练，实现自适应查询与终止。
</div>

## 👥 作者与机构

**Fengji Ma** ¹ · Yan Rong · Xu Li · Xuenan Xu · Chen Zhang · Li Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频字幕生成、多模态交互和强化学习研究者阅读。建议重点阅读第3节方法部分，特别是LOOP-GRPO的信用分配机制和第4节实验设置。可先看图1和表2了解整体框架和主要结果。

## 🌍 研究背景

长段落细粒度音频字幕生成要求模型恢复多样声学事实，避免遗漏和幻觉。现有字幕生成器多为被动单次生成，一旦遗漏细节无法主动查询音频或决定何时停止。本文将该任务形式化为主动证据获取，通过多轮交互闭环解决证据缺口问题。

## 💡 核心创新

1. 提出ACE-Cap框架，将字幕生成转化为主动证据获取过程
2. 设计Composer与Instruct模型的多轮交互机制，形成闭环证据获取
3. 提出LOOP-GRPO训练方法，利用跨度对齐信号进行信用分配
4. 角色交替优化策略，实现Composer和Instruct的协同进化

## 🏗️ 模型架构

ACE-Cap包含三个角色：Captioner、Composer和Instruct模型。Captioner首先生成初始描述；Composer基于描述和交互历史，以文本形式提出关于未解析声学属性的目标问题；Instruct模型以音频为条件提供基于证据的答案。Composer决定何时终止并综合累积证据生成最终字幕。训练采用统一的金标到预测奖励，基于固定金标多选题和冻结的字幕评判器。LOOP-GRPO通过留一法贡献、质量-成本效用和证据保留效用进行信用分配。

## 📊 实验结果

摘要未提供具体实验数据，但表明ACE-Cap在长段落细粒度音频字幕生成任务上优于现有被动单次生成方法，通过主动证据获取减少了遗漏和幻觉。

## 🎯 结论与影响

ACE-Cap将音频字幕生成从被动单次生成转变为自适应过程，学习获取什么证据、何时停止以及如何在长段落中保留证据。该方法有望推动音频字幕生成向更主动、更可靠的方向发展，对自动音频内容描述和辅助听觉系统有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：依赖金标多选题的构建成本，冻结评判器的泛化性，以及多轮交互带来的推理延迟。此外，未报告在标准数据集上的定量结果，缺乏与现有方法的直接对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-25/">← 返回 2026-08-25 速递</a></div>
