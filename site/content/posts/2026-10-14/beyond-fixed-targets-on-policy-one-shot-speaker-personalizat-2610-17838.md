---
title: "Beyond Fixed Targets: On-Policy One-Shot Speaker Personalization for Autoregressive Text-To-Speech Models"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "针对自回归TTS单样本说话人个性化中SFT失效问题，提出GRPO与在线自蒸馏两种on-policy方法，提升相似度并保持可懂度。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音合成</span> <span class="tag-pill tag-pill-soft">#说话人个性化</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#自回归TTS</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17838</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-13</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17838" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17838" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>针对自回归TTS单样本说话人个性化中SFT失效问题，提出GRPO与在线自蒸馏两种on-policy方法，提升相似度并保持可懂度。
</div>

## 👥 作者与机构

**Sangkwon Park** ¹ · Che Hyun Lee · Heeseung Kim · Sungroh Yoon ✉

**机构**：首尔大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做TTS个性化、RLHF/GRPO在语音生成中应用的读者。建议通读，重点看§3的on-policy方法设计与§4的GRPO vs OPSD对比实验，以及关于target diversity的消融分析。若只关心结论，看表1与图2即可。

## 🌍 研究背景

单样本说话人个性化是TTS的重要能力，但自回归TTS在单参考对上做SFT会迅速退化，推理时出现空白或近空输出。此前工作多用零样本伪配对扩充数据，但目标仍是固定、teacher-forced的off-policy监督，相似度提升有限且WER上升。本文要解决的核心问题是：为何单样本SFT失败，以及如何用on-policy监督替代固定off-policy目标。

## 💡 核心创新

1. 指出固定off-policy监督是单样本SFT失败主因
2. 用GRPO+说话人相似度奖励做on-policy优化
3. 提出OPSD，用参考条件教师做在线自蒸馏
4. 验证增益来自on-policy而非目标多样性

## 🏗️ 模型架构

基于自回归TTS模型（如VALL-E类），输入为文本token与参考语音的声学token。GRPO分支：模型采样生成语音，用说话人相似度模型打分作为奖励，组内相对优势更新策略，无需critic。OPSD分支：参考条件教师对模型自身采样输出提供软分布监督，学生在线匹配。两者均保持可懂度，OPSD无需外部奖励评估，适配更快。摘要未给参数量。

## 📊 实验结果

摘要未给出具体指标数值，仅定性说明：GRPO整体性能最强，OPSD适配速度显著更快且无需外部奖励评估。两者均提升说话人相似度并保持可懂度。进一步分析确认增益来自on-policy监督而非目标多样性。缺少与SFT、零样本伪配对基线的定量对比表。

## 🎯 结论与影响

最强结论是on-policy训练可作为单样本AR TTS个性化的有效框架，替代固定off-policy监督。对后续研究，提示RL与自蒸馏在TTS个性化中的潜力，可能推动更多on-policy语音生成工作。工业上，OPSD无需奖励模型，部署成本更低，适合快速个性化定制。

## ⚠️ 局限与未解决问题

摘要未报具体指标、数据集与推理延迟，缺少与主流零样本TTS基线的定量对比；GRPO依赖说话人相似度奖励模型，可能引入奖励黑客；OPSD的教师质量与蒸馏温度等超参未讨论；未验证跨语言、跨域泛化。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
