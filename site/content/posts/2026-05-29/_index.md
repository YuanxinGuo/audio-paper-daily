---
title: "语音/音频论文速递 2026-05-29"
date: 2026-05-29T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 8.2（#音频理解）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音乐生成 | 2篇 | `██████████` |
| #音频理解 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #音频分割 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #对话评估 | 1篇 | `█████` |
| #音乐理解 | 1篇 | `█████` |
| #医学音频问答 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<p class="empty-hint">今日无新论文命中，推荐回顾该方向的经典工作：</p>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://ieeexplore.ieee.org/document/6932438" target="_blank" rel="noopener">A Regression Approach to Speech Enhancement Based on Deep Neural Networks</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2015</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">首次系统验证 DNN 直接回归对数功率谱的语音增强范式，奠定后续大量 mask / mapping 方法的基础。</div>
<div class="card-authors">Yong Xu, Jun Du, Li-Rong Dai, Chin-Hui Lee</div>
</div></div>
<div class="paper-card paper-card-classic">
<div class="card-rank">📚</div>
<div class="card-body">
<a class="card-title" href="https://arxiv.org/abs/1809.07454" target="_blank" rel="noopener">Conv-TasNet: Surpassing Ideal Time-Frequency Magnitude Masking</a> <span class="classic-badge">经典</span>
<div class="card-meta">
<span class="card-venue">TASLP 2019</span>
<span class="tag-pill tag-pill-soft">#语音增强</span>
</div>
<div class="card-tldr">时域端到端分离/增强里程碑，证明 1D 卷积可超越 STFT 域 IRM/IBM 上限。</div>
<div class="card-authors">Yi Luo, Nima Mesgarani</div>
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
| 🥇 | [EvA: An Evidence-First Audio Understanding Paradigm for LALM…](eva-an-evidence-first-audio-understanding-paradigm-for-lalms-2603-27667/) | **8.2** | #音频理解 |
| 🥈 | [AG-REPA: Causal Layer Selection for Representation Alignment…](ag-repa-causal-layer-selection-for-representation-alignment--2603-01006/) | **8.2** | #音频生成 |
| 🥉 | [Beyond Transcripts: A Renewed Perspective on Audio Chapterin…](beyond-transcripts-a-renewed-perspective-on-audio-chaptering-2602-08979/) | **7.8** | #音频分割 |
| 4. | [Evaluating and Rewarding LALMs for Expressive Role-Play TTS …](evaluating-and-rewarding-lalms-for-expressive-role-play-tts--2601-22661/) | **7.8** | #语音合成 |
| 5. | [SegTune: Structured and Fine-Grained Control for Song Genera…](segtune-structured-and-fine-grained-control-for-song-generat-2510-18416/) | **7.8** | #音乐生成 |
| 6. | [GrowLoop: Self-Evolving Conversation Evaluation Seeded by Hu…](growloop-self-evolving-conversation-evaluation-seeded-by-hum-2605-28882/) | **7.8** | #对话评估 |
| 7. | [MusTBENCH: Benchmarking and Advancing Temporal Grounding in …](mustbench-benchmarking-and-advancing-temporal-grounding-in-m-2605-29300/) | **7.5** | #音乐理解 |
| 8. | [MedMosaic: A Challenging Large Scale Benchmark of Diverse Me…](medmosaic-a-challenging-large-scale-benchmark-of-diverse-med-2605-00969/) | **7.2** | #医学音频问答 |
| 9. | [BEAT: Tokenizing and Generating Symbolic Music by Uniform Te…](beat-tokenizing-and-generating-symbolic-music-by-uniform-tem-2604-19532/) | **7.2** | #音乐生成 |
| 10. | [AV-EMO-Reasoning: Benchmarking Emotional Reasoning Capabilit…](av-emo-reasoning-benchmarking-emotional-reasoning-capabiliti-2510-07355/) | **6.5** | #情感推理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="eva-an-evidence-first-audio-understanding-paradigm-for-lalms-2603-27667/">EvA: An Evidence-First Audio Understanding Paradigm for LALMs</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出EvA双路径架构，通过层次聚合和非压缩时间对齐融合增强声学证据保留，在MMAU等基准上取得最佳开源感知结果。</div>
<div class="card-action">
<a href="eva-an-evidence-first-audio-understanding-paradigm-for-lalms-2603-27667/">详情 →</a> · <a href="https://arxiv.org/abs/2603.27667" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="ag-repa-causal-layer-selection-for-representation-alignment--2603-01006/">AG-REPA: Causal Layer Selection for Representation Alignment in Audio Flow Matching</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AG-REPA，一种因果层选择策略，用于音频流匹配中的表示对齐，通过前向门控消融量化各层对速度场的因果贡献，优于传统REPA。</div>
<div class="card-action">
<a href="ag-repa-causal-layer-selection-for-representation-alignment--2603-01006/">详情 →</a> · <a href="https://arxiv.org/abs/2603.01006" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="beyond-transcripts-a-renewed-perspective-on-audio-chaptering-2602-08979/">Beyond Transcripts: A Renewed Perspective on Audio Chaptering</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频分割</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音频章节分割任务，对比文本、纯音频和多模态方法，发现纯音频模型AudioSeg优于文本方法，多模态大模型受限于上下文长度。</div>
<div class="card-action">
<a href="beyond-transcripts-a-renewed-perspective-on-audio-chaptering-2602-08979/">详情 →</a> · <a href="https://arxiv.org/abs/2602.08979" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="evaluating-and-rewarding-lalms-for-expressive-role-play-tts--2601-22661/">Evaluating and Rewarding LALMs for Expressive Role-Play TTS via Mean Continuation Log-Probability</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MCLP指标用于评估和优化角色扮演TTS的风格一致性，并作为强化学习奖励提升表现。</div>
<div class="card-action">
<a href="evaluating-and-rewarding-lalms-for-expressive-role-play-tts--2601-22661/">详情 →</a> · <a href="https://arxiv.org/abs/2601.22661" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="segtune-structured-and-fine-grained-control-for-song-generat-2510-18416/">SegTune: Structured and Fine-Grained Control for Song Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SegTune，一种非自回归框架，通过段级文本提示实现歌曲的结构化细粒度控制，并引入LLM时长预测器实现歌词与音乐精确对齐。</div>
<div class="card-action">
<a href="segtune-structured-and-fine-grained-control-for-song-generat-2510-18416/">详情 →</a> · <a href="https://arxiv.org/abs/2510.18416" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="growloop-self-evolving-conversation-evaluation-seeded-by-hum-2605-28882/">GrowLoop: Self-Evolving Conversation Evaluation Seeded by Human</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#对话评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出GrowLoop，一种自进化的对话评估系统，通过少量人工种子标注和启发式学习持续优化评估准则，实现与人类判断高度对齐。</div>
<div class="card-action">
<a href="growloop-self-evolving-conversation-evaluation-seeded-by-hum-2605-28882/">详情 →</a> · <a href="https://arxiv.org/abs/2605.28882" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="mustbench-benchmarking-and-advancing-temporal-grounding-in-m-2605-29300/">MusTBENCH: Benchmarking and Advancing Temporal Grounding in Music LLMs</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音乐理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MusTBENCH基准测试音乐大模型的时间定位能力，并设计MusT四阶段优化方案显著提升性能。</div>
<div class="card-action">
<a href="mustbench-benchmarking-and-advancing-temporal-grounding-in-m-2605-29300/">详情 →</a> · <a href="https://arxiv.org/abs/2605.29300" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="medmosaic-a-challenging-large-scale-benchmark-of-diverse-med-2605-00969/">MedMosaic: A Challenging Large Scale Benchmark of Diverse Medical Audio</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#医学音频问答</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MedMosaic是一个大规模医学音频问答基准，包含多种音频类型和46,701个问答对，评估13个模型发现推理仍具挑战。</div>
<div class="card-action">
<a href="medmosaic-a-challenging-large-scale-benchmark-of-diverse-med-2605-00969/">详情 →</a> · <a href="https://arxiv.org/abs/2605.00969" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="beat-tokenizing-and-generating-symbolic-music-by-uniform-tem-2604-19532/">BEAT: Tokenizing and Generating Symbolic Music by Uniform Temporal Steps</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出BEAT分词法，以均匀节拍步长编码符号音乐，提升生成质量与结构连贯性。</div>
<div class="card-action">
<a href="beat-tokenizing-and-generating-symbolic-music-by-uniform-tem-2604-19532/">详情 →</a> · <a href="https://arxiv.org/abs/2604.19532" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="av-emo-reasoning-benchmarking-emotional-reasoning-capabiliti-2510-07355/">AV-EMO-Reasoning: Benchmarking Emotional Reasoning Capabilities in Omni-modal LLMS with Audio-visual Cues</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#情感推理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出AV-EMO-Reasoning基准，系统评估全模态大语言模型在音频-视觉线索下的情感推理能力。</div>
<div class="card-action">
<a href="av-emo-reasoning-benchmarking-emotional-reasoning-capabiliti-2510-07355/">详情 →</a> · <a href="https://arxiv.org/abs/2510.07355" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
