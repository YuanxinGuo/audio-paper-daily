---
title: "Cross-lingual Retrieval-Augmented Classification for Dysarthria Severity Assessment"
date: 2026-06-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音障碍评估"]
summary: "提出跨语言检索增强分类方法，利用另一种语言的语音数据提升构音障碍严重度评估性能。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音障碍评估</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#跨语言迁移</span> <span class="tag-pill tag-pill-soft">#检索增强</span> <span class="tag-pill tag-pill-soft">#对比学习</span> <span class="tag-pill tag-pill-soft">#构音障碍严重度评估</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.22910</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.22910" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.22910" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出跨语言检索增强分类方法，利用另一种语言的语音数据提升构音障碍严重度评估性能。
</div>

## 👥 作者与机构

**Taeyoung Jeong** ¹ · Insung Lee · Du-Seong Chang · Myoung-Wan Koo

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音障碍评估、跨语言迁移学习方向的研究者阅读。建议重点看§3的align-retrieve-fuse流程和§4的实验结果，尤其是表1的跨语言提升效果。

## 🌍 研究背景

构音障碍严重度自动评估面临标注病理语音数据稀缺的挑战，现有方法多局限于单语言场景。之前的工作主要使用单语言数据集训练分类器，跨语言泛化能力差。本文旨在利用另一种语言（如韩语和意大利语）的语音数据，通过检索增强来弥补目标语言数据不足的问题。

## 💡 核心创新

1. 提出align-retrieve-fuse跨语言检索增强流水线
2. 使用监督对比学习构建严重度感知的嵌入空间
3. 跨注意力机制融合检索到的跨语言参考特征
4. 在韩语和意大利语数据集上验证跨语言迁移有效性

## 🏗️ 模型架构

输入语音特征（如MFCC）→ 编码器（基于对比学习预训练）生成嵌入；构建跨语言向量数据库；分类器包含检索模块（从数据库中检索top-k相似嵌入）和融合模块（通过跨注意力将输入嵌入与检索嵌入融合），最终输出三个严重度类别的概率。

## 📚 数据集

- Korean post-stroke dysarthria dataset（训练/评估，三分类）
- Italian ALS dysarthria dataset（训练/评估，三分类）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Balanced Accuracy | Korean post-stroke | Monolingual baseline 78.9% | **87.3%** | +8.4% |
| Balanced Accuracy | Italian ALS | Monolingual baseline 66.7% | **86.7%** | +20.0% |

在说话人独立的三分类协议下，CRAC在韩语数据集上达到87.3%的平衡准确率，比单语言基线提升8.4个百分点；在意大利语数据集上达到86.7%，提升20.0个百分点。结果表明跨语言检索增强能有效缓解标注数据稀缺问题，且提升幅度显著。

## 🎯 结论与影响

本文提出的CRAC方法通过跨语言检索增强，显著提升了构音障碍严重度评估的准确率，尤其在目标语言数据稀缺时效果突出。该方法为低资源病理语音分析提供了新思路，有望推动多语言临床评估系统的开发。

## ⚠️ 局限与未解决问题

仅使用了两种语言（韩语和意大利语），跨语言泛化性需更多语言验证；未报告模型参数量和推理速度；检索库的构建依赖另一语言的有标注数据，实际应用中可能仍存在数据获取困难。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-23/">← 返回 2026-06-23 速递</a></div>
