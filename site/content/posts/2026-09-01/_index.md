---
title: "语音/音频论文速递 2026-09-01"
date: 2026-09-01T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 5 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #空间音频生成 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |
| #语音翻译 | 1篇 | `███` |
| #说话人日志 | 1篇 | `███` |
| #音频分类 | 1篇 | `███` |
| #音频指纹 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ouroboros-self-referential-backdoor-attacks-on-speech-enhanc-2608-30329/">Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出Ouroboros后门攻击框架，利用语音增强模型的理想干净输出作为自然触发器，无需外部注入即可在推理时激活后门。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="parallel-time-band-mixing-with-learned-observation-adding-fo-2608-30326/">Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出基于并行时间-频带混合器（PTBM）的语音增强前端，消除循环依赖，提升ASR鲁棒性，仅0.96M参数。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="towards-balanced-spectral-reconstruction-spectrally-adaptive-2608-30739/">Towards Balanced Spectral Reconstruction: Spectrally Adaptive Loss for Streaming Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出两种频谱加权STFT损失函数，改善流式语音增强中高频过度衰减，实现更均衡的频谱重建。</div>
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
<a class="card-title" href="neural-multichannel-distant-speaker-diarization-and-source-s-2608-28661/">Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
</div>
<div class="card-tldr">提出基于Beta先验的贝叶斯说话人日志模型，改进神经FCASA，在AMI数据集上DER和JER显著降低。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="physwave-physics-guided-latent-diffusion-models-for-controll-2608-29549/">PhysWave: Physics-Guided Latent Diffusion Models for Controllable Spatial Audio Generation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#空间音频生成</span>
</div>
<div class="card-tldr">PhysWave提出物理引导的潜在扩散模型，通过共享路点-字幕表示和声学先验实现可控文本到FOA空间音频生成。</div>
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
| 🥇 | [Ouroboros: Self-Referential Backdoor Attacks on Speech Enhan…](ouroboros-self-referential-backdoor-attacks-on-speech-enhanc-2608-30329/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Parallel Time-Band Mixing with Learned Observation-Adding fo…](parallel-time-band-mixing-with-learned-observation-adding-fo-2608-30326/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [PhysWave: Physics-Guided Latent Diffusion Models for Control…](physwave-physics-guided-latent-diffusion-models-for-controll-2608-29549/) 🎯 | **8.8** | #空间音频生成 |
| 4. | [WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs](wnw-waxing-and-waning-kv-cache-for-long-form-speech-llms-2608-22704/) | **8.2** | #语音识别 |
| 5. | [SimulS2ST-Omni: Data-Efficient Streaming Speech-to-Speech Tr…](simuls2st-omni-data-efficient-streaming-speech-to-speech-tra-2607-19810/) | **8.2** | #语音翻译 |
| 6. | [Neural Multichannel Distant Speaker Diarization and Source S…](neural-multichannel-distant-speaker-diarization-and-source-s-2608-28661/) 🎯 | **8.2** | #说话人日志 |
| 7. | [Towards Balanced Spectral Reconstruction: Spectrally Adaptiv…](towards-balanced-spectral-reconstruction-spectrally-adaptive-2608-30739/) 🎯 | **8.2** | #语音增强 |
| 8. | [SubT: Subspace Tuning for Few-shot Generalization of Audio-L…](subt-subspace-tuning-for-few-shot-generalization-of-audio-la-2606-18560/) | **7.8** | #音频分类 |
| 9. | [Variable-Length Audio Fingerprinting](variable-length-audio-fingerprinting-2603-23947/) | **7.8** | #音频指纹 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="ouroboros-self-referential-backdoor-attacks-on-speech-enhanc-2608-30329/">Ouroboros: Self-Referential Backdoor Attacks on Speech Enhancement via Clean Audio Triggers</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Ouroboros后门攻击框架，利用语音增强模型的理想干净输出作为自然触发器，无需外部注入即可在推理时激活后门。</div>
<div class="card-action">
<a href="ouroboros-self-referential-backdoor-attacks-on-speech-enhanc-2608-30329/">详情 →</a> · <a href="https://arxiv.org/abs/2608.30329" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="parallel-time-band-mixing-with-learned-observation-adding-fo-2608-30326/">Parallel Time-Band Mixing with Learned Observation-Adding for Robust ASR Front-Ends</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于并行时间-频带混合器（PTBM）的语音增强前端，消除循环依赖，提升ASR鲁棒性，仅0.96M参数。</div>
<div class="card-action">
<a href="parallel-time-band-mixing-with-learned-observation-adding-fo-2608-30326/">详情 →</a> · <a href="https://arxiv.org/abs/2608.30326" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="physwave-physics-guided-latent-diffusion-models-for-controll-2608-29549/">PhysWave: Physics-Guided Latent Diffusion Models for Controllable Spatial Audio Generation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#空间音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">PhysWave提出物理引导的潜在扩散模型，通过共享路点-字幕表示和声学先验实现可控文本到FOA空间音频生成。</div>
<div class="card-action">
<a href="physwave-physics-guided-latent-diffusion-models-for-controll-2608-29549/">详情 →</a> · <a href="https://arxiv.org/abs/2608.29549" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="wnw-waxing-and-waning-kv-cache-for-long-form-speech-llms-2608-22704/">WnW: Waxing-and-Waning KV Cache for Long-Form Speech LLMs</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出WnW方法，通过分类KV头为锚定、潮汐和固定角色，在长语音LLM中仅保留20%音频token在GPU上，保持接近全缓存的准确率。</div>
<div class="card-action">
<a href="wnw-waxing-and-waning-kv-cache-for-long-form-speech-llms-2608-22704/">详情 →</a> · <a href="https://arxiv.org/abs/2608.22704" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="simuls2st-omni-data-efficient-streaming-speech-to-speech-tra-2607-19810/">SimulS2ST-Omni: Data-Efficient Streaming Speech-to-Speech Translation via Explicit Trajectory Supervision</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种数据高效的流式语音到语音翻译训练方案，通过联合文本-代码轨迹监督和双流Thinker-Talker架构，在仅约2k小时配对数据下达到与闭源系统相当的翻译质量。</div>
<div class="card-action">
<a href="simuls2st-omni-data-efficient-streaming-speech-to-speech-tra-2607-19810/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19810" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="neural-multichannel-distant-speaker-diarization-and-source-s-2608-28661/">Neural Multichannel Distant Speaker Diarization and Source Separation with Beta Speaker Activity Prior</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于Beta先验的贝叶斯说话人日志模型，改进神经FCASA，在AMI数据集上DER和JER显著降低。</div>
<div class="card-action">
<a href="neural-multichannel-distant-speaker-diarization-and-source-s-2608-28661/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28661" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="towards-balanced-spectral-reconstruction-spectrally-adaptive-2608-30739/">Towards Balanced Spectral Reconstruction: Spectrally Adaptive Loss for Streaming Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出两种频谱加权STFT损失函数，改善流式语音增强中高频过度衰减，实现更均衡的频谱重建。</div>
<div class="card-action">
<a href="towards-balanced-spectral-reconstruction-spectrally-adaptive-2608-30739/">详情 →</a> · <a href="https://arxiv.org/abs/2608.30739" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="subt-subspace-tuning-for-few-shot-generalization-of-audio-la-2606-18560/">SubT: Subspace Tuning for Few-shot Generalization of Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频分类</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出子空间微调（SubT），通过几何感知共享变换和零样本原型锚定，缓解音频-语言模型少样本适应中的基类-新类权衡，无需文本编码器反向传播。</div>
<div class="card-action">
<a href="subt-subspace-tuning-for-few-shot-generalization-of-audio-la-2606-18560/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18560" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="variable-length-audio-fingerprinting-2603-23947/">Variable-Length Audio Fingerprinting</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频指纹</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个支持可变长度音频指纹的深度学习模型VLAFP，在实时音频识别和检索任务上超越现有SOTA。</div>
<div class="card-action">
<a href="variable-length-audio-fingerprinting-2603-23947/">详情 →</a> · <a href="https://arxiv.org/abs/2603.23947" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
