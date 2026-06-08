---
title: "CA-TCN: A Causal-Anticausal Temporal Convolutional Network for Direct Auditory Attention Decoding"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#听觉注意力解码"]
summary: "提出CA-TCN，一种因果-反因果时间卷积网络，直接从EEG信号分类注意说话人，在多个数据集上提升解码准确率0.5%-3.2%。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#听觉注意力解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#EEG</span> <span class="tag-pill tag-pill-soft">#时间卷积网络</span> <span class="tag-pill tag-pill-soft">#因果-反因果</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.26394</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-08</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.26394" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.26394" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出CA-TCN，一种因果-反因果时间卷积网络，直接从EEG信号分类注意说话人，在多个数据集上提升解码准确率0.5%-3.2%。
</div>

## 👥 作者与机构

I\~nigo Garc\'ia-Ugarte · Rub\'en Eguinoa · Ricardo San Mart\'in · Daniel Paternain · Carmen Vidaurre

**机构**：纳瓦拉公立大学 · 纳瓦拉大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事听觉注意力解码、脑机接口或语音分离的研究者。建议重点阅读§3模型架构和§4实验结果，尤其是表1和表2的对比。可先看§3.2中因果与反因果卷积的设计细节。

## 🌍 研究背景

听觉注意力解码（AAD）旨在从神经信号（如EEG）中识别多说话人场景下听者关注的语音流。现有方法多基于神经夹带，利用低频相关性，但通常需要干净语音源，且模型性能受限于决策窗口长度。此前SOTA如AADNet在subject-independent和subject-specific设置下表现较好，但仍有提升空间。本文提出CA-TCN，通过显式对齐听觉刺激和神经响应，利用因果和反因果卷积分别处理不同时间方向，以提高解码准确性。

## 💡 核心创新

1. 提出因果-反因果时间卷积网络（CA-TCN）
2. 分别使用因果和反因果卷积对齐刺激与神经响应
3. 不同感受野的卷积在相反时间方向操作
4. 集成多种CNN最佳实践于序列处理

## 🏗️ 模型架构

输入为EEG信号和语音包络特征。主干网络为时间卷积网络（TCN），包含因果卷积和反因果卷积两个分支，分别处理刺激和神经响应，感受野不同且方向相反。随后通过融合层整合特征，最后接全连接分类器输出注意说话人标签。模型参数量未在摘要中给出。

## 📚 数据集

- KUL数据集（训练/评估，具体规模未提及）
- DTU数据集（训练/评估，具体规模未提及）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 解码准确率 | KUL | AADNet (subject-independent) 未给出具体值 | **CA-TCN (subject-independent) 提升0.5%-3.2%** | +0.5% to +3.2% |
| 解码准确率 | DTU | AADNet (subject-specific) 未给出具体值 | **CA-TCN (subject-specific) 提升0.8%-2.9%** | +0.8% to +2.9% |

CA-TCN在subject-independent和subject-specific设置下均优于AADNet，准确率提升0.5%-3.2%。在六种评估设置中的四种，最小期望切换持续时间分布差异具有统计显著性。模型在不同数据集上表现出空间鲁棒性，EEG空间滤波器模式稳定。

## 🎯 结论与影响

CA-TCN通过因果-反因果卷积显式对齐刺激与神经响应，在AAD任务上取得一致提升，且具有在线处理潜力。该工作为AAD提供了更准确统一的模型，有望推动其在助听器、智能耳机等实时系统中的应用。

## ⚠️ 局限与未解决问题

摘要未提及模型参数量、推理延迟等效率指标；仅与AADNet等三个基线对比，缺少与最新方法（如基于Transformer的模型）的比较；未报告在更大数据集或更短决策窗口下的表现；未进行消融实验验证因果/反因果卷积的贡献。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-06-08/">← 返回 2026-06-08 速递</a></div>
