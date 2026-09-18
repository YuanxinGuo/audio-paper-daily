---
title: "语音/音频论文速递 2026-09-18"
date: 2026-09-18T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #音频伪造检测 | 2篇 | `██████████` |
| #目标说话人提取 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #音频诈骗检测 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #关键词识别 | 1篇 | `█████` |
| #音频反欺诈检测 | 1篇 | `█████` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="beyond-the-stability-plasticity-frontier-in-streaming-target-2609-20463/">Beyond the Stability--Plasticity Frontier in Streaming Target Speaker Extraction</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出锚定快权重（AFW）记忆，通过闭环元训练说话人状态动态，突破流式目标说话人提取的稳定性-可塑性前沿。</div>
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
| 🥇 | [Beyond the Stability--Plasticity Frontier in Streaming Targe…](beyond-the-stability-plasticity-frontier-in-streaming-target-2609-20463/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [CoRELoop: Parameter-Efficient Controlled Recurrent Refinemen…](coreloop-parameter-efficient-controlled-recurrent-refinement-2609-19818/) | **7.2** | #音频伪造检测 |
| 🥉 | [Enabling automatic transcription of child-centered audio rec…](enabling-automatic-transcription-of-child-centered-audio-rec-2506-11747/) | **7.0** | #语音识别 |
| 4. | [TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audi…](teleantifraud-2-0-a-refreshable-profile-grounded-and-audio-b-2609-18748/) | **6.8** | #音频诈骗检测 |
| 5. | [Music Hallucination in Audio-Language Models: A Hierarchical…](music-hallucination-in-audio-language-models-a-hierarchical--2609-20195/) | **6.8** | #音频理解 |
| 6. | [Multi-Dimensional Prosody Judgment For Live Streaming Speech…](multi-dimensional-prosody-judgment-for-live-streaming-speech-2609-20124/) | **6.8** | #语音合成 |
| 7. | [CircleMatch: Prototype Matching with Circular Temporal Stati…](circlematch-prototype-matching-with-circular-temporal-statis-2609-20070/) | **6.8** | #关键词识别 |
| 8. | [Robust Workflow Generation via Adversarial Learning for Audi…](robust-workflow-generation-via-adversarial-learning-for-audi-2609-20063/) | **6.8** | #音频伪造检测 |
| 9. | [FRAUDSkill: Structured Frozen-Weight Skill Optimization for …](fraudskill-structured-frozen-weight-skill-optimization-for-a-2609-18766/) | **6.0** | #音频反欺诈检测 |
| 10. | [A Cross-Lingual Acoustic Disease-Alignment Framework for Res…](a-cross-lingual-acoustic-disease-alignment-framework-for-res-2609-19398/) | **6.0** | #语音健康评估 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="beyond-the-stability-plasticity-frontier-in-streaming-target-2609-20463/">Beyond the Stability--Plasticity Frontier in Streaming Target Speaker Extraction</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出锚定快权重（AFW）记忆，通过闭环元训练说话人状态动态，突破流式目标说话人提取的稳定性-可塑性前沿。</div>
<div class="card-action">
<a href="beyond-the-stability-plasticity-frontier-in-streaming-target-2609-20463/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20463" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="coreloop-parameter-efficient-controlled-recurrent-refinement-2609-19818/">CoRELoop: Parameter-Efficient Controlled Recurrent Refinement for Audio Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在冻结的SSL音频深伪检测器上，用轻量循环精炼模块与低秩适配器迭代修正预测，跨域EER从4.85%降至3.74%。</div>
<div class="card-action">
<a href="coreloop-parameter-efficient-controlled-recurrent-refinement-2609-19818/">详情 →</a> · <a href="https://arxiv.org/abs/2609.19818" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="enabling-automatic-transcription-of-child-centered-audio-rec-2506-11747/">Enabling automatic transcription of child-centered audio recordings from real-world environments</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出先检测长时儿童中心录音中可被ASR可靠转写的语音片段，再转写，30%语音上中位WER 0%、均值16%。</div>
<div class="card-action">
<a href="enabling-automatic-transcription-of-child-centered-audio-rec-2506-11747/">详情 →</a> · <a href="https://arxiv.org/abs/2506.11747" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="teleantifraud-2-0-a-refreshable-profile-grounded-and-audio-b-2609-18748/">TeleAntiFraud 2.0: A Refreshable, Profile-Grounded, and Audio-Based Benchmark for Telecom Fraud Detection</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频诈骗检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建可月度冻结更新的电信诈骗音频基准，用近域负样本暴露分类器捷径与预测崩溃问题。</div>
<div class="card-action">
<a href="teleantifraud-2-0-a-refreshable-profile-grounded-and-audio-b-2609-18748/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18748" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="music-hallucination-in-audio-language-models-a-hierarchical--2609-20195/">Music Hallucination in Audio-Language Models: A Hierarchical Formulation and Empirical Study</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">首个针对音频语言模型音乐幻觉的分层多范式实证研究，提出五层感知框架与 MuseDiag 诊断工具，评测九个模型。</div>
<div class="card-action">
<a href="music-hallucination-in-audio-language-models-a-hierarchical--2609-20195/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20195" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="multi-dimensional-prosody-judgment-for-live-streaming-speech-2609-20124/">Multi-Dimensional Prosody Judgment For Live Streaming Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将 Gemini 蒸馏到 Qwen3-Omni 做直播 TTS 多维韵律成对评估，并提出解耦维度判决的 D-LPJ。</div>
<div class="card-action">
<a href="multi-dimensional-prosody-judgment-for-live-streaming-speech-2609-20124/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20124" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="circlematch-prototype-matching-with-circular-temporal-statis-2609-20070/">CircleMatch: Prototype Matching with Circular Temporal Statistics for Tiny Keyword Spotting</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#关键词识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 CircleMatch 原型匹配框架，用无参数循环聚合编码时序，实现约 1k~7k 参数的极小关键词识别模型。</div>
<div class="card-action">
<a href="circlematch-prototype-matching-with-circular-temporal-statis-2609-20070/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20070" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="robust-workflow-generation-via-adversarial-learning-for-audi-2609-20063/">Robust Workflow Generation via Adversarial Learning for Audio Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 ROGUE 双智能体框架，用扰动智能体与策略智能体对抗学习，动态编排多个检测工具以提升音频深伪检测的鲁棒性与泛化性。</div>
<div class="card-action">
<a href="robust-workflow-generation-via-adversarial-learning-for-audi-2609-20063/">详情 →</a> · <a href="https://arxiv.org/abs/2609.20063" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="fraudskill-structured-frozen-weight-skill-optimization-for-a-2609-18766/">FRAUDSkill: Structured Frozen-Weight Skill Optimization for Audio Anti-Fraud Detection</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频反欺诈检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出FRAUDSkill框架，冻结音频语言模型权重，通过外部技能程序与路由策略优化，实现结构化音频反欺诈检测。</div>
<div class="card-action">
<a href="fraudskill-structured-frozen-weight-skill-optimization-for-a-2609-18766/">详情 →</a> · <a href="https://arxiv.org/abs/2609.18766" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="a-cross-lingual-acoustic-disease-alignment-framework-for-res-2609-19398/">A Cross-Lingual Acoustic Disease-Alignment Framework for Respiratory Health Assessment from Spontaneous Speech</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音健康评估</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出CL-DAF跨语言疾病对齐框架，从自发语音中筛选跨语言一致的声学特征，用于COPD等呼吸疾病评估。</div>
<div class="card-action">
<a href="a-cross-lingual-acoustic-disease-alignment-framework-for-res-2609-19398/">详情 →</a> · <a href="https://arxiv.org/abs/2609.19398" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
