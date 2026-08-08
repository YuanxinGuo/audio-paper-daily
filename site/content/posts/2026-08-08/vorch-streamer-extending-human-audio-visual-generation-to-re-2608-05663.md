---
title: "Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音视频生成"]
summary: "提出Vorch-Streamer后训练框架，通过混合教师强制与扩散强制、长时自强制及语音规划令牌，实现实时长时音视频流式生成。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音视频生成</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#流式生成</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#教师强制</span> <span class="tag-pill tag-pill-soft">#长时一致性</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.05663</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.05663" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.05663" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Vorch-Streamer后训练框架，通过混合教师强制与扩散强制、长时自强制及语音规划令牌，实现实时长时音视频流式生成。
</div>

## 👥 作者与机构

**Menglin Han** ¹ · Yang Ding · Yulei Lu · Haoran Yu · Xin Ma · Junyi Chen · Zhangkai Ni · Lin Ma · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音视频生成、流式生成及扩散模型研究者。建议重点阅读第3节方法部分（教师强制与扩散强制的混合策略、自强制训练）及第4节实验（表2、表3）。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

实时长时虚拟人音视频生成需因果连续合成，同时保持音画同步和视觉一致性。现有预训练双向模型在流式场景下存在两个问题：自回归复用生成块导致暴露偏差和视觉漂移；全局语音话语无法指示因果生成器在有限局部上下文下应说哪部分。本文旨在解决这些问题，实现实时长时文本到音视频（T2AV）流式生成。

## 💡 核心创新

1. 混合教师强制与扩散强制训练因果生成器
2. 长时自强制与DMD蒸馏减少暴露偏差
3. 外部语言模型预测25Hz语音规划令牌控制语音进度
4. 四步去噪实现27.12 FPS实时生成
5. 构建80K 12-21秒虚拟人片段合成语料库

## 🏗️ 模型架构

Vorch-Streamer基于预训练双向模型，后训练为因果生成器。输入文本，外部语言模型预测25Hz离散语音规划令牌，其连续特征条件化音频扩散分支。主干为因果生成器，训练时混合教师强制（使用真实上下文）和扩散强制（使用预测上下文），后应用长时自强制（暴露自身分布）与DMD蒸馏。生成时采用四步去噪，联合生成音频和视频，输出音画同步的流式结果。

## 📚 数据集

- 80K虚拟人片段（12-21秒，合成语料库，训练）
- 未指定测试集（评估）

## 📊 实验结果

摘要未提供具体量化指标（如SI-SDR、PESQ等），仅提及生成速度27.12 FPS，超过24 FPS实时播放率，并声称保持有竞争力的音画同步和强身份保持。未提供与基线方法的数值对比。

## 🎯 结论与影响

Vorch-Streamer通过后训练框架有效解决预训练双向模型在流式生成中的暴露偏差和语音进度控制问题，实现实时长时音视频生成。其混合训练策略和语音规划令牌为后续流式生成研究提供新思路，对虚拟人实时交互、直播等工业应用有潜在价值。

## ⚠️ 局限与未解决问题

摘要未提及局限，但作为审稿人可见：缺乏与现有流式方法的定量对比；合成语料库可能引入领域偏差；未报告音频质量指标（如PESQ）和视觉一致性指标；未讨论长时生成中的错误累积上限；未提供消融实验细节。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：8.2</span><a href="/audio-paper-daily/posts/2026-08-08/">← 返回 2026-08-08 速递</a></div>
