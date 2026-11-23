---
title: "Neural Defend Ranks #1 in Global Audio Deepfake Detection Benchmark - ARCAS on the Podonos Independent Leaderboard"
date: 2026-11-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "Neural Defend 的 ARCAS 基础模型在 Podonos 独立榜单上并列第一，优于多家商用检测器，并给出完整评测协议与五轮榜单历史。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">5.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频深伪检测</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#语音合成检测</span> <span class="tag-pill tag-pill-soft">#商业化系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.27215</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.27215" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.27215" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>Neural Defend 的 ARCAS 基础模型在 Podonos 独立榜单上并列第一，优于多家商用检测器，并给出完整评测协议与五轮榜单历史。
</div>

## 👥 作者与机构

**Sivashankar Selvarajan** ¹ · Piyush Verma · Sumit Singh

**机构**：Neural Defend

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频深伪检测、TTS/声音克隆鉴伪与基准评测的研究者与工程团队阅读。若关注方法细节可跳过，本文偏评测报告；建议先看榜单构造与协议一节、误差平衡与统计显著性分析，再看与十个公开基准的对照结论。

## 🌍 研究背景

AI 生成音频检测的商用系统通常只在厂商内部测试集上报结果，买家无法复核，横向比较缺乏可信依据。此前公开对比多依赖各团队自报数据，测试集与标签不统一，且 TTS 与声音克隆系统迭代快，旧基准易饱和。本文借助 Podonos 独立榜单，用私有标签与统一 held-out 集对 28 个系统（16 家厂商与主流开源模型）做可比评测，并报告 ARCAS 系列模型的表现。

## 💡 核心创新

1. 在 Podonos 私有标签独立榜单上系统评测 28 个检测系统
2. ARCAS 290M 与 90M 双规模模型共享第一且误差统计显著更低
3. 默认阈值下假阳/假阴保持平衡且不拒收任何提交文件
4. 给出五轮榜单历史与商用/开源检测器差距分析

## 🏗️ 模型架构

摘要未披露 ARCAS 的具体网络结构，仅说明其为 foundation model 形式的音频深伪检测器，提供 290M 与 90M 两种参数规模。输入为真实语音与当前 TTS/声音克隆系统生成的语音，覆盖六种文件格式；输出为真伪判别分数，在默认阈值下给出二分类判定。摘要未提及主干网络类型、输入特征（如 mel / wav2vec 表征）与训练数据构成，架构细节需查阅原文。

## 📚 数据集

- Podonos 独立榜单 held-out 集（评估，含真实语音与 TTS/声音克隆语音，六种文件格式）
- 十个公开基准完整测试集（评估，用于 ARCAS 290M 对照）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 榜单排名 | Podonos 榜单（2026-10-29 发布，28 系统） | Resemble AI / Hiya / Pindrop / Hive / Reality Defender 等商用系统 | **ARCAS 290M 与 ARCAS 90M 并列第一** | 排名领先全部商用系统 |

摘要给出的是排名与定性结论：ARCAS 两模型并列第一，错误数在统计上显著低于其他系统，默认阈值下假阳与假阴平衡，全部提交文件均被处理无拒收，并处于准确率—延迟前沿。摘要未给出具体错误率、EER 或 AUC 数值，也未列出消融实验；与十个公开基准的对照仅以“结论一致”描述，缺少可核对的数字。

## 🎯 结论与影响

最强结论是 ARCAS 在带私有标签的独立榜单上以统计显著优势领先全部商用与开源检测器。这为音频深伪检测提供了可复核的第三方评测范式，可能推动该方向从自报指标转向独立榜单比较；对工业落地而言，说明商用检测器选型应参考独立基准而非厂商内部测试集。

## ⚠️ 局限与未解决问题

本文为评测报告而非方法论文，ARCAS 的网络结构、训练数据与损失均未在摘要中说明，难以判断性能来源。榜单仅一个 held-out 集，格式与生成器覆盖有限；商用系统预测由厂商自行提交，存在提交策略差异；未报推理延迟具体数值与跨数据集泛化细节。

---

<div class="paper-footer"><span>评分：5.5</span><span>原始：5.5</span><a href="/audio-paper-daily/posts/2026-11-23/">← 返回 2026-11-23 速递</a></div>
