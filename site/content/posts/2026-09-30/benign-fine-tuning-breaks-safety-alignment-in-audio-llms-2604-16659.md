---
title: "Benign Fine-Tuning Breaks Safety Alignment in Audio LLMs"
date: 2026-09-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频大模型安全对齐"]
summary: "首次系统研究音频LLM在良性微调下的安全对齐退化，发现脆弱轴由编码器架构决定，JSR可升至87%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频大模型安全对齐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频LLM</span> <span class="tag-pill tag-pill-soft">#安全对齐</span> <span class="tag-pill tag-pill-soft">#微调脆弱性</span> <span class="tag-pill tag-pill-soft">#越狱攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2604.16659</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2604.16659" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2604.16659" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次系统研究音频LLM在良性微调下的安全对齐退化，发现脆弱轴由编码器架构决定，JSR可升至87%。
</div>

## 👥 作者与机构

**Jaechul Roh** ¹ · Virat Shejwalkar · Amir Houmansadr

**机构**：马萨诸塞大学阿默斯特分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频LLM安全、对齐鲁棒性、多模态越狱的研究者阅读。值得通读，重点看§3的proximity框架与§4的JSR结果表，以及§5的识别-拒绝解离机制分析。若只关心防御，可直接跳到§6的两种防御实验。

## 🌍 研究背景

文本与视觉LLM已被证明良性微调会破坏安全对齐，但音频模态是否因语义与声学双重邻近性而呈现不同脆弱模式尚不清楚。现有安全评估多针对文本，缺乏对音频编码器-投影器-骨干LLM架构的分解分析，也缺少针对音频越狱的系统性基线与防御。本文要回答：音频LLM的良性微调脆弱性由哪一轴主导，以及能否在不改架构的前提下防御。

## 💡 核心创新

1. 提出语义/声学/混合三轴邻近性框架量化音频嵌入空间
2. 发现脆弱主导轴由编码器-投影器架构决定
3. 揭示识别-拒绝解离：模型仍能检测有害内容但拒绝失效
4. 给出数据过滤与文本系统提示两种近零JSR防御

## 🏗️ 模型架构

输入为音频波形，经冻结的音频编码器（如Whisper类）与投影器映射到骨干LLM的输入空间，再交由LLM生成文本。本文不提出新网络，而是以三个SOTA音频LLM为对象，在嵌入空间计算良性样本与有害样本的语义、声学及混合距离，并据此构造微调数据。微调仅更新骨干LLM参数，编码器保持冻结，从而观察晚期层拒绝回路被选择性抑制的现象。

## 📚 数据集

- 三个SOTA音频LLM的公开有害/良性音频指令数据（训练与微调）
- 自建邻近性评估集（评估，按语义/声学/混合轴划分）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| JSR | 三个音频LLM评估集 | 微调前单数字JSR | **最高87%** | 显著上升 |
| JSR | 同上 | 无防御微调后 | **近零** | 数据过滤+系统提示后大幅下降 |

摘要给出JSR从个位数升至最高87%，并指出最有害轴随编码器设计在语义与声学间切换。两种防御（训练数据过滤、推理时文本系统提示）可将JSR降至近零且无需改架构。未提供SI-SDR/PESQ等音频质量指标，也未给出各模型逐项JSR数值与消融细节。

## 🎯 结论与影响

最强结论是音频LLM的良性微调脆弱性由架构条件决定，且识别与拒绝可解离。这提示安全评估必须纳入模态与架构维度，并为后续对齐鲁棒性研究提供音频测试床。工业上意味着部署音频LLM时需在微调数据筛选与推理提示层同时设防。

## ⚠️ 局限与未解决问题

仅评估三个模型，未覆盖开源与闭源全谱系；未报告推理延迟与计算开销；防御仅在本文设定下验证，跨模型泛化未知；缺乏对投影器结构的细粒度消融；JSR定义与攻击强度未在摘要中详述。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-30/">← 返回 2026-09-30 速递</a></div>
