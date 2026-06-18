---
title: "语音/音频论文速递 2026-06-18"
date: 2026-06-18T09:00:00+08:00
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
| #双耳音频 | 1篇 | `███` |
| #视频理解 | 1篇 | `███` |
| #说话人确认 | 1篇 | `███` |
| #环境声音深度伪造检测 | 1篇 | `███` |
| #句子嵌入分析 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |
| #音频感知 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="qc-gan-a-parameter-efficient-quaternion-conformer-gan-for-hi-2606-18611/">QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出QC-GAN，用四元数Conformer生成器结合MetricGAN训练，以0.89M参数在VoiceBank+DEMAND上达到PESQ 3.48，性能媲美SOTA但参数量减半。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="diffvqe-hybrid-diffusion-voice-quality-enhancement-under-aco-2605-08189/">DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">首个可复现的基于扩散的声学回声与噪声联合抑制模型，在性能与复杂度上超越判别式SOTA DeepVQE。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="stupase-towards-low-hallucination-studio-quality-generative--2603-09234/">StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">StuPASE在PASE基础上引入流匹配模块和干目标微调，实现低幻觉的录音室级语音增强。</div>
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
<a class="card-title" href="generalised-transcoding-framework-for-arbitrary-spatial-audi-2606-18480/">Generalised Transcoding Framework for Arbitrary Spatial Audio Capture and Playback Formats</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出统一框架，将Ambisonic或麦克风阵列信号参数化转码为任意目标播放格式，支持旋转，经听感测试验证优于现有方法。</div>
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
| 🥇 | [QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for H…](qc-gan-a-parameter-efficient-quaternion-conformer-gan-for-hi-2606-18611/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Ac…](diffvqe-hybrid-diffusion-voice-quality-enhancement-under-aco-2605-08189/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [StuPASE: Towards Low-Hallucination Studio-Quality Generative…](stupase-towards-low-hallucination-studio-quality-generative--2603-09234/) 🎯 | **9.2** | #语音增强 |
| 4. | [Generalised Transcoding Framework for Arbitrary Spatial Audi…](generalised-transcoding-framework-for-arbitrary-spatial-audi-2606-18480/) 🎯 | **8.8** | #双耳音频 |
| 5. | [Native Active Perception as Reasoning for Omni-Modal Underst…](native-active-perception-as-reasoning-for-omni-modal-underst-2606-19341/) | **8.5** | #视频理解 |
| 6. | [Speaker Verification with Speech-Aware LLMs: Evaluation and …](speaker-verification-with-speech-aware-llms-evaluation-and-a-2603-10827/) | **7.8** | #说话人确认 |
| 7. | [The First Environmental Sound Deepfake Detection Challenge: …](the-first-environmental-sound-deepfake-detection-challenge-b-2603-04865/) | **7.5** | #环境声音深度伪造检测 |
| 8. | [FLiP: Towards understanding and interpreting multimodal mult…](flip-towards-understanding-and-interpreting-multimodal-multi-2604-18109/) | **7.2** | #句子嵌入分析 |
| 9. | [Adaptive Speech-to-Spike Encoding for Spiking Neural Network…](adaptive-speech-to-spike-encoding-for-spiking-neural-network-2606-19039/) | **7.2** | #语音识别 |
| 10. | [EMORSION: Examining the Impact of Audio Parameters on Emotio…](emorsion-examining-the-impact-of-audio-parameters-on-emotion-2606-18266/) | **5.5** | #音频感知 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="qc-gan-a-parameter-efficient-quaternion-conformer-gan-for-hi-2606-18611/">QC-GAN: A Parameter-Efficient Quaternion Conformer GAN for High-Fidelity Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出QC-GAN，用四元数Conformer生成器结合MetricGAN训练，以0.89M参数在VoiceBank+DEMAND上达到PESQ 3.48，性能媲美SOTA但参数量减半。</div>
<div class="card-action">
<a href="qc-gan-a-parameter-efficient-quaternion-conformer-gan-for-hi-2606-18611/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18611" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="diffvqe-hybrid-diffusion-voice-quality-enhancement-under-aco-2605-08189/">DiffVQE: Hybrid Diffusion Voice Quality Enhancement Under Acoustic Echo and Noise</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首个可复现的基于扩散的声学回声与噪声联合抑制模型，在性能与复杂度上超越判别式SOTA DeepVQE。</div>
<div class="card-action">
<a href="diffvqe-hybrid-diffusion-voice-quality-enhancement-under-aco-2605-08189/">详情 →</a> · <a href="https://arxiv.org/abs/2605.08189" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="stupase-towards-low-hallucination-studio-quality-generative--2603-09234/">StuPASE: Towards Low-Hallucination Studio-Quality Generative Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">StuPASE在PASE基础上引入流匹配模块和干目标微调，实现低幻觉的录音室级语音增强。</div>
<div class="card-action">
<a href="stupase-towards-low-hallucination-studio-quality-generative--2603-09234/">详情 →</a> · <a href="https://arxiv.org/abs/2603.09234" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="generalised-transcoding-framework-for-arbitrary-spatial-audi-2606-18480/">Generalised Transcoding Framework for Arbitrary Spatial Audio Capture and Playback Formats</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一框架，将Ambisonic或麦克风阵列信号参数化转码为任意目标播放格式，支持旋转，经听感测试验证优于现有方法。</div>
<div class="card-action">
<a href="generalised-transcoding-framework-for-arbitrary-spatial-audi-2606-18480/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18480" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="native-active-perception-as-reasoning-for-omni-modal-underst-2606-19341/">Native Active Perception as Reasoning for Omni-Modal Understanding</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#视频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出OmniAgent，首个原生全模态智能体，将视频理解建模为POMDP迭代观测-思考-行动循环，实现推理复杂度与视频时长解耦。</div>
<div class="card-action">
<a href="native-active-perception-as-reasoning-for-omni-modal-underst-2606-19341/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19341" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="speaker-verification-with-speech-aware-llms-evaluation-and-a-2603-10827/">Speaker Verification with Speech-Aware LLMs: Evaluation and Augmentation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#说话人确认</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种协议评估语音感知LLM的说话人区分能力，并通过注入ECAPA-TDNN嵌入和LoRA微调实现接近专用系统的说话人确认性能。</div>
<div class="card-action">
<a href="speaker-verification-with-speech-aware-llms-evaluation-and-a-2603-10827/">详情 →</a> · <a href="https://arxiv.org/abs/2603.10827" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="the-first-environmental-sound-deepfake-detection-challenge-b-2603-04865/">The First Environmental Sound Deepfake Detection Challenge: Benchmarking Robustness, Evaluation, and Insights</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#环境声音深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首次举办环境声音深度伪造检测挑战赛，构建数据集、评估协议和基线系统，总结参赛方案和未来方向。</div>
<div class="card-action">
<a href="the-first-environmental-sound-deepfake-detection-challenge-b-2603-04865/">详情 →</a> · <a href="https://arxiv.org/abs/2603.04865" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="flip-towards-understanding-and-interpreting-multimodal-multi-2604-18109/">FLiP: Towards understanding and interpreting multimodal multilingual sentence embeddings</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#句子嵌入分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出因子化线性投影（FLiP）模型，从句子嵌入中恢复词汇内容，揭示多模态多语言编码器的模态和语言偏差。</div>
<div class="card-action">
<a href="flip-towards-understanding-and-interpreting-multimodal-multi-2604-18109/">详情 →</a> · <a href="https://arxiv.org/abs/2604.18109" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="adaptive-speech-to-spike-encoding-for-spiking-neural-network-2606-19039/">Adaptive Speech-to-Spike Encoding for Spiking Neural Networks</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种可学习的残差语音到脉冲编码器，与R-LIF骨干网络联合训练，在GSC-v2上以35k参数达到89.8%准确率，并对比了DFA与BPTT的性能权衡。</div>
<div class="card-action">
<a href="adaptive-speech-to-spike-encoding-for-spiking-neural-network-2606-19039/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19039" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="emorsion-examining-the-impact-of-audio-parameters-on-emotion-2606-18266/">EMORSION: Examining the Impact of Audio Parameters on Emotional Responses and Immersion in Film</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频感知</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">探索性研究电影音频参数（频率、动态、空间）对观众情绪和沉浸感的影响，通过问卷、生理信号和运动追踪多模态评估。</div>
<div class="card-action">
<a href="emorsion-examining-the-impact-of-audio-parameters-on-emotion-2606-18266/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18266" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
