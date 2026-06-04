---
title: "FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频深度伪造检测"]
summary: "提出首个黑盒自动化红队方法FoeGlass，利用LLM的上下文学习能力探索TTS输入空间，生成欺骗ADD模型的音频样本，无需人工监督。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频深度伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#红队测试</span> <span class="tag-pill tag-pill-soft">#上下文学习</span> <span class="tag-pill tag-pill-soft">#文本转语音</span> <span class="tag-pill tag-pill-soft">#对抗攻击</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.05101</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.05101" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.05101" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出首个黑盒自动化红队方法FoeGlass，利用LLM的上下文学习能力探索TTS输入空间，生成欺骗ADD模型的音频样本，无需人工监督。
</div>

## 👥 作者与机构

**Sepehr Dehdashtian** ¹ · Jacob H Seidman · Vishnu N Boddeti · Gaurav Bharaj

**机构**：东北大学 · 华为

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频安全、对抗攻击和深度伪造检测领域的研究者。建议通读，重点看§3方法设计和§4实验（表1、2）。可复现其上下文设计策略。

## 🌍 研究背景

音频深度伪造检测（ADD）模型对防御恶意TTS至关重要，但现有数据集开发策略面临手动收集和盲点发现低效的问题。SOTA基准测试未能充分覆盖生成音频空间中的高错误区域，导致ADD模型鲁棒性不足。本文旨在自动化发现ADD失败模式，无需白盒访问。

## 💡 核心创新

1. 首次提出黑盒自动化红队方法FoeGlass
2. 利用LLM上下文学习探索TTS输入空间
3. 基于多样性度量的上下文设计缓解模式崩溃
4. 攻击可跨不同ADD模型迁移
5. 微调ADD模型可提升鲁棒性达41%

## 🏗️ 模型架构

FoeGlass由三个黑盒组件组成：LLM（如GPT-4）、TTS模型和目标ADD模型。LLM通过上下文学习生成TTS输入文本，上下文包含基于多样性度量的历史攻击样本。TTS模型将文本转为音频，ADD模型判断真伪。迭代优化，选择使ADD误判的样本。无需任何模型内部信息。

## 📚 数据集

- LibriTTS（TTS训练数据）
- ASVspoof2019（ADD评估数据）
- WaveFake（ADD评估数据）
- In-the-Wild（ADD评估数据）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| FNR（假阴性率） | ASVspoof2019 | 无条件采样 0.25 | **0.015** | -94% |
| FNR | WaveFake | 无条件采样 0.30 | **0.02** | -93.3% |

FoeGlass在多个ADD模型上显著降低假阴性率，相比无条件采样和现有欺骗数据集提升高达94%。攻击可迁移至不同ADD模型。微调ADD模型后，鲁棒性提升41%。实验覆盖多种TTS和ADD架构。

## 🎯 结论与影响

FoeGlass证明了简单的上下文学习足以自动化红队测试ADD系统，无需人工或白盒访问。该方法可高效发现盲点，生成的攻击样本可提升ADD模型鲁棒性。对工业界自动化安全评估有重要价值。

## ⚠️ 局限与未解决问题

依赖LLM的上下文学习能力，可能受限于LLM的生成多样性；未评估对更复杂TTS模型（如VALL-E）的效果；未报告计算开销；攻击迁移性仅测试了开源ADD模型。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-06-04/">← 返回 2026-06-04 速递</a></div>
