---
title: "CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频生成"]
summary: "提出免训练的音视频扩散缓存框架 CAVC，利用音频侧漂移可恢复、视频侧不可恢复的非对称性，中段缓存音频去噪与跨模态注意力，末段恢复联合去噪。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频生成</span> <span class="tag-pill tag-pill-soft">#扩散模型加速</span> <span class="tag-pill tag-pill-soft">#推理缓存</span> <span class="tag-pill tag-pill-soft">#跨模态对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.30854</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.30854" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.30854" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出免训练的音视频扩散缓存框架 CAVC，利用音频侧漂移可恢复、视频侧不可恢复的非对称性，中段缓存音频去噪与跨模态注意力，末段恢复联合去噪。
</div>

## 👥 作者与机构

**Lifan Jiang** ¹ · Yibo Zhao · Senlin cheng · Bolei Xu · Xiaobo Li · Can Ye · Dehai Zhao · Deng Cai · … 等 1 人

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做扩散模型推理加速、音视频联合生成的研究者与工程部署同学阅读。建议重点看 §3 关于 modality-asymmetric recoverability 的观测实验与缓存触发判据（收敛检测），以及表 2/表 3 的加速比与视觉动态指标；若关注音频质量，需细看音频保真度与同步性指标是否被牺牲。

## 🌍 研究背景

音视频联合扩散生成（如基于 latent diffusion 的音视频同步生成）通常在整条采样轨迹上对音频与视频 latent 做联合去噪，每个 timestep 都要跑两路模态去噪分支与跨模态注意力，推理开销大。已有加速手段多为通用扩散缓存（如 DeepCache 类特征复用）或步数蒸馏，但直接套用到音视频双模态时未区分两路模态的可恢复性差异，容易在视频侧造成运动与时序细节的持久损失。本文要解决的是：如何在保证视频细粒度精修的前提下，选择性缓存音频侧计算以实现免训练加速。

## 💡 核心创新

1. 发现音视频模态非对称可恢复性：音频漂移可被末段少量联合步修复，视频退化不可逆
2. 提出 sandwich 式三段计算分配：前段联合、中段缓存音频、末段恢复联合
3. 设计音频去噪器输出的收敛自适应缓存触发判据（进入 cache-tolerant regime 才缓存）
4. 中段跳过音频去噪与跨模态注意力的同时保持视频分支独立时空精修

## 🏗️ 模型架构

输入为音频与视频 latent（经各自 VAE 编码），主干为双流扩散去噪网络，每步执行模态专属去噪分支并通过跨模态注意力交互。CAVC 不改动权重，属 training-free 推理调度：先监测音频去噪器输出的收敛程度，判定进入 cache-tolerant regime 后，在中段 timestep 缓存并复用音频去噪输出，跳过音频分支与跨模态注意力计算，视频分支继续完整时空精修；末段恢复若干联合去噪步以削减累积跨模态漂移、改善同步。摘要未给出参数量。

## 📚 数据集

- 多个公开音视频生成 benchmark（评估，摘要未列具体名称）

## 📊 实验结果

摘要仅给出定性结论：在多个公开 benchmark 上实现 1.10–1.35x 墙钟加速，若干视觉动态与时序统计指标提升，音频保真度与音视频对齐保持竞争力。未披露具体指标数值、基线名称与消融细节，无法量化对比。

## 🎯 结论与影响

最强结论是音视频扩散的两路模态在缓存可恢复性上存在可利用的非对称性，据此可免训练获得 1.1–1.35x 加速且不显著损害音频质量与同步。该观测可能推动后续加速工作从“统一缓存”转向“模态差异化调度”，对音视频生成模型的部署成本有直接意义。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与基线，加速比上限仅 1.35x 偏保守；缓存触发判据的阈值敏感性、跨模型/跨采样器泛化性缺少说明；视觉动态指标“提升”的成因（是否仅因保留完整视频精修）未做消融；未报显存与延迟分解。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
