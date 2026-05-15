---
title: "Seconds-Aligned PCA-DAC Latent Diffusion for Symbolic-to-Audio Drum Rendering"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#PCA", "#潜在扩散模型", "#符号到音频", "#音乐生成", "#鼓声合成"]
summary: "提出Sec2Drum-DAC，一种基于PCA-DAC潜在扩散的符号到音频鼓声渲染模型，通过条件潜在扩散和PCA压缩实现高效高质量合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号到音频</span> <span class="tag-pill tag-pill-soft">#潜在扩散模型</span> <span class="tag-pill tag-pill-soft">#PCA</span> <span class="tag-pill tag-pill-soft">#鼓声合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13404</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13404" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13404" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Sec2Drum-DAC，一种基于PCA-DAC潜在扩散的符号到音频鼓声渲染模型，通过条件潜在扩散和PCA压缩实现高效高质量合成。
</div>

## 👥 作者与机构

**Konstantinos Soiledis** ¹ · Maximos Kaliakatsos Papakostas · Dimos Makris · Konstantinos Tsamis

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、音频合成方向的研究者。建议重点阅读§3模型架构与§4实验部分，特别是PCA扩散与确定性回归的对比分析。可先看表1与图2了解性能差异。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从符号鼓谱（如MIDI）生成逼真的鼓声波形。 |
| **核心创新** | 使用PCA压缩DAC码本嵌入作为扩散目标，降低维度 · 条件扩散模型在物理时间对齐的编解码器帧上采样 · 辅助RVQ交叉熵损失改善短步扩散性能 |
| **模型架构** | 输入符号事件特征（时间、力度等）→ 条件潜在扩散模型，以冻结DAC编码器的summed-codebook嵌入经PCA降维后的72维主成分作为扩散目标，预测噪声→ 经确定性PCA重构回1024维DAC潜在空间→ DAC解码器输出波形。参数量未明确给出。 |
| **数据集** | 私有鼓声数据集（训练与评估，含1733个四拍窗口） |
| **关键结果** | PCA扩散在配对谱指标和瞬态指标上优于确定性PCA回归和符号渲染基线，但直接回归在波形L1上更强。辅助RVQ交叉熵在6-25步扩散时改善mel误差、onset-flux余弦和波形L1。具体数值未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但乐器分离领域可借鉴其DAC编解码器与潜在扩散思路，用于分离后音色重建或音源合成。

## ⚠️ 局限与未解决问题

未报告模型参数量与推理速度；仅在私有数据集上评估，缺乏公开基准对比；未消融PCA维度选择的影响；未与最新扩散模型（如AudioLDM）比较。

## 📋 引用

```bibtex
@article{soiledis20262605,
  title  = {Seconds-Aligned PCA-DAC Latent Diffusion for Symbolic-to-Audio Drum Rendering},
  author = {Konstantinos Soiledis and  Maximos Kaliakatsos Papakostas and  Dimos Makris and  Konstantinos Tsamis},
  journal = {arXiv preprint arXiv:2605.13404},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
