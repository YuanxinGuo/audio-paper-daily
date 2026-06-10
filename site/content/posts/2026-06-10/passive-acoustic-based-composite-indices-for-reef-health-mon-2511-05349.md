---
title: "Passive Acoustic-based Composite Indices for Reef Health Monitoring in Noisy Tropical waters"
date: 2026-06-10T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#生物声学"]
summary: "利用CNN去噪器处理噪声掩蔽的珊瑚礁水下录音，提取声学指标与礁健康参数相关，证明被动声学监测可行性。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">6.5</div>
<div class="score-stars">★★★☆☆</div>
<div class="score-tier">前50%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#生物声学</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#被动声学监测</span> <span class="tag-pill tag-pill-soft">#珊瑚礁健康</span> <span class="tag-pill tag-pill-soft">#语音增强方法</span> <span class="tag-pill tag-pill-soft">#卷积神经网络</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2511.05349</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-10</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2511.05349" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2511.05349" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>利用CNN去噪器处理噪声掩蔽的珊瑚礁水下录音，提取声学指标与礁健康参数相关，证明被动声学监测可行性。
</div>

## 👥 作者与机构

**Hari Vishnu** ¹ · Yuen Min Too · Mandar Chitre · Danwei Huang · Teong Beng Koay · Sudhanshi S. Jain

**机构**：新加坡国立大学 · 新加坡热带海洋科学研究所

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合生物声学、水下声学监测领域研究者。重点读§3去噪方法、§4声学指标与礁健康相关性分析。可跳过§2数据采集细节。

## 🌍 研究背景

被动声学监测（PAM）有望实现珊瑚礁长期、大范围评估，但热带水域持续的人为和流致噪声掩盖低频礁声景，阻碍声学指标与礁健康参数的相关性分析。现有方法缺乏有效去噪手段，导致低频声学指标（如声压级、声学复杂度指数）与潜水员评估的活珊瑚丰富度、覆盖度等关联模糊。本文旨在通过CNN去噪器恢复低频声景，并验证去噪后声学指标及高频虾鸣率与礁健康的相关性。

## 💡 核心创新

1. 应用CNN去噪器缓解低频噪声掩蔽
2. 发现去噪后声学指标与礁健康参数显著相关
3. 验证虾鸣率作为鲁棒礁健康指标的时空相关性
4. 提出可推广至其他噪声环境的水声监测框架

## 🏗️ 模型架构

输入为水下录音的频谱图；主干网络为卷积神经网络（CNN）去噪器，结构未详述但属于监督学习；输出为去噪后的频谱图，用于后续声学指标提取（声压级、声学复杂度指数、虾鸣率）。

## 📚 数据集

- 新加坡水域10个珊瑚礁站点两年水下录音（训练/评估，含噪声与干净目标）

## 📊 实验结果

摘要未提供具体数值指标，但定性表明：去噪后低频声学指标（声压级、声学复杂度指数）与活珊瑚丰富度、覆盖度及藻类覆盖度相关；高频虾鸣率与礁参数时空鲁棒相关。

## 🎯 结论与影响

本研究证明被动声学监测结合CNN去噪可有效评估珊瑚礁健康，去噪后声学指标及虾鸣率与礁健康参数显著相关。该方法可推广至其他受噪声干扰的海洋环境，为长期、自动化礁监测提供技术基础。

## ⚠️ 局限与未解决问题

未报告去噪模型的具体架构、参数量及计算开销；缺乏与其他去噪方法的对比；数据集仅限新加坡水域，泛化性待验证；未量化去噪对指标相关性的提升幅度。

---

<div class="paper-footer"><span>评分：6.5</span><span>原始：6.5</span><a href="/audio-paper-daily/posts/2026-06-10/">← 返回 2026-06-10 速递</a></div>
