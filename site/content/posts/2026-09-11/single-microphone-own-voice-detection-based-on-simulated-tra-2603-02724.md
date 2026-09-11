---
title: "Single Microphone Own Voice Detection based on Simulated Transfer Functions for Hearing Aids"
date: 2026-09-11T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "用解析与数值模拟的声学传递函数做数据增强，训练单麦克风自语音检测 Transformer 分类器，仿真集 95.52%，真实录音少样本微调达 91%。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#助听器</span> <span class="tag-pill tag-pill-soft">#数据增强</span> <span class="tag-pill tag-pill-soft">#声学传递函数</span> <span class="tag-pill tag-pill-soft">#Transformer</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.02724</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-11</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.02724" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.02724" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用解析与数值模拟的声学传递函数做数据增强，训练单麦克风自语音检测 Transformer 分类器，仿真集 95.52%，真实录音少样本微调达 91%。
</div>

## 👥 作者与机构

**Mathuranathan Mayuravaani** ¹ · W. Bastiaan Kleijn · Andrew Lensen · Charlotte S{\o}rensen

**机构**：惠灵顿维多利亚大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做助听器/可穿戴语音前端、单通道声学事件检测的研究者与工程团队阅读。建议重点看 §3 的 ATF 模拟与分层微调流程、以及真实录音 few-shot 实验小节；表 1/表 2 的仿真与真实域精度对比值得细看。若只关心分离/增强主干网络，可略读。

## 🌍 研究背景

自语音检测（OVD）可提升助听器佩戴舒适度与语音可懂度，但现有方案多依赖双麦克风或额外传感器（如加速度计、骨导），增加体积、功耗与成本。单麦克风 OVD 因缺乏空间线索而困难，且基于机器学习的方法通常需要昂贵的传递函数实测数据，难以规模化。本文要解决的是：在无实测 ATF 的条件下，仅靠仿真数据训练出可迁移到真实助听器录音的单麦 OVD 模型。

## 💡 核心创新

1. 基于解析 ATF 的数据增强，覆盖大范围空间传播条件
2. 解析→数值仿真 ATF 的分层微调，逐步提升几何真实性
3. Transformer 分类器 + 真实录音 few-shot 微调适配
4. 验证 1 秒短语音段下的鲁棒性

## 🏗️ 模型架构

输入为单通道语音片段（含 1 秒短段）的声学特征，经特征提取后送入 Transformer 编码器做二分类（自语音 / 非自语音）。训练分两阶段：先用解析生成的 ATF 卷积语音构造大规模仿真训练集，使模型学习宽泛的空间传播模式；再用数值模拟（更真实几何）的 ATF 微调，细化空间理解并保持泛化。最终在真实助听器录音上用少量样本 few-shot 微调。摘要未给出参数量与具体特征维度。

## 📚 数据集

- 解析 ATF 仿真数据（训练，数据增强生成）
- 数值模拟 ATF 数据（微调，几何更真实）
- 仿真头与躯干测试集（评估，95.52% 准确率）
- 真实助听器录音（评估/少样本微调，91% 准确率）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 仿真头与躯干测试集 | 未给出 | **95.52%** | — |
| Accuracy | 1 秒语音段 | 未给出 | **90.02%** | — |
| Accuracy | 真实助听器录音（few-shot 微调） | 未给出 | **91%** | — |

摘要报告仿真头与躯干测试集 95.52% 准确率，1 秒短语音段 90.02%，说明对短时长具有鲁棒性；真实助听器录音经少量样本 few-shot 微调后达 91%，表明仿真训练模型可有效适配真实域。摘要未给出与多麦克风/传感器基线的对比数值，也未报告推理延迟、参数量或消融实验细节。

## 🎯 结论与影响

最强结论是：仅用仿真 ATF 训练的单麦克风 OVD 模型，经少量真实数据微调即可在助听器录音上达到 91% 准确率。这为免实测传递函数的单麦 OVD 提供了可行路径，可能推动助听器硬件简化与功耗下降，并启发用仿真数据做声学域适配的后续研究。

## ⚠️ 局限与未解决问题

缺少与多麦克风/传感器 OVD 基线的定量对比，也未报告模型参数量、推理延迟与功耗，难以评估实际部署可行性。真实录音评估规模与说话人/环境多样性未说明，few-shot 微调所需样本量与选取策略不透明，消融实验（解析 vs 数值 ATF 各自贡献）在摘要中缺失。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-11/">← 返回 2026-09-11 速递</a></div>
