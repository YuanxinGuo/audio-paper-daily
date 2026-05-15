---
title: "Bypassing Direct Reconstruction: Speech Detection from MEG via Large-Scale Audio Retrieval"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#MEG", "#对比学习", "#脑信号解码", "#语音检测", "#音频检索"]
summary: "提出两阶段框架，先通过对比学习从大规模音频库检索匹配语音，再基于检索音频进行语音检测，在LibriBrain 2025任务中取得第一。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#脑信号解码</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#音频检索</span> <span class="tag-pill tag-pill-soft">#MEG</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.13099</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.13099" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.13099" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段框架，先通过对比学习从大规模音频库检索匹配语音，再基于检索音频进行语音检测，在LibriBrain 2025任务中取得第一。
</div>

## 👥 作者与机构

**Boda Xiao** ¹ · Bo Wang · Heping Cheng

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事脑信号解码、语音检测或跨模态检索的研究者。重点看§3方法部分和§4实验结果。建议先读§3.1对比学习检索和§3.2语音检测模块，再对比表1中的消融实验。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 从非侵入性脑磁图（MEG）信号中检测语音活动。 |
| **核心创新** | 绕过直接重建，利用大规模音频库检索辅助语音检测 · 对比学习实现MEG与音频跨模态对齐 · 两阶段框架在LibriBrain 2025竞赛中取得最优F1 |
| **模型架构** | 输入：测试MEG信号 → 第一阶段：对比学习模型（MEG编码器+音频编码器）从LibriVox库检索最匹配的语音片段 → 第二阶段：语音检测模型（基于检索音频）输出二进制静音/语音序列。未提及参数量。 |
| **数据集** | LibriBrain 2025（训练/评估） · LibriVox（音频检索库） |
| **关键结果** | 在LibriBrain 2025 Speech Detection扩展赛道取得F1-score 0.962，排名第一。未提供与基线对比的具体数值。 |

## 🎯 与本站重点领域的关联

与本站重点领域无直接关联。但语音检测是语音增强和分离的前置任务，其检索+检测的思路可迁移至语音增强中的噪声估计或目标说话人提取中的辅助信息利用。

## ⚠️ 局限与未解决问题

依赖大规模外部音频库，检索库的覆盖度和质量影响性能；未报告推理延迟；缺乏与直接重建方法的详细对比；未提供消融实验验证各组件贡献。

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

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
