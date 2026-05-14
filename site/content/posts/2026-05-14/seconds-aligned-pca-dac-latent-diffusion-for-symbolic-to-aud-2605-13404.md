---
title: "Seconds-Aligned PCA-DAC Latent Diffusion for Symbolic-to-Audio Drum Rendering"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#PCA压缩", "#潜在扩散模型", "#符号到音频", "#音乐生成", "#鼓声合成"]
summary: "提出Sec2Drum-DAC，一种基于PCA压缩DAC码本的条件潜在扩散模型，用于符号到音频的鼓声渲染，在1,733个测试窗口上优于确定性回归和符号渲染基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#符号到音频</span> <span class="tag-pill tag-pill-soft">#潜在扩散模型</span> <span class="tag-pill tag-pill-soft">#PCA压缩</span> <span class="tag-pill tag-pill-soft">#鼓声合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13404</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13404" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13404" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Sec2Drum-DAC，一种基于PCA压缩DAC码本的条件潜在扩散模型，用于符号到音频的鼓声渲染，在1,733个测试窗口上优于确定性回归和符号渲染基线。
</div>

## 👥 作者与机构

**Konstantinos Soiledis** ¹ · Maximos Kaliakatsos Papakostas · Dimos Makris · Konstantinos Tsamis

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成、音频合成方向的研究者。建议重点阅读§3模型架构和§4实验部分，尤其是表1中的指标对比。可先看§3.2的PCA扩散过程与§4.2的消融实验。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从MIDI鼓谱生成逼真的鼓声波形。 |
| **核心创新** | 使用PCA压缩DAC的求和码本嵌入作为扩散目标，降低维度。 · 在物理时间对齐的编解码器帧位置采样事件特征作为条件。 · 引入辅助RVQ交叉熵损失改善短步扩散性能。 |
| **模型架构** | 输入为符号事件特征（时间、力度等），在编解码器帧位置采样。主干为条件潜在扩散模型，预测72维PCA主成分坐标（从1024维DAC求和码本嵌入经SVD得到）。解码时通过PCA逆变换重建1024维潜在表示，再经DAC解码器生成波形。参数量未明确给出。 |
| **数据集** | 私有鼓声数据集（训练与评估，1,733个四拍窗口） |
| **关键结果** | 在1,733个测试窗口上，PCA扩散相比确定性PCA回归和符号渲染基线在谱指标（如mel误差）和瞬态指标（如起始通量余弦）上均有提升，但直接回归在波形L1上更强。辅助RVQ交叉熵在6-25步扩散时改善mel误差、起始通量余弦和波形L1。具体数值未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但乐器分离领域可借鉴其符号到音频的生成思路，用于分离后音色重建；语音增强领域可参考其条件扩散模型与PCA压缩的降维策略。

## ⚠️ 局限与未解决问题

摘要未报告模型参数量、推理速度或与主流生成模型（如GAN、VAE）的对比；数据集为私有，无法复现；仅评估四拍窗口，未见长序列生成能力；未讨论DAC解码器引入的伪影。

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

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
