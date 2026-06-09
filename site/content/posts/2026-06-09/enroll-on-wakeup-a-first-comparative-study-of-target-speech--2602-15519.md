---
title: "Enroll-on-Wakeup: A First Comparative Study of Target Speech Extraction for Seamless Interaction in Real Noisy Human-Machine Dialogue Scenarios"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#人机交互</span> <span class="tag-pill tag-pill-soft">#生成式模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.15519</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.15519" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.15519" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Enroll-on-Wakeup框架，利用唤醒词片段作为注册语音进行目标说话人提取，首次系统评估了判别式和生成式模型在真实噪声场景下的表现。
</div>

## 👥 作者与机构

**Yiming Yang** ¹ · Guangyong Wang · Haixin Guan · Yanhua Long

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TSE和人机交互方向的研究者。建议重点阅读§3的EoW框架设计和§4的实验结果，特别是表2中不同模型在EoW场景下的性能对比。可关注TTS增强部分对听感提升的效果。

## 🌍 研究背景

目标说话人提取（TSE）通常依赖预录的高质量注册语音，这在人机交互中会打断用户体验且不实用。现有TSE方法在注册语音质量下降时性能严重退化。本文首次系统研究利用自然交互中产生的唤醒词片段作为注册语音的EoW-TSE框架，并评估了判别式（如SepFormer）和生成式（如Diffusion）模型在真实噪声条件下的表现。

## 💡 核心创新

1. 提出EoW框架，利用唤醒词片段自动作为注册参考
2. 首次系统比较判别式和生成式TSE模型在EoW场景下的性能
3. 引入LLM-based TTS进行注册语音增强
4. 在真实人机对话噪声场景下进行多维度评估

## 🏗️ 模型架构

输入为混合语音和唤醒词片段（注册语音）。主干网络采用两种范式：判别式模型（如SepFormer）和生成式模型（如基于Diffusion的TSE）。关键模块包括：注册语音编码器提取目标说话人embedding，与混合语音特征融合后通过分离网络输出目标语音。TTS增强模块使用LLM-based TTS对短噪声注册语音进行扩增。输出为估计的目标说话人语音。

## 📚 数据集

- LibriMix（训练/评估，含不同信噪比）
- WSJ0-2mix（训练/评估）
- 真实噪声人机对话录音（评估，含唤醒词片段）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | LibriMix (test) | SepFormer (clean enrollment) 18.5 | **SepFormer (EoW) 12.3** | -6.2 dB |
| PESQ | LibriMix (test) | SepFormer (clean enrollment) 3.2 | **SepFormer (EoW) 2.5** | -0.7 |
| WER (%) | 真实噪声对话 | SepFormer (clean enrollment) 15.2 | **SepFormer (EoW) 28.6** | +13.4% |

实验表明，当前TSE模型在EoW场景下性能显著下降，SI-SDRi下降约6dB，PESQ下降0.7。TTS增强后，PESQ提升0.3，但WER仍比基线高10%。生成式模型在EoW下表现略优于判别式，但差距不大。消融实验验证了注册语音长度和噪声类型的影响。

## 🎯 结论与影响

本文提出的EoW框架为无缝人机交互中的TSE提供了新思路，但现有模型在短噪声注册条件下性能不足。TTS增强可改善听感，但语音识别精度仍有差距。该工作将推动TSE向更实用的交互场景发展，并启发注册语音质量鲁棒性研究。

## ⚠️ 局限与未解决问题

仅评估了有限几种TSE模型，未涵盖最新Mamba等架构；TTS增强可能引入伪影；实验仅在模拟和有限真实场景下进行，缺乏大规模真实用户研究；未报告推理延迟和计算开销。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
