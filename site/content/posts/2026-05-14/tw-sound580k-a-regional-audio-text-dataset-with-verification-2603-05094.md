---
title: "TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#指令微调", "#数据构建", "#方言语音", "#语音识别", "#音频-语言模型"]
summary: "提出TW-Sound580K，一个台湾地区音频-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，并基于DeSTA 2.5微调得到Tai-LALM，在TAU基准上提升6.5%准确率。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频-语言模型</span> <span class="tag-pill tag-pill-soft">#方言语音</span> <span class="tag-pill tag-pill-soft">#数据构建</span> <span class="tag-pill tag-pill-soft">#指令微调</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.05094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.05094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.05094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出TW-Sound580K，一个台湾地区音频-文本指令数据集，通过验证-生成-批评协议和双ASR验证构建，并基于DeSTA 2.5微调得到Tai-LALM，在TAU基准上提升6.5%准确率。
</div>

## 👥 作者与机构

**Hao-Hui Xie** ¹ · Ho-Lam Chung · Yi-Cheng Lin · Ke-Han Lu · Wenze Ren · Xie Chen · Hung-yi Lee

**机构**：National Taiwan University

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事方言语音识别、音频-语言模型数据构建的研究者。建议通读，重点看§3数据构建流程（VGC协议）和§4.2动态双ASR仲裁策略。可复现其数据筛选方法。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 提升大型音频-语言模型对台湾地区方言韵律的识别能力。 |
| **核心创新** | 提出Verify-Generate-Critique数据构建协议，利用双ASR验证过滤低质量音频 · 引入动态双ASR仲裁策略，在推理时优化转录选择 · 构建首个大规模台湾地区音频-文本指令数据集TW-Sound580K |
| **模型架构** | 输入音频 → DeSTA 2.5-Audio初始化主干（预训练音频编码器+语言模型） → 指令微调 → 输出文本。关键模块：动态双ASR仲裁（推理时并行使用两个ASR系统，根据置信度选择转录）。参数量未明确给出。 |
| **数据集** | TW-Sound580K（训练，台湾地区音频-文本指令数据集） · TAU Benchmark（评估，方言语音理解基准） |
| **关键结果** | 在TAU Benchmark上，Tai-LALM达到49.1%准确率，相比零样本基线（42.6%，使用ASR文本条件）绝对提升6.5%。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但数据构建方法（双ASR验证过滤）可迁移至语音增强或语音分离中的噪声/语音质量筛选；动态仲裁策略可用于多系统融合。

## ⚠️ 局限与未解决问题

数据集仅覆盖台湾地区，泛化性未知；未报告模型参数量及推理延迟；缺乏与更大规模LALM（如Whisper）的对比；未消融VGC各组件贡献。

## 📋 引用

```bibtex
@article{xie20262603,
  title  = {TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling},
  author = {Hao-Hui Xie and  Ho-Lam Chung and  Yi-Cheng Lin and  Ke-Han Lu and  Wenze Ren and  Xie Chen and  Hung-yi Lee},
  journal = {arXiv preprint arXiv:2603.05094},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
