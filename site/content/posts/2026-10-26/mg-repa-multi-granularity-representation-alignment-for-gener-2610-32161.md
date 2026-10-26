---
title: "MG-REPA: Multi-Granularity Representation Alignment for Generative Target Speaker Extraction"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出多粒度表征对齐 MG-REPA，用帧级 SSL 与句级说话人验证模型双分支对齐，加速生成式目标说话人提取训练收敛。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#表征对齐</span> <span class="tag-pill tag-pill-soft">#自监督学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32161</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32161" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32161" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多粒度表征对齐 MG-REPA，用帧级 SSL 与句级说话人验证模型双分支对齐，加速生成式目标说话人提取训练收敛。
</div>

## 👥 作者与机构

**Dohwan Kim** ¹ · Jung-Woo Choi

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做生成式 TSE、扩散/流匹配加速、REPA 类表征对齐的研究者阅读。值得通读，重点看 §3 多粒度对齐设计与时间归一化细节，以及表 2 的收敛曲线和消融表；若只关心结论，看摘要与消融部分即可。

## 🌍 研究背景

生成式 TSE（如基于扩散/MeanFlow 的模型）提取质量高，但训练收敛极慢，需上千 epoch。REPA 通过将扩散 Transformer 隐状态与预训练 SSL 教师对齐来加速训练，已在图像领域验证有效。然而语音/音频领域的现有对齐仅用单一粒度：帧级对齐无法约束目标语音的全局时不变特性（说话人身份），句级对齐又丢失时变内容，而 TSE 同时需要两者。本文要解决的是如何在生成式 TSE 中设计多粒度对齐以兼顾内容与说话人信息并加速收敛。

## 💡 核心创新

1. 帧级用 SSL 模型对齐，约束时变内容
2. 句级用说话人验证模型对齐，约束说话人身份
3. 对帧级目标做时间归一化，去除句级统计量
4. 双分支各专注单一粒度，避免信息冗余

## 🏗️ 模型架构

输入为目标说话人线索与混合语音，主干为生成式扩散 Transformer（MeanFlow-TSE 框架）。在训练时对 Transformer 隐状态施加两路对齐损失：帧级分支将隐状态与预训练 SSL 模型（如 WavLM/HuBERT 类）的帧级表征对齐，并对该目标做时间归一化以剥离句级统计；句级分支将池化后的隐状态与说话人验证模型（如 ECAPA-TDNN 类）的句嵌入对齐。推理时对齐分支移除，仅保留生成主干输出提取的语音。摘要未给出参数量。

## 📚 数据集

- Libri2Mix（训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| OVRL | Libri2Mix | MeanFlow-TSE（2000 epoch） | **达到基线水平，仅用 3.0× 更少 epoch** | 训练加速 3.0× |
| PESQ | Libri2Mix | MeanFlow-TSE（2000 epoch） | **达到基线水平，仅用 2.1× 更少 epoch** | 训练加速 2.1× |

在 Libri2Mix 上，MG-REPA 以 3.0×（OVRL）和 2.1×（PESQ）更少 epoch 达到 MeanFlow-TSE 基线的对应指标；训练 750 epoch 即在侵入式指标上与已发表 2000 epoch 基线相当，并提升非侵入式指标。消融显示多粒度对齐优于任一单粒度对齐。摘要未给出具体数值与推理效率数据。

## 🎯 结论与影响

最强结论是双粒度表征对齐可在显著减少训练 epoch 的同时保持甚至提升生成式 TSE 质量。这为生成式语音模型训练加速提供了可复用范式，提示后续工作可探索更多粒度或跨模态教师。工业落地含义是降低大模型 TSE 的训练成本与迭代周期。

## ⚠️ 局限与未解决问题

仅在 Libri2Mix 单一模拟数据集验证，缺乏真实录音与跨数据集泛化实验；未报告推理延迟与参数量开销；对比基线仅 MeanFlow-TSE，未与 SEPFormer、BSRNN 等判别式 TSE 系统比较；消融规模有限。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
