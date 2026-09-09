---
title: "ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion"
date: 2026-09-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音数据处理"]
summary: "提出从真实双人对话中生成分离、重建和扩展三阶段训练数据的流水线，用于全双工语音模型训练。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音数据处理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#数据生成</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#全双工语音</span> <span class="tag-pill tag-pill-soft">#对话建模</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.08147</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.08147" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.08147" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出从真实双人对话中生成分离、重建和扩展三阶段训练数据的流水线，用于全双工语音模型训练。
</div>

## 👥 作者与机构

**Richard Yucheng He** ¹ · Baodong Cao · Chen Xu · Yihang Liu · Tairan Chen

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合研究全双工语音、对话数据增强或语音分离的学者。建议重点阅读第3节方法部分和第4节实验设计，可先看表1和表2了解数据质量。若关注数据生成，值得通读；若仅关注下游模型，可略读。

## 🌍 研究背景

全双工语音模型需要保留轮流、重叠、打断和反馈等交互信号，但真实录音中这些信号与噪声和说话人混合。现有数据集缺乏此类精细标注，且生成数据难以保持说话人一致性和自然交互。本文旨在构建一个流水线，从真实双人对话中提取并生成高质量的训练数据，以支持全双工模型训练。

## 💡 核心创新

1. 分离阶段采用说话人验证确保身份稳定
2. 重建阶段基于固定文本生成匹配音色并保留交互时序
3. 扩展阶段利用对话上下文生成新对话
4. 引入自动评估器衡量上下文连贯性和自然度

## 🏗️ 模型架构

流水线包含三阶段：分离使用语音分离模型（如SepFormer）提取说话人特定音轨，并关联说话人验证；重建采用语音合成（如VITS）根据转录文本生成匹配音色的语音，并重建停顿、重叠等时序；扩展使用大语言模型（如Gemini）基于上下文生成新对话，再合成语音。输出为带词级对齐和交互指令的语音数据。

## 📊 实验结果

摘要未提供具体对比基线，但报告了各阶段质量指标：分离阶段NISQA MOS 3.56，重建4.41，扩展4.61；说话人相似度0.983-0.991，判别裕度0.199-0.209；扩展的上下文连贯性4.94/5，自然度4.80/5。扩展与重建的交互特征相似，但扩展的轮次、重叠、反馈和打断率分别低4.6%、8.0%、13.2%和16.0%。

## 🎯 结论与影响

本文提出的流水线能生成高质量、说话人一致且交互自然的全双工语音训练数据，为全双工模型训练提供了可行数据来源。其分离-重建-扩展框架可推广至其他对话数据生成任务，对工业界构建全双工语音助手具有潜在价值。

## ⚠️ 局限与未解决问题

作者未报告下游全双工模型训练效果，仅评估数据属性；未与现有数据增强方法对比；自动评估器依赖Gemini，可能引入偏差；未提供人工主观评估；未讨论计算成本。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-09/">← 返回 2026-09-09 速递</a></div>
