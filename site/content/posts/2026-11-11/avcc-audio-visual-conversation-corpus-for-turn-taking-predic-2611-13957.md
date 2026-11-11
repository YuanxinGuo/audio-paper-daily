---
title: "AVCC: Audio-Visual Conversation Corpus for Turn-Taking Prediction with a Human Benchmark"
date: 2026-11-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对话轮次预测"]
summary: "构建AVCC音视频对话语料库，用于多人对话下一说话人预测基准，并给出人类表现参考。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对话轮次预测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#音视频</span> <span class="tag-pill tag-pill-soft">#基准数据集</span> <span class="tag-pill tag-pill-soft">#轮次预测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.13957</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.13957" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.13957" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建AVCC音视频对话语料库，用于多人对话下一说话人预测基准，并给出人类表现参考。
</div>

## 👥 作者与机构

**Haotian Qi** ¹ · Gabriel Skantze

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对话系统、社交机器人、轮次预测方向研究者阅读。值得通读，重点看数据集构建（§3）与人类基准实验（§4），以及RoleVAP与MuVAP的对比表。可先看表2与人类基准对比部分，判断模型与人类差距。

## 🌍 研究背景

多人对话下一说话人预测（NSP）此前多在带逐说话人传感器的语料上研究，各语料事件定义不一，缺乏统一公开基准。现有工作未覆盖机器人单摄像头单麦克风的真实场景，也没有模型与人类表现直接对比。本文旨在将AVCC语料转为公开NSP基准，填补单传感器场景与人类参考的空白。

## 💡 核心创新

1. 将AVCC转为公开NSP基准，含说话人分离测试集
2. 新增865 hold与865 shift事件标注
3. 提供全语料词级强制对齐转写
4. 采集同事件人类参考基准
5. 开源标签、转写与复现脚本

## 🏗️ 模型架构

输入为单静态摄像头视频与单麦克风音频。音频侧采用Role-Relative VAP（RoleVAP）仅音频模型，基于语音活动预测框架建模轮次动态；多模态侧采用MuVAP模型融合音视频特征。输出为在互静音间隙处的hold/shift事件预测，即判断下一说话人是否切换。摘要未给出具体参数量与主干网络细节。

## 📚 数据集

- AVCC（31小时双人/三人线上对话，训练与评估）
- AVCC说话人分离七视频测试集（865 hold/865 shift事件，评估）

## 📊 实验结果

摘要未给出具体数值指标，仅说明对RoleVAP（仅音频）与MuVAP（多模态）进行评分，并采集同事件人类参考基准。具体hold/shift预测准确率、与人类差距等数字需见原文。

## 🎯 结论与影响

本文最强结论是提供了首个面向单摄像头单麦克风场景、含人类参考的公开NSP基准。该基准有望统一后续NSP评测口径，推动社交机器人与对话代理的轮次预测研究，并为工业界提供可复现的评测基线。

## ⚠️ 局限与未解决问题

摘要未报告具体性能数字与人类-模型差距，难以判断方法贡献强度；语料为线上对话，与真实机器人场景仍有域差；未提及推理延迟与实时性，对落地评估不足。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-11/">← 返回 2026-11-11 速递</a></div>
