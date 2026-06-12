---
title: "语音/音频论文速递 2026-06-12"
date: 2026-06-12T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.5（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #生物声学 | 2篇 | `██████████` |
| #音乐生成 | 2篇 | `██████████` |
| #文本到语音合成 | 1篇 | `█████` |
| #语音翻译 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #法律与伦理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="basenet-band-adapted-speech-enhancement-network-with-cross-b-2606-12662/">BASENet: Band-Adapted Speech Enhancement Network with Cross-Band Attention</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出BASENet，按Bark尺度分配不同容量编码器，结合跨频带注意力，以0.83M参数在VoiceBank+DEMAND上达到3.55 PESQ。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="generating-training-targets-for-real-world-speech-enhancemen-2606-13109/">Generating Training Targets for Real-World Speech Enhancement via Close-to-Distant Microphone Projection</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出C2D投影方法，利用近远麦克风真实录音生成配对训练数据，提升远场语音增强性能。</div>
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
| 🥇 | [BASENet: Band-Adapted Speech Enhancement Network with Cross-…](basenet-band-adapted-speech-enhancement-network-with-cross-b-2606-12662/) 🎯 | **9.5** | #语音增强 |
| 🥈 | [Generating Training Targets for Real-World Speech Enhancemen…](generating-training-targets-for-real-world-speech-enhancemen-2606-13109/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [Dolph2Vec: Self-Supervised Representations of Dolphin Vocali…](dolph2vec-self-supervised-representations-of-dolphin-vocaliz-2606-12503/) | **8.2** | #生物声学 |
| 4. | [Decoding Insect Song: A Multitask Semisupervised Orthoptera …](decoding-insect-song-a-multitask-semisupervised-orthoptera-b-2606-13236/) | **7.8** | #生物声学 |
| 5. | [Emo-LiPO: Listwise Preference Optimization for Fine-Grained …](emo-lipo-listwise-preference-optimization-for-fine-grained-e-2606-13006/) | **7.8** | #文本到语音合成 |
| 6. | [NaturalFlow: Reducing Disruptive Pauses for Natural Speech F…](naturalflow-reducing-disruptive-pauses-for-natural-speech-fl-2606-13121/) | **7.2** | #语音翻译 |
| 7. | [Towards Personalized Federated Learning for Dysarthric Speec…](towards-personalized-federated-learning-for-dysarthric-speec-2606-13253/) | **7.2** | #语音识别 |
| 8. | [Generative Modeling of Bach-Style Symbolic Music: A Comparat…](generative-modeling-of-bach-style-symbolic-music-a-comparati-2606-13626/) | **6.8** | #音乐生成 |
| 9. | [The Moving Drone: Negotiating Agency Between the Voice and t…](the-moving-drone-negotiating-agency-between-the-voice-and-th-2606-13640/) | **5.5** | #音乐生成 |
| 10. | [Vocal Identity Under Siege by AI Voice Cloning Technologies](vocal-identity-under-siege-by-ai-voice-cloning-technologies-2606-12812/) | **2.0** | #法律与伦理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="basenet-band-adapted-speech-enhancement-network-with-cross-b-2606-12662/">BASENet: Band-Adapted Speech Enhancement Network with Cross-Band Attention</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出BASENet，按Bark尺度分配不同容量编码器，结合跨频带注意力，以0.83M参数在VoiceBank+DEMAND上达到3.55 PESQ。</div>
<div class="card-action">
<a href="basenet-band-adapted-speech-enhancement-network-with-cross-b-2606-12662/">详情 →</a> · <a href="https://arxiv.org/abs/2606.12662" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="generating-training-targets-for-real-world-speech-enhancemen-2606-13109/">Generating Training Targets for Real-World Speech Enhancement via Close-to-Distant Microphone Projection</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出C2D投影方法，利用近远麦克风真实录音生成配对训练数据，提升远场语音增强性能。</div>
<div class="card-action">
<a href="generating-training-targets-for-real-world-speech-enhancemen-2606-13109/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13109" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="dolph2vec-self-supervised-representations-of-dolphin-vocaliz-2606-12503/">Dolph2Vec: Self-Supervised Representations of Dolphin Vocalizations</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Dolph2Vec，首个针对海豚发声的大规模物种专用自监督模型，在哨声分类和检测任务上显著优于通用基线。</div>
<div class="card-action">
<a href="dolph2vec-self-supervised-representations-of-dolphin-vocaliz-2606-12503/">详情 →</a> · <a href="https://arxiv.org/abs/2606.12503" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="decoding-insect-song-a-multitask-semisupervised-orthoptera-b-2606-13236/">Decoding Insect Song: A Multitask Semisupervised Orthoptera Bioacoustic Classifier</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出PULSE半监督多任务框架，结合弱监督分类、自监督学习和知识蒸馏，显著提升直翅目昆虫声学分类性能。</div>
<div class="card-action">
<a href="decoding-insect-song-a-multitask-semisupervised-orthoptera-b-2606-13236/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13236" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="emo-lipo-listwise-preference-optimization-for-fine-grained-e-2606-13006/">Emo-LiPO: Listwise Preference Optimization for Fine-Grained Emotion Intensity Control in LLM-based Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#文本到语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Emo-LiPO框架，将LLM-based TTS中的情感强度控制建模为排序问题，通过列表式偏好优化实现细粒度情感表达。</div>
<div class="card-action">
<a href="emo-lipo-listwise-preference-optimization-for-fine-grained-e-2606-13006/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13006" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="naturalflow-reducing-disruptive-pauses-for-natural-speech-fl-2606-13121/">NaturalFlow: Reducing Disruptive Pauses for Natural Speech Flow in Simultaneous Speech-to-Speech Translation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出流利度感知优化框架，在同步语音翻译中减少块间停顿，平衡低延迟与自然语音流。</div>
<div class="card-action">
<a href="naturalflow-reducing-disruptive-pauses-for-natural-speech-fl-2606-13121/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13121" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="towards-personalized-federated-learning-for-dysarthric-speec-2606-13253/">Towards Personalized Federated Learning for Dysarthric Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对构音障碍语音识别，提出两种联邦学习个性化聚合策略，在UASpeech和TORGO上取得WER降低。</div>
<div class="card-action">
<a href="towards-personalized-federated-learning-for-dysarthric-speec-2606-13253/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13253" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="generative-modeling-of-bach-style-symbolic-music-a-comparati-2606-13626/">Generative Modeling of Bach-Style Symbolic Music: A Comparative Study of Autoregressive, Latent-Variable, and Adversarial Approaches</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">比较自回归LSTM、潜变量模型和GAN在巴赫风格钢琴音乐生成上的表现，发现自回归模型生成质量最佳。</div>
<div class="card-action">
<a href="generative-modeling-of-bach-style-symbolic-music-a-comparati-2606-13626/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13626" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="the-moving-drone-negotiating-agency-between-the-voice-and-th-2606-13640/">The Moving Drone: Negotiating Agency Between the Voice and the Virtual</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出一种将传统静态 drone 变为动态虚拟代理的音乐系统，通过实时循环和生成式AI实现人声与虚拟 drone 的协作。</div>
<div class="card-action">
<a href="the-moving-drone-negotiating-agency-between-the-voice-and-th-2606-13640/">详情 →</a> · <a href="https://arxiv.org/abs/2606.13640" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="vocal-identity-under-siege-by-ai-voice-cloning-technologies-2606-12812/">Vocal Identity Under Siege by AI Voice Cloning Technologies</a>
<div class="card-meta">
<span class="card-score">2.0</span>
<span class="tag-pill">#法律与伦理</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">本文从法律与伦理角度分析AI语音克隆对声音身份保护的挑战，比较三种法律框架的优劣。</div>
<div class="card-action">
<a href="vocal-identity-under-siege-by-ai-voice-cloning-technologies-2606-12812/">详情 →</a> · <a href="https://arxiv.org/abs/2606.12812" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
