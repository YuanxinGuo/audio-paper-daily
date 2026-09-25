---
title: "DAMSEP: Distance-Aware Monaural Source Separation using Multi-RIR Estimation"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "DAMSEP 首次端到端联合做单通道语音分离与多源 RIR 估计，用 RIR 的 DRR 推断声源远近顺序，并发布 HETMIXR 数据集。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#房间冲激响应生成</span> <span class="tag-pill tag-pill-soft">#声学模拟</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.29749</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/Wenanzhi/DAMSEP" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">Wenanzhi/DAMSEP</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.29749" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.29749" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/Wenanzhi/DAMSEP" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>DAMSEP 首次端到端联合做单通道语音分离与多源 RIR 估计，用 RIR 的 DRR 推断声源远近顺序，并发布 HETMIXR 数据集。
</div>

## 👥 作者与机构

**Wen Wen** ¹ · Qiang Zhou · Yu Xi · Haoyu Li · Bohan Li · Kai Yu

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做单通道分离、RIR 估计与空间线索建模的研究者。建议通读，重点看 §3 的共享去混响与 RIR 估计模块设计、联合损失构成，以及 HETMIXR 构建流程与消融实验；若只关心分离性能，可先看分离指标表与消融表。

## 🌍 研究背景

单通道语音分离此前以 Conv-TasNet、DPRNN、SepFormer 等时域/Transformer 方法为主，目标只是恢复干净内容，忽略 RIR 中蕴含的声源距离线索。RIR 估计方向则多依赖多通道阵列或单独建模，与分离割裂。本文要解决的是：在单麦克风混合下，同时分离多个声源并估计各自的复数卷积传递函数，从而恢复相对远近顺序这一空间信息。

## 💡 核心创新

1. 首个端到端联合训练的单通道分离 + 多源 RIR 估计框架 DAMSEP
2. 共享去混响与 RIR 估计模块，联合源估计与混响重建目标
3. 用估计 RIR 的 DRR 推断声源相对近/远排序
4. 发布含源级 RIR 与几何距离标注的 HETMIXR 数据集

## 🏗️ 模型架构

输入为单通道混合语音波形，经分离主干网络得到各源估计；主干与共享去混响模块、RIR 估计模块耦合，后者输出每个源的复数卷积传递函数。训练同时优化源估计损失与混响重建损失，使分离与 RIR 估计互相约束。最终由估计 RIR 计算 DRR，得到源间相对远近排序。摘要未给出具体参数量与主干网络名。

## 📚 数据集

- HETMIXR（训练与评估，含异构源内容、多样模拟房间、源级 RIR 与几何距离标注）
- 未见房间实测 RIR 生成的混合（评估，泛化测试）
- 单说话人输入（评估，泛化测试）

## 📊 实验结果

摘要仅给出定性结论：在 HETMIXR 上，源分离、RIR 估计与距离排序三项任务均优于对比方法；消融显示源监督与混响重建目标互补；额外实验表明可泛化到单说话人输入及未见房间实测 RIR 生成的混合。摘要未提供 SI-SDR、PESQ 等具体数值，无法列表。

## 🎯 结论与影响

最强结论是单通道分离可同时输出源级 RIR 并据此恢复相对距离排序，把空间信息重新引入单麦分离。该思路可能推动分离与房间声学联合建模的后续研究，并为需要距离感知的语音前端（如远场交互、会议拾音）提供新线索。

## ⚠️ 局限与未解决问题

摘要未报推理延迟与模型规模，缺少与多通道 RIR 估计方法的对比；HETMIXR 以模拟 RIR 为主，实测泛化仅一例；距离排序只给相对近/远，未验证绝对距离精度；消融细节与失败案例分析在摘要中不可见。

## 🔗 开源资源

- **代码**：<https://github.com/Wenanzhi/DAMSEP>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-25/">← 返回 2026-09-25 速递</a></div>
