---
title: "MultiAPI Spoof: A Multi-API Dataset and Local-Attention Network for Speech Anti-spoofing Detection"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音反欺骗"]
summary: "提出MultiAPI Spoof多API语音反欺骗数据集（230小时，30个API），并设计Nes2Net-LA局部注意力网络提升检测鲁棒性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音反欺骗</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音反欺骗</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#局部注意力</span> <span class="tag-pill tag-pill-soft">#API追踪</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2512.07352</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/XuepingZhang/MultiAPI-Spoof" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">XuepingZhang/MultiAPI-Spoof</span></span></a><a class="oc-chip oc-chip-proj" href="https://xuepingzhang.github.io/MultiAPI-Spoof-Dataset/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">xuepingzhang.github.io/MultiAPI-Spoof-Dataset/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2512.07352" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2512.07352" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/XuepingZhang/MultiAPI-Spoof" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://xuepingzhang.github.io/MultiAPI-Spoof-Dataset/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MultiAPI Spoof多API语音反欺骗数据集（230小时，30个API），并设计Nes2Net-LA局部注意力网络提升检测鲁棒性。
</div>

## 👥 作者与机构

**Xueping Zhang** ¹ · Zhenshan Zhang · Yechen Wang · Linxi Li · Liwei Jin · Ming Li ✉

**机构**：武汉大学 · 昆山杜克大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音反欺骗、音频伪造检测方向的研究者。建议通读，重点看§3数据集构建和§4.2模型架构。可先复现代码并评估在自有API上的泛化性。

## 🌍 研究背景

现有语音反欺骗基准仅依赖少量公开模型，与真实场景中商用系统使用多样私有API的现状存在巨大差距。之前SOTA方法在有限数据集上表现良好，但面对未知伪造源时鲁棒性不足。本文旨在构建覆盖多API的合成语音数据集，并设计能捕捉细粒度伪造特征的网络。

## 💡 核心创新

1. 构建230小时、30个API的多源合成语音数据集MultiAPI Spoof
2. 提出Nes2Net-LA，引入局部注意力增强局部上下文建模
3. 定义API追踪任务，实现伪造音频的细粒度溯源

## 🏗️ 模型架构

输入为语音频谱特征，主干网络基于Nes2Net（一种轻量级CNN），关键改进是在特定层插入局部注意力模块（Local-Attention），增强对局部伪造痕迹的捕捉。输出为二分类（真/假）或API类别（追踪任务）。模型参数量未明确给出。

## 📚 数据集

- MultiAPI Spoof（训练/评估，230小时，30个API）
- ASVspoof 2019 LA（评估，用于跨数据集泛化测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| EER (%) | MultiAPI Spoof (unseen APIs) | AASIST 8.12 | **Nes2Net-LA 6.45** | -1.67% |
| tDCF | MultiAPI Spoof (unseen APIs) | AASIST 0.312 | **Nes2Net-LA 0.245** | -0.067 |

在MultiAPI Spoof数据集上，Nes2Net-LA在未见过的API条件下EER为6.45%，优于AASIST的8.12%；tDCF为0.245，优于0.312。在ASVspoof 2019 LA上，Nes2Net-LA也取得有竞争力的结果，表明跨数据集泛化能力。消融实验验证了局部注意力模块的有效性。

## 🎯 结论与影响

本文提出的MultiAPI Spoof数据集和Nes2Net-LA网络显著提升了语音反欺骗在多样伪造源下的鲁棒性，并开创了API追踪新任务。该工作为构建更贴近真实场景的检测系统提供了数据和方法基础，有望推动工业级反欺骗系统的部署。

## ⚠️ 局限与未解决问题

数据集仅包含30个API，可能未覆盖所有商用服务；未报告模型推理延迟和参数量；API追踪任务仅评估了分类准确率，未考虑开放集场景；未与更近期的基线如RawNet3等对比。

## 🔗 开源资源

- **代码**：<https://github.com/XuepingZhang/MultiAPI-Spoof>
- **项目主页**：<https://xuepingzhang.github.io/MultiAPI-Spoof-Dataset/>
- **数据集**：<https://xuepingzhang.github.io/MultiAPI-Spoof-Dataset/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
