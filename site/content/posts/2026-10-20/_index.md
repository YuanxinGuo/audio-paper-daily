---
title: "语音/音频论文速递 2026-10-20"
date: 2026-10-20T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.2（#语音识别）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音识别 | 4篇 | `██████████` |
| #音乐结构分析 | 1篇 | `██` |
| #说话人验证 | 1篇 | `██` |
| #语音事件检测 | 1篇 | `██` |
| #音频处理 | 1篇 | `██` |
| #语音情感识别 | 1篇 | `██` |
| #音频指纹 | 1篇 | `██` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ms-bench-a-condition-stratified-multi-speaker-asr-benchmark-2610-25824/">MS-Bench: A Condition-Stratified Multi-Speaker ASR Benchmark</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
</div>
<div class="card-tldr">提出按说话人数、重叠率、相似度、轮次间隔、声学质量五维分层的多说话人ASR基准MS-Bench，揭示聚合指标掩盖的失败模式。</div>
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
| 🥇 | [MS-Bench: A Condition-Stratified Multi-Speaker ASR Benchmark](ms-bench-a-condition-stratified-multi-speaker-asr-benchmark-2610-25824/) 🎯 | **8.2** | #语音识别 |
| 🥈 | [Structural Context from Audio and Lyric Evidence for Music S…](structural-context-from-audio-and-lyric-evidence-for-music-s-2610-26253/) | **7.8** | #音乐结构分析 |
| 🥉 | [PronCFT: Pronunciation Contextual Fine-Tuning for Contextual…](proncft-pronunciation-contextual-fine-tuning-for-contextual--2610-25766/) | **7.2** | #语音识别 |
| 4. | [Manifold-Constrained Residual Adaptation with Frame-Adaptive…](manifold-constrained-residual-adaptation-with-frame-adaptive-2610-25892/) | **7.2** | #说话人验证 |
| 5. | [Multilingual Voicemail and Answering Machine Detection via P…](multilingual-voicemail-and-answering-machine-detection-via-p-2610-26100/) | **6.8** | #语音事件检测 |
| 6. | [AudioScorer: Learning Question-Aware Token Relevance for Lar…](audioscorer-learning-question-aware-token-relevance-for-larg-2610-26258/) | **6.8** | #音频处理 |
| 7. | [Expert L2 English Speech Evaluation on a Gaming PC: Accuracy…](expert-l2-english-speech-evaluation-on-a-gaming-pc-accuracy--2610-26406/) | **6.8** | #语音识别 |
| 8. | [Label Authority in Speech Emotion Recognition: Intended and …](label-authority-in-speech-emotion-recognition-intended-and-p-2610-26446/) | **6.8** | #语音情感识别 |
| 9. | [TeleASR-Amharic: A Benchmark for Robust Amharic ASR in Reali…](teleasr-amharic-a-benchmark-for-robust-amharic-asr-in-realis-2610-26448/) | **6.8** | #语音识别 |
| 10. | [Applicability and Generalization of Audio Fingerprinting Met…](applicability-and-generalization-of-audio-fingerprinting-met-2610-26112/) | **6.0** | #音频指纹 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="ms-bench-a-condition-stratified-multi-speaker-asr-benchmark-2610-25824/">MS-Bench: A Condition-Stratified Multi-Speaker ASR Benchmark</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出按说话人数、重叠率、相似度、轮次间隔、声学质量五维分层的多说话人ASR基准MS-Bench，揭示聚合指标掩盖的失败模式。</div>
<div class="card-action">
<a href="ms-bench-a-condition-stratified-multi-speaker-asr-benchmark-2610-25824/">详情 →</a> · <a href="https://arxiv.org/abs/2610.25824" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="structural-context-from-audio-and-lyric-evidence-for-music-s-2610-26253/">Structural Context from Audio and Lyric Evidence for Music Structure Analysis Using the New SheetSage-MSA Dataset</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐结构分析</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">构建 SheetSage-MSA 数据集并提出 SCALE，用分离的音频通路建模局部与长程结构，融合带时间戳歌词提升副歌识别。</div>
<div class="card-action">
<a href="structural-context-from-audio-and-lyric-evidence-for-music-s-2610-26253/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26253" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="proncft-pronunciation-contextual-fine-tuning-for-contextual--2610-25766/">PronCFT: Pronunciation Contextual Fine-Tuning for Contextual Biasing of Out-of-Vocabulary Words in LLM-Based ASR</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用固定音素序列做中间监督，训练LLM-ASR先转录音素再匹配候选拼写，缓解OOV词被近音词替换问题。</div>
<div class="card-action">
<a href="proncft-pronunciation-contextual-fine-tuning-for-contextual--2610-25766/">详情 →</a> · <a href="https://arxiv.org/abs/2610.25766" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="manifold-constrained-residual-adaptation-with-frame-adaptive-2610-25892/">Manifold-Constrained Residual Adaptation with Frame-Adaptive Layer Aggregation for Speaker Verification</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人验证</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出流形约束残差适配器MCRA与帧自适应层聚合FALA，以极少可训练参数适配WavLM做说话人验证，VoxCeleb1-O相对EER降22.4%。</div>
<div class="card-action">
<a href="manifold-constrained-residual-adaptation-with-frame-adaptive-2610-25892/">详情 →</a> · <a href="https://arxiv.org/abs/2610.25892" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="multilingual-voicemail-and-answering-machine-detection-via-p-2610-26100/">Multilingual Voicemail and Answering Machine Detection via Pretrained Audio Embeddings and Gradient Boosting Machines</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音事件检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用预训练音频嵌入加梯度提升机做轻量级答录机检测，并开源首个多语言AMD数据集OpenAMD。</div>
<div class="card-action">
<a href="multilingual-voicemail-and-answering-machine-detection-via-p-2610-26100/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26100" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="audioscorer-learning-question-aware-token-relevance-for-larg-2610-26258/">AudioScorer: Learning Question-Aware Token Relevance for Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出轻量AudioScorer，按用户问题给音频token打分，蒸馏冻结LALM的答案梯度显著性排序，实现问题感知的音频token剪枝。</div>
<div class="card-action">
<a href="audioscorer-learning-question-aware-token-relevance-for-larg-2610-26258/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26258" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="expert-l2-english-speech-evaluation-on-a-gaming-pc-accuracy--2610-26406/">Expert L2 English Speech Evaluation on a Gaming PC: Accuracy, Fluency, and Prosody with XLS-R, XEUS, and PhoneticXeus</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在消费级PC上用XLS-R/XEUS/PhoneticXeus表征加岭回归做L2英语发音、流利度、韵律三维度自动评分。</div>
<div class="card-action">
<a href="expert-l2-english-speech-evaluation-on-a-gaming-pc-accuracy--2610-26406/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26406" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="label-authority-in-speech-emotion-recognition-intended-and-p-2610-26446/">Label Authority in Speech Emotion Recognition: Intended and Perceived Ground Truth in Emozionalmente</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在意大利语表演语料 Emozionalmente 上比较三种标签权威：表演条件、听众多数票、完整投票分布，用冻结 XLS-R/HuBERT/WavLM 探针分析。</div>
<div class="card-action">
<a href="label-authority-in-speech-emotion-recognition-intended-and-p-2610-26446/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26446" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="teleasr-amharic-a-benchmark-for-robust-amharic-asr-in-realis-2610-26448/">TeleASR-Amharic: A Benchmark for Robust Amharic ASR in Realistic Telecommunication Conditions</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建阿姆哈拉语电信场景ASR基准，量化信道与噪声退化影响，并验证电信感知数据增强可显著降低极端噪声下WER。</div>
<div class="card-action">
<a href="teleasr-amharic-a-benchmark-for-robust-amharic-asr-in-realis-2610-26448/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26448" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="applicability-and-generalization-of-audio-fingerprinting-met-2610-26112/">Applicability and Generalization of Audio Fingerprinting Methods to Speech</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频指纹</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在语音数据上系统评测主流音频指纹方法，考察噪声、混响、时长、音高与有损压缩的影响，发现自监督方法优于经典方法但弱于音乐场景。</div>
<div class="card-action">
<a href="applicability-and-generalization-of-audio-fingerprinting-met-2610-26112/">详情 →</a> · <a href="https://arxiv.org/abs/2610.26112" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
