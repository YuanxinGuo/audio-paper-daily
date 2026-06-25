---
title: "语音/音频论文速递 2026-06-25"
date: 2026-06-25T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #多模态交互 | 1篇 | `█████` |
| #音乐信息检索 | 1篇 | `█████` |
| #异常声音检测 | 1篇 | `█████` |
| #情感识别 | 1篇 | `█████` |
| #语音翻译 | 1篇 | `█████` |
| #音频效果控制 | 1篇 | `█████` |
| #语音识别后处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="one-model-many-latencies-universal-speech-enhancement-for-di-2606-25621/">One Model, Many Latencies: Universal Speech Enhancement for Diverse Real-Time Applications</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种统一模型，通过可配置前瞻帧和早期退出机制，灵活控制算法和计算延迟，适用于多种实时语音增强场景。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="se-agcnet-an-end-to-end-framework-for-joint-speech-enhanceme-2606-25959/">SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出SE-AGCNet，端到端联合优化语音增强与自动增益控制，在会议场景中同时提升语音质量和响度一致性。</div>
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
| 🥇 | [One Model, Many Latencies: Universal Speech Enhancement for …](one-model-many-latencies-universal-speech-enhancement-for-di-2606-25621/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Wan-Streamer v0.1: End-to-end Real-time Interactive Foundati…](wan-streamer-v0-1-end-to-end-real-time-interactive-foundatio-2606-25041/) | **8.5** | #多模态交互 |
| 🥉 | [SE-AGCNet: An End-to-End Framework for Joint Speech Enhancem…](se-agcnet-an-end-to-end-framework-for-joint-speech-enhanceme-2606-25959/) 🎯 | **8.5** | #语音增强 |
| 4. | [Frequency-Aware Self-Supervised Music Representation Learnin…](frequency-aware-self-supervised-music-representation-learnin-2606-25713/) | **8.2** | #音乐信息检索 |
| 5. | [A Neuromorphic Trigger for Efficient Audio Event Detection](a-neuromorphic-trigger-for-efficient-audio-event-detection-2606-17775/) | **7.8** | #异常声音检测 |
| 6. | [SpeechEQ: Benchmarking Emotional Intelligence Quotient in So…](speecheq-benchmarking-emotional-intelligence-quotient-in-soc-2606-25990/) | **7.8** | #情感识别 |
| 7. | [STEB: A Speech-to-Speech Translation Expressiveness Benchmar…](steb-a-speech-to-speech-translation-expressiveness-benchmark-2606-25529/) | **7.8** | #语音翻译 |
| 8. | [InstructFX2FX: A Multi-turn Text-to-Preset Demo for Iterativ…](instructfx2fx-a-multi-turn-text-to-preset-demo-for-iterative-2606-22005/) | **7.2** | #音频效果控制 |
| 9. | [Graph-Based Phonetic Error Correction of Noisy ASR](graph-based-phonetic-error-correction-of-noisy-asr-2606-24889/) | **7.2** | #语音识别后处理 |
| 10. | [FoleySet: A Multi-Level Human-Annotated Foley Sound Dataset](foleyset-a-multi-level-human-annotated-foley-sound-dataset-2606-25980/) | **7.2** | #音频数据集 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="one-model-many-latencies-universal-speech-enhancement-for-di-2606-25621/">One Model, Many Latencies: Universal Speech Enhancement for Diverse Real-Time Applications</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种统一模型，通过可配置前瞻帧和早期退出机制，灵活控制算法和计算延迟，适用于多种实时语音增强场景。</div>
<div class="card-action">
<a href="one-model-many-latencies-universal-speech-enhancement-for-di-2606-25621/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25621" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="wan-streamer-v0-1-end-to-end-real-time-interactive-foundatio-2606-25041/">Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#多模态交互</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出Wan-Streamer，一个原生流式、端到端的多模态交互基础模型，统一建模语言、音频和视频，实现约200ms模型响应延迟和550ms总交互延迟。</div>
<div class="card-action">
<a href="wan-streamer-v0-1-end-to-end-real-time-interactive-foundatio-2606-25041/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25041" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="se-agcnet-an-end-to-end-framework-for-joint-speech-enhanceme-2606-25959/">SE-AGCNet: An End-to-End Framework for Joint Speech Enhancement and Loudness Control in Meeting Scenarios</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SE-AGCNet，端到端联合优化语音增强与自动增益控制，在会议场景中同时提升语音质量和响度一致性。</div>
<div class="card-action">
<a href="se-agcnet-an-end-to-end-framework-for-joint-speech-enhanceme-2606-25959/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25959" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="frequency-aware-self-supervised-music-representation-learnin-2606-25713/">Frequency-Aware Self-Supervised Music Representation Learning</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出PupuJEPA，一种在2D频谱图上训练的视觉JEPA模型，用于自监督音乐表示学习，在MARBLE基准上超越1D序列SSL模型。</div>
<div class="card-action">
<a href="frequency-aware-self-supervised-music-representation-learnin-2606-25713/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25713" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="a-neuromorphic-trigger-for-efficient-audio-event-detection-2606-17775/">A Neuromorphic Trigger for Efficient Audio Event Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#异常声音检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于脉冲神经网络的神经形态触发器，作为低功耗前端选择性激活下游模型，在ASD和SED任务上实现高F1分数和42.6倍FLOPs降低。</div>
<div class="card-action">
<a href="a-neuromorphic-trigger-for-efficient-audio-event-detection-2606-17775/">详情 →</a> · <a href="https://arxiv.org/abs/2606.17775" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="speecheq-benchmarking-emotional-intelligence-quotient-in-soc-2606-25990/">SpeechEQ: Benchmarking Emotional Intelligence Quotient in Socially Aware Voice Conversational Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#情感识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SpeechEQ框架，评估语音语言模型在多轮对话中的社会语言推理能力，包含2265个对话数据集和SEQ评分指标。</div>
<div class="card-action">
<a href="speecheq-benchmarking-emotional-intelligence-quotient-in-soc-2606-25990/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25990" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="steb-a-speech-to-speech-translation-expressiveness-benchmark-2606-25529/">STEB: A Speech-to-Speech Translation Expressiveness Benchmark for Evaluating Beyond Translation Fidelity</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出STEB基准，评估语音到语音翻译中的表现力（情感、场景风格、非语言声音）保留，发现现有系统在语义翻译上表现良好但表现力保留不足。</div>
<div class="card-action">
<a href="steb-a-speech-to-speech-translation-expressiveness-benchmark-2606-25529/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25529" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="instructfx2fx-a-multi-turn-text-to-preset-demo-for-iterative-2606-22005/">InstructFX2FX: A Multi-turn Text-to-Preset Demo for Iterative Audio Effect Refinement</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频效果控制</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出多轮文本引导音频效果调整系统，结合LLM规划与CLAP优化，实现迭代式音色精调。</div>
<div class="card-action">
<a href="instructfx2fx-a-multi-turn-text-to-preset-demo-for-iterative-2606-22005/">详情 →</a> · <a href="https://arxiv.org/abs/2606.22005" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="graph-based-phonetic-error-correction-of-noisy-asr-2606-24889/">Graph-Based Phonetic Error Correction of Noisy ASR</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别后处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出G-SPIN框架，结合图神经网络与语言模型，对ASR输出中语音学相似的错误进行结构化纠正。</div>
<div class="card-action">
<a href="graph-based-phonetic-error-correction-of-noisy-asr-2606-24889/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24889" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="foleyset-a-multi-level-human-annotated-foley-sound-dataset-2606-25980/">FoleySet: A Multi-Level Human-Annotated Foley Sound Dataset</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频数据集</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">FoleySet是一个包含10,000个音频片段、带两级Foley分类标注的公开数据集，旨在推动数据驱动的Foley音效研究。</div>
<div class="card-action">
<a href="foleyset-a-multi-level-human-annotated-foley-sound-dataset-2606-25980/">详情 →</a> · <a href="https://arxiv.org/abs/2606.25980" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
