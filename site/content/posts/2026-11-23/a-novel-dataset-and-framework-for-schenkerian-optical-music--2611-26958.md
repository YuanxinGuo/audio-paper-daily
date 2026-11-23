---
title: "A Novel Dataset and Framework for Schenkerian Optical Music Recognition"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#光学音乐识别"]
summary: "提出首个手写申克分析标注数据集，并用集成检测与拓扑网络实现申克图的光学识别与排版。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#光学音乐识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#光学音乐识别</span> <span class="tag-pill tag-pill-soft">#乐谱分析</span> <span class="tag-pill tag-pill-soft">#目标检测</span> <span class="tag-pill tag-pill-soft">#图神经网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.26958</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.26958" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.26958" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个手写申克分析标注数据集，并用集成检测与拓扑网络实现申克图的光学识别与排版。
</div>

## 👥 作者与机构

**Yixuan Huang** ¹ · Xiao Yun · Jiayin Zheng · Simon Mak · Yue Jiang · Cynthia Rudin · Stephen Ni-Hahn

**机构**：杜克大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索（ISMIR 方向）与 OMR 研究者阅读。若关注符号检测集成策略，重点看 §3 的裁剪方案集成与 §4 的拓扑装配网络；若关注数据价值，先看数据集构建与 MuNG Studio 集成部分。方法本身与语音/音频信号处理关联弱，语音领域读者可略读。

## 🌍 研究背景

申克分析（SchA）用分层图刻画调性结构与声部进行，是音乐理论与教学的重要工具，但制图流程依赖手绘后逐符号手工录入制谱软件，效率极低。现有手写 CWMN 光学音乐识别（OMR）系统虽能识别小符号，却难以处理乐句连音线等大符号、密集记谱，且完全不识别申克分析专有标记，因此无法直接迁移到 SchA 数字化。本文要解决手写申克图从纸面到结构化语义图再到排版输出的全流程自动化问题。

## 💡 核心创新

1. 多裁剪方案集成的目标检测，提升密集记谱与大符号召回
2. 基于超边注意力与分层消息传递的拓扑装配网络
3. 首个手写申克分析标注数据集及 MuNG Studio 标注集成
4. 首个语义申克图转排版格式的转换算法

## 🏗️ 模型架构

输入为手写乐谱/申克图扫描图像，先经多种图像裁剪方案分别送入目标检测器（集成多个检测模型）得到符号候选框与类别；随后将候选符号构造成图节点，由拓扑神经网络进行记谱装配：候选超边之间相互注意力计算并执行分层消息传递，输出符号间的结构关系（如连音、层级归属）；最终由语义图转排版算法生成可编辑的排版格式。摘要未给出参数量与主干网络细节。

## 📚 数据集

- 自建手写申克分析标注数据集（训练 / 评估，首个此类标注集）
- 手写 CWMN 记谱数据（用于检测与装配训练 / 评估）

## 📊 实验结果

摘要未给出任何定量指标（如检测 mAP、符号识别准确率或图装配 F1），仅定性说明现有 CWMN OMR 模型在大符号、密集记谱与申克标记上失效，本文框架可同时处理 CWMN 与 SchA。具体实验数字需查阅正文。

## 🎯 结论与影响

本文最强结论是将申克分析数字化从纯手工流程转为端到端可自动化的识别—装配—排版管线，并配套首个手写 SchA 标注数据集。对 OMR 与音乐理论计算化后续研究有数据与方法双重推动，工业上可嵌入制谱与音乐教育工具。

## ⚠️ 局限与未解决问题

摘要缺乏定量结果与基线对比，无法判断相对现有 OMR 的实际增益；数据集规模、标注一致性、跨书写者泛化均未说明；集成检测与拓扑装配的计算开销与推理延迟未报；与语音/音频信号处理关联较弱。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
