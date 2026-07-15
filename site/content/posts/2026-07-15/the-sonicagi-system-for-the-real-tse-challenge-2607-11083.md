---
title: "The SonicAGI System for the REAL-TSE Challenge"
date: 2026-07-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出数据驱动方法结合模拟与真实重叠语音，设计低延迟在线系统SwiftNet-Lookahead和离线系统USEF-TFGridNet，在REAL-TSE挑战赛中取得第二和第五名。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#低延迟</span> <span class="tag-pill tag-pill-soft">#跨注意力</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.11083</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.11083" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.11083" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出数据驱动方法结合模拟与真实重叠语音，设计低延迟在线系统SwiftNet-Lookahead和离线系统USEF-TFGridNet，在REAL-TSE挑战赛中取得第二和第五名。
</div>

## 👥 作者与机构

**Kai Li** ¹ · Wendi Sang · Jintao Cheng · Xiaolin Hu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合目标说话人提取和低延迟系统研究者。建议重点阅读§3.1数据模拟策略和§3.2 SwiftNet-Lookahead的lookahead模块设计，以及§3.3 USEF-TFGridNet的幅度域融合。可先看表1和表2的结果。

## 🌍 研究背景

真实场景目标说话人提取面临声学条件不匹配、混响、噪声和重叠语音等挑战。现有方法多基于理想模拟数据，在真实会议场景中性能下降。REAL-TSE挑战赛聚焦于真实会议录音，要求系统在低延迟（在线）或高精度（离线）条件下提取目标说话人。本文旨在通过数据驱动和特定赛道建模提升真实场景TSE性能。

## 💡 核心创新

1. 数据驱动：混合模拟与真实重叠语音训练
2. SwiftNet-Lookahead：单模块有界lookahead实现低延迟因果分离
3. USEF-TFGridNet：帧级注册跨注意力与幅度域融合
4. 冻结离线增强器提供去噪镜像作为辅助监督

## 🏗️ 模型架构

在线系统SwiftNet-Lookahead：输入混合语音→严格因果迭代分离器前插入单有界lookahead模块（96ms延迟）→输出目标语音。离线系统USEF-TFGridNet：帧级注册跨注意力USEF模块结合TFGridNet主干，后接幅度域融合阶段，权衡感知质量与说话人保真度。使用冻结离线增强器生成去噪镜像作为辅助监督。

## 📚 数据集

- REAL-TSE Challenge数据集（训练/评估，真实会议录音与模拟混合）
- Clean speech数据集（模拟混合，来源未明确）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 排名 | REAL-TSE Track 1 (在线) | 挑战基线 | **第2名** | 超过基线 |
| 排名 | REAL-TSE Track 2 (离线) | 挑战基线 | **第5名** | 超过基线 |

在REAL-TSE挑战赛中，SwiftNet-Lookahead在在线赛道排名第二，USEF-TFGridNet在离线赛道排名第五，均超过挑战基线。结果验证了真实数据导向训练和赛道特定建模的有效性。摘要未提供具体指标数值。

## 🎯 结论与影响

本文通过数据驱动和赛道特定建模，在真实会议TSE任务上取得了优于基线的性能。SwiftNet-Lookahead的低延迟设计和USEF-TFGridNet的幅度域融合为实际应用提供了有效方案。后续研究可进一步优化数据模拟策略和模型效率。

## ⚠️ 局限与未解决问题

摘要未报告具体指标（如SI-SDR、PESQ），仅给出排名，难以量化改进幅度。未提供消融实验验证各模块贡献。未讨论模型参数量和推理速度。离线系统排名第五，可能仍有较大提升空间。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-15/">← 返回 2026-07-15 速递</a></div>
