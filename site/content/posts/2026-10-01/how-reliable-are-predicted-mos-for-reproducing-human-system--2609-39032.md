---
title: "How Reliable Are Predicted MOS for Reproducing Human System-Level Preferences in Speech Enhancement?"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出系统级偏好准确率SPA，衡量MOS预测模型能否复现人类对语音增强系统的偏好排序，发现单模型SPA从9.4%到76.8%差异巨大。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#MOS预测</span> <span class="tag-pill tag-pill-soft">#评价指标</span> <span class="tag-pill tag-pill-soft">#域适应</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.39032</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.39032" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.39032" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出系统级偏好准确率SPA，衡量MOS预测模型能否复现人类对语音增强系统的偏好排序，发现单模型SPA从9.4%到76.8%差异巨大。
</div>

## 👥 作者与机构

**Nahomi Kusunoki** ¹ · Tsubasa Ochiai · Naohiro Tawara · Marc Delcroix · Naoyuki Kamo · Tetsuji Ogawa · Shoko Araki

**机构**：日本电信电话公司 · 早稻田大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音增强评测、MOS预测与主观评价的研究者与工程评测人员阅读。建议通读，重点看SPA定义一节与单模型/集成/域适应三组实验的对比表，以及开放条件下的结果分析。若只关心结论，可先看摘要与开放条件实验小节。

## 🌍 研究背景

语音增强系统评价长期依赖MOS预测模型，主流做法是看预测MOS与人类MOS的相关性（如PLCC/SRCC），SOTA模型在相关性上已很高。但相关性高并不保证预测模型与人类在“哪个系统更好”上一致，系统级排序错误会直接误导模型选型。本文要解决的具体问题是：预测MOS能否可靠支撑语音增强系统级比较，并提出SPA来量化这一能力。

## 💡 核心创新

1. 提出系统级偏好准确率SPA，直接衡量预测与人类MOS的系统排序一致性
2. 系统评估单模型、集成、域适应三种设置下的SPA表现
3. 揭示相关性评价无法暴露的系统级偏好错误

## 🏗️ 模型架构

本文为评价方法研究，无新增强网络。流程为：给定多个语音增强系统输出，分别用人类主观听测与多个MOS预测模型打分；对每对系统比较预测MOS与人类MOS给出的偏好是否一致，统计一致比例得到SPA。实验覆盖单预测模型、多模型集成、以及域适应三种设置，并在封闭条件（目标系统与说话人已知）与开放条件（均未知）下分别评估。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SPA | 系统级比较（摘要未指明具体测试集） | 单MOS预测模型最低9.4% | **单MOS预测模型最高76.8%** | 跨模型差异达67.4个百分点 |
| SPA | 系统级比较（摘要未指明具体测试集） | 最佳单模型与人类不一致约23% | **集成仅有限提升** | 集成提升有限 |
| SPA | 封闭条件 vs 开放条件 | 开放条件域适应增益有限 | **封闭条件域适应显著提升** | 封闭条件提升明显，开放条件增益有限 |

摘要给出SPA在单预测模型间从9.4%到76.8%大幅波动，最佳模型仍在约23%的系统比较中与人类判断不一致。集成方法仅带来有限改进；域适应在封闭条件下显著提升SPA，但在目标系统与说话人均未知的开放条件下增益有限。摘要未给出具体数据集名称、相关系数或推理开销等细节。

## 🎯 结论与影响

最强结论是：预测MOS单独用于语音增强系统比较可能得出不可靠结论，SPA能暴露相关性评价掩盖的系统级偏好错误。该工作提示后续MOS预测研究应把系统级排序一致性纳入评价，工业评测流程中不宜仅凭预测MOS选型，需辅以主观验证或SPA类指标。

## ⚠️ 局限与未解决问题

摘要未说明所用语音增强系统集合、测试语料与听测规模，SPA的统计稳定性未知；未报告预测模型推理成本；开放条件下域适应增益有限，说明实用场景仍难解决；缺少与其它排序一致性指标的对比分析。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
