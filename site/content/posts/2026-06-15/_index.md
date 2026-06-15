---
title: "语音/音频论文速递 2026-06-15"
date: 2026-06-15T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#音频问答）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音识别 | 2篇 | `██████████` |
| #音频问答 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #基频估计 | 1篇 | `█████` |
| #音频安全 | 1篇 | `█████` |
| #生物声学 | 1篇 | `█████` |
| #语音识别可解释性 | 1篇 | `█████` |
| #反欺骗检测 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="instantaneous-pitch-estimation-via-wave-u-net-based-fundamen-2606-14324/">Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#基频估计</span>
</div>
<div class="card-tldr">将基波滤波视为语音增强问题，用Wave-U-Net提取基波后计算瞬时频率，实现鲁棒的瞬时基频估计。</div>
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
<a class="card-title" href="leveraging-sound-source-trajectories-for-universal-sound-sep-2409-04843/">Leveraging Sound Source Trajectories for Universal Sound Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出利用声源定位与分离相互促进的迭代框架，通过轨迹细化提升移动声源分离性能。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="spatio-temporal-audio-language-modeling-for-dynamic-sound-so-2606-14141/">Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频问答</span>
</div>
<div class="card-tldr">提出ST-AudioQA数据集和ST-AudioLM模型，实现动态声源的时空音频问答推理。</div>
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
| 🥇 | [Spatio-Temporal Audio Language Modeling for Dynamic Sound So…](spatio-temporal-audio-language-modeling-for-dynamic-sound-so-2606-14141/) 🎯 | **8.8** | #音频问答 |
| 🥈 | [Leveraging Sound Source Trajectories for Universal Sound Sep…](leveraging-sound-source-trajectories-for-universal-sound-sep-2409-04843/) 🎯 | **8.8** | #语音分离 |
| 🥉 | [Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamen…](instantaneous-pitch-estimation-via-wave-u-net-based-fundamen-2606-14324/) 🎯 | **8.5** | #基频估计 |
| 4. | [SARSteer: Safeguarding Large Audio-Language Models via Safe-…](sarsteer-safeguarding-large-audio-language-models-via-safe-a-2510-17633/) | **7.8** | #音频安全 |
| 5. | [Beyond task performance: Decoding bioacoustic embeddings wit…](beyond-task-performance-decoding-bioacoustic-embeddings-with-2606-14662/) | **7.8** | #生物声学 |
| 6. | [Listening with Attention: Entropy-Guided Explainability for …](listening-with-attention-entropy-guided-explainability-for-t-2606-14647/) | **7.8** | #语音识别可解释性 |
| 7. | [From Self-Supervised Speech Models to Mixture-of-Experts for…](from-self-supervised-speech-models-to-mixture-of-experts-for-2606-14639/) | **7.8** | #反欺骗检测 |
| 8. | [MoDiCoL: A Modular Diagnostic Continual Learning Dataset for…](modicol-a-modular-diagnostic-continual-learning-dataset-for--2606-14459/) | **7.2** | #语音识别 |
| 9. | [Learning to Hear Hesitation: Continual Learning for Disfluen…](learning-to-hear-hesitation-continual-learning-for-disfluenc-2606-14391/) | **7.2** | #语音识别 |
| 10. | [AudioDER: A Deduplication-Enhanced Reasoning Dataset for Pos…](audioder-a-deduplication-enhanced-reasoning-dataset-for-post-2606-14591/) | **7.2** | #音频推理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="spatio-temporal-audio-language-modeling-for-dynamic-sound-so-2606-14141/">Spatio-Temporal Audio Language Modeling for Dynamic Sound Sources</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#音频问答</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ST-AudioQA数据集和ST-AudioLM模型，实现动态声源的时空音频问答推理。</div>
<div class="card-action">
<a href="spatio-temporal-audio-language-modeling-for-dynamic-sound-so-2606-14141/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14141" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="leveraging-sound-source-trajectories-for-universal-sound-sep-2409-04843/">Leveraging Sound Source Trajectories for Universal Sound Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出利用声源定位与分离相互促进的迭代框架，通过轨迹细化提升移动声源分离性能。</div>
<div class="card-action">
<a href="leveraging-sound-source-trajectories-for-universal-sound-sep-2409-04843/">详情 →</a> · <a href="https://arxiv.org/abs/2409.04843" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="instantaneous-pitch-estimation-via-wave-u-net-based-fundamen-2606-14324/">Instantaneous Pitch Estimation via Wave-U-Net-Based Fundamental Waveform Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#基频估计</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将基波滤波视为语音增强问题，用Wave-U-Net提取基波后计算瞬时频率，实现鲁棒的瞬时基频估计。</div>
<div class="card-action">
<a href="instantaneous-pitch-estimation-via-wave-u-net-based-fundamen-2606-14324/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14324" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="sarsteer-safeguarding-large-audio-language-models-via-safe-a-2510-17633/">SARSteer: Safeguarding Large Audio-Language Models via Safe-Ablated Refusal Steering</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频安全</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个针对大型音频语言模型的推理时安全防御框架SARSteer，通过文本衍生的拒绝引导和解耦安全空间消融，有效提升有害查询拒绝率同时保持良性响应。</div>
<div class="card-action">
<a href="sarsteer-safeguarding-large-audio-language-models-via-safe-a-2510-17633/">详情 →</a> · <a href="https://arxiv.org/abs/2510.17633" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="beyond-task-performance-decoding-bioacoustic-embeddings-with-2606-14662/">Beyond task performance: Decoding bioacoustic embeddings with speech features</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过回归探针揭示生物声学预训练嵌入编码的语音类声学特征，发现不同模型互补覆盖声学空间，并给出数据驱动的模型选择指南。</div>
<div class="card-action">
<a href="beyond-task-performance-decoding-bioacoustic-embeddings-with-2606-14662/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14662" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="listening-with-attention-entropy-guided-explainability-for-t-2606-14647/">Listening with Attention: Entropy-Guided Explainability for Transformer-Based Audio Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别可解释性</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出LEAF-X框架，结合熵引导注意力加权与多层注意力展开，为Transformer语音识别模型生成忠实且时间精确的解释。</div>
<div class="card-action">
<a href="listening-with-attention-entropy-guided-explainability-for-t-2606-14647/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14647" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="from-self-supervised-speech-models-to-mixture-of-experts-for-2606-14639/">From Self-Supervised Speech Models to Mixture-of-Experts for Robust Anti-Spoofing</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#反欺骗检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将自监督语音模型转换为混合专家架构，提升对未知语音合成方法的泛化能力，在14个欺骗数据集上实现11.9%的EER相对降低。</div>
<div class="card-action">
<a href="from-self-supervised-speech-models-to-mixture-of-experts-for-2606-14639/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14639" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="modicol-a-modular-diagnostic-continual-learning-dataset-for--2606-14459/">MoDiCoL: A Modular Diagnostic Continual Learning Dataset for Robust Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出模块化诊断式持续学习数据集MoDiCoL，用于分析ASR在语言内容、说话人特征和声学环境变化下的鲁棒性。</div>
<div class="card-action">
<a href="modicol-a-modular-diagnostic-continual-learning-dataset-for--2606-14459/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14459" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="learning-to-hear-hesitation-continual-learning-for-disfluenc-2606-14391/">Learning to Hear Hesitation: Continual Learning for Disfluency-Aware ASR</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在预训练ASR模型中引入口吃标记，并通过持续学习在有限数据集上适应口吃语音，避免灾难性遗忘。</div>
<div class="card-action">
<a href="learning-to-hear-hesitation-continual-learning-for-disfluenc-2606-14391/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14391" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="audioder-a-deduplication-enhanced-reasoning-dataset-for-post-2606-14591/">AudioDER: A Deduplication-Enhanced Reasoning Dataset for Post-Training Large Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频推理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出去重增强的音频推理数据集AudioDER，通过声学相似性去重和思维链生成提升LALM后训练效果。</div>
<div class="card-action">
<a href="audioder-a-deduplication-enhanced-reasoning-dataset-for-post-2606-14591/">详情 →</a> · <a href="https://arxiv.org/abs/2606.14591" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
