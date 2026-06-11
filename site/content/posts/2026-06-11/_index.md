---
title: "语音/音频论文速递 2026-06-11"
date: 2026-06-11T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 1篇 | `██████████` |
| #语音增强 | 1篇 | `██████████` |
| #语音识别 | 1篇 | `██████████` |
| #文本到语音合成 | 1篇 | `██████████` |
| #语音安全 | 1篇 | `██████████` |
| #空间音频评估 | 1篇 | `██████████` |
| #声学场景分类 | 1篇 | `██████████` |
| #语音翻译 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="halo-half-frame-rate-adaptive-learnable-operator-for-lightwe-2606-12328/">HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出HALO模块，通过减半内部帧率降低STFT语音增强模型的计算冗余，在轻量级模型上实现性能提升。</div>
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
<a class="card-title" href="inside-the-latent-flow-causal-deciphering-of-attention-dynam-2606-10046/">Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">通过因果干预探针揭示音频分离基础模型SAM Audio的双路径文本条件注意力机制，并提出训练无关的层选注意力缓存加速方法。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sensitivity-analysis-of-generative-spatial-audio-metrics-a-s-2606-11581/">Sensitivity Analysis of Generative Spatial Audio Metrics: A Study on Responsiveness, Smoothness, and Symmetry</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#空间音频评估</span>
</div>
<div class="card-tldr">提出分析框架，评估生成式空间音频指标对空间参数变化的敏感性，定义响应性、平滑性和对称性三个期望属性。</div>
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
| 🥇 | [Inside the Latent Flow: Causal Deciphering of Attention Dyna…](inside-the-latent-flow-causal-deciphering-of-attention-dynam-2606-10046/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightw…](halo-half-frame-rate-adaptive-learnable-operator-for-lightwe-2606-12328/) 🎯 | **8.5** | #语音增强 |
| 🥉 | [ViP-VL: Vietnamese Self-supervised Speech Pretraining Model …](vip-vl-vietnamese-self-supervised-speech-pretraining-model-w-2606-10360/) | **8.2** | #语音识别 |
| 4. | [UR-BERT: Scaling Text Encoders for Massively Multilingual TT…](ur-bert-scaling-text-encoders-for-massively-multilingual-tts-2606-11681/) | **8.2** | #文本到语音合成 |
| 5. | [Where Do Backdoors Live? A Component-Level Analysis of Backd…](where-do-backdoors-live-a-component-level-analysis-of-backdo-2510-01157/) | **7.8** | #语音安全 |
| 6. | [Sensitivity Analysis of Generative Spatial Audio Metrics: A …](sensitivity-analysis-of-generative-spatial-audio-metrics-a-s-2606-11581/) 🎯 | **7.5** | #空间音频评估 |
| 7. | [Towards Event-Robust Acoustic Scene Classification](towards-event-robust-acoustic-scene-classification-2606-06921/) | **7.2** | #声学场景分类 |
| 8. | [NaijaS2ST: A Multi-Accent Benchmark for Speech-to-Speech Tra…](naijas2st-a-multi-accent-benchmark-for-speech-to-speech-tran-2604-16287/) | **7.2** | #语音翻译 |
| 9. | [A Sensitivity Analysis of Multi-Event Audio Grounding in Aud…](a-sensitivity-analysis-of-multi-event-audio-grounding-in-aud-2603-03855/) | **6.5** | #音频理解 |
| 10. | [I Understand How You Feel: Enhancing Deeper Emotional Suppor…](i-understand-how-you-feel-enhancing-deeper-emotional-support-2606-11875/) | **6.5** | #情感验证 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="inside-the-latent-flow-causal-deciphering-of-attention-dynam-2606-10046/">Inside the Latent Flow: Causal Deciphering of Attention Dynamics in Audio Separation Foundation Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过因果干预探针揭示音频分离基础模型SAM Audio的双路径文本条件注意力机制，并提出训练无关的层选注意力缓存加速方法。</div>
<div class="card-action">
<a href="inside-the-latent-flow-causal-deciphering-of-attention-dynam-2606-10046/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10046" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="halo-half-frame-rate-adaptive-learnable-operator-for-lightwe-2606-12328/">HALO: Half-Frame-Rate Adaptive Learnable Operator for Lightweight STFT-Based Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出HALO模块，通过减半内部帧率降低STFT语音增强模型的计算冗余，在轻量级模型上实现性能提升。</div>
<div class="card-action">
<a href="halo-half-frame-rate-adaptive-learnable-operator-for-lightwe-2606-12328/">详情 →</a> · <a href="https://arxiv.org/abs/2606.12328" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="vip-vl-vietnamese-self-supervised-speech-pretraining-model-w-2606-10360/">ViP-VL: Vietnamese Self-supervised Speech Pretraining Model with Vector-Quantization Learning</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ViP-VL，一种基于向量量化的越南语自监督语音预训练模型，在17000小时数据上预训练，刷新四项下游任务SOTA。</div>
<div class="card-action">
<a href="vip-vl-vietnamese-self-supervised-speech-pretraining-model-w-2606-10360/">详情 →</a> · <a href="https://arxiv.org/abs/2606.10360" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="ur-bert-scaling-text-encoders-for-massively-multilingual-tts-2606-11681/">UR-BERT: Scaling Text Encoders for Massively Multilingual TTS Through Universal Romanization and Speech Token Prediction</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#文本到语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出UR-BERT，通过通用罗马化表示和语音token预测目标，将TTS文本编码器扩展到495种语言。</div>
<div class="card-action">
<a href="ur-bert-scaling-text-encoders-for-massively-multilingual-tts-2606-11681/">详情 →</a> · <a href="https://arxiv.org/abs/2606.11681" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="where-do-backdoors-live-a-component-level-analysis-of-backdo-2510-01157/">Where Do Backdoors Live? A Component-Level Analysis of Backdoor Propagation in Speech Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音安全</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统分析后门攻击在语音语言模型各组件间的传播机制，发现后门持久性高度依赖目标组件，且中毒样本在共享嵌入中不可分离。</div>
<div class="card-action">
<a href="where-do-backdoors-live-a-component-level-analysis-of-backdo-2510-01157/">详情 →</a> · <a href="https://arxiv.org/abs/2510.01157" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="sensitivity-analysis-of-generative-spatial-audio-metrics-a-s-2606-11581/">Sensitivity Analysis of Generative Spatial Audio Metrics: A Study on Responsiveness, Smoothness, and Symmetry</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#空间音频评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出分析框架，评估生成式空间音频指标对空间参数变化的敏感性，定义响应性、平滑性和对称性三个期望属性。</div>
<div class="card-action">
<a href="sensitivity-analysis-of-generative-spatial-audio-metrics-a-s-2606-11581/">详情 →</a> · <a href="https://arxiv.org/abs/2606.11581" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="towards-event-robust-acoustic-scene-classification-2606-06921/">Towards Event-Robust Acoustic Scene Classification</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声学场景分类</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出事件迁移声学场景（ESAS）数据集，用于评估声学场景分类系统对未知声音事件的鲁棒性。</div>
<div class="card-action">
<a href="towards-event-robust-acoustic-scene-classification-2606-06921/">详情 →</a> · <a href="https://arxiv.org/abs/2606.06921" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="naijas2st-a-multi-accent-benchmark-for-speech-to-speech-tran-2604-16287/">NaijaS2ST: A Multi-Accent Benchmark for Speech-to-Speech Translation in Low-Resource Nigerian Languages</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">NaijaS2ST是一个面向尼日利亚四种低资源语言的语音翻译基准数据集，包含约50小时/语言的平行语音数据，并评估了级联、端到端和AudioLLM方法。</div>
<div class="card-action">
<a href="naijas2st-a-multi-accent-benchmark-for-speech-to-speech-tran-2604-16287/">详情 →</a> · <a href="https://arxiv.org/abs/2604.16287" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-sensitivity-analysis-of-multi-event-audio-grounding-in-aud-2603-03855/">A Sensitivity Analysis of Multi-Event Audio Grounding in Audio LLMs</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统评估音频LLM在多事件场景下的事件定位与幻觉行为，发现事件数增加导致TPR下降、FPR上升，提示存在权衡。</div>
<div class="card-action">
<a href="a-sensitivity-analysis-of-multi-event-audio-grounding-in-aud-2603-03855/">详情 →</a> · <a href="https://arxiv.org/abs/2603.03855" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="i-understand-how-you-feel-enhancing-deeper-emotional-support-2606-11875/">I Understand How You Feel: Enhancing Deeper Emotional Support Through Multilingual Emotional Validation in Dialogue System</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#情感验证</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出多语言情感验证对话系统，包含语料库、时序检测模型MEGUMI和基准测试。</div>
<div class="card-action">
<a href="i-understand-how-you-feel-enhancing-deeper-emotional-support-2606-11875/">详情 →</a> · <a href="https://arxiv.org/abs/2606.11875" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
