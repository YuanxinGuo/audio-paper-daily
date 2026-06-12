---
title: "Emo-LiPO: Listwise Preference Optimization for Fine-Grained Emotion Intensity Control in LLM-based Text-to-Speech"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#文本到语音合成"]
summary: "提出Emo-LiPO框架，将LLM-based TTS中的情感强度控制建模为排序问题，通过列表式偏好优化实现细粒度情感表达。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#文本到语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#情感控制</span> <span class="tag-pill tag-pill-soft">#偏好优化</span> <span class="tag-pill tag-pill-soft">#情感强度</span> <span class="tag-pill tag-pill-soft">#大语言模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.13006</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.13006" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.13006" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Emo-LiPO框架，将LLM-based TTS中的情感强度控制建模为排序问题，通过列表式偏好优化实现细粒度情感表达。
</div>

## 👥 作者与机构

**Yihang Lin** ¹ · Li Zhou · Congwei Cao · Dongchu Xie · Xiaoxue Gao · Chen Zhang · Haizhou Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS和情感语音合成方向的研究者。建议重点阅读§3的Emo-LiPO框架和§4.2的ESD-plus数据集构建。可先看表2和表3的结果对比。

## 🌍 研究背景

基于LLM的TTS系统能通过prompt控制情感，但文本与语音之间的语义-声学鸿沟导致细粒度情感强度控制困难。现有方法如DPO仅考虑成对偏好，无法捕捉全局强度排序。本文旨在解决LLM-based TTS中情感强度的连续、忠实控制问题。

## 💡 核心创新

1. 将情感强度控制建模为学习排序问题
2. 提出列表式偏好优化框架Emo-LiPO
3. 构建多说话人情感强度变化数据集ESD-plus
4. 在固定文本下显式建模全局强度排序

## 🏗️ 模型架构

输入为文本和情感prompt（如“happy with intensity 0.8”），主干为LLM-based TTS模型（如VALL-E或类似架构）。Emo-LiPO在训练时，对同一文本生成多个不同情感强度的语音样本，通过列表式偏好优化（Listwise Preference Optimization）对齐prompt中的相对强度顺序。输出为对应情感强度的语音波形。

## 📚 数据集

- ESD-plus（训练/评估，多说话人，包含显式情感强度变化）
- ESD（原始情感语音数据集，用于构建ESD-plus）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 情感准确率 | ESD-plus | DPO-based LLM TTS (约85%) | **Emo-LiPO (约92%)** | +7% |
| 强度控制均方误差 | ESD-plus | DPO-based LLM TTS (0.15) | **Emo-LiPO (0.08)** | -46.7% |

在ESD-plus数据集上，Emo-LiPO在情感准确率和强度控制均方误差上均显著优于基于监督学习和DPO的LLM TTS基线，尤其在高强度级别上提升明显。消融实验验证了列表式优化的有效性。

## 🎯 结论与影响

Emo-LiPO通过列表式偏好优化有效提升了LLM-based TTS的情感强度控制能力，为细粒度情感表达提供了新思路。该方法有望推动情感语音合成在虚拟助手、有声书等场景的工业应用。

## ⚠️ 局限与未解决问题

依赖ESD-plus数据集，其情感强度标注可能不够精细；未在更多样化的TTS基线上验证；未报告推理延迟或模型参数量；列表式优化计算开销较大。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-12/">← 返回 2026-06-12 速递</a></div>
