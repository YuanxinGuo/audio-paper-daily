---
title: "Repurposing Image Diffusion Models for Training-Free Music Style Transfer on Mel-spectrograms"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#免训练", "#扩散模型", "#梅尔频谱图", "#自注意力", "#音乐风格迁移"]
summary: "提出Stylus，利用预训练图像扩散模型在梅尔频谱图上实现免训练的音乐风格迁移，通过注入风格键值并保留源结构查询，结合相位保持重建策略提升保真度。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#梅尔频谱图</span> <span class="tag-pill tag-pill-soft">#免训练</span> <span class="tag-pill tag-pill-soft">#自注意力</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2411.15913</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2411.15913" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2411.15913" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Sooyyoungg/Stylus.git" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Stylus，利用预训练图像扩散模型在梅尔频谱图上实现免训练的音乐风格迁移，通过注入风格键值并保留源结构查询，结合相位保持重建策略提升保真度。
</div>

## 👥 作者与机构

**Heehwan Wang** ¹ · Joonwoo Kwon · Sooyoung Kim · Jungwoo Seo · Shinjae Yoo · Yuewei Lin · Jiook Cha

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、风格迁移及扩散模型跨模态应用的研究者。建议重点阅读§3方法部分（自注意力操作与相位保持重建）及§4实验（表1、表2及用户研究）。可先看§3.2与图2理解核心机制。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 免训练音乐风格迁移，将源音乐内容与参考音乐风格融合生成新音频。 |
| **核心创新** | 利用预训练图像扩散模型处理梅尔频谱图实现免训练风格迁移 · 通过自注意力注入风格键值并保留源查询以保持内容结构 · 相位保持重建策略减少频谱图反演伪影 |
| **模型架构** | 输入源与参考梅尔频谱图 → 预训练图像扩散模型（如Stable Diffusion）→ 在去噪过程中替换自注意力层的键和值为参考风格，保留查询为源结构 → 输出风格化梅尔频谱图 → 相位保持重建（使用源相位）得到波形。无额外训练，参数量取决于预训练模型。 |
| **数据集** | MUSDB18（训练/评估，但本文免训练） · Medley-solos-DB（评估） · 个人收集数据集（用户研究） |
| **关键结果** | 在MUSDB18上，Stylus在内容保持（CLAP score）上比最优基线高34.1%，感知质量（LPIPS）高25.7%。用户研究（2925次评分）显示Stylus在风格相似性和整体质量上均优于现有方法。 |

## 🔗 开源资源

- **代码**：<https://github.com/Sooyyoungg/Stylus.git>

## 🎯 与本站重点领域的关联

与本站重点领域中的乐器分离（music source separation）有一定关联，但主任务为风格迁移。可迁移思路：将梅尔频谱图视为图像，利用图像扩散模型处理音频，可能适用于语音增强或分离中的频谱图处理。与语音增强、目标说话人提取、双耳音频无直接关联。

## ⚠️ 局限与未解决问题

依赖预训练图像扩散模型，可能对非音乐音频（如语音）泛化能力未知；相位保持策略假设源相位可用，在无相位信息场景受限；未报告推理延迟或计算开销；仅在音乐数据上评估，缺乏对语音等领域的验证。

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

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
