---
title: "语音/音频论文速递 2026-10-08"
date: 2026-10-08T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 6 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">6</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #声学模拟 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="childvox-a-speech-audio-and-large-audio-language-model-bench-2605-29257/">ChildVox: A Speech, Audio, and Large Audio-Language Model Benchmark in Understanding and Characterizing Sound across Childhood</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音识别</span>
</div>
<div class="card-tldr">ChildVox 整合 17 个儿童音频数据集、20+ 子任务，系统评测自监督、ASR 与大音频语言模型在儿童声学信号理解上的表现。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="lift-se-linguistic-inference-followed-by-flow-transformation-2610-09963/">LIFT-SE: Linguistic Inference Followed by Flow Transformation for Generative Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">LIFT-SE 用两阶段生成框架，先自回归预测干净 codec token，再用条件流匹配细化连续 latent，缓解强噪声混响下的语言幻觉。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="direction-preserving-spatial-audio-signal-enhancement-in-the-2610-09701/">Direction-preserving Spatial Audio Signal Enhancement in The Spherical Harmonic Domain</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在球谐域提出方向保持的多输出波束成形空间音频增强算法，在保留目标声场的同时保留残余干扰的空间线索。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sea-lm-egocentric-spatial-audio-understanding-for-wearable-m-2610-05610/">SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出 SEA-LM，用 FOACODER 编码智能眼镜阵列的一阶 Ambisonics，训练 MLLM 完成定位与空间选择性转录。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="vm-arraydps-virtual-microphone-augmented-diffusion-posterior-2610-09334/">VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterior Sampling for Unsupervised Blind Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">用虚拟麦克风增强扩散后验采样，为无监督盲源分离提供额外多通道一致性约束，2/3说话人任务均优于ArrayDPS。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-study-on-improving-multi-class-audio-source-separation-via-2610-10025/">A Study on Improving Multi-class Audio Source Separation Via Decoupled CLAP Query Optimization and an Automated Data Engine</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出自动化数据引擎清洗训练数据，并用两阶段优化类特定 CLAP 控制信号，提升多类音频源分离性能。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sea-lm-egocentric-spatial-audio-understanding-for-wearable-m-2610-05610/">SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出 SEA-LM，用 FOACODER 编码智能眼镜阵列的一阶 Ambisonics，训练 MLLM 完成定位与空间选择性转录。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="direction-preserving-spatial-audio-signal-enhancement-in-the-2610-09701/">Direction-preserving Spatial Audio Signal Enhancement in The Spherical Harmonic Domain</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在球谐域提出方向保持的多输出波束成形空间音频增强算法，在保留目标声场的同时保留残余干扰的空间线索。</div>
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
| 🥇 | [SEA-LM: Egocentric Spatial Audio Understanding for Wearable …](sea-lm-egocentric-spatial-audio-understanding-for-wearable-m-2610-05610/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterio…](vm-arraydps-virtual-microphone-augmented-diffusion-posterior-2610-09334/) 🎯 | **8.2** | #语音分离 |
| 🥉 | [ChildVox: A Speech, Audio, and Large Audio-Language Model Be…](childvox-a-speech-audio-and-large-audio-language-model-bench-2605-29257/) 🎯 | **8.0** | #语音识别 |
| 4. | [LIFT-SE: Linguistic Inference Followed by Flow Transformatio…](lift-se-linguistic-inference-followed-by-flow-transformation-2610-09963/) 🎯 | **8.0** | #语音增强 |
| 5. | [A Study on Improving Multi-class Audio Source Separation Via…](a-study-on-improving-multi-class-audio-source-separation-via-2610-10025/) 🎯 | **7.8** | #语音分离 |
| 6. | [Direction-preserving Spatial Audio Signal Enhancement in The…](direction-preserving-spatial-audio-signal-enhancement-in-the-2610-09701/) 🎯 | **7.8** | #语音增强 |
| 7. | [ImpactMat: Continuous Material Estimation for Inverse Impact…](impactmat-continuous-material-estimation-for-inverse-impact--2610-07061/) | **7.0** | #声学模拟 |
| 8. | [Do Language Models Need Music Supervision? Verifiable Reward…](do-language-models-need-music-supervision-verifiable-rewards-2609-23665/) | **7.0** | #音乐生成 |
| 9. | [Post-Training Zero-Shot TTS for Fine-Grained Emotion and Dur…](post-training-zero-shot-tts-for-fine-grained-emotion-and-dur-2609-11523/) | **6.8** | #语音合成 |
| 10. | [Unheard but Recognizable: Ultrasonic Signatures for Musical …](unheard-but-recognizable-ultrasonic-signatures-for-musical-i-2610-08850/) | **6.8** | #音乐信息检索 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="sea-lm-egocentric-spatial-audio-understanding-for-wearable-m-2610-05610/">SEA-LM: Egocentric Spatial Audio Understanding for Wearable Microphone Arrays</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 SEA-LM，用 FOACODER 编码智能眼镜阵列的一阶 Ambisonics，训练 MLLM 完成定位与空间选择性转录。</div>
<div class="card-action">
<a href="sea-lm-egocentric-spatial-audio-understanding-for-wearable-m-2610-05610/">详情 →</a> · <a href="https://arxiv.org/abs/2610.05610" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="vm-arraydps-virtual-microphone-augmented-diffusion-posterior-2610-09334/">VM-ARRAYDPS: Virtual Microphone Augmented Diffusion Posterior Sampling for Unsupervised Blind Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用虚拟麦克风增强扩散后验采样，为无监督盲源分离提供额外多通道一致性约束，2/3说话人任务均优于ArrayDPS。</div>
<div class="card-action">
<a href="vm-arraydps-virtual-microphone-augmented-diffusion-posterior-2610-09334/">详情 →</a> · <a href="https://arxiv.org/abs/2610.09334" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="childvox-a-speech-audio-and-large-audio-language-model-bench-2605-29257/">ChildVox: A Speech, Audio, and Large Audio-Language Model Benchmark in Understanding and Characterizing Sound across Childhood</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">ChildVox 整合 17 个儿童音频数据集、20+ 子任务，系统评测自监督、ASR 与大音频语言模型在儿童声学信号理解上的表现。</div>
<div class="card-action">
<a href="childvox-a-speech-audio-and-large-audio-language-model-bench-2605-29257/">详情 →</a> · <a href="https://arxiv.org/abs/2605.29257" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="lift-se-linguistic-inference-followed-by-flow-transformation-2610-09963/">LIFT-SE: Linguistic Inference Followed by Flow Transformation for Generative Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">LIFT-SE 用两阶段生成框架，先自回归预测干净 codec token，再用条件流匹配细化连续 latent，缓解强噪声混响下的语言幻觉。</div>
<div class="card-action">
<a href="lift-se-linguistic-inference-followed-by-flow-transformation-2610-09963/">详情 →</a> · <a href="https://arxiv.org/abs/2610.09963" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="a-study-on-improving-multi-class-audio-source-separation-via-2610-10025/">A Study on Improving Multi-class Audio Source Separation Via Decoupled CLAP Query Optimization and an Automated Data Engine</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出自动化数据引擎清洗训练数据，并用两阶段优化类特定 CLAP 控制信号，提升多类音频源分离性能。</div>
<div class="card-action">
<a href="a-study-on-improving-multi-class-audio-source-separation-via-2610-10025/">详情 →</a> · <a href="https://arxiv.org/abs/2610.10025" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="direction-preserving-spatial-audio-signal-enhancement-in-the-2610-09701/">Direction-preserving Spatial Audio Signal Enhancement in The Spherical Harmonic Domain</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在球谐域提出方向保持的多输出波束成形空间音频增强算法，在保留目标声场的同时保留残余干扰的空间线索。</div>
<div class="card-action">
<a href="direction-preserving-spatial-audio-signal-enhancement-in-the-2610-09701/">详情 →</a> · <a href="https://arxiv.org/abs/2610.09701" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="impactmat-continuous-material-estimation-for-inverse-impact--2610-07061/">ImpactMat: Continuous Material Estimation for Inverse Impact Sound Rendering</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出逆冲击声渲染任务，构建 ImpactMat 单/混合材料冲击声数据集与基准，用前馈模型从录音预测材料参数以重渲染。</div>
<div class="card-action">
<a href="impactmat-continuous-material-estimation-for-inverse-impact--2610-07061/">详情 →</a> · <a href="https://arxiv.org/abs/2610.07061" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="do-language-models-need-music-supervision-verifiable-rewards-2609-23665/">Do Language Models Need Music Supervision? Verifiable Rewards for Multi-Constraint Symbolic Music Generation</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用可验证约束奖励做GRPO训练语言模型生成符号音乐，无需人工标注或奖励模型，四小时内大幅提升多约束满足率。</div>
<div class="card-action">
<a href="do-language-models-need-music-supervision-verifiable-rewards-2609-23665/">详情 →</a> · <a href="https://arxiv.org/abs/2609.23665" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="post-training-zero-shot-tts-for-fine-grained-emotion-and-dur-2609-11523/">Post-Training Zero-Shot TTS for Fine-Grained Emotion and Duration Control via Natural Language</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用后训练框架（SFT+GRPO）为预训练TTS模型加自然语言细粒度情感与时长控制，无需额外推理模块。</div>
<div class="card-action">
<a href="post-training-zero-shot-tts-for-fine-grained-emotion-and-dur-2609-11523/">详情 →</a> · <a href="https://arxiv.org/abs/2609.11523" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="unheard-but-recognizable-ultrasonic-signatures-for-musical-i-2610-08850/">Unheard but Recognizable: Ultrasonic Signatures for Musical Instrument Recognition</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">利用96kSPS录音中的超声频段成分，验证其对单音与复音乐器识别的增益。</div>
<div class="card-action">
<a href="unheard-but-recognizable-ultrasonic-signatures-for-musical-i-2610-08850/">详情 →</a> · <a href="https://arxiv.org/abs/2610.08850" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
