---
title: "AV-QTSS: Class-Query Target Sound Spatialization in Multi-Source 360$^\\circ$ Videos"
date: 2026-10-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "给定单声道多源混合、360°视频与类别查询，定位并渲染出目标声源的FOA空间音频。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#视听定位</span> <span class="tag-pill tag-pill-soft">#一阶Ambisonics</span> <span class="tag-pill tag-pill-soft">#目标声提取</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.34401</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.34401" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.34401" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>给定单声道多源混合、360°视频与类别查询，定位并渲染出目标声源的FOA空间音频。
</div>

## 👥 作者与机构

**Qingyu Luo** ¹ · Peng Zhang · Wenwu Wang · Philip J. B. Jackson

**机构**：萨里大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频渲染、视听声源定位、Ambisonics 的研究者阅读。值得通读，重点看 §3 的 query-conditioned dense binding localizer 与联合优化渲染器设计，以及表 2 的 1~4 源定位/空间精度对比和消融；若只关心方法，可先看定位器与渲染器耦合那一节。

## 🌍 研究背景

360° 沉浸式媒体需要空间音频，现有视听空间化方法（如基于视频预测 Ambisonics 的工作）把整个场景当作一个整体渲染，无法单独控制某个声源。而单声道混合本身不含空间线索，方向必须从视频推断，且画面中常有多个同时发声的物体，类别查询下的目标定位与渲染因此困难。本文要解决的是：在多源 360° 视频中按类别查询单独生成目标声源的 FOA 信号。

## 💡 核心创新

1. 提出 AV-QTSS 新任务：类别查询驱动的目标声源空间化
2. query-conditioned dense binding localizer 预测全场景球面概率图
3. 定位器与 FOA 渲染器端到端联合优化
4. 支持 1~4 个并发声源并迁移到真实 360° 录音

## 🏗️ 模型架构

输入为单声道多源混合音频、360° 视频帧与 13 类 DCASE 声事件本体中的类别查询。视觉分支提取全景特征，与类别查询做稠密绑定，输出覆盖整个球面的概率图作为声源方向后验；该空间概率图与音频特征耦合送入 FOA 渲染器，生成仅含被查询声源的一阶 Ambisonics 信号。定位器与渲染器联合优化，使定位监督与空间音频重建目标互相约束。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- DCASE 声事件本体 13 类（类别查询定义）
- 合成多源 360° 视频数据（1~4 并发源，训练/评估）
- 真实 360° 录音（适配后迁移评估）

## 📊 实验结果

摘要仅定性说明：在 1~4 个并发声源设置下，定位精度与空间音频准确度均优于已有方法与消融变体；定位器经适配后可迁移到真实 360° 录音。未给出 SI-SDR、定位误差角或 FOA 重建等具体数值，也无效率指标。

## 🎯 结论与影响

最强结论是类别查询可在无显式空间线索的单声道混合上，借助 360° 视频实现单源 FOA 空间化。这为可控沉浸式音频渲染开辟了按需分离并定位声源的新范式，对 VR/360° 内容制作中后期单独调整某类声源有直接落地价值。

## ⚠️ 局限与未解决问题

摘要缺具体量化指标与消融细节，难以判断相对基线的实际增益；类别粒度受限于 13 类本体，同类多实例并发时如何区分未说明；真实录音仅做适配后迁移，泛化程度与推理延迟均未报告。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-27/">← 返回 2026-10-27 速递</a></div>
