---
title: "Liberating LLM Capabilities in Full-Duplex Speech Models"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "提出 Listen-Write-Speak 三通道范式，让单一自回归 LLM 在共享因果注意力下同时听、写可见文本、并行说话，无需改架构。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音交互</span> <span class="tag-pill tag-pill-soft">#语音大模型</span> <span class="tag-pill tag-pill-soft">#多模态输出</span> <span class="tag-pill tag-pill-soft">#Token Schema</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.07547</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://royalzhang.com/project/lws-page/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">royalzhang.com/project/lws-page/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.07547" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.07547" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://royalzhang.com/project/lws-page/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 Listen-Write-Speak 三通道范式，让单一自回归 LLM 在共享因果注意力下同时听、写可见文本、并行说话，无需改架构。
</div>

## 👥 作者与机构

**Luoyuan Zhang** ¹ · Bokai Xu · Junbo Cui · Weiyue Sun · Yingjing Xu · Hanyu Liu · Yuan Yao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工语音对话、语音 LLM 输出通道设计的研究者与工程团队阅读。建议重点看 Token Schema 定义与两阶段数据合成管线，以及 Full-Duplex-Bench 与 URO-Bench 的消融对比。若只关心语音增强/分离，可略读。

## 🌍 研究背景

语音 LLM 通常被限制为口语回复，输出只能被言语化，抑制了代码生成、结构化分析、多步推理等文本原生能力，而这些任务需要持久、结构化、可检查的中间输出。已有工作改进口语推理或全双工轮次切换，但仍把文本当作隐藏中间态或从属模态，而非一等输出通道。本文要解决的是：如何在不牺牲实时响应性的前提下，让可见书写成为语音交互的一等输出通道。

## 💡 核心创新

1. 提出 Listen-Write-Speak 文本优先三通道范式，听/写/说并行
2. 用 Token Schema 实现，无需任何架构修改
3. 两阶段数据管线合成逐秒认知标注，对齐输入时间线
4. 共享因果注意力上下文统一三通道输出

## 🏗️ 模型架构

输入为用户连续音频流，经语音编码后送入单一自回归 LLM 主干。模型在共享因果注意力上下文中同时产生三类 token：听（持续接收用户音频）、写（可见自由文本作为主输出）、说（实时口语回复）。三通道通过 Token Schema 区分，无需改动网络结构。训练采用两阶段数据管线，合成与输入时间线一致的逐秒认知标注。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- Full-Duplex-Bench（评估，全双工交互）
- VoiceBench AlpacaEval（评估，指令跟随）
- URO-Bench（评估，消融对比）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| VoiceBench AlpacaEval | VoiceBench AlpacaEval | 未给出 | **4.72** | 未给出 |
| 写作-说话一致性 | 内部评估 | 未给出 | **92.6%** | 未给出 |

摘要报告 LWS 在 Full-Duplex-Bench 上展现强全双工交互，VoiceBench AlpacaEval 达 4.72，写作-说话一致性 92.6%，并在 URO-Bench 上持续优于内部消融。但摘要未给出与外部强基线的具体对比数值，也未报告推理延迟、吞吐等效率指标，实验细节需查阅正文。

## 🎯 结论与影响

最强结论是可见书写可作为语音交互的一等输出通道而不牺牲实时响应性。这为语音 LLM 输出通道设计提供了新范式，可能推动后续研究将结构化文本输出纳入全双工对话系统。工业上对需要可检查中间输出的实时语音助手、编程辅助等场景有潜在价值。

## ⚠️ 局限与未解决问题

摘要未给出与外部 SOTA 的定量对比，仅与内部消融比较，说服力有限；未报告推理延迟、显存与吞吐等实时性关键指标；92.6% 一致性指标定义与评测方式不明；三通道并行输出可能带来 token 预算与延迟权衡，摘要未讨论。

## 🔗 开源资源

- **项目主页**：<https://royalzhang.com/project/lws-page/>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
