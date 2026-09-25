---
title: "Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Cues"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "用单个自回归 LLM 主干统一处理同步（唇动/手势）与异步（注册音频/文本）线索的目标说话人提取，并提出 self-enrollment 机制。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#多模态语音处理</span> <span class="tag-pill tag-pill-soft">#自回归生成</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29238</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://alexwxwu.github.io/tseomni-main/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">alexwxwu.github.io/tseomni-main/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29238" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29238" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://alexwxwu.github.io/tseomni-main/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用单个自回归 LLM 主干统一处理同步（唇动/手势）与异步（注册音频/文本）线索的目标说话人提取，并提出 self-enrollment 机制。
</div>

## 👥 作者与机构

**Wenxuan Wu** ¹ · Shuhan Zhang · Shuai Wang · Haizhou Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态 TSE、LLM-based 语音生成的研究者精读。建议先看 §3 的 self-enrollment 与 token 上下文构造，再看表 2 的视觉帧损坏鲁棒性实验与流式推理部分；对纯判别式 TSE 背景的读者可略读 baseline 对比细节。

## 🌍 研究背景

目标说话人提取此前多为每种线索训练独立提取器：视觉线索（唇动）用 AV-Conformer/AV-SEPFormer 类判别模型，听觉注册线索用 speaker embedding 条件化的分离网络，文本线索则依赖 CLIP 类对齐。这些方法线索异构、难以共享主干，且视觉系统在帧损坏或缺失时性能骤降，需 corruption-matched 训练才能维持鲁棒。本文要解决的核心问题是：能否用单一自回归 LLM 主干同时覆盖同步与异步线索，并在视觉帧缺失时靠 token 历史补偿。

## 💡 核心创新

1. 单一自回归 LLM 主干统一同步与异步线索的 TSE
2. self-enrollment：用自身历史输出语义 token 构成目标语音上下文
3. 视觉前缀 + token 历史实现视听补偿，帧缺失仍可用
4. 支持流式推理与稀疏重叠、多说话人干扰场景

## 🏗️ 模型架构

输入为注册线索（异步音频或文本，或短视觉前缀）与混合语音；主干为自回归 LLM，以 next-token prediction 逐帧预测目标语音的语义 token。关键模块是 self-enrollment：每步以上一步预测的语义 token 作为目标语音上下文，与注册线索初始化拼接，形成连续目标表征。同步视觉线索（唇动、共语手势）以视觉前缀形式注入，视觉帧缺失时模型退化为仅依赖 token 历史，实现视听补偿。输出为语义 token 序列，可解码回目标语音波形，支持流式推理。摘要未给出参数量。

## 📚 数据集

- VoxCeleb2（评估，零样本与视觉损坏鲁棒性测试）
- LRS3（评估，零样本 TSE）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SpeechBERTScore | VoxCeleb2 | 强判别式与生成式基线（具体值未给出） | **0.81** | 持平 |
| SpeechBERTScore | LRS3（zero-shot） | 强判别式与生成式基线（具体值未给出） | **0.89** | 持平 |
| SpeechBERTScore | VoxCeleb2（2 s 干净视觉后移除剩余视觉帧） | 无对应基线 | **0.81** | 与完整视觉持平 |

摘要报告：干净视觉下 TSE-Omni 在 VoxCeleb2 与 LRS3 零样本上 SpeechBERTScore 分别达 0.81 与 0.89，与强判别式和生成式基线持平，且 DNSMOS 更高。VoxCeleb2 上先给 2 s 干净视觉再移除后续视觉帧，SpeechBERTScore 仍保持 0.81，说明 token 历史可补偿视觉缺失。模型在稀疏重叠与多说话人干扰下仍可用，并支持流式推理。摘要未给出 SI-SDR、PESQ 等具体数值与消融细节。

## 🎯 结论与影响

最强结论是：单个自回归 LLM 主干即可统一同步与异步线索的 TSE，并在视觉帧缺失时靠 self-enrollment 维持性能。这为多模态 TSE 提供了“生成式统一主干”的新范式，可能推动后续研究放弃按线索分训的专用提取器。工业上，流式与视觉损坏鲁棒性对视频会议、车载语音等真实场景有直接价值。

## ⚠️ 局限与未解决问题

摘要仅报 SpeechBERTScore 与 DNSMOS，缺少 SI-SDR、PESQ 等分离/增强常用指标，也未给出与具体基线的数值对比表。视觉损坏实验只测了“2 s 干净后移除”一种模式，未覆盖随机帧丢失、模糊、遮挡等更真实 corruption。未报推理延迟与参数量，流式可行性缺乏效率证据。数据集仅 VoxCeleb2 与 LRS3，跨语言与噪声场景泛化未知。

## 🔗 开源资源

- **项目主页**：<https://alexwxwu.github.io/tseomni-main/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
