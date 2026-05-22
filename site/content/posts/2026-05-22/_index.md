---
title: "语音/音频论文速递 2026-05-22"
date: 2026-05-22T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.5（#语音转换）"
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
| #音乐生成 | 2篇 | `██████████` |
| #语音转换 | 1篇 | `█████` |
| #声音事件检测 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #水下声学目标识别 | 1篇 | `█████` |
| #音频情感分析 | 1篇 | `█████` |
| #声音合成 | 1篇 | `█████` |

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
| 🥇 | [OneVoice: One Model, Triple Scenarios-Towards Unified Zero-s…](onevoice-one-model-triple-scenarios-towards-unified-zero-sho-2601-18094/) | **8.5** | #语音转换 |
| 🥈 | [Live Music Diffusion Models: Efficient Fine-Tuning and Post-…](live-music-diffusion-models-efficient-fine-tuning-and-post-t-2605-22717/) | **8.2** | #音乐生成 |
| 🥉 | [Towards Open World Sound Event Detection](towards-open-world-sound-event-detection-2605-03934/) | **7.8** | #声音事件检测 |
| 4. | [A strongly annotated passive acoustic dataset for tropical b…](a-strongly-annotated-passive-acoustic-dataset-for-tropical-b-2605-20578/) | **7.5** | #生物声学 |
| 5. | [Academic Text-to-Music Grand Challenge: Datasets, Baselines,…](academic-text-to-music-grand-challenge-datasets-baselines-an-2605-21538/) | **7.5** | #音乐生成 |
| 6. | [Quantizing Whisper-small: How design choices affect ASR perf…](quantizing-whisper-small-how-design-choices-affect-asr-perfo-2511-08093/) | **7.2** | #语音识别 |
| 7. | [Modulation Feature Enhancement with a Multi-Stage Attention …](modulation-feature-enhancement-with-a-multi-stage-attention--2605-16304/) | **6.5** | #水下声学目标识别 |
| 8. | [Exploring How Audio Effects Alter Emotion with Foundation Mo…](exploring-how-audio-effects-alter-emotion-with-foundation-mo-2509-15151/) | **6.5** | #音频情感分析 |
| 9. | [Real-time, EDM-inspired sonfication of the activity of a sup…](real-time-edm-inspired-sonfication-of-the-activity-of-a-supe-2605-21874/) | **6.5** | #声音合成 |
| 10. | [Go witheFlow: Real-time Emotion Driven Audio Effects Modulat…](go-witheflow-real-time-emotion-driven-audio-effects-modulati-2510-02171/) | **5.5** | #音频效果调制 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="onevoice-one-model-triple-scenarios-towards-unified-zero-sho-2601-18094/">OneVoice: One Model, Triple Scenarios-Towards Unified Zero-shot Voice Conversion</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">OneVoice提出统一框架，通过MoE和双路径路由机制，在单个模型中同时处理语言保持、表现力和歌唱三种语音转换场景。</div>
<div class="card-action">
<a href="onevoice-one-model-triple-scenarios-towards-unified-zero-sho-2601-18094/">详情 →</a> · <a href="https://arxiv.org/abs/2601.18094" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="live-music-diffusion-models-efficient-fine-tuning-and-post-t-2605-22717/">Live Music Diffusion Models: Efficient Fine-Tuning and Post-Training of Interactive Diffusion Music Generators</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Live Music Diffusion Models，通过块级KV缓存和ARC-Forcing对齐，将非流式扩散模型高效转化为交互式音乐生成模型，在消费级硬件上实现实时性能。</div>
<div class="card-action">
<a href="live-music-diffusion-models-efficient-fine-tuning-and-post-t-2605-22717/">详情 →</a> · <a href="https://arxiv.org/abs/2605.22717" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="towards-open-world-sound-event-detection-2605-03934/">Towards Open World Sound Event Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声音事件检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出开放世界声音事件检测范式OW-SED，设计WOOT框架，利用可变形注意力与特征解耦实现已知事件检测、未知事件识别与增量学习。</div>
<div class="card-action">
<a href="towards-open-world-sound-event-detection-2605-03934/">详情 →</a> · <a href="https://arxiv.org/abs/2605.03934" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="a-strongly-annotated-passive-acoustic-dataset-for-tropical-b-2605-20578/">A strongly annotated passive acoustic dataset for tropical bird monitoring</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PteroSet是一个包含15,372个强标注的哥伦比亚热带鸟鸣数据集，提供COCO格式标注和深度学习基线。</div>
<div class="card-action">
<a href="a-strongly-annotated-passive-acoustic-dataset-for-tropical-b-2605-20578/">详情 →</a> · <a href="https://arxiv.org/abs/2605.20578" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="academic-text-to-music-grand-challenge-datasets-baselines-an-2605-21538/">Academic Text-to-Music Grand Challenge: Datasets, Baselines, and Evaluation Methods</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ICME 2026学术文本到音乐生成挑战赛，提供标准化数据集、基线和评估方法，旨在降低学术研究门槛。</div>
<div class="card-action">
<a href="academic-text-to-music-grand-challenge-datasets-baselines-an-2605-21538/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21538" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="quantizing-whisper-small-how-design-choices-affect-asr-perfo-2511-08093/">Quantizing Whisper-small: How design choices affect ASR performance</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统评估了Whisper-small后训练量化的设计选择，发现动态int8量化在57%压缩下提升WER。</div>
<div class="card-action">
<a href="quantizing-whisper-small-how-design-choices-affect-asr-perfo-2511-08093/">详情 →</a> · <a href="https://arxiv.org/abs/2511.08093" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="modulation-feature-enhancement-with-a-multi-stage-attention--2605-16304/">Modulation Feature Enhancement with a Multi-Stage Attention Network for Underwater Acoustic Target Recognition</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#水下声学目标识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于VMD和3/2-D谱的调制特征增强方法，结合多阶段注意力网络和类别平衡损失，提升水下目标识别性能。</div>
<div class="card-action">
<a href="modulation-feature-enhancement-with-a-multi-stage-attention--2605-16304/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16304" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="exploring-how-audio-effects-alter-emotion-with-foundation-mo-2509-15151/">Exploring How Audio Effects Alter Emotion with Foundation Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频情感分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">利用基础模型分析混响、失真等音频效果对音乐情感的影响，揭示非线性关系。</div>
<div class="card-action">
<a href="exploring-how-audio-effects-alter-emotion-with-foundation-mo-2509-15151/">详情 →</a> · <a href="https://arxiv.org/abs/2509.15151" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="real-time-edm-inspired-sonfication-of-the-activity-of-a-supe-2605-21874/">Real-time, EDM-inspired sonfication of the activity of a supercomputer</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#声音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一种受EDM启发的实时声音化方法，将超级计算机节点活动数据转化为风格一致的音乐，用于长时间监控。</div>
<div class="card-action">
<a href="real-time-edm-inspired-sonfication-of-the-activity-of-a-supe-2605-21874/">详情 →</a> · <a href="https://arxiv.org/abs/2605.21874" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="go-witheflow-real-time-emotion-driven-audio-effects-modulati-2510-02171/">Go witheFlow: Real-time Emotion Driven Audio Effects Modulation</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频效果调制</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出witheFlow系统，利用生物信号和音频特征实时调制音频效果，增强音乐表演的人机协作。</div>
<div class="card-action">
<a href="go-witheflow-real-time-emotion-driven-audio-effects-modulati-2510-02171/">详情 →</a> · <a href="https://arxiv.org/abs/2510.02171" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
