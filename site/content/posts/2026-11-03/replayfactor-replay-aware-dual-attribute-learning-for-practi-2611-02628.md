---
title: "ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection"
date: 2026-11-03T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#音频伪造检测"]
summary: "提出双属性重放感知框架ReplayFactor，融合SSL表征与声学先验，并构建18.5万条中文重放伪造语音数据集ReplayFake-CN。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#音频伪造检测</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#深度伪造检测</span> <span class="tag-pill tag-pill-soft">#重放攻击</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#多任务学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.02628</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.02628" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.02628" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出双属性重放感知框架ReplayFactor，融合SSL表征与声学先验，并构建18.5万条中文重放伪造语音数据集ReplayFake-CN。
</div>

## 👥 作者与机构

**Miao He** ¹ · Jiayi Zhou · Yu Zheng · Zhongjie Ba · Peng Cheng · Yuxi Zhou · Junjie Zhu · Changhao Zhang · … 等 1 人

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做语音伪造检测、重放攻击防御与语音安全的研究者阅读。建议通读，重点看§3双属性融合模块与多任务/对比学习损失设计，以及§4 EchoFake开集实验与ReplayFake-CN数据集构建细节；表2与消融表是核心证据。

## 🌍 研究背景

语音深度伪造检测在数字生成语音上已较成熟，AASIST、RawNet2等基于SSL前端（如wav2vec2、WavLM）的检测器在ASVspoof等基准上EER很低。但物理重放会引入信道、房间与设备失真，使这些检测器性能显著下降，而重放是低成本且现实可行的攻击方式。现有工作多聚焦数据集构建与评测，重放感知的检测器设计与数据多样性仍不足，本文针对该痛点提出双属性框架并补充中文多设备重放数据集。

## 💡 核心创新

1. 融合SSL表征与声学先验的双属性重放证据增强
2. 多任务学习联合伪造检测与重放属性判别
3. 监督对比学习提升表征鲁棒性与泛化
4. 构建18.5万条多设备中文重放伪造数据集ReplayFake-CN

## 🏗️ 模型架构

输入为原始语音波形，经自监督前端（SSL，如WavLM类）提取高层表征，同时并行提取声学先验特征（重放信道/设备相关线索），二者通过双属性融合模块拼接或注意力融合形成重放增强表征；主干后接多任务头，分别输出真伪判别与重放属性分类，并引入监督对比学习损失约束类内紧凑、类间分离；最终以融合表征做二分类真伪判定。摘要未给出参数量。

## 📚 数据集

- ReplayFake-CN（自建，训练/评估，约185k条中文重放合成语音，多设备）
- EchoFake（开集评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| macro-F1 | EchoFake 开集 | 基线 60.99% | **76.44%** | +15.45% |
| EER | EchoFake 开集 | 基线 11.86% | **3.05%** | -8.81% |

在EchoFake开集上，macro-F1由60.99%提升至76.44%，EER由11.86%降至3.05%，显示重放场景下泛化显著改善。摘要未给出ReplayFake-CN上的闭集结果、各模块消融数值及推理开销，也未报告与更多重放检测基线的横向对比，需正文补充。

## 🎯 结论与影响

最强结论是双属性融合加多任务/对比学习能显著提升物理重放伪造检测的开集泛化。该思路为语音安全中的重放感知检测提供了可复用范式，并补足中文多设备数据缺口；工业上可用于声纹认证与语音交互系统的重放攻击防线。

## ⚠️ 局限与未解决问题

摘要仅报EchoFake开集两项指标，缺消融、闭集结果与推理延迟；ReplayFake-CN为自建中文数据，设备与语种偏置可能影响跨语种泛化；未与更多重放专用检测器横向对比，声学先验的具体形式与可解释性也未说明。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-11-03/">← 返回 2026-11-03 速递</a></div>
