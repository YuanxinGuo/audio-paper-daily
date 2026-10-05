---
title: "Can External Sources Help the Knowledge Cut-off Issues in Audio Deepfake Detection?"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "将RAG式检索增强引入音频深伪检测，在推理时查询外部知识库，缓解SSL模型的知识截断问题。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频深度伪造检测</span> <span class="tag-pill tag-pill-soft">#检索增强</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#分数级融合</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2509.21728</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2509.21728" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2509.21728" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将RAG式检索增强引入音频深伪检测，在推理时查询外部知识库，缓解SSL模型的知识截断问题。
</div>

## 👥 作者与机构

**Xin Wang** ¹ · Junichi Yamagishi · Xuechen Liu · Wanying Ge

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频深伪检测与SSL微调的读者。建议重点看知识库构建与检索策略一节，以及分数级融合的实验表。若关注RAG在音频的迁移，可通读；若只关心检测精度提升，可只看结论与消融部分。

## 🌍 研究背景

音频深伪检测主流做法是用固定数据集训练参数化模型（如基于SSL前端加分类头），推理与评估均依赖该静态模型。这类方法存在知识截断：训练后无法纳入新出现的伪造算法或新域数据，且对域偏移敏感。已有工作多聚焦更强SSL前端或数据增强，少有在推理阶段引入外部可更新知识。本文要回答检索增强在何种条件下优于纯参数化基线。

## 💡 核心创新

1. 推理时查询外部知识库的检索增强检测框架
2. 刻画检索增强有效的条件：知识库与微调数据不同但同域
3. 线性分数级融合检索与独立检测器

## 🏗️ 模型架构

输入为待测语音，经SSL前端（如Wav2Vec2/XLS-R类）提取表征并由参数化检测器给出分数；同时将语音表征作为查询，从可在线更新的外部知识库中检索相似样本及其标签，得到检索分数；最后将参数化分数与检索分数做线性分数级融合输出真伪判定。摘要未给出具体网络名与参数量。

## 📊 实验结果

摘要未给出具体指标数值，仅给出定性结论：当知识库内容与SSL微调数据不同、但与评估集同域时，检索增强收益最大，线性分数级融合也有效；当测试分布与知识库域差异大时，提升有限且系统仍受域偏移影响。

## 🎯 结论与影响

最强结论是检索增强并非普适增益，其有效性取决于知识库与评估域的匹配关系。这为音频深伪检测提供了推理时可更新知识的新思路，提示后续研究应关注知识库构建与域对齐。工业上可用于持续纳入新伪造样本，但需配套域监控。

## ⚠️ 局限与未解决问题

作者承认系统对域偏移仍脆弱，测试分布偏离知识库时提升有限。作为审稿人可见：缺少具体指标与数据集细节，未报推理延迟与检索开销，未与更多强基线对比，知识库规模与检索质量的影响缺少消融。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-05/">← 返回 2026-10-05 速递</a></div>
