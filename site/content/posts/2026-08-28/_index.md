---
title: "语音/音频论文速递 2026-08-28"
date: 2026-08-28T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频理解 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #语音增强 | 1篇 | `█████` |
| #音频理解与生成 | 1篇 | `█████` |
| #语音代理训练 | 1篇 | `█████` |
| #无声语音识别 | 1篇 | `█████` |
| #语音评估 | 1篇 | `█████` |
| #语音事件检测 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="gan-based-joint-dereverberation-and-directional-filtering-2608-26403/">GAN-based Joint Dereverberation and Directional Filtering</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出联合去混响与方向性滤波的NDDF方法，用GAN实现，优于级联基线，并引入仅依赖输入输出信号的指向性模式估计方法。</div>
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
<a class="card-title" href="array-agnostic-ambisonics-encoding-via-diffusion-posterior-s-2608-24558/">Array-Agnostic Ambisonics Encoding via Diffusion Posterior Sampling</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出ADEPS，一种基于扩散后验采样的阵列无关Ambisonics编码框架，通过嵌入物理采集模型实现任意阵列拓扑的零样本编码。</div>
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
| 🥇 | [Array-Agnostic Ambisonics Encoding via Diffusion Posterior S…](array-agnostic-ambisonics-encoding-via-diffusion-posterior-s-2608-24558/) 🎯 | **9.2** | #双耳音频 |
| 🥈 | [GAN-based Joint Dereverberation and Directional Filtering](gan-based-joint-dereverberation-and-directional-filtering-2608-26403/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [FireRedAudio: A General-Purpose Audio Language Model with De…](fireredaudio-a-general-purpose-audio-language-model-with-dec-2608-24168/) | **8.5** | #音频理解与生成 |
| 4. | [SpeechGym: An Audio-Native Gym for Training Voice Agents via…](speechgym-an-audio-native-gym-for-training-voice-agents-via--2608-26432/) | **8.5** | #语音代理训练 |
| 5. | [EXAM$^2$: $\underline{Ex}tending$ $\underline{A}udio$ $Under…](exam-2-underline-ex-tending-underline-a-udio-understanding-i-2608-23758/) | **7.8** | #音频理解 |
| 6. | [Soft Active Electromyography Interface for Machine Learning-…](soft-active-electromyography-interface-for-machine-learning--2608-27048/) | **7.8** | #无声语音识别 |
| 7. | [Interpretable, Fairly Evaluated Automated L2 Speaking Assess…](interpretable-fairly-evaluated-automated-l2-speaking-assessm-2608-26137/) | **7.8** | #语音评估 |
| 8. | [From Sound to Symptom: Real-Time Respiratory Signal Understa…](from-sound-to-symptom-real-time-respiratory-signal-understan-2608-26163/) | **7.2** | #语音事件检测 |
| 9. | [Direct or Mediated? Task-Dependent Audio Information Routing…](direct-or-mediated-task-dependent-audio-information-routing--2608-27026/) | **7.2** | #音频理解 |
| 10. | [Decay-Region Group Delay as a Forensic Cue for AI-Generated …](decay-region-group-delay-as-a-forensic-cue-for-ai-generated--2608-26346/) | **6.8** | #音频取证 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="array-agnostic-ambisonics-encoding-via-diffusion-posterior-s-2608-24558/">Array-Agnostic Ambisonics Encoding via Diffusion Posterior Sampling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ADEPS，一种基于扩散后验采样的阵列无关Ambisonics编码框架，通过嵌入物理采集模型实现任意阵列拓扑的零样本编码。</div>
<div class="card-action">
<a href="array-agnostic-ambisonics-encoding-via-diffusion-posterior-s-2608-24558/">详情 →</a> · <a href="https://arxiv.org/abs/2608.24558" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="gan-based-joint-dereverberation-and-directional-filtering-2608-26403/">GAN-based Joint Dereverberation and Directional Filtering</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出联合去混响与方向性滤波的NDDF方法，用GAN实现，优于级联基线，并引入仅依赖输入输出信号的指向性模式估计方法。</div>
<div class="card-action">
<a href="gan-based-joint-dereverberation-and-directional-filtering-2608-26403/">详情 →</a> · <a href="https://arxiv.org/abs/2608.26403" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="fireredaudio-a-general-purpose-audio-language-model-with-dec-2608-24168/">FireRedAudio: A General-Purpose Audio Language Model with Decoupled Continuous Representations for Understanding and Generation</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频理解与生成</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">FireRedAudio 提出解耦连续表示，用共享 9B LLM 统一音频理解与生成，支持 ASR、长音频理解、零样本 TTS 和语音编辑。</div>
<div class="card-action">
<a href="fireredaudio-a-general-purpose-audio-language-model-with-dec-2608-24168/">详情 →</a> · <a href="https://arxiv.org/abs/2608.24168" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="speechgym-an-audio-native-gym-for-training-voice-agents-via--2608-26432/">SpeechGym: An Audio-Native Gym for Training Voice Agents via Reinforcement Learning</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音代理训练</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">SpeechGym 提出音频原生环境，通过过程奖励训练语音代理，使其在语音任务上性能翻倍并迁移至新基准。</div>
<div class="card-action">
<a href="speechgym-an-audio-native-gym-for-training-voice-agents-via--2608-26432/">详情 →</a> · <a href="https://arxiv.org/abs/2608.26432" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="exam-2-underline-ex-tending-underline-a-udio-understanding-i-2608-23758/">EXAM$^2$: $\underline{Ex}tending$ $\underline{A}udio$ $Understanding$ $in$ $\underline{M}ultilingual$ $and$ $\underline{M}ultimodal$ $Analysis$</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出EXAM^2基准，覆盖六种语言和多种音频模态，评估并微调LALMs，显著提升多语言和多模态音频理解性能。</div>
<div class="card-action">
<a href="exam-2-underline-ex-tending-underline-a-udio-understanding-i-2608-23758/">详情 →</a> · <a href="https://arxiv.org/abs/2608.23758" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="soft-active-electromyography-interface-for-machine-learning--2608-27048/">Soft Active Electromyography Interface for Machine Learning-Enabled Silent Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#无声语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种软性主动肌电接口，通过指尖电极采集唇部附近EMG信号，结合深度学习实现30词无声语音识别，准确率97.2%，并验证了无人机实时控制。</div>
<div class="card-action">
<a href="soft-active-electromyography-interface-for-machine-learning--2608-27048/">详情 →</a> · <a href="https://arxiv.org/abs/2608.27048" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="interpretable-fairly-evaluated-automated-l2-speaking-assessm-2608-26137/">Interpretable, Fairly Evaluated Automated L2 Speaking Assessment that Beats the Single-Human Ceiling and Why Pause Encoding Does Not Change LLM Fluency Scores</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出可解释的特征+LLM混合系统用于L2口语自动评估，在ICNALE基准上超越多数人工评分者，并证明停顿编码方式不影响LLM流利度评分。</div>
<div class="card-action">
<a href="interpretable-fairly-evaluated-automated-l2-speaking-assessm-2608-26137/">详情 →</a> · <a href="https://arxiv.org/abs/2608.26137" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="from-sound-to-symptom-real-time-respiratory-signal-understan-2608-26163/">From Sound to Symptom: Real-Time Respiratory Signal Understanding for Conversational Healthcare Agents</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音事件检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">HealthCUES利用多模态大模型实现对话场景中的实时咳嗽检测与分类，提供亚秒级延迟和对话感知门控，用于远程医疗。</div>
<div class="card-action">
<a href="from-sound-to-symptom-real-time-respiratory-signal-understan-2608-26163/">详情 →</a> · <a href="https://arxiv.org/abs/2608.26163" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="direct-or-mediated-task-dependent-audio-information-routing--2608-27026/">Direct or Mediated? Task-Dependent Audio Information Routing in Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文通过拼接两段音频，发现LALM在ASR上稳定但AQA性能大幅下降，并揭示任务依赖的音频信息路由机制。</div>
<div class="card-action">
<a href="direct-or-mediated-task-dependent-audio-information-routing--2608-27026/">详情 →</a> · <a href="https://arxiv.org/abs/2608.27026" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="decay-region-group-delay-as-a-forensic-cue-for-ai-generated--2608-26346/">Decay-Region Group Delay as a Forensic Cue for AI-Generated Impulsive Sounds</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频取证</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文发现AI生成的脉冲声音在衰减区域的群延迟分布与真实声音存在可测量差异，可作为取证线索，但跨生成器泛化性有限。</div>
<div class="card-action">
<a href="decay-region-group-delay-as-a-forensic-cue-for-ai-generated--2608-26346/">详情 →</a> · <a href="https://arxiv.org/abs/2608.26346" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
