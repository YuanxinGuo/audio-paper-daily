---
title: "NAACA: Training-Free NeuroAuditory Attentive Cognitive Architecture with Oscillatory Working Memory for Salience-Driven Attention Gating"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力", "#工作记忆", "#异常事件检测", "#音频事件检测", "#音频语言模型"]
summary: "提出无需训练的神经听觉认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的异常事件检测精度。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听觉注意力</span> <span class="tag-pill tag-pill-soft">#工作记忆</span> <span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#异常事件检测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13651</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13651" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13651" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出无需训练的神经听觉认知架构NAACA，通过振荡工作记忆模型实现基于显著性的注意力门控，显著提升音频语言模型在长时录音中的异常事件检测精度。
</div>

## 👥 作者与机构

**Zhongju Yuan** ¹ · Geraint Wiggins · Dick Botteldooren

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究音频事件检测、认知模型与ALM结合的学者。重点看§3的OWM机制与§4.1的XD-Violence实验结果。建议先读图2架构概览，再对比表1的AP提升。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 长时录音中的罕见/显著音频事件检测与定位。 |
| **核心创新** | 无需训练的神经认知架构，将注意力分配重构为听觉显著性过滤问题 · 振荡工作记忆模型，通过能量波动触发高层认知处理 · 在XD-Violence上提升AudioQwen AP 17个百分点并减少无效调用 |
| **模型架构** | 输入音频特征 → OWM（振荡工作记忆）模块，包含多个振荡器维持吸引子状态，通过能量波动检测显著性 → 当能量超过阈值时触发ALM（如AudioQwen）进行高层推理 → 输出事件类别与时间定位。OWM无需训练，参数量未给出。 |
| **数据集** | XD-Violence（评估） · Urban Soundscapes of the World (USoW)（定性案例） |
| **关键结果** | 在XD-Violence上，NAACA将AudioQwen的平均精度（AP）从53.50%提升至70.60%，同时减少不必要的ALM调用。USoW定性案例显示OWM能捕获新事件和子类别转换，对短暂停顿和环境噪声鲁棒。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但其中的听觉显著性过滤思路可迁移至语音增强中的非平稳噪声抑制，以及目标说话人提取中的注意力门控机制。

## ⚠️ 局限与未解决问题

仅在XD-Violence一个数据集上定量评估，缺乏与其他方法的对比（如基于能量的检测器）。未报告推理延迟或计算开销，OWM参数量未给出。定性案例缺乏量化指标。

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

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
