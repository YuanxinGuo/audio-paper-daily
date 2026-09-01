---
title: "WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs"
date: 2026-09-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出WnW方法，通过分类KV头为锚定、潮汐和固定角色，在长语音LLM中仅保留20%音频token在GPU上，保持接近全缓存的准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#KV缓存压缩</span> <span class="tag-pill tag-pill-soft">#长语音</span> <span class="tag-pill tag-pill-soft">#语音LLM</span> <span class="tag-pill tag-pill-soft">#注意力机制</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.22704</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.22704" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.22704" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出WnW方法，通过分类KV头为锚定、潮汐和固定角色，在长语音LLM中仅保留20%音频token在GPU上，保持接近全缓存的准确率。
</div>

## 👥 作者与机构

**Yiming Yao** ¹ · Chenyang Lyu · Xuanfan Ni · Longyue Wang · Weihua Luo · Yazheng Yang · Jinsong Su

**机构**：厦门大学 · 腾讯

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究语音LLM推理效率、KV缓存压缩的学者。建议重点阅读第3节方法设计和第4节实验部分，尤其是表1和表2。可先看§3.2的KV头分类策略和§4.2的准确率对比。

## 🌍 研究背景

长语音输入使KV缓存成为语音LLM的主要内存开销。现有预填充压缩方法在驱逐音频KV后无法恢复，导致长音频上性能下降。本文发现预填充注意力集中在音频起始（注意力汇聚效应），而解码时注意力分布广泛，两者重叠弱。因此提出WnW，通过离线校准分类KV头，动态管理缓存，解决长语音场景下KV缓存压缩的难题。

## 💡 核心创新

1. 提出WnW，动态管理KV缓存，支持解码时恢复被驱逐的音频KV
2. 基于注意力汇聚效应，将KV头分为锚定、潮汐和固定三类
3. 锚定头提供解码时信号，潮汐头按块召回CPU补充
4. 在3B模型上仅用20%GPU token保持接近全缓存准确率
5. 跨语言、任务和领域泛化验证

## 🏗️ 模型架构

输入为长语音音频特征，主干为语音LLM（Voxtral-mini-3b或Qwen2.5-Omni-3B）。WnW通过离线校准将KV头分类：锚定头保留全部音频KV在GPU，并产生解码时信号指示每个token读取的音频区域；潮汐头保留CPU端补充，根据锚定头分数按块召回；固定头仅保留GPU子集，其余永久丢弃。输出为文本token序列。

## 📚 数据集

- LibriSpeech-Long（评估，长语音测试集）
- 其他语言、任务和领域数据集（泛化评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率（接近全缓存） | LibriSpeech-Long | 预填充压缩基线（无法终止） | **WnW（20% GPU token）** | 保持接近全缓存准确率 |

在LibriSpeech-Long上，WnW在仅保留20%音频token在GPU时，准确率接近全缓存，而预填充压缩基线无法终止。结果在语言、任务和领域变化上泛化，CPU-GPU召回增加的解码开销很小。

## 🎯 结论与影响

WnW通过动态管理KV缓存，显著降低长语音LLM的内存占用，同时保持高准确率，为长语音推理提供了高效方案。对后续研究，可探索更细粒度的KV头分类和自适应策略。工业上，可降低长语音服务的部署成本。

## ⚠️ 局限与未解决问题

未报告推理延迟的具体数值，仅称开销小。未与其他动态KV压缩方法对比。依赖离线校准，可能需针对不同模型重新校准。未讨论极端长音频或流式场景。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-09-01/">← 返回 2026-09-01 速递</a></div>
