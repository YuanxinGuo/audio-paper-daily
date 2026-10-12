---
title: "QC-MI-OVSEL: Benchmarking Query-Conditioned Multi-Instance Open-Vocabulary Sound Event Localization"
date: 2026-10-12T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#声源定位"]
summary: "提出查询条件多实例开放词汇声事件定位基准与Q-RSet方法，用查询槽与责任聚合预测声源集合。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#声源定位</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#开放词汇</span> <span class="tag-pill tag-pill-soft">#多实例学习</span> <span class="tag-pill tag-pill-soft">#双耳音频</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.13198</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.13198" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.13198" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出查询条件多实例开放词汇声事件定位基准与Q-RSet方法，用查询槽与责任聚合预测声源集合。
</div>

## 👥 作者与机构

**Yongqiang Chen** ¹ · Peiwei Chang · Yuelan Cheng · Xiatian Zhu · Wenwu Wang

**机构**：上海交通大学 · 萨里大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做声事件定位、开放词汇检测与空间音频的研究者阅读。建议通读，重点看 §3 基准构建流程与 Q-RSet 的查询条件槽设计，以及表 2 中 cardinality 与 absent-query 抑制的消融。若只关心方法，可先看 §4 与实验表。

## 🌍 研究背景

声事件定位与检测（SELD）此前多在闭集类别上评测，DCASE 任务使用固定类别与强标注。开放词汇与查询条件设定下，系统需按自然语言类别查询恢复所有匹配声源，并处理查询类别不存在的情况。现有方法多依赖闭集分类头或单实例假设，难以处理多实例、类别缺失与释义查询，本文为此定义 QC-MI-OVSEL 任务并给出基准与方法。

## 💡 核心创新

1. 定义查询条件多实例开放词汇声事件定位任务与评测协议
2. 构建 4 万场景 FOA 基准，含 83 类与 17 个新类
3. 提出 Q-RSet：查询条件源槽 + 责任证据聚合
4. 支持 absent-query 抑制与基数估计的集合预测

## 🏗️ 模型架构

输入为第一阶 Ambisonics（FOA）多通道音频，提取空间与频谱特征后送入主干网络编码帧级表示。Q-RSet 将自然语言查询编码为查询条件源槽，每个槽通过注意力与帧表示交互，估计该槽对应声源的活动与三维方向。随后用基于责任的证据聚合模块将帧级证据归并到源集合，输出匹配查询的声源集合、基数及 absent 判定。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- QC-MI-OVSEL 基准（训练 / 开发 / 评估，40,000 场景，80,000 查询视图，83 类含 17 新类）

## 📊 实验结果

摘要仅给出定性结论：在源恢复、定位召回、基数估计、精确集合恢复与 absent-query 抑制上优于互补基线。分析显示新类别、释义查询与更高源多重性主要损害源发现与集合补全，而成功恢复源的方位精度相对稳定。未提供具体指标数值。

## 🎯 结论与影响

本文最强结论是查询条件集合预测可同时改善多实例声源恢复与 absent 查询抑制。该基准与 Q-RSet 为开放词汇 SELD 提供可复现评测与基线，后续研究可围绕新类泛化与释义鲁棒性展开。工业上对智能助手、机器人听觉与空间音频检索有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出具体指标数值与消融细节，难以判断提升幅度；基准为合成 FOA 数据，真实房间与阵列差异可能影响泛化；未报告推理延迟与参数量；对比基线描述为互补，缺少与主流 SELD 强方法的直接比较。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-12/">← 返回 2026-10-12 速递</a></div>
