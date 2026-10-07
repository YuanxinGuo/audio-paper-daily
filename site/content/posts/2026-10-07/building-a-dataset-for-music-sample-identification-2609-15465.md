---
title: "Building a Dataset for Music Sample Identification"
date: 2026-10-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐信息检索"]
summary: "从音乐数据库挖掘采样标注，构建比现有基准大近三个数量级的样本识别数据集，并用图连通分量分割避免泄漏。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐信息检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#音乐样本识别</span> <span class="tag-pill tag-pill-soft">#数据泄漏</span> <span class="tag-pill tag-pill-soft">#图分割</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.15465</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.15465" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.15465" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>从音乐数据库挖掘采样标注，构建比现有基准大近三个数量级的样本识别数据集，并用图连通分量分割避免泄漏。
</div>

## 👥 作者与机构

**R. Oguz Araz** ¹ · Xavier Lizarraga · Xavier Serra · Dmitry Bogdanov

**机构**：庞培法布拉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐信息检索、采样识别、音频指纹与版权检测的研究者阅读。值得通读，重点看 §3 数据挖掘与标注流程、§4 图构建与连通分量分割策略，以及泄漏感知的裁剪方法。可先看表 1 的数据规模对比与图 2 的组件分布，再决定是否复现其分割管线。

## 🌍 研究背景

样本识别（SI）指将音乐作品中的元素与其被采样、变换后用于新作品的版本进行匹配，与音频指纹、翻唱识别、版权检测相关。此前该任务关注度低，公开数据稀缺，现有 SI 基准规模很小，难以支撑深度模型训练。同时，直接按标注随机划分训练/测试集会把同一音轨放入不同集合，造成数据泄漏，虚高评估结果。本文要解决的核心问题是：构建大规模公开 SI 数据集，并设计泄漏感知的划分流程。

## 💡 核心创新

1. 从音乐数据库挖掘采样标注，构建约 13 万轨的大规模 SI 数据集
2. 用图建模标注关系，按连通分量划分以避免同轨跨集泄漏
3. 发现单个巨型连通分量占半数标注，提出裁剪策略实现平衡划分
4. 公开数据分析与划分代码，支持非商业科研复用

## 🏗️ 模型架构

本文为数据集与流程工作，非端到端神经网络。流程为：输入为音乐数据库中的采样标注（被采样曲目与采样曲目对）→ 构建以曲目为节点、采样关系为边的无向图 → 计算连通分量 → 发现单一巨型分量包含约一半标注 → 对该分量进行裁剪（trim）以打破过大组件 → 在剩余连通分量上按组件划分训练/验证/测试集，得到 114k / 6k / 10k 轨。输出为泄漏感知的数据集划分与公开代码。

## 📚 数据集

- 自建音乐采样识别数据集（训练 114k 轨、验证 6k 轨、测试 10k 轨，用于训练与评估）
- 现有 SI 基准（用于规模对比，具体名称摘要未给出）

## 📊 实验结果

摘要未给出 SI-SDR、PESQ、WER、MOS 等模型性能指标，也未报告基线方法的定量结果。主要定量信息为数据集规模：训练 114k、验证 6k、测试 10k 轨，比现有 SI 基准大近三个数量级；并指出单一巨型连通分量包含约一半标注。作者未在摘要中提供模型训练或识别准确率实验。

## 🎯 结论与影响

本文最强结论是：通过图连通分量划分并裁剪巨型分量，可构建规模近三个数量级于现有基准且泄漏感知的 SI 数据集。该工作为样本识别提供了数据基础，可能推动音频指纹、采样检测与版权溯源方向的研究。工业上可用于音乐版权检测、采样溯源与内容审核，但需注意其非商业科研用途限制。

## ⚠️ 局限与未解决问题

摘要未报告任何模型性能实验，数据集的实际可用性与难度未知；仅从单一音乐数据库挖掘标注，存在来源偏差与标注噪声；裁剪巨型分量可能丢失部分真实采样关系；未说明数据规模扩大后对训练效率与推理延迟的影响；缺乏与现有 SI 基准在模型层面的对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-07/">← 返回 2026-10-07 速递</a></div>
