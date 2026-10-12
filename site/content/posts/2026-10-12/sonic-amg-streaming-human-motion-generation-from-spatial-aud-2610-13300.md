---
title: "Sonic-AMG: Streaming Human Motion Generation from Spatial Audio"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频驱动动作生成"]
summary: "首个从空间音频流式生成人体动作的框架，用因果Transformer与flow head实现实时在线反应生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频驱动动作生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#动作生成</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#因果Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.13300</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://jingchengni.com/sonic-amg/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">jingchengni.com/sonic-amg/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.13300" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.13300" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://jingchengni.com/sonic-amg/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个从空间音频流式生成人体动作的框架，用因果Transformer与flow head实现实时在线反应生成。
</div>

## 👥 作者与机构

**Jingcheng Ni** ¹ · Zekun Li · Zhiyang Dou · Xiaoyan Cong · Ziyao Zeng · Hongyang Du · Randall Balestriero · Taku Komura · … 等 1 人

**机构**：布朗大学 · 爱丁堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频-动作跨模态生成、空间音频理解与流式生成的研究者阅读。建议重点看§3的token分离编码与rehearsal training设计，以及表1在SAM上的FID/R-precision对比。若只关心语音增强/分离，可跳过。

## 🌍 研究背景

从音频生成人体动作已有工作（如基于完整音频序列的离线生成），但均假设可获取完整声学与空间输入。真实场景中人类只能基于已听到的声音即时反应，存在流式因果约束。现有离线方法无法直接用于在线生成，且训练用真值历史、推理用生成历史导致训练-推理不匹配。本文要解决空间音频下的流式动作生成问题。

## 💡 核心创新

1. 将声学内容与身体相对声源几何编码为分离token
2. 因果Transformer+flow head生成连续动作隐变量
3. rehearsal training混合全序列监督与自回归自rollout
4. spatial feedback用生成根姿态重算声源相对位置

## 🏗️ 模型架构

输入为空间音频，声学内容与身体相对声源几何分别编码为独立token。主干为因果Transformer，接flow head输出连续动作隐变量，再由因果解码器重建动作片段。训练时采用teacher-forcing从真值动作导出历史与声源相对位置；推理时用生成动作。rehearsal training结合全序列监督与短自回归自rollout监督，spatial feedback在训练与推理中均从生成根姿态重算身体相对声源位置。摘要未给出参数量。

## 📚 数据集

- SAM（训练与评估，具体规模摘要未说明）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FID | SAM | 摘要未给出具体基线数值 | **state-of-the-art** | 未给出具体数值 |
| R-precision | SAM | 摘要未给出具体基线数值 | **state-of-the-art** | 未给出具体数值 |

摘要在SAM数据集上报告FID与R-precision达到state-of-the-art，并支持跨声音事件与声源位置的实时在线连贯反应生成。但未给出具体数值、基线名称、消融实验或效率指标，无法量化提升幅度。

## 🎯 结论与影响

本文首次将人体动作生成置于空间音频流式设定，提出rehearsal training与spatial feedback缓解训练-推理不匹配，在SAM上取得最优FID与R-precision。该设定对VR/AR、机器人与虚拟人实时交互有潜在价值，但需更多定量对比验证。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与基线对比，缺少消融实验验证rehearsal training与spatial feedback各自贡献；未报告推理延迟与实时性量化指标；仅在一个数据集SAM上评估，泛化性未知。

## 🔗 开源资源

- **项目主页**：<https://jingchengni.com/sonic-amg/>

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
