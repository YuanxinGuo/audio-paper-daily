---
title: "DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexity Monaural Speech Enhancement"
date: 2026-06-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双分支混合神经网络DBHN-Net，结合ANN与SNN，在保持语音增强性能的同时大幅降低计算复杂度。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#SNN</span> <span class="tag-pill tag-pill-soft">#ANN</span> <span class="tag-pill tag-pill-soft">#Mamba</span> <span class="tag-pill tag-pill-soft">#低复杂度</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.05911</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.05911" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.05911" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双分支混合神经网络DBHN-Net，结合ANN与SNN，在保持语音增强性能的同时大幅降低计算复杂度。
</div>

## 👥 作者与机构

**Cunhang Fan** ¹ · Enrui Liu · Jing Zhou · Jian Kang · Jie Li · Andong Li · Jian Zhou · Zhao Lv · … 等 1 人

**机构**：安徽大学 · 西安交通大学 · 中国科学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注低功耗语音增强部署的研究者。建议重点阅读§3.2 BandSplit与TF-Mamba模块设计，以及§3.3交互与融合模块。可对比表2中的复杂度与性能权衡。

## 🌍 研究背景

基于ANN的语音增强方法性能优异，但高计算复杂度和能耗阻碍了前端部署。SNN虽能降低功耗，但离散二进制激活和时空动态导致信息损失。现有方法难以兼顾性能与低复杂度。本文旨在设计一种混合网络，利用ANN弥补SNN的信息损失，同时通过SNN降低功耗，并引入Mamba模块进一步压缩能耗。

## 💡 核心创新

1. 提出ANN与SNN双分支混合架构
2. 设计BandSplit和TF-Mamba模块压缩能耗
3. 提出SFEG和ITB组件减少信息损失
4. 设计交互模块促进分支间信息融合
5. 提出TF交叉注意力融合模块自适应引导SNN保留关键信息

## 🏗️ 模型架构

输入为单通道时频特征，经BandSplit模块分割频带后分别送入ANN和SNN分支。ANN分支采用TF-Mamba模块提取全局特征；SNN分支由多个SFEG和ITB堆叠，通过残差连接保留信息。两分支间通过交互模块进行多阶段信息交换，最后经TF交叉注意力融合模块合并双分支特征，输出增强后的时频表示。

## 📚 数据集

- DNS-Challenge（训练/评估，公开数据集）
- VoiceBank+DEMAND（训练/评估，公开数据集）
- LibriTTS（训练/评估，公开数据集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank+DEMAND | DCCRN 2.94 | **3.12** | +0.18 |
| SI-SDR (dB) | VoiceBank+DEMAND | DCCRN 18.2 | **19.5** | +1.3 |
| 计算复杂度 (GMACs) | VoiceBank+DEMAND | DCCRN 7.2 | **0.96** | -86.7% |

在三个公开数据集上，DBHN-Net在PESQ和SI-SDR上均优于DCCRN等基线，同时计算复杂度平均降低7.5倍（GMACs从7.2降至0.96）。消融实验验证了双分支、BandSplit、TF-Mamba及融合模块的有效性。

## 🎯 结论与影响

DBHN-Net通过ANN与SNN双分支混合设计，在保持优异语音增强性能的同时大幅降低计算复杂度，为低功耗前端部署提供了可行方案。该工作启发后续研究探索SNN在音频处理中的潜力，并可能推动助听器、可穿戴设备等实时应用。

## ⚠️ 局限与未解决问题

未报告推理延迟或实际功耗测量，仅以GMACs衡量复杂度；SNN分支的能耗优势缺乏硬件实测验证；仅在干净和噪声条件下测试，未见混响场景；未与最新SNN基线（如Spiking-UNet）对比。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-05/">← 返回 2026-06-05 速递</a></div>
