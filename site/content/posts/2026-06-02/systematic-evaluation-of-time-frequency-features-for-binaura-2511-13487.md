---
title: "Systematic Evaluation of Time-Frequency Features for Binaural Sound Source Localization"
date: 2026-06-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声源定位"]
summary: "系统评估双耳声源定位中时频特征组合对CNN性能的影响，发现精心选择的特征组合可超越增加模型复杂度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声源定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#特征工程</span> <span class="tag-pill tag-pill-soft">#卷积神经网络</span> <span class="tag-pill tag-pill-soft">#泛化分析</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.13487</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.13487" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.13487" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>系统评估双耳声源定位中时频特征组合对CNN性能的影响，发现精心选择的特征组合可超越增加模型复杂度。
</div>

## 👥 作者与机构

**Davoud Shariat Panah** ¹ · Alessandro Ragano · Dan Barry · Jan Skoglund · Andrew Hines

**机构**：都柏林大学学院 · 谷歌

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事双耳声源定位或空间音频特征设计的读者。重点看§3特征组合实验和§4.2跨域泛化结果。可跳过§2背景。

## 🌍 研究背景

双耳声源定位（SSL）是空间音频的核心任务，传统方法依赖手工特征如ILD和IPD，近年深度学习模型直接学习原始波形或频谱。然而，特征选择对模型性能的影响缺乏系统研究，尤其在跨HRTF和跨内容泛化场景下。本文旨在填补这一空白，系统评估幅度和相位特征组合对CNN定位精度的影响。

## 💡 核心创新

1. 系统评估幅度和相位特征组合对SSL性能的影响
2. 发现ILD+IPD双特征集在域内足够，但跨域需更丰富输入
3. 低复杂度CNN使用最优特征集达到竞争性能
4. 提供跨HRTF和跨内容泛化的实用指导

## 🏗️ 模型架构

输入为双耳音频的时频特征组合（幅度谱、ILD、相位谱、IPD等），送入2D卷积神经网络（CNN），包含多个卷积层和全连接层，输出为方位角/仰角的分类或回归结果。模型复杂度低，参数量未明确给出。

## 📚 数据集

- CIPIC HRTF数据库（用于生成双耳信号，训练和评估）
- TIMIT数据集（语音内容，用于生成训练/测试信号）
- MUSAN数据集（噪声和音乐，用于生成测试信号）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率（Accuracy） | 域内测试集（CIPIC+TIMIT） | 全特征集（幅度+相位+ILD+IPD） | **ILD+IPD双特征集** | 性能相近，无显著差异 |
| 准确率（Accuracy） | 跨HRTF测试集（不同HRTF） | 单特征（如幅度谱） | **通道谱+ILD+IPD** | 显著提升，具体数值未给出 |

实验表明，在域内测试中，ILD+IPD双特征集即可达到与全特征集相当的精度；但在跨HRTF和跨内容泛化场景下，需要结合通道谱（左右声道幅度谱）与ILD、IPD才能获得最佳性能。低复杂度CNN使用最优特征集与更复杂模型性能相当。

## 🎯 结论与影响

本文系统评估了双耳SSL中时频特征设计的重要性，表明特征选择比模型复杂度更关键。研究为实际系统提供了特征选择指南：域内应用可用ILD+IPD，通用系统需更丰富输入。对工业落地有直接指导意义。

## ⚠️ 局限与未解决问题

仅使用单一CNN架构，未对比其他模型（如Transformer）；实验仅在模拟HRTF数据上进行，未验证真实录音；未报告推理延迟或计算量；跨域泛化测试中HRTF数量有限。

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：6.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-02/">← 返回 2026-06-02 速递</a></div>
