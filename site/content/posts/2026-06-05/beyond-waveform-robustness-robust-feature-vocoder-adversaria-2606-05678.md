---
title: "Beyond Waveform Robustness: Robust Feature-Vocoder Adversarial Attacks on Automatic Speech Recognition"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#对抗攻击"]
summary: "提出基于SSL特征空间的对抗攻击方法，通过声码器重构波形，提升黑盒迁移性和防御绕过能力。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#对抗攻击</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#黑盒攻击</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.05678</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.05678" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.05678" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于SSL特征空间的对抗攻击方法，通过声码器重构波形，提升黑盒迁移性和防御绕过能力。
</div>

## 👥 作者与机构

**Yifan Liao** ¹ · Zongmin Zhang · Zhen Sun · Yuhui Sun · Xinhu Zheng · Xinlei He

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR安全与鲁棒性方向的研究者。建议重点阅读§3方法部分和§4实验对比，特别是表1和表2的WER提升结果。

## 🌍 研究背景

ASR系统易受对抗攻击，但现有方法存在两个局限：黑盒迁移性差，且易被基于波形空间的防御机制缓解。本文旨在通过将攻击从波形空间转移到自监督学习（SSL）特征空间，利用声码器重构波形，同时解决迁移性和防御绕过问题。

## 💡 核心创新

1. Clean-Referenced Feature-Vocoder Attack框架
2. 将对抗搜索空间从波形转移到SSL表示
3. 通过声码器将特征扰动重构为语音波形
4. 仅基于Whisper-small代理模型实现跨模型迁移

## 🏗️ 模型架构

输入为原始语音波形，通过SSL模型（如HuBERT）提取特征表示；在特征空间添加对抗扰动，然后使用声码器（如HiFi-GAN）将扰动后的特征重构为波形。代理模型为Whisper-small，攻击优化在特征空间进行，最终输出对抗波形。

## 📚 数据集

- LibriSpeech（训练/评估，clean和other子集）
- Common Voice（评估，多语言）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | SOTA基线攻击（如FGSM）WER 12.3% | **38.9%** | +26.6% |
| WER | LibriSpeech test-other | SOTA基线攻击WER 15.1% | **51.3%** | +36.2% |

在Whisper-small代理模型上优化，攻击迁移至黑盒模型（如Wav2Vec2、HuBERT）时WER提升显著，最高达+26.6%。针对多种训练防御（如对抗训练、随机平滑），攻击仍有效，WER提升+36.2%。消融实验验证了特征空间扰动和声码器重构的关键作用。

## 🎯 结论与影响

本文揭示了当前ASR鲁棒性评估的盲点：基于波形空间的攻击和防御均存在局限。所提方法通过特征空间攻击有效提升了迁移性和防御绕过能力，为ASR安全研究提供了新视角，可能推动更鲁棒的防御机制设计。

## ⚠️ 局限与未解决问题

仅使用Whisper-small作为代理模型，未探索更大模型或不同架构；未评估对实时系统的影响；声码器可能引入额外计算开销；未在真实世界噪声环境下测试。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
