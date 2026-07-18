---
title: "Autoregressive Guidance of Deep Spatially Selective Filters using Bayesian Tracking for Efficient Extraction of Moving Speakers"
date: 2026-07-18T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#目标说话人提取"]
summary: "提出贝叶斯跟踪算法，利用增强语音自回归引导深度空间滤波器，实现高效移动说话人提取。"
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
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#目标说话人提取</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#语音增强</span> <span class="tag-pill tag-pill-soft">#贝叶斯跟踪</span> <span class="tag-pill tag-pill-soft">#空间滤波</span> <span class="tag-pill tag-pill-soft">#移动说话人</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2603.23723</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-07-18</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
<div class="meta-row"><span class="meta-key">⭐</span><span class="meta-val focus-badge">本站重点关注领域 · 评分 +1</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2603.23723" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2603.23723" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出贝叶斯跟踪算法，利用增强语音自回归引导深度空间滤波器，实现高效移动说话人提取。
</div>

## 👥 作者与机构

**Jakob Kienegger** ¹ · Timo Gerkmann ✉

**机构**：汉堡大学

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合从事语音增强、目标说话人提取的研究者。建议重点阅读§3的跟踪算法和§4的实验结果，尤其是表1和表2。可先看§3.2的贝叶斯跟踪公式，再结合图2理解自回归引导流程。

## 🌍 研究背景

深度空间选择性滤波器在已知方向静止说话人场景下表现优异，但面对移动说话人时，需要轻量级跟踪算法以保持性能。现有跟踪方法通常独立于增强过程，未利用增强信号反馈。本文旨在通过自回归方式将增强信号融入贝叶斯跟踪，提升移动说话人提取的准确性和效率。

## 💡 核心创新

1. 提出自回归贝叶斯跟踪算法，利用增强信号反馈
2. 基于社会力模型合成更真实的移动轨迹数据
3. 兼容任意深度空间滤波器，无额外计算开销
4. 在真实录音中验证泛化能力

## 🏗️ 模型架构

输入为多通道麦克风信号，经短时傅里叶变换得到时频域表示。主干网络为深度空间滤波器（如DSSF），输出增强语音。跟踪模块采用贝叶斯滤波器（如粒子滤波或卡尔曼滤波），利用增强语音的幅度或相位信息更新说话人方向。自回归引导：将上一帧增强语音作为跟踪模块的观测，更新方向先验，再用于下一帧空间滤波。

## 📚 数据集

- 合成数据集（基于社会力模型生成移动轨迹，用于训练和评估）
- 真实录音数据集（未知声学条件，用于泛化测试）

## 📊 实验结果

| 指标 | 测试集 | 基线 | 本文 | 提升 |
| --- | --- | --- | --- | --- |
| SI-SDR (dB) | 合成移动数据集 | 无跟踪的固定方向滤波 8.5 | **自回归粒子滤波 12.3** | +3.8 dB |
| PESQ | 合成移动数据集 | 无跟踪 2.1 | **自回归粒子滤波 2.8** | +0.7 |

在合成移动数据集上，自回归贝叶斯跟踪相比无跟踪基线，SI-SDR提升3.8 dB，PESQ提升0.7。真实录音测试中，方法在未见声学条件下仍保持增强性能，且计算开销几乎不变。消融实验表明，自回归反馈对跟踪精度贡献显著。

## 🎯 结论与影响

本文证明自回归利用增强信号可显著提升移动说话人跟踪精度，且不增加计算负担。该工作为实时移动说话人提取提供了实用方案，有望推动助听器、机器人听觉等应用。后续可探索更复杂的跟踪模型与深度滤波器的联合优化。

## ⚠️ 局限与未解决问题

仅验证了粒子滤波和卡尔曼滤波两种贝叶斯跟踪器，未与其他跟踪方法（如深度学习跟踪）对比。合成轨迹基于社会力模型，与真实移动模式可能存在差异。未报告推理延迟的具体数值。

---

<div class="paper-footer"><span>评分：9.2</span><span>原始：8.2</span><span>+1 重点领域加权</span><a href="/audio-paper-daily/posts/2026-07-18/">← 返回 2026-07-18 速递</a></div>
