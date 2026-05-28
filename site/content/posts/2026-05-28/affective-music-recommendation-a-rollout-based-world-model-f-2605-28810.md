---
title: "Affective Music Recommendation: A Rollout-Based World Model for Offline Preference Optimization"
date: 2026-05-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐推荐"]
summary: "提出基于rollout世界模型的AMRS系统，用于情感音乐推荐，通过离线DPO优化多目标效用函数，在临床和消费场景中验证。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#情感计算</span> <span class="tag-pill tag-pill-soft">#离线偏好优化</span> <span class="tag-pill tag-pill-soft">#世界模型</span> <span class="tag-pill tag-pill-soft">#强化学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.28810</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.28810" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.28810" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于rollout世界模型的AMRS系统，用于情感音乐推荐，通过离线DPO优化多目标效用函数，在临床和消费场景中验证。
</div>

## 👥 作者与机构

**Audrey Chan** ¹ · Aaron Labb\'e · Jacob Lavoie · Jordan Bannister · Ars\`ene Fansi Tchango · Guillaume Lajoie · Laurent Charlin

**机构**：LUCID · 蒙特利尔大学 · Mila

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合推荐系统、情感计算和强化学习研究者阅读。重点看§3世界模型架构和§4离线优化方法。可先看实验部分（§5）了解实际效果。

## 🌍 研究背景

功能性音乐应用（如专注、助眠、临床干预）需要根据听众情感状态推荐音乐，但在线情感实验存在伦理约束，尤其对临床人群。现有推荐系统多依赖显式反馈，难以直接优化情感状态。本文提出AMRS系统，利用离线日志数据训练世界模型，模拟用户情感和行为反应，从而在无在线实验条件下优化推荐策略。

## 💡 核心创新

1. 基于因果Transformer的rollout世界模型，联合预测行为与情感信号
2. 离线DPO优化多目标效用函数，避免分布崩塌
3. 严格冷启动协议下验证世界模型预测保真度
4. 在临床和消费平台部署，验证方法论可行性

## 🏗️ 模型架构

输入特征包括用户历史交互、歌曲特征和上下文（如模式标签）。主干网络为因果Transformer，训练目标为预测下一时刻的engagement、binary rating、valence和arousal。世界模型作为模拟器，用于离线策略训练和部署前压力测试。推荐策略先通过行为克隆初始化，再使用DPO离线微调，优化可配置的多目标效用函数。

## 📚 数据集

- LUCID平台日志数据（训练世界模型，包含临床和消费用户）
- 冷启动测试集（评估世界模型预测能力）

## 📊 实验结果

摘要未提供具体数值指标，但声称世界模型在冷启动协议下能有效预测行为与情感信号；DPO优化相比行为克隆基线提升了预测的valence和arousal，同时保持多样性，避免了贪婪优化导致的分布崩塌。

## 🎯 结论与影响

本文展示了在在线实验不可行时，基于rollout世界模型的离线偏好优化方法可用于情感音乐推荐。AMRS系统已在LUCID平台部署，验证了方法论的有效性。该工作为情感感知推荐系统的离线训练提供了实用框架，对临床和消费场景均有参考价值。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标；缺乏与在线A/B测试的对比；世界模型预测的准确性可能受日志数据偏差影响；未讨论不同情感维度（如valence/arousal）的权重设置对推荐结果的影响。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-05-28/">← 返回 2026-05-28 速递</a></div>
