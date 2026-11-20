---
title: "Rhythm-TTS: High-Fidelity Shortcut Latent Modeling and Probabilistic Rhythm Generation for Zero-Shot Text-to-Speech"
date: 2026-11-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音合成"]
summary: "用离散codec token作语义-声学先验，流匹配直接生成连续语音latent，并加入概率化时长与静音生成器提升韵律多样性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音合成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#零样本TTS</span> <span class="tag-pill tag-pill-soft">#流匹配</span> <span class="tag-pill tag-pill-soft">#韵律建模</span> <span class="tag-pill tag-pill-soft">#离散Token先验</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.02848</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://rhythm-tts.github.io" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">rhythm-tts.github.io</span></span></a><a class="oc-chip oc-chip-demo" href="https://rhythm-tts.github.io" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">rhythm-tts.github.io</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.02848" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.02848" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://rhythm-tts.github.io" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://rhythm-tts.github.io" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用离散codec token作语义-声学先验，流匹配直接生成连续语音latent，并加入概率化时长与静音生成器提升韵律多样性。
</div>

## 👥 作者与机构

**Hieu-Nghia Huynh-Nguyen** ¹ · Ngoc-Son Nguyen · Long-Khanh Pham Huynh Nguyen Dang · Huy Tien Nguyen · Van Nguyen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做零样本TTS与流匹配声学建模的研究者阅读。建议通读，重点看§3的shortcut latent建模（离散token如何作先验而非最终表示）与§4的Duration/Silence Generator设计，再对照实验表的韵律多样性指标与效率对比。

## 🌍 研究背景

零样本TTS主流分两派：离散codec token路线（如基于codec语言模型的方法）序列建模稳定、因子化明确，但推理需codebook查表重组，误差累积导致自然度与说话人相似度存在上限；连续表示路线（如基于flow matching的声学模型）可直接生成细粒度latent，却依赖更重的in-context建模且对齐不够显式。此外，多次合成间的韵律多样性长期被忽视。本文要同时解决保真度上限与韵律单一两个问题。

## 💡 核心创新

1. 离散codec token仅作语义-声学先验，推理时绕过离散到latent的重建路径
2. 用flow matching直接生成整体连续语音latent（shortcut latent modeling）
3. 引入概率化Duration Generator采样动态语速
4. 引入Silence Generator建模静音停顿出现位置
5. 显式以run-to-run韵律多样性作为评价维度

## 🏗️ 模型架构

输入为文本音素序列与参考语音；先由离散codec token模型提供语义-声学先验，替代传统将预测token作为最终声学表示的做法；主干采用flow matching对整体连续语音latent进行生成，条件于上述先验与说话人信息，推理阶段不再经过codebook查表重组。声学生成前串联概率化Duration Generator与Silence Generator，对音素时长与静音停顿进行采样，形成动态节奏模式后再驱动声学生成。整体为非自回归框架，摘要未给出参数量。

## 📚 数据集

- 零样本TTS基准（评估，摘要未列具体数据集名）

## 📊 实验结果

摘要仅定性说明在零样本TTS基准上评估了可懂度、自然度、说话人相似度、效率与run-to-run韵律多样性，并称shortcut latent建模与概率韵律生成提升了非自回归零样本TTS的保真度与时间自然度，未给出任何具体指标数值，故无法列表对比。

## 🎯 结论与影响

最强结论是：把离散token降级为语义-声学先验、用flow matching直接生成连续latent，可在非自回归零样本TTS中同时改善保真度与时间自然度。该思路为离散-连续混合建模范式提供了可复用设计，并把韵律多样性纳入评价，可能推动后续工作关注多次合成的一致性-多样性权衡；工业上有利于降低对重型in-context建模的依赖。

## ⚠️ 局限与未解决问题

摘要未给出任何量化结果，难以判断相对强baseline的实际增益；韵律多样性指标的定义与主观评测规模不明；Duration/Silence Generator的消融、推理延迟与参数量均未在摘要体现；仅在零样本TTS基准评估，跨语种与跨域泛化未知。

## 🔗 开源资源

- **项目主页**：<https://rhythm-tts.github.io>
- **Demo / 试听**：<https://rhythm-tts.github.io>

---

<div class="paper-footer"><span>评分：7.0</span><span>原始：7.0</span><a href="/audio-paper-daily/posts/2026-11-20/">← 返回 2026-11-20 速递</a></div>
