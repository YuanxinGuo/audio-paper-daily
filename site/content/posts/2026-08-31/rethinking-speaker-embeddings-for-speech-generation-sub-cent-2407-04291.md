---
title: "Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity"
date: 2026-08-31T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音生成"]
summary: "提出子中心说话人嵌入建模，在判别训练中保留说话人内变异性，提升零样本语音转换的自然度和韵律多样性。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人嵌入</span> <span class="tag-pill tag-pill-soft">#零样本语音转换</span> <span class="tag-pill tag-pill-soft">#子中心建模</span> <span class="tag-pill tag-pill-soft">#语音生成</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2407.04291</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-31</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2407.04291" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2407.04291" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出子中心说话人嵌入建模，在判别训练中保留说话人内变异性，提升零样本语音转换的自然度和韵律多样性。
</div>

## 👥 作者与机构

**Ismail Rasim Ulgen** ¹ · John H. L. Hansen · Carlos Busso · Berrak Sisman

**机构**：德克萨斯大学达拉斯分校 · 南加州大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音生成、语音转换和说话人嵌入研究者阅读。重点看第3节方法部分和第4节实验设置与结果。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

说话人嵌入广泛用于个性化语音生成，但传统嵌入训练目标为说话人识别，强调类间分离而抑制类内变异，导致嵌入过于紧凑，丢失生成所需的自然变化。本文旨在重新设计嵌入训练，在保持判别性的同时保留说话人内多样性，以提升生成质量。

## 💡 核心创新

1. 提出子中心建模，每个说话人学习多个原型，保留类内变异
2. 在判别训练中引入子中心损失，平衡判别性与多样性
3. 在零样本语音转换中验证，提升自然度和韵律多样性
4. 保持说话人验证性能，兼顾生成与识别
5. 提供理论分析和消融实验，验证子中心有效性

## 🏗️ 模型架构

输入为语音特征（如Mel谱），通过预训练编码器提取帧级特征，然后经池化层得到说话人嵌入。训练时，每个说话人对应K个子中心，嵌入与最近子中心对齐，使用AAM-Softmax等判别损失优化。推理时，嵌入作为条件输入到语音生成模型（如VITS），实现零样本转换。

## 📚 数据集

- VCTK（训练/评估，多说话人语音）
- LibriTTS（训练/评估，多说话人语音）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | VCTK | 基线（如ECAPA-TDNN） | **降低** | 具体数值未给出 |
| Pitch Variability | VCTK | 基线 | **提高** | 具体数值未给出 |
| Naturalness MOS | VCTK | 基线 | **提高** | 具体数值未给出 |
| EER | VoxCeleb1 | 基线 | **保持** | 具体数值未给出 |

实验表明，子中心嵌入在零样本语音转换中显著提升可懂度（WER降低）、韵律多样性（基频标准差增加）和自然度（MOS提高），同时保持说话人验证性能（EER与基线相当）。消融实验验证了子中心数量的影响，并分析了嵌入分布特性。

## 🎯 结论与影响

本文通过子中心建模重新思考说话人嵌入，在保持判别性的同时保留类内变异，显著提升语音生成质量。该方法为生成任务中的说话人嵌入设计提供了新思路，有望推广到其他个性化语音生成任务，并促进工业界语音合成系统的自然度提升。

## ⚠️ 局限与未解决问题

摘要未提供具体数值，缺乏与最新方法的定量对比；未讨论子中心数量对计算复杂度的影响；实验仅在语音转换上验证，未扩展到其他生成任务（如TTS）；未分析子中心嵌入的泛化能力。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-31/">← 返回 2026-08-31 速递</a></div>
