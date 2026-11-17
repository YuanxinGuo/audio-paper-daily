---
title: "语音/音频论文速递 2026-11-17"
date: 2026-11-17T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 0 篇 · 最高分 7.8（#语音合成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">7.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 2篇 | `██████████` |
| #语音伪造检测 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #声学-发音反演 | 1篇 | `█████` |
| #音频事件检测 | 1篇 | `█████` |
| #语音表征分析 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #音频隐私审计 | 1篇 | `█████` |

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
| 🥇 | [VoxMel TTS Technical Report](voxmel-tts-technical-report-2611-20254/) | **7.8** | #语音合成 |
| 🥈 | [Progressive Layer-wise Supervision: Deep-to-Shallow Supervis…](progressive-layer-wise-supervision-deep-to-shallow-supervisi-2611-20630/) | **7.8** | #语音伪造检测 |
| 🥉 | [Learning from Distribution: Rethinking One-Hot Supervision f…](learning-from-distribution-rethinking-one-hot-supervision-fo-2611-20436/) | **7.0** | #语音识别 |
| 4. | [Validating Acoustic-to-Articulatory Inversion with Real-Time…](validating-acoustic-to-articulatory-inversion-with-real-time-2611-20432/) | **6.8** | #声学-发音反演 |
| 5. | [Post-fusion Event-aware Time-Frequency Refinement for Audio …](post-fusion-event-aware-time-frequency-refinement-for-audio--2611-20725/) | **6.8** | #音频事件检测 |
| 6. | [No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its…](no-shot-text-to-speech-limitations-of-zero-shot-tts-and-its--2611-20822/) | **6.8** | #语音合成 |
| 7. | [Layer-wise Linear Probing of an Encoder-free Audio-capable L…](layer-wise-linear-probing-of-an-encoder-free-audio-capable-l-2611-20954/) | **6.8** | #语音表征分析 |
| 8. | [Think2Listen: Evidence-Centric Learning For Agentic Audio Un…](think2listen-evidence-centric-learning-for-agentic-audio-und-2611-21083/) | **6.8** | #音频理解 |
| 9. | [AudioTrace: File-Level Membership Detection for Audio Large …](audiotrace-file-level-membership-detection-for-audio-large-l-2611-21088/) | **6.8** | #音频隐私审计 |
| 10. | [Surprise-Gated Memory for Live Speaker Diarization](surprise-gated-memory-for-live-speaker-diarization-2611-20819/) | **6.5** | #说话人日志 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="voxmel-tts-technical-report-2611-20254/">VoxMel TTS Technical Report</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">VoxMel用固定可逆二维Haar变换把Mel分解为Coarse-Mel与两级残差，实现无tokenizer自回归TTS，0.6B模型WER 1.51%。</div>
<div class="card-action">
<a href="voxmel-tts-technical-report-2611-20254/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20254" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="progressive-layer-wise-supervision-deep-to-shallow-supervisi-2611-20630/">Progressive Layer-wise Supervision: Deep-to-Shallow Supervision Annealing for Efficient and Robust Speech Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出逐层监督退火框架PLS，将共享线性分类器挂到每层Transformer，用指数退火权重从深层向浅层转移监督，激活浅层休眠表征，实现SOTA深度伪造检测。</div>
<div class="card-action">
<a href="progressive-layer-wise-supervision-deep-to-shallow-supervisi-2611-20630/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20630" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="learning-from-distribution-rethinking-one-hot-supervision-fo-2611-20436/">Learning from Distribution: Rethinking One-Hot Supervision for ASR and QA in Speech Language Models</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用预训练文本LLM的条件输出分布替代one-hot监督，缓解ASR训练对语音问答能力的损害，同时提升ASR与QA表现。</div>
<div class="card-action">
<a href="learning-from-distribution-rethinking-one-hot-supervision-fo-2611-20436/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20436" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="validating-acoustic-to-articulatory-inversion-with-real-time-2611-20432/">Validating Acoustic-to-Articulatory Inversion with Real-Time MRI: From Vocal-Tract Fidelity to Phonetic Consequences</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声学-发音反演</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用配对rtMRI语音验证WavLM发音反演模型，发现收缩程度预测优于位置，且反演轨迹低估动态范围，擦音/塞擦音合成误差显著。</div>
<div class="card-action">
<a href="validating-acoustic-to-articulatory-inversion-with-real-time-2611-20432/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20432" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="post-fusion-event-aware-time-frequency-refinement-for-audio--2611-20725/">Post-fusion Event-aware Time-Frequency Refinement for Audio Moment Retrieval</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频事件检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 ETR-AMR，在音频-文本融合后加入事件感知时频精炼，用帧门控与频率重加权提升长音频时刻定位精度。</div>
<div class="card-action">
<a href="post-fusion-event-aware-time-frequency-refinement-for-audio--2611-20725/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20725" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="no-shot-text-to-speech-limitations-of-zero-shot-tts-and-its--2611-20822/">No-Shot Text-to-Speech: Limitations of Zero-Shot TTS and its Evaluation Methods in Representing Queer and Transgender Voices</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">评测六个零样本TTS模型对性别多元声音的合成表现，发现自动指标与人类感知不一致。</div>
<div class="card-action">
<a href="no-shot-text-to-speech-limitations-of-zero-shot-tts-and-its--2611-20822/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20822" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="layer-wise-linear-probing-of-an-encoder-free-audio-capable-l-2611-20954/">Layer-wise Linear Probing of an Encoder-free Audio-capable Language Model</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音表征分析</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用线性探针逐层分析 Gemma-4-12B 无编码器音频语言模型，定位声学、音素、副语言信息在 48 层解码器中的可解码深度。</div>
<div class="card-action">
<a href="layer-wise-linear-probing-of-an-encoder-free-audio-capable-l-2611-20954/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20954" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="think2listen-evidence-centric-learning-for-agentic-audio-und-2611-21083/">Think2Listen: Evidence-Centric Learning For Agentic Audio Understanding With LALMS</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出以证据为中心的智能体音频理解框架，让LALM主动调用音频工具获取区分性线索并据此修正候选判断。</div>
<div class="card-action">
<a href="think2listen-evidence-centric-learning-for-agentic-audio-und-2611-21083/">详情 →</a> · <a href="https://arxiv.org/abs/2611.21083" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="audiotrace-file-level-membership-detection-for-audio-large-l-2611-21088/">AudioTrace: File-Level Membership Detection for Audio Large Language Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频隐私审计</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出音频文件级成员推断任务与AudioTraceBench基准，用音频条件代理问题探测音频LLM训练成员，AUROC达0.60。</div>
<div class="card-action">
<a href="audiotrace-file-level-membership-detection-for-audio-large-l-2611-21088/">详情 →</a> · <a href="https://arxiv.org/abs/2611.21088" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="surprise-gated-memory-for-live-speaker-diarization-2611-20819/">Surprise-Gated Memory for Live Speaker Diarization</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">将视觉持续学习中的惊喜门控记忆迁移到在线说话人日志，用冻结DiariZen主干加校准新奇信号门控一次性记忆库。</div>
<div class="card-action">
<a href="surprise-gated-memory-for-live-speaker-diarization-2611-20819/">详情 →</a> · <a href="https://arxiv.org/abs/2611.20819" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
