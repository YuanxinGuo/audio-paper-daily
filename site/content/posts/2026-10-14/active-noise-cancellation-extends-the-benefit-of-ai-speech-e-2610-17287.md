---
title: "Active noise cancellation extends the benefit of AI speech enhancement in real hearing-aid recordings"
date: 2026-10-14T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "在 KEMAR 上实测三种助听器硬件条件，证明 ANC 通过衰减直通路径，使 AI 语音增强的 SNR 收益从 1.6 dB 提升到 5.1 dB。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#助听器</span> <span class="tag-pill tag-pill-soft">#主动降噪</span> <span class="tag-pill tag-pill-soft">#双耳音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17287</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17287" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17287" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>在 KEMAR 上实测三种助听器硬件条件，证明 ANC 通过衰减直通路径，使 AI 语音增强的 SNR 收益从 1.6 dB 提升到 5.1 dB。
</div>

## 👥 作者与机构

**Andrew T. Sabin** ¹ · Linkai Li

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合助听器算法、AI 语音增强落地、ANC 与听觉前端交叉方向的研究者与工程人员阅读。建议通读，重点看三种硬件条件的对比设置、SII 加权 SNR 的计算方式，以及 §结果中 1500/600/130 Hz 三个截止频率与直通衰减的对应关系。若只关心算法本身可略读，本文核心在硬件-算法协同。

## 🌍 研究背景

AI 语音增强（AI-SE）在耳机与助听器中已能提升 SNR，但助听器存在开放耳道（vent）直通路径：未经处理的原始声音直接抵达鼓膜，与经放大/增强的路径叠加，稀释了算法实际可实现的 SNR 增益。此前仅有仿真预测 ANC 衰减直通路径可放大该收益，缺乏真实硬件录音验证。本文要在真实助听器录音条件下检验这一预测，量化 ANC 对 AI-SE 实际收益的贡献。

## 💡 核心创新

1. 在 KEMAR 上对比标准 RIC、ANC RIC 关/开三种真实硬件条件
2. 用基于干净语音的二值时频掩码估计录音中的语音与噪声谱
3. 以 SII 加权 SNR 量化鼓膜处实际收益，而非仅看算法输出
4. 揭示 AI-SE 收益截止频率随直通路径衰减同步下移（1500→600→130 Hz）

## 🏗️ 模型架构

本文非新网络架构，而是硬件-算法联合测量研究。输入为七种 70 dB SPL 以上真实场景，在 KEMAR 上以 NAL-NL2 目标拟合 N3 听力损失的三种硬件（标准 RIC、ANC RIC 关、ANC RIC 开）录音，AI-SE 算法开/关各录一遍。分析端用由干净语音导出的二值时频掩码从录音中估计语音与噪声谱，据此计算各频段 SNR 与 SII 加权 SNR，并测量直通路径衰减。

## 📚 数据集

- 七种真实声学场景（>70 dB SPL，评估，KEMAR 录音）
- N3 听力损失 NAL-NL2 拟合条件（评估设置）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SII 加权 SNR（AI-SE 开，相对开放耳） | KEMAR 七场景录音 | 标准 RIC 1.6 dB | **ANC RIC（ANC 开）5.1 dB** | +3.5 dB |
| SII 加权 SNR（AI-SE 开，相对开放耳） | KEMAR 七场景录音 | ANC RIC（ANC 关）3.3 dB | **ANC RIC（ANC 开）5.1 dB** | +1.8 dB |
| SII 加权 SNR（AI-SE 关，ANC 开 vs 关） | KEMAR 七场景录音 | ANC 关 | **ANC 开** | +0.2 dB |
| AI-SE 收益 ≥1 dB 的截止频率 | KEMAR 七场景录音 | 标准 RIC 1500 Hz | **ANC RIC（ANC 开）130 Hz** | 下移约 1370 Hz |

AI-SE 在三种条件下高频峰值收益均约 4 dB，但收益维持 ≥1 dB 的频率下限差异显著：标准 RIC 为 1500 Hz，ANC RIC 关为 600 Hz，ANC RIC 开降至 130 Hz，与实测直通路径衰减高度吻合。单独开启 ANC（AI-SE 关）仅带来 0.2 dB 增益，说明 ANC 本身不提升 SNR，而是作为使能技术放大 AI-SE 的收益。摘要未报告推理延迟、参数量或主观听感指标。

## 🎯 结论与影响

最强结论是：ANC 本身几乎不改善 SNR，但通过衰减直通路径，使 AI-SE 的鼓膜处收益从 1.6 dB 提升至 5.1 dB，并把有效频段扩展到 130 Hz。这提示助听器后续研究应将 ANC 与 AI 增强视为协同设计对象，而非独立模块；工业上，具备 ANC 的 RIC 助听器可显著放大现有 AI-SE 算法的实际价值。

## ⚠️ 局限与未解决问题

仅在 KEMAR 单一人工头、N3 听力损失、七场景上验证，缺少真人受试与主观言语可懂度（如 HINT/QuickSIN）结果；未报告算法延迟、功耗与实时性；AI-SE 为单一算法，未验证跨算法泛化；ANC 与 AI-SE 的交互未做消融式频段分析。

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-14/">← 返回 2026-10-14 速递</a></div>
