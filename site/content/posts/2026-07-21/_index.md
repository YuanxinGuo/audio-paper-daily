---
title: "语音/音频论文速递 2026-07-21"
date: 2026-07-21T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.5（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 1篇 | `██████████` |
| #目标说话人提取 | 1篇 | `██████████` |
| #模型量化 | 1篇 | `██████████` |
| #音频深度伪造检测 | 1篇 | `██████████` |
| #乐器合成 | 1篇 | `██████████` |
| #语音深伪检测 | 1篇 | `██████████` |
| #语音翻译 | 1篇 | `██████████` |
| #音视频事件识别 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="unipase-a-generative-model-for-universal-speech-enhancement--2604-14606/">UniPASE: A Generative Model for Universal Speech Enhancement with High Fidelity and Low Hallucinations</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">UniPASE 基于低幻觉 PASE 框架，通过 DeWavLM-Omni 模块和 Adapter+Vocoder 结构实现多采样率通用语音增强，在 URGENT 2026 挑战赛客观评测中获第一。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-tttai-system-for-the-tsa-asr-task-of-the-smartglasses-ch-2607-17867/">The tttAI System for the TSA-ASR Task of the SmartGlasses Challenge 2026</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出级联系统，结合说话人日志、重叠检测、目标说话人提取和ASR，在智能眼镜挑战赛TSA-ASR任务中取得第二名。</div>
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
| 🥇 | [UniPASE: A Generative Model for Universal Speech Enhancement…](unipase-a-generative-model-for-universal-speech-enhancement--2604-14606/) 🎯 | **9.5** | #语音增强 |
| 🥈 | [The tttAI System for the TSA-ASR Task of the SmartGlasses Ch…](the-tttai-system-for-the-tsa-asr-task-of-the-smartglasses-ch-2607-17867/) 🎯 | **8.8** | #目标说话人提取 |
| 🥉 | [Evolution Strategy-Based Calibration for Low-Bit Quantizatio…](evolution-strategy-based-calibration-for-low-bit-quantizatio-2603-08173/) | **8.5** | #模型量化 |
| 4. | [SONAR: Spectral-Contrastive Audio Residuals for Generalizabl…](sonar-spectral-contrastive-audio-residuals-for-generalizable-2511-21325/) | **8.5** | #音频深度伪造检测 |
| 5. | [Anysynth:Zero-Shot Instrument Cloning via In-Context Learnin…](anysynth-zero-shot-instrument-cloning-via-in-context-learnin-2607-11143/) | **8.2** | #乐器合成 |
| 6. | [Time-Frequency Consistency Learning for Robust Speech Deepfa…](time-frequency-consistency-learning-for-robust-speech-deepfa-2607-17761/) | **7.8** | #语音深伪检测 |
| 7. | [X-Translator: A Real-Time Multilingual Speaker-Aware Speech-…](x-translator-a-real-time-multilingual-speaker-aware-speech-t-2607-17544/) | **7.8** | #语音翻译 |
| 8. | [Efficient Audio-Visual Event Recognition via Knowledge Disti…](efficient-audio-visual-event-recognition-via-knowledge-disti-2607-16980/) | **7.2** | #音视频事件识别 |
| 9. | [Dense-Sparse Dynamic Time Warping for Customizing Piano Conc…](dense-sparse-dynamic-time-warping-for-customizing-piano-conc-2607-18189/) | **7.2** | #音频对齐 |
| 10. | [Adaptive Momentum Enhanced Distributed Multichannel Active N…](adaptive-momentum-enhanced-distributed-multichannel-active-n-2607-17165/) | **6.5** | #主动噪声控制 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="unipase-a-generative-model-for-universal-speech-enhancement--2604-14606/">UniPASE: A Generative Model for Universal Speech Enhancement with High Fidelity and Low Hallucinations</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">UniPASE 基于低幻觉 PASE 框架，通过 DeWavLM-Omni 模块和 Adapter+Vocoder 结构实现多采样率通用语音增强，在 URGENT 2026 挑战赛客观评测中获第一。</div>
<div class="card-action">
<a href="unipase-a-generative-model-for-universal-speech-enhancement--2604-14606/">详情 →</a> · <a href="https://arxiv.org/abs/2604.14606" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="the-tttai-system-for-the-tsa-asr-task-of-the-smartglasses-ch-2607-17867/">The tttAI System for the TSA-ASR Task of the SmartGlasses Challenge 2026</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出级联系统，结合说话人日志、重叠检测、目标说话人提取和ASR，在智能眼镜挑战赛TSA-ASR任务中取得第二名。</div>
<div class="card-action">
<a href="the-tttai-system-for-the-tsa-asr-task-of-the-smartglasses-ch-2607-17867/">详情 →</a> · <a href="https://arxiv.org/abs/2607.17867" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="evolution-strategy-based-calibration-for-low-bit-quantizatio-2603-08173/">Evolution Strategy-Based Calibration for Low-Bit Quantization of Speech Models</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#模型量化</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于进化策略的校准方法ESC，解决语音模型低比特量化中激活值范围大导致的信息损失问题，首次实现全INT4量化近无损性能。</div>
<div class="card-action">
<a href="evolution-strategy-based-calibration-for-low-bit-quantizatio-2603-08173/">详情 →</a> · <a href="https://arxiv.org/abs/2603.08173" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="sonar-spectral-contrastive-audio-residuals-for-generalizable-2511-21325/">SONAR: Spectral-Contrastive Audio Residuals for Generalizable Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SONAR框架，通过频谱对比学习显式分离音频的高低频表示，利用高频残差提升深度伪造检测的泛化性，在ASVspoof 2021和in-the-wild上达到SOTA，收敛速度快4倍。</div>
<div class="card-action">
<a href="sonar-spectral-contrastive-audio-residuals-for-generalizable-2511-21325/">详情 →</a> · <a href="https://arxiv.org/abs/2511.21325" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="anysynth-zero-shot-instrument-cloning-via-in-context-learnin-2607-11143/">Anysynth:Zero-Shot Instrument Cloning via In-Context Learning and Asymmetric Hierarchical Guidance</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Anysynth，一种基于上下文流匹配的无嵌入神经合成器，实现零样本乐器克隆，通过直接条件化未压缩参考音频和MIDI，利用自注意力动态检索声学细节，优于嵌入和自回归基线。</div>
<div class="card-action">
<a href="anysynth-zero-shot-instrument-cloning-via-in-context-learnin-2607-11143/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11143" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="time-frequency-consistency-learning-for-robust-speech-deepfa-2607-17761/">Time-Frequency Consistency Learning for Robust Speech Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音深伪检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出时频一致性学习框架，提升语音深伪检测在真实声学前处理管线下的鲁棒性。</div>
<div class="card-action">
<a href="time-frequency-consistency-learning-for-robust-speech-deepfa-2607-17761/">详情 →</a> · <a href="https://arxiv.org/abs/2607.17761" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="x-translator-a-real-time-multilingual-speaker-aware-speech-t-2607-17544/">X-Translator: A Real-Time Multilingual Speaker-Aware Speech-to-Speech Translation System</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">X-Translator 是一个模块化级联的实时语音到语音翻译系统，通过增量段确认和在线说话人提示管理，在长对话和多说话人场景下平衡翻译质量、延迟和说话人一致性。</div>
<div class="card-action">
<a href="x-translator-a-real-time-multilingual-speaker-aware-speech-t-2607-17544/">详情 →</a> · <a href="https://arxiv.org/abs/2607.17544" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="efficient-audio-visual-event-recognition-via-knowledge-disti-2607-16980/">Efficient Audio-Visual Event Recognition via Knowledge Distillation and Dynamic INT8 Quantization of a Hybrid Cross-Attention Network</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音视频事件识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出结合知识蒸馏和动态INT8量化的压缩框架，在音视频事件识别任务上减少59%参数，模型压缩至2.04MB，精度仅降2.14%。</div>
<div class="card-action">
<a href="efficient-audio-visual-event-recognition-via-knowledge-disti-2607-16980/">详情 →</a> · <a href="https://arxiv.org/abs/2607.16980" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="dense-sparse-dynamic-time-warping-for-customizing-piano-conc-2607-18189/">Dense-Sparse Dynamic Time Warping for Customizing Piano Concerto Accompaniments</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频对齐</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出Dense-Sparse DTW算法，利用混合录音作为中介参考，对齐钢琴独奏与管弦乐伴奏，实现个性化伴奏定制。</div>
<div class="card-action">
<a href="dense-sparse-dynamic-time-warping-for-customizing-piano-conc-2607-18189/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18189" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="adaptive-momentum-enhanced-distributed-multichannel-active-n-2607-17165/">Adaptive Momentum Enhanced Distributed Multichannel Active Noise Control for Faster Convergence under Communication Delays</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#主动噪声控制</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对分布式多通道主动噪声控制在通信延迟下收敛慢的问题，提出自适应动量加速的AMAS-MGDFxLMS算法。</div>
<div class="card-action">
<a href="adaptive-momentum-enhanced-distributed-multichannel-active-n-2607-17165/">详情 →</a> · <a href="https://arxiv.org/abs/2607.17165" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
