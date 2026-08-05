---
title: "Identity-Faithful Audio-Visual Target Speaker Extraction with QIANGDA and VOXBLINK2-AVSE"
date: 2026-08-05T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出QIANGDA基准和VOXBLINK2-AVSE数据集，并设计基于AV-HuBERT特征的目标说话人提取方法，强调身份保真。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音视频融合</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#多视图</span> <span class="tag-pill tag-pill-soft">#说话人验证</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.03964</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-05</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.03964" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.03964" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出QIANGDA基准和VOXBLINK2-AVSE数据集，并设计基于AV-HuBERT特征的目标说话人提取方法，强调身份保真。
</div>

## 👥 作者与机构

**Peijun Yang** ¹ · Zhan Jin · Juan Liu · Ming Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事AV-TSE、多模态语音分离的研究者。建议重点阅读第3节（数据集构建）和第4节（方法），并查看表2和表3的结果。可先浏览摘要和结论，再深入实验部分。

## 🌍 研究背景

音频-视觉目标说话人提取旨在利用视频线索分离目标语音，但现有方法可能忽略视觉信息，输出声学上占主导的说话人。缺乏大规模真实场景的AV-TSE基准，且评估指标多关注内容而忽视身份保真。本文构建了中文真实双说话人混合基准QIANGDA，并扩展了大规模AV-TSE数据集，同时提出身份保真的提取方法。

## 💡 核心创新

1. 构建QIANGDA基准，含真实双说话人混合和多视角视频
2. 从VoxBlink2构建大规模AV-TSE数据集VOXBLINK2-AVSE
3. 使用冻结AV-HuBERT特征和层式特征调制
4. 联合评估内容CER和身份准确性
5. 引入OSD检测重叠语音以提升评估可靠性

## 🏗️ 模型架构

输入为混合音频和视频（唇部区域），提取AV-HuBERT特征（冻结，1280维投影），通过目标条件训练和层式特征调制，将视觉特征注入分离网络。分离网络可能基于Conformer或类似结构，输出目标说话人音频。

## 📚 数据集

- QIANGDA（训练/评估，77场景，7598片段，11.84小时，含6042双标注混合）
- VOXBLINK2-AVSE（训练，250828对音频-唇部ROI，28421身份，766.17小时）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| CER | QIANGDA完整清单 | 未提供 | **0.2261** | N/A |
| 严格输出正确率 | QIANGDA完整清单 | 未提供 | **82.22%** | N/A |
| 双输出严格成功率 | QIANGDA完整清单 | 未提供 | **69.53%** | N/A |

在QIANGDA完整清单上，最佳存档检查点获得0.2261 CER，82.22%严格输出正确率，69.53%双输出严格成功率。这些指标表明方法在内容准确性和身份保真方面表现良好，但缺乏与现有方法的对比。

## 🎯 结论与影响

本文通过构建真实场景基准和大规模数据集，推动了AV-TSE研究，并提出了身份保真的提取方法。该方法在内容准确性和身份保真上取得较好平衡，为后续研究提供了新基准和评估协议。对工业应用，如会议系统、助听设备，具有潜在价值。

## ⚠️ 局限与未解决问题

缺乏与现有AV-TSE方法的对比实验；QIANGDA仅含中文，可能限制泛化性；评估指标依赖ASR和说话人识别，可能受其错误影响；未报告推理效率。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-05/">← 返回 2026-08-05 速递</a></div>
