---
title: "语音/音频论文速递 2026-07-02"
date: 2026-07-02T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#语音增强）"
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
| #语音增强 | 2篇 | `██████████` |
| #语音合成 | 2篇 | `██████████` |
| #语音识别 | 1篇 | `█████` |
| #音视频同步评估 | 1篇 | `█████` |
| #无人机声学检测 | 1篇 | `█████` |
| #说话人确认 | 1篇 | `█████` |
| #音乐检索 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ambidrop-ambisonics-based-array-agnostic-neural-speech-enhan-2607-00548/">AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出AmbiDrop框架，利用Ambisonics域和通道丢弃训练实现阵列无关的多通道语音增强，在未见阵列和真实录音上表现鲁棒。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ambidrop-array-agnostic-speech-enhancement-using-ambisonics--2509-14855/">AmbiDrop: Array-Agnostic Speech Enhancement Using Ambisonics Encoding and Dropout-Based Learning</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出AmbiDrop框架，利用Ambisonics编码和通道丢弃训练实现阵列无关的语音增强，无需多几何数据集即可泛化到未见阵列。</div>
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

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/2111.10882" target="_blank" rel="noopener">Binaural Audio Generation via Multi-task Learning</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">ACM TOG 2021</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">联合 mono-to-binaural 与几何信息预测，提升合成空间感。</div>
<div class="card-authors">Sijia Li, Sagar Vaze, et al.</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1812.04204" target="_blank" rel="noopener">2.5D Visual Sound</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">CVPR 2019</span>
<span class="tag-pill tag-pill-soft">#双耳音频</span>
</div>
<div class="card-tldr">用单视频引导 mono → binaural，视听双耳音频合成开创性工作。</div>
<div class="card-authors">Ruohan Gao, Kristen Grauman</div>
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
| 🥇 | [AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enha…](ambidrop-ambisonics-based-array-agnostic-neural-speech-enhan-2607-00548/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [AmbiDrop: Array-Agnostic Speech Enhancement Using Ambisonics…](ambidrop-array-agnostic-speech-enhancement-using-ambisonics--2509-14855/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [NPUsper: Eliminating Redundant Computation for Real-Time Whi…](npusper-eliminating-redundant-computation-for-real-time-whis-2607-01108/) | **8.5** | #语音识别 |
| 4. | [Enhancing Flow Matching with A Unified Guidance Framework fo…](enhancing-flow-matching-with-a-unified-guidance-framework-fo-2607-00363/) | **7.8** | #语音合成 |
| 5. | [AV-SyncBench: Decoupled Benchmarking of Temporal and Semanti…](av-syncbench-decoupled-benchmarking-of-temporal-and-semantic-2607-00726/) | **7.5** | #音视频同步评估 |
| 6. | [EchoHawk: A Reproducible Acoustic Pipeline for Drone Detecti…](echohawk-a-reproducible-acoustic-pipeline-for-drone-detectio-2606-29589/) | **7.2** | #无人机声学检测 |
| 7. | [L-Proto: Language-Aware Episodic Prototypical Training for M…](l-proto-language-aware-episodic-prototypical-training-for-mu-2606-17416/) | **7.2** | #说话人确认 |
| 8. | [A Geometric Perspective on Composable Emotion Steering in Te…](a-geometric-perspective-on-composable-emotion-steering-in-te-2607-00946/) | **7.2** | #语音合成 |
| 9. | [Evaluating Pretrained Music Embeddings for Cross-Performance…](evaluating-pretrained-music-embeddings-for-cross-performance-2607-00777/) | **6.5** | #音乐检索 |
| 10. | [A Text-Steerable Instrument for Sketching Procedural Soundsc…](a-text-steerable-instrument-for-sketching-procedural-soundsc-2607-00309/) | **6.5** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="ambidrop-ambisonics-based-array-agnostic-neural-speech-enhan-2607-00548/">AmbiDrop: Ambisonics-Based Array-Agnostic Neural Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AmbiDrop框架，利用Ambisonics域和通道丢弃训练实现阵列无关的多通道语音增强，在未见阵列和真实录音上表现鲁棒。</div>
<div class="card-action">
<a href="ambidrop-ambisonics-based-array-agnostic-neural-speech-enhan-2607-00548/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00548" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="ambidrop-array-agnostic-speech-enhancement-using-ambisonics--2509-14855/">AmbiDrop: Array-Agnostic Speech Enhancement Using Ambisonics Encoding and Dropout-Based Learning</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AmbiDrop框架，利用Ambisonics编码和通道丢弃训练实现阵列无关的语音增强，无需多几何数据集即可泛化到未见阵列。</div>
<div class="card-action">
<a href="ambidrop-array-agnostic-speech-enhancement-using-ambisonics--2509-14855/">详情 →</a> · <a href="https://arxiv.org/abs/2509.14855" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="npusper-eliminating-redundant-computation-for-real-time-whis-2607-01108/">NPUsper: Eliminating Redundant Computation for Real-Time Whisper on Mobile NPUs</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出NPUsper系统，通过消除冗余计算实现Whisper在移动NPU上的实时转录，显著降低延迟和功耗。</div>
<div class="card-action">
<a href="npusper-eliminating-redundant-computation-for-real-time-whis-2607-01108/">详情 →</a> · <a href="https://arxiv.org/abs/2607.01108" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="enhancing-flow-matching-with-a-unified-guidance-framework-fo-2607-00363/">Enhancing Flow Matching with A Unified Guidance Framework for Efficient and Robust Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一引导框架，通过数据引导和模型引导加速流匹配语音合成并抑制音色泄露。</div>
<div class="card-action">
<a href="enhancing-flow-matching-with-a-unified-guidance-framework-fo-2607-00363/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00363" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="av-syncbench-decoupled-benchmarking-of-temporal-and-semantic-2607-00726/">AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音视频同步评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个解耦时序与语义的音视频同步基准AV-SyncBench，覆盖语音、音乐、声音10场景，含3269视频38390样本，评估5个代表性模型。</div>
<div class="card-action">
<a href="av-syncbench-decoupled-benchmarking-of-temporal-and-semantic-2607-00726/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00726" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="echohawk-a-reproducible-acoustic-pipeline-for-drone-detectio-2606-29589/">EchoHawk: A Reproducible Acoustic Pipeline for Drone Detection, Classification, and Direction-Finding, with a Cautionary Study of Session-Level Data Leakage</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#无人机声学检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">EchoHawk是一个开源、可复现的无人机声学检测、分类与测向流水线，并揭示了公共数据集中会话级数据泄露导致性能虚高的问题。</div>
<div class="card-action">
<a href="echohawk-a-reproducible-acoustic-pipeline-for-drone-detectio-2606-29589/">详情 →</a> · <a href="https://arxiv.org/abs/2606.29589" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="l-proto-language-aware-episodic-prototypical-training-for-mu-2606-17416/">L-Proto: Language-Aware Episodic Prototypical Training for Multilingual Speaker Verification</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人确认</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出语言感知的 episodic 原型训练策略 L-Proto，通过构建语言一致的 episode 减少语言变异，提升多语言说话人确认的跨语言泛化能力。</div>
<div class="card-action">
<a href="l-proto-language-aware-episodic-prototypical-training-for-mu-2606-17416/">详情 →</a> · <a href="https://arxiv.org/abs/2606.17416" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="a-geometric-perspective-on-composable-emotion-steering-in-te-2607-00946/">A Geometric Perspective on Composable Emotion Steering in Text-to-Speech Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">首次从几何视角比较语音语言模型与条件流匹配模块作为情感激活操控点的性能，揭示SLM具有低维情感子空间和强说话人-情感解耦，而CFM存在纠缠问题。</div>
<div class="card-action">
<a href="a-geometric-perspective-on-composable-emotion-steering-in-te-2607-00946/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00946" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="evaluating-pretrained-music-embeddings-for-cross-performance-2607-00777/">Evaluating Pretrained Music Embeddings for Cross-Performance Jazz Standard Recognition</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">使用预训练音乐嵌入进行跨演奏爵士标准曲识别，发现预训练嵌入优于从头训练模型，但受演奏者身份影响。</div>
<div class="card-action">
<a href="evaluating-pretrained-music-embeddings-for-cross-performance-2607-00777/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00777" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="a-text-steerable-instrument-for-sketching-procedural-soundsc-2607-00309/">A Text-Steerable Instrument for Sketching Procedural Soundscapes via Language Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一个实时音乐界面，将自然语言场景描述转换为可演化的程序化音景，支持细粒度参数控制和三种后端。</div>
<div class="card-action">
<a href="a-text-steerable-instrument-for-sketching-procedural-soundsc-2607-00309/">详情 →</a> · <a href="https://arxiv.org/abs/2607.00309" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
