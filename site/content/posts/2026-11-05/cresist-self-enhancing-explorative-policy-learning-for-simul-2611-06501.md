---
title: "CRESiST: Self-Enhancing Explorative Policy Learning for Simultaneous Speech Translation"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音翻译"]
summary: "基于全模态LLM的读写交错端到端同传框架，用RNN-T Actor与LLM Critic自增强学习流式策略，实现KV缓存全复用与无限长推理。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音翻译</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#同声传译</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.06501</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.06501" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.06501" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>基于全模态LLM的读写交错端到端同传框架，用RNN-T Actor与LLM Critic自增强学习流式策略，实现KV缓存全复用与无限长推理。
</div>

## 👥 作者与机构

**Chenyang Le** ¹ · Pei Zhang · Yuxiang Chen · Bing Han · Derek F. Wong · Baosong Yang · Yanmin Qian

**机构**：上海交通大学 · 阿里巴巴达摩院 · 澳门大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做同声传译、流式LLM推理与语音-文本多模态的研究者阅读。值得通读：重点看§3的读写交错架构与KV缓存复用机制，以及§4的Actor-Critic自增强流水线；实验部分先看Pareto前沿图与文档级MuST-C结果，再核对延迟指标定义（是否用LAAL/AL）。

## 🌍 研究背景

同声传译需在翻译质量与延迟间权衡。现有LLM-based SimulST多采用prefix-incremental生成，每步需重算KV缓存，且依赖外部VAD切分无界语音流，造成冗余计算与分段误差。离线对齐（如固定wait-k）又过于刚性，难以适配真实语流。本文要解决的是：在无外部VAD、无离线对齐的前提下，实现端到端、可无限长推理且策略自学习的流式同传。

## 💡 核心创新

1. 读写交错的speech chunk与text token序列建模，实现KV缓存全复用
2. 免分段、支持无限长流的原生推理，无需外部VAD
3. RNN-T Actor动态采样读写轨迹，摆脱刚性离线对齐
4. LLM Critic以语义+延迟内在奖励评估路径并蒸馏回Actor

## 🏗️ 模型架构

输入为流式语音chunk，经全模态LLM的语音编码器转为离散/连续表示，与已生成文本token交错排布成统一读写序列，主干为omni-modal LLM，借助交错结构实现KV cache全复用与无界流推理。策略层由RNN-T Actor在每个chunk处采样read/write动作，LLM-based Critic对采样轨迹给出语义质量与延迟的内在奖励，通过Actor-Critic自增强将最优策略蒸馏回Actor。输出为增量式目标文本token流。摘要未给参数量。

## 📚 数据集

- FLEURS（评估，句级）
- CoVoST2（评估，句级）
- MuST-C（评估，文档级）
- ACL 60/60（评估，文档级）

## 📊 实验结果

摘要称在句级（FLEURS、CoVoST2）与文档级（MuST-C、ACL 60/60）基准上建立新的质量-延迟Pareto前沿，显著优于级联与静态对齐基线，但未给出具体BLEU/延迟数值，无法量化对比。

## 🎯 结论与影响

最强结论是读写交错+自增强策略可在无VAD、无离线对齐下取得更优质量-延迟折中。对同传后续研究的潜在影响在于把流式策略学习从启发式wait-k转向可学习的Actor-Critic范式；工业上意味着更易部署于无界实时语音流、降低KV重算开销。

## ⚠️ 局限与未解决问题

摘要未报告具体指标数值、推理延迟与显存开销；Actor-Critic训练稳定性与奖励设计敏感性缺乏消融；未说明与流式ASR+MT级联在同等算力下的公平比较；文档级评测的延迟度量定义需核实。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
