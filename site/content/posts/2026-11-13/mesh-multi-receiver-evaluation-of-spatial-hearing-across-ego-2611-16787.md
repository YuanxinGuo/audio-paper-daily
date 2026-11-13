---
title: "MESH: Multi-receiver Evaluation of Spatial Hearing across Egocentric and Allocentric Views"
date: 2026-11-13T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出MESH基准，用自我中心与异中心视角评测多接收器共享声场景中的声源关联与空间理解。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">7.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">中等</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间听觉</span> <span class="tag-pill tag-pill-soft">#多接收器</span> <span class="tag-pill tag-pill-soft">#基准评测</span> <span class="tag-pill tag-pill-soft">#语音理解</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.16787</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-12</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.16787" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.16787" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出MESH基准，用自我中心与异中心视角评测多接收器共享声场景中的声源关联与空间理解。
</div>

## 👥 作者与机构

**Wen Wen** ¹ · Bohan Li · KwanHo Tam · Yu Xi · Jing Peng · Shuai Wang · Kai Yu

**机构**：上海交通大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频、分布式语音处理与多模态空间理解的读者。值得通读，重点看§3任务定义与§4数据集构建，以及表2/表3的11种音频模型对比；若关注评测设计可先看消融部分关于peer信息利用的分析。

## 🌍 研究背景

空间听觉评测已有空间预测、转录、跟踪与分布式语音处理等基准，但缺少对“语音信号是否在跨接收器与运动下仍关联到正确物理声源”的评测。现有模型多依赖单接收器局部信息，难以利用同伴元数据与共享3D世界坐标，导致多说话人、动态场景下关联错误。本文构建MESH基准来量化这一关联能力。

## 💡 核心创新

1. 提出自我中心/异中心双视角评测框架
2. 构建近4万问题、13类静态与动态任务
3. 引入peer metadata与共享3D世界坐标关联
4. 系统评测11种音频模型配置与LLM agent

## 🏗️ 模型架构

MESH并非单一网络，而是评测基准：输入为多接收器同步录音及peer metadata（位置、朝向等），自我中心视角用本地录音与元数据，异中心视角将多接收器录音统一到共享3D世界坐标系。任务覆盖静态/动态定位与空间转录共13类，输出为距离估计、方向跟踪与转录文本。评测对象包括11种音频模型配置及调用专家工具的语言模型agent。

## 📚 数据集

- MESH（评测，近4万问题，13类任务）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| 静态距离估计准确率 | MESH | 现有最佳音频模型配置 | **21.90%** | — |
| 动态方向跟踪准确率 | MESH | 现有最佳音频模型配置 | **41.54%** | — |
| WER（四项转录任务） | MESH | 现有最佳音频模型配置 | **59.15%~73.10%** | — |

最佳静态距离估计与动态方向跟踪准确率仅21.90%与41.54%，四项转录任务最低WER在59.15%~73.10%之间。消融与补充实验表明现有模型无法有效利用peer信息，在多说话人与动态场景下表现明显下降，揭示“可获取分布式声学信息”与“有效用于空间语音理解”之间的差距。

## 🎯 结论与影响

最强结论是现有音频模型尚不能有效利用多接收器分布式信息完成空间语音关联。该基准为协作式与分布式空间听觉研究提供统一评测，对多麦克风阵列、AR/VR空间音频与机器人听觉落地有参考价值。

## ⚠️ 局限与未解决问题

作为基准论文，未提出新模型，仅评测现有配置；任务与数据构建细节、接收器数量与场景多样性未在摘要说明；缺少推理延迟与计算开销报告；LLM agent依赖专家工具，公平性需进一步讨论。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-13/">← 返回 2026-11-13 速递</a></div>
