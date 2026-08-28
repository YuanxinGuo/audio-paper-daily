---
title: "Soft Active Electromyography Interface for Machine Learning-Enabled Silent Speech Recognition"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#无声语音识别"]
summary: "提出一种软性主动肌电接口，通过指尖电极采集唇部附近EMG信号，结合深度学习实现30词无声语音识别，准确率97.2%，并验证了无人机实时控制。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#无声语音识别</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#肌电信号</span> <span class="tag-pill tag-pill-soft">#可穿戴设备</span> <span class="tag-pill tag-pill-soft">#人机交互</span> <span class="tag-pill tag-pill-soft">#深度学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.27048</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-28</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.27048" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.27048" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出一种软性主动肌电接口，通过指尖电极采集唇部附近EMG信号，结合深度学习实现30词无声语音识别，准确率97.2%，并验证了无人机实时控制。
</div>

## 👥 作者与机构

**Yuta Kurotaki** ¹ · Shusuke Yamakoshi · Reitaro Yoshida · Yutaka Isoda · Tamami Takano · Yuji Isano · Yusuke Miyake · Kentaro Kuribayashi · … 等 1 人

**机构**：横滨国立大学 · 东京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合人机交互、可穿戴传感和语音识别交叉领域的研究者。建议重点阅读系统设计（§2）和实验部分（§3），特别是电极布局和信号稳定性分析。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

无声语音识别（SSR）为无声环境提供替代通信方式，但传统方法需持续面部附着、存在隐私问题且信号采集不稳定。现有SSR多基于表面肌电（sEMG）或超声，但电极需固定于面部，影响舒适性和实用性。本文旨在开发一种按需采集、高稳定性的软性EMG接口，实现词级SSR，并验证其在噪声环境下的实际应用。

## 💡 核心创新

1. 软性主动EMG接口，指尖电极按需靠近唇部采集信号
2. 集成液态金属互连、透明FPC电极和弹性体封装，确保机械稳定性
3. 深度学习模型实现97.2%的30词分类准确率
4. 实时无人机控制验证在噪声和隐私敏感环境中的实用性

## 🏗️ 模型架构

系统由软性主动EMG接口和深度学习分类器组成。接口采用液态金属互连、透明柔性印刷电路（FPC）电极和弹性体封装，佩戴于手部，指尖电极可移动至唇部附近采集EMG信号。信号经放大和滤波后，输入深度神经网络（DNN）进行词分类。DNN结构未详细说明，但训练后达到97.2%准确率。

## 📚 数据集

- 自建数据集（3名受试者，30词词汇，用于训练和评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | 自建30词词汇 | 未提及 | **97.2% ± 1.3%** | N/A |

实验在3名受试者上进行，平均准确率97.2%±1.3%，表明系统能稳健区分30个词。实时无人机控制实验验证了在噪声和隐私敏感环境中的实用性，但未提供与现有SSR方法的定量对比。

## 🎯 结论与影响

本文展示了软性可穿戴EMG系统在无声语音识别中的潜力，通过按需采集和稳定信号实现高准确率，为安全直观的人机交互提供了新途径。该研究可能推动SSR在助残、军事和消费电子等领域的应用，但需进一步扩大词汇量和受试者规模。

## ⚠️ 局限与未解决问题

实验规模小（3名受试者），词汇量有限（30词），未与现有SSR方法（如基于面部EMG或超声）进行对比。系统需手动移动电极至唇部，可能影响使用便捷性。未报告模型参数量和推理延迟，实时性验证仅限无人机控制。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：7.8</span><a href="/audio-paper-daily/posts/2026-08-28/">← 返回 2026-08-28 速递</a></div>
