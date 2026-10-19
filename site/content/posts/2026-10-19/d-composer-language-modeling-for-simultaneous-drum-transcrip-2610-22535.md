---
title: "D-Composer: Language Modeling for Simultaneous Drum Transcription and Sound Event Decomposition"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "用自回归语言模型把鼓录音分解为带标签的单次击打事件与起始时间，统一鼓转录与音源分解。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音乐信息检索</span> <span class="tag-pill tag-pill-soft">#鼓转录</span> <span class="tag-pill tag-pill-soft">#语言模型</span> <span class="tag-pill tag-pill-soft">#音频分词</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.22535</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.22535" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.22535" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用自回归语言模型把鼓录音分解为带标签的单次击打事件与起始时间，统一鼓转录与音源分解。
</div>

## 👥 作者与机构

**Patrick O'Reilly** ¹ · Saumya Pailwan · Annie Chu · Jason Smith · Bryan Pardo

**机构**：西北大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 MIR、鼓转录/分离与音频 token 语言建模的研究者。值得通读，重点看 §3 的 token 化与序列建模设计、以及合成数据配方；实验部分先看与 AbS 基线在跨音色泛化上的对比表，再看 one-shot 提取的客观指标。

## 🌍 研究背景

鼓转录与鼓源分离此前多依赖任务专用监督，需要高质量成对音频-转录数据。Drum Analysis-by-Synthesis（AbS）以重建式训练统一转录、分离与 one-shot 提取，但难以泛化到电子鼓等多样音色，且不建模同类鼓（如多个 kick）的类内音色变化。本文要解决 AbS 的泛化与数据依赖问题。

## 💡 核心创新

1. 将鼓录音分解建模为自回归语言建模序列
2. 紧凑声学 token 表示替代波形重建目标
3. 合成数据驱动的训练配方，降低成对标注依赖
4. 统一转录与 one-shot 音事件分解为同一生成任务

## 🏗️ 模型架构

输入鼓混音经声学编码器转为紧凑离散 token 序列，与鼓类标签、onset 时间等符号信息交织成统一序列；主干为自回归语言模型（decoder-only Transformer），逐 token 预测事件标签与起始位置；解码端将预测序列还原为转录结果与各单次击打波形/事件，实现分解式输出。摘要未给出参数量。

## 📚 数据集

- 合成鼓数据（训练，作者构建的合成数据）
- 鼓转录/one-shot 提取评测集（评估，摘要未具名）

## 📊 实验结果

摘要仅定性说明：在鼓转录与 one-shot 提取任务上，D-Composer 与 SOTA AbS 系统及任务专用基线相当或更优，并在更广的鼓音色范围（含电子鼓）上泛化更好。摘要未给出 SI-SDR、F1 等具体数值，故不列量化对比。

## 🎯 结论与影响

最强结论是：充足合成数据加紧凑声学 token，语言建模即可统一鼓转录与音事件分解。这为 MIR 中 AbS 路线提供了更简单、泛化更好的替代方案，也提示音频 token 语言模型可迁移到其他结构化音事件任务；工业上利于电子鼓等多样音色的自动扒谱与采样提取。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与模型规模，自回归解码的实时性存疑；评测集与具体指标缺失，跨数据集泛化证据不足；合成数据与真实录音的域差距未量化；缺少对 token 粒度、序列顺序等关键设计的消融。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
