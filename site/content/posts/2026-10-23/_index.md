---
title: "语音/音频论文速递 2026-10-23"
date: 2026-10-23T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.2（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #音频理解 | 1篇 | `█████` |
| #语音合成评估 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #多模态情感识别 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="when-do-self-supervised-representations-help-speech-restorat-2610-30869/">When Do Self-Supervised Representations Help Speech Restoration?</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文质疑SSL特征净化在语音修复中总是有益，发现严重退化下感知相关性崩塌，并提出ERI将修复骨干中间特征注入SSL以缓解该问题。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hc-ainet-an-auditory-inspired-network-with-harmonic-compensa-2610-30818/">HC-AINet: An Auditory-Inspired Network with Harmonic Compensation for Low-Complexity Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出谐波补偿的听觉启发网络 HC-AINet，用 ERB 子带与谐波增益分支在 0.27M 参数下于 VoiceBank-DEMAND 取得 PESQ 3.20。</div>
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
| 🥇 | [When Do Self-Supervised Representations Help Speech Restorat…](when-do-self-supervised-representations-help-speech-restorat-2610-30869/) 🎯 | **8.2** | #语音增强 |
| 🥈 | [HC-AINet: An Auditory-Inspired Network with Harmonic Compens…](hc-ainet-an-auditory-inspired-network-with-harmonic-compensa-2610-30818/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [Qwen-Audio-Jev: A Unified Interface for Audio Decisions](qwen-audio-jev-a-unified-interface-for-audio-decisions-2610-21614/) | **7.2** | #音频理解 |
| 4. | [Beyond Naturalness: Probing Automated Text-To-Speech Evaluat…](beyond-naturalness-probing-automated-text-to-speech-evaluato-2608-09930/) | **7.2** | #语音合成评估 |
| 5. | [Piano2Pop: Expanding Piano Demos into Pop Productions Withou…](piano2pop-expanding-piano-demos-into-pop-productions-without-2610-31510/) | **6.8** | #音乐生成 |
| 6. | [Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-En…](synthetic-to-real-code-switched-asr-a-spontaneous-nepali-eng-2610-30860/) | **6.8** | #语音识别 |
| 7. | [CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-A…](cavc-convergence-adaptive-audio-visual-cache-for-modality-as-2610-30854/) | **6.8** | #音频生成 |
| 8. | [Measuring the Verifier's Floor: How Much Apparent Rare-Word …](measuring-the-verifier-s-floor-how-much-apparent-rare-word-t-2610-31470/) | **6.8** | #语音合成 |
| 9. | [A Sociolinguistic Analysis of Automatic Speech Recognition B…](a-sociolinguistic-analysis-of-automatic-speech-recognition-b-2603-24549/) | **6.0** | #语音识别 |
| 10. | [AGF-Net: A Robust Multimodal Emotion Recognition Model for A…](agf-net-a-robust-multimodal-emotion-recognition-model-for-as-2610-30651/) | **6.0** | #多模态情感识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="when-do-self-supervised-representations-help-speech-restorat-2610-30869/">When Do Self-Supervised Representations Help Speech Restoration?</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文质疑SSL特征净化在语音修复中总是有益，发现严重退化下感知相关性崩塌，并提出ERI将修复骨干中间特征注入SSL以缓解该问题。</div>
<div class="card-action">
<a href="when-do-self-supervised-representations-help-speech-restorat-2610-30869/">详情 →</a> · <a href="https://arxiv.org/abs/2610.30869" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="hc-ainet-an-auditory-inspired-network-with-harmonic-compensa-2610-30818/">HC-AINet: An Auditory-Inspired Network with Harmonic Compensation for Low-Complexity Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出谐波补偿的听觉启发网络 HC-AINet，用 ERB 子带与谐波增益分支在 0.27M 参数下于 VoiceBank-DEMAND 取得 PESQ 3.20。</div>
<div class="card-action">
<a href="hc-ainet-an-auditory-inspired-network-with-harmonic-compensa-2610-30818/">详情 →</a> · <a href="https://arxiv.org/abs/2610.30818" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="qwen-audio-jev-a-unified-interface-for-audio-decisions-2610-21614/">Qwen-Audio-Jev: A Unified Interface for Audio Decisions</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在 Qwen-Audio 上增加 Jev 决策头，用 CHOICE/NOUL/SCORE 三种原语直接输出概率或分数，替代自回归文本生成。</div>
<div class="card-action">
<a href="qwen-audio-jev-a-unified-interface-for-audio-decisions-2610-21614/">详情 →</a> · <a href="https://arxiv.org/abs/2610.21614" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="beyond-naturalness-probing-automated-text-to-speech-evaluato-2608-09930/">Beyond Naturalness: Probing Automated Text-To-Speech Evaluators on Linguistically Grounded Dimensions</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建首个维度级TTS元评估基准，用10维语言学标注体系检验4个MOS预测器与4个Audio-LLM评判器的感知对齐度。</div>
<div class="card-action">
<a href="beyond-naturalness-probing-automated-text-to-speech-evaluato-2608-09930/">详情 →</a> · <a href="https://arxiv.org/abs/2608.09930" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="piano2pop-expanding-piano-demos-into-pop-productions-without-2610-31510/">Piano2Pop: Expanding Piano Demos into Pop Productions Without Aligned Supervision</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 Piano2Pop 任务：将钢琴 MIDI 扩展为流行器乐编曲，用合成钢琴-伴奏配对做伪监督微调 flow-matching 模型。</div>
<div class="card-action">
<a href="piano2pop-expanding-piano-demos-into-pop-productions-without-2610-31510/">详情 →</a> · <a href="https://arxiv.org/abs/2610.31510" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="synthetic-to-real-code-switched-asr-a-spontaneous-nepali-eng-2610-30860/">Synthetic-to-Real Code-Switched ASR: A Spontaneous Nepali-English Podcast Benchmark</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建尼泊尔语-英语语码转换播客基准，用TTS合成数据SFT加GRPO做合成到真实域适配。</div>
<div class="card-action">
<a href="synthetic-to-real-code-switched-asr-a-spontaneous-nepali-eng-2610-30860/">详情 →</a> · <a href="https://arxiv.org/abs/2610.30860" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="cavc-convergence-adaptive-audio-visual-cache-for-modality-as-2610-30854/">CAVC: Convergence-Adaptive Audio-Visual Cache for Modality-Asymmetric Diffusion Generation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出免训练的音视频扩散缓存框架 CAVC，利用音频侧漂移可恢复、视频侧不可恢复的非对称性，中段缓存音频去噪与跨模态注意力，末段恢复联合去噪。</div>
<div class="card-action">
<a href="cavc-convergence-adaptive-audio-visual-cache-for-modality-as-2610-30854/">详情 →</a> · <a href="https://arxiv.org/abs/2610.30854" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="measuring-the-verifier-s-floor-how-much-apparent-rare-word-t-2610-31470/">Measuring the Verifier's Floor: How Much Apparent Rare-Word Text-to-Speech Error Is ASR Error?</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">量化ASR验证器在TTS评测中的误差下限：人类录音上稀有词漏检33-67%，多识别器交叉校验可将表观TTS错误降低2-3倍。</div>
<div class="card-action">
<a href="measuring-the-verifier-s-floor-how-much-apparent-rare-word-t-2610-31470/">详情 →</a> · <a href="https://arxiv.org/abs/2610.31470" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-sociolinguistic-analysis-of-automatic-speech-recognition-b-2603-24549/">A Sociolinguistic Analysis of Automatic Speech Recognition Bias in Newcastle English</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用社会语言学方法分析商用ASR在纽卡斯尔英语上的3000余条转写错误，发现错误按社会群体呈系统性分布。</div>
<div class="card-action">
<a href="a-sociolinguistic-analysis-of-automatic-speech-recognition-b-2603-24549/">详情 →</a> · <a href="https://arxiv.org/abs/2603.24549" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="agf-net-a-robust-multimodal-emotion-recognition-model-for-as-2610-30651/">AGF-Net: A Robust Multimodal Emotion Recognition Model for Asynchronous Audio-Visual Signals Based on Predictive Dynamic Fusion with Negative Learning</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#多模态情感识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出AGF-Net，用音频引导融合、多模态负学习与预测动态融合，在自动分段与含噪音视频下做情感识别。</div>
<div class="card-action">
<a href="agf-net-a-robust-multimodal-emotion-recognition-model-for-as-2610-30651/">详情 →</a> · <a href="https://arxiv.org/abs/2610.30651" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
