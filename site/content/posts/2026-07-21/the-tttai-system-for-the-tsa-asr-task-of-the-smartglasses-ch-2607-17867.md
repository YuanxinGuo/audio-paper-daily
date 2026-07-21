---
title: "The tttAI System for the TSA-ASR Task of the SmartGlasses Challenge 2026"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出级联系统，结合说话人日志、重叠检测、目标说话人提取和ASR，在智能眼镜挑战赛TSA-ASR任务中取得第二名。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#说话人日志</span> <span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#重叠语音处理</span> <span class="tag-pill tag-pill-soft">#级联架构</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.17867</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-21</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.17867" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.17867" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出级联系统，结合说话人日志、重叠检测、目标说话人提取和ASR，在智能眼镜挑战赛TSA-ASR任务中取得第二名。
</div>

## 👥 作者与机构

**Xuanji He** ¹ · Gaoyang Dong · Xiaoxiao Li · Minchuan Chen · Fengjie Zhu

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事说话人日志、目标说话人提取和远场ASR的研究者。建议重点阅读§3级联架构设计，特别是WeSep提取器和主导说话人回退策略。可参考其重叠区域处理思路。

## 🌍 研究背景

智能眼镜场景下的说话人属性语音识别（TSA-ASR）面临长音频、多说话人、频繁重叠的挑战。现有系统多采用级联方式，但重叠区域处理仍是瓶颈。本文针对SmartGlasses Challenge 2026的TSA-ASR任务，提出包含说话人日志、重叠检测、目标说话人提取和ASR的级联系统，旨在提升重叠语音下的识别性能。

## 💡 核心创新

1. 基于WavLM-Large和Conformer的说话人日志模块
2. WeSep目标说话人提取模型结合ECAPA-TDNN嵌入
3. 主导说话人回退策略处理不可靠提取
4. 1.53B参数级联系统在双人对话和多人会议场景验证

## 🏗️ 模型架构

输入为智能眼镜多通道录音，首先使用WavLM-Large提取特征，经Conformer编码器进行帧级说话人分类，再通过嵌入聚类生成全局说话人分段。对重叠区域，采用WeSep目标说话人提取模型，以ECAPA-TDNN说话人嵌入为线索提取目标语音。若提取不可靠，则回退至主导说话人策略。最后使用FireRedASR2-AED（第一通道）进行语音识别。总参数量约1.53B。

## 📚 数据集

- SmartGlasses Challenge 2026 TSA-ASR数据集（Track 1双人对话，Track 2多人会议，评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| tcpCER | Track 1 | 未提供 | **7.10%** | N/A |
| tcpCER | Track 2 | 未提供 | **34.04%** | N/A |

在Track 1（双人对话）上tcpCER为7.10%，Track 2（多人会议）上tcpCER为34.04%，排名第二。摘要未提供消融实验或与其他系统的详细对比，但展示了级联架构在复杂场景下的有效性。

## 🎯 结论与影响

本文提出的级联系统在智能眼镜TSA-ASR任务上取得有竞争力的结果，验证了说话人日志+目标说话人提取+ASR框架的有效性。重叠区域处理策略和回退机制为后续研究提供了参考。系统对工业级智能眼镜语音交互具有潜在应用价值。

## ⚠️ 局限与未解决问题

摘要未提供消融实验，无法评估各模块贡献；未报告推理延迟和模型效率；仅在单一挑战赛数据集上评估，泛化性未知；未与端到端方法对比；Track 2的tcpCER仍较高，重叠语音处理有待改进。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-21/">← 返回 2026-07-21 速递</a></div>
