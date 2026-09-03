---
title: "语音/音频论文速递 2026-09-03"
date: 2026-09-03T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 3 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 1篇 | `██████████` |
| #语音增强 | 1篇 | `██████████` |
| #噪声事件检测 | 1篇 | `██████████` |
| #语音情感识别 | 1篇 | `██████████` |
| #音频取证 | 1篇 | `██████████` |
| #自动混音 | 1篇 | `██████████` |
| #语音合成 | 1篇 | `██████████` |
| #音频理解 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="removing-speech-keeping-activities-a-privacy-firewall-for-ac-2609-02376/">Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出基于U-Net的隐私防火墙，从环境音频中去除语音而保留活动声音，在合成数据上训练，实现0%可检测语音且保持活动识别性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="vaani-noise-event-dataset-a-curated-spontaneous-speech-datas-2609-02474/">VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#噪声事件检测</span>
</div>
<div class="card-tldr">VAANI噪声事件数据集为105种印度语言的野外自发语音提供细粒度时间戳噪声标注，支持噪声鲁棒ASR、SED和语音增强研究。</div>
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
<a class="card-title" href="binaural-sound-event-localization-and-detection-based-on-hrt-2507-20530/">Binaural Sound Event Localization and Detection based on HRTF Cues for Humanoid Robots</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出双耳声音事件定位与检测任务及合成基准数据集，并设计BTFF特征与CRNN模型BiSELDnet，实现多声源联合检测与定位。</div>
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
| 🥇 | [Binaural Sound Event Localization and Detection based on HRT…](binaural-sound-event-localization-and-detection-based-on-hrt-2507-20530/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [Removing Speech, Keeping Activities: A Privacy Firewall for …](removing-speech-keeping-activities-a-privacy-firewall-for-ac-2609-02376/) 🎯 | **8.2** | #语音增强 |
| 🥉 | [VAANI Noise Event Dataset: A curated spontaneous speech data…](vaani-noise-event-dataset-a-curated-spontaneous-speech-datas-2609-02474/) 🎯 | **8.2** | #噪声事件检测 |
| 4. | [Backdoor Attacks on Speech Emotion Recognition via TTS-Gener…](backdoor-attacks-on-speech-emotion-recognition-via-tts-gener-2606-21052/) | **7.2** | #语音情感识别 |
| 5. | [Half-Truth Audio Detection and Localisation: A Lightweight C…](half-truth-audio-detection-and-localisation-a-lightweight-cr-2605-29531/) | **7.2** | #音频取证 |
| 6. | [Understanding Automatic Mixing: A Subtask-Oriented Analysis …](understanding-automatic-mixing-a-subtask-oriented-analysis-o-2609-02835/) | **7.2** | #自动混音 |
| 7. | [Scalable Direction-Following TTS via Voice Impression-Guided…](scalable-direction-following-tts-via-voice-impression-guided-2609-02623/) | **7.2** | #语音合成 |
| 8. | [Auditory Illusion Benchmark for Large Audio Language Models](auditory-illusion-benchmark-for-large-audio-language-models-2609-02277/) | **7.2** | #音频理解 |
| 9. | [Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Si…](choosing-a-peft-variant-for-per-patient-dysarthric-asr-a-sin-2609-02735/) | **6.8** | #语音识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="binaural-sound-event-localization-and-detection-based-on-hrt-2507-20530/">Binaural Sound Event Localization and Detection based on HRTF Cues for Humanoid Robots</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双耳声音事件定位与检测任务及合成基准数据集，并设计BTFF特征与CRNN模型BiSELDnet，实现多声源联合检测与定位。</div>
<div class="card-action">
<a href="binaural-sound-event-localization-and-detection-based-on-hrt-2507-20530/">详情 →</a> · <a href="https://arxiv.org/abs/2507.20530" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="removing-speech-keeping-activities-a-privacy-firewall-for-ac-2609-02376/">Removing Speech, Keeping Activities: A Privacy Firewall for Acoustic Sensing in Assisted Living</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于U-Net的隐私防火墙，从环境音频中去除语音而保留活动声音，在合成数据上训练，实现0%可检测语音且保持活动识别性能。</div>
<div class="card-action">
<a href="removing-speech-keeping-activities-a-privacy-firewall-for-ac-2609-02376/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02376" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="vaani-noise-event-dataset-a-curated-spontaneous-speech-datas-2609-02474/">VAANI Noise Event Dataset: A curated spontaneous speech dataset annotated with timestamps for noise events</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#噪声事件检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">VAANI噪声事件数据集为105种印度语言的野外自发语音提供细粒度时间戳噪声标注，支持噪声鲁棒ASR、SED和语音增强研究。</div>
<div class="card-action">
<a href="vaani-noise-event-dataset-a-curated-spontaneous-speech-datas-2609-02474/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02474" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="backdoor-attacks-on-speech-emotion-recognition-via-tts-gener-2606-21052/">Backdoor Attacks on Speech Emotion Recognition via TTS-Generated Poisoning</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首次系统研究语音情感识别中的投毒后门攻击，利用TTS生成音频嵌入低能量声学触发器，实现高成功率且隐蔽的攻击。</div>
<div class="card-action">
<a href="backdoor-attacks-on-speech-emotion-recognition-via-tts-gener-2606-21052/">详情 →</a> · <a href="https://arxiv.org/abs/2606.21052" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="half-truth-audio-detection-and-localisation-a-lightweight-cr-2605-29531/">Half-Truth Audio Detection and Localisation: A Lightweight Cross-Attentive Architecture and a Cross-Corpus Diagnostic Study</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频取证</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出轻量级CAFNet模型，融合多特征联合分类半真语音并回归篡改边界，跨语料泛化呈能力依赖而非均匀。</div>
<div class="card-action">
<a href="half-truth-audio-detection-and-localisation-a-lightweight-cr-2605-29531/">详情 →</a> · <a href="https://arxiv.org/abs/2605.29531" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="understanding-automatic-mixing-a-subtask-oriented-analysis-o-2609-02835/">Understanding Automatic Mixing: A Subtask-Oriented Analysis of Two-Stage Mixing System</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#自动混音</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过受控听音实验分析两阶段自动混音系统，验证任务分解对混音质量提升的有效性。</div>
<div class="card-action">
<a href="understanding-automatic-mixing-a-subtask-oriented-analysis-o-2609-02835/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02835" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="scalable-direction-following-tts-via-voice-impression-guided-2609-02623/">Scalable Direction-Following TTS via Voice Impression-Guided Pseudo Triplet Construction</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种可扩展的伪三元组构建流程，利用印象可控TTS和LLM生成方向跟随TTS训练数据，实现说话人保持的风格修改。</div>
<div class="card-action">
<a href="scalable-direction-following-tts-via-voice-impression-guided-2609-02623/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02623" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="auditory-illusion-benchmark-for-large-audio-language-models-2609-02277/">Auditory Illusion Benchmark for Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首个针对大音频语言模型的听觉错觉基准，覆盖音乐、语音等十种错觉，结合人类对照实验揭示模型与人类感知差异。</div>
<div class="card-action">
<a href="auditory-illusion-benchmark-for-large-audio-language-models-2609-02277/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02277" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="choosing-a-peft-variant-for-per-patient-dysarthric-asr-a-sin-2609-02735/">Choosing a PEFT Variant for Per-Patient Dysarthric ASR: A Single-Speaker Case Study on Two ASR Bases</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对构音障碍语音识别，比较七种LoRA变体在单说话人场景下的性能，发现LoRA与DoRA无显著差异，QLoRA效果差，全微调仍最优但LoRA接近。</div>
<div class="card-action">
<a href="choosing-a-peft-variant-for-per-patient-dysarthric-asr-a-sin-2609-02735/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02735" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
