---
title: "EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "构建第一人称多模态流下的主动语音助手框架，用语音分离与重合成清洗HoloAssist音频，微调全模态LLM并用DPO优化干预时机。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.12248</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.12248" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.12248" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建第一人称多模态流下的主动语音助手框架，用语音分离与重合成清洗HoloAssist音频，微调全模态LLM并用DPO优化干预时机。
</div>

## 👥 作者与机构

**Heeseung Kim** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态对话、主动式助手、egocentric 感知的研究者。若关注语音分离本身，本文只是数据清洗工具链，可略读 §3 数据构建；若关注 proactive agent，建议通读数据构造与 DPO 部分，并重点看干预时机与人类偏好评估表。

## 🌍 研究背景

主动式视频助手、口语对话系统与第一人称任务理解各自进展迅速，但现有系统未联合解决“何时开口”与“说什么”的问题。传统对话系统多为被动响应，缺乏从连续第一人称视频音频流中判断干预时机的机制；egocentric 数据集如 HoloAssist 含大量真实教学语音，但录音含噪声与重叠，直接训练会引入脏标签。本文要解决的是：如何从第一人称多模态流中训练并评估能主动、适时给出语音指导的助手。

## 💡 核心创新

1. 用语音分离+重合成从 HoloAssist 构造干净音频流
2. 将视频会话转为每时刻“沉默/指导”决策格式
3. 微调 omni-modal LLM 实现主动干预
4. 用 DPO 进一步优化干预行为

## 🏗️ 模型架构

输入为第一人称视频帧与音频流，经语音分离与重合成得到干净语音，再与视频对齐构成多模态序列。主干为 omni-modal LLM，接收视觉与音频 token，输出两种行为：保持沉默或生成语音指导文本（后续可 TTS）。训练分两阶段：先监督微调使模型学会在合适时刻输出指导内容，再用直接偏好优化（DPO）以人类偏好对优化干预时机与内容相关性。摘要未给出参数量与具体网络细节。

## 📚 数据集

- HoloAssist（训练/评估，真实人类教学第一人称视频）

## 📊 实验结果

摘要仅给出定性结论：闭源与开源模型在零样本下很少产生时机恰当、有意义的主动干预，而 EgoVoice 在干预时机、内容相关性与人类偏好上相对零样本主干均有明显提升。未提供 SI-SDR、PESQ、WER 或具体数值，也未报告消融与效率指标。

## 🎯 结论与影响

最强结论是：从第一人称多模态流中主动决定何时说、说什么，可通过数据构造加 LLM 微调与 DPO 显著改善。这为 proactive egocentric assistant 提供了可复用的训练评估范式，可能推动可穿戴 AR 助手从被动问答走向主动协作；工业上对实时性、误触发控制要求高，落地仍需大量工程验证。

## ⚠️ 局限与未解决问题

语音分离仅作为数据清洗手段，未评估分离质量对下游的影响；缺少消融说明 DPO 与 SFT 各自贡献；未报告推理延迟与误触发率，而主动助手对这两点极敏感；评估依赖人类偏好，主观性强，HoloAssist 单一数据集也带来领域偏差。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
