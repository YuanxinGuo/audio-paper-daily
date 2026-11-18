---
title: "A 1000-hour EEG-EMG-audio dataset of Japanese speech production"
date: 2026-11-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#脑电语音解码"]
summary: "发布1020小时日语语音产生同步EEG-EMG-音频多模态数据集，含三种EEG设备与事件标注。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.0</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#脑电语音解码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#多模态数据集</span> <span class="tag-pill tag-pill-soft">#EEG</span> <span class="tag-pill tag-pill-soft">#EMG</span> <span class="tag-pill tag-pill-soft">#语音产生</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.01264</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.01264" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.01264" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布1020小时日语语音产生同步EEG-EMG-音频多模态数据集，含三种EEG设备与事件标注。
</div>

## 👥 作者与机构

**Motoshige Sato** ¹ · Ilya Horiguchi · Masakazu Inoue · Kenichi Tomeoka · Eri Hatakeyama · Yuya Kita · Atsushi Yamamoto · Ippei Fujisawa · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做EEG语音解码、多模态信号处理与跨设备适配的研究者。值得浏览数据描述与验证部分，重点看§技术验证（PSD与ERP分析）及BIDS组织方式；若关注建模方法则本文贡献有限，可仅参考数据规模与设备配置。

## 🌍 研究背景

EEG语音解码长期受限于数据规模小、设备单一、缺乏同步音频与肌电标注。此前公开数据集多为小时级、单设备、朗读词表受限，难以支撑跨设备与纵向研究。本文针对该痛点构建千小时级、多设备、开放词汇的日语语音产生多模态数据集，并附带技术验证。

## 💡 核心创新

1. 1020小时同步EEG-EMG-音频三模态记录
2. 三种EEG系统（61-128通道）跨设备采集
3. 开放词汇朗读+默读复述+听语音三任务范式
4. BIDS格式+语音事件标注与转写

## 🏗️ 模型架构

非模型论文。数据采集流程：受试者执行开放词汇朗读、默读复述与听语音任务，同步记录头皮EEG（g.Pangolin超高密度及g.SCARABEO、eego sports帽式系统，61-128通道）、面部EMG与语音音频；每会话提供时间同步信号、语音事件标注与转写。验证采用功率谱密度与事件相关电位分析刻画跨被试、跨设备、跨任务的频谱与锁时响应。

## 📚 数据集

- 自建EEG-EMG-音频数据集（训练/研究用，1020小时，3名日语母语者）
- Harvard Dataverse（受控访问发布，BIDS格式）

## 📊 实验结果

摘要未给出具体量化指标，仅说明通过功率谱密度与事件相关电位分析验证了跨被试、跨设备、跨任务的频谱特征与锁时响应一致性。未报告解码基线性能、跨设备迁移增益或推理效率等数据。

## 🎯 结论与影响

最强结论是提供了目前规模领先的日语语音产生同步EEG-EMG-音频多模态资源。该数据可推动跨设备适配、纵向建模与EEG表征学习，为语音解码研究提供标准化基准；工业上对脑机接口与辅助沟通系统的数据积累有参考价值。

## ⚠️ 局限与未解决问题

仅3名被试，泛化性受限；语音音频经voice-masking处理，可能影响声学建模；未提供解码基线或跨设备迁移实验，验证仅停留在频谱与ERP层面；受控访问限制复现便利性。

---

<div class="paper-footer"><span>评分：6.0</span><span>原始：6.0</span><a href="/audio-paper-daily/posts/2026-11-18/">← 返回 2026-11-18 速递</a></div>
