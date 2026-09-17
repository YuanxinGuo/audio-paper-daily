---
title: "语音/音频论文速递 2026-09-17"
date: 2026-09-17T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.0（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.0</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #语音识别 | 2篇 | `███████` |
| #音乐信息检索 | 2篇 | `███████` |
| #声源定位与检测 | 1篇 | `███` |
| #音频伪造检测 | 1篇 | `███` |
| #音乐生成 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="g-mamba-sparse-graph-guided-mamba-for-audio-visual-speech-en-2609-18009/">G-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用稀疏异构图引导 Mamba 主干做轻量音视频语音增强，在 LRS3 噪声条件下达 13.091 dB SI-SDR，计算量仅 3.45 G MACs。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="absolute-quality-ratings-of-speech-enhancement-systems-by-li-2609-18714/">Absolute Quality Ratings of Speech Enhancement Systems by Listeners of Different Ages and Degrees of Hearing Loss</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">对比40名年轻正常听力与67名老年（含不同程度听力损失）听者对语音增强系统的主观绝对质量评分，发现老年组对系统间差异的区分度明显收缩。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mask-based-speech-enhancement-for-spatial-audio-a-comparison-2609-18532/">Mask-Based Speech Enhancement for Spatial Audio: A Comparison of Ambisonics, Beamforming, and Microphone Channels</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">系统比较麦克风、波束成形与Ambisonics三种域上做时频掩蔽的语音增强，揭示增强与空间保真度的权衡。</div>
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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mask-based-speech-enhancement-for-spatial-audio-a-comparison-2609-18532/">Mask-Based Speech Enhancement for Spatial Audio: A Comparison of Ambisonics, Beamforming, and Microphone Channels</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">系统比较麦克风、波束成形与Ambisonics三种域上做时频掩蔽的语音增强，揭示增强与空间保真度的权衡。</div>
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
| 🥇 | [G-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech E…](g-mamba-sparse-graph-guided-mamba-for-audio-visual-speech-en-2609-18009/) 🎯 | **8.0** | #语音增强 |
| 🥈 | [Absolute Quality Ratings of Speech Enhancement Systems by Li…](absolute-quality-ratings-of-speech-enhancement-systems-by-li-2609-18714/) 🎯 | **7.8** | #语音增强 |
| 🥉 | [Mask-Based Speech Enhancement for Spatial Audio: A Compariso…](mask-based-speech-enhancement-for-spatial-audio-a-comparison-2609-18532/) 🎯 | **7.8** | #语音增强 |
| 4. | [Task-oriented neural FOA encoding for SELD from irregular mi…](task-oriented-neural-foa-encoding-for-seld-from-irregular-mi-2609-18040/) | **7.0** | #声源定位与检测 |
| 5. | [Arti-JEPA: Adapting Video World Model to Real-Time MRI of th…](arti-jepa-adapting-video-world-model-to-real-time-mri-of-the-2609-09757/) | **6.8** | #语音识别 |
| 6. | [Scalable Music Cover Retrieval Using Lyrics-Aligned Audio Em…](scalable-music-cover-retrieval-using-lyrics-aligned-audio-em-2601-11262/) | **6.8** | #音乐信息检索 |
| 7. | [HearInContext: A Benchmark for Implicit Context in Speech Re…](hearincontext-a-benchmark-for-implicit-context-in-speech-rec-2609-18680/) | **6.8** | #语音识别 |
| 8. | [What Affects the Performance of Fake Audio Detection? Analyz…](what-affects-the-performance-of-fake-audio-detection-analyzi-2609-19067/) | **6.8** | #音频伪造检测 |
| 9. | [Instrument Classification of Solo Sheet Music Images](instrument-classification-of-solo-sheet-music-images-2609-18980/) | **4.5** | #音乐信息检索 |
| 10. | [Encypher: Shared Agency and Social Presence in Collaborative…](encypher-shared-agency-and-social-presence-in-collaborative--2609-18062/) | **3.5** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="g-mamba-sparse-graph-guided-mamba-for-audio-visual-speech-en-2609-18009/">G-Mamba: Sparse Graph-Guided Mamba for Audio-Visual Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用稀疏异构图引导 Mamba 主干做轻量音视频语音增强，在 LRS3 噪声条件下达 13.091 dB SI-SDR，计算量仅 3.45 G MACs。</div>
<div class="card-action">
<a href="g-mamba-sparse-graph-guided-mamba-for-audio-visual-speech-en-2609-18009/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18009" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="absolute-quality-ratings-of-speech-enhancement-systems-by-li-2609-18714/">Absolute Quality Ratings of Speech Enhancement Systems by Listeners of Different Ages and Degrees of Hearing Loss</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">对比40名年轻正常听力与67名老年（含不同程度听力损失）听者对语音增强系统的主观绝对质量评分，发现老年组对系统间差异的区分度明显收缩。</div>
<div class="card-action">
<a href="absolute-quality-ratings-of-speech-enhancement-systems-by-li-2609-18714/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18714" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="mask-based-speech-enhancement-for-spatial-audio-a-comparison-2609-18532/">Mask-Based Speech Enhancement for Spatial Audio: A Comparison of Ambisonics, Beamforming, and Microphone Channels</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统比较麦克风、波束成形与Ambisonics三种域上做时频掩蔽的语音增强，揭示增强与空间保真度的权衡。</div>
<div class="card-action">
<a href="mask-based-speech-enhancement-for-spatial-audio-a-comparison-2609-18532/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18532" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="task-oriented-neural-foa-encoding-for-seld-from-irregular-mi-2609-18040/">Task-oriented neural FOA encoding for SELD from irregular microphone arrays</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#声源定位与检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两阶段SELD框架，用神经残差编码器修正传统FOA编码，并通过教师-学生帧级置换不变蒸馏迁移事件与空间知识。</div>
<div class="card-action">
<a href="task-oriented-neural-foa-encoding-for-seld-from-irregular-mi-2609-18040/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18040" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="arti-jepa-adapting-video-world-model-to-real-time-mri-of-the-2609-09757/">Arti-JEPA: Adapting Video World Model to Real-Time MRI of the Vocal Tract for Speech-Production Analysis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将视频世界模型 V-JEPA 适配到实时 MRI 声道视频，冻结表征用于音素预测、口吃分类与舌切除术后分析。</div>
<div class="card-action">
<a href="arti-jepa-adapting-video-world-model-to-real-time-mri-of-the-2609-09757/">详情 →</a> · <a href="https://arxiv.org/abs/2609.09757" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="scalable-music-cover-retrieval-using-lyrics-aligned-audio-em-2601-11262/">Scalable Music Cover Retrieval Using Lyrics-Aligned Audio Embeddings</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">LIVI 用歌词对齐的音频嵌入做翻唱检索，训练时借助转录与文本嵌入监督，推理时去掉转录步骤，兼顾精度与效率。</div>
<div class="card-action">
<a href="scalable-music-cover-retrieval-using-lyrics-aligned-audio-em-2601-11262/">详情 →</a> · <a href="https://arxiv.org/abs/2601.11262" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="hearincontext-a-benchmark-for-implicit-context-in-speech-rec-2609-18680/">HearInContext: A Benchmark for Implicit Context in Speech Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 HearInContext 中英双语基准，用同音词与助手回复构造隐式/显式上下文，评测 ASR 的上下文利用能力。</div>
<div class="card-action">
<a href="hearincontext-a-benchmark-for-implicit-context-in-speech-rec-2609-18680/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18680" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="what-affects-the-performance-of-fake-audio-detection-analyzi-2609-19067/">What Affects the Performance of Fake Audio Detection? Analyzing Factors in a Continual Learning Setting</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统分析攻击者架构、训练数据、说话人多样性与任务顺序对持续学习下伪造音频检测性能的影响。</div>
<div class="card-action">
<a href="what-affects-the-performance-of-fake-audio-detection-analyzi-2609-19067/">详情 →</a> · <a href="https://arxiv.org/abs/2609.19067" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="instrument-classification-of-solo-sheet-music-images-2609-18980/">Instrument Classification of Solo Sheet Music Images</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">将独奏乐谱图像转为 bootleg score 词序列，用 AWD-LSTM/GPT-2/RoBERTa 做乐器分类，预训练加数据增强提升准确率。</div>
<div class="card-action">
<a href="instrument-classification-of-solo-sheet-music-images-2609-18980/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18980" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="encypher-shared-agency-and-social-presence-in-collaborative--2609-18062/">Encypher: Shared Agency and Social Presence in Collaborative Music Generation for Dance Cyphers</a>
<div class="card-meta">
<span class="card-score">3.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">Encypher 将舞者集体动作特征转为文本提示，实时驱动生成音乐，用于舞蹈 cypher 场景的人机共创。</div>
<div class="card-action">
<a href="encypher-shared-agency-and-social-presence-in-collaborative--2609-18062/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18062" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
