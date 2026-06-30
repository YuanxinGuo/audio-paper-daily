---
title: "语音/音频论文速递 2026-06-30"
date: 2026-06-30T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 9.2（#语音分离）"
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
| #语音分离 | 1篇 | `██████████` |
| #目标说话人提取 | 1篇 | `██████████` |
| #双耳音频 | 1篇 | `██████████` |
| #音频-视频生成 | 1篇 | `██████████` |
| #语音匿名化 | 1篇 | `██████████` |
| #视听连续测试时适应 | 1篇 | `██████████` |
| #声源定位 | 1篇 | `██████████` |
| #和弦识别 | 1篇 | `██████████` |

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
<a class="card-title" href="position-aware-target-speaker-extraction-for-long-form-multi-2606-29497/">Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出PATSE，利用DOA作为空间先验，在长对话中直接提取目标说话人语音，无需显式说话人日志，提升ASR性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="child-centric-voice-anonymization-in-single-and-multi-speake-2606-29897/">Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音匿名化</span>
</div>
<div class="card-tldr">针对儿童语音的匿名化系统，通过域自适应SSL模型在单说话人和多说话人场景下提升可懂度和感知质量，同时保持强隐私保护。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="tf-moe-time-frequency-mixture-of-experts-for-efficient-speec-2606-29575/">TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出TF-MoE，在mel频带分割Conformer中引入时-频交替稀疏MoE，以几乎不增加推理成本提升语音分离性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="position-aware-target-speaker-extraction-for-long-form-multi-2606-29497/">Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出PATSE，利用DOA作为空间先验，在长对话中直接提取目标说话人语音，无需显式说话人日志，提升ASR性能。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="evaluation-of-head-related-transfer-functions-across-five-le-2606-30114/">Evaluation of Head-Related Transfer Functions Across Five Levels of Individualisation in Virtual Reality</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">在VR中比较五种不同个性化程度的HRTF对声源定位的影响，发现高分辨率合成HRTF可媲美实测，而摄影测量合成HRTF和KEMAR性能最差。</div>
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
| 🥇 | [TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Spee…](tf-moe-time-frequency-mixture-of-experts-for-efficient-speec-2606-29575/) 🎯 | **9.2** | #语音分离 |
| 🥈 | [Position-Aware Target Speaker Extraction for Long-Form Multi…](position-aware-target-speaker-extraction-for-long-form-multi-2606-29497/) 🎯 | **8.8** | #目标说话人提取 |
| 🥉 | [Evaluation of Head-Related Transfer Functions Across Five Le…](evaluation-of-head-related-transfer-functions-across-five-le-2606-30114/) 🎯 | **8.5** | #双耳音频 |
| 4. | [Unison: Harmonizing Motion, Speech, and Sound for Human-Cent…](unison-harmonizing-motion-speech-and-sound-for-human-centric-2605-08729/) | **8.2** | #音频-视频生成 |
| 5. | [Child-Centric Voice Anonymization in Single and Multi-Speake…](child-centric-voice-anonymization-in-single-and-multi-speake-2606-29897/) 🎯 | **8.2** | #语音匿名化 |
| 6. | [Audio-Visual Continual Test-Time Adaptation without Forgetti…](audio-visual-continual-test-time-adaptation-without-forgetti-2602-18528/) | **7.8** | #视听连续测试时适应 |
| 7. | [NeuralMUSIC: A Hybrid Neural-Subspace Framework for Robot So…](neuralmusic-a-hybrid-neural-subspace-framework-for-robot-sou-2606-18664/) | **7.8** | #声源定位 |
| 8. | [Enhancing Automatic Chord Recognition via Pseudo-Labeling an…](enhancing-automatic-chord-recognition-via-pseudo-labeling-an-2602-19778/) | **7.8** | #和弦识别 |
| 9. | [ORCA: Open-ended Response Correctness Assessment for Audio Q…](orca-open-ended-response-correctness-assessment-for-audio-qu-2512-09066/) | **7.8** | #音频问答评估 |
| 10. | [Few-Shot Synthetic Accented Speech for ASR Fine-Tuning: What…](few-shot-synthetic-accented-speech-for-asr-fine-tuning-what--2604-27273/) | **7.2** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="tf-moe-time-frequency-mixture-of-experts-for-efficient-speec-2606-29575/">TF-MoE: Time-Frequency Mixture-of-Experts for Efficient Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出TF-MoE，在mel频带分割Conformer中引入时-频交替稀疏MoE，以几乎不增加推理成本提升语音分离性能。</div>
<div class="card-action">
<a href="tf-moe-time-frequency-mixture-of-experts-for-efficient-speec-2606-29575/">详情 →</a> · <a href="https://arxiv.org/abs/2606.29575" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="position-aware-target-speaker-extraction-for-long-form-multi-2606-29497/">Position-Aware Target Speaker Extraction for Long-Form Multi-Party Conversations: A Diarization-Free Framework for ASR</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出PATSE，利用DOA作为空间先验，在长对话中直接提取目标说话人语音，无需显式说话人日志，提升ASR性能。</div>
<div class="card-action">
<a href="position-aware-target-speaker-extraction-for-long-form-multi-2606-29497/">详情 →</a> · <a href="https://arxiv.org/abs/2606.29497" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="evaluation-of-head-related-transfer-functions-across-five-le-2606-30114/">Evaluation of Head-Related Transfer Functions Across Five Levels of Individualisation in Virtual Reality</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在VR中比较五种不同个性化程度的HRTF对声源定位的影响，发现高分辨率合成HRTF可媲美实测，而摄影测量合成HRTF和KEMAR性能最差。</div>
<div class="card-action">
<a href="evaluation-of-head-related-transfer-functions-across-five-le-2606-30114/">详情 →</a> · <a href="https://arxiv.org/abs/2606.30114" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="unison-harmonizing-motion-speech-and-sound-for-human-centric-2605-08729/">Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video Generation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频-视频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Unison统一框架，通过语义引导的音频解耦和双向跨模态强制策略，实现人体中心视频中运动、语音和音效的协同生成。</div>
<div class="card-action">
<a href="unison-harmonizing-motion-speech-and-sound-for-human-centric-2605-08729/">详情 →</a> · <a href="https://arxiv.org/abs/2605.08729" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="child-centric-voice-anonymization-in-single-and-multi-speake-2606-29897/">Child-Centric Voice Anonymization in Single and Multi-Speaker Speech via Domain-Adapted SSL Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音匿名化</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">针对儿童语音的匿名化系统，通过域自适应SSL模型在单说话人和多说话人场景下提升可懂度和感知质量，同时保持强隐私保护。</div>
<div class="card-action">
<a href="child-centric-voice-anonymization-in-single-and-multi-speake-2606-29897/">详情 →</a> · <a href="https://arxiv.org/abs/2606.29897" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="audio-visual-continual-test-time-adaptation-without-forgetti-2602-18528/">Audio-Visual Continual Test-Time Adaptation without Forgetting</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#视听连续测试时适应</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AVReCAP方法，通过选择性参数检索机制动态调整融合层参数，在视听连续测试时适应中缓解灾难性遗忘，无需源数据。</div>
<div class="card-action">
<a href="audio-visual-continual-test-time-adaptation-without-forgetti-2602-18528/">详情 →</a> · <a href="https://arxiv.org/abs/2602.18528" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="neuralmusic-a-hybrid-neural-subspace-framework-for-robot-sou-2606-18664/">NeuralMUSIC: A Hybrid Neural-Subspace Framework for Robot Sound Source Localization</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#声源定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出NeuralMUSIC混合框架，用神经网络估计空间协方差矩阵，结合经典MUSIC算法和频率注意力融合模块，实现鲁棒的机器人声源定位。</div>
<div class="card-action">
<a href="neuralmusic-a-hybrid-neural-subspace-framework-for-robot-sou-2606-18664/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18664" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="enhancing-automatic-chord-recognition-via-pseudo-labeling-an-2602-19778/">Enhancing Automatic Chord Recognition via Pseudo-Labeling and Knowledge Distillation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#和弦识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两阶段训练流程，利用预训练模型生成伪标签并配合知识蒸馏，在无标签数据上训练学生模型，最终超越教师模型和监督基线。</div>
<div class="card-action">
<a href="enhancing-automatic-chord-recognition-via-pseudo-labeling-an-2602-19778/">详情 →</a> · <a href="https://arxiv.org/abs/2602.19778" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="orca-open-ended-response-correctness-assessment-for-audio-qu-2512-09066/">ORCA: Open-ended Response Correctness Assessment for Audio Question Answering</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频问答评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ORCA，一种轻量级模型，用于评估大音频语言模型在开放音频问答中的回答正确性，并建模人类分歧。</div>
<div class="card-action">
<a href="orca-open-ended-response-correctness-assessment-for-audio-qu-2512-09066/">详情 →</a> · <a href="https://arxiv.org/abs/2512.09066" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="few-shot-synthetic-accented-speech-for-asr-fine-tuning-what--2604-27273/">Few-Shot Synthetic Accented Speech for ASR Fine-Tuning: What Helps and When?</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">探究合成口音语音对ASR微调的有效性，发现随机音素扰动即可获得大部分收益，真实口音音素和韵律增益有限。</div>
<div class="card-action">
<a href="few-shot-synthetic-accented-speech-for-asr-fine-tuning-what--2604-27273/">详情 →</a> · <a href="https://arxiv.org/abs/2604.27273" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
