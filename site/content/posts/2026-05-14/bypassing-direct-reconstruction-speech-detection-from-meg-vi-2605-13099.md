---
title: "Bypassing Direct Reconstruction: Speech Detection from MEG via Large-Scale Audio Retrieval"
date: 2026-05-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#MEG", "#对比学习", "#脑信号解码", "#语音检测", "#语音检索"]
summary: "提出两阶段框架，先通过对比学习从大规模音频库检索与MEG匹配的语音片段，再基于检索音频进行语音/静音检测，在LibriBrain 2025任务中取得第一。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脑信号解码</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#语音检索</span> <span class="tag-pill tag-pill-soft">#MEG</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13099</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13099" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13099" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段框架，先通过对比学习从大规模音频库检索与MEG匹配的语音片段，再基于检索音频进行语音/静音检测，在LibriBrain 2025任务中取得第一。
</div>

## 👥 作者与机构

**Boda Xiao** ¹ · Bo Wang · Heping Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事脑信号解码、语音检测或跨模态检索的研究者。建议重点阅读§3的框架设计和§4的实验结果，尤其是检索模块的对比学习细节。可先看表1的F1分数对比。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从非侵入性脑磁图（MEG）信号中检测语音活动，用于脑机接口或神经科学研究。 |
| **核心创新** | 绕过直接重建，利用大规模音频检索辅助语音检测 · 对比学习实现MEG到音频的跨模态匹配 · 两阶段框架将复杂解码转化为检索+分类问题 |
| **模型架构** | 输入：MEG信号 → 第一阶段：对比学习模型（编码器将MEG和音频映射到共享嵌入空间，从LibriVox库检索最匹配音频）→ 第二阶段：语音检测模型（基于检索音频输出二进制静音/语音序列）→ 输出：语音活动序列。未提及参数量。 |
| **数据集** | LibriBrain 2025（训练和评估） · LibriVox（外部音频库，用于检索） |
| **关键结果** | 在LibriBrain 2025 Speech Detection扩展赛道取得第一名，F1-score为0.962。未提供与其他基线的对比。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音检测是语音增强和分离的前置任务，其检索+分类思路可迁移至语音增强中的噪声类型识别或说话人日志。

## ⚠️ 局限与未解决问题

依赖外部音频库的覆盖度，若测试语音不在库中可能失效；未报告检索模块的延迟和计算开销；缺乏与传统端到端方法的直接对比；仅在单一数据集上验证。

## 📋 引用

```bibtex
@article{xiao20262605,
  title  = {Bypassing Direct Reconstruction: Speech Detection from MEG via Large-Scale Audio Retrieval},
  author = {Boda Xiao and  Bo Wang and  Heping Cheng},
  journal = {arXiv preprint arXiv:2605.13099},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/posts/2026-05-14/">← 返回 2026-05-14 速递</a></div>
