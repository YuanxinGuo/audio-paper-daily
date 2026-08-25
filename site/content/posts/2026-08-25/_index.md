---
title: "语音/音频论文速递 2026-08-25"
date: 2026-08-25T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 4 篇 · 最高分 8.8（#语音增强）"
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
| #语音增强 | 3篇 | `██████████` |
| #音频字幕生成 | 1篇 | `███` |
| #语音质量评估 | 1篇 | `███` |
| #双耳音频 | 1篇 | `███` |
| #生物声学 | 1篇 | `███` |
| #语音发展评估 | 1篇 | `███` |
| #音乐情感研究 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="slimdiffuse-towards-efficient-diffusion-based-speech-enhance-2608-21188/">SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhancement using Slimmable Networks</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出SlimDiffuSE，利用可伸缩网络在扩散生成过程中动态调整网络宽度，在保持语音增强性能的同时大幅降低计算复杂度。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mu-net-ultra-low-memory-and-low-complexity-speech-enhancemen-2608-21155/">{\mu}Net: Ultra-Low-Memory and Low-Complexity Speech Enhancement for Embedded Digital Signal Processors</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出μNet，一种仅需90KB内存和28MMACs的超低资源语音增强模型，支持4ms低延迟和全整数运算，性能与同复杂度SOTA相当。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="training-deepfilternet-with-accurate-room-acoustic-simulatio-2608-20971/">Training DeepFilterNet with Accurate Room Acoustic Simulations Improves Single-Channel Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文比较了不同真实感的合成RIR数据集对DeepFilterNet3语音增强训练的影响，发现高保真模拟数据能提升客观指标并显著降低ASR词错误率。</div>
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
<a class="card-title" href="audioworldsim-realistic-binaural-audio-datasets-for-world-mo-2608-21075/">AudioWorldSim: Realistic Binaural Audio Datasets For World Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">AudioWorldSim 是一个基于 SoundSpaces 2.0 的开源平台，用于自动生成真实双耳音频数据集，支持世界模型研究。</div>
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
| 🥇 | [SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhanc…](slimdiffuse-towards-efficient-diffusion-based-speech-enhance-2608-21188/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [{\mu}Net: Ultra-Low-Memory and Low-Complexity Speech Enhance…](mu-net-ultra-low-memory-and-low-complexity-speech-enhancemen-2608-21155/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolutio…](ace-cap-active-evidence-acquisition-via-agentic-co-evolution-2608-16162/) | **8.2** | #音频字幕生成 |
| 4. | [Training DeepFilterNet with Accurate Room Acoustic Simulatio…](training-deepfilternet-with-accurate-room-acoustic-simulatio-2608-20971/) 🎯 | **8.2** | #语音增强 |
| 5. | [DAMOS: Learning Distortion-Aware Speech Quality Assessment t…](damos-learning-distortion-aware-speech-quality-assessment-th-2608-21176/) | **7.8** | #语音质量评估 |
| 6. | [AudioWorldSim: Realistic Binaural Audio Datasets For World M…](audioworldsim-realistic-binaural-audio-datasets-for-world-mo-2608-21075/) 🎯 | **7.8** | #双耳音频 |
| 7. | [An Automated Pipeline for Few-Shot Bird Call Classification:…](an-automated-pipeline-for-few-shot-bird-call-classification--2504-16276/) | **7.2** | #生物声学 |
| 8. | [Self-Supervised Speech Representations Track Spoken Language…](self-supervised-speech-representations-track-spoken-language-2608-20396/) | **7.2** | #语音发展评估 |
| 9. | [Humanoid Musical Robots as Experimental Interfaces for Music…](humanoid-musical-robots-as-experimental-interfaces-for-music-2608-20433/) | **5.5** | #音乐情感研究 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="slimdiffuse-towards-efficient-diffusion-based-speech-enhance-2608-21188/">SlimDiffuSE: Towards Efficient Diffusion-Based Speech Enhancement using Slimmable Networks</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SlimDiffuSE，利用可伸缩网络在扩散生成过程中动态调整网络宽度，在保持语音增强性能的同时大幅降低计算复杂度。</div>
<div class="card-action">
<a href="slimdiffuse-towards-efficient-diffusion-based-speech-enhance-2608-21188/">详情 →</a> · <a href="https://arxiv.org/abs/2608.21188" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="mu-net-ultra-low-memory-and-low-complexity-speech-enhancemen-2608-21155/">{\mu}Net: Ultra-Low-Memory and Low-Complexity Speech Enhancement for Embedded Digital Signal Processors</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出μNet，一种仅需90KB内存和28MMACs的超低资源语音增强模型，支持4ms低延迟和全整数运算，性能与同复杂度SOTA相当。</div>
<div class="card-action">
<a href="mu-net-ultra-low-memory-and-low-complexity-speech-enhancemen-2608-21155/">详情 →</a> · <a href="https://arxiv.org/abs/2608.21155" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="ace-cap-active-evidence-acquisition-via-agentic-co-evolution-2608-16162/">ACE-Cap: Active Evidence Acquisition via Agentic Co-Evolution for Long-Paragraph Fine-Grained Audio Captioning</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频字幕生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ACE-Cap框架，将长段落细粒度音频字幕生成建模为主动证据获取过程，通过Composer与Instruct模型的多轮交互和LOOP-GRPO训练，实现自适应查询与终止。</div>
<div class="card-action">
<a href="ace-cap-active-evidence-acquisition-via-agentic-co-evolution-2608-16162/">详情 →</a> · <a href="https://arxiv.org/abs/2608.16162" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="training-deepfilternet-with-accurate-room-acoustic-simulatio-2608-20971/">Training DeepFilterNet with Accurate Room Acoustic Simulations Improves Single-Channel Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文比较了不同真实感的合成RIR数据集对DeepFilterNet3语音增强训练的影响，发现高保真模拟数据能提升客观指标并显著降低ASR词错误率。</div>
<div class="card-action">
<a href="training-deepfilternet-with-accurate-room-acoustic-simulatio-2608-20971/">详情 →</a> · <a href="https://arxiv.org/abs/2608.20971" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="damos-learning-distortion-aware-speech-quality-assessment-th-2608-21176/">DAMOS: Learning Distortion-Aware Speech Quality Assessment through Explicit Distortion Localization</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音质量评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DAMOS框架，通过显式失真定位辅助语音质量评估，在多个基准上超越现有方法并展现强泛化能力。</div>
<div class="card-action">
<a href="damos-learning-distortion-aware-speech-quality-assessment-th-2608-21176/">详情 →</a> · <a href="https://arxiv.org/abs/2608.21176" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="audioworldsim-realistic-binaural-audio-datasets-for-world-mo-2608-21075/">AudioWorldSim: Realistic Binaural Audio Datasets For World Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">AudioWorldSim 是一个基于 SoundSpaces 2.0 的开源平台，用于自动生成真实双耳音频数据集，支持世界模型研究。</div>
<div class="card-action">
<a href="audioworldsim-realistic-binaural-audio-datasets-for-world-mo-2608-21075/">详情 →</a> · <a href="https://arxiv.org/abs/2608.21075" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="an-automated-pipeline-for-few-shot-bird-call-classification--2504-16276/">An Automated Pipeline for Few-Shot Bird Call Classification: A Case Study with the Tooth-Billed Pigeon</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种自动化少样本鸟鸣分类流程，利用大型分类网络的嵌入空间和余弦相似度，成功检测极危物种齿嘴鸠的叫声。</div>
<div class="card-action">
<a href="an-automated-pipeline-for-few-shot-bird-call-classification--2504-16276/">详情 →</a> · <a href="https://arxiv.org/abs/2504.16276" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="self-supervised-speech-representations-track-spoken-language-2608-20396/">Self-Supervised Speech Representations Track Spoken Language Convergence to Adult Models in Infants and Children Who Are Deaf/Hard-of-Hearing</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音发展评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用HuBERT嵌入距离追踪聋儿与照护者语音的收敛，实现语言发展的可扩展评估。</div>
<div class="card-action">
<a href="self-supervised-speech-representations-track-spoken-language-2608-20396/">详情 →</a> · <a href="https://arxiv.org/abs/2608.20396" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="humanoid-musical-robots-as-experimental-interfaces-for-music-2608-20433/">Humanoid Musical Robots as Experimental Interfaces for Music-Evoked Emotion</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音乐情感研究</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出将音乐人形机器人作为研究音乐诱发情感的多模态交互实验平台，并以WAS-5为例论证可行性。</div>
<div class="card-action">
<a href="humanoid-musical-robots-as-experimental-interfaces-for-music-2608-20433/">详情 →</a> · <a href="https://arxiv.org/abs/2608.20433" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
