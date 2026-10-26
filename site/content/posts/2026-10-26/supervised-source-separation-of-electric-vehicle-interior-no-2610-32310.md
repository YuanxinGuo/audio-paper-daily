---
title: "Supervised Source Separation of Electric Vehicle Interior Noise Using a Hybrid Transformer Architecture"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学模拟"]
summary: "将电动车内噪声分解为四类源贡献，用混合Transformer做有监督双耳分离，并以工况信息条件化、物理参数化生成器合成训练数据。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学模拟</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#条件分离</span> <span class="tag-pill tag-pill-soft">#数据合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32310</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32310" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32310" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将电动车内噪声分解为四类源贡献，用混合Transformer做有监督双耳分离，并以工况信息条件化、物理参数化生成器合成训练数据。
</div>

## 👥 作者与机构

**Philipp Diel** ¹ · Zhuo Cao · Arne Hildenbrand · Marco G\"unther · Stefan Pischinger · Hanno Scharr · Steffen Marburg

**机构**：亚琛工业大学 · 于利希研究中心 · 德国航空航天中心

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做声学工程、传递路径分析、以及把语音分离方法迁移到非语音领域的读者。值得通读，重点看 §3 的条件化设计与 §4 的参数化数据生成器，以及合成/实测验证的对比表；若只关心分离网络本身，可略读架构细节。

## 🌍 研究背景

电动车内声是风噪、胎噪、动力总成（电驱与逆变器）噪声、辅驱噪声的叠加，其相对平衡决定总响度与主观音质。传统上分解这些贡献依赖传递路径分析（TPA），需大量测量campaign与专家经验，成本高。已有分离方法多针对语音/音乐，缺少面向技术系统多源、且带工况条件的方案。本文把该分解形式化为四目标源的有监督双耳分离问题，试图用数据驱动方式替代部分测量工作。

## 💡 核心创新

1. 把车内噪声分解建模为四源有监督双耳分离任务
2. 引入工况条件（电驱转速/负载、车速、辅驱转速）消歧源贡献
3. 改造音乐demixing的混合时域-频谱Transformer用于技术系统
4. 用物理参数化生成器合成带标签的分量声，规避实测stem成本

## 🏗️ 模型架构

输入为双耳车内录音（时域波形与频谱表示），主干沿用为音乐demixing设计的混合Transformer：时域分支与频谱分支并行，经Transformer块建模长程依赖后融合，输出四路目标源估计。关键改动是条件化：将电驱转速、电驱负载、车速、辅驱转速等工况信息编码后注入网络，用于区分频谱上重叠的源贡献。摘要未给出参数量与具体层数。

## 📚 数据集

- 物理参数化合成数据生成器（训练，随机虚拟整车硬件配置与驾驶场景）
- 合成车内声（评估）
- 实测车内声（评估）

## 📊 实验结果

摘要仅说明在合成与实测车内声上验证了分离性能，并强调方法用于技术系统声学贡献分析的可行性，未给出SI-SDR、PESQ等具体数值，也无与TPA或通用分离baseline的定量对比，因此无法列出结果表。

## 🎯 结论与影响

最强结论是：以工况条件化的混合Transformer加物理合成数据，可在合成与实测车内声上实现四类噪声贡献的分离，为技术系统声学贡献分析提供可行路径。对后续研究，提示了把语音/音乐分离范式迁移到工程声学、并以参数化仿真补足标签的方向；工业上可能降低TPA测量campaign的依赖。

## ⚠️ 局限与未解决问题

训练完全依赖参数化合成数据，合成到实测的域差距是核心隐忧；摘要未报告与TPA或通用分离baseline的定量对比，也缺少消融证明工况条件的必要性；未提推理延迟与实时性，实测验证规模不明。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
