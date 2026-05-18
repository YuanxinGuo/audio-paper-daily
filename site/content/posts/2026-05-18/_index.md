---
title: "语音/音频论文速递 2026-05-18"
date: 2026-05-18T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 9.2（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #音乐生成 | 2篇 | `███████` |
| #语音带宽扩展 | 1篇 | `███` |
| #音频编码 | 1篇 | `███` |
| #多模态生成 | 1篇 | `███` |
| #有害语音检测 | 1篇 | `███` |
| #视频编辑 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="global-rotation-equivariant-phase-modeling-for-speech-enhanc-2602-08556/">Global Rotation Equivariant Phase Modeling for Speech Enhancement with Deep Magnitude-Phase Interaction</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出全局旋转等变相位建模的幅度-相位双流框架，通过保持相位流旋转等变性提升语音增强性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="cis-bwe-chaos-informed-speech-bandwidth-extension-2507-15970/">CIS-BWE: Chaos-Informed Speech Bandwidth Extension</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音带宽扩展</span>
</div>
<div class="card-tldr">提出NDSI-BWE框架，利用七个基于非线性动力学的判别器引导复数ConformerNeXt生成器，实现语音带宽扩展，参数减少8倍，在多个指标上达到新SOTA。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="real-time-speech-restoration-using-data-prediction-mean-flow-2605-16251/">Real-time Speech Restoration using Data Prediction Mean Flows</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种基于数据预测均值流的实时语音恢复模型，在极低计算量下实现与离线模型相当的音频质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="leveraging-local-and-global-knowledge-integration-with-time--2506-13127/">Leveraging Local and Global Knowledge Integration with Time-Frequency Calibrated Distillation for Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出I²SRF-TFCKD框架，通过组内组间递归融合和时频校准蒸馏，提升低复杂度学生模型在语音增强上的性能。</div>
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
| 🥇 | [Global Rotation Equivariant Phase Modeling for Speech Enhanc…](global-rotation-equivariant-phase-modeling-for-speech-enhanc-2602-08556/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [CIS-BWE: Chaos-Informed Speech Bandwidth Extension](cis-bwe-chaos-informed-speech-bandwidth-extension-2507-15970/) 🎯 | **8.8** | #语音带宽扩展 |
| 🥉 | [Real-time Speech Restoration using Data Prediction Mean Flow…](real-time-speech-restoration-using-data-prediction-mean-flow-2605-16251/) 🎯 | **8.8** | #语音增强 |
| 4. | [Leveraging Local and Global Knowledge Integration with Time-…](leveraging-local-and-global-knowledge-integration-with-time--2506-13127/) 🎯 | **8.6** | #语音增强 |
| 5. | [Two-Dimensional Quantization for Geometry-Aware Audio Coding](two-dimensional-quantization-for-geometry-aware-audio-coding-2512-01537/) | **8.2** | #音频编码 |
| 6. | [JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching](jam-flow-joint-audio-motion-synthesis-with-flow-matching-2506-23552/) | **8.2** | #多模态生成 |
| 7. | [Beyond Content: A Comprehensive Speech Toxicity Dataset and …](beyond-content-a-comprehensive-speech-toxicity-dataset-and-d-2605-15984/) | **7.8** | #有害语音检测 |
| 8. | [Sound Sparks Motion: Audio and Text Tuning for Video Editing](sound-sparks-motion-audio-and-text-tuning-for-video-editing-2605-15307/) | **7.5** | #视频编辑 |
| 9. | [ARIA: A Diagnostic Framework for Music Training Data Attribu…](aria-a-diagnostic-framework-for-music-training-data-attribut-2605-16181/) | **7.5** | #音乐生成 |
| 10. | [Modeling Music as a Time-Frequency Image: A 2D Tokenizer for…](modeling-music-as-a-time-frequency-image-a-2d-tokenizer-for--2605-15831/) | **7.2** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="global-rotation-equivariant-phase-modeling-for-speech-enhanc-2602-08556/">Global Rotation Equivariant Phase Modeling for Speech Enhancement with Deep Magnitude-Phase Interaction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出全局旋转等变相位建模的幅度-相位双流框架，通过保持相位流旋转等变性提升语音增强性能。</div>
<div class="card-action">
<a href="global-rotation-equivariant-phase-modeling-for-speech-enhanc-2602-08556/">详情 →</a> · <a href="https://arxiv.org/abs/2602.08556" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="cis-bwe-chaos-informed-speech-bandwidth-extension-2507-15970/">CIS-BWE: Chaos-Informed Speech Bandwidth Extension</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音带宽扩展</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出NDSI-BWE框架，利用七个基于非线性动力学的判别器引导复数ConformerNeXt生成器，实现语音带宽扩展，参数减少8倍，在多个指标上达到新SOTA。</div>
<div class="card-action">
<a href="cis-bwe-chaos-informed-speech-bandwidth-extension-2507-15970/">详情 →</a> · <a href="https://arxiv.org/abs/2507.15970" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="real-time-speech-restoration-using-data-prediction-mean-flow-2605-16251/">Real-time Speech Restoration using Data Prediction Mean Flows</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种基于数据预测均值流的实时语音恢复模型，在极低计算量下实现与离线模型相当的音频质量。</div>
<div class="card-action">
<a href="real-time-speech-restoration-using-data-prediction-mean-flow-2605-16251/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16251" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="leveraging-local-and-global-knowledge-integration-with-time--2506-13127/">Leveraging Local and Global Knowledge Integration with Time-Frequency Calibrated Distillation for Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出I²SRF-TFCKD框架，通过组内组间递归融合和时频校准蒸馏，提升低复杂度学生模型在语音增强上的性能。</div>
<div class="card-action">
<a href="leveraging-local-and-global-knowledge-integration-with-time--2506-13127/">详情 →</a> · <a href="https://arxiv.org/abs/2506.13127" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="two-dimensional-quantization-for-geometry-aware-audio-coding-2512-01537/">Two-Dimensional Quantization for Geometry-Aware Audio Coding</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频编码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出二维量化（Q2D2），将特征对投影到结构化2D网格（六边形、菱形、矩形）量化，提升音频压缩效率与码本利用率，在语音、音频、音乐上达到SOTA重建质量。</div>
<div class="card-action">
<a href="two-dimensional-quantization-for-geometry-aware-audio-coding-2512-01537/">详情 →</a> · <a href="https://arxiv.org/abs/2512.01537" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="jam-flow-joint-audio-motion-synthesis-with-flow-matching-2506-23552/">JAM-Flow: Joint Audio-Motion Synthesis with Flow Matching</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#多模态生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出JAM-Flow，利用流匹配和MM-DiT架构统一联合生成面部运动与语音，支持多种条件输入。</div>
<div class="card-action">
<a href="jam-flow-joint-audio-motion-synthesis-with-flow-matching-2506-23552/">详情 →</a> · <a href="https://arxiv.org/abs/2506.23552" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="beyond-content-a-comprehensive-speech-toxicity-dataset-and-d-2605-15984/">Beyond Content: A Comprehensive Speech Toxicity Dataset and Detection Framework Incorporating Paralinguistic Cues</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#有害语音检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出大规模有害语音数据集ToxiAlert-Bench及双头神经网络框架，利用副语言线索提升检测性能。</div>
<div class="card-action">
<a href="beyond-content-a-comprehensive-speech-toxicity-dataset-and-d-2605-15984/">详情 →</a> · <a href="https://arxiv.org/abs/2605.15984" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="sound-sparks-motion-audio-and-text-tuning-for-video-editing-2605-15307/">Sound Sparks Motion: Audio and Text Tuning for Video Editing</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#视频编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无需训练的测试时调优框架，通过调整音频潜变量和文本条件扰动实现视频运动编辑。</div>
<div class="card-action">
<a href="sound-sparks-motion-audio-and-text-tuning-for-video-editing-2605-15307/">详情 →</a> · <a href="https://arxiv.org/abs/2605.15307" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="aria-a-diagnostic-framework-for-music-training-data-attribut-2605-16181/">ARIA: A Diagnostic Framework for Music Training Data Attribution</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ARIA框架，将音乐生成模型的训练数据归因分解到多个音乐维度，并给出可靠性诊断。</div>
<div class="card-action">
<a href="aria-a-diagnostic-framework-for-music-training-data-attribut-2605-16181/">详情 →</a> · <a href="https://arxiv.org/abs/2605.16181" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="modeling-music-as-a-time-frequency-image-a-2d-tokenizer-for--2605-15831/">Modeling Music as a Time-Frequency Image: A 2D Tokenizer for Music Generation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出BandTok，一种面向音乐生成的2D梅尔频谱分词器，用单一码本表示频带token，简化自回归建模。</div>
<div class="card-action">
<a href="modeling-music-as-a-time-frequency-image-a-2d-tokenizer-for--2605-15831/">详情 →</a> · <a href="https://arxiv.org/abs/2605.15831" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
