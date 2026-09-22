---
title: "LiteCASS: A Lightweight End-to-End Network for Real-Time Stereo Cinematic Audio Source Separation"
date: 2026-09-22T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音分离"]
summary: "LiteCASS 用两个紧凑 U-Net 加 STFT 子带重排，实现 1.06M 参数、0.72G MACs/s 的实时立体声电影音源分离。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#轻量化模型</span> <span class="tag-pill tag-pill-soft">#实时推理</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.23453</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-22</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.23453" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.23453" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>LiteCASS 用两个紧凑 U-Net 加 STFT 子带重排，实现 1.06M 参数、0.72G MACs/s 的实时立体声电影音源分离。
</div>

## 👥 作者与机构

**Yuanxin Guo** ¹ · Qiang Ji · Mengmei Liu · Yuhan Lv · Ningning Pan · Gongping Huang

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做轻量化分离、实时音频部署与电影音源分离的研究者与工程同学。建议通读，重点看 §3 的子带重排与双 U-Net 级联设计、以及立体声扩展 DnR v3 的实验表。可先看表 2 的参数量/MACs 对比，再回看消融确认两阶段分工是否必要。

## 🌍 研究背景

电影音源分离（CASS）需把混音拆成对白、音乐、音效三轨。此前 SOTA 如 DnR、Bandit 等依赖大规模参数网络与 GPU 级算力，难以实时部署；且绝大多数方法只处理单声道，立体声场景几乎空白。本文要解决的是：在资源受限条件下，如何用极轻量端到端网络完成实时立体声 CASS，同时保持分离质量。

## 💡 核心创新

1. 确定性 STFT 子带重排，降低频带建模复杂度
2. 双紧凑 U-Net 级联：先提对白，再从非语音分音乐/SFX
3. 多任务波形域 L1 损失统一监督三路 stem
4. 首个轻量实时立体声 CASS 端到端方案

## 🏗️ 模型架构

输入为立体声波形，经确定性 STFT 子带重排得到紧凑频带表示，送入两个联合训练的紧凑 U-Net。第一个 U-Net 估计对白 stem；第二个 U-Net 在预测的非语音成分上进一步分离音乐与 SFX。输出为波形域三路 stem，用多任务 L1 损失监督。LiteCASS-K8 仅 1.06M 参数、0.72G MACs/s。

## 📚 数据集

- DnR v3 的立体声空间化扩展（训练与评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | 空间化立体声 DnR v3 | 对比的 CASS 基线（具体值摘要未给） | **平均 SI-SDR 最高** | 摘要未给具体数值 |

摘要仅说明 LiteCASS-K8 在对比基线中取得最高平均 SI-SDR，并给出 1.06M 参数与 0.72G MACs/s 的效率指标，未提供逐 stem 的 SI-SDR、PESQ 或消融数值。立体声扩展数据集上的跨条件泛化与实时延迟也未量化。

## 🎯 结论与影响

最强结论是：极轻量双 U-Net 级联即可在立体声 CASS 上超过更重的基线。这为实时电影音源分离与端侧部署提供了可行路线，后续研究可沿子带重排与级联分工继续压缩或提升质量。

## ⚠️ 局限与未解决问题

摘要未给逐 stem 指标、消融与推理延迟，双 U-Net 分工的必要性缺乏验证；评估仅限 DnR v3 空间化扩展，数据集 bias 与真实电影混音泛化未知；与单声道 SOTA 的公平对比也不充分。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-22/">← 返回 2026-09-22 速递</a></div>
