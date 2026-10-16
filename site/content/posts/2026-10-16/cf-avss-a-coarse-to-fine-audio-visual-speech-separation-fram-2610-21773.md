---
title: "CF-AVSS: A Coarse-to-Fine Audio-Visual Speech Separation Framework with Target-Speaker Refinement and Post-Fusion for Real-World AVSE Challenge"
date: 2026-10-16T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出由粗到细两阶段音视频语音增强框架，用双视觉流SPAV-TFGridNet粗估，再用TFGridNet精炼并后融合，在Real-World AVSE Challenge两赛道CER最低。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#音视频多模态</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.21773</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-16</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.21773" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.21773" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出由粗到细两阶段音视频语音增强框架，用双视觉流SPAV-TFGridNet粗估，再用TFGridNet精炼并后融合，在Real-World AVSE Challenge两赛道CER最低。
</div>

## 👥 作者与机构

**Longjie Luo** ¹ · Zhongshu Hou · Yuepeng Li · Gang Yang · Shidong Shang · Fan Zhou

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频语音分离/增强、多模态目标说话人提取的研究者与竞赛选手阅读。建议重点看第一阶段双视觉流SPAV-TFGridNet的渐进抑制机制、第二阶段TFGridNet精炼网络的设计，以及开发集校准融合策略；表1/表2的OVRL与CER对比值得细读。若关注落地，可先看融合与推理效率部分。

## 🌍 研究背景

音视频语音增强（AVSE）利用视觉线索从含混响、噪声和重叠说话人的混合中恢复目标语音，是近年多模态语音处理热点。此前方法多依赖单阶段AVSE网络或纯音频分离模型（如TFGridNet、SEPFormer），在强干扰与混响下容易残留干扰语音、损伤目标语音质量，且对视觉信息利用不充分。本文针对ISCSLP 2026 Real-World AVSE Challenge的真实场景，提出由粗到细两阶段框架，先粗估再精炼，以同时提升感知质量与识别准确率。

## 💡 核心创新

1. 双同步视觉流扩展SPAV-TFGridNet，渐进抑制干扰语音
2. TFGridNet目标说话人精炼网络，以原混合与双粗估为输入
3. 开发集校准的粗估与精炼结果后融合策略
4. 在真实挑战赛两赛道取得最低CER（12.31%/14.79%）

## 🏗️ 模型架构

输入为含噪混响混合语音及其对应的两路同步视觉流（如唇部/面部）。第一阶段将渐进式SPAV-TFGridNet扩展为双视觉流结构，逐步抑制干扰说话人，同时保留目标混响与共享背景噪声，输出两路视觉有序的粗估。第二阶段以原始混合和两路粗估为输入，经TFGridNet目标说话人精炼网络进一步恢复目标语音、提升信号质量。最后将粗估与精炼结果按开发集校准的融合权重组合，输出最终增强语音。摘要未给出参数量。

## 📚 数据集

- ISCSLP 2026 Real-World AVSE Challenge 数据集（训练/评估，Track 1 与 Track 2）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | Real-World AVSE Challenge Track 1 | 未给出具体基线值 | **12.31%** | 两赛道最低 |
| CER | Real-World AVSE Challenge Track 2 | 未给出具体基线值 | **14.79%** | 两赛道最低 |
| OVRL | Real-World AVSE Challenge Track 1 | 未给出具体基线值 | **并列第一** | 并列第一 |
| OVRL | Real-World AVSE Challenge Track 2 | 未给出具体基线值 | **第二名** | 排名第二 |

摘要仅报告了挑战赛排名与CER：Track 1与Track 2的CER分别为12.31%和14.79%，均为两赛道最低；OVRL在Track 1并列第一、Track 2排名第二。未给出SI-SDR、PESQ、STOI等客观指标数值，也未提供消融实验、参数量或推理延迟信息，具体提升幅度无法量化。

## 🎯 结论与影响

本文最强结论是：由粗到细两阶段AVSE框架配合双视觉流与后融合，在真实AVSE挑战赛两赛道均取得最低CER，验证了渐进抑制加精炼策略的有效性。该思路对多模态目标说话人提取与真实场景语音增强有参考价值，工业上可用于视频会议、助听与直播降噪等需要视觉辅助的目标语音恢复场景。

## ⚠️ 局限与未解决问题

摘要未给出与具体基线的数值对比，缺少SI-SDR/PESQ等客观指标与消融实验，无法判断各模块贡献；两阶段结构可能带来较高推理延迟与参数量，摘要未报告效率指标；融合权重依赖开发集校准，跨域泛化性未知；视觉流质量对性能的影响未讨论。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-16/">← 返回 2026-10-16 速递</a></div>
