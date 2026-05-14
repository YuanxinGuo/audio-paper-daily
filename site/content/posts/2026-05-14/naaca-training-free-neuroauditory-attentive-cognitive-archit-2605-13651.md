---
title: "NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力", "#工作记忆", "#训练无关", "#音频事件检测", "#音频语言模型"]
summary: "提出一种无需训练的神经听觉认知架构NAACA，通过振荡工作记忆（OWM）模拟听觉显著性过滤，在XD-Violence上将AudioQwen的平均精度从53.50%提升至70.60%，同时减少不必要的ALM调用。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听觉注意力</span> <span class="tag-pill tag-pill-soft">#工作记忆</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#训练无关</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13651</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13651" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13651" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种无需训练的神经听觉认知架构NAACA，通过振荡工作记忆（OWM）模拟听觉显著性过滤，在XD-Violence上将AudioQwen的平均精度从53.50%提升至70.60%，同时减少不必要的ALM调用。
</div>

## 👥 作者与机构

**Zhongju Yuan** ¹ · Geraint Wiggins · Dick Botteldooren

**机构**：Ghent University · Queen Mary University of London

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对音频语言模型注意力机制、认知架构或事件检测感兴趣的读者。建议重点阅读§3的OWM机制和§4.1的定量结果，可先看表1与图3理解性能提升。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 长时音频记录中的罕见显著性事件检测与定位。 |
| **核心创新** | 将注意力分配重构为听觉显著性过滤问题 · 提出振荡工作记忆（OWM）模拟吸引子状态与能量波动 · 无需训练即可提升ALM性能并降低计算开销 |
| **模型架构** | 输入音频特征 → OWM模块（神经振荡器维持稳定吸引子状态，检测能量波动）→ 当能量波动超过阈值时触发ALM（如AudioQwen）进行高层推理 → 输出事件标签。无额外训练参数。 |
| **数据集** | XD-Violence（评估） · Urban Soundscapes of the World (USoW)（定性案例） |
| **关键结果** | 在XD-Violence上，NAACA将AudioQwen的平均精度（AP）从53.50%提升至70.60%，提升17.10个百分点，同时减少了不必要的ALM调用次数。USoW数据集定性案例显示OWM能捕获新事件和子类别转移，对短暂停顿和环境噪声鲁棒。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。本文主要关注音频事件检测和ALM效率，而非语音增强、分离或双耳音频。但其中的显著性过滤和注意力门控机制可迁移至语音增强中的噪声事件抑制或目标说话人提取中的注意力聚焦。

## ⚠️ 局限与未解决问题

仅在两个数据集上评估，缺乏大规模消融实验；未报告推理延迟或计算量对比；OWM阈值设定依赖经验，未讨论自适应方法；定性案例缺乏量化指标。

## 📋 引用

```bibtex
@article{yuan20262605,
  title  = {NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating},
  author = {Zhongju Yuan and  Geraint Wiggins and  Dick Botteldooren},
  journal = {arXiv preprint arXiv:2605.13651},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
