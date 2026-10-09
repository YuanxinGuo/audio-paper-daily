---
title: "Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用冻结TTS模型的语音token似然作奖励，通过GRPO训练文本风格规划器，提升对话TTS的风格与情感相似度。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#风格控制</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.11461</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.11461" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.11461" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用冻结TTS模型的语音token似然作奖励，通过GRPO训练文本风格规划器，提升对话TTS的风格与情感相似度。
</div>

## 👥 作者与机构

**Shiao Zhu** ¹ · Lianbo Liu · Sizhen Lyu · Yuzhe Wang · Sheng Li · Takahiro Shinozaki

**机构**：东京工业大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做可控TTS、LLM风格规划与RLHF语音方向的研究者。建议重点看§3的SRSP框架与GRPO奖励设计，以及表2的风格/情感相似度对比；若关注落地可看推理开销讨论。方法思路可迁移，值得通读。

## 🌍 研究背景

自然语言风格描述为LLM与可控TTS提供可解释接口，但现有做法把描述当伪标签，将目标声学压缩成文本，描述保真度未必等于对特定合成器的有效控制。作者实证发现语音-文本对齐只能弱预测同一话语候选指令的下游声学相似度，说明仅靠文本监督不足，需要直接以下游TTS的声学反馈来优化风格规划器。

## 💡 核心创新

1. 用冻结TTS的teacher-forced语音token似然作奖励
2. GRPO组相对策略优化训练文本风格规划器
3. 实证揭示语音-文本对齐与声学相似度弱相关
4. 对话历史+回复文本生成候选风格指令

## 🏗️ 模型架构

输入为对话历史与待合成回复文本，经基于LLM的文本风格规划器生成多条候选风格指令；候选指令送入冻结的下游TTS模型，计算目标语音token的teacher-forced似然作为奖励；采用GRPO在组内做相对优势估计更新规划器，无需可微TTS。输出为选定的风格指令，供TTS合成。摘要未给参数量。

## 📚 数据集

- ISCSLP 2026 CoT-TTS 语料英文子集（训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 语音风格相似度 | ISCSLP 2026 CoT-TTS 英文子集 | Base LLM / target-audio-informed captioning | **更高** | 提升 |
| 情感相似度 | ISCSLP 2026 CoT-TTS 英文子集 | Base LLM / target-audio-informed captioning | **更高** | 提升 |
| Mel-Cepstral Distortion | ISCSLP 2026 CoT-TTS 英文子集 | Base LLM / target-audio-informed captioning | **更低** | 下降 |

摘要仅给出相对结论：SRSP在语音风格与情感相似度上高于Base LLM和target-audio-informed captioning基线，MCD更低；LLM表达性语音评测在上下文适当性与参考一致性上优于所有基线。未提供具体数值、消融、推理延迟或跨数据集泛化结果。

## 🎯 结论与影响

最强结论是以下游TTS声学反馈作奖励可训练出更有效的文本风格规划器，优于纯文本伪标签。该思路提示风格控制应从描述保真转向合成器在环优化，后续可探索更高效奖励与多语言迁移；工业上可用于对话TTS的细粒度风格调控。

## ⚠️ 局限与未解决问题

仅英文子集、单一TTS后端，泛化性未知；未报推理延迟与训练成本；缺少奖励设计消融与人工MOS；基线数量有限，未与更强风格控制方法对比。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-09/">← 返回 2026-10-09 速递</a></div>
