---
title: "Averaging Collusion Breaks Traceability in Personalized Neural Audio Watermarking"
date: 2026-11-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "发现个性化神经音频水印在多样本平均共谋下溯源失效率高达87.7-99.7%，并提出置信度筛选缓解。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#安全性评估</span> <span class="tag-pill tag-pill-soft">#共谋攻击</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.04400</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Silwan5z/neural-audio-watermark-collusion-attack" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Silwan5z/neural-audio-watermark-collusion-attack</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.04400" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.04400" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Silwan5z/neural-audio-watermark-collusion-attack" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发现个性化神经音频水印在多样本平均共谋下溯源失效率高达87.7-99.7%，并提出置信度筛选缓解。
</div>

## 👥 作者与机构

**Yangming Liu** ¹ · Haiyun Li · Dongfu Song · Ziang Xu · Jiehui Luo · Yining Zhang · Zhiyong Wu

**机构**：清华大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频水印、模型溯源与安全评估的研究者阅读。值得通读，重点看 §3 的共谋攻击设计与表 2 的五系统失效率对比，以及 §4 的 payload-aware 加权攻击与置信度筛选实验。若只关心防御，可直接看置信度筛选小节与结论。

## 🌍 研究背景

个性化神经音频水印把用户专属 payload 嵌入音频，用于追踪泄露副本的来源。此前评估（如 TimbreWM、WMCodec 等系统）基本假设只拿到单份个性化副本，考察的是压缩、加噪等单副本鲁棒性。但真实分发中同一录音可能流出多份不同 payload 的副本，简单逐样本平均即可稀释或混淆各 payload，使溯源失效。本文要回答：多样本共谋平均是否会破坏可溯源性，以及解码器对不同 payload 组合如何响应。

## 💡 核心创新

1. 提出逐样本平均共谋攻击，量化多副本溯源失效
2. 分析各系统解码器对 coalition payload 组成的响应差异
3. payload-aware 混合加权，将解码器导向指定非成员
4. 初步置信度筛选，拒绝共谋诱导的错误归属

## 🏗️ 模型架构

本文为攻击/评估研究，不提出新的水印网络。流程为：取同一原始录音的 N 份个性化水印副本（各含不同用户 payload），在波形域做逐样本平均得到共谋混合；将混合送入被攻击系统的解码器（TimbreWM、WMCodec 等五个神经音频水印系统），统计解码出的 payload 与任一成员/非成员的匹配情况，定义 tracing-failure rate。进一步在 payload-aware 设定下按 payload 组成调整混合权重，并尝试用解码置信度做筛选。

## 📚 数据集

- 五个神经音频水印系统（TimbreWM、WMCodec 等，被攻击对象）
- 原始音频样本（用于生成多份个性化水印副本，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| tracing-failure rate（两份平均） | 五个水印系统 | 单副本评估（可溯源） | **87.7-99.7%** | 溯源基本失效 |
| target success rate（payload-aware 加权） | TimbreWM | 随机/无加权 | **92.3%** | 导向指定非成员 |

两份副本平均即可在五个系统中造成 87.7-99.7% 的溯源失败率，且音频质量基本保持。解码器对 coalition payload 组成的响应因系统而异：TimbreWM 多数一致性高，WMCodec 明显偏低。payload-aware 加权在 TimbreWM 上达到 92.3% 的目标成功率。置信度筛选可拒绝大量共谋诱导的错误归属，同时保留多数有效单副本输出，但仅为初步结果。

## 🎯 结论与影响

最强结论是：简单平均两份个性化副本就足以让现有神经音频水印溯源失效，多副本可溯源性应作为独立评估维度。这会推动后续水印系统在训练与评估中加入共谋鲁棒性，对工业界音频溯源与版权追踪的部署提出新的安全前提。

## ⚠️ 局限与未解决问题

攻击仅限逐样本平均与简单加权，未覆盖裁剪、重编码等更强共谋；置信度筛选只是初步，缺少误拒率/漏检率的系统量化；五个系统的选择与音频素材规模未充分说明；未报告攻击的计算开销与防御后的性能代价。

## 🔗 开源资源

- **代码**：<https://github.com/Silwan5z/neural-audio-watermark-collusion-attack>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-04/">← 返回 2026-11-04 速递</a></div>
