---
title: "From Talking to Singing: A New Challenge for Audio-Visual Deepfake Detection"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频伪造检测"]
summary: "提出文本引导的音视频伪造检测框架T-AVFD，解决从说话到歌唱场景的域偏移问题，并构建歌唱头部深度伪造数据集SHDF。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音伪造检测</span> <span class="tag-pill tag-pill-soft">#跨模态一致性</span> <span class="tag-pill tag-pill-soft">#歌唱场景</span> <span class="tag-pill tag-pill-soft">#文本引导</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.27944</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.27944" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.27944" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出文本引导的音视频伪造检测框架T-AVFD，解决从说话到歌唱场景的域偏移问题，并构建歌唱头部深度伪造数据集SHDF。
</div>

## 👥 作者与机构

**Ke Liu** ¹ · Jiwei Wei · Wenyu Zhang · Shuchang Zhou · Ruikun Chai · Yutao Dai · Chaoning Zhang · Yang Yang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频伪造检测、多模态学习研究者。重点读§3方法部分和§4实验，特别是跨场景泛化结果。可先看表1和表2对比。

## 🌍 研究背景

现有音视频伪造检测方法多依赖跨模态不一致性，但在歌唱场景中，节奏性发声削弱了音视频耦合，导致性能显著下降。目前缺乏歌唱场景的伪造检测基准。本文旨在构建歌唱场景数据集并提出跨场景泛化的检测框架。

## 💡 核心创新

1. 构建歌唱头部深度伪造数据集SHDF
2. 提出文本引导的音视频伪造检测框架T-AVFD
3. 设计面部真实性模式学习器，对齐多粒度文本描述
4. 提出多模态差分权重学习模块，自适应整合一致性特征

## 🏗️ 模型架构

T-AVFD框架包含两个核心模块：面部真实性模式学习器和多模态差分权重学习模块。输入为视频帧和音频，面部模式学习器使用预训练视觉编码器提取面部特征，并通过跨模态注意力与文本描述对齐，学习通用真实性模式。权重学习模块使用音频和视频编码器提取特征，计算差分权重，自适应融合音频-视觉一致性和真实性模式。输出为伪造概率。

## 📚 数据集

- SHDF（歌唱头部深度伪造数据集，训练/评估）
- FakeAVCeleb（说话场景，训练/评估）
- DFDC（说话场景，训练/评估）
- DeepfakeTIMIT（说话场景，训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| AUC | SHDF | AV-Lip-Sync (0.812) | **0.892** | +0.080 |
| AUC | FakeAVCeleb | AV-Lip-Sync (0.876) | **0.913** | +0.037 |
| AUC | DFDC | AV-Lip-Sync (0.832) | **0.861** | +0.029 |
| AUC | DeepfakeTIMIT | AV-Lip-Sync (0.901) | **0.924** | +0.023 |

T-AVFD在多个数据集上一致优于基线，尤其在歌唱场景SHDF上AUC提升8.0%。跨数据集泛化实验显示，在说话场景训练后直接测试歌唱场景，T-AVFD仍保持较高性能，表明其跨场景鲁棒性。消融实验验证了文本引导和差分权重模块的有效性。

## 🎯 结论与影响

本文提出的T-AVFD框架通过文本引导和多模态差分权重学习，有效解决了从说话到歌唱场景的域偏移问题，在多个伪造检测数据集上取得一致提升。该工作为音视频伪造检测提供了新思路，特别是对非典型发声场景的泛化能力，对实际部署具有重要价值。

## ⚠️ 局限与未解决问题

未报告模型参数量和推理速度；SHDF数据集规模较小且仅包含一种歌唱风格；文本描述依赖预训练模型，可能引入偏差；未在真实世界深度伪造视频上验证。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
