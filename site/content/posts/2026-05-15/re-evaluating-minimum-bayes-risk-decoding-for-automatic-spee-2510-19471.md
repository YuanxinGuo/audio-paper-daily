---
title: "Re-evaluating Minimum Bayes Risk Decoding for Automatic Speech Recognition"
date: 2026-05-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#Whisper", "#最小贝叶斯风险解码", "#波束搜索", "#语音识别"]
summary: "将最小贝叶斯风险解码应用于ASR和语音翻译任务，在Whisper模型上验证其优于波束搜索。"
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

<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2510.19471" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2510.19471" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/CyberAgentAILab/mbr-for-asr" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>将最小贝叶斯风险解码应用于ASR和语音翻译任务，在Whisper模型上验证其优于波束搜索。
</div>

## 👥 作者与机构

**Yuu Jinnai** ¹

**机构**：CyberAgent

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合ASR和ST领域的研究者，尤其是关注解码策略优化的读者。建议重点阅读§3实验设置和§4结果分析，对比MBR与波束搜索在不同语言和模型上的表现。可先看表1和表2。

## 🌍 研究背景

在文本生成任务（如机器翻译）中，基于采样的最小贝叶斯风险（MBR）解码已被证明优于波束搜索。然而，在语音到文本任务（如ASR和语音翻译）中，波束搜索仍是主流。本文旨在验证MBR解码在ASR和ST任务上的有效性，填补这一空白。

## 💡 核心创新

1. 首次系统评估MBR解码在ASR/ST任务上的表现
2. 在Whisper及其衍生模型上跨语言（英/日）验证
3. 开源代码便于复现和进一步研究

## 🏗️ 模型架构

使用Whisper及其衍生模型作为基础ASR/ST系统。输入为音频特征，经编码器-解码器架构生成候选序列。MBR解码过程：从模型输出分布中采样N个候选序列，使用质量评估函数（如负词错误率）计算每个候选与所有候选的期望风险，选择风险最小的序列作为最终输出。

## 📚 数据集

- LibriSpeech（英语ASR评估）
- Common Voice（英语ASR评估）
- JSUT（日语ASR评估）
- CoVoST 2（英语-德语语音翻译评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| WER | LibriSpeech test-clean | 波束搜索 3.0 | **MBR 2.6** | -0.4 |
| WER | LibriSpeech test-other | 波束搜索 7.2 | **MBR 6.5** | -0.7 |
| WER | Common Voice en | 波束搜索 11.5 | **MBR 10.8** | -0.7 |
| CER | JSUT | 波束搜索 4.2 | **MBR 3.8** | -0.4 |
| BLEU | CoVoST 2 en-de | 波束搜索 28.1 | **MBR 29.0** | +0.9 |

在多个ASR和ST基准上，MBR解码一致优于波束搜索：LibriSpeech test-clean上WER从3.0降至2.6（-13%），test-other上从7.2降至6.5（-10%）；日语ASR的CER从4.2降至3.8；语音翻译BLEU从28.1提升至29.0。MBR在采样数量N=30时达到最佳性能，且对质量评估函数的选择不敏感。

## 🎯 结论与影响

MBR解码在ASR和ST任务上显著优于波束搜索，为离线高精度语音识别和翻译提供了新范式。该方法可无缝集成到现有基于Whisper的系统中，有望推动工业界采用基于采样的解码策略。后续可探索更高效的质量评估函数和自适应采样策略。

## ⚠️ 局限与未解决问题

实验仅基于Whisper模型，未验证在其他架构（如Conformer）上的泛化性；MBR解码计算开销较大（需采样多个候选并计算风险），未报告推理延迟；未在流式ASR场景下评估；仅测试英语和日语，多语言泛化未知。

## 🔗 开源资源

- **代码**：<https://github.com/CyberAgentAILab/mbr-for-asr>

---

<div class="paper-footer"><span>评分：7.5</span><span>原始：7.5</span><a href="/audio-paper-daily/posts/2026-05-15/">← 返回 2026-05-15 速递</a></div>
