---
title: "SonicWorld: Source-Centric Latent Dynamics for Spatial Audio Reasoning"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频推理"]
summary: "提出Sonic-Bench基准与SonicWorld模型，用源中心隐动态与Omni LLM做动态空间音频推理，方向准确率与方位误差均优于Spatial-Omni。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频推理</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#空间音频</span> <span class="tag-pill tag-pill-soft">#多模态大模型</span> <span class="tag-pill tag-pill-soft">#声源定位</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.17131</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-15</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.17131" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.17131" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出Sonic-Bench基准与SonicWorld模型，用源中心隐动态与Omni LLM做动态空间音频推理，方向准确率与方位误差均优于Spatial-Omni。
</div>

## 👥 作者与机构

**Chenlong Wei** ¹ · Hanling Wang · Mingjin Lou · Yufan Shi · Yandong Sun · Sheldon Yu · Xiaohui Zhu · Xiaobo Jin · … 等 1 人

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频理解、音频-语言多模态、声源运动推理的研究者阅读。建议重点看§3的Sonic-Bench构建流程与§4的源状态转移/循环更新模块，以及表2的Sonic-Bench主结果和零样本迁移表。若只关心语音增强/分离可略读。

## 🌍 研究背景

动态空间音频推理要求模型把变化的声学观测关联到正确声源并恢复其空间状态，重叠语音与声源运动使问题更难。此前Spatial-Omni等工作多依赖静态或单帧空间线索，缺乏对源身份持续跟踪与时间区间查询能力，在双源与运动场景下方向准确率低、方位误差大。本文要解决的是：如何在重叠与运动条件下，对特定目标源做定位、距离估计与运动推理。

## 💡 核心创新

1. 构建Sonic-Bench：2.8K一阶Ambisonics片段、28.8K目标问答、480个仿真室内场景
2. 提出源中心持久状态表示，融合物理、学习声学与语义特征
3. 用学习到的状态转移与循环更新建模源动态，再投影进Omni LLM做空间推理
4. 覆盖单/双源下的定位、距离估计与运动推理三类任务

## 🏗️ 模型架构

输入为一阶Ambisonics空间音频片段及目标特定问题。模型先提取物理声学线索、学习式声学特征与语义特征，将其整合为每个声源的持久源状态；通过学习的转移函数与循环更新机制在时间上维护和演化这些状态，以跟踪运动与重叠源；随后把源状态投影到Omni LLM的表示空间，由LLM完成定位、距离估计与运动推理的问答输出。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- Sonic-Bench（训练/评估，2.8K Ambisonics片段、28.8K问答、480场景）
- Spatial LibriSpeech（零样本迁移评估）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 方向准确率 | Sonic-Bench test | Spatial-Omni 31.98% | **34.69%** | +2.71% |
| 方位角误差 | Sonic-Bench test | Spatial-Omni 57.22° | **48.01°** | -9.21° |
| 方向准确率 | Spatial LibriSpeech（零样本） | Spatial-Omni 27.14% | **73.98%** | +46.84% |
| 方位角误差 | Spatial LibriSpeech（零样本） | Spatial-Omni 70.74° | **19.29°** | -51.45° |

在Sonic-Bench测试集上，SonicWorld方向准确率由31.98%升至34.69%，方位误差由57.22°降至48.01°，提升幅度有限；但在零样本迁移到Spatial LibriSpeech时表现突出，方向准确率73.98%、方位误差19.29°，远优于Spatial-Omni的27.14%与70.74°，说明源中心隐动态表示具有较强泛化性。摘要未报告距离估计、运动推理的细分结果，也无消融与效率指标。

## 🎯 结论与影响

最强结论是源中心持久状态加循环更新能显著提升跨数据集零样本空间定位泛化。该思路可能推动空间音频理解从静态单帧推理转向源级时序跟踪，并为AR/VR、机器人与智能座舱中的目标声源查询提供可落地范式。

## ⚠️ 局限与未解决问题

Sonic-Bench主结果提升仅约2.7个百分点，方位误差仍近48°，绝对性能偏低；基准为仿真数据，真实房间泛化未知；摘要未给距离估计与运动推理细分、无消融、无推理延迟与参数量，也未说明与更多空间音频baseline的对比。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-15/">← 返回 2026-10-15 速递</a></div>
