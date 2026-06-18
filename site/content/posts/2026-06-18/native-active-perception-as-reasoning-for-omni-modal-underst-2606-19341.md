---
title: "Native Active Perception as Reasoning for Omni-Modal Understanding"
date: 2026-06-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#视频理解"]
summary: "提出OmniAgent，首个原生全模态智能体，将视频理解建模为POMDP迭代观测-思考-行动循环，实现推理复杂度与视频时长解耦。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">8.5</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#视频理解</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#主动感知</span> <span class="tag-pill tag-pill-soft">#多模态推理</span> <span class="tag-pill tag-pill-soft">#强化学习</span> <span class="tag-pill tag-pill-soft">#POMDP</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.19341</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.19341" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.19341" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出OmniAgent，首个原生全模态智能体，将视频理解建模为POMDP迭代观测-思考-行动循环，实现推理复杂度与视频时长解耦。
</div>

## 👥 作者与机构

**Zhenghao Xing** ¹ · Ruiyang Xu · Yuxuan Wang · Jinzheng He · Ziyang Ma · Qize Yang · Yunfei Chu · Jin Xu · … 等 3 人

**机构**：香港中文大学 · 阿里巴巴

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合多模态推理与视频理解研究者。重点读§3的POMDP框架与§4.2的TAURA强化学习算法。建议先看表1的基准对比与图3的推理扩展曲线。

## 🌍 研究背景

长视频理解中，被动模型采用“全看”范式，计算成本随视频时长线性增长。现有交互式框架依赖全局预扫描，上下文成本仍与视频长度相关。本文旨在通过主动感知机制，使模型按需选择性提取音视频线索，将推理复杂度与原始视频时长解耦，实现正测试时扩展。

## 💡 核心创新

1. 提出POMDP迭代观测-思考-行动框架
2. Agentic SFT：best-of-N轨迹合成与双阶段质量控制
3. TAURA：基于回合级熵的自适应优势重标定强化学习

## 🏗️ 模型架构

OmniAgent基于多模态大语言模型（如Qwen2.5-VL-7B），输入视频帧与音频特征。核心为POMDP循环：观测模块接收当前视觉/音频片段，思考模块更新文本记忆并决定下一步动作（如继续观察、查询记忆、输出答案），行动模块执行动作。通过Agentic SFT初始化策略，再经TAURA强化学习优化。模型参数量7B。

## 📚 数据集

- VideoMME（评估）
- LVBench（评估）
- 其他8个基准（评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 准确率 | LVBench | Qwen2.5-VL-72B 47.3% | **OmniAgent-7B 50.5%** | +3.2% |

在VideoMME、LVBench等10个基准上，OmniAgent-7B达到开源模型最佳性能。在LVBench上以7B参数超越72B模型。消融实验验证了Agentic SFT和TAURA的有效性。推理扩展曲线显示性能随推理轮次增加而提升，验证了正测试时扩展。

## 🎯 结论与影响

OmniAgent通过主动感知机制实现了推理复杂度与视频时长的解耦，并在多个基准上取得开源SOTA。其POMDP框架为长视频理解提供了新范式，强化学习方法TAURA可推广至其他主动感知任务。对工业应用，可降低长视频分析的计算成本。

## ⚠️ 局限与未解决问题

未报告推理延迟与计算开销；仅在7B模型上验证，更大模型效果未知；主动感知的决策可解释性不足；未在真实场景中测试；依赖预训练的多模态骨干，可能继承其偏见。

---

<div class="paper-footer"><span>评分：8.5</span><span>原始：8.5</span><a href="/audio-paper-daily/posts/2026-06-18/">← 返回 2026-06-18 速递</a></div>
