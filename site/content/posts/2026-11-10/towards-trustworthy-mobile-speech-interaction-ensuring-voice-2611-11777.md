---
title: "Towards Trustworthy Mobile Speech Interaction: Ensuring Voice Authenticity and Transmission Integrity"
date: 2026-11-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音水印"]
summary: "MoBiMark利用手机超声波探测声道特征，结合内容嵌入生成双层动态水印，实现实时语音来源认证与传输防篡改。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音水印</span> <span class="tag-pill tag-pill-soft">#声学感知</span> <span class="tag-pill tag-pill-soft">#移动端部署</span> <span class="tag-pill tag-pill-soft">#语音安全</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.11777</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.11777" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.11777" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>MoBiMark利用手机超声波探测声道特征，结合内容嵌入生成双层动态水印，实现实时语音来源认证与传输防篡改。
</div>

## 👥 作者与机构

**Guodong Liu** ¹ · Lei Wang · Dongxu Liu · Qianran Qiao · Haipeng Dai · He Huang · Guihai Chen

**机构**：南京大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音安全、声学感知与移动端系统的研究者阅读。若关注水印鲁棒性或设备端部署，可重点看水印嵌入/检测联合训练部分与INT8量化实验；若关注语音增强/分离则相关性较低，可略读。建议先看系统架构图与攻击评测表。

## 🌍 研究背景

生成式语音模型使高保真克隆与编辑成本极低，基于声纹的移动端身份认证安全性被削弱。现有语音水印多面向离线保护或仅对合成语音加水印，无法在采集时刻验证“这句话确实出自真实说话人”。本文要解决实时采集场景下的来源认证与传输篡改检测问题。

## 💡 核心创新

1. 超声波多频探测提取声道回波特征作为生物签名
2. UID与SID双层动态水印绑定内容与身份
3. 嵌入器与检测器联合训练兼顾音质
4. INT8量化实现手机端轻量部署

## 🏗️ 模型架构

系统在商用手机上发射多频超声波探测信号，采集声道回波并提取回波特征；同时提取内容相关的语音嵌入，二者融合生成双层动态水印（持久UID + 每句SID）。联合训练的嵌入器将水印注入语音，检测器从接收语音中解出水印以完成来源认证与传播篡改检测；系统级优化配合INT8量化支持端侧实时运行。

## 📚 数据集

- 50名用户、4款手机的自采数据集（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 来源与传播攻击平均准确率 | 50用户4机型自采数据 | 未给出具体基线数值 | **99.79%** | — |

摘要仅报告在50名用户、4款手机上的来源与传播攻击平均准确率达99.79%，并称对语音质量与可懂度影响可忽略；未给出与具体水印基线的对比数值、消融实验及推理延迟等效率指标。

## 🎯 结论与影响

最强结论是超声波声道签名与内容嵌入融合的双层水印可在采集时刻完成来源认证与篡改检测。该思路为移动语音交互安全提供了新范式，对端侧语音认证与防伪落地有参考价值。

## ⚠️ 局限与未解决问题

缺少与现有语音水印方法的定量对比与消融；自采50人数据规模与多样性有限，跨设备、跨环境泛化未验证；未报告推理延迟、功耗与超声波探测对用户体验的影响。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-10/">← 返回 2026-11-10 速递</a></div>
