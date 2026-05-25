---
title: "Word-Level Modeling with Alignment-Aware Acoustic Fusion for Text-Assisted Intelligibility Prediction in Listeners with Hearing Loss"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音可懂度预测"]
summary: "提出基于对齐感知声学融合的词级建模方法，利用Whisper和参考文本预测听力受损者的语音可懂度。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音可懂度预测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#听力障碍</span> <span class="tag-pill tag-pill-soft">#文本辅助</span> <span class="tag-pill tag-pill-soft">#Whisper</span> <span class="tag-pill tag-pill-soft">#对齐感知</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2605.23604</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-05-25</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2605.23604" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2605.23604" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于对齐感知声学融合的词级建模方法，利用Whisper和参考文本预测听力受损者的语音可懂度。
</div>

## 👥 作者与机构

**Kazushi Nakazawa** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音可懂度预测、听力辅助技术研究者阅读。建议重点读§3.2对齐感知融合模块和§4实验结果，可复现其词级预测框架。

## 🌍 研究背景

语音可懂度预测对助听器评估至关重要，但现有方法多为句子级回归，忽略了词级正确性。CPC3挑战要求预测听力受损者的句子可懂度，实际由参考词识别结果决定。传统方法未充分利用参考文本信息，且缺乏对局部声学特征的精细建模。本文旨在通过词级建模和对齐感知融合提升预测精度。

## 💡 核心创新

1. 参考条件词级正确性建模
2. 基于字符级交叉注意力的词对齐局部声学分支
3. 全局声学分支用于校准
4. 联合融合策略整合文本和声学特征

## 🏗️ 模型架构

输入为退化语音和参考文本。使用冻结Whisper编码器提取语音特征，教师强制解码器以参考文本为条件生成词级隐藏状态。添加两个声学分支：1) 词对齐局部声学分支，通过字符级交叉注意力对齐语音帧与文本词，提取局部声学特征；2) 全局声学分支，对整句语音编码。最后融合解码器状态与两个声学分支，预测每个词的正确概率，句子可懂度由有效参考词的平均正确概率得到。

## 📚 数据集

- CPC3官方数据集（训练/评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| RMSE | CPC3官方评估集 | 解码器基线 24.92 | **联合融合 24.39** | -0.53 |
| 相关系数 | CPC3官方评估集 | 解码器基线 0.795 | **联合融合 0.806** | +0.011 |
| 错误词F1 | CPC3官方评估集 | N/A | **0.778** | N/A |
| MCC | CPC3官方评估集 | N/A | **0.626** | N/A |

在CPC3官方评估集上，联合融合方法相比解码器基线在RMSE上降低0.53，相关系数提升0.011。使用Whisper medium时趋势一致，表明改进源于词级预测粒度和对齐感知融合。消融实验验证了各分支的有效性。

## 🎯 结论与影响

本文通过词级正确性建模和对齐感知声学融合，显著提升了听力受损者语音可懂度预测的准确性。该方法为可懂度预测提供了更细粒度的框架，有望推动助听器个性化评估的发展。

## ⚠️ 局限与未解决问题

仅使用CPC3单一数据集，泛化性未知；未报告推理延迟；未与最新可懂度预测模型（如STOI、ESTOI）对比；词对齐依赖字符级交叉注意力，可能受对齐误差影响。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-05-25/">← 返回 2026-05-25 速递</a></div>
