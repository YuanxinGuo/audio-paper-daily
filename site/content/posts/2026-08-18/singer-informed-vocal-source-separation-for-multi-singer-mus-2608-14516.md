---
title: "Singer-Informed Vocal Source Separation for Multi-Singer Music Mixtures"
date: 2026-08-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#乐器分离"]
summary: "提出基于歌手注册嵌入的引导分离框架，通过特征拼接或FiLM调制，在多歌手混合中显著提升目标歌手提取质量。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#乐器分离</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#目标说话人提取</span> <span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#FiLM</span> <span class="tag-pill tag-pill-soft">#多歌手分离</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2608.14516</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-08-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner"><div class="oc-headline"><span class="oc-pulse"></span><span class="oc-title">本论文已开源</span><span class="oc-hint">点击下方卡片直达对应资源</span></div><div class="oc-grid"><a class="oc-chip oc-chip-code" href="https://github.com/jocelynxu01/singer-separation-paper" target="_blank" rel="noopener"><span class="oc-icon">💻</span><span class="oc-text"><span class="oc-label">代码仓库</span><span class="oc-sub">jocelynxu01/singer-separation-paper</span></span></a></div></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2608.14516" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2608.14516" target="_blank" rel="noopener">📑 PDF</a><a class="rsrc rsrc-code" href="https://github.com/jocelynxu01/singer-separation-paper" target="_blank" rel="noopener">💻 代码</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于歌手注册嵌入的引导分离框架，通过特征拼接或FiLM调制，在多歌手混合中显著提升目标歌手提取质量。
</div>

## 👥 作者与机构

**Jocelyn Xu** ¹ · Minje Kim

**机构**：伊利诺伊大学厄巴纳-香槟分校

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合音乐源分离、目标说话人提取研究者阅读。建议重点阅读第3节方法部分和第4节实验设置，特别是表2的结果对比。可先看摘要和结论，再深入方法细节。

## 🌍 研究背景

传统音乐源分离系统通常只提取单一歌声，无法区分多个歌手。现有方法如D3Net、BSRNN等在单歌手场景表现良好，但在多歌手混合中难以分离目标歌手。本文提出利用目标歌手的短注册音频学习嵌入，通过特征拼接或FiLM调制引导分离网络，以解决多歌手场景下的目标提取问题。

## 💡 核心创新

1. 引入歌手注册嵌入引导分离
2. 采用FiLM调制融合歌手信息
3. 构建基于DAMP-VSEP的Duet数据集
4. 质量过滤和非重叠注册段设计

## 🏗️ 模型架构

输入为混合音频和注册音频，分别通过编码器提取特征和歌手嵌入。歌手嵌入通过特征拼接或FiLM调制注入到U-Net主干网络中，引导分离过程。输出为估计的目标歌手歌声。

## 📚 数据集

- DAMP-VSEP（构建Duet数据集，训练/评估）
- DAMP-VSEP（质量过滤，非重叠注册段）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR | Duet测试集 | 基线模型 0.33 dB | **5.58 dB** | +5.25 dB |

实验表明，基线模型在单歌手场景表现良好，但在多歌手场景下目标歌手SI-SDR仅0.33 dB，而本文方法提升至5.58 dB。FAD指标也显示本文方法生成音频的感知质量更优，与目标音频分布更对齐。

## 🎯 结论与影响

本文提出的歌手引导分离框架显著提升了多歌手混合中目标歌手的提取质量，SI-SDR提升5.25 dB。该方法为音乐源分离提供了新思路，可扩展到更多歌手场景，对音乐制作和翻唱分离有实际应用价值。

## ⚠️ 局限与未解决问题

实验仅在二重唱场景验证，未扩展到更多歌手；依赖注册音频质量，未探讨注册音频长度影响；未与最新SOTA方法（如HTDemucs）对比；缺乏推理效率分析。

## 🔗 开源资源

- **代码**：<https://github.com/jocelynxu01/singer-separation-paper>

---

<div class="paper-footer"><span>评分：8.8</span><span>原始：7.8</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-08-18/">← 返回 2026-08-18 速递</a></div>
