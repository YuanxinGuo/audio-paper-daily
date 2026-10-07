---
title: "Audiovisual joint learning for end-to-end hearing aids"
date: 2026-10-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出 AV-NeuroAMP，端到端融合含噪语音、目标说话人视频与听力图，联合完成语音增强、个性化放大与动态范围压缩。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#听力辅助</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.08579</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.08579" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.08579" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出 AV-NeuroAMP，端到端融合含噪语音、目标说话人视频与听力图，联合完成语音增强、个性化放大与动态范围压缩。
</div>

## 👥 作者与机构

**You-Jin Li** ¹ · Yu Tsao · Borching Su · Kuan-Chung Ting · Fan-Gang Zeng

**机构**：台湾中央研究院 · 台湾大学 · 加州大学欧文分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合助听器算法、AV 语音分离与个性化增强方向的研究者与工程团队阅读。建议通读，重点看 §3 中 AC-FiLM 的调制方式与端到端联合训练目标，以及表 2/表 3 的客观与主观结果；若关注落地，需额外核对推理延迟与助听器算力预算。

## 🌍 研究背景

助听器在竞争说话人场景下的语音理解仍困难。传统方案将语音增强（SE）与听力损失补偿分两阶段处理，增强误差与信号失真会传递到放大级；纯音频 SE 在目标与干扰语音声学特征相近时收益有限。已有工作多依赖音频单模态或分阶段流水线，缺少将目标说话人视觉线索与听者听力图统一建模的端到端框架。本文要解决的是：如何在含竞争说话人的噪声中，联合完成个性化增强与放大。

## 💡 核心创新

1. 提出 AV-NeuroAMP 端到端视听框架，联合 SE、个性化放大与动态范围压缩
2. 设计 AC-FiLM，用听力图条件调制特征以注入听者特异听力曲线
3. 引入目标说话人视频作为线索，缓解竞争语音下音频单模态分离困难
4. 在未见 Mandarin 测试集上验证跨语言泛化能力

## 🏗️ 模型架构

输入为含噪语音、目标说话人视频与听者听力图三路信息。音频与视频特征经各自编码器提取后融合，主干完成语音增强；听力图通过 AC-FiLM 生成逐通道的缩放与偏置，对中间特征做特征级线性调制，从而注入听者特异听力曲线。增强后的表示继续经过个性化放大与动态范围压缩模块，最终输出可直接驱动助听器的语音波形。整体为端到端可训练框架，摘要未给出具体参数量与主干网络名。

## 📚 数据集

- 域内英语测试集（评估，摘要未具名）
- 未见 Mandarin 测试集（跨语言评估，摘要未具名）

## 📊 实验结果

摘要仅给出定性结论：AV-NeuroAMP 在域内英语测试集上优于传统放大、纯音频 NeuroAMP 与两阶段系统，且改进在未见 Mandarin 测试集上保持。听力测试包含模拟听力损失的正常听力受试者与真实听力损失听者，语音质量与可懂度均有提升，竞争说话人条件下收益最大。摘要未提供 SI-SDR、PESQ、WER 或 MOS 等具体数值，故无法列出量化对比。

## 🎯 结论与影响

最强结论是端到端视听个性化放大在竞争语音场景下优于分阶段与传统助听方案，且跨语言仍成立。这为助听器算法从“先增强后补偿”转向联合优化提供了实证支持，可能推动后续研究将听力图与视觉线索纳入统一可微框架。工业上若算力与延迟可控，有望改善真实助听器在多人交谈环境中的可用性。

## ⚠️ 局限与未解决问题

摘要未给出任何客观指标数值、参数量与推理延迟，难以判断相对 SOTA 的实际增益幅度；测试集未具名，训练/评估数据规模与说话人重叠情况不明；缺少消融验证 AC-FiLM 与视觉分支各自贡献；听力测试样本量与统计显著性未报告；端到端系统在助听器低功耗芯片上的可行性未讨论。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-07/">← 返回 2026-10-07 速递</a></div>
