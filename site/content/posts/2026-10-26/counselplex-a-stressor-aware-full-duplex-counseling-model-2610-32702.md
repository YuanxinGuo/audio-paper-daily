---
title: "CounselPlex: A Stressor-Aware Full-Duplex Counseling Model"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音对话系统"]
summary: "提出 CounselPlex 全双工心理咨询框架，用压力源状态更新与注入缓解模型只关注最新话语的 Stressor Blindness 问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音对话系统</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#全双工语音交互</span> <span class="tag-pill tag-pill-soft">#心理咨询对话</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#位置编码增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32702</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32702" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32702" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 CounselPlex 全双工心理咨询框架，用压力源状态更新与注入缓解模型只关注最新话语的 Stressor Blindness 问题。
</div>

## 👥 作者与机构

**Yeonju Kim** ¹ · Bella Godiva · Yong Man Ro

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做全双工语音交互、对话式 LLM 与心理健康应用的研究者阅读。值得浏览而非通读：重点看 §3 中压力源状态的更新时机（seeker silence）与注入位置，以及 RPSA 的位置编码设计；实验部分关注 LLM-judge 评测协议与基线选择，判断其结论可信度。

## 🌍 研究背景

全双工语音模型可同时听与说，实现低延迟自然交互，是近期语音对话研究热点。但现有模型在心理咨询场景中倾向只处理最新一轮话语，丢失求助者长期困扰（stressor）的上下文，作者称之为 Stressor Blindness。此前工作多聚焦轮次切换与延迟优化，缺少对长程问题状态的显式建模，本文即针对该缺陷提出压力源感知框架。

## 💡 核心创新

1. 在求助者静默期更新短时压力源状态
2. 将压力源状态注入监听阶段的位置表示
3. 提出 RoPE Position Shift Augmentation (RPSA) 扩展位置覆盖
4. 用 LLM-judge 评估咨询质量与压力源 grounding

## 🏗️ 模型架构

摘要未给出完整网络细节。整体为全双工语音框架：输入为双向语音流，主干为支持同时听说的语音-语言模型；关键模块包括在求助者静默段触发的压力源状态更新模块，以及把该状态注入监听阶段特定位置的注入机制；训练侧引入 RPSA，对 RoPE 位置索引做偏移增强以覆盖更长轮次深度。输出为咨询回复语音。参数量与具体主干网络摘要未说明。

## 📊 实验结果

摘要仅称 LLM-judge 评测显示咨询质量与压力源 grounding 优于强基线，并称 RPSA 在更长轮次深度上带来提升，但未给出任何具体指标数值、数据集名称或基线名称，无法量化比较。

## 🎯 结论与影响

最强结论是显式维护并注入压力源状态可缓解全双工咨询模型的长程上下文丢失。若评测协议可靠，该思路可迁移到其他需要长期用户状态的全双工助手场景，对心理健康类语音产品有落地参考价值。

## ⚠️ 局限与未解决问题

摘要未披露数据集、基线细节与量化指标，LLM-judge 评测主观性强且易受评委模型偏置影响；缺少人工评估与延迟、算力开销报告；压力源状态更新依赖静默检测，噪声环境下鲁棒性未知。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
