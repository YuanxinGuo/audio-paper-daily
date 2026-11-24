---
title: "Audio-Visual Rearrangement"
date: 2026-11-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多模态具身智能"]
summary: "提出视听重排任务：智能体听语音请求、定位说话人、取物送达，构建数据集并提出融合运动感知空间音频模块的视听大模型框架。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多模态具身智能</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视听导航</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#大型语言模型</span> <span class="tag-pill tag-pill-soft">#具身智能</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.30171</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.30171" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.30171" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出视听重排任务：智能体听语音请求、定位说话人、取物送达，构建数据集并提出融合运动感知空间音频模块的视听大模型框架。
</div>

## 👥 作者与机构

**Ruohao Guo** ¹ · Jiatong Ye · Chenwei Dong · Jinxing Zhou · Dantong Niu · Guangyao Li · Zhenbo Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合具身智能与视听多模态方向研究者阅读。值得浏览以了解任务定义与数据集构建，重点看 §3 数据集设计与 §4 空间音频模块如何编码方位线索；若关注语音增强/分离则相关性低，可略读。

## 🌍 研究背景

现有具身导航与视听导航工作多依赖视觉目标或文本指令，缺少对语音请求中说话人方位与相对空间指代的理解。传统声源定位与波束成形方法难以与高层语义指令结合，而视听大语言模型虽能融合视觉与语言，却很少显式建模运动中的空间音频线索。本文要解决智能体在真实室内环境中听懂语音请求、声学定位说话人并完成取物送达的问题。

## 💡 核心创新

1. 定义视听重排（AVR）新任务，涵盖显式目标、说话人相对空间指代与隐式意图三类查询
2. 构建含八种子类型、多样取送要求的 AVR 数据集
3. 在视听大语言模型中嵌入运动感知空间音频模块，随智能体移动更新空间线索
4. 采用多任务指令微调，联合监督语音理解、空间音频感知与视觉 grounding

## 🏗️ 模型架构

输入为智能体视角的 RGB 视频流与多通道空间音频（语音请求）。语音经编码器提取语义与方位特征，视觉经视觉编码器提取场景表征，二者送入视听大语言模型主干。核心是运动感知空间音频模块：将多通道音频的空间线索编码为随智能体位姿更新的空间 token，并与语言指令对齐。输出为动作预测（导航与抓取放置）。多任务指令微调同时优化语音理解、空间音频感知与视觉 grounding 三个辅助头。摘要未给出参数量。

## 📚 数据集

- AVR 自建数据集（训练与评估，含三类查询、八种子类型）

## 📊 实验结果

摘要仅说明在已见与未见环境中建立了基线性能，未给出 SI-SDR、WER、成功率等具体数值，也未报告与现有方法的定量对比，因此无法列出结果表。

## 🎯 结论与影响

最强结论是：将运动感知空间音频模块接入视听大语言模型可支撑语音驱动的取物送达任务，并在已见与未见环境中给出基线。该任务定义为具身智能与视听多模态研究提供了新评测点，对服务机器人语音交互落地有潜在参考价值。

## ⚠️ 局限与未解决问题

摘要未给出任何定量指标与基线对比，难以判断方法有效性；数据集规模、场景多样性未说明；缺少消融验证空间音频模块与多任务微调各自贡献；未报告推理延迟与实时性，而具身场景对时延敏感。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-24/">← 返回 2026-11-24 速递</a></div>
