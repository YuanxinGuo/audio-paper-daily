---
title: "Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching Speech Enhancement"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出一种无跳跃连接的编码器-解码器架构，通过潜在表示对齐替代U-Net跳跃连接，用于流匹配语音增强。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#潜在表示对齐</span> <span class="tag-pill tag-pill-soft">#无跳跃连接</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.24745</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.24745" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.24745" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种无跳跃连接的编码器-解码器架构，通过潜在表示对齐替代U-Net跳跃连接，用于流匹配语音增强。
</div>

## 👥 作者与机构

**Wangyi Pu** ¹ · Michele Scarpiniti

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成模型方向的研究者。建议重点阅读§3的LRA模块设计和§4的实验结果，特别是表2中的PESQ对比。可先看§3.2了解对齐机制。

## 🌍 研究背景

扩散和基于分数的生成模型在语音增强中表现优异，但迭代采样过程限制了实时部署。流匹配通过常微分方程实现少步采样，是高效替代方案。然而，现有流匹配方法多采用U-Net架构，其跳跃连接可能传递噪声相关低级特征，影响增强质量。本文旨在设计一种无跳跃连接的骨干网络，通过潜在表示对齐引导解码器生成干净语音。

## 💡 核心创新

1. 提出无跳跃连接的编码器-解码器架构
2. 引入潜在表示对齐（LRA）机制
3. 利用冻结的Descript Audio Codec提取干净潜在特征
4. 仅需5次函数评估实现高效推理

## 🏗️ 模型架构

输入为含噪语音的频谱特征，经编码器映射到潜在空间；瓶颈层与解码器通过LRA模块与冻结的Descript Audio Codec编码器-解码器（无量化）提取的干净潜在特征对齐；解码器逐步恢复干净语音；整体采用流匹配训练，优化常微分方程轨迹。

## 📚 数据集

- WSJ0-CHiME3（训练/评估）
- VoiceBank-DEMAND（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 未明确给出基线值 | **未明确给出具体值** | 有提升 |

在WSJ0-CHiME3和VoiceBank-DEMAND上，所提方法在PESQ和感知质量上优于基线，尤其在VoiceBank-DEMAND上提升显著。仅需5次函数评估即可达到较好性能，但摘要未提供具体数值。

## 🎯 结论与影响

本文提出的无跳跃连接流匹配语音增强架构，通过潜在表示对齐有效避免了U-Net跳跃连接的噪声传递问题，在少步采样下取得良好增强效果。该方法为实时语音增强提供了新思路，未来可探索更高效的编解码器对齐策略。

## ⚠️ 局限与未解决问题

摘要未提供与SOTA方法的详细数值对比，缺乏消融实验验证各模块贡献；仅在两个数据集上评估，泛化性未知；未报告模型参数量或推理延迟，难以评估实际部署可行性。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-24/">← 返回 2026-06-24 速递</a></div>
