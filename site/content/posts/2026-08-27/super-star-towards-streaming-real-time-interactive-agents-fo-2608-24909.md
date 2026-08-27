---
title: "Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans"
date: 2026-08-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#共语手势生成"]
summary: "提出流式共语手势生成框架，结合流式语音响应与在线手势生成，实现低延迟、语音同步的实时交互数字人。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#共语手势生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#数字人</span> <span class="tag-pill tag-pill-soft">#自进化训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.24909</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://super-star-2026.github.io/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">super-star-2026.github.io/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.24909" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.24909" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://super-star-2026.github.io/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出流式共语手势生成框架，结合流式语音响应与在线手势生成，实现低延迟、语音同步的实时交互数字人。
</div>

## 👥 作者与机构

**Wentao Jiang** ¹ · Youchen Xie · Haidi Fan · Yajing Chen · Xin Wang · Ye Shi · Jingya Wang

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合数字人、多模态交互、生成式AI研究者。重点看第3节（方法）和第4节（实验）。先看§3.2的因果多模态自回归模型和§3.3的数据合成流程，再对照表2的延迟-质量对比。

## 🌍 研究背景

现有共语手势生成多在离线设置下研究，依赖完整语音片段，无法满足实时交互的延迟要求。先前方法要么需要未来语音信息，要么推理延迟高，不适合在线应用。本文旨在解决实时交互数字人的在线共语手势生成问题，提出流式框架。

## 💡 核心创新

1. 因果多模态自回归模型，仅用当前语音和运动历史预测手势
2. 面向虚拟伴侣场景的离线数据合成流程，主题和情感感知
3. 自进化训练循环，利用在线用户反馈持续优化数据生成
4. 流式语音响应与在线手势生成耦合的实时交互框架
5. 在延迟-质量权衡、语音-运动同步和用户偏好上超越基线

## 🏗️ 模型架构

输入为流式响应语音特征和运动历史，通过因果多模态自回归模型预测身体运动。模型采用自回归方式，每个时间步基于当前语音和先前运动生成手势，无需未来信息。具体网络结构未详述，但强调因果性和多模态融合。输出为连续的身体运动序列。

## 📚 数据集

- 虚拟伴侣对话数据集（训练，由合成流程生成）
- 在线交互用户反馈数据（训练，自进化循环）
- 评估数据集（评估，未具体说明）

## 📊 实验结果

摘要未提供具体数值，但声称在延迟-质量权衡、语音-运动同步和用户偏好上优于现有基线。实验包括离线评估和在线用户研究，但具体指标未给出。

## 🎯 结论与影响

本文提出首个流式共语手势生成框架，实现低延迟、语音同步的实时交互。通过因果建模和自进化训练，显著提升用户体验。对数字人交互领域有重要影响，为在线手势生成提供了新范式，有望推动实时虚拟助手和游戏角色的自然交互。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题：因果模型可能牺牲手势质量；数据合成流程依赖虚拟伴侣场景，泛化性未知；自进化循环需要在线部署，可能引入冷启动问题；未报告具体延迟数值和计算开销。

## 🔗 开源资源

- **项目主页**：<https://super-star-2026.github.io/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-27/">← 返回 2026-08-27 速递</a></div>
