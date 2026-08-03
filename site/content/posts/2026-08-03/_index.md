---
title: "语音/音频论文速递 2026-08-03"
date: 2026-08-03T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音识别 | 2篇 | `██████████` |
| #语音分离 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频分类 | 1篇 | `█████` |
| #多模态生成 | 1篇 | `█████` |
| #音频理解与生成一致性评估 | 1篇 | `█████` |
| #主动噪声控制 | 1篇 | `█████` |
| #音乐情感识别 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="few-shot-contrastive-adaptation-for-audio-abuse-detection-in-2604-09094/">Few-Shot Contrastive Adaptation for Audio Abuse Detection in Low-Resource Indic Languages</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频分类</span>
</div>
<div class="card-tldr">本文研究利用CLAP音频表示直接检测低资源印度语言的辱骂性语音，无需转录，少量标注即可接近全监督性能。</div>
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
<a class="card-title" href="unsupervised-single-channel-speech-separation-with-diffusion-2509-24395/">Unsupervised Single-Channel Speech Separation with Diffusion under Speaker-Embedding Guidance</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出无监督单通道语音分离方法，利用扩散模型和说话人嵌入引导，在逆扩散过程中保持说话人一致性并分离不同说话人。</div>
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
| 🥇 | [Unsupervised Single-Channel Speech Separation with Diffusion…](unsupervised-single-channel-speech-separation-with-diffusion-2509-24395/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [ParaASR: Multi-Token Prediction for Fast and Long-Context LL…](paraasr-multi-token-prediction-for-fast-and-long-context-llm-2607-29279/) | **8.5** | #语音识别 |
| 🥉 | [BeatEdit: Symbolic Music Generation as Explicit Editing](beatedit-symbolic-music-generation-as-explicit-editing-2607-11124/) | **8.2** | #音乐生成 |
| 4. | [Few-Shot Contrastive Adaptation for Audio Abuse Detection in…](few-shot-contrastive-adaptation-for-audio-abuse-detection-in-2604-09094/) 🎯 | **8.2** | #音频分类 |
| 5. | [OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for J…](omnivae-an-audio-video-vae-with-cross-modal-alignment-for-jo-2607-23855/) | **7.8** | #多模态生成 |
| 6. | [DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual …](doublehelix-structured-cross-modal-fusion-for-audio-visual-s-2607-29112/) | **7.8** | #语音识别 |
| 7. | [TORUS: A Test of Rendering-Understanding Self-Coherence for …](torus-a-test-of-rendering-understanding-self-coherence-for-u-2607-28896/) | **7.5** | #音频理解与生成一致性评估 |
| 8. | [Model-Agnostic Meta-Learning Initialization for Distributed …](model-agnostic-meta-learning-initialization-for-distributed--2607-29117/) | **7.2** | #主动噪声控制 |
| 9. | [Learning to Predict Performance-induced Emotion Differences …](learning-to-predict-performance-induced-emotion-differences--2607-28876/) | **6.8** | #音乐情感识别 |
| 10. | [Do Music Foundation Models Embed Pitch in Helical Structure?](do-music-foundation-models-embed-pitch-in-helical-structure-2607-29086/) | **6.5** | #音频表征分析 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="unsupervised-single-channel-speech-separation-with-diffusion-2509-24395/">Unsupervised Single-Channel Speech Separation with Diffusion under Speaker-Embedding Guidance</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无监督单通道语音分离方法，利用扩散模型和说话人嵌入引导，在逆扩散过程中保持说话人一致性并分离不同说话人。</div>
<div class="card-action">
<a href="unsupervised-single-channel-speech-separation-with-diffusion-2509-24395/">详情 →</a> · <a href="https://arxiv.org/abs/2509.24395" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="paraasr-multi-token-prediction-for-fast-and-long-context-llm-2607-29279/">ParaASR: Multi-Token Prediction for Fast and Long-Context LLM-Based Speech Recognition</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">ParaASR利用多令牌预测让4B LLM解码器每步生成多个令牌，在保持识别质量的同时大幅降低延迟，支持32K上下文和30分钟音频单次转录。</div>
<div class="card-action">
<a href="paraasr-multi-token-prediction-for-fast-and-long-context-llm-2607-29279/">详情 →</a> · <a href="https://arxiv.org/abs/2607.29279" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="beatedit-symbolic-music-generation-as-explicit-editing-2607-11124/">BeatEdit: Symbolic Music Generation as Explicit Editing</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">BeatEdit提出首个基于显式编辑操作的符号音乐生成框架，利用BEAT编码实现高效、高质量的局部修改。</div>
<div class="card-action">
<a href="beatedit-symbolic-music-generation-as-explicit-editing-2607-11124/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11124" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="few-shot-contrastive-adaptation-for-audio-abuse-detection-in-2604-09094/">Few-Shot Contrastive Adaptation for Audio Abuse Detection in Low-Resource Indic Languages</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频分类</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文研究利用CLAP音频表示直接检测低资源印度语言的辱骂性语音，无需转录，少量标注即可接近全监督性能。</div>
<div class="card-action">
<a href="few-shot-contrastive-adaptation-for-audio-abuse-detection-in-2604-09094/">详情 →</a> · <a href="https://arxiv.org/abs/2604.09094" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="omnivae-an-audio-video-vae-with-cross-modal-alignment-for-jo-2607-23855/">OmniVAE: An Audio-Video VAE with Cross-Modal Alignment for Joint Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#多模态生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">OmniVAE提出联合训练的音频-视频VAE，通过对比学习和语义蒸馏实现跨模态对齐，提升下游音视频联合生成质量。</div>
<div class="card-action">
<a href="omnivae-an-audio-video-vae-with-cross-modal-alignment-for-jo-2607-23855/">详情 →</a> · <a href="https://arxiv.org/abs/2607.23855" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="doublehelix-structured-cross-modal-fusion-for-audio-visual-s-2607-29112/">DoubleHelix: Structured Cross-Modal Fusion for Audio-Visual Speech Recognition with LLMs</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DoubleHelix框架，通过迭代跨模态交互与退化感知增强，在LRS3上实现0.68% WER，相对提升5.6%。</div>
<div class="card-action">
<a href="doublehelix-structured-cross-modal-fusion-for-audio-visual-s-2607-29112/">详情 →</a> · <a href="https://arxiv.org/abs/2607.29112" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="torus-a-test-of-rendering-understanding-self-coherence-for-u-2607-28896/">TORUS: A Test of Rendering-Understanding Self-Coherence for Unified Audio Models</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音频理解与生成一致性评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个统一音频模型自一致性测试基准TORUS，包含48个三阶段测试和432个六选一问题，评估模型理解自身生成内容的能力。</div>
<div class="card-action">
<a href="torus-a-test-of-rendering-understanding-self-coherence-for-u-2607-28896/">详情 →</a> · <a href="https://arxiv.org/abs/2607.28896" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="model-agnostic-meta-learning-initialization-for-distributed--2607-29117/">Model-Agnostic Meta-Learning Initialization for Distributed Multichannel Active Noise Control</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#主动噪声控制</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于模型无关元学习（MAML）的初始化策略，用于分布式多通道主动噪声控制，加速自适应滤波器收敛并提升降噪性能。</div>
<div class="card-action">
<a href="model-agnostic-meta-learning-initialization-for-distributed--2607-29117/">详情 →</a> · <a href="https://arxiv.org/abs/2607.29117" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="learning-to-predict-performance-induced-emotion-differences--2607-28876/">Learning to Predict Performance-induced Emotion Differences in Classical Piano Music</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文提出Delta-VA框架，用表演特定特征预测古典钢琴演奏中情感（效价-唤醒）相对平均表演的偏差，并引入几何评估指标。</div>
<div class="card-action">
<a href="learning-to-predict-performance-induced-emotion-differences--2607-28876/">详情 →</a> · <a href="https://arxiv.org/abs/2607.28876" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="do-music-foundation-models-embed-pitch-in-helical-structure-2607-29086/">Do Music Foundation Models Embed Pitch in Helical Structure?</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频表征分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文分析音乐基础模型中间表征，发现音高信息以螺旋结构编码，且清晰度随模型和声学特性变化。</div>
<div class="card-action">
<a href="do-music-foundation-models-embed-pitch-in-helical-structure-2607-29086/">详情 →</a> · <a href="https://arxiv.org/abs/2607.29086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
