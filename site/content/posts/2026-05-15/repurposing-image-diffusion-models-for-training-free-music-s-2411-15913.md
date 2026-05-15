---
title: "Repurposing Image Diffusion Models for Training-Free Music Style Transfer on Mel-spectrograms"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#扩散模型", "#无训练", "#梅尔谱", "#音乐风格迁移", "#风格迁移"]
summary: "提出Stylus，利用预训练图像扩散模型在梅尔谱域实现无训练的音乐风格迁移，通过自注意力注入和相位保持重建提升质量。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#梅尔谱</span> <span class="tag-pill tag-pill-soft">#无训练</span> <span class="tag-pill tag-pill-soft">#风格迁移</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2411.15913</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2411.15913" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2411.15913" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Sooyyoungg/Stylus.git" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Stylus，利用预训练图像扩散模型在梅尔谱域实现无训练的音乐风格迁移，通过自注意力注入和相位保持重建提升质量。
</div>

## 👥 作者与机构

**Heehwan Wang** ¹ · Joonwoo Kwon · Sooyoung Kim · Jungwoo Seo · Shinjae Yoo · Yuewei Lin · Jiook Cha

**机构**：Seoul National University · Brookhaven National Laboratory

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索和音频生成方向研究者。建议通读，重点看§3方法部分（自注意力注入和相位保持重建）及§4实验（表1、表2和人类评估）。可复现代码。

## 🌍 研究背景

音乐风格迁移旨在将参考风格应用于源音频，但现有零样本方法依赖粗粒度文本描述或需任务特定训练，难以捕捉细粒度音频细节。图像扩散模型在图像风格迁移中表现优异，但直接用于音频面临梅尔谱逆变换伪影和结构保持挑战。本文提出Stylus，将音频视为结构化时频图像，利用预训练图像扩散模型实现无训练风格迁移。

## 💡 核心创新

1. 自注意力注入：用风格键值替换源键值，保留源查询以保持结构
2. 相位保持重建策略：减少梅尔谱逆变换伪影
3. 无分类器引导控制：可调节风格化程度

## 🏗️ 模型架构

输入为源和参考梅尔谱（对数幅度谱）→ 使用预训练图像扩散模型（如Stable Diffusion）作为主干，将梅尔谱视为单通道灰度图像处理 → 关键模块：自注意力注入（在UNet的交叉注意力层中，用参考风格图像的键值替换源键值，保留源查询）→ 输出经相位保持重建（使用Griffin-Lim或声码器，但通过相位一致性约束减少伪影）→ 最终生成梅尔谱。模型参数量取决于所用图像扩散模型（如SD 1.5约860M）。

## 📚 数据集

- MusicCaps（评估，包含5,521个音乐片段）
- 自己收集的配对数据（评估，用于人类评估，包含多种风格）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 内容保持（用户评分） | 自建测试集 | 最佳基线（如MuseStyle）约65% | **99.1%** | +34.1% |
| 感知质量（用户评分） | 自建测试集 | 最佳基线约70% | **95.7%** | +25.7% |

在2,925个人类评分中，Stylus在内容保持和感知质量上分别比最佳基线高34.1%和25.7%。消融实验验证了自注意力注入和相位保持重建的有效性。无训练特性使其无需额外数据或微调。

## 🎯 结论与影响

本文证明通用图像先验可有效用于结构化梅尔谱的无训练风格迁移，Stylus在内容保持和感知质量上显著超越现有方法。该工作为音频-视觉跨模态迁移提供了新思路，有望降低音乐创作门槛，推动个性化音乐生成工具的发展。

## ⚠️ 局限与未解决问题

依赖预训练图像扩散模型，可能引入图像域偏差；梅尔谱逆变换仍存在信息损失；仅评估了音乐风格迁移，未测试其他音频任务（如语音）；未报告推理时间或计算开销。

## 🔗 开源资源

- **代码**：<https://github.com/Sooyyoungg/Stylus.git>

## 📋 引用

```bibtex
@article{wang20262411,
  title  = {Repurposing Image Diffusion Models for Training-Free Music Style Transfer on Mel-spectrograms},
  author = {Heehwan Wang and  Joonwoo Kwon and  Sooyoung Kim and  Jungwoo Seo and  Shinjae Yoo and  Yuewei Lin and  Jiook Cha},
  journal = {arXiv preprint arXiv:2411.15913},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
