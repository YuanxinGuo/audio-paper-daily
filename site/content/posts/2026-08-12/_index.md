---
title: "语音/音频论文速递 2026-08-12"
date: 2026-08-12T09:00:00+08:00
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
| #语音增强 | 2篇 | `██████████` |
| #音频伪造检测 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #音频事件定位 | 1篇 | `█████` |
| #神经音频表征 | 1篇 | `█████` |
| #多模态指令跟随 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #声源定位 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dave-a-decoupled-audio-visual-enhancement-framework-for-real-2608-09288/">DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">DAVE提出解耦的音视频增强框架，通过大规模语料DAVE-Corpus和渐进多目标优化，在真实场景语音分离中提升鲁棒性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-watermark-shortcut-how-provenance-marking-sabotages-audi-2606-23335/">The Watermark Shortcut: How Provenance Marking Sabotages Audio Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频伪造检测</span>
</div>
<div class="card-tldr">发现语音水印作为虚假线索导致深度伪造检测器性能下降，提出去相关训练可修复。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="mitigating-over-suppression-in-speech-enhancement-via-infere-2608-07781/">Mitigating Over-Suppression in Speech Enhancement via Inference-Time Rethink-and-Refine Correction Module</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种推理时重思与修正模块，通过ASR对齐识别过抑制区间并选择性重混，无需训练即可提升多种语音增强模型的感知质量和可懂度。</div>
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
<a class="card-title" href="dave-a-decoupled-audio-visual-enhancement-framework-for-real-2608-09288/">DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">DAVE提出解耦的音视频增强框架，通过大规模语料DAVE-Corpus和渐进多目标优化，在真实场景语音分离中提升鲁棒性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dynamic-clustering-for-cross-segment-permutation-alignment-i-2608-09451/">Dynamic Clustering for Cross-Segment Permutation Alignment in Long Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出一种免训练的动态聚类方法，利用说话人嵌入参考池对齐长语音分离中的跨段排列，作为即插即用后处理模块，在稀疏长语音场景中表现优异。</div>
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
| 🥇 | [DAVE: A Decoupled Audio-Visual Enhancement Framework for Rea…](dave-a-decoupled-audio-visual-enhancement-framework-for-real-2608-09288/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [The Watermark Shortcut: How Provenance Marking Sabotages Aud…](the-watermark-shortcut-how-provenance-marking-sabotages-audi-2606-23335/) 🎯 | **8.8** | #音频伪造检测 |
| 🥉 | [Dynamic Clustering for Cross-Segment Permutation Alignment i…](dynamic-clustering-for-cross-segment-permutation-alignment-i-2608-09451/) 🎯 | **8.8** | #语音分离 |
| 4. | [Mitigating Over-Suppression in Speech Enhancement via Infere…](mitigating-over-suppression-in-speech-enhancement-via-infere-2608-07781/) 🎯 | **8.8** | #语音增强 |
| 5. | [SpotSound: Enhancing Large Audio-Language Models with Fine-G…](spotsound-enhancing-large-audio-language-models-with-fine-gr-2604-13023/) | **8.2** | #音频事件定位 |
| 6. | [Topographic Constraints Shape Brain-Like Component Structure…](topographic-constraints-shape-brain-like-component-structure-2509-24039/) | **7.8** | #神经音频表征 |
| 7. | [MCIF: Multimodal Crosslingual Instruction-Following Benchmar…](mcif-multimodal-crosslingual-instruction-following-benchmark-2507-19634/) | **7.8** | #多模态指令跟随 |
| 8. | [IndexTTS 2.5 Technical Report](indextts-2-5-technical-report-2601-03888/) | **7.8** | #语音合成 |
| 9. | [Physics-Informed Learning for Robust Acoustic Localization w…](physics-informed-learning-for-robust-acoustic-localization-w-2608-08911/) | **7.8** | #声源定位 |
| 10. | [A Multi-Scale Temporal Framework with Dynamic Fusion for EEG…](a-multi-scale-temporal-framework-with-dynamic-fusion-for-eeg-2608-09088/) | **6.5** | #情感识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="dave-a-decoupled-audio-visual-enhancement-framework-for-real-2608-09288/">DAVE: A Decoupled Audio-Visual Enhancement Framework for Real-World Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">DAVE提出解耦的音视频增强框架，通过大规模语料DAVE-Corpus和渐进多目标优化，在真实场景语音分离中提升鲁棒性。</div>
<div class="card-action">
<a href="dave-a-decoupled-audio-visual-enhancement-framework-for-real-2608-09288/">详情 →</a> · <a href="https://arxiv.org/abs/2608.09288" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="the-watermark-shortcut-how-provenance-marking-sabotages-audi-2606-23335/">The Watermark Shortcut: How Provenance Marking Sabotages Audio Deepfake Detection</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发现语音水印作为虚假线索导致深度伪造检测器性能下降，提出去相关训练可修复。</div>
<div class="card-action">
<a href="the-watermark-shortcut-how-provenance-marking-sabotages-audi-2606-23335/">详情 →</a> · <a href="https://arxiv.org/abs/2606.23335" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="dynamic-clustering-for-cross-segment-permutation-alignment-i-2608-09451/">Dynamic Clustering for Cross-Segment Permutation Alignment in Long Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种免训练的动态聚类方法，利用说话人嵌入参考池对齐长语音分离中的跨段排列，作为即插即用后处理模块，在稀疏长语音场景中表现优异。</div>
<div class="card-action">
<a href="dynamic-clustering-for-cross-segment-permutation-alignment-i-2608-09451/">详情 →</a> · <a href="https://arxiv.org/abs/2608.09451" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="mitigating-over-suppression-in-speech-enhancement-via-infere-2608-07781/">Mitigating Over-Suppression in Speech Enhancement via Inference-Time Rethink-and-Refine Correction Module</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种推理时重思与修正模块，通过ASR对齐识别过抑制区间并选择性重混，无需训练即可提升多种语音增强模型的感知质量和可懂度。</div>
<div class="card-action">
<a href="mitigating-over-suppression-in-speech-enhancement-via-infere-2608-07781/">详情 →</a> · <a href="https://arxiv.org/abs/2608.07781" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="spotsound-enhancing-large-audio-language-models-with-fine-gr-2604-13023/">SpotSound: Enhancing Large Audio-Language Models with Fine-Grained Temporal Grounding</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频事件定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">SpotSound 提出一种带时间定位能力的音频语言模型，通过新训练目标抑制幻觉时间戳，并构建了目标事件占比极低的 SpotSound-Bench 基准，在时间定位任务上达到 SOTA。</div>
<div class="card-action">
<a href="spotsound-enhancing-large-audio-language-models-with-fine-gr-2604-13023/">详情 →</a> · <a href="https://arxiv.org/abs/2604.13023" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="topographic-constraints-shape-brain-like-component-structure-2509-24039/">Topographic Constraints Shape Brain-Like Component Structure in Auditory Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#神经音频表征</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出TopoAudio，在音频模型训练中引入拓扑约束，使内部表征更接近人脑听觉皮层的组件结构，同时保持任务性能。</div>
<div class="card-action">
<a href="topographic-constraints-shape-brain-like-component-structure-2509-24039/">详情 →</a> · <a href="https://arxiv.org/abs/2509.24039" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="mcif-multimodal-crosslingual-instruction-following-benchmark-2507-19634/">MCIF: Multimodal Crosslingual Instruction-Following Benchmark from Scientific Talks</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#多模态指令跟随</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MCIF是首个基于科学演讲的跨语言人工标注多模态指令跟随基准，覆盖四种语言和三种模态，评估23个模型发现普遍挑战。</div>
<div class="card-action">
<a href="mcif-multimodal-crosslingual-instruction-following-benchmark-2507-19634/">详情 →</a> · <a href="https://arxiv.org/abs/2507.19634" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="indextts-2-5-technical-report-2601-03888/">IndexTTS 2.5 Technical Report</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">IndexTTS 2.5通过语义码率减半、Zipformer架构、跨语言策略和GRPO优化，实现多语言情感语音合成，速度提升2.28倍且质量持平。</div>
<div class="card-action">
<a href="indextts-2-5-technical-report-2601-03888/">详情 →</a> · <a href="https://arxiv.org/abs/2601.03888" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="physics-informed-learning-for-robust-acoustic-localization-w-2608-08911/">Physics-Informed Learning for Robust Acoustic Localization with Calibrated Uncertainty</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声源定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出物理信息学习框架，修正双曲定位在复杂户外声景中的极端误差，并提供校准的不确定性估计。</div>
<div class="card-action">
<a href="physics-informed-learning-for-robust-acoustic-localization-w-2608-08911/">详情 →</a> · <a href="https://arxiv.org/abs/2608.08911" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="a-multi-scale-temporal-framework-with-dynamic-fusion-for-eeg-2608-09088/">A Multi-Scale Temporal Framework with Dynamic Fusion for EEG-Based Emotion Recognition</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出多尺度时间框架，用共享注意力编码器和动态融合模块处理EEG信号，在二分类和三分类情感识别中优于全信号基线。</div>
<div class="card-action">
<a href="a-multi-scale-temporal-framework-with-dynamic-fusion-for-eeg-2608-09088/">详情 →</a> · <a href="https://arxiv.org/abs/2608.09088" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
