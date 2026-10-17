---
title: "Backward Compatibility in Zero-Bit Neural Audio Watermarking"
date: 2026-10-17T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频水印"]
summary: "形式化零比特音频水印的向后兼容问题，用冻结旧嵌入器链训练新检测器，并用角度多样性损失抑制嵌入器坍缩。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频水印</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#音频水印</span> <span class="tag-pill tag-pill-soft">#零比特水印</span> <span class="tag-pill tag-pill-soft">#对抗鲁棒性</span> <span class="tag-pill tag-pill-soft">#模型版本兼容</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.22296</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.22296" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.22296" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>形式化零比特音频水印的向后兼容问题，用冻结旧嵌入器链训练新检测器，并用角度多样性损失抑制嵌入器坍缩。
</div>

## 👥 作者与机构

**Admir Krnić** ¹ · Kosta Pavlović · Petar Nedić · Željko Bolević · Slavko Kovačević · Igor Djurović

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音频水印、模型版本管理与安全部署的研究者阅读。建议通读，重点看 §3 的 legacy chain 训练框架与 ADL 定义，以及 TNR 相关实验表；若只关心方法，可先看 ADL 的损失公式与消融。

## 🌍 研究背景

神经音频水印通常把嵌入器与检测器成对联合训练，隐含假设部署静态不变。实际系统中嵌入器与检测器会因安全与版本管理被选择性更新或解耦，导致旧内容检测失效，更严重的是检测器对非目标嵌入器产生高误报。此前工作多关注鲁棒性与不可感知性，较少形式化跨版本兼容与负样本误报问题，本文针对这一部署痛点提出训练框架。

## 💡 核心创新

1. 形式化零比特音频水印的向后兼容定义
2. 冻结旧嵌入器链 + 性能加权采样训练新检测器
3. 提出 Angular Diversity Loss 抑制嵌入器坍缩
4. 揭示并量化 TNR 对链外嵌入器的灾难性退化

## 🏗️ 模型架构

输入为音频波形，嵌入器与检测器均为神经网络（摘要未给出具体主干与参数量）。训练时新检测器与一串冻结的 legacy 嵌入器组成 legacy chain，按各版本性能加权采样训练样本，使检测器覆盖所有历史版本。新嵌入器训练时额外加入 Angular Diversity Loss，在输出空间约束其与链内嵌入器角度分离，避免嵌入器坍缩，从而恢复对链外嵌入器的真负率。

## 📊 实验结果

摘要未给出具体数据集、指标数值或参数量，仅定性说明：组合方法在检测准确率与感知音频质量无明显损失的前提下，将链外嵌入器的 TNR 恢复到接近完美水平，并指出仅用 legacy chain 训练会造成 TNR 灾难性下降。

## 🎯 结论与影响

最强结论是向后兼容可通过冻结旧嵌入器链训练新检测器实现，但必须配合角度多样性约束才能避免负样本误报。该工作为水印系统的版本演进与安全解耦提供了可操作训练范式，对工业界水印模型迭代部署有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报告具体数据集、TNR/准确率数值、感知质量指标与推理开销，缺少与现有水印基线的定量对比；legacy chain 长度增长时的可扩展性与存储成本未讨论；ADL 权重敏感性缺少消融说明。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-10-17/">← 返回 2026-10-17 速递</a></div>
