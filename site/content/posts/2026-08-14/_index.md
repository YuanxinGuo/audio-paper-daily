---
title: "语音/音频论文速递 2026-08-14"
date: 2026-08-14T09:00:00+08:00
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
| #语音增强 | 4篇 | `██████████` |
| #音乐生成 | 2篇 | `█████` |
| #语音合成 | 2篇 | `█████` |
| #音频-视觉身份替换 | 1篇 | `██` |
| #关键词唤醒 | 1篇 | `██` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="rt-semamba-real-time-speech-enhancement-mamba-via-progressiv-2608-12099/">RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">RT-SEMamba提出基于因果时频Mamba的实时语音增强模型，通过渐进式知识蒸馏将8层教师压缩为1层学生，在Voicebank-DEMAND上达到3.18 PESQ，速度提升2.75倍。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="rethinking-language-model-based-generative-speech-enhancemen-2608-12082/">Rethinking Language Model-Based Generative Speech Enhancement in the Latent Space of a Neural Audio Codec</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文统一了六种基于语言模型的生成式语音增强范式，首次在统一实验设置下比较，并提出辅助损失微调策略提升主客观指标。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hybrid-real-and-complex-valued-neural-network-architecture-f-2509-21185/">Hybrid Real- and Complex-Valued Neural Network Architecture for Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出混合实值-复值神经网络用于单声道语音增强，在匹配参数下以更低计算量提升语音可懂度和质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="deep-learning-based-relative-transfer-matrix-estimation-for--2608-11627/">Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文提出三种深度学习框架估计多源多麦克风的相对传递矩阵，在客观指标上优于传统协方差方法，并验证了其在语音增强中的有效性。</div>
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
| 🥇 | [RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressi…](rt-semamba-real-time-speech-enhancement-mamba-via-progressiv-2608-12099/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [Rethinking Language Model-Based Generative Speech Enhancemen…](rethinking-language-model-based-generative-speech-enhancemen-2608-12082/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [UniSwap: Streaming Audio-Visual Identity Swapping for Talkin…](uniswap-streaming-audio-visual-identity-swapping-for-talking-2608-11752/) | **8.2** | #音频-视觉身份替换 |
| 4. | [MuseCritic: Learning Multi-Aspect Song Rewards through Natur…](musecritic-learning-multi-aspect-song-rewards-through-natura-2608-11755/) | **8.2** | #音乐生成 |
| 5. | [Phoenix TTS: High-Fidelity Synthesis and Voice Conversion vi…](phoenix-tts-high-fidelity-synthesis-and-voice-conversion-via-2608-11737/) | **8.2** | #语音合成 |
| 6. | [Hybrid Real- and Complex-Valued Neural Network Architecture …](hybrid-real-and-complex-valued-neural-network-architecture-f-2509-21185/) 🎯 | **8.2** | #语音增强 |
| 7. | [Synaspot: A Lightweight, Streaming Multi-modal Framework for…](synaspot-a-lightweight-streaming-multi-modal-framework-for-k-2512-15124/) | **7.8** | #关键词唤醒 |
| 8. | [Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS …](confucius4-tts-transcript-free-cross-lingual-zero-shot-tts-w-2608-11650/) | **7.8** | #语音合成 |
| 9. | [Deep Learning Based Relative Transfer Matrix Estimation for …](deep-learning-based-relative-transfer-matrix-estimation-for--2608-11627/) 🎯 | **7.8** | #语音增强 |
| 10. | [Do Text-to-Music Models Really Follow Instructions? A Counte…](do-text-to-music-models-really-follow-instructions-a-counter-2608-11899/) | **7.2** | #音乐生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="rt-semamba-real-time-speech-enhancement-mamba-via-progressiv-2608-12099/">RT-SEMamba: Real-Time Speech Enhancement Mamba via Progressive Knowledge Distillation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">RT-SEMamba提出基于因果时频Mamba的实时语音增强模型，通过渐进式知识蒸馏将8层教师压缩为1层学生，在Voicebank-DEMAND上达到3.18 PESQ，速度提升2.75倍。</div>
<div class="card-action">
<a href="rt-semamba-real-time-speech-enhancement-mamba-via-progressiv-2608-12099/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12099" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="rethinking-language-model-based-generative-speech-enhancemen-2608-12082/">Rethinking Language Model-Based Generative Speech Enhancement in the Latent Space of a Neural Audio Codec</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文统一了六种基于语言模型的生成式语音增强范式，首次在统一实验设置下比较，并提出辅助损失微调策略提升主客观指标。</div>
<div class="card-action">
<a href="rethinking-language-model-based-generative-speech-enhancemen-2608-12082/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12082" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="uniswap-streaming-audio-visual-identity-swapping-for-talking-2608-11752/">UniSwap: Streaming Audio-Visual Identity Swapping for Talking Videos</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频-视觉身份替换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">UniSwap提出首个流式联合音视频身份替换框架，通过扩散Transformer同时迁移外观和音色，并采用多种策略实现高效长视频生成。</div>
<div class="card-action">
<a href="uniswap-streaming-audio-visual-identity-swapping-for-talking-2608-11752/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11752" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="musecritic-learning-multi-aspect-song-rewards-through-natura-2608-11755/">MuseCritic: Learning Multi-Aspect Song Rewards through Natural-Language Aesthetic Critiques</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MUSECRITIC，一种半标量奖励模型，通过生成自然语言审美评论作为中间表示来预测歌曲的连续奖励分数，显著提升评分准确率并有效用于歌曲生成的强化学习对齐。</div>
<div class="card-action">
<a href="musecritic-learning-multi-aspect-song-rewards-through-natura-2608-11755/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11755" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="phoenix-tts-high-fidelity-synthesis-and-voice-conversion-via-2608-11737/">Phoenix TTS: High-Fidelity Synthesis and Voice Conversion via Flow-Matching-Driven Speech Tokenization</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">Phoenix TTS通过联合优化语音分词器与流匹配生成模型，弥合离散令牌与连续声学空间差距，实现高保真零样本语音合成与转换。</div>
<div class="card-action">
<a href="phoenix-tts-high-fidelity-synthesis-and-voice-conversion-via-2608-11737/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11737" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="hybrid-real-and-complex-valued-neural-network-architecture-f-2509-21185/">Hybrid Real- and Complex-Valued Neural Network Architecture for Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出混合实值-复值神经网络用于单声道语音增强，在匹配参数下以更低计算量提升语音可懂度和质量。</div>
<div class="card-action">
<a href="hybrid-real-and-complex-valued-neural-network-architecture-f-2509-21185/">详情 →</a> · <a href="https://arxiv.org/abs/2509.21185" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="synaspot-a-lightweight-streaming-multi-modal-framework-for-k-2512-15124/">Synaspot: A Lightweight, Streaming Multi-modal Framework for Keyword Spotting with Audio-Text Synergy</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#关键词唤醒</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出轻量流式多模态关键词唤醒框架，通过去声纹的语音注册和数学解码，在LibriPhase和WenetPrase上以更少参数超越现有流式方法。</div>
<div class="card-action">
<a href="synaspot-a-lightweight-streaming-multi-modal-framework-for-k-2512-15124/">详情 →</a> · <a href="https://arxiv.org/abs/2512.15124" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="confucius4-tts-transcript-free-cross-lingual-zero-shot-tts-w-2608-11650/">Confucius4-TTS: Transcript-Free Cross-Lingual Zero-Shot TTS with a Learnable Speaker Encoder</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">Confucius4-TTS提出无需参考音频转录的跨语言零样本TTS系统，支持14种语言，通过可学习说话人编码器提取音色，在CV3-Eval上WER达3.73%。</div>
<div class="card-action">
<a href="confucius4-tts-transcript-free-cross-lingual-zero-shot-tts-w-2608-11650/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11650" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="deep-learning-based-relative-transfer-matrix-estimation-for--2608-11627/">Deep Learning Based Relative Transfer Matrix Estimation for Multiple Sources and Multiple Microphones</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文提出三种深度学习框架估计多源多麦克风的相对传递矩阵，在客观指标上优于传统协方差方法，并验证了其在语音增强中的有效性。</div>
<div class="card-action">
<a href="deep-learning-based-relative-transfer-matrix-estimation-for--2608-11627/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11627" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="do-text-to-music-models-really-follow-instructions-a-counter-2608-11899/">Do Text-to-Music Models Really Follow Instructions? A Counterfactual Evaluation of Key and Beat Grouping</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出匹配反事实评估框架，分离文本到音乐模型中指令控制与输出先验，发现现有模型在节拍分组上的控制力被高估。</div>
<div class="card-action">
<a href="do-text-to-music-models-really-follow-instructions-a-counter-2608-11899/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11899" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
