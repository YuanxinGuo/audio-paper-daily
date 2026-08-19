---
title: "语音/音频论文速递 2026-08-19"
date: 2026-08-19T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 4 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #语音合成 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #共语手势生成 | 1篇 | `█████` |
| #符号音乐压缩 | 1篇 | `█████` |
| #主动噪声控制 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-novel-binaural-cue-preservation-loss-for-dnn-based-binaura-2608-16299/">A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出两种双耳线索保持损失，直接惩罚掩蔽引起的左右频谱关系失真，联合建模ILD和IPD，在保持降噪性能的同时减少失真并改善ILD保持。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="navigating-speech-enhancement-for-real-time-mri-a-systematic-2608-16125/">Navigating Speech Enhancement for Real-Time MRI: A Systematic Assessment of Signal Quality, Source Preservation, and Downstream Tasks</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">系统评估三种通用语音增强系统在实时MRI语音上的效果，发现增强效果因任务而异，不能一概而论。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="separate-first-then-associate-a-two-stage-approach-for-real--2608-14812/">Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出分离-关联两阶段方法，先用音频-only模型分离多说话人混合，再用音频-视觉CLIP匹配目标人脸视频，提升真实场景AVSE性能。</div>
</div></div>

### #目标说话人提取

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1810.04826" target="_blank" rel="noopener">VoiceFilter: Targeted Voice Separation by Speaker-Conditioned Spectrogram Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2019</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">基于 d-vector 条件化的时频域目标说话人提取代表作，TSE 领域绕不开的基线。</div>
<div class="card-authors">Quan Wang, Hannah Muckenhirn, Kevin Wilson, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2005.04686" target="_blank" rel="noopener">SpEx+: A Complete Time Domain Speaker Extraction Network</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">Interspeech 2020</span>
<span class="tag-pill tag-pill-soft">#目标说话人提取</span>
</div>
<div class="card-tldr">时域 TSE 系列里程碑，多尺度编码器 + 共享说话人编码器，长期占据 SOTA。</div>
<div class="card-authors">Meng Ge, Chenglin Xu, Longbiao Wang, Eng Siong Chng, Jianwu Dang, Haizhou Li</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="separate-first-then-associate-a-two-stage-approach-for-real--2608-14812/">Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出分离-关联两阶段方法，先用音频-only模型分离多说话人混合，再用音频-视觉CLIP匹配目标人脸视频，提升真实场景AVSE性能。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="numerical-and-perceptual-validity-of-synthetic-head-related--2608-16722/">Numerical and perceptual validity of synthetic Head-Related Transfer Functions at scale</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">大规模评估合成HRTF在数值与感知上的有效性，发现合成HRTF在行为定位上与实测相当，优于KEMAR，但存在低频后部误差。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-novel-binaural-cue-preservation-loss-for-dnn-based-binaura-2608-16299/">A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出两种双耳线索保持损失，直接惩罚掩蔽引起的左右频谱关系失真，联合建模ILD和IPD，在保持降噪性能的同时减少失真并改善ILD保持。</div>
</div></div>

### #乐器分离

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://archives.ismir.net/ismir2017/paper/000171.pdf" target="_blank" rel="noopener">Singing Voice Separation with Deep U-Net Convolutional Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ISMIR 2017</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">Spotify 的 U-Net 人声分离，奠定频域 MSS 主流框架。</div>
<div class="card-authors">Andreas Jansson, Eric Humphrey, Nicola Montecchio, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1906.04032" target="_blank" rel="noopener">Open-Unmix - A Reference Implementation for Music Source Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">JOSS 2019</span>
<span class="tag-pill tag-pill-soft">#乐器分离</span>
</div>
<div class="card-tldr">MUSDB18 上最常被引的开源基线，BLSTM 频域分离的「教科书」实现。</div>
<div class="card-authors">Fabian-Robert Stöter, Stefan Uhlich, Antoine Liutkus, Yuki Mitsufuji</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Numerical and perceptual validity of synthetic Head-Related …](numerical-and-perceptual-validity-of-synthetic-head-related--2608-16722/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [Memory Efficient Audio Synthesis with Decoupled Temporal Dep…](memory-efficient-audio-synthesis-with-decoupled-temporal-dep-2607-23811/) | **8.5** | #语音合成 |
| 🥉 | [A Novel Binaural Cue Preservation Loss for DNN-Based Binaura…](a-novel-binaural-cue-preservation-loss-for-dnn-based-binaura-2608-16299/) 🎯 | **8.2** | #双耳音频 |
| 4. | [Geometry-adaptive Ambisonic encoding for sparse microphone a…](geometry-adaptive-ambisonic-encoding-for-sparse-microphone-a-2608-16240/) | **8.2** | #声学模拟 |
| 5. | [Navigating Speech Enhancement for Real-Time MRI: A Systemati…](navigating-speech-enhancement-for-real-time-mri-a-systematic-2608-16125/) 🎯 | **8.2** | #语音增强 |
| 6. | [Separate First, Then Associate: A Two-Stage Approach for Rea…](separate-first-then-associate-a-two-stage-approach-for-real--2608-14812/) 🎯 | **8.2** | #语音增强 |
| 7. | [EchoMask: Speech-Queried Attention-based Mask Modeling for H…](echomask-speech-queried-attention-based-mask-modeling-for-ho-2504-09209/) | **7.8** | #共语手势生成 |
| 8. | [UOT-IR: Structured Routing of High-Polyphony Symbolic Music …](uot-ir-structured-routing-of-high-polyphony-symbolic-music-i-2608-00576/) | **7.2** | #符号音乐压缩 |
| 9. | [Feedforward Active Speech Suppression Based on Time Series P…](feedforward-active-speech-suppression-based-on-time-series-p-2608-16092/) | **6.8** | #主动噪声控制 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="numerical-and-perceptual-validity-of-synthetic-head-related--2608-16722/">Numerical and perceptual validity of synthetic Head-Related Transfer Functions at scale</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">大规模评估合成HRTF在数值与感知上的有效性，发现合成HRTF在行为定位上与实测相当，优于KEMAR，但存在低频后部误差。</div>
<div class="card-action">
<a href="numerical-and-perceptual-validity-of-synthetic-head-related--2608-16722/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16722" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="memory-efficient-audio-synthesis-with-decoupled-temporal-dep-2607-23811/">Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出一种内存高效的音频合成架构，通过解耦时间与深度处理的扩散Transformer，在设备端实现实时、低内存的语音合成。</div>
<div class="card-action">
<a href="memory-efficient-audio-synthesis-with-decoupled-temporal-dep-2607-23811/">详情 →</a> · <a href="https://arxiv.org/abs/2607.23811" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="a-novel-binaural-cue-preservation-loss-for-dnn-based-binaura-2608-16299/">A Novel Binaural Cue Preservation Loss for DNN-Based Binaural Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两种双耳线索保持损失，直接惩罚掩蔽引起的左右频谱关系失真，联合建模ILD和IPD，在保持降噪性能的同时减少失真并改善ILD保持。</div>
<div class="card-action">
<a href="a-novel-binaural-cue-preservation-loss-for-dnn-based-binaura-2608-16299/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16299" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="geometry-adaptive-ambisonic-encoding-for-sparse-microphone-a-2608-16240/">Geometry-adaptive Ambisonic encoding for sparse microphone arrays of variable topology using physics-informed diffusion</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DiffM2A，一种几何自适应的条件扩散框架，用于从稀疏且拓扑可变的麦克风阵列中鲁棒地编码高阶Ambisonics，无需伪逆计算。</div>
<div class="card-action">
<a href="geometry-adaptive-ambisonic-encoding-for-sparse-microphone-a-2608-16240/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16240" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="navigating-speech-enhancement-for-real-time-mri-a-systematic-2608-16125/">Navigating Speech Enhancement for Real-Time MRI: A Systematic Assessment of Signal Quality, Source Preservation, and Downstream Tasks</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统评估三种通用语音增强系统在实时MRI语音上的效果，发现增强效果因任务而异，不能一概而论。</div>
<div class="card-action">
<a href="navigating-speech-enhancement-for-real-time-mri-a-systematic-2608-16125/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16125" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="separate-first-then-associate-a-two-stage-approach-for-real--2608-14812/">Separate First, Then Associate: A Two-Stage Approach for Real-World Audio-Visual Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出分离-关联两阶段方法，先用音频-only模型分离多说话人混合，再用音频-视觉CLIP匹配目标人脸视频，提升真实场景AVSE性能。</div>
<div class="card-action">
<a href="separate-first-then-associate-a-two-stage-approach-for-real--2608-14812/">详情 →</a> · <a href="https://arxiv.org/abs/2608.14812" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="echomask-speech-queried-attention-based-mask-modeling-for-ho-2504-09209/">EchoMask: Speech-Queried Attention-based Mask Modeling for Holistic Co-Speech Motion Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#共语手势生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于语音查询注意力的掩码建模框架，通过运动-音频对齐和选择性掩码提升共语手势生成质量。</div>
<div class="card-action">
<a href="echomask-speech-queried-attention-based-mask-modeling-for-ho-2504-09209/">详情 →</a> · <a href="https://arxiv.org/abs/2504.09209" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="uot-ir-structured-routing-of-high-polyphony-symbolic-music-i-2608-00576/">UOT-IR: Structured Routing of High-Polyphony Symbolic Music into Fixed-Budget Representations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#符号音乐压缩</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于约束非平衡最优传输的UOT-IR框架，将高复调符号音乐压缩为固定预算表示，在SymphonyNet上取得最优性能。</div>
<div class="card-action">
<a href="uot-ir-structured-routing-of-high-polyphony-symbolic-music-i-2608-00576/">详情 →</a> · <a href="https://arxiv.org/abs/2608.00576" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="feedforward-active-speech-suppression-based-on-time-series-p-2608-16092/">Feedforward Active Speech Suppression Based on Time Series Prediction of Speech Signals Using Neural Networks</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#主动噪声控制</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种基于神经网络时间序列预测的前馈主动语音抑制方法，通过预测未来信号改进控制滤波器更新，提升非平稳语音的降噪效果。</div>
<div class="card-action">
<a href="feedforward-active-speech-suppression-based-on-time-series-p-2608-16092/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16092" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
