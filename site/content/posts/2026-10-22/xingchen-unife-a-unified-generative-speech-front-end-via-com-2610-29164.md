---
title: "XingChen-UniFE: A Unified Generative Speech Front-End via Complementary Acoustic-Semantic Modeling"
date: 2026-10-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出双流编码器融合语义与声学表征，驱动大音频语言模型统一完成通用语音修复与目标说话人提取。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.29164</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.29164" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.29164" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双流编码器融合语义与声学表征，驱动大音频语言模型统一完成通用语音修复与目标说话人提取。
</div>

## 👥 作者与机构

**Kelan Kuang** ¹ · Qihan Hu · Jian Kang · Jie Li · Yongxiang Li · Yi Liu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音前端统一建模与 LALM 语音生成的研究者阅读。建议通读，重点看 §3 双流编码器与双向交叉注意力设计，以及 GSR/TSE 联合训练的消融表；若关注落地，需核对推理延迟与 token 生成开销。

## 🌍 研究背景

通用语音修复（GSR）与目标说话人提取（TSE）长期被当作两个独立任务，各自有专用模型：GSR 常用 BSRNN、Demucs 等判别式结构，TSE 多依赖 speaker embedding 条件化的时频掩码网络。这些方法任务专用、难以共享表征，且对未见退化条件泛化有限。近期大音频语言模型（LALM）展现出统一建模潜力，但如何把细粒度声学结构与高层语义有效注入离散 token 生成仍是开放问题。本文试图用单一 LALM 同时覆盖 GSR 与 TSE。

## 💡 核心创新

1. 双流编码器：SSL 语义分支 + 可学习声学分支并行建模
2. 双向交叉注意力实现语义与声学表征互融
3. 以任务与说话人信息条件化 LALM 生成离散语音 token
4. 单一模型统一 GSR 与 TSE 两类前端任务

## 🏗️ 模型架构

输入为含噪/含混语音的复杂频谱。双流编码器中，自监督学习模型（SSL）提供分层语义特征，可学习声学分支从复杂频谱提取细粒度结构；双向交叉注意力模块在两条流之间交换信息，得到融合表征。融合表征连同任务标识与说话人信息作为条件，驱动大音频语言模型自回归生成离散语音 token，再解码为修复后语音。摘要未给出参数量与具体 SSL 骨干名称。

## 📊 实验结果

摘要仅声称在 GSR 与 TSE 上均取得强性能，并对未见退化条件具备稳健泛化，但未给出任何具体指标数值、测试集名称或与基线的对比结果，因此无法量化评估改进幅度。

## 🎯 结论与影响

最强结论是用双流语义-声学表征条件化 LALM，可在单一模型中统一 GSR 与 TSE 并泛化到未见退化。这为语音前端从任务专用判别模型转向生成式统一建模提供了可行路径，若推理成本可控，对统一降噪/提取的工业管线有参考价值。

## ⚠️ 局限与未解决问题

摘要缺少具体指标、数据集与基线对比，难以判断相对 SOTA 的真实增益；未报告参数量、推理延迟与 token 生成开销，LALM 方案的实际部署成本存疑；双流与交叉注意力的贡献缺乏消融证据；TSE 的说话人线索形式（embedding 还是注册语音）未说明。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-22/">← 返回 2026-10-22 速递</a></div>
