---
title: "Modeling and Link Budget Feasibility Analysis of Secure LoRa-Based Peer-to-Peer Communication for Short-Range Tactical Networks"
date: 2026-11-20T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声学模拟"]
summary: "提出基于LoRa的微型加密语音对讲设备方案，用链路预算论证1-1.5km视距通信可行性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">3.5</div>
<div class="score-stars">★★☆☆☆</div>
<div class="score-tier">后50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声学模拟</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#LoRa通信</span> <span class="tag-pill tag-pill-soft">#链路预算分析</span> <span class="tag-pill tag-pill-soft">#语音加密传输</span> <span class="tag-pill tag-pill-soft">#战术通信</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2602.23924</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-20</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">✋ 可以跳过</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2602.23924" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2602.23924" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于LoRa的微型加密语音对讲设备方案，用链路预算论证1-1.5km视距通信可行性。
</div>

## 👥 作者与机构

**Ayush Kumar Agrawal** ¹ · Soumendu Das · Rashmi Keshri · Saptaparna De · Jayendra Kumar

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做战术通信、低功耗物联网语音终端的工程读者浏览。本文偏系统设计与链路预算推导，非语音信号处理算法研究，语音/音频顶会读者价值有限。若关注LoRa语音传输可行性，可重点看链路预算推导与AES-128加密流程两节，其余可略读。

## 🌍 研究背景

战术、军事与灾害救援场景常缺乏可用通信基础设施，且易被截获。现有VHF/UHF电台与软件定义电台体积大、功耗高，难以做成轻量可穿戴免手持设备。LoRa凭借chirp扩频调制具备远距离、低功耗、低电磁足迹特性，但此前多用于IoT遥测，鲜有面向安全语音对讲的系统级设计与链路预算论证。本文要解决的是：在视距条件下用LoRa构建1-1.5km微型加密语音对讲终端的可行性与理论框架。

## 💡 核心创新

1. 语音激活采集+数字音频压缩的低功耗前端链路
2. AES-128加密后经LoRa chirp扩频低功耗发射
3. 基于链路预算的1-1.5km视距通信距离理论论证
4. 面向可穿戴免手持的人体工学与基础设施无关设计

## 🏗️ 模型架构

系统为端到端嵌入式链路：输入端由语音激活采集模块（VAD触发）拾取语音，经数字音频压缩降低码率，送入嵌入式微控制器处理；随后进行AES-128加密，再通过LoRa收发模块以chirp扩频调制低功耗发射。接收端对称解密并回放。论文侧重系统框图与链路预算推导，未给出神经网络或信号处理主干网络，也未报告参数量；核心是发射功率、路径损耗、接收灵敏度与扩频增益构成的链路预算方程，用以论证1-1.5km视距可达性。

## 📊 实验结果

摘要未给出任何量化实验结果，如误码率、语音质量（PESQ/MOS）、端到端时延、实测通信距离或功耗数据，仅以链路预算理论推导论证通信距离可行性，缺少实测验证与对比基线。

## 🎯 结论与影响

最强结论是链路预算表明LoRa可在视距下支撑1-1.5km的加密语音对讲。对低功耗战术语音终端方向有工程参考价值，提示LoRa可超出IoT遥测范畴用于安全语音平台。工业落地上面向可穿戴免手持应急通信有一定潜力，但需实测数据支撑。

## ⚠️ 局限与未解决问题

仅有理论链路预算，缺实测距离、误码率、语音质量与功耗数据；未与现有VHF/UHF或SDR方案做量化对比；无消融分析；视距假设限制了复杂传播环境适用性；语音压缩与加密对时延和音质的影响未评估。

---

<div class="paper-footer"><span>评分：3.5</span><span>原始：3.5</span><a href="/audio-paper-daily/posts/2026-11-20/">← 返回 2026-11-20 速递</a></div>
