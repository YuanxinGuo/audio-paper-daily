---
title: "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Whisper", "#最小贝叶斯风险解码", "#波束搜索", "#语音识别"]
summary: "本文系统评估了最小贝叶斯风险解码在ASR和语音翻译任务中的效果，发现其多数情况下优于波束搜索。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音识别</span> <span class="tag-pill tag-pill-soft">#最小贝叶斯风险解码</span> <span class="tag-pill tag-pill-soft">#波束搜索</span> <span class="tag-pill tag-pill-soft">#Whisper</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2510.19471</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/CyberAgentAILab/mbr-for-asr" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">CyberAgentAILab/mbr-for-asr</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.19471" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.19471" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CyberAgentAILab/mbr-for-asr" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>本文系统评估了最小贝叶斯风险解码在ASR和语音翻译任务中的效果，发现其多数情况下优于波束搜索。
</div>

## 👥 作者与机构

**Yuu Jinnai** ¹

**机构**：CyberAgent AI Lab

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR和ST领域的研究者阅读。建议重点看§3实验设置和§4结果分析，特别是表1-3的对比。可先看摘要和结论，再深入实验部分。

## 🌍 研究背景

在文本生成任务中，基于采样的最小贝叶斯风险解码已被证明优于波束搜索，但在语音到文本任务如ASR和ST中，波束搜索仍是主流。本文旨在验证MBR解码在ASR/ST中的有效性，使用Whisper及其衍生模型在英语和日语上评估。

## 💡 核心创新

1. 首次系统评估MBR解码在ASR/ST任务上的表现
2. 使用Whisper系列模型进行多语言实验
3. 开源代码便于复现

## 🏗️ 模型架构

输入语音特征 → Whisper编码器 → Whisper解码器生成候选序列 → 基于采样生成N个候选 → 使用MBR解码（基于负对数似然或BLEU等效用函数）选择最优序列 → 输出文本。未提及参数量。

## 📚 数据集

- LibriSpeech (英语ASR评估)
- Common Voice (英语ASR评估)
- JSUT (日语ASR评估)
- CoVoST2 (英语-日语ST评估)

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | 波束搜索 3.0 | **MBR 2.8** | -0.2 |
| WER | LibriSpeech test-other | 波束搜索 7.5 | **MBR 7.1** | -0.4 |
| WER | Common Voice en | 波束搜索 12.1 | **MBR 11.5** | -0.6 |
| WER | JSUT | 波束搜索 6.8 | **MBR 6.3** | -0.5 |
| BLEU | CoVoST2 en-ja | 波束搜索 22.4 | **MBR 23.1** | +0.7 |

在多个数据集上，MBR解码在WER和BLEU指标上均优于波束搜索，提升幅度在0.2-0.7之间。消融实验显示，候选数量增加可进一步提升性能，但计算成本也相应增加。

## 🎯 结论与影响

MBR解码在ASR和ST任务中普遍优于波束搜索，尤其在高精度要求的离线场景下具有潜力。该工作可能推动语音领域解码策略的转变，但计算开销需权衡。

## ⚠️ 局限与未解决问题

仅评估了Whisper模型，未涉及其他ASR架构；未报告推理延迟；候选数量对性能的影响分析不够深入；未在更大规模数据集上验证。

## 🔗 开源资源

- **代码**：<https://github.com/CyberAgentAILab/mbr-for-asr>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
