---
title: "语音/音频论文速递 2026-10-09"
date: 2026-10-09T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 8.5（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 2篇 | `██████████` |
| #语音分离 | 2篇 | `██████████` |
| #语音增强 | 1篇 | `█████` |
| #音频-视觉事件定位 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #语音对话系统 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="prolombard-structured-multi-scale-modeling-for-normal-to-lom-2609-04828/">ProLombard: Structured Multi-Scale Modeling for Normal-to-Lombard Speech Conversion</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">ProLombard 用语句-音素-帧三级多尺度建模做正常语音到 Lombard 语音转换，通过 ASE 与音素级解耦提升可懂度与音质。</div>
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
<a class="card-title" href="smoothconv-and-duplexconv-complementary-mandarin-multi-party-2610-11150/">SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">发布 SmoothConv 与 DuplexConv 两个共 2100 小时中文多方对话语料，含同步说话人级音轨与细粒度标注，并给出分离/MSASR/轮次检测基准。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="egovoice-proactive-spoken-assistance-from-egocentric-multimo-2610-12248/">EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">构建第一人称多模态流下的主动语音助手框架，用语音分离与重合成清洗HoloAssist音频，微调全模态LLM并用DPO优化干预时机。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="midashenglm-spatial-unifying-general-audio-understanding-and-2610-11156/">MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">小米提出首个开源统一音频语言模型 MiDashengLM-Spatial，通过 Spatial-Dasheng 编码器与语义-空间分层条件模块，同时支持通用音频理解与空间感知。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="savu-bench-a-real-world-benchmark-for-spatial-audio-visual-u-2610-10624/">SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual Understanding</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出真实场景音视频空间理解基准 SAVU-Bench，含七项任务与诊断集，发现音频空间感知是主要瓶颈。</div>
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
| 🥇 | [MiDashengLM-Spatial: Unifying General Audio Understanding an…](midashenglm-spatial-unifying-general-audio-understanding-and-2610-11156/) 🎯 | **8.5** | #双耳音频 |
| 🥈 | [ProLombard: Structured Multi-Scale Modeling for Normal-to-Lo…](prolombard-structured-multi-scale-modeling-for-normal-to-lom-2609-04828/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [SmoothConv and DuplexConv: Complementary Mandarin Multi-Part…](smoothconv-and-duplexconv-complementary-mandarin-multi-party-2610-11150/) 🎯 | **8.0** | #语音分离 |
| 4. | [SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual …](savu-bench-a-real-world-benchmark-for-spatial-audio-visual-u-2610-10624/) 🎯 | **7.8** | #双耳音频 |
| 5. | [EgoVoice: Proactive Spoken Assistance from Egocentric Multim…](egovoice-proactive-spoken-assistance-from-egocentric-multimo-2610-12248/) 🎯 | **7.5** | #语音分离 |
| 6. | [Open-Vocabulary Audio-Visual Event Localization via Complex-…](open-vocabulary-audio-visual-event-localization-via-complex--2610-11846/) | **7.0** | #音频-视觉事件定位 |
| 7. | [Self-Supervised Speech Representations for Cross-Speaker Dys…](self-supervised-speech-representations-for-cross-speaker-dys-2610-11825/) | **6.8** | #语音识别 |
| 8. | [Beyond Speech Captions: Speech-Rewarded Style Planning for C…](beyond-speech-captions-speech-rewarded-style-planning-for-co-2610-11461/) | **6.8** | #语音合成 |
| 9. | [Breaking the Group Size Barrier: Parameter-Efficient Group D…](breaking-the-group-size-barrier-parameter-efficient-group-da-2610-11237/) | **6.0** | #音乐生成 |
| 10. | [DuplexAgent-RSI: Recursive Harness Improvement for Full-Dupl…](duplexagent-rsi-recursive-harness-improvement-for-full-duple-2610-11299/) | **5.5** | #语音对话系统 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="midashenglm-spatial-unifying-general-audio-understanding-and-2610-11156/">MiDashengLM-Spatial: Unifying General Audio Understanding and Spatial Awareness</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">小米提出首个开源统一音频语言模型 MiDashengLM-Spatial，通过 Spatial-Dasheng 编码器与语义-空间分层条件模块，同时支持通用音频理解与空间感知。</div>
<div class="card-action">
<a href="midashenglm-spatial-unifying-general-audio-understanding-and-2610-11156/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11156" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="prolombard-structured-multi-scale-modeling-for-normal-to-lom-2609-04828/">ProLombard: Structured Multi-Scale Modeling for Normal-to-Lombard Speech Conversion</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">ProLombard 用语句-音素-帧三级多尺度建模做正常语音到 Lombard 语音转换，通过 ASE 与音素级解耦提升可懂度与音质。</div>
<div class="card-action">
<a href="prolombard-structured-multi-scale-modeling-for-normal-to-lom-2609-04828/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04828" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="smoothconv-and-duplexconv-complementary-mandarin-multi-party-2610-11150/">SmoothConv and DuplexConv: Complementary Mandarin Multi-Party Conversational Speech Corpora for Speech Interaction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发布 SmoothConv 与 DuplexConv 两个共 2100 小时中文多方对话语料，含同步说话人级音轨与细粒度标注，并给出分离/MSASR/轮次检测基准。</div>
<div class="card-action">
<a href="smoothconv-and-duplexconv-complementary-mandarin-multi-party-2610-11150/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11150" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="savu-bench-a-real-world-benchmark-for-spatial-audio-visual-u-2610-10624/">SAVU-BENCH: A Real-World Benchmark for Spatial Audio-Visual Understanding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出真实场景音视频空间理解基准 SAVU-Bench，含七项任务与诊断集，发现音频空间感知是主要瓶颈。</div>
<div class="card-action">
<a href="savu-bench-a-real-world-benchmark-for-spatial-audio-visual-u-2610-10624/">详情 →</a> · <a href="https://arxiv.org/abs/2610.10624" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="egovoice-proactive-spoken-assistance-from-egocentric-multimo-2610-12248/">EgoVoice: Proactive Spoken Assistance from Egocentric Multimodal Streams</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建第一人称多模态流下的主动语音助手框架，用语音分离与重合成清洗HoloAssist音频，微调全模态LLM并用DPO优化干预时机。</div>
<div class="card-action">
<a href="egovoice-proactive-spoken-assistance-from-egocentric-multimo-2610-12248/">详情 →</a> · <a href="https://arxiv.org/abs/2610.12248" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="open-vocabulary-audio-visual-event-localization-via-complex--2610-11846/">Open-Vocabulary Audio-Visual Event Localization via Complex-Valued Fusion</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频-视觉事件定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用复值神经网络融合音视频相似度，在开放词汇音视频事件定位任务上取得SOTA。</div>
<div class="card-action">
<a href="open-vocabulary-audio-visual-event-localization-via-complex--2610-11846/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11846" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="self-supervised-speech-representations-for-cross-speaker-dys-2610-11825/">Self-Supervised Speech Representations for Cross-Speaker Dysarthria Detection During Awake Craniotomy</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在清醒开颅手术录音上系统评估语音表征与分类器对构音障碍检测的影响，发现多层wav2vec 2.0表征比分类器选择更关键。</div>
<div class="card-action">
<a href="self-supervised-speech-representations-for-cross-speaker-dys-2610-11825/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11825" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="beyond-speech-captions-speech-rewarded-style-planning-for-co-2610-11461/">Beyond Speech Captions: Speech-Rewarded Style Planning for Conversational Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用冻结TTS模型的语音token似然作奖励，通过GRPO训练文本风格规划器，提升对话TTS的风格与情感相似度。</div>
<div class="card-action">
<a href="beyond-speech-captions-speech-rewarded-style-planning-for-co-2610-11461/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11461" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="breaking-the-group-size-barrier-parameter-efficient-group-da-2610-11237/">Breaking the Group Size Barrier: Parameter-Efficient Group Dance Generation with Chain-of-Dancers</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">ChainDance 将群舞生成分解为逐舞者条件链式生成，用冻结单人扩散骨干加两个轻量模块，支持可变群组规模。</div>
<div class="card-action">
<a href="breaking-the-group-size-barrier-parameter-efficient-group-da-2610-11237/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11237" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="duplexagent-rsi-recursive-harness-improvement-for-full-duple-2610-11299/">DuplexAgent-RSI: Recursive Harness Improvement for Full-Duplex Voice Agent Collaboration</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#语音对话系统</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出DuplexAgent全双工语音协作系统，用六个可编辑模块编排对话与异步委派，并以Duplex-Harness-RSI闭环从交互轨迹自动修复模块。</div>
<div class="card-action">
<a href="duplexagent-rsi-recursive-harness-improvement-for-full-duple-2610-11299/">详情 →</a> · <a href="https://arxiv.org/abs/2610.11299" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
