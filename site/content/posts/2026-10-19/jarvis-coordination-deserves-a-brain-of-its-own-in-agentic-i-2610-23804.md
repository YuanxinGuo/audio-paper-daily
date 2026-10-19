---
title: "Jarvis: Coordination Deserves a Brain of Its Own in Agentic Interactive Models"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "提出 Jarvis 协调框架，用类型化决策模型 JEV 与代码校验管理前后台模型的任务版本，提升全双工语音智能体的任务成功率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#智能体协调</span> <span class="tag-pill tag-pill-soft">#语音交互</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.23804</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.23804" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.23804" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 Jarvis 协调框架，用类型化决策模型 JEV 与代码校验管理前后台模型的任务版本，提升全双工语音智能体的任务成功率。
</div>

## 👥 作者与机构

**Yuxiang Wang** ¹ · Shengbo Cai · Zhixian Zhao · Yingda Shen · Yuancheng Wang · Xueyao Zhang · Liqiang Zhang · Teddy Sun · … 等 2 人

**机构**：香港中文大学（深圳）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工语音对话、语音智能体系统的研究者与工程团队阅读。值得通读，重点看 §3 的 JEV 决策模型与版本化任务记录设计，以及表 2 中 tau-Voice 与 Full-Duplex-Bench v3 的对比；若只关心声学前端可略读。

## 🌍 研究背景

全双工语音交互系统通常采用快慢双脑架构：前台实时模型维持对话，后台慢模型负责复杂推理与工具调用。但用户在任务执行中可能修改、取消或替换请求，导致在途计划与结果过期。前台模型只看到对话历史，后台只看到自身任务，二者缺乏对彼此状态的共同视图，现有系统缺少显式的协调层来处理任务版本失效问题。

## 💡 核心创新

1. 提出 JEV 类型化决策模型，按当前活跃任务选择操作
2. 基于版本化任务记录的代码级状态校验，防止对已替换版本执行决策
3. 计划执行前与结果播报前的双重再校验机制
4. 以用户完整听到作为答案交付的判定标准

## 🏗️ 模型架构

系统为协调外壳（harness），模型负责判断、代码负责执行。输入为每轮用户话语与当前活跃任务集合，JEV 决策模型输出类型化操作，操作作用于版本化任务记录；执行前由代码校验所选任务版本与当前状态一致，不一致则拒绝。计划执行前与结果播报前各做一次再校验。Jarvis-Audio 直接套用于三个全双工语音模型；Jarvis-Omni 增加视觉输入，在播报前与播报中复核答案所依据的证据。摘要未给出参数量。

## 📚 数据集

- tau-Voice（评估，278 个任务）
- Full-Duplex-Bench v3（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 任务成功数 | tau-Voice | Qwen Audio Agent 29/278 | **Jarvis 192/278** | +163 个任务（约 6.6 倍） |
| Pass1 | Full-Duplex-Bench v3 | GPT-Realtime 60% | **Jarvis-Audio（开源 9B 前台模型）69%** | +9% |

在前后台模型固定的条件下，仅替换协调层即可将 tau-Voice 任务成功数从 29 提升至 192（共 278 任务），且增益在各基准与各前台模型上均成立，说明提升来自协调机制而非模型能力。与已发表系统相比，Jarvis-Audio 用开源 9B 前台模型在 Full-Duplex-Bench v3 上取得 69% Pass1，高于 GPT-Realtime 的 60%。摘要未报告延迟与消融细节。

## 🎯 结论与影响

最强结论是：双脑如何协调与双脑本身多强同等重要，协调层可独立带来大幅任务成功率提升。这为全双工语音智能体提供了可复用的系统设计范式，提示后续研究应把协调状态管理作为一等公民。工业上意味着无需更换大模型即可显著改善语音助手任务完成率。

## ⚠️ 局限与未解决问题

摘要未给出推理延迟、协调层自身开销与消融实验，难以判断实时性代价；任务成功判定依赖用户完整听到，评测口径与既有工作不完全可比；Jarvis-Omni 的视觉复核缺乏定量结果；基准覆盖仍以 tau-Voice 与 Full-Duplex-Bench 为主。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
