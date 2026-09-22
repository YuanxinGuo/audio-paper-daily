---
title: "OmniEcho: Spatial Audio Understanding for Embodied Agents"
date: 2026-09-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出 OmniEchoBench 空间视听基准与 OmniEcho 全模态模型，用 FOA 空间编码器实现声源定位与声引导导航。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#视听导航</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#声源定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.23407</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.23407" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.23407" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 OmniEchoBench 空间视听基准与 OmniEcho 全模态模型，用 FOA 空间编码器实现声源定位与声引导导航。
</div>

## 👥 作者与机构

**Ruixun Liu** ¹ · **Yuxuan Wang** ¹ · Jiacheng Xie · Yuhuan You · Donghua Cai · Junming Lin · Xiong-Hui Chen · Zhifang Guo · … 等 5 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频、视听多模态与具身导航的研究者阅读。建议通读，重点看 §3 的 OmniEchoBench 六任务定义与 FOA 数据采集流程，以及 §4 中 FOA 空间编码器与语义音频双通路的融合设计；表 2、表 3 的感知与导航结果需对照 baseline 细看。若只关心方法，可先看 §4.2 与消融部分。

## 🌍 研究背景

人类能轻松定位声源方向并与视觉线索联合推理，但具身智能体仍难做到。现有空间音频研究多聚焦单一任务（如 DOA 估计或 SELD），缺乏统一的视听感知与导航评测；同时真实 FOA 空间音频数据稀缺，训练监督难以规模化。本文要解决的是：如何系统评测并建模具身场景下的空间音频理解，并验证空间音频对导航的实际价值。

## 💡 核心创新

1. 构建 OmniEchoBench：6 任务、197 场景、2972 QA、900 导航样本的 FOA 视听基准
2. 提出几何一致的可控空间音频渲染管线，支持规模化训练监督
3. OmniEcho 引入 FOA 空间编码器与预训练语义音频双通路
4. 将空间音频接入视听语言导航，验证声引导导航可行性

## 🏗️ 模型架构

输入为第一人称 FOA 空间音频与同步视觉观测。音频侧分两路：FOA 空间编码器提取方向与距离等空间线索，预训练语义音频通路提取内容语义；视觉侧由视觉编码器处理帧序列。两路音频特征与视觉特征经跨模态融合后送入全模态大语言模型主干，输出感知问答答案或导航动作序列。摘要未给出具体参数量与主干网络名。

## 📚 数据集

- OmniEchoBench（自建基准，197 个真实空间视听场景、2972 QA、900 导航样本，评估）
- 30 个真实环境采集的 FOA 音频（数据来源，训练/评估）
- 可控渲染管线生成的合成空间音频（训练监督）

## 📊 实验结果

摘要仅给出定性结论：OmniEcho 在空间视听感知上达到 state-of-the-art，声引导导航性能接近传统视觉语言导航。未提供 SI-SDR、定位误差、成功率等具体数值，也未说明对比基线名称与消融细节，需查阅正文表格确认提升幅度。

## 🎯 结论与影响

最强结论是空间音频可作为具身场景推理与导航的有效信号，且 OmniEcho 在空间视听感知上达到 SOTA。该工作为空间音频理解提供了统一基准与渲染监督范式，可能推动后续视听导航与全模态模型研究；工业上对机器人、AR/VR 的声引导交互有参考价值。

## ⚠️ 局限与未解决问题

摘要自认细粒度空间定位与距离估计仍是开放难题。作为审稿人可见：缺少具体指标数值与基线对比，未报告推理延迟与模型规模；渲染管线合成数据与真实 FOA 的域差异未量化；导航任务仅称接近传统 VLN，未说明差距来源。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：7.5</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-22/">← 返回 2026-09-22 速递</a></div>
