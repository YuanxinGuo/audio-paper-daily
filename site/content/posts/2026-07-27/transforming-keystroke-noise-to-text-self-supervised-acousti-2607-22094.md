---
title: "Transforming Keystroke Noise to Text: Self-Supervised Acoustic Eavesdropping Attacks on Keyboards"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学侧信道攻击"]
summary: "提出自监督声学侧信道攻击方法，仅凭键盘敲击声重建文本，无需目标设备标注数据，在多种真实场景下达到高重建准确率。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学侧信道攻击</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#键盘声学攻击</span> <span class="tag-pill tag-pill-soft">#Transformer</span> <span class="tag-pill tag-pill-soft">#隐私安全</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2607.22094</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2607.22094" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2607.22094" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出自监督声学侧信道攻击方法，仅凭键盘敲击声重建文本，无需目标设备标注数据，在多种真实场景下达到高重建准确率。
</div>

## 👥 作者与机构

**Atsunori Okada** ¹ · Akira Ito · Rei Ueno · Yuichi Hayashi · Naofumi Homma

**机构**：东北大学（日本）

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合语音/音频安全、隐私保护领域研究者阅读。建议重点读§3方法部分（声学聚类+Transformer语言模型+自训练）和§4实验（不同距离、隔墙、在线会议场景）。可关注其自监督框架如何应对声学-字符映射不确定性。

## 🌍 研究背景

声学侧信道攻击利用设备发出的声音（如键盘敲击）窃取敏感信息。传统方法需目标设备标注数据或特定录音条件，限制了实用性。现有无监督方法在低数据量下准确率低。本文旨在实现无需目标设备标注、仅需少量敲击样本即可高精度重建文本的自监督攻击方法。

## 💡 核心创新

1. 无监督声学聚类与Transformer语言模型结合
2. 迭代自训练框架稳定字符推断
3. 跨平台、远距离、隔墙等真实场景鲁棒性验证

## 🏗️ 模型架构

输入为键盘敲击音频片段，经特征提取后送入无监督聚类模块生成伪标签；然后使用Transformer-based语言模型对字符序列建模，通过迭代自训练优化聚类和语言模型；最终输出重建文本。未提及参数量。

## 📚 数据集

- 自采集键盘敲击数据集（包含多个笔记本电脑平台，近距离、远距离、隔墙、在线会议等场景）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 字符重建准确率 | 近距离录音（智能手机靠近目标设备） | 无监督基线（未明确数值） | **99%** | 显著优于基线 |
| 字符重建准确率 | 远距离录音（约3米同桌面） | 无监督基线 | **>90%** | 显著优于基线 |
| 字符重建准确率 | 隔墙录音（接触式麦克风） | 无监督基线 | **>90%** | 显著优于基线 |
| 字符重建准确率 | 在线会议背景键盘噪声 | 无监督基线 | **>90%** | 显著优于基线 |

在近距离录音下，仅需100-150次敲击即可达到99%准确率；远距离、隔墙、在线会议等场景下，150-250次敲击后准确率超过90%。显著优于先前无监督基线，尤其在低数据量下优势明显。

## 🎯 结论与影响

本文证明仅凭音频即可在无目标设备标注、少量敲击样本下高精度重建键盘输入，揭示了此前被低估的隐私风险。该工作对声学侧信道攻击领域有重要推动作用，可能促使键盘设备厂商加强声学隔离或引入抗侧信道输入机制。

## ⚠️ 局限与未解决问题

实验仅在有限几种笔记本电脑平台上进行，未测试机械键盘或不同声学环境；未报告模型参数量和推理速度；未与有监督方法对比；自训练过程可能对聚类初始化敏感。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-07-27/">← 返回 2026-07-27 速递</a></div>
