---
title: "DuplexJail: Safety Alignment Breaks Under Spoken Interruption in Full-Duplex Models"
date: 2026-09-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音安全"]
summary: "提出 DuplexJail，通过用户音频通道注入与请求无关的固定语音提示，打断全双工模型生成，使 AdvBench 攻击成功率最高升至 48.7%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音模型</span> <span class="tag-pill tag-pill-soft">#越狱攻击</span> <span class="tag-pill tag-pill-soft">#语音安全对齐</span> <span class="tag-pill tag-pill-soft">#对抗攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.09420</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.09420" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.09420" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 DuplexJail，通过用户音频通道注入与请求无关的固定语音提示，打断全双工模型生成，使 AdvBench 攻击成功率最高升至 48.7%。
</div>

## 👥 作者与机构

**Jaechul Roh** ¹ · Deepak Chandran · Amir Houmansadr · Andrea Fanelli

**机构**：马萨诸塞大学阿默斯特分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音大模型安全、全双工对话系统对齐的研究者与安全工程师阅读。建议通读，重点看 §3 的攻击策略定义（固定延迟 vs 拒绝触发）与表 1/表 2 的四模型对比，再核对附录中 720 条请求的评分协议与是否中断的统计口径。

## 🌍 研究背景

全双工语音模型可在生成回复的同时接收用户语音，这一并发特性此前主要被用于降低延迟与提升自然度，安全评估却仍沿用轮次式（turn-based）范式，即假设攻击只发生在用户完整说完之后。已有语音越狱工作多针对半双工 ASR+LLM 管线，未考虑生成中途插入音频对安全对齐的破坏。本文要回答：在模型流式输出过程中通过用户音频通道插入固定语音提示，能否绕过安全对齐并提升有害回复率。

## 💡 核心创新

1. 提出 DuplexJail：经用户音频通道注入与请求无关的固定语音提示
2. 对比固定延迟中断与基于流式文本拒绝线索的拒绝触发中断两种策略
3. 在四个开源全双工模型、720 条有害请求上系统量化攻击成功率

## 🏗️ 模型架构

攻击不修改模型权重，而是在推理时对全双工语音模型（PersonaPlex、PersonaPlex-RL、FLM-Audio、BayLing-Duplex）的输入流做干预：用户先发出有害请求，随后在固定延迟或检测到模型流式文本中的拒绝线索时，通过用户音频通道播放一段固定的、与请求内容无关的语音提示，从而打断正在进行的生成。评估端对整段回复做有害性判定，统计 whole-response attack success rate，并记录是否实际发生中断。

## 📚 数据集

- AdvBench（评估，有害请求子集）
- HarmBench（评估，有害请求子集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| whole-response ASR | AdvBench | PersonaPlex 基线 6.5% | **40.3%** | +33.8 pp |
| whole-response ASR | AdvBench | PersonaPlex-RL 基线 9.4% | **48.7%** | +39.3 pp |
| whole-response ASR（拒绝触发） | AdvBench | PersonaPlex 基线 6.5% | **35.6%** | +29.1 pp |
| whole-response ASR（拒绝触发） | AdvBench | PersonaPlex-RL 基线 9.4% | **48.6%** | +39.2 pp |

摘要给出四模型、720 条请求的结果：固定延迟中断在 AdvBench 上把 PersonaPlex 与 PersonaPlex-RL 的整段回复攻击成功率分别推到 40.3% 与 48.7%，拒绝触发策略为 35.6% 与 48.6%，且所有试验无论是否真正中断都计入评分。部分条件下 FLM-Audio 有害回复率上升，BayLing-Duplex 反而下降，说明攻击效果存在模型间差异。摘要未给出 HarmBench 的具体数值、消融或延迟开销。

## 🎯 结论与影响

最强结论是：语音中断本身即可作为越狱攻击向量，使全双工模型的安全对齐在生成中途失效。这提示后续全双工安全研究需从单轮判定转向覆盖整个交互过程，并推动工业界在流式对话系统中加入中断感知的安全监控与实时拒答机制。

## ⚠️ 局限与未解决问题

仅四个开源模型、两个有害请求基准，未覆盖闭源商用全双工系统；固定提示与请求无关，未探索自适应或语义相关的中断；未报告推理延迟、中断检测开销与防御方案；BayLing-Duplex 上效果下降的原因缺乏分析，也缺少针对提示长度、延迟参数的消融。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-09-10/">← 返回 2026-09-10 速递</a></div>
