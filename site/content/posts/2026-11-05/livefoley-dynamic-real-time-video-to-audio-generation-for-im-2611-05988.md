---
title: "LiveFoley: Dynamic Real-Time Video-to-Audio Generation for Immersive Interactive Worlds"
date: 2026-11-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "LiveFoley 用尾随滑窗把非因果视觉前端改造成流式模块，并用加宽去噪窗口的 LocDiT 提升流式 V2A 的音质与时序对齐。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#视频到音频生成</span> <span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#实时推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.05988</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://dalision.github.io/livefoley-page/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">dalision.github.io/livefoley-page/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.05988" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.05988" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://dalision.github.io/livefoley-page/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>LiveFoley 用尾随滑窗把非因果视觉前端改造成流式模块，并用加宽去噪窗口的 LocDiT 提升流式 V2A 的音质与时序对齐。
</div>

## 👥 作者与机构

**Yusheng Dai** ¹ · Vladimir Iashin · Kangdi Wang · Yuxuan Jiang · Ilpo Viertola · Weiqiang Wang · Qiuhong Ke · Min Zhao · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做视频到音频生成、流式扩散推理与交互式内容生成的读者。值得通读，重点看 §3 的 Trailing Sliding Window 与 Unified Varhop 设计、§4 的 History/Future-Warmup LocDiT 对比，以及时序对齐指标表；工程侧关注 hop size 与延迟预算的权衡曲线。

## 🌍 研究背景

视频到音频（V2A）生成近年由扩散模型推动，离线模型如 Diff-Foley、FoleyCrafter 在音质与语义匹配上已较成熟，但需完整视频与多次迭代去噪，无法用于交互式场景。流式 V2A 为压延迟通常缩小视觉前端感受野并采用因果自回归扩散，导致视听对齐变差、逐 patch 独立去噪使音质下降。本文要解决的是在几乎不可感知延迟下同时保住对齐精度与生成质量。

## 💡 核心创新

1. Trailing Sliding Window：无需重训即把非因果段级视觉编码器转为流式
2. Unified Varhop Framework：用可调 hop size 适配不同延迟与算力预算
3. History LocDiT：引入历史上下文提升音质且零额外延迟
4. Future-Warmup LocDiT：用近似未来条件打破自回归死锁

## 🏗️ 模型架构

输入为流式视频帧，经尾随滑窗改造的段级视觉编码器（非因果前端重对齐窗口）提取视听特征，hop size 可配置以控制前视延迟；音频侧采用因果自回归扩散主干，以局部扩散 Transformer（LocDiT）头逐 patch 去噪，默认 History LocDiT 在时间维上扩展去噪窗口纳入历史上下文，可选 Future-Warmup LocDiT 引入近似未来条件；输出为流式生成的音频波形。摘要未给出参数量。

## 📊 实验结果

摘要仅给出定性结论：LiveFoley 在时序对齐上可匹配离线模型，在生成质量上领先现有流式系统，并称延迟低于人类感知阈值；未披露具体数据集、指标数值与消融结果，需查阅正文与项目页确认。

## 🎯 结论与影响

最强结论是流式 V2A 可在不可感知延迟下达到离线级的视听对齐，同时以加宽去噪窗口弥补因果扩散的音质损失。这为交互式世界、游戏与虚拟现实的实时音效生成提供了可行路径，也提示流式扩散可通过上下文窗口设计而非单纯缩小感受野来折中质量与延迟。

## ⚠️ 局限与未解决问题

摘要缺少定量结果、数据集说明与延迟/算力实测，难以核验“匹配离线模型”的宣称；Future-Warmup 引入后端前视，其可接受性缺乏主观听测支撑；未报告与离线 SOTA 在音质指标上的差距及失败案例分析。

## 🔗 开源资源

- **项目主页**：<https://dalision.github.io/livefoley-page/>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-11-05/">← 返回 2026-11-05 速递</a></div>
