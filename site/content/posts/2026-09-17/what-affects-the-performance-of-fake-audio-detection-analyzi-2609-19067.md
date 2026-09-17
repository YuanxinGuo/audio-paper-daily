---
title: "What Affects the Performance of Fake Audio Detection? Analyzing Factors in a Continual Learning Setting"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "系统分析攻击者架构、训练数据、说话人多样性与任务顺序对持续学习下伪造音频检测性能的影响。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#持续学习</span> <span class="tag-pill tag-pill-soft">#音频深度伪造检测</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#鲁棒性分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.19067</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.19067" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.19067" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统分析攻击者架构、训练数据、说话人多样性与任务顺序对持续学习下伪造音频检测性能的影响。
</div>

## 👥 作者与机构

**Yixuan Xiao** ¹ · Ngoc Thang Vu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频深度伪造检测与持续学习的研究者阅读。建议重点看实验设置与结果分析章节，尤其是任务顺序与说话人多样性对三种检测模型、四种训练策略的敏感性对比。可先看攻击者训练数据集相关结论，再关注任务顺序实验设计，作为自身鲁棒性评估的参考清单。

## 🌍 研究背景

深度伪造音频生成技术日益成熟，检测系统需随时间适应新攻击。此前工作多聚焦单一攻击类型下的检测精度，常用 AASIST、RawNet2 等模型在 ASVspoof 等基准上评测，但很少系统考察持续学习场景中攻击者架构、攻击者训练数据、说话人多样性、任务顺序等因素如何影响检测性能。本文针对这一空白，在持续学习设定下量化这些因素的影响。

## 💡 核心创新

1. 系统解耦攻击者架构、训练数据、说话人多样性、任务顺序四类因素
2. 对比直接微调、单类分类、随机回放、LwF 四种持续学习策略
3. 发现伪造伪影主要源自攻击者训练数据集而非架构

## 🏗️ 模型架构

摘要未给出具体网络结构细节。实验使用三种检测模型，分别以四种策略训练：直接微调、单类分类、随机回放、Learning without Forgetting。输入为伪造/真实音频，输出为真伪判别。摘要未提及参数量、特征类型或主干网络名称，具体架构需查阅正文。

## 📚 数据集

- 摘要未指明具体数据集名称，仅提及攻击者训练数据集与说话人多样性设置

## 📊 实验结果

摘要未给出具体指标数值。结论性发现包括：伪造音频的伪影可能主要来自攻击者的训练数据集，仅改变攻击者架构不足以挑战检测系统；任务顺序与说话人多样性会显著影响性能，且不同检测模型与训练策略的敏感程度不同。

## 🎯 结论与影响

最强结论是攻击者训练数据集而非架构是伪造伪影的主要来源，且任务顺序与说话人多样性对持续学习检测性能影响显著。这提示后续研究在构建持续学习基准时需控制这些变量，工业部署中应关注数据分布漂移与任务顺序带来的性能波动。

## ⚠️ 局限与未解决问题

摘要未给出具体数据集、指标数值与消融细节，难以判断结论的统计显著性。未报告推理延迟与模型规模。三种检测模型与四种策略的组合虽广，但缺少对攻击者架构与训练数据交叉因素的定量分解，任务顺序实验的重复次数与方差也未说明。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-17/">← 返回 2026-09-17 速递</a></div>
