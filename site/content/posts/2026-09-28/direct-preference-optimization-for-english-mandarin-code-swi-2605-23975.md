---
title: "Direct Preference Optimization for English-Mandarin Code-Switching Speech Recognition in Audio LLMs"
date: 2026-09-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "用DPO对齐Audio LLM，构造偏好对纠正英汉语码切换识别中的漏语、翻译替代与幻觉三类失败模式。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#代码切换</span> <span class="tag-pill tag-pill-soft">#偏好优化</span> <span class="tag-pill tag-pill-soft">#音频大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23975</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23975" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23975" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用DPO对齐Audio LLM，构造偏好对纠正英汉语码切换识别中的漏语、翻译替代与幻觉三类失败模式。
</div>

## 👥 作者与机构

**Trung Nguyen Quang** ¹ · Cheng Yi Lewis Won · Minh Duc Pham · Yingxu He · Shuo Sun · Ai Ti Aw

**机构**：新加坡科技研究局

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多语种/语码切换ASR与Audio LLM对齐的研究者。建议通读，重点看失败模式分类定义与偏好对构造流程（§3），以及表2的ID/OOD MER对比；若关注落地，需自行补看推理开销与数据构造成本。

## 🌍 研究背景

Audio LLM（如Qwen-Audio、SALMONN类）在多语种ASR上表现强，但对英汉语码切换语音存在系统性失败：漏掉一种语言、把转写变成翻译、以及幻觉输出。此前多依赖监督微调或提示工程，难以直接约束“保持混合语言构成”这一行为目标，且缺乏对失败模式的显式建模。本文要解决的是如何用对齐手段让模型在转写提示下保留语码切换内容而非翻译。

## 💡 核心创新

1. 归纳三类语码切换失败模式：漏语、翻译替代、幻觉
2. 用DPO构造chosen/rejected偏好对，rejected显式模仿失败模式
3. 在三个Audio LLM上验证行为一致性偏移
4. 100K偏好对、570小时规模的对齐训练

## 🏗️ 模型架构

输入为英汉语码切换语音及其转写提示，经Audio LLM的音频编码器与LLM主干联合处理。训练阶段不改变主干结构，而是在已有Audio LLM上做DPO：对同一语音构造chosen（保留混合语言转写）与rejected（漏语/翻译/幻觉）响应对，用偏好损失优化策略模型相对参考模型的输出分布。摘要未给出具体参数量与网络细节。

## 📚 数据集

- 自建英汉语码切换偏好数据集（100K对，570小时，训练）
- 分布内测试集（评估，具体名称未给出）
- 分布外测试集（评估，具体名称未给出）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MER | 分布内测试集 | 未对齐Audio LLM基线（数值未给出） | **未给出绝对值** | -89.6% |
| MER | 分布外测试集 | 未对齐Audio LLM基线（数值未给出） | **未给出绝对值** | -20.0% |

摘要仅报告相对MER下降：分布内最高降89.6%，分布外降20.0%，未给出绝对MER、WER或各模型分项数值，也无消融与效率指标。可确认的是三个Audio LLM均出现一致的行为偏移，即从翻译转向保留语言构成。

## 🎯 结论与影响

最强结论是DPO能有效诱导多语种Audio LLM产生正确的语码切换转写行为，而非依赖额外监督标注。这为语码切换ASR提供了一条轻量对齐路径，后续可推广到其他语言对与更多失败模式；工业上意味着可用偏好数据低成本修正大模型转写偏差。

## ⚠️ 局限与未解决问题

摘要未给绝对MER/WER、未说明基线模型与规模、无消融验证三类失败模式各自的贡献，也未报告推理延迟与训练成本；偏好对构造依赖人工或规则标注，可能存在分布偏置，OOD提升仅20%说明泛化仍有限。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-09-28/">← 返回 2026-09-28 速递</a></div>
