---
title: "PromptSep-Speaker: Generative Target Speaker Extraction via Multimodal Prompting and Semantic Alignment"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "用潜扩散生成式框架统一四种目标线索（时序、文本、注册音频、说话人描述）做目标说话人提取，并用冻结 WavLM 对齐损失监督交叉注意力。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">9.2</div>
<div class="score-stars">★★★★★</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#扩散模型</span> <span class="tag-pill tag-pill-soft">#多模态提示</span> <span class="tag-pill tag-pill-soft">#语音分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.23066</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">🔥 强烈推荐通读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.23066" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.23066" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用潜扩散生成式框架统一四种目标线索（时序、文本、注册音频、说话人描述）做目标说话人提取，并用冻结 WavLM 对齐损失监督交叉注意力。
</div>

## 👥 作者与机构

**Yutong Wen** ¹ · Ke Chen · Prem Seetharaman · Haonan Chen · Oriol Nieto · Paris Smaragdis · Justin Salamon · Zeyu Jin

**机构**：Adobe Research · 伊利诺伊大学厄巴纳-香槟分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做 TSE、生成式语音分离与多模态提示的研究者精读。建议重点看 §3 的多线索条件注入设计与 WavLM 对齐损失，以及表 2/表 3 的分线索对比和听测结果；若关注落地，需额外核查推理步数与延迟。

## 🌍 研究背景

TSE 此前主流是掩码预测模型（如基于 Conformer/BSRNN 的判别式系统），依赖注册音频或文本描述等单一线索，且掩码方法易产生可听伪影、跨声学条件泛化差。单一线索又难以同时做到广泛可得与可靠判别。本文要解决的是：如何在生成式框架下统一多种可互换线索，并让模型充分利用每种线索而不需额外标注。

## 💡 核心创新

1. 潜扩散生成式 TSE 框架，统一四种可互换线索
2. 时序/文本/注册音频/说话人描述四类条件注入
3. 冻结 WavLM 表征 + 辅助对齐损失监督 query-mixture 交叉注意力
4. 无需额外标注即可获得线索-混合对齐监督

## 🏗️ 模型架构

输入为混合语音与目标线索（说话人时序、转写文本、注册音频、说话人 caption）。线索经各自编码器映射为条件嵌入，通过 query-mixture 交叉注意力注入潜扩散主干；扩散在潜空间去噪生成目标语音，再由解码器还原波形。冻结 WavLM 提供表征，辅助对齐损失约束交叉注意力与目标语音语义一致，无需额外标签。摘要未给出参数量。

## 📚 数据集

- 四个评估集（评估，具体名称摘要未列）
- 听测研究（主观评估）

## 📊 实验结果

摘要称在四个评估集与一项听测研究中，PromptSep-Speaker 在 TSE 与通用源分离基线上取得 SOTA，分离准确度与质量在各线索模态上均有提升；但摘要未给出 SI-SDR、PESQ、MOS 等具体数值，无法量化对比。

## 🎯 结论与影响

最强结论是生成式建模加多模态提示可同时提升分离质量与场景适用性。这为 TSE 从掩码范式转向扩散生成、并统一异构线索提供了可复用路线，对工业上多入口（注册音频/文本/描述）的个性化提取有直接参考价值。

## ⚠️ 局限与未解决问题

摘要未报推理步数与延迟，扩散模型实时性存疑；四个评估集名称与具体指标缺失，无法判断跨条件泛化；对齐损失与各线索的消融细节未在摘要体现；与最新判别式 TSE 的公平对比需看正文。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
