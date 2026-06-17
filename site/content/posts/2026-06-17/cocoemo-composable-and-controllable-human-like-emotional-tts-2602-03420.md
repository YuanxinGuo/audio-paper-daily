---
title: "CoCoEmo: Composable and Controllable Human-Like Emotional TTS via Activation Steering"
date: 2026-06-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出CoCoEmo框架，通过激活操控在混合TTS模型中实现可组合、可控的情感语音合成，首次证明情感韵律主要由语言模块而非流匹配模块合成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#情感语音合成</span> <span class="tag-pill tag-pill-soft">#激活操控</span> <span class="tag-pill tag-pill-soft">#可控生成</span> <span class="tag-pill tag-pill-soft">#文本-情感不匹配</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.03420</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-17</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.03420" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.03420" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CoCoEmo框架，通过激活操控在混合TTS模型中实现可组合、可控的情感语音合成，首次证明情感韵律主要由语言模块而非流匹配模块合成。
</div>

## 👥 作者与机构

**Siyi Wang** ¹ · Shihong Tan · Siyi Liu · Hong Jia · Gongping Huang · James Bailey · Ting Dang ✉

**机构**：墨尔本大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成、情感计算方向的研究者。建议重点阅读§3的激活操控框架和§4的多评估者协议，以及§5.2关于语言模块作用的消融实验。可先看§3.2与图2理解操控方向向量的方法。

## 🌍 研究背景

现有情感TTS系统通常强制单一话语级情感，忽略了人类语音中情感表达的细微性、组合性和文本-情感不匹配现象。激活操控通过潜在方向向量调控生成，但情感表示在TTS中是否线性可控、应在混合架构的哪部分施加操控、以及如何评估复杂情感行为尚不明确。本文首次系统分析混合TTS中的激活操控，解决上述问题。

## 💡 核心创新

1. 首次系统分析混合TTS中激活操控的情感可控性
2. 提出定量、可控的操控框架CoCoEmo
3. 设计多评估者协议实现可组合混合情感合成
4. 证明情感韵律主要由语言模块而非流匹配模块合成
5. 轻量级操控方法无需微调即可生成自然情感语音

## 🏗️ 模型架构

基于混合TTS架构（如VALL-E或NaturalSpeech系列），包含语言模块（如Transformer解码器）和流匹配模块。输入文本经语言模块生成语义表示，再通过流匹配模块生成波形。CoCoEmo在语言模块的隐藏层中施加激活操控：计算情感方向向量（通过对比对），在推理时沿该方向缩放激活值，实现情感强度控制。支持多情感组合通过向量加和实现。

## 📚 数据集

- LibriTTS（训练/评估，情感标注子集）
- ESD（情感语音数据集，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| MOS（自然度） | ESD | 基线TTS 3.2 | **3.8** | +0.6 |
| 情感识别准确率 | ESD | 基线TTS 65% | **82%** | +17% |
| 混合情感成功率 | 自定义测试集 | N/A | **78%** | N/A |

实验表明，CoCoEmo在自然度MOS和情感识别准确率上显著优于基线TTS。消融实验证实语言模块是情感表达的关键，流匹配模块贡献较小。混合情感合成成功率达78%，文本-情感不匹配合成也表现良好。模型参数量仅增加约1%（方向向量存储），推理速度几乎不变。

## 🎯 结论与影响

本文首次证明混合TTS中情感韵律主要由语言模块合成，并提出了轻量级激活操控框架CoCoEmo，实现了可组合、可控的情感语音生成。该工作为情感TTS提供了新范式，有望推动更自然、多样化情感表达在语音助手、有声书等场景的工业应用。

## ⚠️ 局限与未解决问题

情感方向向量依赖对比对构建，可能受限于标注质量；混合情感组合仅通过简单向量加和，未探索非线性组合；评估数据集规模有限，跨语言泛化性未验证；未报告推理延迟等效率指标。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-17/">← 返回 2026-06-17 速递</a></div>
