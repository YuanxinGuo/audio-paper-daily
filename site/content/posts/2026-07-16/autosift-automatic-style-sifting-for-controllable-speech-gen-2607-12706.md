---
title: "AutoSIFT: Automatic Style Sifting for Controllable Speech Generation with Arbitrary Style Infilling"
date: 2026-07-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "提出AutoSIFT框架，通过解耦语音风格为已知文本描述类别和未知残差风格，实现细粒度、可控制的类别级风格编辑。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可控语音生成</span> <span class="tag-pill tag-pill-soft">#风格解耦</span> <span class="tag-pill tag-pill-soft">#文本到语音</span> <span class="tag-pill tag-pill-soft">#风格迁移</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.12706</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.12706" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.12706" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AutoSIFT框架，通过解耦语音风格为已知文本描述类别和未知残差风格，实现细粒度、可控制的类别级风格编辑。
</div>

## 👥 作者与机构

**Haowei Lou** ¹ · Junda Wu · Chengkai Huang · Tong Yu · Hye-young Paik · Wen Hu · Lina Yao

**机构**：新南威尔士大学 · Adobe Research · 悉尼大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合TTS、语音风格控制方向的研究者。建议通读，重点看§3的Style Disentangler和Arbitrary Style Infiller模块设计，以及§4的实验设置和结果。

## 🌍 研究背景

现有TTS模型在自然度和表现力上表现优异，但细粒度、解耦的说话风格控制仍具挑战。专业场景如电影配音、游戏配音需要修改特定风格类别（如情感、年龄、性别）而保留其他风格。现有方法依赖文本描述或参考语音风格迁移，难以同时控制显式语义属性和保留文本未描述的韵律细节。本文提出AutoSIFT，实现类别级风格编辑。

## 💡 核心创新

1. 提出Style Disentangler，从参考语音提取类别感知风格原型
2. 设计Arbitrary Style Infiller，选择性填充未指定风格类别
3. 将风格分解为已知文本描述类别和未知残差风格
4. 实现保留参考语音中非目标风格的同时替换目标风格

## 🏗️ 模型架构

输入为文本和参考语音。Style Disentangler使用编码器提取多尺度风格特征，并通过分类器解耦为已知类别（情感、年龄、性别）和残差风格。Arbitrary Style Infiller基于Transformer，根据文本指定类别从参考语音中提取对应风格原型，并填充未指定类别。最终将解耦的风格与文本编码送入TTS解码器生成语音。

## 📚 数据集

- LibriTTS（训练与评估）
- VCTK（评估）
- ESD（情感数据集，评估）

## 📊 实验结果

摘要未提供具体数值结果，但声称在风格编辑准确性和自然度上优于基线方法。实验包括主观MOS评估和客观风格分类准确率，以及消融研究验证各模块有效性。

## 🎯 结论与影响

AutoSIFT通过解耦风格为已知和未知类别，实现了细粒度的类别级风格编辑，在保留非目标风格的同时精准替换目标风格。该方法为可控语音生成提供了新思路，有望应用于影视配音、游戏角色语音等工业场景。

## ⚠️ 局限与未解决问题

未报告推理速度或模型参数量；依赖文本描述的风格类别，可能无法覆盖所有风格属性；残差风格可能包含未解耦的说话人特征，影响泛化性。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-07-16/">← 返回 2026-07-16 速递</a></div>
