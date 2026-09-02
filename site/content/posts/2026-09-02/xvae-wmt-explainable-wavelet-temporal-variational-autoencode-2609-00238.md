---
title: "XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencoder for Blind Source Separation of Heart and Lung Sounds"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出无监督可解释生成式AI模型XVAE-WMT，结合VAE、小波变换和时序一致性损失，实现心音与肺音盲源分离，无需配对干净数据。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#生物声学</span> <span class="tag-pill tag-pill-soft">#生成式AI</span> <span class="tag-pill tag-pill-soft">#可解释AI</span> <span class="tag-pill tag-pill-soft">#小波变换</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.00238</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.00238" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.00238" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无监督可解释生成式AI模型XVAE-WMT，结合VAE、小波变换和时序一致性损失，实现心音与肺音盲源分离，无需配对干净数据。
</div>

## 👥 作者与机构

**Yasaman Torabi** ¹ · Shahram Shirani · James P. Reilly

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事生物医学信号处理、语音分离及可解释AI的研究者。建议重点阅读方法部分（第3节）和实验部分（第4节），特别是关于SHAP特征选择和时序一致性损失的消融。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

心音和肺音分离是生物医学信号处理的关键任务，有助于心肺疾病诊断。现有监督方法依赖配对干净数据，且基于STFT的VAE方法缺乏潜在空间可解释性。本文旨在开发无监督、可解释的分离算法，无需配对数据，同时提升时频定位能力。

## 💡 核心创新

1. 引入CWT前端替代STFT，提升时频定位
2. 结合SHAP实现潜在特征降维，保持分离质量
3. 提出时序一致性损失增强时间连续性
4. 无需配对干净录音的无监督生成式框架
5. 后验输出掩码提升分离性能

## 🏗️ 模型架构

输入为心音和肺音混合信号，经连续小波变换（CWT）得到时频表示，送入变分自编码器（VAE）编码为潜在变量。编码器采用卷积结构，解码器重建时频表示。关键模块包括SHAP特征选择（保留前75%潜在特征）和时序一致性损失。输出通过后验掩码得到分离的心音和肺音时频表示，再逆变换为时域信号。

## 📚 数据集

- 数据集1（评估，心音肺音混合，具体名称未给出）
- 数据集2（评估，具体名称未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SDR | 未指定 | 未给出 | **26.8 dB** | 未给出 |
| SIR | 未指定 | 未给出 | **32.8 dB** | 未给出 |
| SAR | 未指定 | 未给出 | **28.6 dB** | 未给出 |

摘要报告了在两个数据集上的SDR、SIR和SAR指标，分别达到26.8 dB、32.8 dB和28.6 dB，但未提供与基线方法的对比或消融实验细节。SHAP降维至前75%潜在特征仍能保持分离质量，表明潜在空间具有可解释性。

## 🎯 结论与影响

XVAE-WMT实现了无需配对数据的无监督心音肺音分离，通过CWT和时序一致性损失提升了性能，并利用SHAP增强了可解释性。该工作为生物声学分离提供了新思路，可能推动可解释生成式AI在医疗信号处理中的应用，但需进一步验证泛化性。

## ⚠️ 局限与未解决问题

摘要未提供与现有方法的定量对比，缺乏消融实验验证各组件贡献。数据集细节和规模未说明，可能影响泛化评估。未提及计算复杂度和推理延迟，实际应用可行性待考。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-02/">← 返回 2026-09-02 速递</a></div>
