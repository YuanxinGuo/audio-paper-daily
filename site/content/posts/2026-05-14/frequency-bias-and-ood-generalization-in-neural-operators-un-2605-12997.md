---
title: "Frequency Bias and OOD Generalization in Neural Operators under a Variable-Coefficient Wave Equation"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#分布外泛化", "#波动方程", "#物理模拟", "#神经算子", "#频率偏差"]
summary: "研究FNO和DeepONet在变系数波动方程下对频率和光滑度分布偏移的泛化能力，发现频率偏移下FNO误差激增而DeepONet更稳健。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#物理模拟</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#神经算子</span> <span class="tag-pill tag-pill-soft">#分布外泛化</span> <span class="tag-pill tag-pill-soft">#波动方程</span> <span class="tag-pill tag-pill-soft">#频率偏差</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.12997</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.12997" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.12997" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>研究FNO和DeepONet在变系数波动方程下对频率和光滑度分布偏移的泛化能力，发现频率偏移下FNO误差激增而DeepONet更稳健。
</div>

## 👥 作者与机构

**Runlong Xie** ¹ · An Luo

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合对神经算子泛化性感兴趣的读者。重点看§3实验设置和§4结果分析，可先看表1和图2。无需通读全文。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 用于快速预测波动方程在不同初始条件下的终端解。 |
| **核心创新** | 系统分析频率和光滑度偏移对神经算子的影响 · 揭示FNO和DeepONet在频率偏移下的不同行为 · 指出架构表示偏差对OOD泛化的关键作用 |
| **模型架构** | 输入为初始条件函数，FNO通过傅里叶层在频域学习映射，DeepONet通过分支网络和主干网络组合学习算子。未提及参数量。 |
| **数据集** | 一维变系数波动方程模拟数据（训练和测试） |
| **关键结果** | 在光滑度偏移下，FNO和DeepONet性能稳定，FNO误差更低；在频率偏移下，FNO对未见高频输入误差急剧上升，DeepONet退化较缓但整体误差更高。具体数值未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但研究频率偏差对模型泛化的影响，对语音增强中处理未见噪声频谱或语音分离中处理未见音高可能具有迁移思路。

## ⚠️ 局限与未解决问题

仅在一维波动方程上实验，未扩展到高维或更复杂PDE；未提供模型参数量和推理时间；缺乏对频率偏移下误差来源的深入消融分析。

## 📋 引用

```bibtex
@article{xie20262605,
  title  = {Frequency Bias and OOD Generalization in Neural Operators under a Variable-Coefficient Wave Equation},
  author = {Runlong Xie and  An Luo},
  journal = {arXiv preprint arXiv:2605.12997},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
