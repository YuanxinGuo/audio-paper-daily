---
title: "DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "提出DuplexAgent全双工语音协作系统，用六个可编辑模块编排对话与异步委派，并以Duplex-Harness-RSI闭环从交互轨迹自动修复模块。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音交互</span> <span class="tag-pill tag-pill-soft">#语音智能体</span> <span class="tag-pill tag-pill-soft">#LLM智能体</span> <span class="tag-pill tag-pill-soft">#系统评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11299</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11299" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11299" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DuplexAgent全双工语音协作系统，用六个可编辑模块编排对话与异步委派，并以Duplex-Harness-RSI闭环从交互轨迹自动修复模块。
</div>

## 👥 作者与机构

**Yingda Shen** ¹ · Yuxiang Wang · Kunyu Feng · Qinke Ni · Jiaqi Li · Minghao Hsu · Junan Zhang · Dekun Chen · … 等 2 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音智能体、全双工对话系统与LLM agent编排的研究者与工程团队阅读。建议重点看harness六模块的划分方式与RSI闭环（模拟器生成测试→失败轨迹→Exam Planner选测→Harness Editor改模块）的设计，以及harness消融实验部分；若关注语音增强/分离本身则可略读。

## 🌍 研究背景

语音智能体正收敛到一种协作范式：全双工模型常驻实时通道负责连续听说，搜索、推理与编码通过异步委派交给能力更强的编码智能体。但全双工模型难以胜任复杂推理与工具调用，编码智能体的顺序接口又不适合实时对话，二者结合需要一个协调任务接受、进度、取消、替换与结果投递的harness。现有harness多依赖耦合启发式规则，难以从证据中系统化改进，本文即针对这一可改进性问题。

## 💡 核心创新

1. 将协作harness拆为六个可编辑模块，便于定点修复
2. Duplex-Harness-RSI闭环：从交互轨迹自动诊断并修复模块
3. 模拟器自动生成定时测试对话并产出失败轨迹
4. Exam Planner按弱点与修复档案选择下一轮测试
5. Harness Editor提出针对性模块改动，形成自改进循环

## 🏗️ 模型架构

系统由全双工对话前端与异步委派后端组成。全双工模型常驻实时通道，负责连续监听与说话；复杂任务经harness委派给推理LLM与编码智能体池。harness以六个可编辑模块表达任务接受、进度跟踪、取消、替换与结果投递等工作流。Duplex-Harness-RSI为闭环：模拟器生成带时间戳的测试对话并运行系统，产出失败轨迹；Exam Planner据此与修复档案选择下一批测试；Harness Editor提出模块级修改并回灌harness。摘要未给出参数量与具体网络结构。

## 📚 数据集

- 智能/agentic/全双工基准（评估，摘要未列具体数据集名）

## 📊 实验结果

摘要仅定性说明：在智能、agentic与全双工基准上，DuplexAgent在spoken-knowledge与executable-tool得分上优于所对比的委派系统，同时保持较强的打断响应能力。harness消融显示，模块化可验证闭环优于初始harness，也优于缺少诊断与修复档案的反复编辑。摘要未给出任何具体指标数值、数据集名称或效率指标，故无法列表对比。

## 🎯 结论与影响

最强结论是：服务用户的能力（推理LLM与编码智能体）同时可被复用来改进系统自身的协作harness，形成自改进闭环。这为全双工语音智能体的harness工程提供了可验证、可迭代的范式，后续研究或可沿模块化诊断与修复档案方向扩展。工业上意味着语音助手可在不重训前端模型的前提下，通过harness迭代提升复杂任务完成度。

## ⚠️ 局限与未解决问题

摘要未给出任何量化指标、数据集名称与推理延迟，难以判断实际增益幅度；harness六模块的划分依据与模块间耦合程度未说明；自改进闭环的稳定性、是否会过拟合模拟器分布、以及修复档案的规模上限均未讨论；与主流全双工/委派系统的对比细节缺失。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
