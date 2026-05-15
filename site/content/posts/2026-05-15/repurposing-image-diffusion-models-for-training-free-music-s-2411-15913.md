---
title: "Repurposing Image Diffusion Models for Training-Free Music Style Transfer on Mel-spectrograms"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐风格迁移"]
summary: "提出Stylus，利用预训练图像扩散模型在梅尔频谱图上实现无需训练的音乐风格迁移，通过自注意力注入和相位保持重建提升质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐风格迁移</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#梅尔频谱图</span> <span class="tag-pill tag-pill-soft">#无训练</span> <span class="tag-pill tag-pill-soft">#自注意力</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2411.15913</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Sooyyoungg/Stylus.git" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Sooyyoungg/Stylus.git</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2411.15913" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2411.15913" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Sooyyoungg/Stylus.git" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Stylus，利用预训练图像扩散模型在梅尔频谱图上实现无需训练的音乐风格迁移，通过自注意力注入和相位保持重建提升质量。
</div>

## 👥 作者与机构

**Heehwan Wang** ¹ · Joonwoo Kwon · Sooyoung Kim · Jungwoo Seo · Shinjae Yoo · Yuewei Lin · Jiook Cha

**机构**：纽约大学 · 布鲁克海文国家实验室

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和生成式音频研究者。建议通读，重点看§3.2自注意力注入机制和§3.3相位保持重建策略，以及表2的消融实验。可复现代码。

## 🌍 研究背景

音乐风格迁移旨在将源音频的结构与参考风格融合，但现有零样本方法依赖粗糙文本描述或需昂贵任务特定训练，难以捕捉细粒度音频细节。图像扩散模型在视觉风格迁移上表现优异，但直接应用于音频面临频谱结构差异和逆变换伪影问题。本文探索将音频表示为梅尔频谱图，利用预训练图像扩散模型进行无训练风格迁移，解决结构保持和保真度挑战。

## 💡 核心创新

1. 自注意力键值注入：用参考风格键值替换源键值，保留查询以保持结构
2. 相位保持重建策略：结合幅度和相位信息减少频谱逆变换伪影
3. 无分类器引导控制：可调节风格化强度，平衡内容与风格
4. 首次验证图像扩散模型可直接用于结构化梅尔频谱图的无训练变换

## 🏗️ 模型架构

输入为源和参考音频的梅尔频谱图（对数幅度谱）。主干网络使用预训练图像扩散模型（如Stable Diffusion）。关键模块：自注意力层中，源频谱的查询（Q）保持不变，而键（K）和值（V）替换为参考频谱的键和值，实现风格注入。随后，通过相位保持重建模块，将扩散输出与原始相位结合，经短时傅里叶逆变换生成音频。模型参数量取决于所用图像扩散模型（如Stable Diffusion约860M参数），但无需训练。

## 📚 数据集

- MusicCaps（评估，包含5,521个音乐片段）
- 自己收集的钢琴和管弦乐数据集（评估，用于风格迁移）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 内容保留（用户评分） | MusicCaps | AudioLDM 2（3.2/5） | **4.3/5** | +34.1% |
| 感知质量（用户评分） | MusicCaps | AudioLDM 2（3.1/5） | **3.9/5** | +25.7% |

在MusicCaps数据集上，Stylus在内容保留和感知质量上分别比AudioLDM 2提升34.1%和25.7%。消融实验验证了自注意力注入和相位保持重建的有效性。用户研究包含2,925个评分，统计显著。此外，Stylus在跨乐器风格迁移（如钢琴→管弦乐）上表现稳健，且推理速度快于需要微调的方法。

## 🎯 结论与影响

Stylus证明预训练图像扩散模型可有效用于梅尔频谱图的音乐风格迁移，无需任务特定训练。其自注意力注入和相位保持策略显著优于现有零样本方法。该工作为利用通用视觉先验进行音频生成开辟了新路径，对个性化音乐创作和音频编辑有潜在工业价值。

## ⚠️ 局限与未解决问题

依赖梅尔频谱图表示，可能丢失相位信息；风格迁移效果受限于预训练图像模型的能力；未在真实世界录音上评估；缺乏与基于文本的音频生成模型的直接对比（如MusicGen）；未报告推理延迟和计算成本。

## 🔗 开源资源

- **代码**：<https://github.com/Sooyyoungg/Stylus.git>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
