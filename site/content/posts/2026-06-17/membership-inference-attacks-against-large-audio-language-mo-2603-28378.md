---
title: "Membership Inference Attacks against Large Audio Language Models"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频安全"]
summary: "首次系统评估大音频语言模型的成员推理攻击，提出盲基线协议控制分布偏移，发现记忆是跨模态的。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频安全</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#成员推理攻击</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#隐私审计</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.28378</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/snooow1029/ALM_MIA" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">snooow1029/ALM_MIA</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.28378" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.28378" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/snooow1029/ALM_MIA" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首次系统评估大音频语言模型的成员推理攻击，提出盲基线协议控制分布偏移，发现记忆是跨模态的。
</div>

## 👥 作者与机构

**Jia-Kai Dong** ¹ · Yu-Xiang Lin · Hung-Yi Lee ✉

**机构**：台湾大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合关注AI安全、隐私审计的研究者。建议通读，重点看§3盲基线协议和§4.2模态解耦实验。可复现其代码库。

## 🌍 研究背景

成员推理攻击（MIA）用于检测模型是否记忆了特定训练样本，对隐私审计至关重要。然而，现有MIA评估在音频领域尚未系统化，且常因训练/测试分布差异导致虚假高成功率。本文首次针对大音频语言模型（LALM）进行MIA评估，发现常见音频数据集存在近乎完美的可分性（AUC~1.0），因此提出盲基线协议以控制分布偏移，并揭示LALM的记忆机制。

## 💡 核心创新

1. 首次系统评估LALM的MIA
2. 提出多模态盲基线（文本/频谱/韵律）
3. 引入盲基线协议控制分布偏移
4. 模态解耦实验揭示跨模态记忆
5. 建立LALM隐私审计标准

## 🏗️ 模型架构

本文不提出新模型架构，而是评估框架。使用多种MIA方法（如损失、置信度、参考模型）攻击预训练LALM（如AudioGPT、LTU）。盲基线基于文本（ASR转录）、频谱（Mel谱）和韵律（F0、能量）特征训练二分类器，无需模型推理。分布匹配数据集通过重采样或合成实现。

## 📚 数据集

- LibriSpeech（训练/评估，用于ASR任务）
- VoxCeleb（训练/评估，用于说话人识别）
- AudioCaps（训练/评估，用于音频字幕）
- Clotho（训练/评估，用于音频字幕）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| AUC | LibriSpeech | 盲基线（文本）0.99 | **MIA方法（损失）0.98** | -0.01 |
| AUC | VoxCeleb | 盲基线（频谱）1.00 | **MIA方法（损失）0.99** | -0.01 |

实验表明，常见音频数据集上盲基线AUC接近1.0，说明分布偏移主导MIA。使用分布匹配数据集后，MIA AUC降至0.6-0.7，但仍显著高于随机。模态解耦显示，仅当说话人身份与文本绑定（如ASR任务）时记忆才出现，纯音频或纯文本任务无记忆。

## 🎯 结论与影响

本文首次系统评估LALM的MIA，揭示了分布偏移的混淆效应，并提出盲基线协议作为标准。核心发现是LALM的记忆是跨模态的，源于语音身份与文本的绑定。这为未来LALM隐私审计提供了方法论基础，并提示工业部署需关注多模态记忆风险。

## ⚠️ 局限与未解决问题

仅评估了有限数量的LALM和数据集，未覆盖所有主流模型。盲基线协议依赖特征选择，可能遗漏其他分布偏移。未探讨防御机制（如差分隐私）。计算开销未报告。

## 🔗 开源资源

- **代码**：<https://github.com/snooow1029/ALM_MIA>

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
