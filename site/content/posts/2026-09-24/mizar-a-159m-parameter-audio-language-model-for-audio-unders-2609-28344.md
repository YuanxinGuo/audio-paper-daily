---
title: "Mizar: A 159M-Parameter Audio-Language Model for Audio Understanding"
date: 2026-09-24T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "Mizar 用 159.3M 参数把 CED-Small 音频编码器接到 SmolLM2-135M，经三阶段训练在 MMAU/MMAR/ADQA 上超过同规模 ALM。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频语言模型</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#高效推理</span> <span class="tag-pill tag-pill-soft">#音频问答</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.28344</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/KaiyangLi1992/Mizar_159M" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">KaiyangLi1992/Mizar_159M</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.28344" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.28344" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/KaiyangLi1992/Mizar_159M" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Mizar 用 159.3M 参数把 CED-Small 音频编码器接到 SmolLM2-135M，经三阶段训练在 MMAU/MMAR/ADQA 上超过同规模 ALM。
</div>

## 👥 作者与机构

**Kaiyang Li** ¹ · Shaobo Han · Yue Tian · Shihao Ji

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做端侧多模态、小规模 ALM 与音频问答的研究者与工程团队阅读。建议通读，重点看 §3 的三阶段训练配方与 frequency-merging mapper 设计，以及表 2 的五个随机种子结果；若关注部署，直接看 CPU 延迟 1.09 s 的实验设置与量化细节。

## 🌍 研究背景

音频语言模型（ALM）把声学感知与语言模型知识结合，但主流方案参数量大、显存与算力需求高，难以在端侧落地。此前 200M 以下的小 ALM 在 MMAU、MMAR 等推理型音频问答基准上表现有限，主要瓶颈在于音频编码器与语言模型之间的模态对齐不足、训练数据与阶段划分粗糙。本文针对 <200M 参数区间，提出架构、数据与三阶段训练的组合配方，目标是在保持小体积的同时提升音频理解准确率并支持 CPU 本地推理。

## 💡 核心创新

1. CED-Small + SmolLM2-135M 的 159.3M 紧凑 ALM 架构
2. frequency-merging mapper 做音频-语言模态对齐
3. 三阶段训练：对齐、音频依赖微调、后训练补弱项
4. ReasonAQA/AudioMCQ/AVQA 混合监督数据配方
5. 单 CPU 本地推理，MMAU 平均延迟 1.09 s

## 🏗️ 模型架构

输入为原始音频波形，经 CED-Small 音频编码器提取帧级声学表征；随后由 frequency-merging mapper 在频域维度做下采样与投影，压缩 token 数并映射到 SmolLM2-135M 的文本嵌入空间；语言模型以自回归方式生成答案。整体参数量 159.3M，其中音频编码器与语言模型均取小规模配置，mapper 为轻量模块。训练分三阶段：Stage 1 音频-语言对齐，Stage 2 音频依赖微调，Stage 3 后训练强化弱技能并保留已学能力。

## 📚 数据集

- ReasonAQA（训练监督）
- AudioMCQ（训练监督）
- AVQA（训练监督）
- MMAU / MMAR / ADQA-clean（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | MMAU | 此前 <200M 最佳 ALM | **52.92%** | 超过此前最佳 |
| Accuracy | MMAR | 此前 <200M 最佳 ALM | **42.42%** | 超过此前最佳 |
| Accuracy | ADQA-clean | 此前 <200M 最佳 ALM | **36.02%** | 超过此前最佳 |

摘要报告五个随机种子下的平均准确率：MMAU 52.92%、MMAR 42.42%、ADQA-clean 36.02%，三项均超过此前 200M 以下最佳 ALM。部署侧给出单 CPU 本地推理结果：MMAU 问题从打开音频文件到生成完整答案平均延迟 1.09 秒。摘要未给出各阶段消融、mapper 变体对比或与更大模型的差距分析。

## 🎯 结论与影响

最强结论是：在 159.3M 参数预算内，通过架构、数据与三阶段训练的组合配方，可在多个音频理解基准上超过同规模 ALM 并实现 CPU 实时推理。这为端侧音频理解提供了可复现的小模型基线，后续研究可围绕 mapper 设计、阶段划分与数据配比继续优化。工业上意味着无需 GPU 即可在本地设备部署音频问答能力。

## ⚠️ 局限与未解决问题

摘要仅给出三项基准的准确率，缺少与更大 ALM 的对比、各训练阶段与 mapper 的消融、以及延迟测试的硬件与量化配置。训练数据以问答/多选题为主，可能带来基准偏置；未报告内存占用、能耗与多语言泛化，也未说明 ADQA-clean 之外噪声条件下的鲁棒性。

## 🔗 开源资源

- **代码**：<https://github.com/KaiyangLi1992/Mizar_159M>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-24/">← 返回 2026-09-24 速递</a></div>
