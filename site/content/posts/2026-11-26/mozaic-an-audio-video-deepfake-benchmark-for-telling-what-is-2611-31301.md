---
title: "MOZAIC: An Audio-Video Deepfake Benchmark for Telling What Is Fake"
date: 2026-11-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "构建音视频配对四分类深度伪造基准，量化视觉与语音模态贡献，评测12个MLLM与训练检测器。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态基准</span> <span class="tag-pill tag-pill-soft">#音视频伪造检测</span> <span class="tag-pill tag-pill-soft">#语音转换</span> <span class="tag-pill tag-pill-soft">#可解释性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.31301</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://vectorinstitute.github.io/mozaic/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">vectorinstitute.github.io/mozaic/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.31301" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.31301" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://vectorinstitute.github.io/mozaic/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建音视频配对四分类深度伪造基准，量化视觉与语音模态贡献，评测12个MLLM与训练检测器。
</div>

## 👥 作者与机构

**Shaina Raza** ¹ · Mohamed Hafez · Ahmed Y. Radwan · Khalid Elgazzar · Kathryn Hume

**机构**：Vector Institute

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 deepfake 检测、多模态可信 AI 的研究者。值得通读，重点看 §3 四路标签构造与 T1~T4 任务定义、表 2 的 MLLM 四分类结果、以及 held-out 生成器泛化实验。可先看 T1 的 35.6% vs 98.4% 对比，再读 LoRA 解释性提升部分。

## 🌍 研究背景

音视频 deepfake 检测已有大量二分类基准（真/假），主流方法用 CNN/ViT 或 MLLM 做二分类判别。但二分类标签无法区分检测器依赖画面、声音还是编码痕迹，导致模型在跨生成器时性能骤降却难以诊断。本文要解决的是：构建一个能直接测量各模态贡献的配对基准，并系统评测 MLLM 与专用检测器在真实性、操纵类型、身份验证与解释四类任务上的表现。

## 💡 核心创新

1. 四路配对标签：每条源片段同时发布真/假视频×真/假音频四种组合
2. 覆盖换脸、整帧视频扩散与语音转换三类伪造
3. 四任务体系 T1~T4 含解释性评估
4. 系统评测 12 个 AV-MLLM 并做 LoRA 微调

## 🏗️ 模型架构

基准本身不含单一网络：输入为配对音视频片段，伪造由 inner-face swapping、whole-frame video diffusion 与 voice conversion 三类生成器产生。评测侧分两条线：一是 12 个现成 AV 多模态大模型（如 Qwen2.5-Omni、OmniVinci）直接零样本推理四分类；二是训练四个专用检测器（视觉/音频/融合分支）做 T1 判别；三是对 MLLM 用 LoRA 微调以提升 T4 解释质量。输出为四路真伪标签、操纵类型、身份匹配与文本解释。

## 📚 数据集

- MOZAIC（训练+评估，137,745 片段 / 15,014 源对）
- MOZAIC-SMALL（轻量评估子集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 四路 T1 准确率 | MOZAIC | 最佳 MLLM 零样本 | **35.6%** | — |
| T1 准确率 | MOZAIC | 最佳 MLLM 35.6% | **训练检测器 98.4%** | +62.8% |
| 解释得分 | MOZAIC T4 | OmniVinci 4.17 | **LoRA 微调 7.40** | +3.23 |
| T1 准确率（换脸生成器留出） | MOZAIC held-out | 同分布 98.4% | **78.3%** | -20.1% |

最佳 MLLM 在四路 T1 仅 35.6%，且对纯视频伪造识别率 43.6% 远高于纯语音伪造 7.5%，说明模型严重偏视觉。训练检测器达 98.4%，但换脸生成器留出后降至 78.3%，泛化明显不足。LoRA 微调显著提升解释分数（OmniVinci 4.17→7.40，Qwen2.5-Omni 4.42→6.98）。

## 🎯 结论与影响

最强结论是：现有 AV-MLLM 在细粒度音视频真伪判别上远弱于专用检测器，且几乎忽略语音伪造线索。该基准为后续模态归因与跨生成器泛化研究提供可量化平台，对内容审核落地提示需专用检测器而非直接依赖 MLLM。

## ⚠️ 局限与未解决问题

伪造生成器种类有限（三类），未报推理延迟与算力开销；held-out 泛化仅测换脸一种生成器；语音伪造仅 voice conversion，缺 TTS 与拼接攻击；四路标签构造可能引入生成伪影偏差。

## 🔗 开源资源

- **项目主页**：<https://vectorinstitute.github.io/mozaic/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-11-26/">← 返回 2026-11-26 速递</a></div>
