---
title: "Detect, Attend and Extract: Keyword Guided Target Speaker Extraction"
date: 2026-06-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出DAE-TSE框架，利用关键词（部分转录）作为线索提取目标说话人语音，无需干净注册语音。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.5</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#关键词引导</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#说话人提取</span> <span class="tag-pill tag-pill-soft">#部分转录</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.07977</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.07977" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.07977" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出DAE-TSE框架，利用关键词（部分转录）作为线索提取目标说话人语音，无需干净注册语音。
</div>

## 👥 作者与机构

**Haoyu Li** ¹ · Yu Xi · Yidi Jiang · Shuai Wang · Kate Knill · Mark Gales · Haizhou Li · Kai Yu

**机构**：上海交通大学 · 剑桥大学 · 新加坡国立大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合目标说话人提取、语音分离领域的研究者。建议通读，重点看§3的DAE范式设计和§4的实验对比。可先看表1和表2了解性能提升。

## 🌍 研究背景

目标说话人提取（TSE）通常依赖预注册的干净语音作为说话人线索，但在实际场景中，干净注册语音难以获取。现有方法受限于此，应用范围受限。本文提出利用关键词（部分转录）作为线索，提供更灵活的替代方案，解决注册语音不可用的问题。

## 💡 核心创新

1. 首次使用部分转录作为TSE线索
2. 提出Detect-Attend-Extract (DAE)范式
3. 关键词检测与说话人注意力结合
4. 无需干净注册语音，提升实用性

## 🏗️ 模型架构

DAE-TSE遵循Detect-Attend-Extract范式。输入为混合语音和关键词文本，首先通过关键词检测模块（基于预训练语音识别模型）检测关键词出现位置；然后注意力模块根据关键词内容生成说话人表征，引导提取网络；最后提取网络（基于Conformer或类似结构）输出目标说话人语音。

## 📚 数据集

- LibriMix（训练/评估，含多说话人混合）
- WSJ0-2mix（评估，2说话人混合）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi (dB) | Libri2Mix | SpEx+ (17.5) | **18.9** | +1.4 |
| PESQ | Libri2Mix | SpEx+ (3.12) | **3.28** | +0.16 |

在Libri2Mix和WSJ0-2mix上，DAE-TSE优于依赖干净注册语音的基线方法（如SpEx+），SI-SDRi提升约1.4 dB，PESQ提升0.16。消融实验验证了各模块的有效性，且关键词长度对性能影响较小。

## 🎯 结论与影响

本文首次证明部分转录可作为TSE的有效线索，DAE-TSE在无需注册语音的情况下超越传统方法，为实际场景提供灵活方案。后续可探索关键词选择策略和跨语言泛化，工业上可应用于智能音箱、会议系统等。

## ⚠️ 局限与未解决问题

依赖关键词的准确检测，在噪声环境下性能可能下降；仅验证了英文关键词；未报告推理延迟和模型参数量；与基于注册语音的方法在极端混响下的对比缺失。

---

<div class="paper-footer"><span>评分：9.5</span><span>原始：8.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-09/">← 返回 2026-06-09 速递</a></div>
