---
title: "语音/音频论文速递 2026-08-31"
date: 2026-08-31T09:00:00+08:00
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
| #语音增强 | 1篇 | `██████████` |
| #语音生成 | 1篇 | `██████████` |
| #双耳音频 | 1篇 | `██████████` |
| #音乐生成 | 1篇 | `██████████` |
| #音乐理解 | 1篇 | `██████████` |
| #语音翻译 | 1篇 | `██████████` |
| #声速剖面估计 | 1篇 | `██████████` |
| #语音情感识别 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="low-power-end-to-end-cochlear-implant-speech-denoising-with--2608-28493/">Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种受Deep ACE启发的SNN，同时进行语音增强和人工耳蜗编码，在保持VSTOI和SNRi性能的同时，能耗降低六倍以上。</div>
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
<a class="card-title" href="effects-of-hrtf-augmentation-on-predicted-spatial-release-fr-2608-28422/">Effects of HRTF Augmentation on Predicted Spatial Release from Masking in Music</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">本文提出通过增强个性化HRTF来提升音乐中乐器分离的空间线索，听觉模型预测显示对正常听力有益，但对听力损失者效果减弱。</div>
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
| 🥇 | [Low-Power End-to-End Cochlear Implant Speech Denoising with …](low-power-end-to-end-cochlear-implant-speech-denoising-with--2608-28493/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Rethinking Speaker Embeddings for Speech Generation: Sub-Cen…](rethinking-speaker-embeddings-for-speech-generation-sub-cent-2407-04291/) | **7.8** | #语音生成 |
| 🥉 | [Effects of HRTF Augmentation on Predicted Spatial Release fr…](effects-of-hrtf-augmentation-on-predicted-spatial-release-fr-2608-28422/) 🎯 | **7.8** | #双耳音频 |
| 4. | [How Far Should Tokenization Go? Predictive Effectiveness and…](how-far-should-tokenization-go-predictive-effectiveness-and--2608-18025/) | **7.2** | #音乐生成 |
| 5. | [MuSP-Bench: Advanced Multimodal Benchmarking of Music Unders…](musp-bench-advanced-multimodal-benchmarking-of-music-underst-2608-28212/) | **7.2** | #音乐理解 |
| 6. | [Is Prosody Lost in Translation? Fine-Grained Cross-Lingual P…](is-prosody-lost-in-translation-fine-grained-cross-lingual-pr-2608-27848/) | **7.2** | #语音翻译 |
| 7. | [An Attention-Assisted AI Model for Real-Time Underwater Soun…](an-attention-assisted-ai-model-for-real-time-underwater-soun-2502-12817/) | **6.8** | #声速剖面估计 |
| 8. | [A Shaky Voice Is Not Always a Dodge: Benchmarking Textual an…](a-shaky-voice-is-not-always-a-dodge-benchmarking-textual-and-2608-28040/) | **6.8** | #语音情感识别 |
| 9. | [Predicting Turn-Taking Outcomes in Multi-Party Conversation:…](predicting-turn-taking-outcomes-in-multi-party-conversation--2608-27988/) | **6.8** | #对话分析 |
| 10. | [Effectiveness of IoT and Deep Learning for Detection and Sev…](effectiveness-of-iot-and-deep-learning-for-detection-and-sev-2608-27480/) | **6.8** | #生物声学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="low-power-end-to-end-cochlear-implant-speech-denoising-with--2608-28493/">Low-Power End-to-End Cochlear Implant Speech Denoising with Spiking Neural Networks</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种受Deep ACE启发的SNN，同时进行语音增强和人工耳蜗编码，在保持VSTOI和SNRi性能的同时，能耗降低六倍以上。</div>
<div class="card-action">
<a href="low-power-end-to-end-cochlear-implant-speech-denoising-with--2608-28493/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28493" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="rethinking-speaker-embeddings-for-speech-generation-sub-cent-2407-04291/">Rethinking Speaker Embeddings for Speech Generation: Sub-Center Modeling for Capturing Intra-Speaker Diversity</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出子中心说话人嵌入建模，在判别训练中保留说话人内变异性，提升零样本语音转换的自然度和韵律多样性。</div>
<div class="card-action">
<a href="rethinking-speaker-embeddings-for-speech-generation-sub-cent-2407-04291/">详情 →</a> · <a href="https://arxiv.org/abs/2407.04291" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="effects-of-hrtf-augmentation-on-predicted-spatial-release-fr-2608-28422/">Effects of HRTF Augmentation on Predicted Spatial Release from Masking in Music</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文提出通过增强个性化HRTF来提升音乐中乐器分离的空间线索，听觉模型预测显示对正常听力有益，但对听力损失者效果减弱。</div>
<div class="card-action">
<a href="effects-of-hrtf-augmentation-on-predicted-spatial-release-fr-2608-28422/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28422" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="how-far-should-tokenization-go-predictive-effectiveness-and--2608-18025/">How Far Should Tokenization Go? Predictive Effectiveness and Relational Losslessness</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出有效性-无损框架，用预测码长统一判定符号音乐token化边界，实验表明显式时间坐标和可逆BPE影响预测性能。</div>
<div class="card-action">
<a href="how-far-should-tokenization-go-predictive-effectiveness-and--2608-18025/">详情 →</a> · <a href="https://arxiv.org/abs/2608.18025" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="musp-bench-advanced-multimodal-benchmarking-of-music-underst-2608-28212/">MuSP-Bench: Advanced Multimodal Benchmarking of Music Understanding across Score and Performance</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MuSP-Bench，一个包含490个问题的多模态音乐理解基准，评估前沿模型在乐谱与演奏音频上的表现，发现模型在两者上均存在显著困难。</div>
<div class="card-action">
<a href="musp-bench-advanced-multimodal-benchmarking-of-music-underst-2608-28212/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28212" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="is-prosody-lost-in-translation-fine-grained-cross-lingual-pr-2608-27848/">Is Prosody Lost in Translation? Fine-Grained Cross-Lingual Prosody Similarity Across Languages</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音翻译</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首个细粒度跨语言韵律相似性分析，基于多语言配音数据，揭示不同语言对间韵律结构的关联性，为表达性语音翻译提供指导。</div>
<div class="card-action">
<a href="is-prosody-lost-in-translation-fine-grained-cross-lingual-pr-2608-27848/">详情 →</a> · <a href="https://arxiv.org/abs/2608.27848" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="an-attention-assisted-ai-model-for-real-time-underwater-soun-2502-12817/">An Attention-Assisted AI Model for Real-Time Underwater Sound Speed Estimation Leveraging Remote Sensing Sea Surface Temperature Data</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声速剖面估计</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出自注意力嵌入的多模态融合CNN，利用遥感海表温度和历史声速剖面估计实时水下声速分布，精度和稳定性优于现有方法。</div>
<div class="card-action">
<a href="an-attention-assisted-ai-model-for-real-time-underwater-soun-2502-12817/">详情 →</a> · <a href="https://arxiv.org/abs/2502.12817" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="a-shaky-voice-is-not-always-a-dodge-benchmarking-textual-and-2608-28040/">A Shaky Voice Is Not Always a Dodge: Benchmarking Textual and Vocal Evasion Detection in Earnings Calls</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出DualEvasion基准，用于财报电话会议中文本和语音双模态的规避检测，发现现有模型在语音信心检测上表现不佳。</div>
<div class="card-action">
<a href="a-shaky-voice-is-not-always-a-dodge-benchmarking-textual-and-2608-28040/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28040" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="predicting-turn-taking-outcomes-in-multi-party-conversation--2608-27988/">Predicting Turn-Taking Outcomes in Multi-Party Conversation: Interpretable Modelling of Speech and Gaze Dynamics with Interpersonal Closeness</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#对话分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本研究利用可解释的语音和凝视特征预测四人自由对话中的话轮转换结果（间隙或重叠），并发现凝视特征在噪声条件下具有鲁棒性。</div>
<div class="card-action">
<a href="predicting-turn-taking-outcomes-in-multi-party-conversation--2608-27988/">详情 →</a> · <a href="https://arxiv.org/abs/2608.27988" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="effectiveness-of-iot-and-deep-learning-for-detection-and-sev-2608-27480/">Effectiveness of IoT and Deep Learning for Detection and Severity Assessment of Postelectrotermes militaris in Tea Plantations</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于IoT声学监测与CNN的茶树白蚁侵染检测与严重度评估框架，在真实茶园实现81.5%准确率。</div>
<div class="card-action">
<a href="effectiveness-of-iot-and-deep-learning-for-detection-and-sev-2608-27480/">详情 →</a> · <a href="https://arxiv.org/abs/2608.27480" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
