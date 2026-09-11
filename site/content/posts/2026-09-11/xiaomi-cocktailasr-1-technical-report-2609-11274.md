---
title: "Xiaomi-CocktailASR-1 Technical Report"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "小米提出基于LLM的端到端目标说话人ASR，用参考语音作声纹提示直接转写目标说话人，无需语音分离，并支持拒识与CoT推理。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#鸡尾酒会问题</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.11274</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.11274" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.11274" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>小米提出基于LLM的端到端目标说话人ASR，用参考语音作声纹提示直接转写目标说话人，无需语音分离，并支持拒识与CoT推理。
</div>

## 👥 作者与机构

**Yiru Zhang** ¹ · Hang Su · Lichun Fan · Ying Zeng · Chang Liu · Yifeng Wang · Yuquan Liang · Tao Li · … 等 5 人

**机构**：小米

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TS-ASR、LLM-based语音识别与鸡尾酒会问题的研究者阅读。建议通读，重点看§3的声纹提示注入方式与拒识机制，以及多说话人/单说话人基准上的对比表；若关注落地，需额外核查推理延迟与流式能力。

## 🌍 研究背景

鸡尾酒会场景下多说话人ASR仍是瓶颈。此前TS-ASR主流做法有两类：一是带说话人embedding的端到端架构（如基于Conformer的分离+识别联合模型），二是近期LLM-based探索。前者依赖语音分离、单说话人性能下降；后者难以在目标说话人缺席时拒识，且单说话人精度退化。本文要解决的是：在统一LLM架构下兼顾多说话人与单说话人识别精度，并具备目标缺席拒识能力。

## 💡 核心创新

1. 以参考语音作voiceprint prompt，免分离直接转写目标说话人
2. 统一架构兼顾多说话人与单说话人ASR性能
3. 目标说话人缺席时输出空文本的拒识能力
4. 支持Chain-of-Thought推理模式输出显式推理步骤

## 🏗️ 模型架构

输入为混合语音与参考语音两路。参考语音经声学编码器提取声纹提示（voiceprint prompt），与混合语音的声学特征一并送入LLM-based端到端主干，由LLM自回归解码目标说话人文本，无需显式语音分离模块。模型支持CoT模式，在解码时先输出推理步骤再给出转写结果；当检测到目标说话人不在混合中时输出空文本实现拒识。摘要未给出参数量与具体网络层配置。

## 📚 数据集

- 合成多说话人基准（评估）
- 真实多说话人基准（评估）
- 单说话人ASR基准（评估，验证单说话人性能）

## 📊 实验结果

摘要仅称在多种合成与真实多说话人基准上达到state-of-the-art，并保持与主流ASR相当的单说话人性能，同时具备拒识能力，但未给出任何具体指标数值、数据集名称或基线对比数字，无法量化提升幅度。

## 🎯 结论与影响

最强结论是：LLM-based端到端架构可在不显式分离的前提下统一处理多说话人TS-ASR与单说话人ASR，并附带拒识与CoT能力。这为鸡尾酒会ASR提供了免分离的新范式，后续研究可能围绕声纹提示设计与拒识校准展开；工业上利于在统一模型中同时服务单/多说话人场景，降低系统复杂度。

## ⚠️ 局限与未解决问题

摘要未报告任何量化指标、参数量、推理延迟与流式能力，也未说明拒识的误拒/漏拒率；缺少与SEPFormer、TS-ASR等强基线的具体对比与消融。真实基准的说话人重叠度、噪声条件与数据集偏置未知，CoT模式带来的额外延迟代价也未评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
