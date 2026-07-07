---
title: "语音/音频论文速递 2026-07-07"
date: 2026-07-07T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 8 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">8</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #目标说话人提取 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |
| #暴力检测 | 1篇 | `█████` |
| #语音编解码 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="measuring-the-robustness-of-audio-deepfake-detection-under-r-2503-17577/">Measuring the Robustness of Audio Deepfake Detection under Real-World Corruption</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频深度伪造检测</span>
</div>
<div class="card-tldr">系统评估10种音频深度伪造检测模型在18种真实世界失真下的鲁棒性，发现模型对噪声鲁棒但对音频修改和压缩脆弱，语音基础模型表现更优。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="weakly-guided-and-autoregressive-beamformer-parameterization-2607-04471/">Weakly Guided and Autoregressive Beamformer Parameterization for Generalizable Moving Speaker Extraction in Higher-Order Ambisonics</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出一种弱引导自回归波束成形参数化方法，仅需目标初始方向，在高阶Ambisonics中实现可泛化的移动说话人提取。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="noisy-environment-adaptation-of-neural-speech-codec-via-foca-2607-04195/">Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出FocalSE方法，在神经语音编解码器的连续嵌入空间中进行特征去噪、噪声分离和噪声识别，提升低比特率低信噪比下的语音重建质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="duplexchat-constructing-speaker-separated-full-duplex-dialog-2607-04941/">DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出DuplexChat语料库及构建流水线，从播客生成双通道全双工对话语音，用于口语对话语言模型训练。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ranking-the-impact-of-contextual-specialization-in-neural-sp-2607-04826/">Ranking the Impact of Contextual Specialization in Neural Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">系统研究语音增强模型根据上下文信息（说话人、噪声、语言等）进行特化训练的效果，发现说话人特化收益最大，小模型可匹敌十倍大通用模型。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="assessing-the-impact-of-noise-and-speech-enhancement-on-the--2605-03776/">Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音编解码</span>
</div>
<div class="card-tldr">评估经典与神经语音编解码器在噪声条件下的可懂度，并探究编码前语音增强的影响。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="startse-towards-streaming-target-speaker-extraction-via-chun-2604-19635/">StarTSE: Towards Streaming Target Speaker Extraction via Chunk-wise Interleaved Splicing of Autoregressive Language Model</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出首个面向流式目标说话人提取的自回归模型，通过分块交错拼接范式实现稳定高效的低延迟推理。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="weakly-guided-and-autoregressive-beamformer-parameterization-2607-04471/">Weakly Guided and Autoregressive Beamformer Parameterization for Generalizable Moving Speaker Extraction in Higher-Order Ambisonics</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出一种弱引导自回归波束成形参数化方法，仅需目标初始方向，在高阶Ambisonics中实现可泛化的移动说话人提取。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="startse-towards-streaming-target-speaker-extraction-via-chun-2604-19635/">StarTSE: Towards Streaming Target Speaker Extraction via Chunk-wise Interleaved Splicing of Autoregressive Language Model</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出首个面向流式目标说话人提取的自回归模型，通过分块交错拼接范式实现稳定高效的低延迟推理。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="duplexchat-constructing-speaker-separated-full-duplex-dialog-2607-04941/">DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出DuplexChat语料库及构建流水线，从播客生成双通道全双工对话语音，用于口语对话语言模型训练。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mixture-constrained-max-pooling-improves-separation-based-bi-2607-03221/">Mixture-Constrained Max Pooling Improves Separation-Based Bird Species Classification</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#生物声学</span>
</div>
<div class="card-tldr">提出混合约束最大池化（MCM）方法，利用分离后各通道与原始混合物的物种概率联合决策，提升基于分离的鸟类物种分类性能。</div>
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
| 🥇 | [StarTSE: Towards Streaming Target Speaker Extraction via Chu…](startse-towards-streaming-target-speaker-extraction-via-chun-2604-19635/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [Measuring the Robustness of Audio Deepfake Detection under R…](measuring-the-robustness-of-audio-deepfake-detection-under-r-2503-17577/) 🎯 | **8.8** | #音频深度伪造检测 |
| 🥉 | [Weakly Guided and Autoregressive Beamformer Parameterization…](weakly-guided-and-autoregressive-beamformer-parameterization-2607-04471/) 🎯 | **8.8** | #目标说话人提取 |
| 4. | [Noisy Environment Adaptation of Neural Speech Codec via Foca…](noisy-environment-adaptation-of-neural-speech-codec-via-foca-2607-04195/) 🎯 | **8.8** | #语音增强 |
| 5. | [AudioX-Turbo: A Unified Framework for Efficient Anything-to-…](audiox-turbo-a-unified-framework-for-efficient-anything-to-a-2606-12555/) | **8.5** | #音频生成 |
| 6. | [DuplexChat: Constructing Speaker-Separated Full-Duplex Dialo…](duplexchat-constructing-speaker-separated-full-duplex-dialog-2607-04941/) 🎯 | **8.5** | #语音分离 |
| 7. | [Ranking the Impact of Contextual Specialization in Neural Sp…](ranking-the-impact-of-contextual-specialization-in-neural-sp-2607-04826/) 🎯 | **8.2** | #语音增强 |
| 8. | [Mixture-Constrained Max Pooling Improves Separation-Based Bi…](mixture-constrained-max-pooling-improves-separation-based-bi-2607-03221/) 🎯 | **8.2** | #生物声学 |
| 9. | [AViS-Mamba: Adaptive Visual Steering of Audio State-Space Dy…](avis-mamba-adaptive-visual-steering-of-audio-state-space-dyn-2604-03329/) | **7.8** | #暴力检测 |
| 10. | [Assessing the Impact of Noise and Speech Enhancement on the …](assessing-the-impact-of-noise-and-speech-enhancement-on-the--2605-03776/) 🎯 | **7.5** | #语音编解码 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="startse-towards-streaming-target-speaker-extraction-via-chun-2604-19635/">StarTSE: Towards Streaming Target Speaker Extraction via Chunk-wise Interleaved Splicing of Autoregressive Language Model</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个面向流式目标说话人提取的自回归模型，通过分块交错拼接范式实现稳定高效的低延迟推理。</div>
<div class="card-action">
<a href="startse-towards-streaming-target-speaker-extraction-via-chun-2604-19635/">详情 →</a> · <a href="https://arxiv.org/abs/2604.19635" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="measuring-the-robustness-of-audio-deepfake-detection-under-r-2503-17577/">Measuring the Robustness of Audio Deepfake Detection under Real-World Corruption</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统评估10种音频深度伪造检测模型在18种真实世界失真下的鲁棒性，发现模型对噪声鲁棒但对音频修改和压缩脆弱，语音基础模型表现更优。</div>
<div class="card-action">
<a href="measuring-the-robustness-of-audio-deepfake-detection-under-r-2503-17577/">详情 →</a> · <a href="https://arxiv.org/abs/2503.17577" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="weakly-guided-and-autoregressive-beamformer-parameterization-2607-04471/">Weakly Guided and Autoregressive Beamformer Parameterization for Generalizable Moving Speaker Extraction in Higher-Order Ambisonics</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种弱引导自回归波束成形参数化方法，仅需目标初始方向，在高阶Ambisonics中实现可泛化的移动说话人提取。</div>
<div class="card-action">
<a href="weakly-guided-and-autoregressive-beamformer-parameterization-2607-04471/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04471" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="noisy-environment-adaptation-of-neural-speech-codec-via-foca-2607-04195/">Noisy Environment Adaptation of Neural Speech Codec via Focal Mask and Noise Feature Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FocalSE方法，在神经语音编解码器的连续嵌入空间中进行特征去噪、噪声分离和噪声识别，提升低比特率低信噪比下的语音重建质量。</div>
<div class="card-action">
<a href="noisy-environment-adaptation-of-neural-speech-codec-via-foca-2607-04195/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04195" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="audiox-turbo-a-unified-framework-for-efficient-anything-to-a-2606-12555/">AudioX-Turbo: A Unified Framework for Efficient Anything-to-Audio Generation</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一高效的多模态到音频生成框架AudioX-Turbo，通过教师-学生蒸馏实现4步采样，性能优于多步基线。</div>
<div class="card-action">
<a href="audiox-turbo-a-unified-framework-for-efficient-anything-to-a-2606-12555/">详情 →</a> · <a href="https://arxiv.org/abs/2606.12555" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="duplexchat-constructing-speaker-separated-full-duplex-dialog-2607-04941/">DuplexChat: Constructing Speaker-Separated Full-Duplex Dialogue Speech at Scale for Spoken Dialogue Language Modeling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DuplexChat语料库及构建流水线，从播客生成双通道全双工对话语音，用于口语对话语言模型训练。</div>
<div class="card-action">
<a href="duplexchat-constructing-speaker-separated-full-duplex-dialog-2607-04941/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04941" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="ranking-the-impact-of-contextual-specialization-in-neural-sp-2607-04826/">Ranking the Impact of Contextual Specialization in Neural Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统研究语音增强模型根据上下文信息（说话人、噪声、语言等）进行特化训练的效果，发现说话人特化收益最大，小模型可匹敌十倍大通用模型。</div>
<div class="card-action">
<a href="ranking-the-impact-of-contextual-specialization-in-neural-sp-2607-04826/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04826" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="mixture-constrained-max-pooling-improves-separation-based-bi-2607-03221/">Mixture-Constrained Max Pooling Improves Separation-Based Bird Species Classification</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出混合约束最大池化（MCM）方法，利用分离后各通道与原始混合物的物种概率联合决策，提升基于分离的鸟类物种分类性能。</div>
<div class="card-action">
<a href="mixture-constrained-max-pooling-improves-separation-based-bi-2607-03221/">详情 →</a> · <a href="https://arxiv.org/abs/2607.03221" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="avis-mamba-adaptive-visual-steering-of-audio-state-space-dyn-2604-03329/">AViS-Mamba: Adaptive Visual Steering of Audio State-Space Dynamics for Violence Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#暴力检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AViS-Mamba，用视觉流自适应调控音频编码器的状态空间动态，在暴力检测任务上达到SOTA。</div>
<div class="card-action">
<a href="avis-mamba-adaptive-visual-steering-of-audio-state-space-dyn-2604-03329/">详情 →</a> · <a href="https://arxiv.org/abs/2604.03329" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="assessing-the-impact-of-noise-and-speech-enhancement-on-the--2605-03776/">Assessing the Impact of Noise and Speech Enhancement on the Intelligibility of Speech Codecs</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音编解码</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">评估经典与神经语音编解码器在噪声条件下的可懂度，并探究编码前语音增强的影响。</div>
<div class="card-action">
<a href="assessing-the-impact-of-noise-and-speech-enhancement-on-the--2605-03776/">详情 →</a> · <a href="https://arxiv.org/abs/2605.03776" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
