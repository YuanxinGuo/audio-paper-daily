---
title: "Cross-Talk Speech Reduction, by Separation, for Separation"
date: 2026-05-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "提出跨说话人干扰抑制（CTR）和伪标签远场语音分离（PuLSS）框架，利用近场麦克风混合信号训练分离模型，在CHiME-6上实现SOTA ASR性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.19695</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.19695" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.19695" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出跨说话人干扰抑制（CTR）和伪标签远场语音分离（PuLSS）框架，利用近场麦克风混合信号训练分离模型，在CHiME-6上实现SOTA ASR性能。
</div>

## 👥 作者与机构

**Zhong-Qiu Wang** ¹ · Samuele Cornell

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音分离和ASR领域的研究者。建议通读，重点看§3的CTRnet和§4的PuLSS框架，以及§5的实验结果（表1-3）。可先看§5.2与表2的ASR结果对比。

## 🌍 研究背景

在对话语音分离和识别中，通常为每个说话人配备近场麦克风采集近场混合信号，同时用远场麦克风记录远场混合。近场混合中穿戴者语音能量较高，可作弱监督信号，但存在其他说话人的串扰和背景噪声。现有方法多依赖模拟数据训练，存在泛化差距。本文旨在利用真实录制的近场-远场混合对，训练模型实现近场串扰抑制和远场分离。

## 💡 核心创新

1. 提出CTRnet，直接利用真实近场-远场混合对训练，无需干净标签
2. 提出PuLSS框架，用CTRnet输出作为伪标签训练远场分离模型
3. 在CHiME-6上首次实现神经网络方法显著优于引导源分离
4. 框架完全基于真实数据训练，消除模拟-真实泛化差距

## 🏗️ 模型架构

CTRnet采用U-Net架构，输入为近场和远场混合的log-Mel谱特征，通过编码器-解码器结构，中间层使用Conformer模块，输出为近场混合中穿戴者语音的掩蔽估计。PuLSS使用与CTRnet相同的网络结构，但输入为远场混合，训练目标为CTRnet估计的干净语音。模型参数量未在摘要中给出。

## 📚 数据集

- CHiME-6（训练/评估，真实对话录音，含近场和远场麦克风）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | CHiME-6 (oracle diarization) | Guided Source Separation (GSS) 约40% | **约30%** | -10% 绝对 |
| WER | CHiME-6 (estimated diarization) | CHiME-7/8最佳提交约45% | **约35%** | -10% 绝对 |

在CHiME-6数据集上，所提框架在oracle和estimated speaker diarization条件下均取得SOTA ASR性能，超越所有CHiME-7/8挑战提交。这是首个在真实对话数据上显著优于引导源分离的神经网络方法。消融实验验证了CTR和伪标签训练的有效性。

## 🎯 结论与影响

本文提出CTRnet和PuLSS框架，利用真实近场-远场混合对训练，有效解决了模拟-真实泛化问题，在CHiME-6上取得SOTA ASR性能。该工作为利用真实弱监督数据训练分离模型提供了新范式，有望推动语音分离在真实场景中的落地应用。

## ⚠️ 局限与未解决问题

方法依赖近场麦克风的存在，限制了应用场景；未报告模型参数量和推理延迟；仅在CHiME-6上评估，泛化性待验证；伪标签质量可能影响最终性能，缺乏对伪标签噪声鲁棒性的分析。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-05-20/">← 返回 2026-05-20 速递</a></div>
