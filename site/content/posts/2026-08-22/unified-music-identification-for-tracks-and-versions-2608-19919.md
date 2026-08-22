---
title: "Unified Music Identification for Tracks and Versions"
date: 2026-08-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐识别"]
summary: "本文提出统一基准评估曲目识别与版本识别，发现现有模型无法同时兼顾准确性与鲁棒性，并训练基线模型证明统一系统的可行性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#版本识别</span> <span class="tag-pill tag-pill-soft">#曲目识别</span> <span class="tag-pill tag-pill-soft">#鲁棒性</span> <span class="tag-pill tag-pill-soft">#统一基准</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.19919</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.19919" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.19919" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文提出统一基准评估曲目识别与版本识别，发现现有模型无法同时兼顾准确性与鲁棒性，并训练基线模型证明统一系统的可行性。
</div>

## 👥 作者与机构

**R. Oguz Araz** ¹ · Joan Serr\`a · Yuki Mitsufuji · Xavier Serra · Dmitry Bogdanov

**机构**：庞培法布拉大学 · 索尼计算机科学实验室 · 索尼AI

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索（MIR）研究者阅读，重点关注第3节统一基准的设计和第4节基线模型的训练细节。若关注鲁棒性，可细读表2和表3的对比结果。

## 🌍 研究背景

音乐识别领域，曲目识别（TI）和版本识别（VI）传统上被分开处理。TI旨在匹配精确曲目，VI旨在匹配翻唱或改编版本。然而，每个曲目本身是其最接近的版本，因此VI理论上可以涵盖TI。但VI系统需要同时应对信号处理和音频退化，现有模型往往在准确性和鲁棒性上难以兼顾。本文旨在探索VI能否统一TI，并为此构建统一基准。

## 💡 核心创新

1. 提出统一基准，同时评估TI和VI的准确性与鲁棒性
2. 系统比较7个现有模型，揭示其各自局限
3. 训练基线模型，证明统一系统在10秒查询下可行
4. 分析限制TI性能的两个检索约束
5. 展望统一扩展到其他音乐识别任务

## 🏗️ 模型架构

本文未提供具体模型架构细节，仅提及训练基线模型。基线模型可能基于音频嵌入，输入为音频片段，输出为嵌入向量，通过相似度检索实现识别。具体网络结构未在摘要中说明。

## 📊 实验结果

摘要中未提供具体数值结果，仅说明现有模型在统一基准上均无法同时达到高准确性和鲁棒性，而训练的统一基线模型在10秒查询下可行。具体指标和对比数据未给出。

## 🎯 结论与影响

本文通过统一基准揭示了TI和VI的兼容性，证明统一系统可行，为音乐识别任务的一体化提供了方向。对后续研究，该基准可作为标准评估工具，推动更鲁棒的统一模型发展。工业上，可简化音乐识别系统，降低成本。

## ⚠️ 局限与未解决问题

摘要未提及模型具体架构和参数量，缺乏消融实验和效率分析。统一基准的构建细节和数据集来源未说明，可能影响可复现性。此外，仅验证了10秒查询，其他时长未探讨。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-08-22/">← 返回 2026-08-22 速递</a></div>
