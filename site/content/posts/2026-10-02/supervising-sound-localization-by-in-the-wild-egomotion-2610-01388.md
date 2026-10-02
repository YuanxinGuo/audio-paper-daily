---
title: "Supervising Sound Localization by In-the-wild Egomotion"
date: 2026-10-02T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#双耳音频"]
summary: "用视频中相机自运动作为弱监督信号，训练双耳音频模型预测声源方向，并构建真实场景音视频数据集。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#双耳音频</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#双耳音频</span> <span class="tag-pill tag-pill-soft">#声源定位</span> <span class="tag-pill tag-pill-soft">#自监督学习</span> <span class="tag-pill tag-pill-soft">#音视频学习</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2610.01388</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-10-02</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2610.01388" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2610.01388" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>用视频中相机自运动作为弱监督信号，训练双耳音频模型预测声源方向，并构建真实场景音视频数据集。
</div>

## 👥 作者与机构

**Anna Min** ¹ · Ziyang Chen · Hang Zhao · Andrew Owens

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做双耳音频、声源定位与音视频自监督的研究者阅读。建议重点看方法部分如何用多视角几何估计相机运动并构造监督信号，以及数据集构建与评估协议。若关注定位精度与泛化，先看实验表格与消融；若关注数据采集流程，看数据集一节。

## 🌍 研究背景

双耳声源定位传统上依赖 ILD/ITD 等线索，或使用仿真 HRTF 数据训练，但仿真与真实场景存在域差距。已有监督方法需要昂贵的方位标注，难以规模化。本文提出以视频中相机自运动作为弱监督：相机移动时声源相对方向变化，可与视觉估计的相机运动保持一致，从而在真实数据上学习定位，缓解标注瓶颈。

## 💡 核心创新

1. 用相机自运动作为双耳定位的弱监督信号
2. 结合多视角几何估计相机运动构造方向一致性约束
3. 融合传统双耳线索与自运动监督
4. 构建含自运动的真实音视频定位数据集

## 🏗️ 模型架构

输入为双耳音频与视频帧。音频分支提取双耳特征并预测声源方向；视觉分支用传统多视角几何方法从视频估计相机运动。训练时约束音频预测方向随相机运动的变化与视觉估计一致，并与 ILD/ITD 等传统双耳线索联合优化。输出为声源相对方向估计。摘要未给出具体网络名与参数量。

## 📚 数据集

- 自建真实世界音视频数据集（训练与评估，含自运动）

## 📊 实验结果

摘要仅说明模型能从真实数据成功学习并在声源定位任务上表现良好，未给出 SI-SDR、角度误差等具体数值，也未列出与基线的定量对比。因此无法填写结果表，需查阅正文确认定位精度、消融与跨场景泛化表现。

## 🎯 结论与影响

本文最强结论是相机自运动可作为真实场景下双耳声源定位的有效弱监督，减少对人工方位标注的依赖。该思路可能推动音视频自监督定位与真实数据训练的研究，对 AR/VR、机器人听觉等需要空间音频理解的落地场景有参考价值。

## ⚠️ 局限与未解决问题

摘要未给出定量指标与基线对比，难以判断相对传统双耳方法的实际增益；自运动监督依赖视觉几何估计精度，在纹理弱或动态场景可能退化；未说明推理延迟与模型规模，也缺少消融验证各线索贡献。

---

<div class="paper-footer"><span>评分：7.8</span><span>原始：6.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-10-02/">← 返回 2026-10-02 速递</a></div>
