---
title: "AcousticAgent: A Floorplan-Centric Simulation Platform for Distributed Multi-Room Speech Processing"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学模拟"]
summary: "提出以户型图为中心的多房间声学仿真平台，生成多通道RIR并构建FP-RIR数据集，验证分布式麦克风对远场语音处理的价值。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学模拟</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#房间冲激响应生成</span> <span class="tag-pill tag-pill-soft">#多房间声学</span> <span class="tag-pill tag-pill-soft">#分布式麦克风</span> <span class="tag-pill tag-pill-soft">#语音增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.22936</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.22936" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.22936" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出以户型图为中心的多房间声学仿真平台，生成多通道RIR并构建FP-RIR数据集，验证分布式麦克风对远场语音处理的价值。
</div>

## 👥 作者与机构

**Zhiqi Ai** ¹ · Han Cheng · Shiyi Mu · Yongjin Zhou · Shugong Xu

**机构**：上海大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做RIR仿真、分布式麦克风阵列、远场语音增强与声源定位的研究者与工程团队阅读。建议重点看§3的混合几何-声学求解器与户型图感知建模，以及§5的声学保真度验证与分布式处理实验；数据集构建细节可快速浏览。若关注语音增强算法本身，本文价值有限，可只看实验对比部分。

## 🌍 研究背景

现有声学仿真工具分两类：一类在参数化房间中高效生成RIR（如image-source方法），但难以扩展到大量可编辑的住宅多房间场景；另一类依赖预先构建的三维场景，构建成本高、不可批量生成。真实住宅多房间数据稀缺，导致远场语音增强、分布式麦克风处理等研究缺乏大规模、可控、声学连通的评测资源。本文要解决的是如何从结构化户型图自动构建可编辑、声学连通的多房间场景并批量生成多通道RIR。

## 💡 核心创新

1. 以户型图为中心，联合建模房间几何、连通性、家具与材质
2. 面向场景的声学材质数据库，语义元素映射到声学参数
3. 户型图感知的混合几何-声学求解器生成多通道RIR
4. 支持方向性/移动声源与分布式麦克风配置
5. VLM辅助从户型图图像与文本构建场景

## 🏗️ 模型架构

输入为结构化户型图（含房间多边形、门窗连通关系）及可选文本描述；VLM模块解析户型图图像与文本，生成场景语义标注；声学材质数据库将家具、墙面等语义元素映射为吸声/散射系数；核心为户型图感知的混合几何-声学求解器，结合几何声学（镜像源/射线追踪）与波动声学处理低频，跨房间传播考虑门窗连通与衍射，输出多通道RIR及混响音频；支持方向性与移动声源轨迹、分布式麦克风阵列配置。摘要未给出参数量。

## 📚 数据集

- FP-RIR（自建，15,376个住宅户型图，用于训练/评估仿真与下游任务）
- 真实房间实测数据（用于声学保真度验证）

## 📊 实验结果

摘要未给出具体指标数值，仅说明在真实测量数据上验证了声学保真度，并在单设备与分布式麦克风设置下评估了全屋声源定位、语音增强与远场语音处理，结果表明户型图感知建模有效、分布式空间处理在多房间环境中有收益。缺少SI-SDR、PESQ、定位误差等定量结果，无法判断提升幅度。

## 🎯 结论与影响

最强结论是户型图感知建模可支撑大规模住宅多房间声学仿真，且分布式麦克风在多房间远场处理中优于单设备。该平台与FP-RIR为远场语音、分布式阵列研究提供了可扩展评测资源，对智能家居多设备语音交互的仿真验证有落地价值。

## ⚠️ 局限与未解决问题

摘要未报告任何定量指标与消融，声学保真度验证的误差范围不明；混合求解器在高频/复杂连通结构下的精度与计算开销未讨论；FP-RIR仅覆盖住宅户型，材质与家具分布可能存在偏置；下游语音增强实验缺少与主流RIR数据集（如DNS-Challenge）的横向对比。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
