---
title: "语音/音频论文速递 2026-08-22"
date: 2026-08-22T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#音频生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频生成 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #对话系统 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音乐识别 | 1篇 | `█████` |
| #关键词识别 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="linearly-constrained-deep-beamformer-for-multi-speaker-scena-2605-21141/">Linearly Constrained Deep Beamformer for Multi-Speaker Scenarios</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种深度波束成形框架，通过自适应多损失约束直接估计满足线性空间约束的波束权重，在多说话人场景中优于经典LCMV。</div>
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

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1508.04306" target="_blank" rel="noopener">Deep Clustering: Discriminative Embeddings for Segmentation and Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2016</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">用嵌入聚类绕开 permutation 问题的开山之作，SS 领域必读。</div>
<div class="card-authors">John R. Hershey, Zhuo Chen, Jonathan Le Roux, Shinji Watanabe</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1607.00325" target="_blank" rel="noopener">Permutation Invariant Training of Deep Models for Speaker-Independent Multi-talker Speech Separation</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ICASSP 2017</span>
<span class="tag-pill tag-pill-soft">#语音分离</span>
</div>
<div class="card-tldr">PIT 提出，至今仍是大多数分离/TSE 工作的训练目标。</div>
<div class="card-authors">Dong Yu, Morten Kolbæk, Zheng-Hua Tan, Jesper Jensen</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="fourier-is-frontier-frequency-aware-autoencoding-for-high-fi-2608-19843/">Fourier is Frontier: Frequency-Aware Autoencoding for High-Fidelity Music Reconstruction</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频生成</span>
</div>
<div class="card-tldr">提出 ear-VAE2，一种基于复数 STFT 的频域自编码器，通过频率感知激活和双耳感知精化器，在音乐重建中显著提升高保真度。</div>
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
| 🥇 | [Fourier is Frontier: Frequency-Aware Autoencoding for High-F…](fourier-is-frontier-frequency-aware-autoencoding-for-high-fi-2608-19843/) 🎯 | **9.2** | #音频生成 |
| 🥈 | [Linearly Constrained Deep Beamformer for Multi-Speaker Scena…](linearly-constrained-deep-beamformer-for-multi-speaker-scena-2605-21141/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Towards Quantifying Benchmark Optimization in ASR Models](towards-quantifying-benchmark-optimization-in-asr-models-2608-19936/) | **7.8** | #语音识别 |
| 4. | [MINT-Bench: A Comprehensive Multilingual Benchmark for Instr…](mint-bench-a-comprehensive-multilingual-benchmark-for-instru-2604-17958/) | **7.8** | #语音合成 |
| 5. | [Real-time Generation of Listener Nodding via Prediction of K…](real-time-generation-of-listener-nodding-via-prediction-of-k-2607-12329/) | **7.2** | #对话系统 |
| 6. | [MultiVerse: A Creator-Centered Approach to Steering Context-…](multiverse-a-creator-centered-approach-to-steering-context-a-2608-19350/) | **7.2** | #音乐生成 |
| 7. | [Unified Music Identification for Tracks and Versions](unified-music-identification-for-tracks-and-versions-2608-19919/) | **7.2** | #音乐识别 |
| 8. | [A Multiplication-Free Feature Extractor for Signal Classific…](a-multiplication-free-feature-extractor-for-signal-classific-2608-17108/) | **7.2** | #关键词识别 |
| 9. | [Does Listening Matter? Backchanneling and Nodding in AI Clon…](does-listening-matter-backchanneling-and-nodding-in-ai-clone-2608-19527/) | **6.8** | #人机交互 |
| 10. | [Dancing Through Soundscapes: Designing a Low-Cost, Sound-Bas…](dancing-through-soundscapes-designing-a-low-cost-sound-based-2608-19827/) | **5.5** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="fourier-is-frontier-frequency-aware-autoencoding-for-high-fi-2608-19843/">Fourier is Frontier: Frequency-Aware Autoencoding for High-Fidelity Music Reconstruction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 ear-VAE2，一种基于复数 STFT 的频域自编码器，通过频率感知激活和双耳感知精化器，在音乐重建中显著提升高保真度。</div>
<div class="card-action">
<a href="fourier-is-frontier-frequency-aware-autoencoding-for-high-fi-2608-19843/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19843" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="linearly-constrained-deep-beamformer-for-multi-speaker-scena-2605-21141/">Linearly Constrained Deep Beamformer for Multi-Speaker Scenarios</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种深度波束成形框架，通过自适应多损失约束直接估计满足线性空间约束的波束权重，在多说话人场景中优于经典LCMV。</div>
<div class="card-action">
<a href="linearly-constrained-deep-beamformer-for-multi-speaker-scena-2605-21141/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21141" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="towards-quantifying-benchmark-optimization-in-asr-models-2608-19936/">Towards Quantifying Benchmark Optimization in ASR Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文提出量化ASR模型基准优化程度的方法，通过行为探针发现高分模型在音频不确定时仍输出基准参考文本，且该行为可被因果操纵。</div>
<div class="card-action">
<a href="towards-quantifying-benchmark-optimization-in-asr-models-2608-19936/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19936" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="mint-bench-a-comprehensive-multilingual-benchmark-for-instru-2604-17958/">MINT-Bench: A Comprehensive Multilingual Benchmark for Instruction-Following Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MINT-Bench 是一个多语言指令跟随 TTS 的综合基准，通过分层多轴分类和混合评估协议，系统评估内容一致性、指令遵循和感知质量。</div>
<div class="card-action">
<a href="mint-bench-a-comprehensive-multilingual-benchmark-for-instru-2604-17958/">详情 →</a> · <a href="https://arxiv.org/abs/2604.17958" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="real-time-generation-of-listener-nodding-via-prediction-of-k-2607-12329/">Real-time Generation of Listener Nodding via Prediction of Kinematic Parameters for Avatar Dialogue Systems</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#对话系统</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于VAP的实时点头时序与运动参数预测模型，集成到虚拟人对话系统，主观评估优于基线。</div>
<div class="card-action">
<a href="real-time-generation-of-listener-nodding-via-prediction-of-k-2607-12329/">详情 →</a> · <a href="https://arxiv.org/abs/2607.12329" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="multiverse-a-creator-centered-approach-to-steering-context-a-2608-19350/">MultiVerse: A Creator-Centered Approach to Steering Context-Adaptive Lyrics</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出创作者中心的自适应媒体创作方法，通过MultiVerse系统让词曲作者显式控制歌词随听众和场景变化，并验证其优于提示词工作流。</div>
<div class="card-action">
<a href="multiverse-a-creator-centered-approach-to-steering-context-a-2608-19350/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19350" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="unified-music-identification-for-tracks-and-versions-2608-19919/">Unified Music Identification for Tracks and Versions</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文提出统一基准评估曲目识别与版本识别，发现现有模型无法同时兼顾准确性与鲁棒性，并训练基线模型证明统一系统的可行性。</div>
<div class="card-action">
<a href="unified-music-identification-for-tracks-and-versions-2608-19919/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19919" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="a-multiplication-free-feature-extractor-for-signal-classific-2608-17108/">A Multiplication-Free Feature Extractor for Signal Classification: Keyword Spotting Case Study</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#关键词识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种免乘法特征提取器iRDT，用于关键词识别，在保持精度的同时大幅降低计算复杂度，适合超低功耗边缘设备。</div>
<div class="card-action">
<a href="a-multiplication-free-feature-extractor-for-signal-classific-2608-17108/">详情 →</a> · <a href="https://arxiv.org/abs/2608.17108" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="does-listening-matter-backchanneling-and-nodding-in-ai-clone-2608-19527/">Does Listening Matter? Backchanneling and Nodding in AI Clone</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#人机交互</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文研究在AI克隆中加入实时预测的言语反馈和点头行为，显著提升用户对真实感和共在感的评价。</div>
<div class="card-action">
<a href="does-listening-matter-backchanneling-and-nodding-in-ai-clone-2608-19527/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19527" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="dancing-through-soundscapes-designing-a-low-cost-sound-based-2608-19827/">Dancing Through Soundscapes: Designing a Low-Cost, Sound-Based Device for Sensing and Interpreting Movement and Dance</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">设计一种低成本、基于声音的装置，将舞蹈动作转化为可探索的生成式声景，并反思工作坊中的参与体验。</div>
<div class="card-action">
<a href="dancing-through-soundscapes-designing-a-low-cost-sound-based-2608-19827/">详情 →</a> · <a href="https://arxiv.org/abs/2608.19827" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
