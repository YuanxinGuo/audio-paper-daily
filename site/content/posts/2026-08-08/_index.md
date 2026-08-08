---
title: "语音/音频论文速递 2026-08-08"
date: 2026-08-08T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.2（#音视频生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音视频生成 | 1篇 | `██████████` |
| #音乐转录 | 1篇 | `██████████` |
| #空间音频理解 | 1篇 | `██████████` |
| #音频生成 | 1篇 | `██████████` |
| #语音驱动说话头生成 | 1篇 | `██████████` |
| #语音编码 | 1篇 | `██████████` |
| #乐器合成 | 1篇 | `██████████` |
| #音乐混音 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://ieeexplore.ieee.org/document/6932438" target="_blank" rel="noopener">A Regression Approach to Speech Enhancement Based on Deep Neural Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2015</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">首次系统验证 DNN 直接回归对数功率谱的语音增强范式，奠定后续大量 mask / mapping 方法的基础。</div>
<div class="card-authors">Yong Xu, Jun Du, Li-Rong Dai, Chin-Hui Lee</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1809.07454" target="_blank" rel="noopener">Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2019</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">时域端到端分离/增强里程碑，证明 1D 卷积可超越 STFT 域 IRM/IBM 上限。</div>
<div class="card-authors">Yi Luo, Nima Mesgarani</div>
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
| 🥇 | [Vorch-Streamer: Extending Human Audio-Visual Generation to R…](vorch-streamer-extending-human-audio-visual-generation-to-re-2608-05663/) | **8.2** | #音视频生成 |
| 🥈 | [Audio-to-Score Transcription using Pre-trained Features, Dat…](audio-to-score-transcription-using-pre-trained-features-data-2608-06165/) | **8.2** | #音乐转录 |
| 🥉 | [PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Under…](phasecoder-microphone-geometry-agnostic-spatial-audio-unders-2601-21124/) | **8.2** | #空间音频理解 |
| 4. | [KVAE: Family of Tokenizers for Multimodal Generative Models](kvae-family-of-tokenizers-for-multimodal-generative-models-2608-05798/) | **7.8** | #音频生成 |
| 5. | [PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads](pd-gs-phoneme-driven-3dgs-for-audio-driven-talking-heads-2608-05218/) | **7.8** | #语音驱动说话头生成 |
| 6. | [LILAC: An Idempotent Neural Speech Codec](lilac-an-idempotent-neural-speech-codec-2608-05727/) | **7.8** | #语音编码 |
| 7. | [Explicit and Stable Pseudospectral Time-Domain Method for th…](explicit-and-stable-pseudospectral-time-domain-method-for-th-2608-06139/) | **7.2** | #乐器合成 |
| 8. | [Rethinking Automatic Music Mixing as Sequential Stem Blendin…](rethinking-automatic-music-mixing-as-sequential-stem-blendin-2608-05506/) | **7.2** | #音乐混音 |
| 9. | [A Study of ASR Adaptation and Representation Dimensionality …](a-study-of-asr-adaptation-and-representation-dimensionality--2608-05165/) | **6.8** | #语音情感识别 |
| 10. | [The interface of intonation and lexical tone: Boundary pheno…](the-interface-of-intonation-and-lexical-tone-boundary-phenom-2608-05364/) | **6.5** | #语音韵律 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="vorch-streamer-extending-human-audio-visual-generation-to-re-2608-05663/">Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音视频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Vorch-Streamer后训练框架，通过混合教师强制与扩散强制、长时自强制及语音规划令牌，实现实时长时音视频流式生成。</div>
<div class="card-action">
<a href="vorch-streamer-extending-human-audio-visual-generation-to-re-2608-05663/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05663" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="audio-to-score-transcription-using-pre-trained-features-data-2608-06165/">Audio-to-Score Transcription using Pre-trained Features, Data Augmentation, and the New SheetSage-A2S Dataset</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐转录</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文提出基于预训练特征和数据增强的音频到乐谱转录模型，并发布首个流行音乐A2S数据集SheetSage-A2S，在古典和流行音乐上均取得显著提升。</div>
<div class="card-action">
<a href="audio-to-score-transcription-using-pre-trained-features-data-2608-06165/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06165" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="phasecoder-microphone-geometry-agnostic-spatial-audio-unders-2601-21124/">PhaseCoder: Microphone Geometry-Agnostic Spatial Audio Understanding for Multimodal LLMs</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#空间音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PhaseCoder 提出一种与麦克风几何无关的 Transformer 空间音频编码器，生成空间音频令牌，使多模态 LLM 能进行空间推理和定向转录。</div>
<div class="card-action">
<a href="phasecoder-microphone-geometry-agnostic-spatial-audio-unders-2601-21124/">详情 →</a> · <a href="https://arxiv.org/abs/2601.21124" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="kvae-family-of-tokenizers-for-multimodal-generative-models-2608-05798/">KVAE: Family of Tokenizers for Multimodal Generative Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">KVAE 系列 tokenizer 覆盖音频、图像、视频，在重建和生成指标上匹配或超越多个前沿开源 tokenizer，并公开训练细节与代码。</div>
<div class="card-action">
<a href="kvae-family-of-tokenizers-for-multimodal-generative-models-2608-05798/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05798" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="pd-gs-phoneme-driven-3dgs-for-audio-driven-talking-heads-2608-05218/">PD-GS: Phoneme-Driven 3DGS for Audio-Driven Talking Heads</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音驱动说话头生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PD-GS通过音素驱动3DGS，利用ASR强制对齐的音素令牌增强口型准确性，减少唇部闭合错误。</div>
<div class="card-action">
<a href="pd-gs-phoneme-driven-3dgs-for-audio-driven-talking-heads-2608-05218/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05218" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="lilac-an-idempotent-neural-speech-codec-2608-05727/">LILAC: An Idempotent Neural Speech Codec</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音编码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">LILAC 提出一种构造性幂等的 24kHz 语音编解码器，在 0.75 kbit/s 下重编码不改变 token，质量接近 SOTA。</div>
<div class="card-action">
<a href="lilac-an-idempotent-neural-speech-codec-2608-05727/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05727" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="explicit-and-stable-pseudospectral-time-domain-method-for-th-2608-06139/">Explicit and Stable Pseudospectral Time-Domain Method for the F\"oppl-von K\'arm\'an Equations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#乐器合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种显式稳定的伪谱时域方法，用于Föppl-von Kármán板非线性模态合成，降低计算成本并保持频率控制优势。</div>
<div class="card-action">
<a href="explicit-and-stable-pseudospectral-time-domain-method-for-th-2608-06139/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06139" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="rethinking-automatic-music-mixing-as-sequential-stem-blendin-2608-05506/">Rethinking Automatic Music Mixing as Sequential Stem Blending</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐混音</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将自动音乐混音重构为顺序茎混合任务，用潜流匹配模型逐茎处理，并引入退化数据合成策略。</div>
<div class="card-action">
<a href="rethinking-automatic-music-mixing-as-sequential-stem-blendin-2608-05506/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05506" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-study-of-asr-adaptation-and-representation-dimensionality--2608-05165/">A Study of ASR Adaptation and Representation Dimensionality Reduction in Persian Speech Emotion Recognition Using Whisper</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究使用Whisper进行波斯语语音情感识别，通过PCA降维减少参数，并探索ASR微调对下游任务的影响。</div>
<div class="card-action">
<a href="a-study-of-asr-adaptation-and-representation-dimensionality--2608-05165/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05165" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="the-interface-of-intonation-and-lexical-tone-boundary-phenom-2608-05364/">The interface of intonation and lexical tone: Boundary phenomena in Mandarin varieties</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音韵律</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">综述普通话变体中语调与声调在边界现象中的交互，探讨f0如何共同传达句子功能与态度信息。</div>
<div class="card-action">
<a href="the-interface-of-intonation-and-lexical-tone-boundary-phenom-2608-05364/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05364" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
