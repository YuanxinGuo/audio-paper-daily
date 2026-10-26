---
title: "NECTAR: Automatic Negative Clue Estimation via Centroid-Space Mapping for Target Speaker Extraction"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "利用混合语音质心位于各说话人质心中点的性质，自动估计干扰说话人负线索用于目标说话人提取。"
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
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#负线索建模</span> <span class="tag-pill tag-pill-soft">#说话人表征</span> <span class="tag-pill tag-pill-soft">#Libri2Mix</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32133</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32133" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32133" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用混合语音质心位于各说话人质心中点的性质，自动估计干扰说话人负线索用于目标说话人提取。
</div>

## 👥 作者与机构

**Hyungjun Yoo** ¹ · Yongjoon Lee · Jung-Woo Choi

**机构**：韩国科学技术院

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TSE 与说话人表征的研究者阅读。建议通读，重点看 §3 质心空间关系分析与 CSM 模块设计，以及表 2 中与 enrollment-only 基线的 SI-SDRi 对比；若关注负线索建模可直接复现 CSM 结构。

## 🌍 研究背景

TSE 主流做法是以 enrollment 语音为正向线索（如 SpEx+、VoiceFilter 类方法），通过 speaker embedding 条件化分离网络。痛点在于仅有目标线索，缺少对干扰说话人的显式刻画，当干扰与目标音色接近时容易泄漏。已有工作尝试用 mixture 或干扰估计构造负线索，但难以从目标 enrollment 直接获得干扰表征。本文要解决的是如何从观测混合中自动推导干扰相关的负线索。

## 💡 核心创新

1. 发现混合质心近似位于各说话人质心中点，单句 embedding 不具备该性质
2. 提出 Centroid-Space Mapper (CSM) 从混合与 enrollment 估计质心表征
3. 由质心关系自动导出干扰负线索并注入 TSE 网络

## 🏗️ 模型架构

输入为混合语音与目标 enrollment 语音，分别经说话人编码器提取帧级/句级表征。CSM 模块以混合表征与目标 enrollment 表征为输入，映射到质心空间，估计混合质心与目标质心，再依据质心中点关系反推干扰说话人质心表征，作为负线索。负线索与目标 enrollment 线索共同条件化分离主干（摘要未明确主干网络名），输出目标说话人波形。摘要未给出参数量。

## 📚 数据集

- LibriSpeech train-clean-100（训练）
- Libri2Mix（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi | Libri2Mix | 对比系统（同为 LibriSpeech train-clean-100 训练） | **16.18 dB** | 最高 |

摘要仅报告在 Libri2Mix 上、与同样使用 LibriSpeech train-clean-100 训练的系统相比取得最高 SI-SDRi 16.18 dB，未给出各基线具体数值、消融实验、跨数据集泛化与推理开销信息，负线索贡献的定量消融需见正文。

## 🎯 结论与影响

最强结论是质心空间的中点关系可作为从混合中自动获取干扰负线索的可靠依据，并在 Libri2Mix 上取得领先 SI-SDRi。该思路为 TSE 中负线索建模提供了无需干扰 enrollment 的新途径，对实际场景中干扰未知的部署有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出基线逐项数值与负线索消融，难以判断增益来源；仅在 Libri2Mix 单一合成数据集验证，真实录音与混响条件下质心中点假设是否成立未知；未报告参数量与推理延迟，CSM 估计误差对性能的影响也未讨论。

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
