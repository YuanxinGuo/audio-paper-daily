---
title: "SHB-AE: Spherical harmonic beamforming based Ambisonics encoding and upscaling method for smartphone microphone array"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["论文详情"]
tags: ["#空间音频编码"]
summary: "提出基于球谐波束形成的Ambisonics编码与升阶方法，利用智能手机四麦克风阵列实现四阶Ambisonics编码。"
ShowToc: true
TocOpen: false
---

<div class="paper-hero">
<div class="hero-score">
<div class="score-num">7.2</div>
<div class="score-stars">★★★★☆</div>
<div class="score-tier">前25%</div>
</div>
<div class="hero-meta">
<div class="meta-row"><span class="meta-key">主任务</span><span class="meta-val tag-pill">#空间音频编码</span></div>
<div class="meta-row"><span class="meta-key">标签</span><span class="meta-val"><span class="tag-pill tag-pill-soft">#Ambisonics</span> <span class="tag-pill tag-pill-soft">#球谐波束形成</span> <span class="tag-pill tag-pill-soft">#智能手机麦克风阵列</span> <span class="tag-pill tag-pill-soft">#声场编码</span></span></div>
<div class="meta-row"><span class="meta-key">arXiv</span><span class="meta-val mono">2606.04584</span></div>
<div class="meta-row"><span class="meta-key">发布</span><span class="meta-val">2026-06-04</span></div>
<div class="meta-row"><span class="meta-key">建议</span><span class="meta-val">⏳ 按需阅读</span></div>
</div>
</div>

<div class="opensource-banner opensource-banner-empty"><span class="oc-icon-sm">🔒</span><span>暂未在摘要中发现公开代码或 demo</span></div>
<div class="resources"><a class="rsrc rsrc-arxiv" href="https://arxiv.org/abs/2606.04584" target="_blank" rel="noopener">📄 arXiv</a><a class="rsrc rsrc-pdf" href="https://arxiv.org/pdf/2606.04584" target="_blank" rel="noopener">📑 PDF</a></div>

<div class="tldr-box">
<span class="tldr-tag">TL;DR</span>提出基于球谐波束形成的Ambisonics编码与升阶方法，利用智能手机四麦克风阵列实现四阶Ambisonics编码。
</div>

## 👥 作者与机构

**Yuhuan You** ¹ · Yufan Qian · Tianshu Qu · Bin Wang · Xueyang Lv

<sub>¹ = 第一作者　✉ = 通讯作者</sub>

## 📖 阅读建议

适合空间音频、阵列信号处理方向研究者。建议重点阅读§3方法部分及§4实验验证，关注其波束形成器设计与实际阵列验证。

## 🌍 研究背景

高阶Ambisonics（HOA）因其播放设备适应性和头部朝向集成能力，在VR/AR空间音频中备受关注。当前HOA录制依赖大型球阵列（SMA），而智能手机等便携设备受限于麦克风数量与不规则排布。现有方法难以用少量麦克风实现高阶Ambisonics编码。本文旨在利用智能手机的4个不规则麦克风实现四阶Ambisonics编码与升阶。

## 💡 核心创新

1. 基于阵列流形设计各阶球谐函数的波束形成器
2. 仅用4个不规则麦克风实现四阶Ambisonics编码
3. 支持Ambisonics升阶（从低阶到高阶）
4. 在真实智能手机阵列及仿真自由场条件下验证

## 🏗️ 模型架构

输入：智能手机麦克风阵列（4个不规则麦克风）的时域信号。首先通过短时傅里叶变换（STFT）得到频域信号。然后，针对每个球谐函数阶数（0到4阶），基于阵列流形设计对应的波束形成器（球谐波束形成），将麦克风信号加权求和得到各阶Ambisonics分量（B格式信号）。输出：四阶Ambisonics（25个通道）的频域表示，可进一步逆变换到时域。方法无需训练，为解析方法。

## 📚 数据集

- 真实智能手机阵列录音（含噪声和混响，用于评估）
- 仿真自由场阵列数据（用于对比评估）

## 📊 实验结果

摘要未提供具体数值指标，仅说明在真实智能手机阵列及仿真自由场条件下，方法成功实现了四阶Ambisonics编码与升阶，且对噪声和混响具有鲁棒性。

## 🎯 结论与影响

本文提出的SHB-AE方法利用智能手机4个不规则麦克风，通过球谐波束形成实现四阶Ambisonics编码与升阶，为便携设备空间音频录制提供了新思路。该方法无需训练，计算高效，有望推动移动VR/AR应用中的空间音频采集。

## ⚠️ 局限与未解决问题

摘要未提及与现有方法的定量对比（如与球阵列的精度差距）；未报告计算复杂度或实时性；仅在单一智能手机阵列上验证，泛化性未知；未讨论低频性能限制（小阵列低频分辨率差）。

---

<div class="paper-footer"><span>评分：7.2</span><span>原始：7.2</span><a href="/audio-paper-daily/posts/2026-06-04/">← 返回 2026-06-04 速递</a></div>
