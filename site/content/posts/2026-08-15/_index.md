---
title: "语音/音频论文速递 2026-08-15"
date: 2026-08-15T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#音频生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">2</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频生成 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #视频到音频生成 | 1篇 | `█████` |
| #语音生成 | 1篇 | `█████` |
| #语音评估 | 1篇 | `█████` |
| #语音病理检测 | 1篇 | `█████` |
| #音频处理 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="voxaudio-vocalized-audio-synthesis-via-multi-reward-autoregr-2608-12951/">VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频生成</span>
</div>
<div class="card-tldr">VoxAudio 提出因果自回归流匹配模型，通过分块因果分解、多奖励微调和带转写标注的语料库，实现语音与环境声融合的可控生成。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hybridsb-moe-dual-domain-schr-odinger-bridges-with-scene-ada-2608-12715/">HybridSB-MoE: Dual-Domain Schr\"odinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出双域Schrödinger桥与场景自适应专家路由的语音增强框架，在VoiceBank+DEMAND上以更少采样步数超越扩散与SB基线。</div>
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
| 🥇 | [VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoreg…](voxaudio-vocalized-audio-synthesis-via-multi-reward-autoregr-2608-12951/) 🎯 | **9.2** | #音频生成 |
| 🥈 | [HybridSB-MoE: Dual-Domain Schr\"odinger Bridges with Scene-A…](hybridsb-moe-dual-domain-schr-odinger-bridges-with-scene-ada-2608-12715/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [ControlFoley: Unified and Controllable Video-to-Audio Genera…](controlfoley-unified-and-controllable-video-to-audio-generat-2604-15086/) | **8.2** | #视频到音频生成 |
| 4. | [CookVoice: Unified Framework for Style Controllable Multi-Mo…](cookvoice-unified-framework-for-style-controllable-multi-mod-2608-11590/) | **8.2** | #语音生成 |
| 5. | [SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic…](sravaani-1-0-scaling-inclusive-speech-recognition-for-indic--2608-08235/) | **8.2** | #语音识别 |
| 6. | [CASA: Content-Acoustic Speaking Assessment with Speech Encod…](casa-content-acoustic-speaking-assessment-with-speech-encode-2608-13101/) | **7.8** | #语音评估 |
| 7. | [Alignment Drift in Single-Model Speculative Decoding for ASR…](alignment-drift-in-single-model-speculative-decoding-for-asr-2608-12703/) | **7.2** | #语音识别 |
| 8. | [Motor, Cognitive, or Corpus? What Survives Cross-Lingual Tra…](motor-cognitive-or-corpus-what-survives-cross-lingual-transf-2608-13425/) | **7.2** | #语音病理检测 |
| 9. | [Drive-to-Music: Context-Aware Generative Audio for In-Vehicl…](drive-to-music-context-aware-generative-audio-for-in-vehicle-2608-12615/) | **6.5** | #音频生成 |
| 10. | [Longest Filled Common Subsequence for Song Identification fr…](longest-filled-common-subsequence-for-song-identification-fr-2509-12261/) | **6.5** | #音频处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="voxaudio-vocalized-audio-synthesis-via-multi-reward-autoregr-2608-12951/">VoxAudio: Vocalized Audio Synthesis via Multi-Reward Autoregressive Flow Matching</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">VoxAudio 提出因果自回归流匹配模型，通过分块因果分解、多奖励微调和带转写标注的语料库，实现语音与环境声融合的可控生成。</div>
<div class="card-action">
<a href="voxaudio-vocalized-audio-synthesis-via-multi-reward-autoregr-2608-12951/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12951" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="hybridsb-moe-dual-domain-schr-odinger-bridges-with-scene-ada-2608-12715/">HybridSB-MoE: Dual-Domain Schr\"odinger Bridges with Scene-Adaptive Expert Routing for Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双域Schrödinger桥与场景自适应专家路由的语音增强框架，在VoiceBank+DEMAND上以更少采样步数超越扩散与SB基线。</div>
<div class="card-action">
<a href="hybridsb-moe-dual-domain-schr-odinger-bridges-with-scene-ada-2608-12715/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12715" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="controlfoley-unified-and-controllable-video-to-audio-generat-2604-15086/">ControlFoley: Unified and Controllable Video-to-Audio Generation with Cross-Modal Conflict Handling</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#视频到音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">ControlFoley提出统一视频到音频生成框架，通过联合视觉编码、时频解耦和模态鲁棒训练，实现文本、视频和参考音频的精细控制，并引入VGGSound-TVC基准评估视觉-文本冲突下的可控性。</div>
<div class="card-action">
<a href="controlfoley-unified-and-controllable-video-to-audio-generat-2604-15086/">详情 →</a> · <a href="https://arxiv.org/abs/2604.15086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="cookvoice-unified-framework-for-style-controllable-multi-mod-2608-11590/">CookVoice: Unified Framework for Style Controllable Multi-Modal Human Voice Generation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">CookVoice提出统一框架，将人声分解为内容、韵律和风格三因子，实现语音与歌声生成、风格控制、声音模仿、转换和编辑等多种任务，仅43.51M参数且支持4步ODE高效推理。</div>
<div class="card-action">
<a href="cookvoice-unified-framework-for-style-controllable-multi-mod-2608-11590/">详情 →</a> · <a href="https://arxiv.org/abs/2608.11590" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="sravaani-1-0-scaling-inclusive-speech-recognition-for-indic--2608-08235/">SraVaani 1.0: Scaling Inclusive Speech Recognition for Indic Languages</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">SraVaani-1.0 是一个覆盖 65 种印度语言和方言的多语言 ASR 模型，通过三阶段训练（自监督预训练、音频-图像对齐、TDT-CTC 微调）在多个基准上取得领先 WER，尤其为低资源语言提供开源识别能力。</div>
<div class="card-action">
<a href="sravaani-1-0-scaling-inclusive-speech-recognition-for-indic--2608-08235/">详情 →</a> · <a href="https://arxiv.org/abs/2608.08235" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="casa-content-acoustic-speaking-assessment-with-speech-encode-2608-13101/">CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CASA，结合Whisper-medium和Qwen3.5-2B，在口语评估中取得SOTA，并分离内容与声学贡献。</div>
<div class="card-action">
<a href="casa-content-acoustic-speaking-assessment-with-speech-encode-2608-13101/">详情 →</a> · <a href="https://arxiv.org/abs/2608.13101" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="alignment-drift-in-single-model-speculative-decoding-for-asr-2608-12703/">Alignment Drift in Single-Model Speculative Decoding for ASR: Mechanism, Correction, and Cost</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文揭示单模型投机解码在ASR中的对齐漂移问题，提出基于验证注意力的位置读取和AnchorDraft训练方法，提升端到端推理速度。</div>
<div class="card-action">
<a href="alignment-drift-in-single-model-speculative-decoding-for-asr-2608-12703/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12703" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="motor-cognitive-or-corpus-what-survives-cross-lingual-transf-2608-13425/">Motor, Cognitive, or Corpus? What Survives Cross-Lingual Transfer in Speech-Based Parkinsons Disease Detection</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音病理检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文通过层分析探究SSL语音模型在跨语种帕金森病检测中的迁移能力，发现层选择依赖语料库，且迁移信号缺乏病理特异性。</div>
<div class="card-action">
<a href="motor-cognitive-or-corpus-what-survives-cross-lingual-transf-2608-13425/">详情 →</a> · <a href="https://arxiv.org/abs/2608.13425" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="drive-to-music-context-aware-generative-audio-for-in-vehicle-2608-12615/">Drive-to-Music: Context-Aware Generative Audio for In-Vehicle Experiences</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">Drive-to-Music 利用行车记录仪图像和车辆遥测数据，实时生成与驾驶场景匹配的音乐，实现个性化车载音频体验。</div>
<div class="card-action">
<a href="drive-to-music-context-aware-generative-audio-for-in-vehicle-2608-12615/">详情 →</a> · <a href="https://arxiv.org/abs/2608.12615" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="longest-filled-common-subsequence-for-song-identification-fr-2509-12261/">Longest Filled Common Subsequence for Song Identification from Degraded Audio via Construct--Merge--Solve--Adapt Optimization</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文提出自适应CMSA框架求解NP难的LFCS问题，在大规模实例上达到SOTA，并首次将LFCS应用于歌曲识别，但音频实验较初步。</div>
<div class="card-action">
<a href="longest-filled-common-subsequence-for-song-identification-fr-2509-12261/">详情 →</a> · <a href="https://arxiv.org/abs/2509.12261" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
