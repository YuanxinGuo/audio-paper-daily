---
title: "语音/音频论文速递 2026-07-29"
date: 2026-07-29T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 9.2（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #音视频编辑评估 | 1篇 | `█████` |
| #AI音乐检测 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ll-sdr-low-latency-speech-enhancement-through-discrete-repre-2603-20242/">LL-SDR: Low-Latency Speech enhancement through Discrete Representations</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出LL-SDR，一种基于离散表示的语音增强框架，通过VO-RVQ解耦语音和噪声，并引入潜在空间判别器提升增强质量，实现低延迟高性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="faster-enhancer-c-a-dependency-free-int8-runtime-for-streami-2607-25350/">faster-enhancer.c: A Dependency-Free int8 Runtime for Streaming Speech Enhancement on Commodity CPUs</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">将流式语音增强模型FastEnhancer-Medium移植为纯C int8运行时，在CPU上实现3.3倍加速，且精度损失极小。</div>
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
<a class="card-title" href="spacing-out-on-the-reliability-of-binaural-music-source-sepa-2607-25919/">Spacing Out: On the Reliability of Binaural Music Source Separation Metrics</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">通过感知实验评估双耳音乐源分离中客观空间失真指标与人类感知的相关性，发现ITD估计不可靠，需设计专用空间指标。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spacing-out-on-the-reliability-of-binaural-music-source-sepa-2607-25919/">Spacing Out: On the Reliability of Binaural Music Source Separation Metrics</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">通过感知实验评估双耳音乐源分离中客观空间失真指标与人类感知的相关性，发现ITD估计不可靠，需设计专用空间指标。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [LL-SDR: Low-Latency Speech enhancement through Discrete Repr…](ll-sdr-low-latency-speech-enhancement-through-discrete-repre-2603-20242/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [faster-enhancer.c: A Dependency-Free int8 Runtime for Stream…](faster-enhancer-c-a-dependency-free-int8-runtime-for-streami-2607-25350/) 🎯 | **8.5** | #语音增强 |
| 🥉 | [Spacing Out: On the Reliability of Binaural Music Source Sep…](spacing-out-on-the-reliability-of-binaural-music-source-sepa-2607-25919/) 🎯 | **8.2** | #双耳音频 |
| 4. | [AVE-Compass: Towards Holistic Evaluation for Audio-Video Edi…](ave-compass-towards-holistic-evaluation-for-audio-video-edit-2607-24821/) | **7.8** | #音视频编辑评估 |
| 5. | [Finding the noise: Zero-shot AI Music Detection](finding-the-noise-zero-shot-ai-music-detection-2607-25530/) | **7.8** | #AI音乐检测 |
| 6. | [From Semantics to Readout: Mechanistic Understanding of Audi…](from-semantics-to-readout-mechanistic-understanding-of-audio-2607-25355/) | **7.8** | #音频理解 |
| 7. | [MusiChat: Vibe Composing for Music Creation](musichat-vibe-composing-for-music-creation-2607-24873/) | **7.2** | #音乐生成 |
| 8. | [GraphIDyOM: A graph-native Python reimplementation of IDyOM …](graphidyom-a-graph-native-python-reimplementation-of-idyom-f-2607-25787/) | **6.5** | #音乐信息检索 |
| 9. | [Audio dequantization using instantaneous frequency](audio-dequantization-using-instantaneous-frequency-2510-16813/) | **6.5** | #音频处理 |
| 10. | [LLM4OSC: Profile-Bound Natural Language Control with Determi…](llm4osc-profile-bound-natural-language-control-with-determin-2607-26024/) | **6.5** | #音频控制 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="ll-sdr-low-latency-speech-enhancement-through-discrete-repre-2603-20242/">LL-SDR: Low-Latency Speech enhancement through Discrete Representations</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出LL-SDR，一种基于离散表示的语音增强框架，通过VO-RVQ解耦语音和噪声，并引入潜在空间判别器提升增强质量，实现低延迟高性能。</div>
<div class="card-action">
<a href="ll-sdr-low-latency-speech-enhancement-through-discrete-repre-2603-20242/">详情 →</a> · <a href="https://arxiv.org/abs/2603.20242" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="faster-enhancer-c-a-dependency-free-int8-runtime-for-streami-2607-25350/">faster-enhancer.c: A Dependency-Free int8 Runtime for Streaming Speech Enhancement on Commodity CPUs</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将流式语音增强模型FastEnhancer-Medium移植为纯C int8运行时，在CPU上实现3.3倍加速，且精度损失极小。</div>
<div class="card-action">
<a href="faster-enhancer-c-a-dependency-free-int8-runtime-for-streami-2607-25350/">详情 →</a> · <a href="https://arxiv.org/abs/2607.25350" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="spacing-out-on-the-reliability-of-binaural-music-source-sepa-2607-25919/">Spacing Out: On the Reliability of Binaural Music Source Separation Metrics</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过感知实验评估双耳音乐源分离中客观空间失真指标与人类感知的相关性，发现ITD估计不可靠，需设计专用空间指标。</div>
<div class="card-action">
<a href="spacing-out-on-the-reliability-of-binaural-music-source-sepa-2607-25919/">详情 →</a> · <a href="https://arxiv.org/abs/2607.25919" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="ave-compass-towards-holistic-evaluation-for-audio-video-edit-2607-24821/">AVE-Compass: Towards Holistic Evaluation for Audio-Video Editing Abilities</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音视频编辑评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AVE-Compass基准，系统评估音视频联合编辑能力，并设计AVE-Agent智能体框架提升跨模态编辑一致性。</div>
<div class="card-action">
<a href="ave-compass-towards-holistic-evaluation-for-audio-video-edit-2607-24821/">详情 →</a> · <a href="https://arxiv.org/abs/2607.24821" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="finding-the-noise-zero-shot-ai-music-detection-2607-25530/">Finding the noise: Zero-shot AI Music Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#AI音乐检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种零样本AI音乐检测方法，结合伪影提取与非负矩阵分解，在未知生成模型场景下实现高精度检测与聚类。</div>
<div class="card-action">
<a href="finding-the-noise-zero-shot-ai-music-detection-2607-25530/">详情 →</a> · <a href="https://arxiv.org/abs/2607.25530" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="from-semantics-to-readout-mechanistic-understanding-of-audio-2607-25355/">From Semantics to Readout: Mechanistic Understanding of Audio Tokens after Fine-Tuning for Temporal Audio Grounding</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过时间音频定位任务，系统分析了大音频语言模型微调前后音频token的语义、解码器可读性及时间对齐变化，提出语义到读出机制。</div>
<div class="card-action">
<a href="from-semantics-to-readout-mechanistic-understanding-of-audio-2607-25355/">详情 →</a> · <a href="https://arxiv.org/abs/2607.25355" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="musichat-vibe-composing-for-music-creation-2607-24873/">MusiChat: Vibe Composing for Music Creation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MusiChat 是一个通过自然语言对话实现迭代式音乐创作的系统，采用层次化可控生成框架和混合意图路由机制。</div>
<div class="card-action">
<a href="musichat-vibe-composing-for-music-creation-2607-24873/">详情 →</a> · <a href="https://arxiv.org/abs/2607.24873" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="graphidyom-a-graph-native-python-reimplementation-of-idyom-f-2607-25787/">GraphIDyOM: A graph-native Python reimplementation of IDyOM for musical expectation modelling</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">GraphIDyOM是IDyOM的图原生Python重实现，将长期和短期预测记忆表示为显式图对象，支持网络分析和交互应用。</div>
<div class="card-action">
<a href="graphidyom-a-graph-native-python-reimplementation-of-idyom-f-2607-25787/">详情 →</a> · <a href="https://arxiv.org/abs/2607.25787" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="audio-dequantization-using-instantaneous-frequency-2510-16813/">Audio dequantization using instantaneous frequency</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种利用瞬时频率的相位感知正则化方法进行音频去量化，避免l1正则化的能量损失伪影。</div>
<div class="card-action">
<a href="audio-dequantization-using-instantaneous-frequency-2510-16813/">详情 →</a> · <a href="https://arxiv.org/abs/2510.16813" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="llm4osc-profile-bound-natural-language-control-with-determin-2607-26024/">LLM4OSC: Profile-Bound Natural Language Control with Deterministic Validation for Open Sound Control</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频控制</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出LLM4OSC架构，通过设备配置文件约束和确定性验证，使LLM生成安全的OSC控制指令，消除幻觉和错误发送。</div>
<div class="card-action">
<a href="llm4osc-profile-bound-natural-language-control-with-determin-2607-26024/">详情 →</a> · <a href="https://arxiv.org/abs/2607.26024" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
