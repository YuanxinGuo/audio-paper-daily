---
title: "Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音转换"]
summary: "提出Zero-VC，利用说话人匿名化作为扰动机制，在零前瞻流式语音转换中平衡音色泄露与效用保持。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音转换</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人匿名化</span> <span class="tag-pill tag-pill-soft">#流式处理</span> <span class="tag-pill tag-pill-soft">#零前瞻</span> <span class="tag-pill tag-pill-soft">#零样本</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.20218</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://amphionteam.github.io/Zero-VC-demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">amphionteam.github.io/Zero-VC-demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://amphionteam.github.io/Zero-VC-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">amphionteam.github.io/Zero-VC-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.20218" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.20218" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://amphionteam.github.io/Zero-VC-demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://amphionteam.github.io/Zero-VC-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Zero-VC，利用说话人匿名化作为扰动机制，在零前瞻流式语音转换中平衡音色泄露与效用保持。
</div>

## 👥 作者与机构

**Yudong Li** ¹ · Zihao Fang · Junwen Qiu · Ruihai Jing · Ruixiang Hang · Yingda Shen · Zhizheng Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音转换和说话人匿名化方向的研究者。建议重点阅读§3的扰动机制设计和§4的零前瞻网络结构，以及表2的延迟对比。

## 🌍 研究背景

零样本流式语音转换面临音色与语言内容解耦的挑战。现有方法依赖信息瓶颈（IB）或说话人扰动。IB丢弃韵律信息，需显式注入基频等特征，导致算法前瞻延迟；扰动方法则忽视音色泄露与效用保持的权衡。本文发现说话人匿名化（SA）的目标天然适合平衡这两者，因此引入SA作为新型扰动机制。

## 💡 核心创新

1. 引入说话人匿名化作为扰动机制，显式抑制音色泄露
2. 严格因果零前瞻网络，消除算法延迟
3. SA鲁棒表示减轻生成器对未来上下文的依赖
4. 在VCTK和LibriTTS上实现流式VC，延迟低于40ms

## 🏗️ 模型架构

输入语音经说话人匿名化模块提取匿名化表示，作为扰动特征；同时提取内容特征。两者送入严格因果的零前瞻生成网络，该网络采用因果卷积和循环结构，无未来帧缓冲。输出为转换后的语音。

## 📚 数据集

- VCTK（训练/评估，109说话人）
- LibriTTS（训练/评估，多说话人）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | VCTK | 原始语音 0.0% | **12.3%** | +12.3% |
| WER | VCTK | 原始语音 2.1% | **3.5%** | +1.4% |
| 延迟 | VCTK | 基线方法 80ms | **40ms** | -40ms |

在VCTK和LibriTTS上，Zero-VC在保持较低WER（3.5%）的同时实现了12.3%的EER，优于现有扰动方法。延迟仅40ms，满足流式需求。消融实验验证了SA扰动对音色泄露抑制的有效性。

## 🎯 结论与影响

Zero-VC通过说话人匿名化作为扰动机制，首次在零前瞻流式VC中有效平衡了音色泄露与效用保持。该方法为低延迟语音转换提供了新思路，有望推动实时语音匿名化应用。

## ⚠️ 局限与未解决问题

未在真实噪声/混响环境下评估；仅使用VCTK和LibriTTS，跨语言泛化未知；未报告计算复杂度或模型参数量；与更先进的扰动方法（如StarGANv2-VC）对比不足。

## 🔗 开源资源

- **项目主页**：<https://amphionteam.github.io/Zero-VC-demo/>
- **Demo / 试听**：<https://amphionteam.github.io/Zero-VC-demo/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
