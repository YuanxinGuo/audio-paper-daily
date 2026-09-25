---
title: "Beyond Model Size: Redesigning LiSenNet for embedded speech enhancement"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "将37k参数的子带双路径LiSenNet重构为NPU兼容的静态int8图，在STM32上以RTF 0.30实时运行且PESQ不降。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#模型量化</span> <span class="tag-pill tag-pill-soft">#边缘部署</span> <span class="tag-pill tag-pill-soft">#轻量级网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29866</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29866" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29866" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将37k参数的子带双路径LiSenNet重构为NPU兼容的静态int8图，在STM32上以RTF 0.30实时运行且PESQ不降。
</div>

## 👥 作者与机构

Cl\'ement Laroche · Rasmus Kongsgaard Olsson

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做嵌入式语音增强、TinyML音频部署的工程研究者与MCU固件工程师阅读。建议通读，重点看 §3 中循环瓶颈替换为卷积频率/时间 mixer 的设计、int8 静态化改写细节，以及表 2 的 FP32/int8 对比与 4.83 ms 延迟数据；若只关心算法可跳过 NPU 算子约束部分。

## 🌍 研究背景

此前轻量语音增强（如 LiSenNet、DTLN、RNNoise 系）已把参数量与 MACs 压到几十 k 量级，名义上适配 MCU；但这些网络依赖 RNN/GRU 等动态算子与动态量化范围，无法映射到 STM32 Neural-ART 这类只支持静态 int8 算子集的 NPU。本文要解决的是：在保持增强质量的前提下，把子带双路径模型改写成受限 NPU 可执行的静态图，并验证实时性。

## 💡 核心创新

1. 用卷积频率/时间 mixer 替换循环瓶颈，消除动态状态算子
2. 将不支持算子改写为静态 int8 兼容原语
3. 解码器采用有界激活以抑制量化后质量下降
4. 对比无状态感受野重算与持久流式状态的效率

## 🏗️ 模型架构

输入为子带分解后的时频特征，主干沿用 LiSenNet 的子带双路径结构：频率维与时间维分别由卷积 mixer 建模，替代原 GRU 循环瓶颈；所有算子改写为静态 int8 可执行原语，解码器使用有界激活（如 clamp 型）限制量化动态范围。模型仅 37k 参数，输出为增强后的子带谱并重建时域波形，整体以持久流式状态在 NPU 上逐帧推理。

## 📚 数据集

- VoiceBank-DEMAND（评估，PESQ 指标）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 循环 LiSenNet FP32 3.01 | **3.08** | +0.07 |
| PESQ | VoiceBank-DEMAND | 循环 LiSenNet int8 2.93 | **3.01** | +0.08 |
| RTF | STM32N6570-DK（16 ms hop） | 无状态感受野重算（同帧率，慢一个数量级） | **4.83 ms / hop，RTF 0.30** | 约 10× 加速 |

摘要给出 VoiceBank-DEMAND 上 PESQ：FP32 3.08 vs 3.01、int8 3.01 vs 2.93，量化后仍超过循环基线。部署于 STM32N6570-DK，每 16 ms hop 耗时 4.83 ms，RTF 0.30；无状态感受野重算虽加速器利用率更高但慢一个数量级。摘要未报告 SI-SDR、参数量以外的内存占用与能耗数据。

## 🎯 结论与影响

最强结论是：在受限 NPU 上，参数量、算子兼容性、量化范围与持久流式状态必须协同设计，才能同时保住质量与实时性。这为 MCU 端语音增强提供了可复用的改写范式，也提示后续轻量网络设计应把 NPU 算子集作为一等约束，对耳机、助听器等低功耗产品落地有直接参考价值。

## ⚠️ 局限与未解决问题

仅在 VoiceBank-DEMAND 单一数据集、单一 NPU 平台验证，泛化性未知；未报告内存占用、能耗与功耗实测；缺少与 DTLN、RNNoise 等同类 MCU 方案的横向对比；无消融量化各改写模块的独立贡献；PESQ 提升幅度较小，主观听感未评估。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
