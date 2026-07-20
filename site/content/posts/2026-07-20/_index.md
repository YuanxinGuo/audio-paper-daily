---
title: "语音/音频论文速递 2026-07-20"
date: 2026-07-20T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.2（#语音合成）"
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
| #语音合成 | 2篇 | `██████████` |
| #音频混合风格建模 | 1篇 | `█████` |
| #自监督学习 | 1篇 | `█████` |
| #后门防御 | 1篇 | `█████` |
| #音乐质量评估 | 1篇 | `█████` |
| #声源定位 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #视频编解码 | 1篇 | `█████` |

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
| 🥇 | [AuEmoChat: Authentic Emotion Understanding and Rendering for…](auemochat-authentic-emotion-understanding-and-rendering-for--2607-15755/) | **8.2** | #语音合成 |
| 🥈 | [StemFX: Learning Mixing Style Representations via Autoregres…](stemfx-learning-mixing-style-representations-via-autoregress-2607-15634/) | **8.2** | #音频混合风格建模 |
| 🥉 | [AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Le…](av-jepa-extending-lejepa-to-audio-visual-self-supervised-lea-2607-15295/) | **7.8** | #自监督学习 |
| 4. | [RobustSpeechFlow: Learning Robust Text-to-Speech Trajectorie…](robustspeechflow-learning-robust-text-to-speech-trajectories-2605-22083/) | **7.6** | #语音合成 |
| 5. | [SpeechGuard: Online Defense against Backdoor Attacks on Spee…](speechguard-online-defense-against-backdoor-attacks-on-speec-2607-15697/) | **7.2** | #后门防御 |
| 6. | [Song Aesthetics Evaluation with Multi-Stem Attention and Hie…](song-aesthetics-evaluation-with-multi-stem-attention-and-hie-2601-12222/) | **7.2** | #音乐质量评估 |
| 7. | [Acoustic Imaging for UAV Detection: Dense Beamformed Energy …](acoustic-imaging-for-uav-detection-dense-beamformed-energy-m-2508-00307/) | **7.2** | #声源定位 |
| 8. | [Natural Backdoor Attacks on Speech Recognition Models](natural-backdoor-attacks-on-speech-recognition-models-2607-15724/) | **6.5** | #语音识别 |
| 9. | [Data-driven Video Codec with Implicit Neural Representations](data-driven-video-codec-with-implicit-neural-representations-2607-15298/) | **5.5** | #视频编解码 |
| 10. | [Harmonic and transposition constraints arising from the use …](harmonic-and-transposition-constraints-arising-from-the-use--2502-07524/) | **4.5** | #音乐制作分析 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="auemochat-authentic-emotion-understanding-and-rendering-for--2607-15755/">AuEmoChat: Authentic Emotion Understanding and Rendering for Conversational Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AuEmoChat框架，通过离散情感令牌空间和令牌合并算法，实现更真实的情感对话语音合成。</div>
<div class="card-action">
<a href="auemochat-authentic-emotion-understanding-and-rendering-for--2607-15755/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15755" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="stemfx-learning-mixing-style-representations-via-autoregress-2607-15634/">StemFX: Learning Mixing Style Representations via Autoregressive FX Chain Prediction on Source-Separated Stems</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频混合风格建模</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出StemFX，通过自回归预测源分离音轨上的可变长度效果链来学习音频混合风格表示。</div>
<div class="card-action">
<a href="stemfx-learning-mixing-style-representations-via-autoregress-2607-15634/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15634" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="av-jepa-extending-lejepa-to-audio-visual-self-supervised-lea-2607-15295/">AV-JEPA: Extending LeJEPA to Audio-Visual Self-Supervised Learning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#自监督学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AV-JEPA，将LeJEPA扩展到音视频自监督学习，采用早期融合ViT和模态丢弃，无需解码器或负样本，在VGGSound和AudioSet上取得有竞争力的分类与检索性能。</div>
<div class="card-action">
<a href="av-jepa-extending-lejepa-to-audio-visual-self-supervised-lea-2607-15295/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15295" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="robustspeechflow-learning-robust-text-to-speech-trajectories-2605-22083/">RobustSpeechFlow: Learning Robust Text-to-Speech Trajectories via Augmentation-based Contrastive Flow Matching</a>
<div class="card-meta">
<span class="card-score">7.6</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过扩展对比流匹配与长度保持的重复/跳过潜在增强，提升TTS对齐鲁棒性，降低字错误率。</div>
<div class="card-action">
<a href="robustspeechflow-learning-robust-text-to-speech-trajectories-2605-22083/">详情 →</a> · <a href="https://arxiv.org/abs/2605.22083" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="speechguard-online-defense-against-backdoor-attacks-on-speec-2607-15697/">SpeechGuard: Online Defense against Backdoor Attacks on Speech Recognition Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#后门防御</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SpeechGuard，首个在线后门防御流程，通过自适应扰动注入检测并净化中毒音频样本，保护语音识别模型。</div>
<div class="card-action">
<a href="speechguard-online-defense-against-backdoor-attacks-on-speec-2607-15697/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15697" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="song-aesthetics-evaluation-with-multi-stem-attention-and-hie-2601-12222/">Song Aesthetics Evaluation with Multi-Stem Attention and Hierarchical Uncertainty Modeling</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐质量评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出多轨注意力融合与分层粒度感知区间聚合的歌曲美学评估框架，在AI生成和人工创作歌曲数据集上优于现有模型。</div>
<div class="card-action">
<a href="song-aesthetics-evaluation-with-multi-stem-attention-and-hie-2601-12222/">详情 →</a> · <a href="https://arxiv.org/abs/2601.12222" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="acoustic-imaging-for-uav-detection-dense-beamformed-energy-m-2508-00307/">Acoustic Imaging for UAV Detection: Dense Beamformed Energy Maps and U-Net SELD</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声源定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出U-Net模型将360°声源定位转化为球面语义分割任务，通过分割波束成形能量图实现无人机检测，并泛化至DCASE SELD任务。</div>
<div class="card-action">
<a href="acoustic-imaging-for-uav-detection-dense-beamformed-energy-m-2508-00307/">详情 →</a> · <a href="https://arxiv.org/abs/2508.00307" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="natural-backdoor-attacks-on-speech-recognition-models-2607-15724/">Natural Backdoor Attacks on Speech Recognition Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出使用日常自然声音作为触发器，对语音识别模型实施后门攻击，仅需5%中毒样本即可接近100%攻击成功率。</div>
<div class="card-action">
<a href="natural-backdoor-attacks-on-speech-recognition-models-2607-15724/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15724" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="data-driven-video-codec-with-implicit-neural-representations-2607-15298/">Data-driven Video Codec with Implicit Neural Representations</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#视频编解码</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出用单个SIREN网络同时编码视频和音频，通过知识蒸馏和量化压缩，但性能远低于传统编解码器。</div>
<div class="card-action">
<a href="data-driven-video-codec-with-implicit-neural-representations-2607-15298/">详情 →</a> · <a href="https://arxiv.org/abs/2607.15298" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="harmonic-and-transposition-constraints-arising-from-the-use--2502-07524/">Harmonic and transposition constraints arising from the use of the Roland TR-808 bass drum</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#音乐制作分析</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">研究嘻哈制作人Scott Storch将歌曲调性移调以适应TR-808底鼓而非调鼓以适应调性的做法，分析其背后的声学与制作动机。</div>
<div class="card-action">
<a href="harmonic-and-transposition-constraints-arising-from-the-use--2502-07524/">详情 →</a> · <a href="https://arxiv.org/abs/2502.07524" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
