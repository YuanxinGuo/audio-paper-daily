---
title: "Unified Target-Speaker ASR with Text and Enrollment Speech Cues"
date: 2026-09-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出统一双线索TS-ASR框架，单模型支持文本线索、注册语音或两者，用交叉注意力条件模块与负线索采样，五字文本线索下CER降至8.80%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#Conformer</span> <span class="tag-pill tag-pill-soft">#多说话人</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.33853</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.33853" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.33853" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出统一双线索TS-ASR框架，单模型支持文本线索、注册语音或两者，用交叉注意力条件模块与负线索采样，五字文本线索下CER降至8.80%。
</div>

## 👥 作者与机构

**Yuxiang Mei** ¹ · Yuchen Yan · Dongxing Xu · Jiaen Liang · Yanhua Long

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做目标说话人ASR、多说话人识别与线索融合的研究者阅读。建议通读，重点看 §3 的交叉注意力线索条件模块与负线索采样设计，以及表 2 中五种录音/域条件下的 CER 对比。可先看双线索融合与并行融合的消融，再复现五字线索设置。

## 🌍 研究背景

目标说话人ASR需在多说话人混合中识别指定说话人。此前主流依赖注册语音（enrollment）做说话人条件，另一支用已知文本线索（如唤醒词）定位目标。两类线索信息互补，但通常被分开研究，缺少统一框架。本文要解决的是：如何在单一模型中同时利用文本线索与注册语音，并在双线索训练下提供线索有效性监督。

## 💡 核心创新

1. 统一双线索TS-ASR框架，单模型支持文本、注册语音或两者
2. 交叉注意力线索条件模块嵌入共享Conformer块
3. 负线索采样为双线索训练提供线索有效性监督
4. 拼接式双线索融合优于并行融合

## 🏗️ 模型架构

输入为多说话人混合语音特征与可选线索（文本线索的词元序列或注册语音的说话人嵌入）。主干为共享Conformer块，交叉注意力线索条件模块插入其中：文本线索与混合表示交互，按已知词汇内容提取目标说话人信息；注册语音提供互补说话人信息。双线索时拼接两路条件表示。输出为识别词元序列，训练时用负线索采样做线索有效性监督。摘要未给参数量。

## 📚 数据集

- 30,000条双说话人混合（训练/评估，覆盖五种录音/域条件）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | 五种录音/域条件双说话人混合 | text-only 17.32 | **8.80** | -8.52% |
| CER | 五种录音/域条件双说话人混合 | enrollment-only 29.06 | **8.80** | -20.26% |
| CER | 五种录音/域条件双说话人混合 | parallel dual-cue 9.49 | **8.80** | -0.69% |

在30,000条双说话人混合、五种录音/域条件、四种oracle文本线索长度下评估。五字文本线索时，拼接双线索CER 8.80%，优于纯文本17.32%、纯注册29.06%与并行双线索9.49%，且在全部五个评估子集上双线索CER更低。摘要未给消融细节、推理延迟与参数量。

## 🎯 结论与影响

最强结论是联合利用词汇与说话人互补信息可显著降低TS-ASR的CER，拼接双线索在五字线索下即达8.80%。这为线索融合式目标说话人ASR提供了统一基线，后续可探索线索长度自适应与真实唤醒词场景。工业上对唤醒词+注册语音的个性化识别有直接参考价值。

## ⚠️ 局限与未解决问题

文本线索为oracle、长度受控，未验证真实ASR识别出的唤醒词噪声；仅双说话人混合，未涉及更多说话人或混响；缺少参数量、推理延迟与负线索采样消融的量化；五种域条件的具体构成摘要未说明。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-29/">← 返回 2026-09-29 速递</a></div>
