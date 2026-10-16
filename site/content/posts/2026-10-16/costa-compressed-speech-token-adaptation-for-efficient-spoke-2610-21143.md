---
title: "CoSTA: Compressed Speech Token Adaptation for Efficient Spoken Dialogue Models"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话模型"]
summary: "CoSTA 通过均值初始化词表扩展与发音/对话适配，将生成与合成 token 空间解耦，实现约 1.7 倍语音 token 生成加速且保持回复质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话模型</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音对话</span> <span class="tag-pill tag-pill-soft">#语音token压缩</span> <span class="tag-pill tag-pill-soft">#自回归生成加速</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.21143</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.21143" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.21143" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>CoSTA 通过均值初始化词表扩展与发音/对话适配，将生成与合成 token 空间解耦，实现约 1.7 倍语音 token 生成加速且保持回复质量。
</div>

## 👥 作者与机构

**Yingzhuo Deng** ¹ · Chong Li · Bingxin Liu · Yi Shu · Tianyu Peng · Can Xie · Siyao Song · Shuo Ren · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音对话系统（SDM）推理加速与低码率 tokenizer 的研究者与工程团队阅读。建议重点看 §3 的词表扩展与确定性扩展机制，以及表 2/表 3 中压缩率、延迟与质量的权衡曲线；若关注落地，可先看效率与吞吐实验部分。

## 🌍 研究背景

语音对话模型（SDM）通常让生成与合成共享同一 speech-token 空间，导致自回归序列过长、推理成本高。已有做法是换用低码率 tokenizer 缩短序列，但会带来压缩-质量权衡，且需替换整套 tokenizer/decoder，代价高、兼容性差。本文要解决的是：在不更换原 tokenizer 与 decoder 的前提下，降低生成端序列长度、加速推理，同时保持回复质量。

## 💡 核心创新

1. 均值初始化词表扩展，向生成 token 空间注入压缩表示
2. 发音适配与对话适配两阶段后训练，缓解压缩带来的质量损失
3. 确定性扩展回原 speech-token 空间，保持合成端兼容
4. 生成与合成 token 空间解耦的 post-hoc 框架

## 🏗️ 模型架构

输入为对话上下文对应的 speech token 序列，主干沿用原 SDM 的自回归生成网络。CoSTA 在生成端词表中通过均值初始化新增压缩 token 词条，扩展生成 token 空间；随后进行发音适配与对话适配微调，使模型学会使用压缩表示；生成完成后，通过确定性映射将压缩 token 扩展回原始 speech-token 空间，再送入原有 decoder 合成语音。整个流程不修改原 tokenizer 与 decoder，属 post-hoc 兼容式改造。

## 📚 数据集

- 双语语音对话基准（评估，摘要未给出具体名称与规模）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| speech-token 生成速度 | 双语语音对话基准 | 原始 SDM 生成速度 | **约 1.7× 加速** | +1.7× |

摘要报告约 1.7 倍 speech-token 生成加速、更低的全回复延迟与更高吞吐，同时保持回复质量。分析显示在有限预算下交互更持久，并呈现压缩、解码效率与质量之间的实际权衡。另有实验表明方法可跨架构迁移，并与低码率 tokenization 互补。摘要未给出 SI-SDR/PESQ/WER 等具体数值。

## 🎯 结论与影响

最强结论是：无需替换 tokenizer 与 decoder，仅通过生成端词表扩展与适配即可获得约 1.7 倍生成加速并保持质量。这为 SDM 推理加速提供了一条低侵入路径，可能推动后续研究在 token 空间解耦与压缩-效率权衡上继续探索；工业上有利于在既有 SDM 部署上低成本提速。

## ⚠️ 局限与未解决问题

摘要未给出具体质量指标数值与统计显著性，缺少与低码率 tokenizer 方案的直接对比；压缩率、延迟、质量三者权衡的边界条件未量化；未报告额外训练成本与推理显存开销；跨架构迁移的适用范围与失败案例未说明。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
