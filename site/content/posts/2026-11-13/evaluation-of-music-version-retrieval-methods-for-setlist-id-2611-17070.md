---
title: "Evaluation of Music Version Retrieval Methods for Setlist Identification in Live Concerts"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐版本检索"]
summary: "在 ASID 基准上评测 Re-MOVE、CLEWS 与自研 NAVE 三种音乐版本检索方法用于演唱会歌单识别，NAVE 以 256 维嵌入取得最佳检索性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐版本检索</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#音频嵌入</span> <span class="tag-pill tag-pill-soft">#现场演出</span> <span class="tag-pill tag-pill-soft">#基准评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.17070</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.17070" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.17070" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在 ASID 基准上评测 Re-MOVE、CLEWS 与自研 NAVE 三种音乐版本检索方法用于演唱会歌单识别，NAVE 以 256 维嵌入取得最佳检索性能。
</div>

## 👥 作者与机构

**Andres Ferraro** ¹ · Albin Correya

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐信息检索、音频嵌入与大规模检索系统的研究者与工程团队阅读。若关注现场录音鲁棒匹配，建议通读；重点看 §3 的 NAVE 嵌入模型设计、§4 的 ASID 评测协议与结果表，以及音乐/非音乐门控的消融部分。可先看结果表与定性分析图，再回看方法细节。

## 🌍 研究背景

音乐版本检索（version identification）此前以 Re-MOVE 等基于 2D 傅里叶变换特征与和声匹配的方法为代表，在翻唱识别上表现稳定。但现场演唱会录音存在编曲差异大、背景噪声强、需对长时连续音频高效处理等问题，传统方法难以规模化。本文以 ASID 歌单识别基准为场景，系统比较经典方法与神经嵌入方法，并考察紧凑嵌入与音乐门控预处理能否在真实现场条件下兼顾精度与存储/服务成本。

## 💡 核心创新

1. 将 CLEWS 与自研 NAVE 神经音频版本嵌入引入 ASID 歌单识别任务
2. NAVE 仅用 256 维嵌入，较 CLEWS 的 1024 维存储降低四倍且检索更优
3. 系统评估音乐/非音乐门控对检测与时序覆盖的影响
4. 定性分析揭示门控可改善识别边界，超出标准 ASID 指标所反映的范围

## 🏗️ 模型架构

输入为现场演唱会连续录音与参考曲库音频，均切分为片段级音频后提取特征。对比三条路线：Re-MOVE 采用传统 2D 傅里叶变换特征与和声匹配；CLEWS 为基于神经网络的音频版本嵌入模型，输出 1024 维嵌入；NAVE 为内部神经音频版本嵌入模型，输出 256 维嵌入。检索阶段以片段级嵌入在参考曲库中做相似度匹配，得到歌曲命中与时序定位。另加音乐/非音乐门控模块作为预处理，过滤非音乐片段以改善检测与时序覆盖。摘要未给出参数量与主干网络细节。

## 📚 数据集

- ASID 基准（评估，现场演唱会录音与参考曲库匹配）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 检索性能（ASID 基准指标） | ASID | Re-MOVE | **NAVE / CLEWS 显著更优（摘要未给具体数值）** | 显著提升（未给具体数值） |

摘要仅给出定性结论：NAVE 与 CLEWS 显著优于 Re-MOVE；NAVE 以 256 维嵌入在存储降低四倍的情况下取得更好检索性能。音乐/非音乐门控带来检测与时序覆盖的适度提升，定性分析显示其可改善识别边界。摘要未报告具体指标数值、消融规模与推理延迟，需查阅正文表格确认。

## 🎯 结论与影响

本文最强结论是片段级神经音频嵌入可作为可扩展歌单识别的强基础，紧凑 256 维表示即可在真实现场条件下取得高精度并大幅降低存储与服务成本。这为后续现场音乐检索与大规模曲库匹配研究提供了明确基线选择，也提示工业部署可优先考虑低维嵌入方案。

## ⚠️ 局限与未解决问题

工作以评测为主，方法创新有限；仅在 ASID 单一基准上验证，跨数据集泛化未知；摘要未给具体指标数值与统计显著性，门控改进幅度被描述为 modest；未报告推理延迟与大规模服务实测成本；与更多版本检索基线（如基于 CQT/和声的方法）对比不足。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
