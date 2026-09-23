---
title: "Modality-Gated Deep Adapters: Adding a Modality to a Frozen Embedding Model with Exact Preservation"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频处理"]
summary: "提出模态门控深度适配器，在冻结多模态嵌入LLM上新增音频/热成像模态，保证原有输出逐位不变。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#参数高效微调</span> <span class="tag-pill tag-pill-soft">#多模态嵌入</span> <span class="tag-pill tag-pill-soft">#适配器</span> <span class="tag-pill tag-pill-soft">#音频-文本检索</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.26182</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-hf" href="https://huggingface.co/EximiusLabs" target="_blank" rel="noopener"><span class="oc-icon">🤗</span><span class="oc-text"><span class="oc-label">HuggingFace</span><span class="oc-sub">🤗 EximiusLabs</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.26182" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.26182" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-hf" href="https://huggingface.co/EximiusLabs" target="_blank" rel="noopener">🤗 HuggingFace</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出模态门控深度适配器，在冻结多模态嵌入LLM上新增音频/热成像模态，保证原有输出逐位不变。
</div>

## 👥 作者与机构

**Abdul Basit Tonmoy** ¹ · Kazi Fardinul Hoque · Md. Shahrier Islam Arham · Arman Luthra

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态嵌入、参数高效微调与检索系统的研究者阅读。若关注音频-文本检索或模态扩展的工程落地，建议通读；否则可先看 §3 门控适配器设计与隔离矩阵命题，再看表 1 的 R@10 对比与不变性测试。

## 🌍 研究背景

多模态嵌入模型已大规模部署，检索索引与行为审计依赖基座模型的精确输出。现有 LoRA 类参数高效方法在扩展新模态时会改写文本路径，即使权重合并也改变已存嵌入，导致索引失效。本文要在冻结基座上新增模态，同时保证原有输出逐位不变。

## 💡 核心创新

1. 每层解码器挂瓶颈适配器，按模态分组为 pack，仅编码该模态时执行
2. 无 pack 认领的输入走基座原计算图，逐位不变
3. 共载 pack 用精确零隔离矩阵组合，训练后仍成立
4. 音频以 connector token 注入，热成像复用冻结视觉路径

## 🏗️ 模型架构

输入为文本 token 或新模态 connector token；主干是冻结的 2B 多模态嵌入 LLM，每层解码器插入瓶颈适配器，按模态组成 pack。推理时仅激活对应模态 pack，其余输入走原图；多 pack 共载时用精确零隔离矩阵组合。输出为嵌入向量，用于检索。

## 📚 数据集

- 音频-文本检索数据（训练/评估，规模未详述）
- 热成像-文本数据（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| audio-to-text R@10 | 音频-文本检索 | 同训练控制组 | **+3.4 至 +5.4 点** | +3.4~+5.4 |
| thermal-to-text R@10 | 热成像-文本检索 | 0.224 | **0.785** | +0.561 |

音频 pack 在 11 倍数据上复现，每个随机种子均为正增益；热成像 pack 以约七倍余量通过预注册验收门。编码器替换实验显示，外部音频编码器在 CLAP 式比较中优于 Whisper 系，但在冻结 LLM 内 R@10 低 16 点，说明容量应放在层内。

## 🎯 结论与影响

最强结论是模态门控适配器可在冻结嵌入模型上新增模态且原有输出逐位不变。这为多模态检索系统的增量扩展提供了可验证的工程路径，降低重索引成本，对工业界维护大规模嵌入索引有直接意义。

## ⚠️ 局限与未解决问题

摘要未给出音频检索的绝对 R@10 与基线具体值，缺少与 LoRA 等方法的直接对比表；热成像仅一个数据集；未报推理延迟与适配器参数量；不变性仅在发布 checkpoint 上验证。

## 🔗 开源资源

- **HuggingFace**：<https://huggingface.co/EximiusLabs>

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
