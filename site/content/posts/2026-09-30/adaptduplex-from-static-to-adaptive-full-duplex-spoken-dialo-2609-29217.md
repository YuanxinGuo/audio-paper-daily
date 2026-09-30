---
title: "AdaptDuplex: from static to adaptive full-duplex spoken dialogue"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "在 Qwen3-Omni 上扩展 token 级协议与自适应窗口机制，实现全双工语音对话的动态决策与低延迟响应。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工对话</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#语音交互</span> <span class="tag-pill tag-pill-soft">#自适应决策</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29217</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29217" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29217" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在 Qwen3-Omni 上扩展 token 级协议与自适应窗口机制，实现全双工语音对话的动态决策与低延迟响应。
</div>

## 👥 作者与机构

**Zhiyang Zhou** ¹ · Yingxin Shang · Zhou Wang · Hongwei Cai · Weixu Wang · Shuran Zhou · Shuofeng Zhao · Wenke Fan · … 等 4 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工语音对话、端到端语音大模型、人机交互时序建模的研究者与工程团队阅读。建议重点看 §3 的三层协同设计（token 协议、双流对齐、自适应窗口）与 §4 的三阶段 Thinker 课程训练流程，再对照表 2/表 3 的 Full-Duplex-Bench 指标。若只关心落地，可先看自适应窗口与 logits bias 运行时控制部分。

## 🌍 研究背景

全双工语音对话要求亚秒级延迟下同时听与说，但对话节奏与认知负荷时刻变化。现有系统（如 DuplexOmni、MiniCPM-o）多采用静态工作点，缺乏对“何时听、何时说、是否打断、是否思考”的系统化自适应决策机制，导致在重叠语音、轮次切换等场景下时序僵硬、响应延迟高。本文要在 Qwen3-Omni 基础上引入可训练、可运行时控制的自适应决策机制，解决静态工作点与动态对话需求之间的矛盾。

## 💡 核心创新

1. token 级协议将每个窗口编码为规范序列，行为决策显式化为 token
2. 有界文本领先的双流对齐训练，实现听/说同步
3. 自适应窗口时长预测 + 非阻塞认知整合与多飞行外部推理
4. 三阶段 Thinker 课程 + Talker-only 与联合 SFT 的渐进训练管线
5. logits bias 实现免训练运行时行为控制

## 🏗️ 模型架构

以 Qwen3-Omni 为基座，输入为连续语音流并按窗口切分。核心是三层协同：① token 级协议层，将每个窗口表示为规范 token 序列，把听/说/打断/思考等行为决策显式化为可预测 token；② 双流对齐层，通过有界文本领先（bounded text lead）约束语音与文本流对齐；③ 自适应机制层，动态预测离散窗口时长，并按需触发非阻塞认知整合与多飞行外部推理。训练采用三阶段 Thinker 课程，随后 Talker-only SFT 与联合 SFT，GRPO 作为初步增量。运行时通过 logits bias 免训练控制行为。摘要未给出参数量。

## 📚 数据集

- Full-Duplex-Bench v1（评估，轮次切换/重叠行为/时序指标）
- Full-Duplex-Bench v1.5（评估）
- HumDial-FDBench（评估，人类录音全双工对话，Final score）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 可比指标胜出数（轮次切换/重叠行为/时序） | Full-Duplex-Bench v1 & v1.5 | DuplexOmni（21 项可比指标） | **18/21 项胜出** | 胜出 18 项 |
| 可比指标胜出数 | Full-Duplex-Bench v1 & v1.5 | MiniCPM-o 4.5（22 项可比指标） | **19/22 项胜出** | 胜出 19 项 |
| Final score | HumDial-FDBench | 对比的全双工模型 | **69.6** | 最高 Final score |

在 Full-Duplex-Bench v1 与 v1.5 上，AdaptDuplex 在 21 项可比指标中 18 项优于 DuplexOmni，在 22 项中 19 项优于 MiniCPM-o 4.5，交互决策与响应时序均有提升。在人类录音的 HumDial-FDBench 上取得对比模型中最高的 Final score 69.6。摘要未给出消融实验、推理延迟与参数量等效率指标，也未报告各单项指标的具体数值。

## 🎯 结论与影响

最强结论是：将行为决策显式 token 化并配合自适应窗口，可在不重训的情况下让全双工对话模型动态调整听/说策略，并在多个基准上稳定超过 DuplexOmni 与 MiniCPM-o 4.5。该思路为全双工对话的“可控制决策层”提供了可复用范式，后续研究可沿 token 协议与课程训练继续扩展。工业上，logits bias 的免训练控制有利于快速调参与产品化部署。

## ⚠️ 局限与未解决问题

摘要仅给出胜出指标数量与一个 Final score，缺少各指标具体数值、消融实验与推理延迟/显存开销；GRPO 仅作“初步增量”，其贡献未量化；自适应窗口与多飞行推理的额外计算成本未讨论；评估集中在 Full-Duplex-Bench 与 HumDial-FDBench，跨语言与跨领域泛化未知。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
