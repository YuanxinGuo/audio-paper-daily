---
title: "CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation"
date: 2026-09-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频-视觉导航"]
summary: "提出循环-时序注意力网络CTAN，用双向循环一致性约束与跨模态记忆增强视听语义融合，提升具身音频导航成功率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频-视觉导航</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态融合</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#具身智能</span> <span class="tag-pill tag-pill-soft">#跨模态注意力</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.17420</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.17420" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.17420" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出循环-时序注意力网络CTAN，用双向循环一致性约束与跨模态记忆增强视听语义融合，提升具身音频导航成功率。
</div>

## 👥 作者与机构

**Teng Liu** ¹ · Yinfeng Yu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做具身智能、视听多模态融合与导航的研究者阅读。若关注跨模态注意力机制设计，可重点看 §3 的 AVRCA 与 TCMM 模块及 Replica/Matterport3D 上的消融实验；若只关心语音增强/分离，可略读。建议先看方法框架图与 SR/SPL 对比表。

## 🌍 研究背景

音频-视觉具身导航要求机器人融合视觉与双耳音频线索定位声源。此前方法（如 AV-WaN、SoundSpaces 系列）多采用简单多模态拼接或注意力聚合，难以刻画异构模态间的几何与语义关系，在复杂环境中出现信息退化，且存在听觉盲区导致性能骤降。本文旨在通过主动语义增强融合而非直接拼接，提升跨模态交互鲁棒性。

## 💡 核心创新

1. AVRCA 双向循环一致性约束强化视听空间语义
2. TCMM 时序跨模态记忆融合历史上下文
3. 面向听觉盲区的动态特征增强机制

## 🏗️ 模型架构

输入为视觉观测（RGB-D）与双耳音频频谱特征。主干采用视觉编码器与音频编码器分别提取模态特征，核心模块 AVRCA 通过视觉→音频、音频→视觉双向重建与循环一致性损失对齐语义空间；TCMM 以记忆单元动态聚合实时增强特征与历史上下文。融合特征送入导航策略网络输出动作，摘要未给出参数量。

## 📚 数据集

- Replica（评估，具身导航基准）
- Matterport3D（评估，真实场景重建基准）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SR | Replica / Matterport3D | 此前音频-视觉导航方法（摘要未给具体值） | **摘要未给具体数值** | 优于基线 |

摘要仅声明在 Replica 与 Matterport3D 上于 SR、SPL、SNA 三项指标优于此前音频-视觉导航方法，未给出具体数值、消融实验、推理延迟或跨数据集泛化结果，实验细节需查阅正文。

## 🎯 结论与影响

最强结论是双向循环一致性加时序记忆可有效提升视听导航的语义融合质量。若结果可复现，该融合范式可迁移至其他视听具身任务；工业上对服务机器人声源定位导航有参考价值，但需验证真实环境鲁棒性。

## ⚠️ 局限与未解决问题

摘要未提供任何定量结果、消融与效率指标，无法判断各模块贡献；Replica 与 Matterport3D 均为仿真环境，缺乏真实机器人验证；与最新视听导航基线的对比完整性未知。

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：6.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-16/">← 返回 2026-09-16 速递</a></div>
