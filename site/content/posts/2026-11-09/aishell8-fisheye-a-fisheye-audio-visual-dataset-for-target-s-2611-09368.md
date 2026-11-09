---
title: "AISHELL8-FISHEYE: A Fisheye Audio-Visual Dataset for Target Speaker Extraction with Distortion-Aware Baselines"
date: 2026-11-09T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "发布47小时中文鱼眼音视频数据集AISHELL8-FISHEYE，并提出融合畸变感知分支的音视频目标说话人提取基线。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero hero-focus">
<div class="hero-score">
<div class="score-num">8.0</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#音视频语音处理</span> <span class="tag-pill tag-pill-soft">#数据集</span> <span class="tag-pill tag-pill-soft">#鱼眼相机</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2611.09368</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-11-09</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2611.09368" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2611.09368" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>发布47小时中文鱼眼音视频数据集AISHELL8-FISHEYE，并提出融合畸变感知分支的音视频目标说话人提取基线。
</div>

## 👥 作者与机构

**Peijun Yang** ¹ · Zhan Jin · Juan Liu · Hui Bu · Xiaoyi Qin · Ruyi Gan · Hao Wang · Ming Li

**机构**：西北工业大学 · 希尔贝壳

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合做音视频TSE、多模态前端与数据集构建的研究者阅读。建议通读，重点看§3数据集构建与划分协议、§4畸变感知分支的迁移方式，以及表2中鱼眼与普通相机输入的对比结果；若只关心方法，可先看消融部分理解视觉适配的必要性。

## 🌍 研究背景

音视频目标说话人提取（AV-TSE）在普通相机视频上已较成熟，唇读编码器配合Conformer类主干可显著提升SI-SDRi。但鱼眼相机虽覆盖广角，却引入面部与唇形几何畸变，使常规唇读特征失配。现有AV-TSE数据集多为普通视角，缺乏配对鱼眼/普通相机、说话人互斥划分的可复现基准，畸变视觉线索下的提取性能上限尚不清楚。本文构建该数据集并给出畸变感知基线。

## 💡 核心创新

1. 构建47.03小时中文鱼眼音视频语料，含配对鱼眼与普通相机视频
2. 说话人互斥划分+合成双说话人混合，保证可复现评估
3. 将鱼眼头部姿态估计的畸变感知分支冻结迁移至TSE
4. 验证视觉适配对畸变分支生效的必要性

## 🏗️ 模型架构

输入为鱼眼视频帧与混合语音。视觉侧采用唇读编码器提取唇部特征，并并联一个从鱼眼头部姿态估计任务迁移来的冻结畸变感知分支，两路视觉特征融合后与音频特征（如STFT幅度谱经编码器）在分离主干中做跨模态融合，输出目标说话人掩码或时域波形。摘要未给出参数量与具体主干网络名，仅说明唇读编码器可适配（微调）或冻结两种设置。

## 📚 数据集

- AISHELL8-FISHEYE（训练/评估，47.03小时，94名普通话说话人，配对鱼眼与普通相机视频）
- 合成双说话人混合（评估，基于上述语料构建）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDRi | AISHELL8-FISHEYE 鱼眼测试集 | 适配唇读编码器 10.47 dB | **加畸变感知分支 11.84 dB** | +1.37 dB |

在鱼眼视频上，向适配后的唇读编码器加入冻结畸变感知分支，SI-SDRi由10.47 dB升至11.84 dB；但若唇读编码器冻结，该分支不带来增益，说明视觉侧适配是关键。与配对普通相机输入相比仍有明显差距，摘要未给出该差距的具体数值，也未报告PESQ、WER或推理延迟等指标。

## 🎯 结论与影响

最强结论是：畸变感知分支只有在唇读编码器同步适配时才能提升鱼眼条件下的TSE性能。该数据集为畸变视觉线索下的音视频分离提供了可复现基准，后续工作可围绕鱼眼几何校正与跨视角特征对齐展开；工业上对广角会议/车载拾音场景有参考价值。

## ⚠️ 局限与未解决问题

仅报告SI-SDRi单一指标，缺PESQ/WER与主观评测；未给出与普通相机差距的量化值；畸变分支为冻结迁移，未探索端到端联合训练；数据集仅中文、94人，规模与语言多样性有限；未报推理延迟与模型参数量。

---

<div class="paper-footer"><span>评分：8.0</span><span>原始：7.0</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-11-09/">← 返回 2026-11-09 速递</a></div>
