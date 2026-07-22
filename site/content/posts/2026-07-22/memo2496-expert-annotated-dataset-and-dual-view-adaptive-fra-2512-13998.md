---
title: "Memo2496: Expert-Annotated Dataset and Dual-view Adaptive Framework for Music Emotion Recognition"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音乐情感识别"]
summary: "提出含2,496首器乐轨道的专家标注情感数据集Memo2496，以及双流自适应框架DAMER，在三个数据集上取得最优或竞争性结果。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音乐情感识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐情感识别</span> <span class="tag-pill tag-pill-soft">#双流注意力融合</span> <span class="tag-pill tag-pill-soft">#课程学习</span> <span class="tag-pill tag-pill-soft">#对比学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.13998</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.13998" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.13998" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出含2,496首器乐轨道的专家标注情感数据集Memo2496，以及双流自适应框架DAMER，在三个数据集上取得最优或竞争性结果。
</div>

## 👥 作者与机构

**Qilin Li** ¹ · C. L. Philip Chen · Tong Zhang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐信息检索、情感计算方向的研究者。建议重点阅读§3的DAMER框架（DSAF、PCL、SAML模块）和§4的实验结果（表1-3及消融实验）。可复现代码已开源。

## 🌍 研究背景

音乐情感识别（MER）受限于专家标注数据稀缺和跨语料库泛化能力不足。现有数据集如PMEmo、1000songs规模有限且标注一致性差。主流方法多基于单一特征（如Mel谱）和简单分类器，难以捕捉音乐中的复杂情感变化。本文旨在提供高质量标注数据集和鲁棒的多视角融合框架。

## 💡 核心创新

1. 构建2,496首器乐轨道的连续效价-唤醒度专家标注数据集Memo2496
2. 双流注意力融合（DSAF）实现Mel谱与耳蜗图token级交互
3. 渐进式置信标注（PCL）基于温度调度和JS散度的课程伪标签
4. 风格锚定记忆学习（SAML）利用标注对比队列正则化同情感嵌入

## 🏗️ 模型架构

输入为Mel谱和耳蜗图双流特征，经DSAF模块进行token级双向注意力融合；融合特征送入分类/回归头。PCL模块在训练中逐步生成伪标签并调整置信度；SAML模块维护标注对比队列，通过对比学习拉近同情感样本嵌入。整体框架端到端训练。

## 📚 数据集

- Memo2496（2,496首器乐轨道，30位专家标注连续效价-唤醒度，用于训练和评估）
- 1000songs（1,000首歌曲，用于外部评估）
- PMEmo（794首歌曲，用于外部评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 唤醒度准确率 | Memo2496 | 未明确给出具体值 | **最高** | 未明确 |
| 唤醒度准确率 | 1000songs | 未明确给出具体值 | **最高** | 未明确 |
| 效价准确率 | PMEmo | 未明确给出具体值 | **最高** | 未明确 |

DAMER在Memo2496和1000songs上唤醒度准确率最高，在PMEmo上效价准确率最高且唤醒度具有竞争力。消融实验验证了DSAF、PCL、SAML各模块的有效性。补充回归实验展示了Memo2496连续情感标签的直接使用。

## 🎯 结论与影响

本文通过高质量数据集Memo2496和双流自适应框架DAMER，显著提升了音乐情感识别的性能，尤其在唤醒度上表现突出。该工作为MER提供了标准化基准和可复现框架，有望推动跨语料库情感分析研究。数据集和代码开源有利于工业应用。

## ⚠️ 局限与未解决问题

数据集仅包含器乐轨道，缺乏人声；情感标注为连续值但主要评估采用二分类协议；未报告模型参数量和推理速度；与现有方法的对比不够全面（缺少近年基于Transformer的MER方法）。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-22/">← 返回 2026-07-22 速递</a></div>
