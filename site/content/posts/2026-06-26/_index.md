---
title: "语音/音频论文速递 2026-06-26"
date: 2026-06-26T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.5（#音乐生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音乐生成 | 1篇 | `██████████` |
| #音频水印 | 1篇 | `██████████` |
| #语音合成 | 1篇 | `██████████` |
| #音频处理 | 1篇 | `██████████` |
| #文本相似度编码 | 1篇 | `██████████` |
| #音频编码 | 1篇 | `██████████` |
| #歌唱质量评估 | 1篇 | `██████████` |
| #音频事件检测 | 1篇 | `██████████` |

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
| 🥇 | [Pianist Transformer: Towards Expressive Piano Performance Re…](pianist-transformer-towards-expressive-piano-performance-ren-2512-02652/) | **8.5** | #音乐生成 |
| 🥈 | [Latent-Mark: An Audio Watermark Robust to Neural Codec Compr…](latent-mark-an-audio-watermark-robust-to-neural-codec-compre-2603-05310/) | **8.2** | #音频水印 |
| 🥉 | [VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforceme…](voicetta-enhancing-zero-shot-text-to-speech-via-reinforcemen-2606-26534/) | **7.8** | #语音合成 |
| 4. | [Deep Regularized RNNs for Virtual Analog Modeling](deep-regularized-rnns-for-virtual-analog-modeling-2509-15622/) | **7.5** | #音频处理 |
| 5. | [AnySimLite: A Lightweight Few-Shot Similarity Encoder for On…](anysimlite-a-lightweight-few-shot-similarity-encoder-for-on--2606-26452/) | **7.2** | #文本相似度编码 |
| 6. | [Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audi…](elastic-time-dynamic-frame-rate-bottlenecks-for-neural-audio-2606-27320/) | **7.2** | #音频编码 |
| 7. | [Listening Like a Judge: A Music-Aware Framework for Automati…](listening-like-a-judge-a-music-aware-framework-for-automatic-2606-26451/) | **7.2** | #歌唱质量评估 |
| 8. | [Soroll-IA: A Weakly Labeled Audio Dataset for Real-World Ind…](soroll-ia-a-weakly-labeled-audio-dataset-for-real-world-indu-2606-26195/) | **7.2** | #音频事件检测 |
| 9. | [Neural Speaker Diarization via Multilingual Training: Evalua…](neural-speaker-diarization-via-multilingual-training-evaluat-2606-26144/) | **7.2** | #说话人日志 |
| 10. | [Generative AI and Copyright Infringement: A Legal-Technical …](generative-ai-and-copyright-infringement-a-legal-technical-a-2606-26111/) | **5.5** | #法律分析 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="pianist-transformer-towards-expressive-piano-performance-ren-2512-02652/">Pianist Transformer: Towards Expressive Piano Performance Rendering via Scalable Self-Supervised Pre-Training</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出Pianist Transformer，通过大规模自监督预训练和高效非对称Transformer架构，实现从乐谱到富有表现力的钢琴演奏生成。</div>
<div class="card-action">
<a href="pianist-transformer-towards-expressive-piano-performance-ren-2512-02652/">详情 →</a> · <a href="https://arxiv.org/abs/2512.02652" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="latent-mark-an-audio-watermark-robust-to-neural-codec-compre-2603-05310/">Latent-Mark: An Audio Watermark Robust to Neural Codec Compression</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Latent-Mark，首个在神经音频编解码器压缩下鲁棒的零比特音频水印框架，通过将水印嵌入编解码器不变潜在空间实现。</div>
<div class="card-action">
<a href="latent-mark-an-audio-watermark-robust-to-neural-codec-compre-2603-05310/">详情 →</a> · <a href="https://arxiv.org/abs/2603.05310" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="voicetta-enhancing-zero-shot-text-to-speech-via-reinforcemen-2606-26534/">VoiceTTA: Enhancing Zero-Shot Text-to-Speech via Reinforcement Learning-Based Test-Time Adaptation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出VoiceTTA，通过强化学习在推理时优化可学习前缀，提升零样本TTS对罕见说话风格的模仿能力。</div>
<div class="card-action">
<a href="voicetta-enhancing-zero-shot-text-to-speech-via-reinforcemen-2606-26534/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26534" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="deep-regularized-rnns-for-virtual-analog-modeling-2509-15622/">Deep Regularized RNNs for Virtual Analog Modeling</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出深度控制条件LSTM和伽马通滤波器组损失，在虚拟模拟建模中消除时变控制噪声伪影，同时保持建模精度。</div>
<div class="card-action">
<a href="deep-regularized-rnns-for-virtual-analog-modeling-2509-15622/">详情 →</a> · <a href="https://arxiv.org/abs/2509.15622" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="anysimlite-a-lightweight-few-shot-similarity-encoder-for-on--2606-26452/">AnySimLite: A Lightweight Few-Shot Similarity Encoder for On-Device Speech-Adjacent Classification</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#文本相似度编码</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出AnySimLite，一种轻量级少样本相似度编码器，通过将多个语音相关分类任务转化为文本相似度问题，在边缘设备上实现SOTA或接近SOTA的性能，模型大小仅为SOTA基线的1/250。</div>
<div class="card-action">
<a href="anysimlite-a-lightweight-few-shot-similarity-encoder-for-on--2606-26452/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26452" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="elastic-time-dynamic-frame-rate-bottlenecks-for-neural-audio-2606-27320/">Elastic Time: Dynamic Frame Rate Bottlenecks for Neural Audio Coding</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频编码</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出Elastic Time动态帧率瓶颈，将固定帧率音频自编码器转为动态帧率，在推理时实现率控并提升效率-质量权衡。</div>
<div class="card-action">
<a href="elastic-time-dynamic-frame-rate-bottlenecks-for-neural-audio-2606-27320/">详情 →</a> · <a href="https://arxiv.org/abs/2606.27320" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="listening-like-a-judge-a-music-aware-framework-for-automatic-2606-26451/">Listening Like a Judge: A Music-Aware Framework for Automatic Singing Performance Evaluation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#歌唱质量评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MusicJudge框架，通过模态引导的多模态分析，结合歌词正确性与音高-节奏保真度，实现自动歌唱质量评估。</div>
<div class="card-action">
<a href="listening-like-a-judge-a-music-aware-framework-for-automatic-2606-26451/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26451" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="soroll-ia-a-weakly-labeled-audio-dataset-for-real-world-indu-2606-26195/">Soroll-IA: A Weakly Labeled Audio Dataset for Real-World Industrial Port Monitoring</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频事件检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发布了一个22小时、26类工业港口声音事件的弱标注数据集，含两个专家标注版本，并提供CNN14和MobileNetV2基准结果。</div>
<div class="card-action">
<a href="soroll-ia-a-weakly-labeled-audio-dataset-for-real-world-indu-2606-26195/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26195" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="neural-speaker-diarization-via-multilingual-training-evaluat-2606-26144/">Neural Speaker Diarization via Multilingual Training: Evaluation on Low-Resource Nepali-Hindi Speech</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文通过多语言训练，比较EEND-EDA和DiaPer两种端到端神经说话人日志架构在低资源尼泊尔-印地语上的表现，DiaPer在多数场景下DER更低。</div>
<div class="card-action">
<a href="neural-speaker-diarization-via-multilingual-training-evaluat-2606-26144/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26144" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="generative-ai-and-copyright-infringement-a-legal-technical-a-2606-26111/">Generative AI and Copyright Infringement: A Legal-Technical Analysis of AI Music Generation Systems Under 17 U.S.C. Title 17</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#法律分析</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">本文从法律和技术角度分析AI音乐生成系统（如Google Gemini）在17 U.S.C. Title 17下的版权侵权风险，指出歌词复制侵权风险高，而语音克隆主要涉及州级公开权。</div>
<div class="card-action">
<a href="generative-ai-and-copyright-infringement-a-legal-technical-a-2606-26111/">详情 →</a> · <a href="https://arxiv.org/abs/2606.26111" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
