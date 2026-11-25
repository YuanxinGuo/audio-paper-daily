---
title: "SynAVID: A Synthetic Audio-Visual Immersive Dataset of Dynamic Scenes"
date: 2026-11-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出SynAVID合成视听沉浸数据集，含8个室内外场景，提供视角相关的双耳音频与配对参考，用于视觉重建、双耳音频重建与视听编辑评测。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#视听合成</span> <span class="tag-pill tag-pill-soft">#声学模拟</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.32311</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-24</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://avery-xu.github.io/synavid-project/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">avery-xu.github.io/synavid-project/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.32311" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.32311" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://avery-xu.github.io/synavid-project/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出SynAVID合成视听沉浸数据集，含8个室内外场景，提供视角相关的双耳音频与配对参考，用于视觉重建、双耳音频重建与视听编辑评测。
</div>

## 👥 作者与机构

**Jun Xu** ¹ · Sujing Li · Chunhao Bi · Zhengxue Cheng · Ronghua Wu · Qunshan Gu · Li Song

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做双耳音频合成、视听联合建模与沉浸式场景重建的研究者阅读。值得通读，重点看 §3 数据生成管线（几何感知声学合成如何与视觉渲染共享场景动态）与 §4 评测协议；若只关心双耳音频，先看音频重建实验与表 2 的 spectral/interaural/perceptual 三类指标对比。

## 🌍 研究背景

沉浸式场景建模需要视角变化与场景条件变化下同步的视听观测及参考，但真实采集难以获得受控变化的配对参考。现有双耳音频数据集多为静态听者或缺乏与视觉几何严格对齐的声学合成，视听编辑评测也缺少成对目标参考。本文构建合成数据集，用共享场景动态、声源事件与观察者位姿同时驱动视觉渲染与几何感知声学合成，以支持可控变化下的重建与编辑评测。

## 💡 核心创新

1. 共享场景动态驱动视觉渲染与几何感知双耳声学合成
2. 固定相机阵列与移动轨迹结合的分钟级episode设计
3. 提供几何与实例标注及配对参考用于编辑评测
4. 受控几何变化产生听者相关的声学响应

## 🏗️ 模型架构

数据生成管线而非单一网络：以场景几何、声源事件与观察者位姿为共享输入，视觉侧用固定相机阵列与移动轨迹渲染多视角图像；声学侧基于场景几何做几何感知合成，输出随视角变化的双耳音频。每条分钟级episode同步视觉与音频观测，并附几何、实例标注与配对参考。摘要未给出具体网络结构与参数量，评测部分对现有视觉重建、双耳音频重建与视听编辑方法进行基准测试。

## 📚 数据集

- SynAVID（自建合成数据集，8个室内外场景，用于训练与评估）

## 📊 实验结果

摘要未给出具体数值指标，仅给出定性结论：混合观测配置在固定与移动测试视角上普遍改善视觉重建，但瞬态占用与稀疏观测区域仍具挑战；不同方法在频谱、双耳间与感知音频指标上的排序不一致；几何与实例标注揭示观测支持不均与局部高斯表示问题；受控几何变化产生听者相关的声学响应。

## 🎯 结论与影响

最强结论是共享场景动态驱动的合成管线能提供视角相关双耳音频与配对参考，支撑可控条件下的重建与编辑评测。对双耳音频与视听联合建模方向，提供了可复现的基准与诊断性标注；工业上可用于沉浸式内容生成与音频渲染算法的受控评测，但合成到真实的迁移仍需验证。

## ⚠️ 局限与未解决问题

全合成数据存在与真实录音的域差距，摘要未报告推理延迟或计算成本；评测仅覆盖现有方法，缺少与真实采集数据集的交叉验证；音频指标排序不一致说明单一聚合分数不足，但未给出统一评价建议。

## 🔗 开源资源

- **项目主页**：<https://avery-xu.github.io/synavid-project/>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-25/">← 返回 2026-11-25 速递</a></div>
