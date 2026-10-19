---
title: "SEA-HELM Audio: Evaluating Multilingual ASR-LLM Pipeline Performance Across SEA-HELM Subsets"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出 SEA-HELM Audio 基准，用合成语音评测东南亚多语言 ASR-LLM 级联管线，量化语音与文本输入间的性能落差。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多语言ASR</span> <span class="tag-pill tag-pill-soft">#ASR-LLM级联</span> <span class="tag-pill tag-pill-soft">#评测基准</span> <span class="tag-pill tag-pill-soft">#语音理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.19869</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.19869" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.19869" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 SEA-HELM Audio 基准，用合成语音评测东南亚多语言 ASR-LLM 级联管线，量化语音与文本输入间的性能落差。
</div>

## 👥 作者与机构

**Aulia Adila** ¹ · Yixian Tan · Jonathan Heng · Kunat Pipatanakul · Donghang Wu · Anocha Sutaveephamochanon

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多语言语音助手、ASR-LLM 级联系统评测的工程与研究同学阅读。值得通读，但重点看评测协议设计与各语言 speech gap 结果表，而非方法创新。可先看任务定义与 Tamil 退化分析两节，再对照自身管线做同类压力测试。

## 🌍 研究背景

现有语音助手多采用 ASR 级联 LLM 的管线，但主流评测仍以文本基准（如 SEA-HELM）为主，无法反映语音输入带来的误差累积。此前多语言语音评测多聚焦 WER 等识别指标，缺少对下游推理与指令遵循能力的端到端衡量，尤其东南亚低资源语言缺乏系统对比。本文要回答：文本基准上的表现能否预测语音输入下的可靠性，以及各语言退化程度差异。

## 💡 核心创新

1. 将文本基准 SEA-HELM 扩展为语音输入版本
2. 定义 speech gap 量化语音与文本准确率差
3. 覆盖五种语言的多选题与指令遵循双任务
4. 统一 verifier 对比开源与商用 ASR-LLM

## 🏗️ 模型架构

评测框架而非新模型：输入为合成语音，先经 ASR 系统转写为文本，再送入 LLM 完成多选题推理与指令遵循任务；文本输入路径直接喂原始文本作为对照。两条路径使用相同 verifier 判分，以文本准确率减语音准确率得到 speech gap。摘要未给出具体 ASR 与 LLM 主干网络名称及参数量。

## 📚 数据集

- SEA-HELM 文本基准（扩展为语音版本，评估）
- 合成语音数据（由文本基准合成，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率下降（多选题推理） | SEA-HELM Audio 五语言 | 文本输入准确率 | **语音输入准确率** | -9.00 至 -18.50 个百分点 |
| 准确率下降（指令遵循） | SEA-HELM Audio 五语言 | 文本输入准确率 | **语音输入准确率** | -20.00 至 -42.86 个百分点 |
| 准确率下降（Tamil） | SEA-HELM Audio | 文本输入准确率 | **语音输入准确率** | 超过 -40 个百分点 |

摘要给出主要结论：多选题推理退化 9.00–18.50 个百分点，指令遵循退化 20.00–42.86 个百分点，Tamil 退化最大超过 40 点。未报告各 ASR-LLM 系统的逐项数值、消融或推理延迟，也未区分退化来自 ASR 识别错误还是 LLM 对转写噪声的鲁棒性。

## 🎯 结论与影响

最强结论是文本基准无法预测语音输入下语音助手的可靠性，语音链路存在显著且语言相关的性能落差。这提示后续多语言语音助手研究需以语音端到端评测为准，工业落地时应针对高退化语言单独优化 ASR 与纠错环节。

## ⚠️ 局限与未解决问题

仅使用合成语音，未验证真实录音与口音、噪声、信道差异下的表现；未拆解退化来源（ASR 错误率 vs LLM 鲁棒性）；未报告延迟与成本；语言仅五种，东南亚其他低资源语言缺失；对比系统细节披露不足。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
