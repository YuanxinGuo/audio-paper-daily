---
title: "Fr\\'echet Distance Loss on Speech Representations for Text-to-Speech Synthesis"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出SR-FD损失，通过匹配语音表示的分布来提升少步扩散TTS的可懂度，在Seed-TTS上降低WER 36.5%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#分布正则化</span> <span class="tag-pill tag-pill-soft">#少步采样</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.06027</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.06027" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.06027" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SR-FD损失，通过匹配语音表示的分布来提升少步扩散TTS的可懂度，在Seed-TTS上降低WER 36.5%。
</div>

## 👥 作者与机构

**Ho-Lam Chung** ¹ · Kuan-Po Huang · Bo-Ru Lu · Hung-yi Lee

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS和生成模型研究者。重点读§3方法部分和§4实验。建议先看§3.2的SR-FD损失定义，再对比表1的WER结果。

## 🌍 研究背景

少步扩散和流匹配TTS模型通常使用局部目标（如条件流匹配、重构损失）训练，这些损失优化稳定但未考虑生成语音是否符合高质量语音分布。现有方法依赖判别器或推理时计算，增加复杂度。本文旨在设计一种训练时的分布正则化器，无需额外模块，提升少步采样语音的可懂度。

## 💡 核心创新

1. 提出Speech Representation Fréchet Distance (SR-FD)损失
2. 利用冻结Whisper和CTC特征的均值和协方差匹配
3. 在微调阶段使用与部署相同的少步采样器
4. 无需判别器或推理时额外计算
5. 在Seed-TTS上实现四步采样超越十步基线

## 🏗️ 模型架构

基于tokenizer-free的流匹配自回归TTS模型（Seed-TTS）。输入文本编码为条件，主干为流匹配网络。微调时，模型使用四步采样器合成语音，提取Whisper和CTC特征，计算其与预计算参考统计量的Fréchet距离作为额外损失。参考统计量来自三个互补内容目标（原始文本、ASR转录、对齐特征）。

## 📚 数据集

- Seed-TTS英文内部数据集（训练/微调/评估，未公开规模）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER (%) | Seed-TTS英文测试集 | VoxCPM2四步基线 2.2279 | **SR-FD四步微调 1.4147** | -0.8132 (-36.5%) |
| WER (%) | Seed-TTS英文测试集 | VoxCPM2十步基线 1.7366 | **SR-FD四步微调 1.4147** | -0.3219 (-18.5%) |

SR-FD四步微调在WER上显著优于原四步和十步基线，且说话人相似度和客观质量指标与十步基线持平。错误分析表明改进来自所有提示长度的内容替换减少。消融实验验证了三个内容目标组合的必要性。

## 🎯 结论与影响

SR-FD损失有效提升了少步TTS的可懂度，无需额外模型或推理开销。该方法为分布正则化在生成模型中的应用提供了新思路，有望推广到其他语音生成任务。工业上可降低TTS系统的推理步数而不牺牲质量。

## ⚠️ 局限与未解决问题

仅在Seed-TTS英文数据上验证，未测试其他TTS架构或语言。参考统计量需预先计算，可能对数据分布变化敏感。未报告计算开销或训练时间对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
