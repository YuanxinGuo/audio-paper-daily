---
title: "NPUsper: Eliminating Redundant Computation for Real-Time Whisper on Mobile NPUs"
date: 2026-07-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出NPUsper系统，通过消除冗余计算实现Whisper在移动NPU上的实时转录，显著降低延迟和功耗。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#移动端NPU</span> <span class="tag-pill tag-pill-soft">#流式推理</span> <span class="tag-pill tag-pill-soft">#冗余计算消除</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.01108</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/npusper/NPUsper" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">npusper/NPUsper</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.01108" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.01108" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/npusper/NPUsper" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出NPUsper系统，通过消除冗余计算实现Whisper在移动NPU上的实时转录，显著降低延迟和功耗。
</div>

## 👥 作者与机构

**Sihyeon Lee** ¹ · Hojeong Lee · Sungwon Woo · Chengpo Yan · Suman Banerjee · Seyeon Kim

**机构**：威斯康星大学麦迪逊分校 · 三星电子

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别与移动端部署研究者。建议通读，重点看§3（幻觉令牌检测）和§4（受控展开）。可复现代码。

## 🌍 研究背景

Whisper模型在移动NPU上实时流式转录面临两大挑战：一是流式推理中填充（padding）导致大量冗余计算；二是自回归解码的KV缓存和计算图调度开销大。现有流式系统如Faster-Whisper等未针对NPU优化。本文旨在消除这些冗余，实现低延迟、低功耗的实时转录。

## 💡 核心创新

1. 在线幻觉令牌检测：利用解码器交叉注意力时间模式识别幻觉令牌
2. 受控展开：将自回归解码转为K步块图，消除KV缓存冗余计算
3. 减少图调度开销：通过块图执行降低NPU调度次数

## 🏗️ 模型架构

输入为短音频片段（最小化携带信息）→ Whisper编码器 → 解码器交叉注意力层检测幻觉令牌并跳过 → 受控展开将自回归解码转换为K步块图，在NPU上高效执行 → 输出文本。系统设计避免填充，每个推理轮次处理短输入。

## 📚 数据集

- LibriSpeech（评估，clean/other）
- Common Voice（评估）
- TED-LIUM（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 每词延迟 | LibriSpeech clean | Faster-Whisper 1.0x | **0.21x** | -79% |
| TTFT | LibriSpeech clean | Faster-Whisper 1.0x | **0.03x** | -97% |
| 平均功耗 | LibriSpeech clean | Faster-Whisper 1.0x | **0.11x** | -89% |

NPUsper在LibriSpeech、Common Voice、TED-LIUM上相比Faster-Whisper、Whisper.cpp等基线，每词延迟降低最多4.84倍，TTFT降低最多33.2倍，平均功耗降低88.64%，同时保持相当的转录准确率（WER差异<0.5%）。消融实验验证了幻觉检测和受控展开各自的有效性。

## 🎯 结论与影响

NPUsper通过在线幻觉令牌检测和受控展开，显著提升了Whisper在移动NPU上的实时转录效率，延迟和功耗大幅降低。该工作为大型语音模型在边缘设备上的高效部署提供了新思路，有望推动实时语音交互应用。

## ⚠️ 局限与未解决问题

仅针对Whisper模型，未验证对其他自回归语音模型的泛化性；幻觉检测依赖阈值设定，可能影响鲁棒性；未报告不同NPU硬件上的性能差异。

## 🔗 开源资源

- **代码**：<https://github.com/npusper/NPUsper>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-02/">← 返回 2026-07-02 速递</a></div>
