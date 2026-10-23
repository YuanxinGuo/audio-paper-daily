---
title: "Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "构建尼泊尔语-英语语码转换播客基准，用TTS合成数据SFT加GRPO做合成到真实域适配。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语码转换</span> <span class="tag-pill tag-pill-soft">#合成数据</span> <span class="tag-pill tag-pill-soft">#GRPO</span> <span class="tag-pill tag-pill-soft">#低资源语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.30860</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.30860" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.30860" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>构建尼泊尔语-英语语码转换播客基准，用TTS合成数据SFT加GRPO做合成到真实域适配。
</div>

## 👥 作者与机构

**Firoj Paudel** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做低资源/语码转换ASR与合成数据适配的研究者阅读。建议通读，重点看§3数据构建与去泄漏审计流程、§4两阶段框架、表2的MER/SPER对比，以及GRPO消融（script reward近零方差）这一负结果，它比正结果更有信息量。

## 🌍 研究背景

尼泊尔语-英语语码转换口语ASR的核心痛点是书写系统混淆（Devanagari与拉丁字母混写）和切换点错误率高。此前多语言基础模型（如Whisper类）在低资源语码转换上MER偏高，而监督微调依赖昂贵的人工语码转换语音标注。本文要解决的是：在真实语码转换数据稀缺条件下，如何用少量合成语音把多语言模型适配到自发的尼泊尔语-英语播客语音上。

## 💡 核心创新

1. 多说话人双引擎TTS合成0.95h语码转换语音做SFT
2. 两阶段合成到真实适配：SFT + GRPO
3. GRPO引入转写奖励与书写系统奖励
4. 构建13,044条播客语码转换基准并审计去泄漏

## 🏗️ 模型架构

输入为语音特征，主干为现成多语言编码器-解码器ASR基础模型（摘要未指明具体网络名）。Stage 1在双引擎、多说话人TTS合成的0.95h语码转换语音上做监督微调，使模型适配语码转换与书写系统映射。Stage 2在SFT收敛模型上做GRPO：对每条语音采样候选转写组，用转写奖励（MER）与书写系统奖励（SCR）构造组内相对优势更新策略。输出为混合Devanagari/Latin的转写文本。摘要未给出参数量。

## 📚 数据集

- 自建尼泊尔语-英语播客基准（评估，13,044句/15.45h，测试10,214、开发2,830）
- TTS合成语码转换语音（训练，0.95h）
- 单语基准（评估，尼泊尔语MER与英语WER）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MER | 自建播客测试集 | 基线 23.40% | **21.52%** | -1.88 pp |
| SPER | 自建播客测试集 | 基线 35.89% | **28.77%** | -7.12 pp |
| SCR_en | 自建播客测试集（173句） | SFT 6.45% | **GRPO 6.36%** | -0.09 pp (p≤0.001) |
| SPER | 自建播客测试集 | SFT 28.77% | **GRPO 28.70%** | -0.07 pp (p=0.022) |
| 尼泊尔语MER | 单语基准 | 基线 20.80%（由2.38pp增益反推） | **18.42%** | -2.38 pp |

合成SFT是跨域迁移的主要来源，MER降1.88pp、SPER降7.12pp；GRPO仅对173句（1.69%）产生统计显著但幅度很小的调整。关键消融显示：在SFT已收敛的编码器-解码器设定下，辅助书写系统奖励与仅用MER优化结果几乎相同，因为合成数据上候选组的书写系统方差接近零。单语上尼泊尔语MER改善2.71pp，英语WER基本保持（3.38% vs 3.33%）。

## 🎯 结论与影响

最强结论是：少量TTS合成语码转换语音的SFT即可带来主要跨域收益，而GRPO在合成数据上因奖励方差不足难以发挥。这提示后续研究应把强化学习用在真实或高多样性rollout数据上，并重视书写系统一致性指标。对工业落地，意味着可用廉价TTS快速适配低资源语码转换ASR，但需自建审计过的真实评测集。

## ⚠️ 局限与未解决问题

GRPO增益极小且仅覆盖1.69%测试句，实用价值有限；合成数据仅0.95h、单一语言对，泛化性未知；未报告推理延迟与模型规模；缺少与更强语码转换专用基线（如带语码转换词典/语言ID约束解码）的对比；基准仅一个播客来源，存在域偏置。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-23/">← 返回 2026-10-23 速递</a></div>
