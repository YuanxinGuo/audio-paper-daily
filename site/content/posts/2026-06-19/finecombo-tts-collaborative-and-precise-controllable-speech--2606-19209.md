---
title: "FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "提出FineCombo-TTS，通过文本描述和参考语音联合控制语音合成，实现灵活精确的声学属性调控。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#可控语音合成</span> <span class="tag-pill tag-pill-soft">#条件流匹配</span> <span class="tag-pill tag-pill-soft">#文本描述</span> <span class="tag-pill tag-pill-soft">#参考语音</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19209</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19209" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19209" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出FineCombo-TTS，通过文本描述和参考语音联合控制语音合成，实现灵活精确的声学属性调控。
</div>

## 👥 作者与机构

**Shuoyi Zhou** ¹ · Yixuan Zhou · Peiji Yang · Yifan Hu · Yicheng Zhong · Zhisheng Wang · Zhiyong Wu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音合成领域研究者，重点关注§3的模型架构和§4的FineEdit数据集构建。建议通读全文，特别是条件流匹配模块的设计。

## 🌍 研究背景

可控语音合成是TTS研究热点。现有方法要么基于参考语音（控制音色但缺乏精细属性控制），要么基于文本描述（控制全局风格但无法精确指定声学细节）。近期联合方法仍松散耦合，语音建模音色而文本控制风格，缺乏对声学属性的细粒度联合控制。本文旨在解决这一问题，提出统一框架实现基于参考语音和文本描述的灵活精确控制。

## 💡 核心创新

1. 提出统一声学表示，避免显式属性解耦
2. 引入条件流匹配（CFM）的语音方差预测器
3. 构建FineEdit结构化配对数据集，编码源-目标属性变化
4. 支持相对属性控制，实现灵活精确的合成

## 🏗️ 模型架构

输入为参考语音和文本描述。首先通过编码器提取统一声学表示，然后送入基于条件流匹配（CFM）的语音方差预测器，该预测器以文本描述为条件，建模参考语音到目标语音的细粒度变换。最后通过声码器合成波形。整体框架端到端训练，无需显式属性解耦。

## 📚 数据集

- FineEdit（构建的结构化配对数据集，用于训练和评估）
- LibriTTS（可能用于预训练或补充数据，摘要未明确）

## 📊 实验结果

摘要未提供具体数值结果，但声称实验表明方法实现了灵活、精确且富有表现力的可控语音合成。具体指标（如MOS、自然度、可控性评分）需查阅全文。

## 🎯 结论与影响

FineCombo-TTS通过统一声学表示和条件流匹配，实现了基于参考语音和文本描述的协同精确控制，避免了显式解耦的复杂性。该方法为可控语音合成提供了新范式，有望推动个性化语音生成和交互式应用的发展。

## ⚠️ 局限与未解决问题

摘要未提及局限。可能的问题包括：FineEdit数据集规模及多样性未知；相对属性控制的精度缺乏量化评估；与现有方法（如YourTTS、VALL-E）的对比未在摘要中体现。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-06-19/">← 返回 2026-06-19 速递</a></div>
