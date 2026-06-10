---
title: "ERM-MinMaxGAP: Benchmarking and Mitigating Gender Bias in Multilingual Multimodal Speech-LLM Emotion Recognition"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音情感识别"]
summary: "提出多语言多模态情感识别性别偏见基准，并设计ERM-MinMaxGAP方法缓解偏见，在Qwen2-Audio上提升性能并缩小性别差距。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#性别偏见</span> <span class="tag-pill tag-pill-soft">#多语言</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#公平性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.21050</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.21050" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.21050" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出多语言多模态情感识别性别偏见基准，并设计ERM-MinMaxGAP方法缓解偏见，在Qwen2-Audio上提升性能并缩小性别差距。
</div>

## 👥 作者与机构

**Zi Haur Pang** ¹ · Xiaoxue Gao · Tatsuya Kawahara · Nancy F. Chen ✉

**机构**：新加坡科技研究局（A*STAR） · 京都大学 · 新加坡国立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音情感识别、公平性研究的读者。建议重点阅读§3（基准构建）和§4（ERM-MinMaxGAP方法），以及表2/3的性能与偏见结果。可先看摘要和结论判断相关性。

## 🌍 研究背景

语音情感识别（SER）系统常表现出性别相关的性能差异，但多语言语音大模型（LLM）中这种偏见如何跨语言和模态表现尚不明确。现有研究多聚焦单语言或单模态，缺乏多语言多模态的性别偏见基准。本文旨在量化并缓解多语言多模态SER中的性别偏见。

## 💡 核心创新

1. 构建多语言多模态SER性别偏见基准（MELD-ST扩展）
2. 提出自适应公平性权重机制
3. 设计MinMaxGAP正则化器约束最大性别损失差距
4. 在Qwen2-Audio上实现统一的多语言多模态公平性训练

## 🏗️ 模型架构

输入：多语言（英/日/德）语音和文本特征。主干：Qwen2-Audio多模态语音大模型。关键模块：ERM-MinMaxGAP训练目标，包含自适应公平性权重（根据语言和模态调整）和MinMaxGAP正则化（最小化各语言各模态内男女最大损失差距）。输出：情感类别概率。

## 📚 数据集

- MELD-ST（多语言扩展，含英语/日语/德语，训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 加权准确率（W-Acc） | MELD-ST多语言 | ERM基线（未公开具体值） | **ERM-MinMaxGAP** | +5.5%（单模态）/+5.0%（多模态） |
| 性别偏见差距（最大男女损失差） | MELD-ST多语言 | ERM基线 | **ERM-MinMaxGAP** | -0.1%（单模态）/-1.4%（多模态） |

实验表明，性别偏见强烈依赖于语言，多模态融合并未可靠改善公平性。ERM-MinMaxGAP在单模态和多模态设置下分别提升SER性能5.5%和5.0%，同时将性别偏见差距缩小0.1%和1.4%。消融实验验证了自适应权重和MinMaxGAP正则化的有效性。

## 🎯 结论与影响

本文揭示了多语言多模态SER中性别偏见的语言依赖性，并提出ERM-MinMaxGAP方法有效缓解偏见。该工作为公平性SER研究提供了多语言基准和实用训练框架，有望推动语音大模型在跨语言场景下的公平部署。

## ⚠️ 局限与未解决问题

仅基于MELD-ST数据集，语言和情感类别有限；未报告推理效率或模型大小；未与其他公平性方法（如对抗训练）对比；性别偏见仅考虑二元性别，未涵盖非二元性别。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
