---
title: "语音/音频论文速递 2026-11-03"
date: 2026-11-03T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #双耳音频 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #音频伪造检测 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |
| #语音交互系统评测 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="high-frequency-safeguard-and-weighted-objective-scoring-band-2611-02235/">High Frequency Safeguard and Weighted Objective Scoring Bandwidth Extension</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出HFSWO，用Swin复数谱双流对抗框架加两个专用判别器约束高频能量分布，参数量比AP-BWE少74.6%。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="q-bwe-quantum-chaos-informed-speech-bandwidth-extension-2611-02250/">Q-BWE: Quantum Chaos-Informed Speech Bandwidth Extension</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用量子混沌判别器替代多判别器，指导Lattice-ConformerNeXt生成器做语音带宽扩展，参数量更少。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatex-array-flexible-multichannel-to-multichannel-target-sp-2611-03119/">SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出首个阵列灵活的多通道到多通道目标说话人提取框架，利用麦克风坐标与目标DOA重建各通道目标语音并保留空间信息。</div>
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
<a class="card-title" href="spatial-transfusion-from-structured-spatial-scene-understand-2611-02330/">Spatial Transfusion: From Structured Spatial Scene Understanding to Generation and Editing</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">将预训练空间音频理解模型通过流匹配扩展到一阶Ambisonics生成与编辑，冻结主干并用LoRA路由实现统一框架。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ananas-a-networked-audio-system-for-distributed-spatial-audi-2611-03077/">Ananas: A Networked Audio System for Distributed Spatial Audio Applications</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出基于低成本微控制器与Faust语言的网络化空间音频系统Ananas，用PTP实现纳秒级同步，支持波场合成与高阶Ambisonics。</div>
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
| 🥇 | [High Frequency Safeguard and Weighted Objective Scoring Band…](high-frequency-safeguard-and-weighted-objective-scoring-band-2611-02235/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Spatial Transfusion: From Structured Spatial Scene Understan…](spatial-transfusion-from-structured-spatial-scene-understand-2611-02330/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [SPATEX: Array-Flexible Multichannel-to-Multichannel Target S…](spatex-array-flexible-multichannel-to-multichannel-target-sp-2611-03119/) 🎯 | **8.8** | #目标说话人提取 |
| 4. | [ReplayFactor: Replay-Aware Dual-Attribute Learning for Pract…](replayfactor-replay-aware-dual-attribute-learning-for-practi-2611-02628/) | **7.2** | #音频伪造检测 |
| 5. | [Q-BWE: Quantum Chaos-Informed Speech Bandwidth Extension](q-bwe-quantum-chaos-informed-speech-bandwidth-extension-2611-02250/) 🎯 | **7.0** | #语音增强 |
| 6. | [Ananas: A Networked Audio System for Distributed Spatial Aud…](ananas-a-networked-audio-system-for-distributed-spatial-audi-2611-03077/) 🎯 | **7.0** | #双耳音频 |
| 7. | [Deployment-constrained key estimation with a DSP-guided tran…](deployment-constrained-key-estimation-with-a-dsp-guided-tran-2611-02408/) | **6.8** | #音乐信息检索 |
| 8. | [InteractionBench: Measuring Timing, Task Accuracy, Whisper a…](interactionbench-measuring-timing-task-accuracy-whisper-and--2611-02430/) | **6.8** | #语音交互系统评测 |
| 9. | [How Much Prosody Does Your ASR Encoder Already Know](how-much-prosody-does-your-asr-encoder-already-know-2611-02602/) | **6.8** | #语音识别 |
| 10. | [A Compact Statistical View of Musical-Instrument Directivity](a-compact-statistical-view-of-musical-instrument-directivity-2611-02927/) | **6.8** | #声学模拟 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="high-frequency-safeguard-and-weighted-objective-scoring-band-2611-02235/">High Frequency Safeguard and Weighted Objective Scoring Bandwidth Extension</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出HFSWO，用Swin复数谱双流对抗框架加两个专用判别器约束高频能量分布，参数量比AP-BWE少74.6%。</div>
<div class="card-action">
<a href="high-frequency-safeguard-and-weighted-objective-scoring-band-2611-02235/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02235" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="spatial-transfusion-from-structured-spatial-scene-understand-2611-02330/">Spatial Transfusion: From Structured Spatial Scene Understanding to Generation and Editing</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将预训练空间音频理解模型通过流匹配扩展到一阶Ambisonics生成与编辑，冻结主干并用LoRA路由实现统一框架。</div>
<div class="card-action">
<a href="spatial-transfusion-from-structured-spatial-scene-understand-2611-02330/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02330" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="spatex-array-flexible-multichannel-to-multichannel-target-sp-2611-03119/">SPATEX: Array-Flexible Multichannel-to-Multichannel Target Speech Extraction using Direction Clue</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个阵列灵活的多通道到多通道目标说话人提取框架，利用麦克风坐标与目标DOA重建各通道目标语音并保留空间信息。</div>
<div class="card-action">
<a href="spatex-array-flexible-multichannel-to-multichannel-target-sp-2611-03119/">详情 →</a> · <a href="https://arxiv.org/abs/2611.03119" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="replayfactor-replay-aware-dual-attribute-learning-for-practi-2611-02628/">ReplayFactor: Replay-Aware Dual-Attribute Learning for Practical Speech Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双属性重放感知框架ReplayFactor，融合SSL表征与声学先验，并构建18.5万条中文重放伪造语音数据集ReplayFake-CN。</div>
<div class="card-action">
<a href="replayfactor-replay-aware-dual-attribute-learning-for-practi-2611-02628/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02628" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="q-bwe-quantum-chaos-informed-speech-bandwidth-extension-2611-02250/">Q-BWE: Quantum Chaos-Informed Speech Bandwidth Extension</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用量子混沌判别器替代多判别器，指导Lattice-ConformerNeXt生成器做语音带宽扩展，参数量更少。</div>
<div class="card-action">
<a href="q-bwe-quantum-chaos-informed-speech-bandwidth-extension-2611-02250/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02250" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="ananas-a-networked-audio-system-for-distributed-spatial-audi-2611-03077/">Ananas: A Networked Audio System for Distributed Spatial Audio Applications</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出基于低成本微控制器与Faust语言的网络化空间音频系统Ananas，用PTP实现纳秒级同步，支持波场合成与高阶Ambisonics。</div>
<div class="card-action">
<a href="ananas-a-networked-audio-system-for-distributed-spatial-audi-2611-03077/">详情 →</a> · <a href="https://arxiv.org/abs/2611.03077" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="deployment-constrained-key-estimation-with-a-dsp-guided-tran-2611-02408/">Deployment-constrained key estimation with a DSP-guided transformer reranker</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用21.5k参数的DSP引导Transformer重排序器，在115KB模型下把色度模板调性估计的MIREX从61.08提升到73.55。</div>
<div class="card-action">
<a href="deployment-constrained-key-estimation-with-a-dsp-guided-tran-2611-02408/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02408" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="interactionbench-measuring-timing-task-accuracy-whisper-and--2611-02430/">InteractionBench: Measuring Timing, Task Accuracy, Whisper and Volume, and Grounding in Real-Time Voice Systems</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音交互系统评测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 InteractionBench，用同一批录音音频在 13 个场景下同时评测实时语音系统的时序、任务准确率、耳语与音量、多轮接地四项能力。</div>
<div class="card-action">
<a href="interactionbench-measuring-timing-task-accuracy-whisper-and--2611-02430/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02430" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="how-much-prosody-does-your-asr-encoder-already-know-2611-02602/">How Much Prosody Does Your ASR Encoder Already Know</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">系统检验流式 Zipformer ASR 编码器各层已隐含多少韵律信息，发现首层之后韵律特征对端点检测的增益基本消失。</div>
<div class="card-action">
<a href="how-much-prosody-does-your-asr-encoder-already-know-2611-02602/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02602" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="a-compact-statistical-view-of-musical-instrument-directivity-2611-02927/">A Compact Statistical View of Musical-Instrument Directivity</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出乐器指向性的统计紧凑描述，将4阶30频带数据从492kB压缩到约100kB并保持距离几何。</div>
<div class="card-action">
<a href="a-compact-statistical-view-of-musical-instrument-directivity-2611-02927/">详情 →</a> · <a href="https://arxiv.org/abs/2611.02927" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
