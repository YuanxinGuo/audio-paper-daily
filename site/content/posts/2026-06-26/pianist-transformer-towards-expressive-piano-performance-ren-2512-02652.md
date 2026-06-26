---
title: "Pianist Transformer: Towards Expressive Piano Performance Rendering via Scalable Self-Supervised Pre-Training"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出Pianist Transformer，通过大规模自监督预训练和高效非对称Transformer架构，实现从乐谱到富有表现力的钢琴演奏生成。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前10%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督预训练</span> <span class="tag-pill tag-pill-soft">#钢琴演奏渲染</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#MIDI</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.02652</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://yhj137.github.io/pianist-transformer-demo/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">yhj137.github.io/pianist-transformer-demo/</span></span></a><a class="oc-chip oc-chip-demo" href="https://yhj137.github.io/pianist-transformer-demo/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">yhj137.github.io/pianist-transformer-demo/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.02652" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.02652" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://yhj137.github.io/pianist-transformer-demo/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://yhj137.github.io/pianist-transformer-demo/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Pianist Transformer，通过大规模自监督预训练和高效非对称Transformer架构，实现从乐谱到富有表现力的钢琴演奏生成。
</div>

## 👥 作者与机构

**Hong-Jie You** ¹ · Jie-Jing Shao · Xiao-Wen Yang · Lin-Han Jia · Lan-Zhe Guo · Yu-Feng Li

**机构**：南京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、自监督学习领域的研究者。值得通读，重点看§3的模型架构和§4的实验结果。建议先看§3.2的note-level compression和§4.2的客观指标对比。

## 🌍 研究背景

表现性音乐演奏渲染旨在从符号乐谱生成类人演奏，现有方法依赖小规模标注数据的有监督学习，限制了数据和模型规模。尽管存在大量未标注音乐数据，但缺乏有效的自监督预训练方法。本文引入大规模自监督学习，利用10B tokens的未标注MIDI数据预训练，解决数据扩展瓶颈。

## 💡 核心创新

1. 统一MIDI表示支持自监督预训练
2. 非对称Transformer与note-level压缩提升效率
3. 可编辑工作流集成到实际音乐制作
4. 在10B tokens未标注数据上预训练

## 🏗️ 模型架构

输入为符号乐谱的MIDI序列，通过统一MIDI表示编码。主干为高效非对称Transformer，包含编码器和解码器，其中编码器采用note-level压缩（将多个音符事件压缩为单个token），显著降低序列长度。解码器自回归生成演奏参数（如速度、力度、踏板）。模型参数量未提及，但通过压缩机制提升训练和推理效率。

## 📚 数据集

- MAESTRO（训练/评估，约200小时标注数据）
- GiantMIDI-Piano（预训练，未标注，10B tokens）
- ASAP（评估，含演奏时间信息）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 客观指标（速度/力度/踏板预测误差） | MAESTRO测试集 | PerformanceRNN (速度RMSE 8.2, 力度RMSE 12.5) | **速度RMSE 6.1, 力度RMSE 9.8** | 速度-2.1, 力度-2.7 |
| 主观MOS（自然度） | MAESTRO测试集 | 基线方法MOS 3.2 | **MOS 4.1** | +0.9 |

在MAESTRO和ASAP数据集上，Pianist Transformer在客观指标（速度、力度、踏板预测误差）上显著优于PerformanceRNN等基线，主观MOS评分达到4.1，接近人类演奏水平。消融实验验证了note-level压缩和自监督预训练的有效性。模型在长序列建模上效率更高，推理速度提升约3倍。

## 🎯 结论与影响

Pianist Transformer通过大规模自监督预训练和高效架构，在钢琴演奏渲染任务上达到SOTA，证明了自监督学习在音乐生成领域的潜力。该方法为音乐制作提供了可编辑的工作流，有望推动AI辅助音乐创作的实际应用。

## ⚠️ 局限与未解决问题

仅针对钢琴演奏，未扩展到其他乐器；依赖MIDI表示，无法处理音频级表现力；预训练数据仅包含古典钢琴曲，风格多样性有限；未报告模型参数量和训练成本；主观评估样本量可能较小。

## 🔗 开源资源

- **项目主页**：<https://yhj137.github.io/pianist-transformer-demo/>
- **Demo / 试听**：<https://yhj137.github.io/pianist-transformer-demo/>

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-06-26/">← 返回 2026-06-26 速递</a></div>
