---
title: "AutoMV: An Automatic Multi-Agent System for Music Video Generation"
date: 2026-11-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "提出免训练多智能体框架 AutoMV，用 LLM 编剧与导演智能体依据时间对齐歌词与音乐分析规划整首歌的视觉叙事，并构建 M2VBench 评测基准。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐视频生成</span> <span class="tag-pill tag-pill-soft">#多智能体</span> <span class="tag-pill tag-pill-soft">#多模态评估</span> <span class="tag-pill tag-pill-soft">#歌词对齐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.12196</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.12196" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.12196" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出免训练多智能体框架 AutoMV，用 LLM 编剧与导演智能体依据时间对齐歌词与音乐分析规划整首歌的视觉叙事，并构建 M2VBench 评测基准。
</div>

## 👥 作者与机构

**Xiaoxuan Tang** ¹ · Xinping Lei · Chaoran Zhu · Shiyun Chen · Ruibin Yuan · Yizhi Li · Changjae Oh · Ge Zhang · … 等 5 人

**机构**：昆山杜克大学 · 伦敦玛丽女王大学 · 剑桥大学 · 北京智源人工智能研究院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音乐生成、多模态生成与 LLM Agent 规划的研究者阅读。若关注音乐-视觉跨模态对齐，值得通读；重点看 §3 的 Screenwriter/Director 分工与角色库机制，以及 §4 M2VBench 的 12 项评分细则和专家评测表。若只关心音频信号处理可略读。

## 🌍 研究背景

音乐视频生成此前多依赖音乐到视频的短片段生成或音频反应式视觉特效，代表工作只能产出数秒 clip，且几乎不利用歌词语义。整首歌 MV 需要理解隐喻性、多语言、副歌重复的歌词，并把意象按歌曲结构铺排，现有方法缺乏长时叙事规划与角色一致性约束。本文要解决的是：如何在无训练条件下，从时间对齐歌词与音乐分析生成结构完整、角色一致、镜头类型合理的整首歌 MV，并给出可信评测。

## 💡 核心创新

1. LLM Screenwriter + Director 双智能体分工规划整曲视觉叙事
2. 共享 character bank 维持跨镜头角色一致性
3. 按镜头路由至 cinematic 或 lip-sync 渲染并加验证
4. 构建 M2VBench：30 首官方 MV + 12 项专家评分细则
5. 验证多模态 judge 在 rubric 引导下可复现专家排序

## 🏗️ 模型架构

输入为整首歌音频及其时间对齐歌词，先做音乐分析（结构、节拍、段落）与歌词语义解析；Screenwriter 智能体据此生成分段的叙事大纲与场景描述，Director 智能体将大纲拆解为逐镜头（shot）计划，并通过共享 character bank 查询/写入角色外观描述以保证一致性；每个镜头按内容路由到 cinematic 渲染或 lip-sync 渲染分支，渲染结果经验证模块检查后拼接为整曲 MV。全流程 training-free，依赖现成 LLM 与视频生成模型，摘要未给参数量。

## 📚 数据集

- M2VBench（评估，30 首已发布歌曲及官方 MV）

## 📊 实验结果

摘要仅给出定性结论：专家评测显示 AutoMV 优于其他基线，但与人类制作的官方 MV 仍有差距；消融表明时间对齐歌词对音乐主题对齐与叙事性贡献显著；所选多模态 judge 在 rubric 引导下能复现专家对自动系统的排序，细粒度评分上存在偏差。摘要未披露具体指标数值。

## 🎯 结论与影响

最强结论是免训练多智能体规划加角色库可在整首歌尺度上生成结构连贯、角色一致的 MV，并显著优于现有音乐到视频基线。其 M2VBench 与 rubric 驱动的 judge 复现实验，为音乐视频生成提供了可复用的评测范式，对内容创作工具落地有直接参考价值。

## ⚠️ 局限与未解决问题

与人类 MV 仍有明显差距；摘要未给客观指标数值与推理成本，缺少与更多视频生成基线的定量对比；M2VBench 仅 30 首，规模与风格覆盖有限；多模态 judge 在细粒度评估上存在偏差，评分可靠性待验证；未报告生成时延与算力开销。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-18/">← 返回 2026-11-18 速递</a></div>
