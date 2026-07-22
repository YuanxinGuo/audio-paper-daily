---
title: "语音/音频论文速递 2026-07-22"
date: 2026-07-22T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #听觉注意力解码 | 1篇 | `█████` |
| #音频事件定位 | 1篇 | `█████` |
| #音乐情感识别 | 1篇 | `█████` |
| #多模态嵌入 | 1篇 | `█████` |
| #听觉注意解码 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="towards-array-invariant-speech-enhancement-via-geometry-awar-2607-18658/">Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出几何感知动态卷积框架，将固定阵列语音增强模型扩展为阵列不变系统，在RealMAN数据集上验证有效性。</div>
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
| 🥇 | [Towards Array-Invariant Speech Enhancement via Geometry-Awar…](towards-array-invariant-speech-enhancement-via-geometry-awar-2607-18658/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [End-to-End Markov State Sequence Learning for Auditory Atten…](end-to-end-markov-state-sequence-learning-for-auditory-atten-2607-18614/) | **8.2** | #听觉注意力解码 |
| 🥉 | [Harness TTS: Towards Context-Aware Expressive Speech Synthes…](harness-tts-towards-context-aware-expressive-speech-synthesi-2607-17900/) | **7.8** | #语音合成 |
| 4. | [Auto-AEG: Scalable Data Construction for Open-Vocabulary Aud…](auto-aeg-scalable-data-construction-for-open-vocabulary-audi-2607-04383/) | **7.8** | #音频事件定位 |
| 5. | [Memo2496: Expert-Annotated Dataset and Dual-view Adaptive Fr…](memo2496-expert-annotated-dataset-and-dual-view-adaptive-fra-2512-13998/) | **7.8** | #音乐情感识别 |
| 6. | [Fusion Embedding: A Unified Embedding Space for Text, Image,…](fusion-embedding-a-unified-embedding-space-for-text-image-vi-2607-18666/) | **7.8** | #多模态嵌入 |
| 7. | [CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis w…](cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-wi-2607-18629/) | **7.8** | #语音合成 |
| 8. | [Addressing Limited Data in Auditory Attention Decoding with …](addressing-limited-data-in-auditory-attention-decoding-with--2607-18345/) | **7.2** | #听觉注意解码 |
| 9. | [Teleportation Game: Quantum Teleportation in Multi-Agent Sys…](teleportation-game-quantum-teleportation-in-multi-agent-syst-2607-19212/) | **6.5** | #音乐生成 |
| 10. | [What the Waveform Knows: Transparent-first Speech and Audio …](what-the-waveform-knows-transparent-first-speech-and-audio-i-2607-18704/) | **5.5** | #语音处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="towards-array-invariant-speech-enhancement-via-geometry-awar-2607-18658/">Towards Array-Invariant Speech Enhancement via Geometry-Aware Dynamic Convolution</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出几何感知动态卷积框架，将固定阵列语音增强模型扩展为阵列不变系统，在RealMAN数据集上验证有效性。</div>
<div class="card-action">
<a href="towards-array-invariant-speech-enhancement-via-geometry-awar-2607-18658/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18658" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="end-to-end-markov-state-sequence-learning-for-auditory-atten-2607-18614/">End-to-End Markov State Sequence Learning for Auditory Attention Decoding</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#听觉注意力解码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出端到端马尔可夫状态序列学习框架，将听觉注意力解码建模为两状态序列，用CRF联合优化窗口级发射和状态转移，在动态AVGC数据集上达到86.5%因果准确率。</div>
<div class="card-action">
<a href="end-to-end-markov-state-sequence-learning-for-auditory-atten-2607-18614/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18614" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="harness-tts-towards-context-aware-expressive-speech-synthesi-2607-17900/">Harness TTS: Towards Context-Aware Expressive Speech Synthesis with Harness Layer</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Harness TTS，通过轻量控制层将风格控制转化为闭集提示工具路由，实现上下文感知的表达性语音合成。</div>
<div class="card-action">
<a href="harness-tts-towards-context-aware-expressive-speech-synthesi-2607-17900/">详情 →</a> · <a href="https://arxiv.org/abs/2607.17900" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="auto-aeg-scalable-data-construction-for-open-vocabulary-audi-2607-04383/">Auto-AEG: Scalable Data Construction for Open-Vocabulary Audio Event Grounding</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频事件定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Auto-AEG流水线，通过自动数据构建和强化学习微调，解决开放词汇音频事件定位的数据稀缺问题。</div>
<div class="card-action">
<a href="auto-aeg-scalable-data-construction-for-open-vocabulary-audi-2607-04383/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04383" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="memo2496-expert-annotated-dataset-and-dual-view-adaptive-fra-2512-13998/">Memo2496: Expert-Annotated Dataset and Dual-view Adaptive Framework for Music Emotion Recognition</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐情感识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出含2,496首器乐轨道的专家标注情感数据集Memo2496，以及双流自适应框架DAMER，在三个数据集上取得最优或竞争性结果。</div>
<div class="card-action">
<a href="memo2496-expert-annotated-dataset-and-dual-view-adaptive-fra-2512-13998/">详情 →</a> · <a href="https://arxiv.org/abs/2512.13998" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="fusion-embedding-a-unified-embedding-space-for-text-image-vi-2607-18666/">Fusion Embedding: A Unified Embedding Space for Text, Image, Video, and Audio</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#多模态嵌入</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Fusion Embedding系列，通过轻量连接器将音频嵌入到冻结的视觉-语言嵌入空间中，实现跨模态检索。</div>
<div class="card-action">
<a href="fusion-embedding-a-unified-embedding-space-for-text-image-vi-2607-18666/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18666" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-wi-2607-18629/">CS-ETS: Chaos-Inspired Samba-Based EMG-To-Speech Synthesis with Nonlinear Chaotic Losses</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CS-ETS，结合Samba编码器和混沌损失函数，实现高效EMG-to-Speech合成，参数量减少40.79%，性能显著提升。</div>
<div class="card-action">
<a href="cs-ets-chaos-inspired-samba-based-emg-to-speech-synthesis-wi-2607-18629/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18629" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="addressing-limited-data-in-auditory-attention-decoding-with--2607-18345/">Addressing Limited Data in Auditory Attention Decoding with Diffusion Generative Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#听觉注意解码</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">利用扩散概率模型生成合成EEG数据，增强听觉注意解码在短时间窗下的性能。</div>
<div class="card-action">
<a href="addressing-limited-data-in-auditory-attention-decoding-with--2607-18345/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18345" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="teleportation-game-quantum-teleportation-in-multi-agent-syst-2607-19212/">Teleportation Game: Quantum Teleportation in Multi-Agent Systems for Interactive Music</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于量子隐形传态的多智能体交互音乐系统，利用量子态编码旋律与节奏，支持人类与量子智能体实时即兴互动。</div>
<div class="card-action">
<a href="teleportation-game-quantum-teleportation-in-multi-agent-syst-2607-19212/">详情 →</a> · <a href="https://arxiv.org/abs/2607.19212" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="what-the-waveform-knows-transparent-first-speech-and-audio-i-2607-18704/">What the Waveform Knows: Transparent-first Speech and Audio Intelligence with Caption Studio</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#语音处理</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出一个透明优先的语音与音频智能平台Caption Studio，集成转录、说话人日志、语音分析和字幕生成。</div>
<div class="card-action">
<a href="what-the-waveform-knows-transparent-first-speech-and-audio-i-2607-18704/">详情 →</a> · <a href="https://arxiv.org/abs/2607.18704" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
