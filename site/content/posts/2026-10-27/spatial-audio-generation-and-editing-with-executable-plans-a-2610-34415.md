---
title: "Spatial Audio Generation and Editing with Executable Plans and Self-Distilling Transfusion"
date: 2026-10-27T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "提出AMBIT统一框架，用可执行ScenePlan与Transfusion主干实现原生FOA空间音频生成与编辑。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.8</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#空间音频生成</span> <span class="tag-pill tag-pill-soft">#音频编辑</span> <span class="tag-pill tag-pill-soft">#一阶Ambisonics</span> <span class="tag-pill tag-pill-soft">#扩散模型</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.34415</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-27</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-proj" href="https://wjm-george.github.io/AMBIT/" target="_blank" rel="noopener"><span class="oc-icon">🌐</span><span class="oc-text"><span class="oc-label">项目主页</span><span class="oc-sub">wjm-george.github.io/AMBIT/</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.34415" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.34415" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-proj" href="https://wjm-george.github.io/AMBIT/" target="_blank" rel="noopener">🌐 项目主页</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出AMBIT统一框架，用可执行ScenePlan与Transfusion主干实现原生FOA空间音频生成与编辑。
</div>

## 👥 作者与机构

**Kam Man Wu** ¹ · Yu Zhang · Pengjun Fang · Mingfei Chen · Weijia Chen · Zeyue Tian · Qifeng Chen

**机构**：香港科技大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做空间音频生成、FOA/Ambisonics渲染与音频编辑的研究者阅读。建议通读，重点看§3的ScenePlan表示与Transfusion主干、§4的FOA-aware VAE（非对称分组KL与空间协方差匹配）以及OPSD自蒸馏部分；实验先看表2的生成质量与编辑保真度对比。

## 🌍 研究背景

空间音频制作需要同时决定声源内容与声场合成，现有文本到音频生成多输出单声道/立体声，缺乏原生FOA与可控编辑能力；编辑任务还要求保留未修改声源，传统方法难以在指令引导下兼顾内容改动与声学细节保持。本文要解决原生FOA生成与指令式编辑的统一建模问题。

## 💡 核心创新

1. 可执行ScenePlan统一描述声源内容、活动与3D轨迹
2. Transfusion主干耦合自回归规划与rectified-flow渲染
3. FOA-aware连续VAE：共享解码全向恢复+非对称分组KL+空间协方差匹配
4. 联合on-policy自蒸馏OPSD在采样状态上精炼规划与渲染

## 🏗️ 模型架构

输入为文本指令或参考音频，经自回归规划模块生成可执行ScenePlan（声源内容、活动区间、3D轨迹），再由rectified-flow渲染器生成FOA潜变量；共享Transfusion主干连接两阶段。FOA-aware连续VAE以共享解码器做全向恢复，用非对称分组KL与空间协方差匹配保持通道间结构。编辑时对比特征定位改动，全参考潜变量提供残差声学细节。OPSD用目标条件教师监督学生自生成前缀与采样状态。

## 📚 数据集

- 语音、音乐与一般声音的混合数据集（训练与评估）

## 📊 实验结果

摘要仅定性说明在语音、音乐与声音上生成内容与空间质量优于基线，指令编辑的声学保真度与未编辑声源保持更好，未给出SI-SDR、PESQ、MOS等具体数值，也无消融数据，需查阅正文表格确认。

## 🎯 结论与影响

最强结论是ScenePlan+Transfusion+FOA-VAE+OPSD的组合可统一原生FOA生成与指令编辑并保持未编辑源。对空间音频可控生成方向有推动，工业上可用于VR/游戏与影视空间声制作的原型流程。

## ⚠️ 局限与未解决问题

摘要未报客观指标与推理延迟，缺少与专用FOA生成/编辑基线的定量对比；OPSD训练成本与稳定性未讨论；编辑评测依赖主观或有限指标，数据集偏置与泛化性待验证。

## 🔗 开源资源

- **项目主页**：<https://wjm-george.github.io/AMBIT/>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-27/">← 返回 2026-10-27 速递</a></div>
