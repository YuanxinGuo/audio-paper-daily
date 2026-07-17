---
title: "ITGPT: A Transformer Based Architecture for the Generation of Dance Dance Revolution and In the Groove Charts"
date: 2026-07-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐游戏谱面生成"]
summary: "提出基于Transformer的ITGPT模型，用于自动生成Dance Dance Revolution和In the Groove游戏的谱面，相比前人工作提升了生成准确率并降低了计算成本。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐游戏谱面生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#谱面生成</span> <span class="tag-pill tag-pill-soft">#节奏游戏</span> <span class="tag-pill tag-pill-soft">#DDR</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.14148</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.14148" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.14148" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于Transformer的ITGPT模型，用于自动生成Dance Dance Revolution和In the Groove游戏的谱面，相比前人工作提升了生成准确率并降低了计算成本。
</div>

## 👥 作者与机构

**Miguel O'Malley** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对音乐游戏谱面自动生成感兴趣的读者。可重点阅读第3节模型架构和第4节实验对比。若关注生成质量，建议查看附录中的谱面示例。

## 🌍 研究背景

Dance Dance Revolution (DDR) 和 In the Groove (ITG) 是节奏游戏，玩家需根据歌曲谱面踩踏舞垫上的箭头。手动制作谱面耗时且困难，因此自动生成谱面具有实际需求。此前已有基于规则或简单机器学习的方法，但生成质量有限。本文旨在利用Transformer架构提升谱面生成的准确性和效率。

## 💡 核心创新

1. 提出ITGPT，首个基于Transformer的DDR/ITG谱面生成模型
2. 采用自回归生成方式，逐帧预测谱面步骤
3. 引入位置编码和注意力机制捕捉歌曲节奏与谱面的时序关系
4. 相比前人方法显著降低计算成本

## 🏗️ 模型架构

ITGPT基于Transformer解码器架构。输入为歌曲的音频特征（如梅尔频谱）或节拍信息，通过嵌入层转换为向量序列。模型使用多层Transformer解码器，每层包含自注意力机制和前馈网络，以自回归方式逐帧生成谱面步骤（上、下、左、右箭头及组合）。输出为每一步的概率分布，通过采样得到最终谱面。模型参数量未在摘要中提及。

## 📚 数据集

- DDR/ITG公开谱面数据集（训练与评估，具体规模未提及）

## 📊 实验结果

摘要未提供具体数值结果，仅声称相比前人工作提升了生成准确率并降低了计算成本。建议读者查阅论文全文获取详细实验数据。

## 🎯 结论与影响

本文提出的ITGPT模型在DDR/ITG谱面自动生成任务上取得了优于前人的效果，验证了Transformer架构在该领域的有效性。该工作为节奏游戏谱面生成提供了新思路，有望降低人工制作成本，推动游戏内容自动化生成的发展。

## ⚠️ 局限与未解决问题

摘要未提及模型在多样化歌曲风格上的泛化能力、生成谱面的可玩性评估、以及与其他生成方法（如GAN、RNN）的对比。此外，缺乏对生成谱面质量的主观评测（如玩家体验）。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-07-17/">← 返回 2026-07-17 速递</a></div>
