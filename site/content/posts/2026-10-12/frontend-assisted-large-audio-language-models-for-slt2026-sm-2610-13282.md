---
title: "Frontend-Assisted Large Audio-Language Models for SLT2026 SmartGlasses Challenge"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "面向SmartGlasses Challenge Track 1，用SoulX-Transcriber多模态大模型做时间戳说话人属性ASR，并对比前端分离对性能的影响。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#说话人日志</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.13282</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.13282" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.13282" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向SmartGlasses Challenge Track 1，用SoulX-Transcriber多模态大模型做时间戳说话人属性ASR，并对比前端分离对性能的影响。
</div>

## 👥 作者与机构

**Yushi Wang** ¹ · Zeyan Song · Xiaobin Rong · Chengwei Liu · Jun Gao · Jing Lu

**机构**：南京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做说话人属性ASR、会议/眼镜场景远场识别的工程与研究者阅读。建议重点看前端处理对比实验与最终系统配置部分，尤其是GSS与数据驱动分离在验证集上的增益差异；若关注大模型ASR微调流程，可通读§3。

## 🌍 研究背景

时间戳说话人属性ASR需在重叠语音、噪声与远场条件下同时输出文本、时间戳与说话人标签。此前主流方案多为级联系统：先做语音分离或目标说话人提取，再接ASR与说话人日志，误差逐级累积。近期多模态大模型可直接吃全长音频并生成结构化转写，但前端处理是否仍有增益、在眼镜场景下是否稳定尚不清楚。本文针对SmartGlasses Challenge Track 1，系统比较规则式GSS与数据驱动分离前端对SoulX-Transcriber的影响。

## 💡 核心创新

1. 将SoulX-Transcriber多模态大模型用于时间戳说话人属性ASR
2. 系统对比规则式GSS与数据驱动语音分离前端增益
3. 面向推理稳定性选择微调后的大模型作为最终提交

## 🏗️ 模型架构

输入为全长双人对话音频，主干为SoulX-Transcriber多模态大语言模型，直接生成含时间戳与说话人属性的结构化转写。前端可选两条路径：规则式Guided Source Separation（GSS）与数据驱动语音分离模型，用于抑制重叠与噪声后再送入大模型。最终提交采用微调后的SoulX-Transcriber，未叠加前端以保推理稳定。摘要未给出参数量与具体网络细节。

## 📚 数据集

- SmartGlasses Challenge Track 1 验证集（评估前端处理效果）
- SmartGlasses Challenge Track 1 测试集（最终评估，tcpCER 6.22）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| tcpCER | SmartGlasses Challenge Track 1 测试集 | 未给出具体基线数值 | **6.22** | 摘要未给出对比增量 |

摘要仅报告最终系统在测试集上tcpCER为6.22，并指出规则式GSS与数据驱动分离前端均在验证集上带来提升。但未给出各前端的具体数值、消融对比、推理延迟或与官方基线的差距，实验信息较为有限。

## 🎯 结论与影响

本文最强结论是微调SoulX-Transcriber在挑战赛测试集取得tcpCER 6.22，且前端处理在验证集有效但为稳定性未纳入最终系统。这提示大模型ASR与前端分离的协同仍需在稳定性与增益间权衡，对眼镜类远场多说话人转写落地有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出基线数值、前端增益的具体量化、消融实验与推理延迟；最终系统放弃前端仅以稳定性为由，缺乏系统性分析；数据集与赛道特定，泛化性未知。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
