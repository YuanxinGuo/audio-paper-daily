---
title: "QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出QC-GAN，用四元数Conformer生成器结合MetricGAN训练，以0.89M参数在VoiceBank+DEMAND上达到PESQ 3.48，性能媲美SOTA但参数量减半。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#四元数卷积</span> <span class="tag-pill tag-pill-soft">#Conformer</span> <span class="tag-pill tag-pill-soft">#MetricGAN</span> <span class="tag-pill tag-pill-soft">#参数高效</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.18611</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.18611" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.18611" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出QC-GAN，用四元数Conformer生成器结合MetricGAN训练，以0.89M参数在VoiceBank+DEMAND上达到PESQ 3.48，性能媲美SOTA但参数量减半。
</div>

## 👥 作者与机构

**Shogo Yamauchi** ¹ · Hideaki Tamori · Makoto Sakai · Yosuke Yamano · Tohru Nitta

**机构**：东京工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和轻量化模型研究者。建议重点读§3架构设计和§4实验对比，尤其是表1的参数量与PESQ关系。可复现其四元数模块设计。

## 🌍 研究背景

语音增强任务中，现有基于GAN的方法（如SEGAN、MetricGAN）虽能提升感知质量，但模型参数量大，难以部署在资源受限设备。Conformer结构在语音任务中表现优异，但标准Conformer参数量仍较高。四元数神经网络通过超复数表示编码多维度信息，可减少参数量。本文旨在结合四元数Conformer与MetricGAN，实现高保真且参数高效的语音增强。

## 💡 核心创新

1. 四元数Conformer生成器：用Hamilton积编码幅度和相位，减少参数
2. MetricGAN判别器：优化近似PESQ分数，提升感知质量
3. 35K超轻量变体：仅3.5万参数仍达PESQ 3.23

## 🏗️ 模型架构

输入含噪语音频谱→四元数Conformer生成器：先通过四元数卷积层提取特征，再经多个四元数Conformer块（含四元数多头自注意力和四元数前馈网络），最后输出增强频谱。生成器参数仅0.89M。判别器采用MetricGAN架构，以PESQ近似函数作为目标，优化生成器输出。

## 📚 数据集

- VoiceBank+DEMAND（训练/评估，包含28种噪声）
- DNS-Challenge 3（评估，真实场景噪声）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | MetricGAN+ (3.15) | **3.48** | +0.33 |
| 参数量 | VoiceBank+DEMAND | MetricGAN+ (1.86M) | **0.89M** | -52% |

QC-GAN在VoiceBank+DEMAND上PESQ达3.48，优于MetricGAN+的3.15，且参数量仅0.89M（减少52%）。35K参数变体PESQ为3.23，超越多数传统方法。在DNS-Challenge 3上验证了泛化能力，但未提供具体数值。

## 🎯 结论与影响

QC-GAN以极低参数量实现了与SOTA相当的语音增强性能，证明了四元数Conformer在参数效率上的优势。该工作为轻量化语音增强提供了新思路，有望推动在移动设备上的实时应用。

## ⚠️ 局限与未解决问题

仅报告PESQ指标，缺乏其他客观指标（如STOI、SI-SDR）和主观听感测试。DNS-Challenge 3上未给出具体数值，泛化性证据不足。未与最新轻量模型（如TinyLSTMs）对比。未提供推理延迟或计算量（FLOPs）。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
