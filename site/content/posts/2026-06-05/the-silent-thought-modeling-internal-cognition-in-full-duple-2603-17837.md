---
title: "The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#全双工语音对话"]
summary: "提出FLAIR方法，在用户说话时通过潜在推理模拟内部认知，实现全双工语音对话中的实时思考。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#全双工语音对话</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#潜在推理</span> <span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#语音理解</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.17837</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.17837" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.17837" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FLAIR方法，在用户说话时通过潜在推理模拟内部认知，实现全双工语音对话中的实时思考。
</div>

## 👥 作者与机构

**Donghang Wu** ¹ · Tianyu Zhang · Yuxin Li · Hexin Liu · Chen Chen · Eng Siong Chng · Yoshua Bengio

**机构**：南洋理工大学 · 蒙特利尔大学 · Mila研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音对话系统、全双工交互研究者。重点读§3方法设计和§4实验。建议先看§3.2的潜在推理机制和§4.2的全双工指标。

## 🌍 研究背景

全双工语音对话系统要求模型在听的同时思考，但现有方法要么依赖后处理推理引入延迟，要么无法严格遵循因果性。人类在对话中会进行内部认知处理，受此启发，本文提出在语音感知过程中进行潜在推理，避免额外延迟。

## 💡 核心创新

1. 提出FLAIR潜在推理框架，递归更新潜在嵌入
2. 设计ELBO目标实现教师强制训练，无需显式推理标注
3. 实现听与思考并行，严格遵循因果性
4. 在全双工交互指标上取得竞争性能

## 🏗️ 模型架构

输入语音特征经编码器得到潜在嵌入，递归地将其作为下一步输入，形成连续推理链。解码器基于最终潜在嵌入生成响应。训练采用ELBO目标，通过教师强制优化。

## 📚 数据集

- 未在摘要中明确指定数据集

## 📊 实验结果

摘要未提供具体数值，但声称在多个语音基准上取得竞争结果，并在全双工交互指标上表现稳健。

## 🎯 结论与影响

FLAIR通过潜在推理实现听与思考并行，为全双工语音对话提供新范式。有望推动更自然的人机交互，减少响应延迟。

## ⚠️ 局限与未解决问题

未报告具体数据集和指标，缺乏与现有方法的定量对比。潜在推理的可解释性不足，且未讨论计算开销。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
