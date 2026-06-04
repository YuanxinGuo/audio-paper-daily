---
title: "Masked Wavelet Scattering Transform Neural Field for Sound Field Reconstruction"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声场重建"]
summary: "提出基于掩蔽小波散射变换的神经场框架，用于声场重建，以HRTF上采样为验证任务。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声场重建</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#小波散射变换</span> <span class="tag-pill tag-pill-soft">#神经场</span> <span class="tag-pill tag-pill-soft">#HRTF上采样</span> <span class="tag-pill tag-pill-soft">#声学模拟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.04370</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.04370" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.04370" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于掩蔽小波散射变换的神经场框架，用于声场重建，以HRTF上采样为验证任务。
</div>

## 👥 作者与机构

**Xinmeng Luan** ¹ · Samuel A. Verburg · Efren Fernandez-Grande · Gary Scavone

**机构**：麦吉尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合声场重建、HRTF处理方向的研究者。可重点读§3方法部分和§4实验对比。建议关注WST掩蔽策略与神经场结合的有效性。

## 🌍 研究背景

声场重建旨在从稀疏观测恢复完整声场，在空间音频、HRTF个性化中重要。现有方法如线性插值、稀疏恢复精度有限，深度学习方法依赖大量数据。小波散射变换可提取多尺度统计特征，但直接用于重建易引入噪声。本文提出将WST作为先验约束，通过掩蔽策略保留信息性结构，解决稀疏观测下重建精度低的问题。

## 💡 核心创新

1. WST作为多尺度特征提取器嵌入神经场损失函数
2. 两阶段掩蔽策略：先学通用掩蔽，再用于个体HRTF
3. 在HRTF上采样任务上验证框架有效性

## 🏗️ 模型架构

输入稀疏观测声场（如少量HRTF角度）→ 神经场网络（隐式表示，MLP）输出连续声场。训练损失包含数据保真项和WST特征匹配项。WST系数经掩蔽处理：第一阶段从多受试者数据集学习二进制掩蔽，第二阶段将该掩蔽应用于个体HRTF的WST系数，保留统计结构。

## 📚 数据集

- 多受试者HRTF数据集（训练掩蔽，规模未提及）
- 个体HRTF数据集（评估上采样，规模未提及）

## 📊 实验结果

摘要未提供具体数值结果，仅提及与基线方法对比及消融实验验证了各组件有效性。需查阅全文获取定量指标。

## 🎯 结论与影响

本文提出基于掩蔽WST的神经场框架，通过多尺度统计先验提升稀疏观测下声场重建质量。HRTF上采样实验表明方法有效。未来可扩展至其他声场重建任务，为空间音频个性化提供新思路。

## ⚠️ 局限与未解决问题

仅以HRTF上采样作为概念验证，未在更广泛声场重建任务上验证；未报告计算复杂度或推理时间；掩蔽学习依赖多受试者数据，个体差异可能影响泛化。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-06-04/">← 返回 2026-06-04 速递</a></div>
