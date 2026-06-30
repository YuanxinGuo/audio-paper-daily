---
title: "Audio-Visual Continual Test-Time Adaptation without Forgetting"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视听连续测试时适应"]
summary: "提出AVReCAP方法，通过选择性参数检索机制动态调整融合层参数，在视听连续测试时适应中缓解灾难性遗忘，无需源数据。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视听连续测试时适应</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#测试时适应</span> <span class="tag-pill tag-pill-soft">#视听学习</span> <span class="tag-pill tag-pill-soft">#灾难性遗忘</span> <span class="tag-pill tag-pill-soft">#跨模态融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.18528</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-30</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.18528" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.18528" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AVReCAP方法，通过选择性参数检索机制动态调整融合层参数，在视听连续测试时适应中缓解灾难性遗忘，无需源数据。
</div>

## 👥 作者与机构

**Sarthak Kumar Maharana** ¹ · Akshay Mehra · Bhavya Ramakrishna · Yunhui Guo · Guan-Ming Su

**机构**：马里兰大学 · 三星研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究测试时适应、视听学习或灾难性遗忘的读者。建议重点阅读§3方法部分和§4实验，特别是表1和表2的对比结果。可先看§3.2选择性参数检索机制。

## 🌍 研究背景

视听连续测试时适应旨在使源模型在测试时持续适应未标注的非平稳域，其中单模态或双模态可能发生分布偏移，导致在线跨模态学习困难。现有SOTA方法因持续参数更新而遭受灾难性遗忘，性能甚至低于源模型。本文旨在解决这一问题，提出无需源数据的测试时适应方法。

## 💡 核心创新

1. 发现仅适应融合层可提升当前域及后续域性能
2. 提出选择性参数检索机制动态获取最优融合层参数
3. 利用小批量测试数据从缓冲区检索参数并集成
4. 无需源数据即可缓解灾难性遗忘

## 🏗️ 模型架构

输入为视听特征（来自预训练编码器），主干网络包含模态特定编码器和融合层。AVReCAP方法维护一个融合层参数缓冲区，在测试时，使用小批量测试数据通过选择性检索机制从缓冲区选出最优参数，集成到模型中适应当前分布，然后保存回缓冲区。

## 📚 数据集

- AV-MNIST（训练/评估，含单模态和双模态损坏）
- VGG-Sound（训练/评估，含单模态和双模态损坏）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | AV-MNIST（双模态损坏） | TENT 45.2% | **AVReCAP 72.8%** | +27.6% |
| Accuracy | VGG-Sound（双模态损坏） | TENT 38.5% | **AVReCAP 55.2%** | +16.7% |

在AV-MNIST和VGG-Sound数据集上，AVReCAP在单模态和双模态损坏下均显著优于现有方法，且有效缓解灾难性遗忘。消融实验验证了选择性检索机制和融合层适应策略的有效性。

## 🎯 结论与影响

本文证明仅适应融合层可提升跨域性能，并基于此提出AVReCAP，通过选择性参数检索机制在测试时动态调整融合层，显著优于现有方法。该方法为视听测试时适应提供了新思路，有望推动在线适应在视听应用中的实际部署。

## ⚠️ 局限与未解决问题

方法依赖预训练编码器，未探索端到端联合训练；缓冲区大小和检索策略可能影响性能；实验仅在两个数据集上进行，泛化性需进一步验证；未报告推理延迟等效率指标。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-30/">← 返回 2026-06-30 速递</a></div>
