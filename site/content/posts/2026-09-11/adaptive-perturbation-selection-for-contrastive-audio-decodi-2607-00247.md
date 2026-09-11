---
title: "Adaptive Perturbation Selection for Contrastive Audio Decoding"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频理解"]
summary: "为大音频语言模型设计自适应扰动选择策略，通过时域/频域/幅度扰动构造负分支，缓解幻觉。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#对比解码</span> <span class="tag-pill tag-pill-soft">#大音频语言模型</span> <span class="tag-pill tag-pill-soft">#幻觉缓解</span> <span class="tag-pill tag-pill-soft">#提示工程</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.00247</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.00247" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.00247" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>为大音频语言模型设计自适应扰动选择策略，通过时域/频域/幅度扰动构造负分支，缓解幻觉。
</div>

## 👥 作者与机构

**Aaron Isidore Grace** ¹ · Zhouyuan Huo · Weiran Wang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做大音频语言模型（LALM）幻觉缓解与对比解码的研究者阅读。建议重点看扰动库构建（时域/频域/幅度）与轻量选择器的设计，以及表 2 中不同任务的最优扰动对比。若只关心语音增强/分离，可略读。

## 🌍 研究背景

大音频语言模型（LALM）常因语言先验压过声学证据而产生幻觉。现有对比解码（CD）方法多采用掩码或加噪等粗糙扰动构造负分支，未系统探索结构化音频变换。本文要回答：不同任务下哪种扰动最有效，并能否按样本自适应选择最优负分支。

## 💡 核心创新

1. 系统评估时域/频域/幅度等多域扰动库
2. 用二元 yes/no 约束减少虚假确认
3. 训练轻量选择器按隐状态动态路由负分支

## 🏗️ 模型架构

输入为音频与文本提示，主干为现成大音频语言模型（LALM）。方法不修改主干，而是在解码阶段构造正/负分支：对音频施加时域反转、频谱扰动、频率滤波、幅度缩放等变换得到负样本。轻量选择器以模型隐状态为输入，预测每个样本应使用哪种扰动分支，再结合对比解码打分输出最终文本。

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | temporal order task | 原始音频 74.7% | **音频反转 81.4%** | +6.7% |
| Accuracy | existence task | 无选择器 | **加选择器** | +4.3% |

摘要给出两个具体数字：时域反转将 temporal order 任务准确率从 74.7% 提升到 81.4%；轻量选择器在 existence 任务上额外带来 +4.3% 增益。其余扰动库对比、消融与跨任务泛化细节未在摘要中给出，需查阅正文。

## 🎯 结论与影响

最强结论是：最优音频扰动高度任务相关，且可用轻量选择器按样本自适应路由。这为 LALM 幻觉缓解提供了免训练+轻量微调的实用范式，对工业界部署低幻觉音频对话系统有参考价值。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与选择器参数量；扰动库覆盖范围与任务类型有限；未与更多 CD 基线在统一设置下全面对比；选择器依赖隐状态，跨模型迁移性未知。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
