---
title: "HC-AINet: An Auditory-Inspired Network with Harmonic Compensation for Low-Complexity Speech Enhancement"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出谐波补偿的听觉启发网络 HC-AINet，用 ERB 子带与谐波增益分支在 0.27M 参数下于 VoiceBank-DEMAND 取得 PESQ 3.20。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#低复杂度模型</span> <span class="tag-pill tag-pill-soft">#听觉感知滤波</span> <span class="tag-pill tag-pill-soft">#相位估计</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.30818</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.30818" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.30818" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出谐波补偿的听觉启发网络 HC-AINet，用 ERB 子带与谐波增益分支在 0.27M 参数下于 VoiceBank-DEMAND 取得 PESQ 3.20。
</div>

## 👥 作者与机构

**Nan Li** ¹ · Xiaoxiong Wu · Huawei Liu · Ziping Zhao

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做低复杂度语音增强与端侧部署的研究者与工程师阅读。建议通读，重点看 §3 中谐波位置图与谐波/全局增益融合机制，以及表 2 的参数量-PESQ 权衡对比；若关注相位重建，细读紧凑相位估计器部分。

## 🌍 研究背景

VoiceBank-DEMAND 上 PESQ 已从早期 CNN/LSTM 提升到 MetricGAN+、SEGAN 等生成式方法，但参数量与算力开销大，难以部署到耳机、助听器等资源受限设备。听觉启发子带方法（如 ERB 滤波器组）能显著降算力，但其平滑增益难以区分谐波峰与邻近噪声，导致音质细节丢失。本文要在极低参数量约束下同时保持噪声抑制与谐波结构保真。

## 💡 核心创新

1. 三角 ERB 滤波器组提供紧凑子带特征，降低前端算力
2. 谐波位置图约束谐波增益仅在选定频点生效
3. 全局增益与谐波增益并行预测并学习融合权重
4. 幅度导出的最小相位线索联合条件化紧凑相位估计器

## 🏗️ 模型架构

输入为含噪语音波形，经三角等效矩形带宽（ERB）滤波器组得到 64 子带紧凑特征；主干为轻量网络，由 inverted-residual 单元、时序 Conformer 层与并行频率门控卷积组成，分别建模通道、时序与频带依赖。网络输出全局增益、谐波增益及二者融合权重；谐波位置图由含噪频谱导出，将谐波贡献限制在原始频率网格的选定 bin 上，全局分支控制整体谱包络。补偿后的幅度、含噪相位与幅度导出的最小相位线索共同条件化紧凑相位估计器，最终重建波形。全模型约 0.27M 参数。

## 📚 数据集

- VoiceBank-DEMAND（评估，含 PESQ/STOI 指标）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| PESQ | VoiceBank-DEMAND | 摘要未给出具体基线值 | **3.20** | 摘要未给出 |
| STOI | VoiceBank-DEMAND | 摘要未给出具体基线值 | **0.95** | 摘要未给出 |
| 参数量 | VoiceBank-DEMAND | 摘要未给出具体基线值 | **约 0.27M** | 摘要未给出 |

摘要仅报告 64 带模型在 VoiceBank-DEMAND 上 PESQ 3.20、STOI 0.95、参数量约 0.27M，未给出与具体基线（如 MetricGAN+、SEGAN、DPCRN）的逐项对比数值，也未提供消融实验、推理延迟或跨数据集泛化结果，因此改进幅度无法从摘要直接量化。

## 🎯 结论与影响

最强结论是：在约 0.27M 参数的极低复杂度下，谐波补偿的听觉启发子带结构仍能达到 PESQ 3.20 的增强质量。这为端侧语音增强提供了可参考的谐波保真设计范式，后续工作可沿谐波位置建模与轻量相位估计两条线继续推进，对耳机、助听器芯片落地有直接意义。

## ⚠️ 局限与未解决问题

摘要未给出与主流低复杂度基线（DPCRN、FRCRN、GaGNet 等）的逐项数值对比，缺少消融验证谐波分支与相位估计器各自贡献；仅在 VoiceBank-DEMAND 单一合成数据集评估，真实噪声与混响泛化未知；未报告推理延迟、MACs 与内存占用等端侧关键指标。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
