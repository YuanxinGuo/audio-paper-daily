---
title: "MS-Bench: A Condition-Stratified Multi-Speaker ASR Benchmark"
date: 2026-10-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出按说话人数、重叠率、相似度、轮次间隔、声学质量五维分层的多说话人ASR基准MS-Bench，揭示聚合指标掩盖的失败模式。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多说话人ASR</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#语音大模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.25824</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://aslp-lab.github.io/MS-Bench/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">aslp-lab.github.io/MS-Bench/</span></span></a><a class="oc-chip oc-chip-demo" href="https://aslp-lab.github.io/MS-Bench/" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">aslp-lab.github.io/MS-Bench/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.25824" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.25824" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://aslp-lab.github.io/MS-Bench/" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://aslp-lab.github.io/MS-Bench/" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出按说话人数、重叠率、相似度、轮次间隔、声学质量五维分层的多说话人ASR基准MS-Bench，揭示聚合指标掩盖的失败模式。
</div>

## 👥 作者与机构

**Chunjiang He** ¹ · Zheng Zi · Bingshen Mu · Yurun Li · Jingyi Wang · Zhonghua Fu · Lei Xie ✉

**机构**：西北工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多说话人ASR、说话人日志与语音大模型评测的研究者与工程团队阅读。建议通读，重点看五维条件分层的定义（§3）与分层结果分析（§4 及主表），并对照其公开 demo 页确认各系统在重叠率与说话人相似度上的差异；若只关心建模方法可略读实验细节。

## 🌍 研究背景

多说话人ASR随端到端语音大模型快速进步，但现有基准（如 LibriMix、AMI、AliMeeting 派生评测）通常只覆盖有限的重叠率、说话人数与场景，难以定位系统在何种条件下失效。已有工作多用整体 WER 或 cpWER 汇总，掩盖了重叠、说话人相似度、轮次间隔、声学质量等因素的差异化影响。本文要解决的是评测粒度不足的问题，构建条件分层的多说话人ASR基准以暴露条件相关的失败模式。

## 💡 核心创新

1. 提出五维条件分层：说话人数、重叠率、说话人相似度、轮次间隔、声学质量
2. 整合公开与内部基准，覆盖多场景、多语言、多录音设备
3. 同时评测词法识别、说话人归属与时间预测三类指标
4. 系统对比商用、开源与级联系统，定位条件相关失效

## 🏗️ 模型架构

本文为基准与评测研究，非单一模型架构。流程为：整合公开与内部多说话人录音 → 对每条录音在五个维度上打标（说话人数、重叠率、说话人相似度、轮次间隔、声学质量）→ 将各维度划分为条件区间并分层 → 在分层子集上统一评测代表性系统。被评测系统包括商用API、开源端到端语音大模型与级联（分离/日志+ASR）系统，指标覆盖词法识别、说话人归属与时间预测。摘要未给出参数量与具体主干网络。

## 📚 数据集

- MS-Bench（整合公开与内部多说话人数据，用于分层评测）
- 公开多说话人基准（作为MS-Bench组成部分，具体名称摘要未列）
- 内部多说话人录音（补充场景与设备覆盖，规模摘要未给）

## 📊 实验结果

摘要未给出具体数值结果，仅给出定性结论：重叠率同时影响词法识别与说话人归属；说话人相似度、轮次间隔、声学质量等因素呈现任务特定影响，分别作用于识别、归属或时间预测。作者据此论证聚合指标会掩盖重要失败模式，强调条件分层评测的必要性。

## 🎯 结论与影响

最强结论是：单一聚合指标会系统性掩盖多说话人ASR的条件相关失效，重叠率是同时损害识别与说话人归属的关键因素。该工作有望推动后续多说话人ASR研究按条件报告结果，并为工业系统选型与瓶颈定位提供细粒度诊断工具。

## ⚠️ 局限与未解决问题

作为基准论文，缺少对分层阈值敏感性的消融；内部数据未公开可能影响可复现性；未报告各系统推理延迟与算力开销；被评测系统清单与分层样本量在摘要中不明确，跨语言与设备维度的覆盖均衡性有待正文核实。

## 🔗 开源资源

- **项目主页**：<https://aslp-lab.github.io/MS-Bench/>
- **Demo / 试听**：<https://aslp-lab.github.io/MS-Bench/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-20/">← 返回 2026-10-20 速递</a></div>
