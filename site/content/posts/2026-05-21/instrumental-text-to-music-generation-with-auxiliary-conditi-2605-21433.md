---
title: "Instrumental Text-to-Music Generation with Auxiliary Conditioning Branches"
date: 2026-05-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐生成"]
summary: "本文研究在数据受限条件下，辅助条件分支（歌词和音色）对文本到乐器音乐生成的影响，发现即使退化输入，这些分支仍作为训练锚点提升性能。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#文本到音乐生成</span> <span class="tag-pill tag-pill-soft">#扩散变换器</span> <span class="tag-pill tag-pill-soft">#消融研究</span> <span class="tag-pill tag-pill-soft">#乐器音乐</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.21433</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.21433" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.21433" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文研究在数据受限条件下，辅助条件分支（歌词和音色）对文本到乐器音乐生成的影响，发现即使退化输入，这些分支仍作为训练锚点提升性能。
</div>

## 👥 作者与机构

**Junyoung Koh** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐生成和扩散模型研究者。重点读§3消融实验和§4.2结果分析，了解辅助分支的意外作用。可跳过§2背景。

## 🌍 研究背景

文本到音乐生成近年快速发展，自回归和扩散模型可从自然语言提示生成高质量音乐。但这些进展依赖大规模数据和预训练，难以隔离特定设计选择的影响。本文聚焦数据受限场景，使用扩散变换器（DiT）骨干，并加入歌词和音色条件分支，但任务为纯乐器音乐生成，因此这些分支接收退化信号。作者通过控制消融研究，探究这些分支的实际贡献。

## 💡 核心创新

1. 在DiT中引入歌词和音色辅助条件分支
2. 系统消融揭示辅助分支的训练锚点作用
3. 在ICME 2026 ATTM挑战赛中获得最高MOS
4. 提出效率和性能两个提交版本

## 🏗️ 模型架构

输入为文本嵌入（T5）和可选歌词/音色条件，主干为扩散变换器（DiT）。歌词分支使用预训练歌词编码器，音色分支使用音色嵌入。模型通过扩散过程生成mel谱图，再经声码器合成音频。参数量未明确给出。

## 📚 数据集

- 内部数据集（训练，未公开规模）
- ICME 2026 ATTM挑战赛数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS | ICME 2026 ATTM挑战赛 | 未明确基线 | **最高MOS** | 第一 |

消融实验显示，移除辅助分支后模型在AudioBox美学、LLM评判和人类MOS上得分降低；将节省参数用于增加DiT深度仅能部分恢复。在ICME 2026 ATTM挑战赛中，性能提交在客观指标和35人MOS评估中均获第一，效率提交在客观指标中并列第二。

## 🎯 结论与影响

辅助条件分支在退化输入下仍显著提升生成质量，其作用超越显式条件内容，可能作为训练锚点。该发现对数据受限场景下的模型设计有指导意义，提示未来可探索更高效的条件利用方式。工业上可用于资源受限的音乐生成应用。

## ⚠️ 局限与未解决问题

未开源代码和模型；数据集未公开，难以复现；仅验证了乐器音乐任务，泛化性未知；未与最新大规模模型（如MusicGen）对比；消融仅涉及分支有无，未深入分析分支内部机制。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-21/">← 返回 2026-05-21 速递</a></div>
