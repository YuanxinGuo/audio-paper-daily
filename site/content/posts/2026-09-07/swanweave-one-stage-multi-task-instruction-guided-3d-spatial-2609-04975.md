---
title: "SwanWeave:One-Stage Multi-Task Instruction-Guided 3D Spatial Audio Editing"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频编辑"]
summary: "首个基于指令的一阶段多任务3D空间音频编辑框架，通过SE-MoE和SPO实现高质量FOA编辑。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频编辑</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#音频生成</span> <span class="tag-pill tag-pill-soft">#多任务学习</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.04975</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-09-07</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/MM-Speech/SwanWeave" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">MM-Speech/SwanWeave</span></span></a><a class="oc-chip oc-chip-proj" href="https://swanaigc.github.io/#swanweave" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">swanaigc.github.io/#swanweave</span></span></a><a class="oc-chip oc-chip-demo" href="https://swanaigc.github.io/#swanweave" target="_blank" rel="noopener"><span class="oc-icon">🔊</span><span class="oc-text"><span class="oc-label">在线 Demo</span><span class="oc-sub">swanaigc.github.io/#swanweave</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.04975" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.04975" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/MM-Speech/SwanWeave" target="_blank" rel="noopener">💻 代码</a><a class="rsrc rsrc-proj" href="https://swanaigc.github.io/#swanweave" target="_blank" rel="noopener">🌐 项目主页</a><a class="rsrc rsrc-demo" href="https://swanaigc.github.io/#swanweave" target="_blank" rel="noopener">🔊 Demo</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>首个基于指令的一阶段多任务3D空间音频编辑框架，通过SE-MoE和SPO实现高质量FOA编辑。
</div>

## 👥 作者与机构

**Ke Lei** ¹ · Chenyuhao Wen · Yu Zhang · Wenxiang Guo · Changhao Pan · Sashuai Zhou · Yongshi Li · Ruiqi Li · … 等 4 人

**机构**：浙江大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音频生成、空间音频处理及多模态指令跟随研究者阅读。建议重点阅读第3节方法部分（SE-MoE和SPO）以及第4节实验对比。可先看摘要和图表，再深入方法细节。

## 🌍 研究背景

空间音频编辑需根据用户指令修改现有声场，同时保持场景其余部分不变。现有语言引导编辑主要针对传统音频或依赖顺序操作，无法直接支持复杂3D空间指令的一阶段编辑。本文旨在解决FOA波形中联合推理音频事件、空间信息、动态变化和环境信息的问题。

## 💡 核心创新

1. 提出SwanWeave，首个一阶段多任务指令引导3D空间音频编辑框架
2. 设计SE-MoE（空间编辑混合专家）实现双级路由，处理复合指令和局部编辑
3. 引入SPO（空间偏好优化），基于DPO的对齐目标，提升自然语言接地
4. 构建包含十多种单操作和复合任务的配对FOA监督数据集
5. 采用分阶段训练策略，增强模型对指令的理解和编辑能力

## 🏗️ 模型架构

SwanWeave采用编码器-解码器架构，输入为FOA波形和文本指令。编码器提取音频和文本特征，通过SE-MoE模块进行任务感知的专家选择，其中双级路由分别处理复合指令和帧级局部编辑。解码器生成编辑后的FOA波形。训练采用分阶段策略，先进行任务学习，再通过SPO进行偏好优化。

## 📚 数据集

- 基于开源语音和音效语料库构建的配对FOA数据集（训练/评估）
- 可控房间模拟生成（训练）

## 📊 实验结果

实验表明，SwanWeave在所有任务上均优于现有通用音频编辑器和空间音频基线，但摘要未提供具体数值。

## 🎯 结论与影响

SwanWeave首次实现一阶段多任务指令引导的3D空间音频编辑，通过SE-MoE和SPO显著提升编辑质量和指令跟随能力。该工作为空间音频编辑提供了新范式，有望推动虚拟现实、游戏和影视制作中的空间音频内容创作。

## ⚠️ 局限与未解决问题

摘要未提及局限，但可能包括：依赖模拟数据，真实场景泛化未知；未报告推理效率；复合指令的编辑质量可能受限于任务组合的复杂性。

## 🔗 开源资源

- **代码**：<https://github.com/MM-Speech/SwanWeave>
- **项目主页**：<https://swanaigc.github.io/#swanweave>
- **Demo / 试听**：<https://swanaigc.github.io/#swanweave>

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-09-07/">← 返回 2026-09-07 速递</a></div>
