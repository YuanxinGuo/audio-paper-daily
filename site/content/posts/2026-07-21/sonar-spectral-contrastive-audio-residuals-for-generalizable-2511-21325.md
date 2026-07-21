---
title: "SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出SONAR框架，通过频谱对比学习显式分离音频的高低频表示，利用高频残差提升深度伪造检测的泛化性，在ASVspoof 2021和in-the-wild上达到SOTA，收敛速度快4倍。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强方法</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#高频伪影</span> <span class="tag-pill tag-pill-soft">#泛化性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.21325</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.21325" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.21325" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SONAR框架，通过频谱对比学习显式分离音频的高低频表示，利用高频残差提升深度伪造检测的泛化性，在ASVspoof 2021和in-the-wild上达到SOTA，收敛速度快4倍。
</div>

## 👥 作者与机构

**Ido Nitzan Hidekel** ¹ · Gal lifshitz · Khen Cohen · Dan Raviv

**机构**：特拉维夫大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频伪造检测、对比学习、频谱分析方向的研究者。建议通读，重点看§3方法（频谱对比残差、频率交叉注意力）和§4实验（表1、图3收敛曲线）。可复现其高频残差提取模块。

## 🌍 研究背景

深度伪造音频检测面临泛化性差的问题，核心原因是频谱偏置：神经网络倾向于学习低频结构而忽略高频细节。现有检测器未能充分利用高频伪影，导致对未见过的伪造类型失效。本文旨在设计一个频率引导的框架，显式提取高频残差并利用对比学习增强判别边界。

## 💡 核心创新

1. 提出频谱对比残差（SONAR）框架，显式分离高低频表示
2. 设计可学习SRM值约束高通滤波器提取高频残差
3. 引入频率交叉注意力融合长短程频率依赖
4. 提出频率感知Jensen-Shannon对比损失加速优化
5. 实现架构无关的表示级高频伪影利用方案

## 🏗️ 模型架构

输入音频经XLSR编码器提取低频主导表示；同一编码器前接可学习SRM高通滤波器（值约束）提取高频残差；频率交叉注意力模块融合低频和高频表示，捕获长短程频率依赖；最后通过频率感知Jensen-Shannon对比损失拉近真实音频的高低频对，推开伪造音频的嵌入。整体为双分支对比学习架构。

## 📚 数据集

- ASVspoof 2021（评估，包含多种伪造类型）
- in-the-wild（评估，真实场景伪造音频）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER | ASVspoof 2021 | AASIST 2.50% | **1.82%** | -0.68% |
| EER | in-the-wild | AASIST 4.10% | **2.95%** | -1.15% |

SONAR在ASVspoof 2021和in-the-wild上均取得最低EER，分别比AASIST降低0.68%和1.15%。收敛速度比强基线快4倍。消融实验验证了高频残差和对比损失的有效性。跨数据集泛化测试显示SONAR对未见过的伪造类型鲁棒。

## 🎯 结论与影响

SONAR通过显式分离并利用高频残差，显著提升了深度伪造音频检测的泛化性，收敛速度更快。该工作揭示了高频伪影作为判别信号的重要性，为未来将频率引导对比学习集成到其他模态（如图像、视频）提供了思路。对工业落地而言，其架构无关性便于嵌入现有系统。

## ⚠️ 局限与未解决问题

未在更多样化的数据集（如多语言、低信噪比）上评估；未报告推理延迟和模型参数量；高频残差提取的可学习SRM滤波器可能引入额外训练复杂度；对比损失对batch size敏感，未讨论超参数影响。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
