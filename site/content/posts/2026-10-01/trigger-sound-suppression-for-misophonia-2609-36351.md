---
title: "Trigger Sound Suppression for Misophonia"
date: 2026-10-01T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "面向恐音症，构建10类触发声数据集，用流式双路网络按one-hot/multi-hot条件选择性抑制1-3种触发声，30人听测验证降低不适。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#目标声音提取</span> <span class="tag-pill tag-pill-soft">#数据集构建</span> <span class="tag-pill tag-pill-soft">#主观评测</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.36351</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-01</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.36351" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.36351" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>面向恐音症，构建10类触发声数据集，用流式双路网络按one-hot/multi-hot条件选择性抑制1-3种触发声，30人听测验证降低不适。
</div>

## 👥 作者与机构

**Vaishnavi Vidyasagar** ¹ · Jasmine Zhang · Mahima Uliyar · Seunghyun Oh · Emily Catherine Gates · Mark Zachary Rosenthal · Shyamnath Gollakota

**机构**：华盛顿大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做选择性/条件语音增强、目标声提取以及音频-健康交叉方向的研究者。建议通读，重点看 §3 的流式双路网络与条件注入方式、§4 的数据集构建与触发类定义，以及听测协议与统计部分。可先看表 2 的客观指标与听测结果表，再回看消融确认 multi-hot 条件是否真的有效。

## 🌍 研究背景

恐音症影响 5-20% 人群，对特定触发声（咀嚼、敲击等）耐受度下降。现有方案要么是认知行为疗法（仅对少数人有效），要么是耳塞/主动降噪，后者把整个声场一起压掉，牺牲环境感知与交流。通用语音增强/分离模型面向人声，不做"按类别选择性抑制非语音触发声"。本文要解决的是：在保留其余声场的前提下，从流式音频中定向抑制 1-3 类触发声。

## 💡 核心创新

1. 构建覆盖 10 类常见触发声的恐音症专用数据集
2. 6 ms chunk 的流式双路网络，满足实时低延迟
3. one-hot 与 multi-hot 条件注入，支持同时抑制 1-3 类触发声
4. 30 名临床显著恐音症成人参与的听测验证

## 🏗️ 模型架构

输入为 6 ms 音频 chunk 的时域/时频特征，主干采用流式 dual-path 网络（dual-path RNN/Transformer 风格的分块+跨块建模），在块内与块间交替建模以兼顾短时细节与上下文。条件侧通过 one-hot 或 multi-hot 触发类别向量注入（如条件 embedding 调制归一化或拼接），使同一模型可切换抑制目标。输出为与输入等长的抑制后波形，仅衰减被指定类别，保留其余声场。摘要未给出参数量与具体模块名。

## 📚 数据集

- 自建恐音症触发声数据集（10 类常见触发声，训练/评估，规模未披露）
- 30 名临床显著恐音症成人的听测（主观评估）

## 📊 实验结果

摘要仅报告主观听测结论：30 名临床显著恐音症被试对抑制后音频报告显著更低的 distress 与 arousal、更高的 valence，未给出 SI-SDR/PESQ 等客观数值、基线对比或消融数据，因此无法量化相对现有方法的增益。

## 🎯 结论与影响

最强结论是：条件化流式网络可在保留声场的同时选择性抑制触发声，并在真实恐音症人群中显著改善主观不适。这为"个性化、类别可控的音频抑制"提供了可行性证据，可能推动助听/耳机端的定向声音管理功能落地。

## ⚠️ 局限与未解决问题

缺少客观指标与强基线对比，未报告推理延迟、模型规模与实时性实测；数据集规模、触发类标注质量与泛化性未说明；听测仅 30 人且为被试内设计，可能存在期望偏差；multi-hot 条件与 one-hot 的消融不充分。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-01/">← 返回 2026-10-01 速递</a></div>
