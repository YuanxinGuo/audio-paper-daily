---
title: "语音/音频论文速递 2026-08-11"
date: 2026-08-11T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音乐生成 | 3篇 | `██████████` |
| #语音增强 | 1篇 | `███` |
| #音频生成 | 1篇 | `███` |
| #语音编辑 | 1篇 | `███` |
| #音频超分辨率 | 1篇 | `███` |
| #音频大模型安全 | 1篇 | `███` |
| #音乐分类 | 1篇 | `███` |
| #可穿戴计算 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="cloud-boosted-low-compute-multi-channel-speech-enhancement-2608-07423/">Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出云-边协作的低计算多通道语音增强框架，通过延迟服务器输出、逐层特征增强和协作维纳滤波，显著提升边缘模型性能。</div>
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
| 🥇 | [Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement](cloud-boosted-low-compute-multi-channel-speech-enhancement-2608-07423/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Objects as Audio-Visual Modal Sound Fields](objects-as-audio-visual-modal-sound-fields-2608-05145/) | **8.2** | #音频生成 |
| 🥉 | [Multi Codec Discrete Diffusion Model for Text Guided Speech …](multi-codec-discrete-diffusion-model-for-text-guided-speech--2608-06424/) | **8.2** | #语音编辑 |
| 4. | [FiPA-SR -- FiLM-Conditioned Perceptually Informed Audio Supe…](fipa-sr-film-conditioned-perceptually-informed-audio-super-r-2605-30594/) | **7.8** | #音频超分辨率 |
| 5. | [GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradi…](grm-utility-aware-jailbreak-attacks-on-audio-llms-via-gradie-2604-09222/) | **7.2** | #音频大模型安全 |
| 6. | [MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Genera…](mi-midi-mechanistic-interpretability-of-text-to-midi-generat-2608-06638/) | **7.2** | #音乐生成 |
| 7. | [From Prompting to Describing: A Cross-Cultural Study of Lang…](from-prompting-to-describing-a-cross-cultural-study-of-langu-2608-06634/) | **7.2** | #音乐生成 |
| 8. | [Frame-Level Pansori Mode Classification with Complementary A…](frame-level-pansori-mode-classification-with-complementary-a-2608-06633/) | **7.2** | #音乐分类 |
| 9. | [Omni-modal decomposition autoencoders learn full-stack weara…](omni-modal-decomposition-autoencoders-learn-full-stack-weara-2608-07385/) | **7.2** | #可穿戴计算 |
| 10. | [Beyond Call and Response: Modelling Reciprocal Coordination …](beyond-call-and-response-modelling-reciprocal-coordination-i-2608-07376/) | **6.8** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="cloud-boosted-low-compute-multi-channel-speech-enhancement-2608-07423/">Cloud-Boosted Low-Compute Multi-Channel Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出云-边协作的低计算多通道语音增强框架，通过延迟服务器输出、逐层特征增强和协作维纳滤波，显著提升边缘模型性能。</div>
<div class="card-action">
<a href="cloud-boosted-low-compute-multi-channel-speech-enhancement-2608-07423/">详情 →</a> · <a href="https://arxiv.org/abs/2608.07423" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="objects-as-audio-visual-modal-sound-fields-2608-05145/">Objects as Audio-Visual Modal Sound Fields</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AV-MSF，用3D高斯泼溅和视觉特征先验，从多视图图像和少量撞击声重建物体级模态声音场，实现高质量撞击声渲染。</div>
<div class="card-action">
<a href="objects-as-audio-visual-modal-sound-fields-2608-05145/">详情 →</a> · <a href="https://arxiv.org/abs/2608.05145" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="multi-codec-discrete-diffusion-model-for-text-guided-speech--2608-06424/">Multi Codec Discrete Diffusion Model for Text Guided Speech Inpainting and Editing</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SIEDD，一种基于分层编解码器离散扩散的文本引导语音修复与编辑框架，在RealEdit基准上达到最优编辑性能，并优于自回归基线。</div>
<div class="card-action">
<a href="multi-codec-discrete-diffusion-model-for-text-guided-speech--2608-06424/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06424" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="fipa-sr-film-conditioned-perceptually-informed-audio-super-r-2605-30594/">FiPA-SR -- FiLM-Conditioned Perceptually Informed Audio Super-Resolution</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频超分辨率</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FiPA-SR，一种基于GAN的音频超分辨率模型，通过FiLM层适配不同输入带宽，在MUSDB上超越AudioSR且更高效。</div>
<div class="card-action">
<a href="fipa-sr-film-conditioned-perceptually-informed-audio-super-r-2605-30594/">详情 →</a> · <a href="https://arxiv.org/abs/2605.30594" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="grm-utility-aware-jailbreak-attacks-on-audio-llms-via-gradie-2604-09222/">GRM: Utility-Aware Jailbreak Attacks on Audio LLMs via Gradient-Ratio Masking</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频大模型安全</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于梯度比掩码的频带选择性越狱攻击框架GRM，在保持高越狱成功率的同时显著降低对正常任务的效用损失。</div>
<div class="card-action">
<a href="grm-utility-aware-jailbreak-attacks-on-audio-llms-via-gradie-2604-09222/">详情 →</a> · <a href="https://arxiv.org/abs/2604.09222" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="mi-midi-mechanistic-interpretability-of-text-to-midi-generat-2608-06638/">MI-MIDI: Mechanistic Interpretability of Text-to-MIDI Generation Models via Probing, Lenses and Steering</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文对两种文本到MIDI生成模型进行机制可解释性分析，揭示音乐概念在模型内部的线性表示与操控方法。</div>
<div class="card-action">
<a href="mi-midi-mechanistic-interpretability-of-text-to-midi-generat-2608-06638/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06638" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="from-prompting-to-describing-a-cross-cultural-study-of-langu-2608-06634/">From Prompting to Describing: A Cross-Cultural Study of Language for AI-Generated Music</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过配对真实Udio提示与听众描述，构建音乐提示词汇分类法，发现提示以体裁和叙事为主，叙事提示导致语义错位，且跨文化描述存在差异。</div>
<div class="card-action">
<a href="from-prompting-to-describing-a-cross-cultural-study-of-langu-2608-06634/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06634" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="frame-level-pansori-mode-classification-with-complementary-a-2608-06633/">Frame-Level Pansori Mode Classification with Complementary Audio Representations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐分类</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文提出46小时帧级盘索里调式标注，评估四种互补音频表示，发现模型学习调式相关特征而非记忆曲目，并揭示源分离对特定调式的影响。</div>
<div class="card-action">
<a href="frame-level-pansori-mode-classification-with-complementary-a-2608-06633/">详情 →</a> · <a href="https://arxiv.org/abs/2608.06633" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="omni-modal-decomposition-autoencoders-learn-full-stack-weara-2608-07385/">Omni-modal decomposition autoencoders learn full-stack wearable disentangled representations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#可穿戴计算</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出OmniDecVAEs，一种可扩展的多模态变分分解自编码器，在多达30模态的HAR任务中实现全栈解耦表示，提升识别精度与生成质量。</div>
<div class="card-action">
<a href="omni-modal-decomposition-autoencoders-learn-full-stack-weara-2608-07385/">详情 →</a> · <a href="https://arxiv.org/abs/2608.07385" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="beyond-call-and-response-modelling-reciprocal-coordination-i-2608-07376/">Beyond Call and Response: Modelling Reciprocal Coordination in Human-AI Vocal Ensembles</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文提出将无指挥人声合唱视为耦合动态系统，构建能进入集体状态而非仅跟踪的歌声智能体研究架构。</div>
<div class="card-action">
<a href="beyond-call-and-response-modelling-reciprocal-coordination-i-2608-07376/">详情 →</a> · <a href="https://arxiv.org/abs/2608.07376" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
