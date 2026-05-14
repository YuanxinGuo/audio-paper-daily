---
title: "LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#LMU", "#后验融合", "#婴儿哭声分类", "#跨域泛化"]
summary: "提出基于LMU的时序建模与后验融合框架，融合多特征进行跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#婴儿哭声分类</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#婴儿哭声分类</span> <span class="tag-pill tag-pill-soft">#LMU</span> <span class="tag-pill tag-pill-soft">#后验融合</span> <span class="tag-pill tag-pill-soft">#跨域泛化</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02245</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02245" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02245" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LMU的时序建模与后验融合框架，融合多特征进行跨域婴儿哭声分类，在Baby2020和Baby Crying数据集上提升宏F1。
</div>

## 👥 作者与机构

**Niloofar Jazaeri** ¹ · Hilmi R. Dajani · Marco Janeczek · Martin Bouchard

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事婴儿哭声分析或小样本音频分类的研究者。重点看§3的LMU时序建模和§4的后验融合策略，表2的跨域结果值得细读。建议先看§3.2与表2。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 用于婴儿哭声的跨域分类，支持实时设备端监测。 |
| **核心创新** | 用LMU替代LSTM实现稳定时序建模且参数量更少 · 提出熵门控加权后验融合提升跨域泛化 · 融合MFCC、STFT和F0多分支特征 |
| **模型架构** | 输入MFCC、STFT和F0三路特征 → 多分支CNN编码器 → 增强型LMU时序建模 → 全连接分类 → 后验融合（熵门控加权）。参数量未明确给出。 |
| **数据集** | Baby2020（训练与评估） · Baby Crying（跨域评估） |
| **关键结果** | 在Baby2020和Baby Crying数据集上，跨域评估宏F1优于LSTM基线，具体数值未在摘要中给出。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但LMU时序建模和后验融合策略可迁移至语音增强/分离中的时序建模与多系统融合。

## ⚠️ 局限与未解决问题

摘要未提供具体宏F1数值及与强基线对比；未报告模型参数量和推理延迟；仅两个数据集，域偏移多样性有限；缺乏消融实验验证各组件贡献。

## 📋 引用

```bibtex
@article{jazaeri20262603,
  title  = {LMU-Based Sequential Learning and Posterior Ensemble Fusion for Cross-Domain Infant Cry Classification},
  author = {Niloofar Jazaeri and  Hilmi R. Dajani and  Marco Janeczek and  Martin Bouchard},
  journal = {arXiv preprint arXiv:2603.02245},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
