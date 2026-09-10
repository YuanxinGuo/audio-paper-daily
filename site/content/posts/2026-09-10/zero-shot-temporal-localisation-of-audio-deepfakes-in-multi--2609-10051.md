---
title: "Zero-Shot Temporal Localisation of Audio Deepfakes in Multi-Speaker Conversations"
date: 2026-09-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出多说话人对话中音频深度伪造的时序定位任务TDLMC，用免训练五阶段流水线包装冻结二分类检测器，实现片段级定位。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音伪造检测</span> <span class="tag-pill tag-pill-soft">#时序定位</span> <span class="tag-pill tag-pill-soft">#零样本</span> <span class="tag-pill tag-pill-soft">#多说话人对话</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.10051</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.10051" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.10051" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多说话人对话中音频深度伪造的时序定位任务TDLMC，用免训练五阶段流水线包装冻结二分类检测器，实现片段级定位。
</div>

## 👥 作者与机构

**Soumyadeep Roy** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音反欺骗/深度伪造检测的研究者与安全风控工程师阅读。建议重点看任务形式化定义与新增时序指标（t-IoU、t-DR、MS-DCF）一节，以及两阈值迟滞有限状态机解码器部分；实验表与校准集划分值得细读。若只关心检测精度可略读。

## 🌍 研究背景

语音克隆欺诈正从整段伪造转向“外科手术式注入”：真实对话中仅一两句被替换为合成语音。此前 SOTA 多为话语级二分类检测器（如基于 ASVspoof 系列训练的 AASIST、RawNet 等），每段只输出一个 real/fake 标签，无法报告合成语音位于何处。同时 EER、min-DCF 在文件同时含真假两类时定义失效。本文要解决的是：在无监督、无重训条件下，对多说话人对话中的伪造片段做时序定位。

## 💡 核心创新

1. 形式化 TDLMC 任务并提出适配的时序指标 t-IoU、t-DR、MS-DCF
2. 免训练五阶段流水线，直接包装冻结二分类检测器输出片段级结果
3. 两阈值迟滞有限状态机解码器，将噪声窗口分数转为连贯区间
4. 跨三个冻结检测器验证同一解码器，并做校准集选参的受控分析

## 🏗️ 模型架构

输入为多说话人对话音频，先做分段/滑窗得到窗口级片段，送入冻结的二元深度伪造检测器（backbone 可为 AASIST 类或 ASVspoof 5 强基线）获得每窗 real/fake 分数；随后经五阶段免训练流水线处理，核心是两阈值迟滞有限状态机解码器：高阈值进入伪造态、低阈值退出，抑制抖动生成连贯伪造区间；最后输出带时间边界的片段级定位结果。解码器常数在留出校准集上选取，无需任何重训。

## 📚 数据集

- ASVspoof 5（构造 180 段多说话人对话，评估）
- AMI（真实多说话人对话，评估误报率）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| temporal IoU | ASVspoof 5 构造对话 | 训练式定位器（同流水线） | **0.90** | +约0.04（本文免训练反而略低） |
| temporal detection rate | ASVspoof 5 构造对话 | — | **0.95** | — |
| MS-DCF | ASVspoof 5 构造对话 | — | **0.26** | — |
| false-alarm rate | 真实语音 / AMI | — | **<6% / <2%** | — |

在 180 段构造对话上，强 backbone 下 t-IoU 0.90、t-DR 0.95、MS-DCF 0.26；真实语音误报低于 6%，AMI 真实多说话人对话低于 2%。相同流水线下训练式定位器仅将 t-IoU 提升约 0.04，说明放弃监督代价有限。跨三个冻结检测器验证同一解码器，受控分析将残余误报归因于 backbone 域差而非解码器。

## 🎯 结论与影响

最强结论是：无需重训即可用冻结二分类检测器实现多说话人对话中的伪造时序定位，t-IoU 达 0.90，且监督带来的增益仅约 0.04。这为 TDLMC 提供了首个零样本基线与可复用 benchmark，后续研究可在此基础上比较监督/半监督方法。工业上意味着现有话语级检测器可低成本升级为可定位系统，利于取证与风控。

## ⚠️ 局限与未解决问题

对话为人工构造而非真实注入场景，180 段规模偏小；仅单作者、无开源链接；未报推理延迟与计算开销；训练式定位器对比仅一句带过，缺详细消融；误报归因于 backbone 域差但未给出跨域修复方案；指标定义与 EER 不可比的论证可再充分。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-10/">← 返回 2026-09-10 速递</a></div>
