---
title: "TamilEOT: A Dataset and Model for Semantic End-of-Turn Detection in Tamil Telephone Speech"
date: 2026-11-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音事件检测"]
summary: "发布首个泰米尔语电话语音语义轮次结束检测数据集与两个轻量检测器，并公开负类标注失败经验。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.8</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音事件检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#端到端轮次检测</span> <span class="tag-pill tag-pill-soft">#语音活动检测</span> <span class="tag-pill tag-pill-soft">#低资源语言</span> <span class="tag-pill tag-pill-soft">#数据集构建</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.05631</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.05631" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.05631" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布首个泰米尔语电话语音语义轮次结束检测数据集与两个轻量检测器，并公开负类标注失败经验。
</div>

## 👥 作者与机构

**Santhoshkumar V** ¹

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音 agent、VAD/轮次检测与低资源语言数据构建的工程与研究读者。值得通读，重点看 §数据集构建与负类标注（44.4% 人工一致率）以及 §训练杠杆消融（仅编码器容量有效）；表 2 的 zero-shot 到微调对比与流式适配器 2.60 点损失可直接指导落地。

## 🌍 研究背景

语音 agent 在每个停顿处需判断说话人是否说完，无语言模型时只能依赖固定静音超时：过短会打断用户，过长则每轮都付出完整等待。此前语义轮次检测工作（如 Smart Turn 系列）主要覆盖英语等资源丰富语言，南印度语言缺少公开数据与模型，泰米尔语电话语音场景尤甚。本文要解决泰米尔语语义 EOT 检测的数据与模型空白，并量化构建成本与标注陷阱。

## 💡 核心创新

1. 首个泰米尔语电话语音语义 EOT 开放数据集，18,485 个轮次边界
2. 基于 Smart Turn v3 架构的两个纯音频检测器（8.7 MB / 21 MB）
3. 用音频 LLM 标注器替代规则负类标签，97.5% 一致率、成本 5.69 美元
4. 系统报告六种训练杠杆与流式适配器部署损失

## 🏗️ 模型架构

输入为电话语音片段（轮次边界附近的音频窗），特征经编码器提取后送入 Smart Turn v3 架构的纯音频分类头，输出“已结束/未结束”二分类概率。两个模型仅编码器容量不同，参数量对应 8.7 MB 与 21 MB 两个版本。摘要未给出更细的层数、特征类型与训练目标细节，仅说明单线程笔记本 CPU 上推理低于 150 ms。

## 📚 数据集

- TamilEOT 主集：116 通真实泰米尔语电话对话，18,485 个标注轮次边界（训练/评估）
- TamilEOT 轮次级伴随集：4,774 个完整轮次及停顿结构（分析/评估）
- 留出测试集：30 通未见通话的 4,168 个片段（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| Accuracy | 留出集（4,168 片段，30 通未见通话） | zero-shot 70.30% | **83.71%（8.7 MB）/ 86.13%（21 MB）** | +13.4 / +15.8 个百分点 |
| ROC-AUC | 留出集（4,168 片段） | zero-shot 0.751 | **0.921** | +0.170 |

微调后准确率从 zero-shot 70.30% 提升至 83.71%（8.7 MB）与 86.13%（21 MB），ROC-AUC 从 0.751 升至 0.921，两模型单线程笔记本 CPU 推理均低于 150 ms。六种训练杠杆中仅编码器容量带来实质变化，三次相同运行波动达 0.87 个准确率点，构成可检测下限。规则负类标签与盲测人工仅 44.4% 一致，低于随机；音频 LLM 标注器达 97.5% 一致。将标注边界回放经生产 VAD 与流式适配器额外损失 2.60 点，7.8% 边界根本未到达模型。

## 🎯 结论与影响

最强结论是：在泰米尔语电话语音上，仅靠编码器容量扩展即可把语义 EOT 准确率从 70.30% 提到 86.13%，且模型可在 CPU 实时运行。该工作为低资源语言轮次检测提供了可复现数据与负结果基线，提示后续研究应优先关注标注质量与流式管线损耗，而非训练技巧。对语音 agent 落地意味着更短的响应等待与更少打断。

## ⚠️ 局限与未解决问题

仅单一语言、单一电话域，泛化性未知；未与英语 Smart Turn 之外的语义 EOT 方法对比；未报告延迟分布与内存占用细节；0.87 点运行波动使部分消融结论不显著；规则负类标签失败虽被披露，但 LLM 标注器本身的偏差未评估。

---

<div class="paper-footer"><span>评分：6.8</span><span>原始：6.8</span><a href="/audio-paper-daily/posts/2026-11-02/">← 返回 2026-11-02 速递</a></div>
