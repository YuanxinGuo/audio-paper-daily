---
title: "MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-语言预训练"]
summary: "提出概率性音频-语言预训练框架MixProLAP，通过混合音频-文本对建模多对多对齐的不确定性，在检索任务上优于确定性基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-语言预训练</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态对齐</span> <span class="tag-pill tag-pill-soft">#不确定性建模</span> <span class="tag-pill tag-pill-soft">#音频-文本检索</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.20418</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.20418" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.20418" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出概率性音频-语言预训练框架MixProLAP，通过混合音频-文本对建模多对多对齐的不确定性，在检索任务上优于确定性基线。
</div>

## 👥 作者与机构

**Yu Nakagome** ¹ · Jaesong Lee · Soo-Whan Chung

**机构**：NAVER Corporation

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态学习、音频-文本检索方向的研究者。建议重点阅读§3的混合策略和多层级包含损失设计，以及§4的检索实验结果。可先看表1对比结果。

## 🌍 研究背景

音频-文本对齐面临固有歧义：真实声学环境常包含多个重叠声音事件，同一场景可用不同文本描述。现有对比学习方法学习确定性点嵌入，无法建模这种多对多对应关系。本文旨在通过概率建模和混合策略解决该问题。

## 💡 核心创新

1. 提出概率性音频-语言预训练框架，将模态表示为分布而非点嵌入
2. 设计混合音频-文本对策略，模拟真实重叠声音并捕获语义包含关系
3. 引入多层级包含损失，强制表示符合语义包含关系

## 🏗️ 模型架构

输入音频和文本对。音频编码器提取特征，文本编码器提取文本特征。每个模态通过投影头映射为高斯分布的均值和方差。训练时，混合音频-文本对（如将两个音频混合，对应文本拼接）作为输入，通过KL散度对齐分布，并加入多层级包含损失。推理时使用分布均值作为嵌入进行检索。

## 📚 数据集

- AudioCaps（训练/评估，音频-文本对）
- Clotho（训练/评估，音频-文本对）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| R@1 | AudioCaps (audio-to-text) | CLAP (deterministic) 42.1 | **45.3** | +3.2 |
| R@1 | AudioCaps (text-to-audio) | CLAP (deterministic) 38.7 | **41.5** | +2.8 |
| R@1 | Clotho (audio-to-text) | CLAP (deterministic) 18.9 | **20.6** | +1.7 |
| R@1 | Clotho (text-to-audio) | CLAP (deterministic) 16.2 | **18.1** | +1.9 |

在AudioCaps和Clotho的音频-文本检索任务上，MixProLAP在R@1上比确定性CLAP基线提升1.7~3.2个百分点。消融实验验证了混合策略和包含损失的有效性。模型参数量与CLAP相当，推理时仅使用均值，无额外计算开销。

## 🎯 结论与影响

MixProLAP通过概率建模和混合策略有效处理音频-文本对齐中的多对多歧义，在检索任务上取得一致提升。该工作为多模态预训练中的不确定性建模提供了新思路，有望推广到其他含歧义对齐任务。工业上可提升音频搜索和推荐系统的鲁棒性。

## ⚠️ 局限与未解决问题

仅在两个英文数据集上评估，未验证跨语言或噪声场景下的泛化性。混合策略依赖预定义的混合比例，未探索自适应混合。未与近期概率性对比学习方法（如Probabilistic CLIP）对比。推理时未利用分布方差信息。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
