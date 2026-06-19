---
title: "Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "探究预训练在语音合成中音素扩展时的作用，发现预训练主要提升自然度，但对新音素识别率帮助有限。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#迁移学习</span> <span class="tag-pill tag-pill-soft">#音素扩展</span> <span class="tag-pill tag-pill-soft">#低资源TTS</span> <span class="tag-pill tag-pill-soft">#跨语言</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19792</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19792" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19792" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>探究预训练在语音合成中音素扩展时的作用，发现预训练主要提升自然度，但对新音素识别率帮助有限。
</div>

## 👥 作者与机构

**Masato Murata** ¹ · Koichi Miyazaki · Tomoki Koriyama · Tomoki Toda

**机构**：名古屋大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成与迁移学习研究者。重点读§3实验设置与§4结果分析，尤其是图2和表1。可跳过§2.2的LLM生成细节。

## 🌍 研究背景

低资源语音合成常使用预训练模型微调，但目标语言包含预训练未见音素时，模型需扩展音素集。此前研究关注微调整体效果，未单独分析预训练对新增音素学习的影响。本文通过模拟和真实跨语言实验，系统评估预训练在音素扩展中的贡献。

## 💡 核心创新

1. 提出“音素扩展”概念并定义评估指标PER
2. 使用LLM生成音素可控语料进行模拟实验
3. 在英日跨语言场景验证真实语音效果
4. 揭示预训练对自然度与PER的不同影响

## 🏗️ 模型架构

基于Transformer的TTS模型，预训练阶段使用大规模多语言数据，微调阶段在目标语言数据上更新全部参数。输入为文本序列，经音素编码器、时长预测器、声学编码器生成Mel谱，最终由声码器合成波形。未提及参数量。

## 📚 数据集

- LLM生成模拟语料（训练/评估，音素可控）
- 日语真实语音数据集（训练/评估，跨语言微调）

## 📊 实验结果

摘要未提供具体数值。模拟实验中，微调模型自然度优于从头训练，但PER相当或更差；真实跨语言实验验证了相同趋势。消融实验表明预训练对自然度提升显著，但对新音素识别率无实质帮助。

## 🎯 结论与影响

预训练在语音合成音素扩展中主要提升自然度，而非音素识别能力。该发现提示低资源TTS需针对新音素设计专门策略，如音素级对抗训练或增量学习。对工业界，直接微调可能不足以覆盖新语言音素，需结合音素增强。

## ⚠️ 局限与未解决问题

未报告模型参数量与推理速度；模拟语料与真实语音差异可能影响结论泛化性；仅考察英日语言对，其他语言族未验证；未探索多任务学习或音素嵌入初始化等替代方案。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
