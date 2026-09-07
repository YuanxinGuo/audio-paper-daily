---
title: "Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "提出证据接地生成式语音增强框架，结合确定性估计与LLM自回归生成，通过SNR条件接地和局部细化提升低信噪比感知质量。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#大语言模型</span> <span class="tag-pill tag-pill-soft">#自回归生成</span> <span class="tag-pill tag-pill-soft">#离散编码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04245</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04245" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04245" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出证据接地生成式语音增强框架，结合确定性估计与LLM自回归生成，通过SNR条件接地和局部细化提升低信噪比感知质量。
</div>

## 👥 作者与机构

**Hao Shi** ¹ · Yuan Gao · Zhaoheng Ni · Junyi Peng · Gongping Huang · Yu Tsao · Xugang Lu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音增强和生成式模型研究者。重点阅读第3节方法部分（SNR-CSG和GNR-LLM）以及第4节实验设置与结果。可先看图1和表2了解整体框架和主要增益。

## 🌍 研究背景

基于LLM的自回归语音增强能生成自然语音，但可能产生幻觉内容；确定性方法保留观测信息但残留噪声。现有方法未有效结合两者优势。本文提出利用确定性估计作为证据，引导自回归生成，并通过接地机制平衡内容保真与感知质量。

## 💡 核心创新

1. 提出Code-Space Grounding (CSG) 惩罚FSQ空间中远离证据的候选
2. SNR-CSG根据残差SNR自适应调节接地强度
3. GNR-LLM利用LLM排名和局部FSQ邻域细化锚点
4. Whisper-guided DPRNN生成增强波形作为证据
5. 统一框架结合确定性估计与生成式先验

## 🏗️ 模型架构

输入含噪语音经Whisper-guided DPRNN生成增强波形，与观测混合后经FSQ tokenizer离散化为证据序列。该序列条件化自回归clean-speech token生成器，并在解码时通过CSG惩罚候选。SNR-CSG根据残差SNR估计映射到接地强度，构建自适应锚点。GNR-LLM额外执行一次teacher-forced pass，结合LLM top-K候选与局部FSQ邻域，细化输出。

## 📚 数据集

- in-domain dataset（训练/评估）
- controlled-SNR dataset（评估）
- DNS no-reverb dataset（评估）

## 📊 实验结果

摘要未提供具体数值，但声称SNR-CSG提供鲁棒自动接地，GNR-LLM在低SNR下显著提升感知质量而不牺牲内容保真。实验覆盖域内、受控SNR和DNS无混响条件。

## 🎯 结论与影响

本文提出证据接地生成式SE框架，有效结合确定性估计与LLM生成，通过自适应接地和局部细化提升低SNR感知质量。对后续研究，该框架可推广至其他生成式语音处理任务，并可能推动LLM在语音增强中的实际应用。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：依赖预训练模型（Whisper、LLM）导致计算开销大；FSQ离散化可能引入信息损失；接地强度估计依赖SNR，实际场景SNR估计可能不准确；实验未报告与最新判别式方法的全面对比。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-07/">← 返回 2026-09-07 速递</a></div>
