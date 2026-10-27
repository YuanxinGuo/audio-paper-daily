---
title: "Support-guided OOD Removal with Diffusion"
date: 2026-10-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "用扩散先验加损坏支撑掩码，迭代恢复被局部OOD污染的信号，覆盖图像与乐器/语音音频。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#OOD鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.33194</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/voilalab/SORD" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">voilalab/SORD</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.33194" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.33194" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/voilalab/SORD" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用扩散先验加损坏支撑掩码，迭代恢复被局部OOD污染的信号，覆盖图像与乐器/语音音频。
</div>

## 👥 作者与机构

**Alireza Kheirandish** ¹ · Sara Fridovich-Keil

**机构**：德克萨斯大学奥斯汀分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做扩散先验、盲源分离与鲁棒信号恢复的研究者。值得通读，重点看 §3 的 SORD 迭代算法与支撑引导采样公式，以及音频实验表（乐器/人声局部污染）。可先看与 posterior-sampling inpainting 的对比，再核对是否报告推理步数与耗时。

## 🌍 研究背景

真实信号常被分布未知的局部结构化扰动污染，如录音中偶发背景声、照片水印、投影阴影。现有做法依赖成对干净-污染数据训练监督网络，或对每种源单独训练扩散模型做分离，前者受限于配对数据获取，后者模型数量随源数增长。本文要在无配对数据、无污染统计模型的前提下，仅凭污染支撑二值图与一个干净信号预训练扩散模型完成恢复。

## 💡 核心创新

1. 仅用污染支撑二值图 + 单一干净扩散先验，无需配对数据
2. 支撑引导的迭代采样，将掩码约束注入扩散后验采样
3. 统一框架跨图像与音频，覆盖乐器与人声局部污染
4. 与 posterior-sampling inpainting 同先验同掩码下对比更优

## 🏗️ 模型架构

输入为观测 y 与污染支撑二值掩码 m。方法不训练新网络，直接复用预训练于干净信号的扩散模型作为先验。迭代过程交替两步：在支撑区域外保持观测一致（数据一致性投影），在支撑区域内用扩散反向采样补全，形成类似投影梯度式的交替采样；每步以掩码约束条件化去噪网络输出，逐步收敛到干净信号 x。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- 自然图像与人脸（评估，含手写数字、水印、阴影等局部污染）
- 乐器录音（评估，含其他乐器与人类语音的时域局部污染）

## 📊 实验结果

摘要仅定性说明 SORD 与 posterior-sampling inpainting（同先验同掩码）、需为每个源单独训练扩散模型的源分离基线，以及若干基准上的成对监督网络相比具有竞争力并常更优，未给出 SI-SDR、PESQ 等具体数值，故无法列表量化。

## 🎯 结论与影响

最强结论是：单一干净扩散先验加支撑掩码即可在无配对数据下恢复局部 OOD 污染信号，并在多类基准上追平或超过专用基线。这为扩散先验用于鲁棒分离与恢复提供了轻量范式，工业上可降低对配对数据和逐源模型的依赖。

## ⚠️ 局限与未解决问题

支撑掩码需已知，实际中如何自动获取未讨论；音频仅定性描述，缺 SI-SDR/PESQ 等量化与推理步数、耗时报告；未给出消融说明掩码精度敏感性；与监督分离基线的对比范围有限。

## 🔗 开源资源

- **代码**：<https://github.com/voilalab/SORD>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-27/">← 返回 2026-10-27 速递</a></div>
