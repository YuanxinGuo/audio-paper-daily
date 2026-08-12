---
title: "DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation"
date: 2026-08-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "DAVE提出解耦的音视频增强框架，通过大规模语料DAVE-Corpus和渐进多目标优化，在真实场景语音分离中提升鲁棒性。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频融合</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#多目标优化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.09288</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.09288" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.09288" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>DAVE提出解耦的音视频增强框架，通过大规模语料DAVE-Corpus和渐进多目标优化，在真实场景语音分离中提升鲁棒性。
</div>

## 👥 作者与机构

**Wei Zhou** ¹ · Wanyi Ning · Yinshang Guo · Qianxiao Fang · Haitao Qian · Yingpeng Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音视频语音增强、分离的研究者。建议重点阅读第3节（DAVE-Corpus构建）和第4节（渐进多目标优化），以及第5节的实验对比。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

真实场景下的音视频语音增强面临视觉输入不可靠和缺乏大规模真实声学训练数据两大挑战。现有方法通常将视觉特征直接融合进分离网络，导致对降质视觉信号敏感。本文旨在通过解耦框架和构建大规模语料来解决这些问题，提升在真实场景下的鲁棒性。

## 💡 核心创新

1. 构建DAVE-Corpus大规模训练语料，含219,411个混合样本
2. 提出渐进多目标优化策略，联合优化分离、可懂度、说话人身份和感知质量
3. 设计认证选择性增强链，仅在无参考分区应用处理，保证参考指标不降级
4. 解耦视觉特征融合，提高对视觉降质的鲁棒性

## 🏗️ 模型架构

DAVE采用解耦架构：视觉特征提取后不直接注入分离网络，而是通过辅助分支指导增强。输入为音视频流，音频经编码器得到特征，视觉经预训练模型提取嵌入。主干网络可能采用Conformer或类似结构进行分离。输出为增强后的语音波形。具体细节未在摘要中给出。

## 📚 数据集

- DAVE-Corpus（训练，219,411个混合样本，由公共会议语料组合声学增强生成）
- Real-World Audio-Visual Speech Enhancement Challenge（评估）

## 📊 实验结果

摘要未提供具体数值指标，但提到在真实世界音视频语音增强挑战赛上验证了DAVE在真实混合场景和视觉降质条件下的鲁棒性。具体指标如SI-SDR、PESQ等未给出。

## 🎯 结论与影响

DAVE通过解耦框架和大规模语料，有效提升了真实场景下音视频语音增强的鲁棒性，尤其在视觉输入不可靠时。该工作为音视频增强提供了新思路，可能推动该领域在真实场景的落地应用。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能存在的问题：DAVE-Corpus基于会议语料，可能缺乏多样性；解耦架构可能增加计算开销；未报告推理延迟；对比基线未明确。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-12/">← 返回 2026-08-12 速递</a></div>
