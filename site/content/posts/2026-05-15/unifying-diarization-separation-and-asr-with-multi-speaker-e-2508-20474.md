---
title: "Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#多说话人ASR", "#多说话人语音处理", "#联合训练", "#语音分离", "#说话人日志"]
summary: "提出统一多说话人编码器（UME），通过共享语音基础编码器和残差加权和编码联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#多说话人语音处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#联合训练</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2508.20474</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2508.20474" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2508.20474" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一多说话人编码器（UME），通过共享语音基础编码器和残差加权和编码联合学习说话人日志、语音分离和多说话人ASR，在LibriMix上显著优于单任务基线。
</div>

## 👥 作者与机构

**Muhammad Shakeel** ¹ · Yui Sudo · Yifan Peng · Chyi-Jiunn Lin · Shinji Watanabe

**机构**：CMU

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事说话人日志、语音分离或多说话人ASR的研究者。建议通读，重点看§3的UME架构和§4的实验结果，特别是表1-3的对比。可先看§3.2的残差加权和编码设计。

## 🧩 模型一栏概览

| 项 | 内容 |
| --- | --- |
| **应用场景** | 重叠语音场景下的多说话人语音处理，如会议转录、对话分析。 |
| **核心创新** | 共享语音基础编码器联合学习三个任务 · 残差加权和编码利用多层语义信息 · 任务间自底向上对齐提升重叠语音性能 |
| **模型架构** | 输入语音特征 → 共享语音基础编码器（如WavLM） → 从多层提取隐藏表示 → 残差加权和编码（RWSE）融合 → 分别输出说话人日志、分离语音和ASR结果。参数量未明确给出。 |
| **数据集** | LibriMix（训练和评估） · Libri2Mix（评估） · Libri3Mix（评估） |
| **关键结果** | 在Libri2Mix和Libri3Mix上，说话人日志DER分别为1.37%和2.29%，优于先前研究；语音分离和多说话人ASR也显著优于单任务基线，具体指标见原文。 |

## 🎯 与本站重点领域的关联

直接相关语音分离和说话人日志，同时涉及多说话人ASR。对语音增强有间接参考价值（重叠语音处理）。双耳音频和乐器分离不直接相关。

## ⚠️ 局限与未解决问题

仅在LibriMix上评估，缺乏真实场景（如会议、噪声）验证；未报告推理延迟和模型参数量；未与端到端联合模型（如EEND-EDA）对比；缺少消融实验验证RWSE各层贡献。

## 📋 引用

```bibtex
@article{shakeel20262508,
  title  = {Unifying Diarization, Separation, and ASR with Multi-Speaker Encoder},
  author = {Muhammad Shakeel and  Yui Sudo and  Yifan Peng and  Chyi-Jiunn Lin and  Shinji Watanabe},
  journal = {arXiv preprint arXiv:2508.20474},
  year   = {2026}
}
```

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
