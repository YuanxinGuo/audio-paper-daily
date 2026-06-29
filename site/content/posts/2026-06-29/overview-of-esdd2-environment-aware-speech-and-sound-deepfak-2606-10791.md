---
title: "Overview of ESDD2: Environment-Aware Speech and Sound Deepfake Detection Challenge"
date: 2026-06-29T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深伪检测"]
summary: "ESDD2挑战赛总结，聚焦环境感知的语音和声音深伪检测，最佳系统Macro-F1达0.8775，显著优于基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深伪检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#环境感知</span> <span class="tag-pill tag-pill-soft">#语音深伪检测</span> <span class="tag-pill tag-pill-soft">#声音深伪检测</span> <span class="tag-pill tag-pill-soft">#挑战赛总结</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.10791</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-29</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.10791" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.10791" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ESDD2挑战赛总结，聚焦环境感知的语音和声音深伪检测，最佳系统Macro-F1达0.8775，显著优于基线。
</div>

## 👥 作者与机构

**Xueping Zhang** ¹ · Han Yin · Yang Xiao · Lin Zhang · Ting Dang · Rohan Kumar Das · Ming Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事音频深伪检测、反欺诈研究的学者和工程师。建议重点阅读第3节（系统设计分析）和第4节（实验结果与EER分析），了解top系统的模块化分解、跨域自监督编码器、数据增强和选择性集成策略。

## 🌍 研究背景

音频深伪检测面临语音和环境声音独立或联合操纵的挑战。现有方法多针对单一模态，缺乏对环境感知的考虑。ESDD2挑战赛旨在推动环境感知的深伪检测研究，提供CompSpoofV2数据集和基线。此前基线方法（分离增强联合学习）Macro-F1仅0.6327，表明任务难度。

## 💡 核心创新

1. 模块化任务分解策略
2. 跨域自监督编码器应用
3. 针对性数据增强方法
4. 选择性集成而非简单模型缩放

## 🏗️ 模型架构

挑战赛不限定架构，top系统通常采用模块化设计：输入为语音和环境声音的联合特征，通过跨域自监督编码器（如WavLM、HuBERT）提取特征，再经任务分解模块分别处理语音和声音深伪检测，最后通过选择性集成融合多模型输出。

## 📚 数据集

- CompSpoofV2（训练/验证/测试，包含语音和环境声音的深伪样本）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Macro-F1 | ESDD2测试集 | 分离增强联合学习基线 0.6327 | **最佳系统 0.8775** | +0.2448 |

最佳系统Macro-F1达0.8775，远超基线0.6327。辅助EER分析显示，检测伪造环境声音成分和泛化到未见生成器仍具挑战。top系统普遍采用模块化分解、跨域自监督编码器、数据增强和选择性集成。

## 🎯 结论与影响

ESDD2挑战赛表明，环境感知的深伪检测中，模块化任务分解和跨域自监督学习是有效策略。最佳系统大幅超越基线，但伪造环境声音检测和泛化性仍是难点。未来研究可聚焦于环境成分的鲁棒检测和生成器泛化。

## ⚠️ 局限与未解决问题

挑战赛仅报告了Macro-F1和EER，缺乏对计算效率、模型大小和推理延迟的分析。测试集可能未覆盖所有真实场景，泛化性有待验证。此外，未提供消融实验量化各模块贡献。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-29/">← 返回 2026-06-29 速递</a></div>
