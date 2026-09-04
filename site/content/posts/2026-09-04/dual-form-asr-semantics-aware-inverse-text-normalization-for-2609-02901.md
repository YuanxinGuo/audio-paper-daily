---
title: "Dual-Form ASR: Semantics-Aware Inverse Text Normalization for Chinese Speech Recognition"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音识别"]
summary: "提出双形式ASR框架，通过成对口语/书面语监督和ITN-MWER损失，实现语义感知的逆文本正则化，提升中文ASR书面语输出的可读性。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#逆文本正则化</span> <span class="tag-pill tag-pill-soft">#语义感知</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#中文语音识别</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.02901</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.02901" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.02901" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双形式ASR框架，通过成对口语/书面语监督和ITN-MWER损失，实现语义感知的逆文本正则化，提升中文ASR书面语输出的可读性。
</div>

## 👥 作者与机构

**Fengrun Zhang** ¹ · Li Fu · Wangjin Zhou · Lu Fan · Youzheng Wu · Xiaodong He

**机构**：京东 · 中国科学院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音识别和文本正则化研究者阅读。建议重点阅读第3节（方法）和第4节（实验），特别是ITN-MWER损失和REQUIRE-ITN/FORBID-ITN评估协议。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

现代ASR系统需要同时输出口语形式和书面形式（经ITN处理），但传统级联方法将ASR和ITN分离，导致错误传播且无法利用声学上下文，尤其对语义相关的数字表达处理不佳。现有ITN方法多基于规则或独立模型，缺乏对语义的建模。本文旨在通过联合建模ASR和ITN，利用成对监督和序列级训练目标，提升中文ASR的书面语输出质量。

## 💡 核心创新

1. 提出DF-ASR框架，联合建模口语和书面语形式，支持提示级选择
2. 利用LLM驱动的生成-评判流程构建成对训练数据
3. 提出ITN-MWER序列级目标，对规范化敏感跨度赋予更高错误代价
4. 设计REQUIRE-ITN/FORBID-ITN协议，分别评估必要规范化和禁止跨度保留
5. 在SpeechIO中文子集上验证，优于开源ASR-ITN系统，接近闭源强系统

## 🏗️ 模型架构

DF-ASR基于编码器-解码器架构，输入为声学特征（如Fbank），编码器采用Conformer或类似结构，解码器为Transformer。模型通过提示（prompt）控制输出形式：口语或书面语。训练时使用成对口语-书面语文本作为目标，并引入ITN-MWER损失，该损失在序列级计算，对规范化敏感跨度（如数字、日期）的错误赋予更高权重。推理时，用户可通过提示选择输出形式。

## 📚 数据集

- SpeechIO中文子集（评估，手动标注）
- 内部训练数据（训练，包含成对口语-书面语文本，由LLM生成）

## 📊 实验结果

摘要未提供具体数值指标，但表明DF-ASR在SpeechIO中文子集上持续优于开源ASR-ITN系统，并与强闭源参考系统竞争。同时，模型保持了可靠的提示级控制，能根据提示输出口语或书面语形式。

## 🎯 结论与影响

DF-ASR通过联合建模ASR和ITN，利用成对监督和序列级目标，显著提升了中文ASR的书面语输出质量，同时保持口语输出的灵活性。该方法为ASR-ITN一体化建模提供了新思路，有望推动工业界ASR系统的简化与性能提升。

## ⚠️ 局限与未解决问题

摘要未提及局限性。可能存在的问题包括：依赖LLM生成训练数据可能引入噪声；ITN-MWER需要标注规范化敏感跨度，成本较高；实验仅在中文子集上评估，泛化性未知；未与最新端到端ITN方法对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-09-04/">← 返回 2026-09-04 速递</a></div>
