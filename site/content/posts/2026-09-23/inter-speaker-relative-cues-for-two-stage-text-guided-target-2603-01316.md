---
title: "Inter-Speaker Relative Cues for Two-Stage Text-Guided Target Speech Extraction"
date: 2026-09-23T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出两阶段文本引导目标说话人提取框架，用相对线索替代绝对类别线索，先分离候选源再用文本分类器选目标。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音分离</span> <span class="tag-pill tag-pill-soft">#文本引导</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.01316</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-23</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.01316" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.01316" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出两阶段文本引导目标说话人提取框架，用相对线索替代绝对类别线索，先分离候选源再用文本分类器选目标。
</div>

## 👥 作者与机构

**Wang Dai** ¹ · Archontis Politis · Tuomas Virtanen

**机构**：坦佩雷大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TSE、多模态语音前端与文本条件生成的研究者阅读。建议通读，重点看 §2 相对线索的理论论证与 §3 两阶段框架设计，以及分类准确率与 TSE 指标对比表；若只关心结论可先看 WHAM!-noise 鲁棒性实验与线索类型消融。

## 🌍 研究背景

文本引导 TSE 通常用绝对类别属性（如性别、语言）作为条件，但连续值属性在离散化时会丢失细粒度区分。此前 SOTA 多为单阶段文本条件提取（如基于 enrollment 音频的 ECAPA-TDNN 选择），在无注册语音或隐私受限场景下受限。本文要解决：相对线索能否比独立线索保留更多判别信息，以及两阶段框架能否在信号级与感知指标上超越单阶段方法。

## 💡 核心创新

1. 从人类感知与标签量化角度论证相对线索保留细粒度区分
2. 两阶段框架：分离模型生成候选源 + 文本引导分类器选目标
3. 训练两个分类模型对比相对线索与独立线索的判别力
4. 在 WHAM!-noise 下验证文本线索的噪声鲁棒性

## 🏗️ 模型架构

输入为混合语音与文本线索。第一阶段用语音分离模型生成多个候选源；第二阶段对每个候选源提取嵌入，与文本线索嵌入计算相似度，由文本引导分类器选出目标说话人。框架内训练两个独立分类模型分别使用相对线索与独立线索，比较分类准确率与 TSE 性能。摘要未给出具体主干网络名与参数量。

## 📚 数据集

- WHAM!-noise（评估，噪声鲁棒性测试）

## 📊 实验结果

摘要仅给出定性结论：相对线索在整体分类准确率与 TSE 性能上优于独立线索；两阶段框架在信号级与客观感知指标上显著优于单阶段文本条件提取；在受控目标选择对比中，all cues、random cues 与 temporal order 设置优于基于 ECAPA-TDNN 注册音频的强基线，language 与 distance 线索具竞争力；WHAM!-noise 下文本线索噪声鲁棒性强。未提供具体数值。

## 🎯 结论与影响

最强结论是相对文本线索在两阶段 TSE 中同时提升分类准确率与提取性能，并在无注册语音或隐私受限时提供可行替代。该结果提示后续 TSE 研究可重新审视线索表示粒度与两阶段选择范式。工业上可用于无法采集注册音频的个性化语音前端场景。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与参数量，缺少与更多单阶段 TSE 基线的定量对比；两阶段框架引入额外分离与分类开销，未报推理延迟；线索类型判别力差异仅定性描述，缺少消融细节与跨数据集泛化验证。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-23/">← 返回 2026-09-23 速递</a></div>
