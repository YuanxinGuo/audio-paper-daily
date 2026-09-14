---
title: "Real-Time Music Source Separation on a Low-Power Audio DSP"
date: 2026-09-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "在2MB SRAM、2.07 GMAC/s的低功耗音频DSP上实现实时音乐源分离，MUSDB18-HQ达4.70 dB cSDR，10.43 ms/11.6 ms hop。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#乐器分离</span> <span class="tag-pill tag-pill-soft">#实时推理</span> <span class="tag-pill tag-pill-soft">#嵌入式部署</span> <span class="tag-pill tag-pill-soft">#模型压缩</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.12201</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-14</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.12201" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.12201" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在2MB SRAM、2.07 GMAC/s的低功耗音频DSP上实现实时音乐源分离，MUSDB18-HQ达4.70 dB cSDR，10.43 ms/11.6 ms hop。
</div>

## 👥 作者与机构

**Jianan Li** ¹ · Li Liu · Ken Malsky · Gabby Yi

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做实时音频部署、嵌入式模型压缩、音乐分离工程化的读者。建议通读，重点看 §3 的连续卷积上下文训练与 gated complex FIR deep filter 设计，以及表 2 的 MAC/内存约束对比；若只关心算法，可先看消融部分。

## 🌍 研究背景

音乐源分离在桌面 CPU/GPU 上已有 TasNet、X-UMX、RT-STT 等实时系统，但均未针对嵌入式音频 DSP 的 2 MB SRAM 与 2.07 GMAC/s 约束设计。16–51 M 参数的 TasNet/X-UMX 家族受内存限制，RT-STT 则需 5.5 倍可用 MAC 率，参数计数也无法预测实际可行性（权重复用跨度 1x–345x）。本文要回答：能否在商用低功耗 DSP 上构建真正可运行的实时音乐分离系统。

## 💡 核心创新

1. 连续而非分块补零卷积上下文训练，避免逐帧推理崩溃
2. 门控复数 FIR deep filter，提供延迟可调旋钮
3. 严格因果下仍增益 0.38 dB 的轻量分离架构
4. 面向 2 MB SRAM / 2.07 GMAC/s 的嵌入式协同设计

## 🏗️ 模型架构

输入为波形帧，主干采用轻量卷积分离网络，核心是门控复数 FIR deep filter 模块，在频域对复数谱做可调延迟的滤波增强。训练时使用连续卷积上下文而非 block-padded 方式，保证逐帧推理时状态一致。模型参数量与权重复用经过嵌入式约束优化，输出各 stem 的复数掩蔽或滤波后频谱，逆变换回波形。摘要未给出具体参数量，但强调适配 2 MB SRAM 与 2.07 GMAC/s。

## 📚 数据集

- MUSDB18-HQ（评估，音乐源分离标准测试集）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| cSDR | MUSDB18-HQ | 不适用嵌入式的系统（约 5.2–5.4 dB） | **4.70 dB** | 落后 0.5–0.7 dB |

摘要给出 cSDR 4.70 dB，落后不适配嵌入式的系统 0.5–0.7 dB；推理耗时 10.43 ms，满足 11.6 ms hop 实时约束。训练上下文消融显示：block-wise 训练模型 3.93 dB，但逐帧推理 2 秒内崩溃为静音；连续上下文训练是可行关键。门控复数 FIR deep filter 在严格因果下仍带来 0.38 dB 增益。未报告参数量、内存占用细节与更多基线对比。

## 🎯 结论与影响

本文证明在 2 MB SRAM、2.07 GMAC/s 的低功耗 DSP 上可实时运行音乐源分离，cSDR 4.70 dB 仅落后大模型 0.5–0.7 dB。连续卷积上下文训练与门控复数 FIR deep filter 为嵌入式音频分离提供了可复用设计范式，对耳机、助听器、便携播放器等端侧音乐处理有直接落地意义。

## ⚠️ 局限与未解决问题

仅在一个 DSP 平台验证，未给出参数量、峰值内存与功耗数据；对比基线未列出具体系统名与完整指标；MUSDB18-HQ 单一数据集，缺乏跨域泛化；未讨论多通道或双耳扩展；训练上下文崩溃现象仅定性描述，缺少系统性消融。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-14/">← 返回 2026-09-14 速递</a></div>
