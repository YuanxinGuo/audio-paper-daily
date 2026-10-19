---
title: "TV-AudioRemover: Joint Text-Visual Guided Sound Removal with Multi-Task Hard-Mixture Curriculum"
date: 2026-10-19T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "用编辑后视频与文本指令联合引导，从混合音轨中移除被删物体对应的声音，并构建百万级数据集与评测基准。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#多模态</span> <span class="tag-pill tag-pill-soft">#音视频</span> <span class="tag-pill tag-pill-soft">#数据增强</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2609.25864</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-19</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://yjx-research.github.io/TV-AudioRemover/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">yjx-research.github.io/TV-AudioRemover/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2609.25864" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2609.25864" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://yjx-research.github.io/TV-AudioRemover/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用编辑后视频与文本指令联合引导，从混合音轨中移除被删物体对应的声音，并构建百万级数据集与评测基准。
</div>

## 👥 作者与机构

**Xinyue Guo** ¹ · Jianxuan Yang · Daiguo Zhou · Jiagao Hu · Yuxuan Chen · Fei Wang · Jian Luan

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频联合、多模态声音编辑与目标声源分离的研究者阅读。建议通读：重点看 §3 的 task token 与模态全局引导设计、§4 的 hard-mixture curriculum 构造方式，以及 AV-Remove-Bench 的指标定义与 MLLM 评测协议；数据合成 pipeline 可快速浏览。

## 🌍 研究背景

视频物体移除（video inpainting）已能在像素层面删掉目标物体，但原音轨中该物体产生的声音仍然存在，造成音画不一致。现有方案分两类：视频修复模型只处理像素、不碰音频；音频编辑/声音移除模型多由文本单模态驱动，语义定位与时序同步能力弱。本文要解决的是：在给定编辑后视频与自然语言指令的条件下，从原始混合音频中精准抑制被移除物体对应的声音，同时保留其余声源。

## 💡 核心创新

1. 文本+编辑后视频双模态引导的目标声音移除框架
2. 百万级单物体音视频对齐数据构建与混合配对合成 pipeline
3. task token 与模态特定全局引导的指令建模
4. 多任务训练强化任务角色理解
5. 语义相似混合的 hard-mixture curriculum 微调

## 🏗️ 模型架构

输入为原始混合音频的时频特征、编辑后视频帧序列与自然语言指令。音频与视觉分别经各自编码器提取特征，文本指令经语言模型编码；通过 task token 注入任务角色信息，并以模态特定的全局引导（global guidance）将视觉上下文与指令意图融合进音频分离主干，输出被移除声源的估计，再从混合中相减得到净化音轨。摘要未给出参数量与具体主干网络名。

## 📚 数据集

- 自建百万级单物体音视频对齐数据集（训练）
- 由其合成的 mixture-target 配对数据（训练/微调）
- AV-Remove-Bench（评估，本文提出）

## 📊 实验结果

摘要仅声称在主观与客观指标上均达到 state-of-the-art，未给出任何具体数值、对比基线名称或测试集规模，因此无法量化改进幅度。消融方面提到多任务训练与 hard-mixture curriculum 均带来增益，但同样缺少数字。需查阅正文表格确认提升量级与统计显著性。

## 🎯 结论与影响

最强结论是：将视觉编辑结果与文本指令联合作为条件，可显著优于单模态文本驱动的声音移除。该工作把“视频物体移除”扩展到声学域，提出数据集与基准，可能推动音视频一致性编辑这一新子方向；工业上对视频后期、影视重制与内容审核中的目标声音擦除有直接价值。

## ⚠️ 局限与未解决问题

摘要未报告推理延迟与模型规模，难以判断实用性；百万级数据由 pipeline 合成，真实场景域偏移风险未知；AV-Remove-Bench 与 MLLM 评测协议由作者自建，客观性与与人工听感的相关性需验证；缺少与强音频分离基线（如 BSRNN、Bandit 类）的逐项对比细节。

## 🔗 开源资源

- **项目主页**：<https://yjx-research.github.io/TV-AudioRemover/>

---

<div class="paper-footer"><span>评分：8.2</span><span>原始：7.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-19/">← 返回 2026-10-19 速递</a></div>
