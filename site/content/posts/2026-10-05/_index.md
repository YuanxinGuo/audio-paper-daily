---
title: "语音/音频论文速递 2026-10-05"
date: 2026-10-05T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #音乐信息检索 | 2篇 | `██████████` |
| #语音分离 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #多音高估计 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="echodistill-robust-large-audio-language-models-via-noisy-to--2605-23954/">EchoDistill: Robust Large Audio Language Models via Noisy-to-Clean Self-Distillation</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">EchoDistill 用干净音频作特权信息做噪声到干净自蒸馏，提升 LALM 在 -10dB 加性噪声下的任务准确率。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="multiclass-speech-classification-under-noise-disparity-2610-03381/">Multiclass Speech Classification Under Noise Disparity</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">针对多类语音分类中的噪声不均衡问题，提出多类交叉增强训练策略，并对比语音增强预处理，发现后者反而有害。</div>
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
<a class="card-title" href="gaanet-global-guided-asymmetric-attention-network-for-audio--2610-02752/">GAANet: Global-guided Asymmetric Attention Network for Audio-Visual Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出非对称多尺度融合与全局引导注意力，用于音视频语音分离，LRS2 上达 16.5 dB SI-SNRi，仅 3.3M 参数。</div>
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
| 🥇 | [GAANet: Global-guided Asymmetric Attention Network for Audio…](gaanet-global-guided-asymmetric-attention-network-for-audio--2610-02752/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [EchoDistill: Robust Large Audio Language Models via Noisy-to…](echodistill-robust-large-audio-language-models-via-noisy-to--2605-23954/) 🎯 | **8.0** | #语音增强 |
| 🥉 | [Multiclass Speech Classification Under Noise Disparity](multiclass-speech-classification-under-noise-disparity-2610-03381/) 🎯 | **7.8** | #语音增强 |
| 4. | [Personalized Automatic Speech Recognition for a Dysarthric a…](personalized-automatic-speech-recognition-for-a-dysarthric-a-2610-03017/) | **7.0** | #语音识别 |
| 5. | [Note-Level Temporal Grounding of Musical Concepts in Large A…](note-level-temporal-grounding-of-musical-concepts-in-large-a-2608-29480/) | **6.8** | #音乐信息检索 |
| 6. | [Hearing is Believing? Evaluating and Analyzing Audio Languag…](hearing-is-believing-evaluating-and-analyzing-audio-language-2601-23149/) | **6.8** | #音频理解 |
| 7. | [Controllable Embedding Transformation for Mood-Guided Music …](controllable-embedding-transformation-for-mood-guided-music--2510-20759/) | **6.8** | #音乐信息检索 |
| 8. | [Can External Sources Help the Knowledge Cut-off Issues in Au…](can-external-sources-help-the-knowledge-cut-off-issues-in-au-2509-21728/) | **6.8** | #音频深度伪造检测 |
| 9. | [Revisiting Input Time-frequency Representations in Multi-pit…](revisiting-input-time-frequency-representations-in-multi-pit-2610-03656/) | **6.8** | #多音高估计 |
| 10. | [Rubric-Based Optimization for Text-to-Music Generation](rubric-based-optimization-for-text-to-music-generation-2610-03589/) | **6.8** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="gaanet-global-guided-asymmetric-attention-network-for-audio--2610-02752/">GAANet: Global-guided Asymmetric Attention Network for Audio-Visual Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出非对称多尺度融合与全局引导注意力，用于音视频语音分离，LRS2 上达 16.5 dB SI-SNRi，仅 3.3M 参数。</div>
<div class="card-action">
<a href="gaanet-global-guided-asymmetric-attention-network-for-audio--2610-02752/">详情 →</a> · <a href="https://arxiv.org/abs/2610.02752" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="echodistill-robust-large-audio-language-models-via-noisy-to--2605-23954/">EchoDistill: Robust Large Audio Language Models via Noisy-to-Clean Self-Distillation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">EchoDistill 用干净音频作特权信息做噪声到干净自蒸馏，提升 LALM 在 -10dB 加性噪声下的任务准确率。</div>
<div class="card-action">
<a href="echodistill-robust-large-audio-language-models-via-noisy-to--2605-23954/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23954" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="multiclass-speech-classification-under-noise-disparity-2610-03381/">Multiclass Speech Classification Under Noise Disparity</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对多类语音分类中的噪声不均衡问题，提出多类交叉增强训练策略，并对比语音增强预处理，发现后者反而有害。</div>
<div class="card-action">
<a href="multiclass-speech-classification-under-noise-disparity-2610-03381/">详情 →</a> · <a href="https://arxiv.org/abs/2610.03381" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="personalized-automatic-speech-recognition-for-a-dysarthric-a-2610-03017/">Personalized Automatic Speech Recognition for a Dysarthric and Tracheostomic Speaker using Artificial Conversations</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">为一名气管造口伴严重构音障碍的捷克语者构建个性化Whisper ASR，发布33小时人工对话数据集，CER相对降低50%。</div>
<div class="card-action">
<a href="personalized-automatic-speech-recognition-for-a-dysarthric-a-2610-03017/">详情 →</a> · <a href="https://arxiv.org/abs/2610.03017" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="note-level-temporal-grounding-of-musical-concepts-in-large-a-2608-29480/">Note-Level Temporal Grounding of Musical Concepts in Large Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 MusicGroundingBench，用算法生成的钢琴音频与精确符号对齐，评测大型音频语言模型的音符级音乐概念时序定位与理解能力。</div>
<div class="card-action">
<a href="note-level-temporal-grounding-of-musical-concepts-in-large-a-2608-29480/">详情 →</a> · <a href="https://arxiv.org/abs/2608.29480" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="hearing-is-believing-evaluating-and-analyzing-audio-language-2601-23149/">Hearing is Believing? Evaluating and Analyzing Audio Language Model Sycophancy with SYAUDIO</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出首个音频语言模型谄媚性评测基准SYAUDIO，含4319道音频题，揭示噪声与语速下的音频特有谄媚模式。</div>
<div class="card-action">
<a href="hearing-is-believing-evaluating-and-analyzing-audio-language-2601-23149/">详情 →</a> · <a href="https://arxiv.org/abs/2601.23149" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="controllable-embedding-transformation-for-mood-guided-music--2510-20759/">Controllable Embedding Transformation for Mood-Guided Music Retrieval</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出情绪引导的音乐嵌入变换框架，通过学习轻量翻译模型将种子音频嵌入映射到目标情绪嵌入，同时保留流派与配器属性。</div>
<div class="card-action">
<a href="controllable-embedding-transformation-for-mood-guided-music--2510-20759/">详情 →</a> · <a href="https://arxiv.org/abs/2510.20759" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="can-external-sources-help-the-knowledge-cut-off-issues-in-au-2509-21728/">Can External Sources Help the Knowledge Cut-off Issues in Audio Deepfake Detection?</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将RAG式检索增强引入音频深伪检测，在推理时查询外部知识库，缓解SSL模型的知识截断问题。</div>
<div class="card-action">
<a href="can-external-sources-help-the-knowledge-cut-off-issues-in-au-2509-21728/">详情 →</a> · <a href="https://arxiv.org/abs/2509.21728" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="revisiting-input-time-frequency-representations-in-multi-pit-2610-03656/">Revisiting Input Time-frequency Representations in Multi-pitch Estimation for Vocal Ensembles</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#多音高估计</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在合唱多音高估计中，线性STFT输入优于HCQT，且特征提取成本大幅降低，挑战了频率自适应表示的必要性。</div>
<div class="card-action">
<a href="revisiting-input-time-frequency-representations-in-multi-pit-2610-03656/">详情 →</a> · <a href="https://arxiv.org/abs/2610.03656" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="rubric-based-optimization-for-text-to-music-generation-2610-03589/">Rubric-Based Optimization for Text-to-Music Generation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用音频语言模型对生成音乐按评分标准打分，构建偏好对做DPO或直接做标量奖励，优化文本到音乐生成。</div>
<div class="card-action">
<a href="rubric-based-optimization-for-text-to-music-generation-2610-03589/">详情 →</a> · <a href="https://arxiv.org/abs/2610.03589" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
