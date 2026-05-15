---
title: "Repurposing Image Diffusion Models for Training-Free Music Style Transfer on Mel-spectrograms"
date: 2026-05-15T09:00:00+08:00
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
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
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

适合对音乐风格迁移、扩散模型跨模态应用感兴趣的读者。建议通读，重点看§3方法部分（自注意力操作与相位保持重建）及§4实验（表1、图3）。可复现代码已开源。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 免训练地将参考音乐的风格迁移到源音乐上，用于个性化音乐创作。 |
| **核心创新** | 将图像扩散模型直接用于梅尔频谱图风格迁移，无需训练 · 通过自注意力机制注入风格键值，保留源结构查询 · 相位保持重建策略减少频谱图反演伪影 |
| **模型架构** | 输入源和参考音频的梅尔频谱图 → 使用预训练Stable Diffusion作为主干，在去噪过程中替换自注意力层的键和值为参考风格的特征，保留查询为源结构 → 通过CFG引导控制风格化程度 → 输出梅尔频谱图经相位保持重建（使用原始相位）得到音频。参数量未给出。 |
| **数据集** | FMA (训练，用于提取风格) · MUSDB18 (评估，源音乐) |
| **关键结果** | 在2925个人类评分中，Stylus在内容保留上比SOTA基线高34.1%，感知质量高25.7%。无自动指标（如SI-SDR）报告。 |

## 🔗 开源资源

- **代码**：<https://github.com/Sooyyoungg/Stylus.git>

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联，但方法可迁移至语音增强/分离：将语音视为时频图像，利用图像扩散先验进行免训练增强或分离，值得关注。

## ⚠️ 局限与未解决问题

依赖预训练图像扩散模型，对非音乐音频（如语音）的适用性未验证；未报告推理延迟；缺乏与基于音频的扩散模型（如AudioLDM）的对比；相位保持策略假设源相位可用，在无源相位场景下可能失效。

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

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
