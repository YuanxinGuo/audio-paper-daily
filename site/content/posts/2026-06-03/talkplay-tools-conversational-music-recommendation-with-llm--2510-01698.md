---
title: "TalkPlay-Tools: Conversational Music Recommendation with LLM Tool Calling"
date: 2026-06-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐推荐"]
summary: "提出基于LLM工具调用的音乐推荐系统，统一检索-重排序流程，支持多种检索方式。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐推荐</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#工具调用</span> <span class="tag-pill tag-pill-soft">#检索重排序</span> <span class="tag-pill tag-pill-soft">#对话系统</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.01698</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-03</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.01698" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.01698" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LLM工具调用的音乐推荐系统，统一检索-重排序流程，支持多种检索方式。
</div>

## 👥 作者与机构

**Seungheon Doh** ¹ · Keunwoo Choi · Juhan Nam

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐推荐和对话系统研究者。重点看§3系统架构和§4实验部分，了解工具调用如何整合多种检索。可先读§3.2工具规划模块。

## 🌍 研究背景

现有基于LLM的生成式推荐系统主要依赖模型内部知识，忽略了元数据过滤、属性检索等传统但有效的方法。本文旨在将LLM作为端到端推荐系统，通过工具调用统一布尔过滤、稀疏检索、稠密检索和生成式检索，实现多模态查询和灵活的工具编排。

## 💡 核心创新

1. 提出LLM工具调用统一检索-重排序框架
2. 设计工具规划模块预测工具类型、顺序和参数
3. 整合布尔过滤、BM25、嵌入相似度、语义ID四种检索
4. 支持多模态用户查询和自然语言交互

## 🏗️ 模型架构

输入用户自然语言查询，LLM首先进行工具规划，预测需要调用的工具（布尔过滤、BM25、嵌入相似度、生成式检索）及其执行顺序和参数。然后依次执行各工具，得到候选列表，最后通过重排序模块输出最终推荐结果。系统端到端训练，LLM作为核心控制器。

## 📚 数据集

- 未在摘要中明确提及数据集

## 📊 实验结果

摘要未提供具体实验数据，仅声称在多种推荐场景下达到竞争性能。需要查看全文获取详细指标。

## 🎯 结论与影响

本文提出的LLM工具调用框架为对话式音乐推荐提供了新范式，通过灵活组合多种检索方法提升了推荐效果和可解释性。未来可扩展到其他领域，并探索更复杂的工具编排策略。

## ⚠️ 局限与未解决问题

摘要未报告具体性能指标和对比基线，缺乏定量评估。未讨论工具调用延迟和计算开销。未提及用户研究和实际部署可行性。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-03/">← 返回 2026-06-03 速递</a></div>
