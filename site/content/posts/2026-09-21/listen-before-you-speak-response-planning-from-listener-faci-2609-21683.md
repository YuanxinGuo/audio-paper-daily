---
title: "Listen Before You Speak: Response Planning from Listener Facial Reactions for Conversational Speech Generation"
date: 2026-09-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出 ReACT-TTS 两阶段框架，用 1 秒听者面部反应序列预测下一句的情感与韵律，再接入 Grad-TTS 实现语音生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对话语音合成</span> <span class="tag-pill tag-pill-soft">#多模态情感识别</span> <span class="tag-pill tag-pill-soft">#韵律建模</span> <span class="tag-pill tag-pill-soft">#语音合成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.21683</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/CYJ1/ReACT-TTS_public" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">CYJ1/ReACT-TTS_public</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.21683" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.21683" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CYJ1/ReACT-TTS_public" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 ReACT-TTS 两阶段框架，用 1 秒听者面部反应序列预测下一句的情感与韵律，再接入 Grad-TTS 实现语音生成。
</div>

## 👥 作者与机构

**Yunji Chu** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做对话 TTS、多模态情感/韵律建模的研究者阅读。建议重点看 §3 的两阶段设计与 §4 的 MELD 双人协议实验，表 2 的十种子 macro-F1/VAD 一致性与消融值得细读；Grad-TTS 端到端部分较薄，可快速略过。

## 🌍 研究背景

对话语音合成通常只依赖文本与对话历史，忽略听者在说话人开口前的即时反馈。已有工作多把情感/韵律预测当作纯文本任务，或使用静态图像而非时序面部动态。本文认为听者开口前 1 秒的面部反应携带互补线索，可用来规划下一句的情感与韵律，从而提升对话语音的语境适配性。

## 💡 核心创新

1. 用 1 秒 pre-response 听者面部序列做响应规划
2. 两阶段解耦：先预测情感/韵律，再语音实现
3. 在 MELD 双人协议上做十种子统计与视觉变体消融
4. 接入 Grad-TTS 骨干完成端到端语音实现

## 🏗️ 模型架构

输入为对话文本与听者开口前 1 秒的面部序列；视觉分支对帧序列做时序建模（Temporal conditioning），与文本分支融合后预测下一句的情感类别与韵律（VAD）表示；预测出的响应风格作为条件接入 Grad-TTS 骨干，生成最终语音波形。摘要未给出参数量与具体网络层细节。

## 📚 数据集

- MELD（训练/评估，双人 dyadic 协议）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-F1 | MELD dyadic | Text-only | **Temporal** | 十种子均值更高（具体数值未给出） |
| VAD concordance | MELD dyadic | Text-only | **Temporal** | 十种子均值更高（具体数值未给出） |
| 主观偏好 | 20 名语音研究者语境适配研究 | Text-only 9% | **Temporal 76%** | +67 个百分点 |

在严格双人 MELD 协议下，Temporal 条件在十个随机种子上取得更高的 macro-F1 与 VAD 一致性，准确率基本持平。消融显示时序建模优于其他视觉变体，显式 early-to-late 差分并非必要；正确听者反应平均优于循环错配。20 名语音研究者中 76% 偏好 Temporal，9% 偏好 Text-only，15% 无偏好。摘要未报告 SI-SDR/PESQ/MOS 等语音质量指标。

## 🎯 结论与影响

最强结论是开口前听者动态可作为对话响应规划的互补线索，并在主观语境适配研究中获得明显偏好。这为对话 TTS 引入多模态听者建模提供了初步证据，后续可探索更细粒度的韵律控制与真实交互场景落地。

## ⚠️ 局限与未解决问题

仅用 MELD 单一数据集，跨语料泛化未知；未报告语音质量/自然度客观指标与推理延迟；Grad-TTS 端到端部分实验较薄；主观研究仅 20 人且为语音研究者，非普通听者；缺少与更强对话 TTS 基线的对比。

## 🔗 开源资源

- **代码**：<https://github.com/CYJ1/ReACT-TTS_public>

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-09-21/">← 返回 2026-09-21 速递</a></div>
