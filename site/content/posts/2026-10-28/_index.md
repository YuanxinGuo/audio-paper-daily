---
title: "语音/音频论文速递 2026-10-28"
date: 2026-10-28T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #目标说话人提取 | 2篇 | `███████` |
| #音乐生成 | 1篇 | `███` |
| #说话人日志 | 1篇 | `███` |
| #多模态嵌入 | 1篇 | `███` |
| #音频理解 | 1篇 | `███` |
| #脑电信号解码 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="streamse-neural-audio-codec-based-streaming-speech-enhanceme-2610-37024/">StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在冻结神经音频编解码器的连续潜空间做逐帧回归，实现20M参数、无前瞻、单次前向的流式语音增强，可在手机单核实时运行。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="design-and-architecture-of-airmod-an-active-noise-cancellati-2610-37083/">Design and Architecture of Airmod: An Active Noise Cancellation and Deep Learning System for Real-Time Respiratory Rate Estimation from Tracheal Sounds</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">Airmod 用双麦克风主动降噪加 CNN-BiGRU 检测气管音吸呼气事件，实时估计呼吸率，已获 FDA 510(k) 认证。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="perceptual-differences-and-preferences-in-speech-enhancement-2610-36892/">Perceptual Differences and Preferences in Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">用众包三角测试与成对偏好测试，考察四个语音增强系统在可辨别性与偏好两个维度上的感知差异。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="tap2listen-instant-target-switching-for-streaming-audio-visu-2610-36643/">Tap2Listen: Instant Target Switching for Streaming Audio-Visual Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出流式音视频目标说话人提取模型 Tap2Listen，将目标无关音频编码与目标相关视觉条件解耦，实现 0.12ms 目标切换与首帧满质量输出。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-lightweight-dual-branch-visual-front-end-for-efficient-aud-2610-36834/">A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出双分支视觉前端，用唇部ROI卷积与面部关键点时序卷积替代ResNet18，视觉编码计算降90%以上。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-lightweight-dual-branch-visual-front-end-for-efficient-aud-2610-36834/">A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出双分支视觉前端，用唇部ROI卷积与面部关键点时序卷积替代ResNet18，视觉编码计算降90%以上。</div>
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
| 🥇 | [Tap2Listen: Instant Target Switching for Streaming Audio-Vis…](tap2listen-instant-target-switching-for-streaming-audio-visu-2610-36643/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [StreamSE: Neural Audio Codec-based Streaming Speech Enhancem…](streamse-neural-audio-codec-based-streaming-speech-enhanceme-2610-37024/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Design and Architecture of Airmod: An Active Noise Cancellat…](design-and-architecture-of-airmod-an-active-noise-cancellati-2610-37083/) 🎯 | **7.8** | #语音增强 |
| 4. | [Perceptual Differences and Preferences in Speech Enhancement](perceptual-differences-and-preferences-in-speech-enhancement-2610-36892/) 🎯 | **7.8** | #语音增强 |
| 5. | [A Lightweight Dual-Branch Visual Front-End for Efficient Aud…](a-lightweight-dual-branch-visual-front-end-for-efficient-aud-2610-36834/) 🎯 | **7.8** | #目标说话人提取 |
| 6. | [Streaming Generation for Music Accompaniment](streaming-generation-for-music-accompaniment-2510-22105/) | **7.2** | #音乐生成 |
| 7. | [Understanding Everyday Communication Patterns, Stress, and P…](understanding-everyday-communication-patterns-stress-and-pro-2610-37270/) | **6.8** | #说话人日志 |
| 8. | [EmbeddingGemma 2: Unified and Efficient Multimodal Represent…](embeddinggemma-2-unified-and-efficient-multimodal-representa-2610-37364/) | **6.0** | #多模态嵌入 |
| 9. | [Beyond Answer Changes: Matched Same-Class Controls for Local…](beyond-answer-changes-matched-same-class-controls-for-local--2610-37605/) | **6.0** | #音频理解 |
| 10. | [EEG-Based Decoding of Musical Mode and Melodic Direction Usi…](eeg-based-decoding-of-musical-mode-and-melodic-direction-usi-2610-37148/) | **5.8** | #脑电信号解码 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="tap2listen-instant-target-switching-for-streaming-audio-visu-2610-36643/">Tap2Listen: Instant Target Switching for Streaming Audio-Visual Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出流式音视频目标说话人提取模型 Tap2Listen，将目标无关音频编码与目标相关视觉条件解耦，实现 0.12ms 目标切换与首帧满质量输出。</div>
<div class="card-action">
<a href="tap2listen-instant-target-switching-for-streaming-audio-visu-2610-36643/">详情 →</a> · <a href="https://arxiv.org/abs/2610.36643" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="streamse-neural-audio-codec-based-streaming-speech-enhanceme-2610-37024/">StreamSE: Neural Audio Codec-based Streaming Speech Enhancement for On-device Inference</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在冻结神经音频编解码器的连续潜空间做逐帧回归，实现20M参数、无前瞻、单次前向的流式语音增强，可在手机单核实时运行。</div>
<div class="card-action">
<a href="streamse-neural-audio-codec-based-streaming-speech-enhanceme-2610-37024/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37024" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="design-and-architecture-of-airmod-an-active-noise-cancellati-2610-37083/">Design and Architecture of Airmod: An Active Noise Cancellation and Deep Learning System for Real-Time Respiratory Rate Estimation from Tracheal Sounds</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">Airmod 用双麦克风主动降噪加 CNN-BiGRU 检测气管音吸呼气事件，实时估计呼吸率，已获 FDA 510(k) 认证。</div>
<div class="card-action">
<a href="design-and-architecture-of-airmod-an-active-noise-cancellati-2610-37083/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37083" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="perceptual-differences-and-preferences-in-speech-enhancement-2610-36892/">Perceptual Differences and Preferences in Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用众包三角测试与成对偏好测试，考察四个语音增强系统在可辨别性与偏好两个维度上的感知差异。</div>
<div class="card-action">
<a href="perceptual-differences-and-preferences-in-speech-enhancement-2610-36892/">详情 →</a> · <a href="https://arxiv.org/abs/2610.36892" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="a-lightweight-dual-branch-visual-front-end-for-efficient-aud-2610-36834/">A Lightweight Dual-Branch Visual Front-End for Efficient Audio-Visual Target Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出双分支视觉前端，用唇部ROI卷积与面部关键点时序卷积替代ResNet18，视觉编码计算降90%以上。</div>
<div class="card-action">
<a href="a-lightweight-dual-branch-visual-front-end-for-efficient-aud-2610-36834/">详情 →</a> · <a href="https://arxiv.org/abs/2610.36834" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="streaming-generation-for-music-accompaniment-2510-22105/">Streaming Generation for Music Accompaniment</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">研究实时音频到音频的伴奏生成，提出以未来可见度tf与输出块长k为设计变量，系统刻画延迟与连贯性的权衡。</div>
<div class="card-action">
<a href="streaming-generation-for-music-accompaniment-2510-22105/">详情 →</a> · <a href="https://arxiv.org/abs/2510.22105" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="understanding-everyday-communication-patterns-stress-and-pro-2610-37270/">Understanding Everyday Communication Patterns, Stress, and Productivity in Hybrid Work through Egocentric Wearable Audio Sensing</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用第一视角可穿戴音频传感器采集混合办公沟通行为，并以教师-学生蒸馏提升低维特征下的说话人日志性能。</div>
<div class="card-action">
<a href="understanding-everyday-communication-patterns-stress-and-pro-2610-37270/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37270" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="embeddinggemma-2-unified-and-efficient-multimodal-representa-2610-37364/">EmbeddingGemma 2: Unified and Efficient Multimodal Representations</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#多模态嵌入</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出开源多模态嵌入模型 EmbeddingGemma 2，统一表征文本、图像、音频、视频，在嵌入基准上取得 Pareto 前沿。</div>
<div class="card-action">
<a href="embeddinggemma-2-unified-and-efficient-multimodal-representa-2610-37364/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37364" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="beyond-answer-changes-matched-same-class-controls-for-local--2610-37605/">Beyond Answer Changes: Matched Same-Class Controls for Local Audio Evidence</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出同类别匹配对照协议，区分音频语言模型对事件类别与波形改写的敏感度。</div>
<div class="card-action">
<a href="beyond-answer-changes-matched-same-class-controls-for-local--2610-37605/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37605" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="eeg-based-decoding-of-musical-mode-and-melodic-direction-usi-2610-37148/">EEG-Based Decoding of Musical Mode and Melodic Direction Using Empirical Mode Decomposition</a>
<div class="card-meta">
<span class="card-score">5.8</span>
<span class="tag-pill">#脑电信号解码</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用EMD分解钢琴演奏时EEG信号，取前四个IMF的能量特征训练宽神经网络，解码调式与旋律走向。</div>
<div class="card-action">
<a href="eeg-based-decoding-of-musical-mode-and-melodic-direction-usi-2610-37148/">详情 →</a> · <a href="https://arxiv.org/abs/2610.37148" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
