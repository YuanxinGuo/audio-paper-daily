---
title: "ICASSP 2026 Radar Acoustic Speech Enhancement (RASE) Challenge"
date: 2026-10-26T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#语音增强"]
summary: "ICASSP 2026 首届毫米波雷达振动测声语音增强挑战赛，发布配对数据集、基线系统与 Codabench 评测框架。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#语音增强</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#毫米波雷达</span> <span class="tag-pill tag-pill-soft">#挑战赛</span> <span class="tag-pill tag-pill-soft">#多模态</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.32202</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-26</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.32202" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.32202" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>ICASSP 2026 首届毫米波雷达振动测声语音增强挑战赛，发布配对数据集、基线系统与 Codabench 评测框架。
</div>

## 👥 作者与机构

**Zhi-Wei Tan** ¹ · V. G. Reju · Ritesh C. Tewari · Ruotong Ding · Patrick A. Naylor · Andy W. H. Khong

**机构**：南洋理工大学 · 新加坡科技设计大学 · 萨里大学 · 香港理工大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做多模态语音增强、非麦克风传感、穿玻璃拾音的研究者与参赛者阅读。建议通读全文，重点看数据集构建与预处理流程、基线系统结构、评测指标定义与赛道设置；若准备参赛，先看数据划分与 Codabench 提交规范，再复现基线。

## 🌍 研究背景

语音增强长期依赖麦克风，但在穿玻璃、隔墙、强噪声或隐私受限场景中麦克风失效。毫米波雷达可通过振动测声（vibrometry）非接触拾取语音，近年出现少量可行性研究，但缺乏公开配对数据、统一预处理与可比基线，结果难以复现与横向比较。本文要解决的是该方向缺少公共基准的问题，通过挑战赛形式建立首个雷达语音增强评测平台。

## 💡 核心创新

1. 首个毫米波雷达振动测声语音增强公开挑战赛
2. 构建雷达与干净语音配对数据集及标准化预处理
3. 提供统一基线系统与 Codabench 安全评测框架
4. 统一客观指标，支持可复现横向比较

## 🏗️ 模型架构

摘要未给出基线网络细节。整体流程为：毫米波雷达回波经标准化预处理提取振动/相位相关特征，输入基线语音增强系统映射到干净语音波形或频谱，输出增强语音；评测在 Codabench 平台上以统一客观指标自动打分。具体主干网络、输入特征维度与参数量摘要未披露。

## 📚 数据集

- 自建配对雷达-干净语音数据集（训练/评估，规模摘要未给出）

## 📊 实验结果

摘要为挑战赛介绍，未报告具体增强指标数值，也未给出基线在 SI-SDR、PESQ、STOI 等指标上的结果。文中主要说明数据集、预处理、基线系统与评测框架的构建，实验性结论需查阅正文与排行榜。

## 🎯 结论与影响

本文最强结论是建立了首个雷达语音增强公共基准，把此前零散的可行性研究转为可复现的社区评测。若数据集与基线质量可靠，将推动非麦克风传感语音增强的标准化研究，并对穿玻璃、隐私敏感场景的工业拾音方案产生参考价值。

## ⚠️ 局限与未解决问题

作为挑战赛论文，摘要未给出基线性能数字、数据规模与说话人/环境多样性，难以判断任务难度与数据偏置；雷达硬件与采集条件可能限制泛化；缺少与传统麦克风阵列方案的对比，也未讨论推理延迟与实时性。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-26/">← 返回 2026-10-26 速递</a></div>
