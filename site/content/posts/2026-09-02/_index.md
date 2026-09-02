---
title: "语音/音频论文速递 2026-09-02"
date: 2026-09-02T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 4 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #语音分离 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |
| #生物声学 | 1篇 | `███` |
| #说话人验证 | 1篇 | `███` |
| #语音识别 | 1篇 | `███` |
| #语音情感识别 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="abse-net-a-lightweight-neural-model-for-active-binaural-spee-2609-00966/">ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出ABSE-NET，将双耳MVDR与轻量级神经网络级联，在开放式助听器中联合增强语音并抑制声泄漏，无需耳内麦克风。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="cleaner-speech-weaker-generalization-revisiting-pitt-derived-2609-00276/">Cleaner Speech, Weaker Generalization: Revisiting Pitt-Derived Benchmarks for Alzheimer's Disease Detection</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">本文系统评估语音增强和数据集筛选对阿尔茨海默病检测的影响，发现增强数据提升域内性能但损害跨域泛化，提示“更干净”的数据集不一定更可靠。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="u-past-a-phase-aware-audio-spectrogram-transformer-u-net-for-2609-00431/">U-PAST: A Phase-Aware Audio Spectrogram Transformer-U-Net for Single-Channel Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出U-PAST，一种在复数谱域进行自注意力建模的Transformer-U-Net混合架构，用于单通道语音增强，在参数效率上优于大型基线。</div>
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
<a class="card-title" href="xvae-wmt-explainable-wavelet-temporal-variational-autoencode-2609-00238/">XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencoder for Blind Source Separation of Heart and Lung Sounds</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出无监督可解释生成式AI模型XVAE-WMT，结合VAE、小波变换和时序一致性损失，实现心音与肺音盲源分离，无需配对干净数据。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="abse-net-a-lightweight-neural-model-for-active-binaural-spee-2609-00966/">ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出ABSE-NET，将双耳MVDR与轻量级神经网络级联，在开放式助听器中联合增强语音并抑制声泄漏，无需耳内麦克风。</div>
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
| 🥇 | [XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencod…](xvae-wmt-explainable-wavelet-temporal-variational-autoencode-2609-00238/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [ABSE-NET: A Lightweight Neural Model for Active Binaural Spe…](abse-net-a-lightweight-neural-model-for-active-binaural-spee-2609-00966/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Cleaner Speech, Weaker Generalization: Revisiting Pitt-Deriv…](cleaner-speech-weaker-generalization-revisiting-pitt-derived-2609-00276/) 🎯 | **8.2** | #语音增强 |
| 4. | [U-PAST: A Phase-Aware Audio Spectrogram Transformer-U-Net fo…](u-past-a-phase-aware-audio-spectrogram-transformer-u-net-for-2609-00431/) 🎯 | **8.2** | #语音增强 |
| 5. | [Phrase-Localized Language-Contrastive Guidance: Training-Fre…](phrase-localized-language-contrastive-guidance-training-free-2609-01016/) | **7.8** | #语音合成 |
| 6. | [Zero-Shot Respiratory Sound Classification through LLM-Augme…](zero-shot-respiratory-sound-classification-through-llm-augme-2609-00055/) | **7.8** | #生物声学 |
| 7. | [A Unified Uncertainty-Aware Back-End for Speaker Verificatio…](a-unified-uncertainty-aware-back-end-for-speaker-verificatio-2609-01221/) | **7.8** | #说话人验证 |
| 8. | [Soft Posterior Speaker Injection for Multi-Talker Speech Rec…](soft-posterior-speaker-injection-for-multi-talker-speech-rec-2609-01287/) | **7.2** | #语音识别 |
| 9. | [VocalAffectBench: Evaluating Vocal Emotion Recognition in AI…](vocalaffectbench-evaluating-vocal-emotion-recognition-in-ai--2608-28932/) | **6.8** | #语音情感识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="xvae-wmt-explainable-wavelet-temporal-variational-autoencode-2609-00238/">XVAE-WMT: Explainable Wavelet-Temporal Variational Autoencoder for Blind Source Separation of Heart and Lung Sounds</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无监督可解释生成式AI模型XVAE-WMT，结合VAE、小波变换和时序一致性损失，实现心音与肺音盲源分离，无需配对干净数据。</div>
<div class="card-action">
<a href="xvae-wmt-explainable-wavelet-temporal-variational-autoencode-2609-00238/">详情 →</a> · <a href="https://arxiv.org/abs/2609.00238" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="abse-net-a-lightweight-neural-model-for-active-binaural-spee-2609-00966/">ABSE-NET: A Lightweight Neural Model for Active Binaural Speech Enhancement in Open-Fit Hearing Aids</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ABSE-NET，将双耳MVDR与轻量级神经网络级联，在开放式助听器中联合增强语音并抑制声泄漏，无需耳内麦克风。</div>
<div class="card-action">
<a href="abse-net-a-lightweight-neural-model-for-active-binaural-spee-2609-00966/">详情 →</a> · <a href="https://arxiv.org/abs/2609.00966" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="cleaner-speech-weaker-generalization-revisiting-pitt-derived-2609-00276/">Cleaner Speech, Weaker Generalization: Revisiting Pitt-Derived Benchmarks for Alzheimer's Disease Detection</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文系统评估语音增强和数据集筛选对阿尔茨海默病检测的影响，发现增强数据提升域内性能但损害跨域泛化，提示“更干净”的数据集不一定更可靠。</div>
<div class="card-action">
<a href="cleaner-speech-weaker-generalization-revisiting-pitt-derived-2609-00276/">详情 →</a> · <a href="https://arxiv.org/abs/2609.00276" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="u-past-a-phase-aware-audio-spectrogram-transformer-u-net-for-2609-00431/">U-PAST: A Phase-Aware Audio Spectrogram Transformer-U-Net for Single-Channel Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出U-PAST，一种在复数谱域进行自注意力建模的Transformer-U-Net混合架构，用于单通道语音增强，在参数效率上优于大型基线。</div>
<div class="card-action">
<a href="u-past-a-phase-aware-audio-spectrogram-transformer-u-net-for-2609-00431/">详情 →</a> · <a href="https://arxiv.org/abs/2609.00431" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="phrase-localized-language-contrastive-guidance-training-free-2609-01016/">Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无训练推理框架LCG，通过短语级语言对比引导和自注意力探测，恢复代码切换语音中外语短语的母语口音，无需微调或外部对齐。</div>
<div class="card-action">
<a href="phrase-localized-language-contrastive-guidance-training-free-2609-01016/">详情 →</a> · <a href="https://arxiv.org/abs/2609.01016" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="zero-shot-respiratory-sound-classification-through-llm-augme-2609-00055/">Zero-Shot Respiratory Sound Classification through LLM-Augmented Audio-Text Alignment</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用医学LLM合成语义锚点，将自监督呼吸音编码器与临床术语对齐，实现零样本呼吸音分类，超越通用音频模型。</div>
<div class="card-action">
<a href="zero-shot-respiratory-sound-classification-through-llm-augme-2609-00055/">详情 →</a> · <a href="https://arxiv.org/abs/2609.00055" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="a-unified-uncertainty-aware-back-end-for-speaker-verificatio-2609-01221/">A Unified Uncertainty-Aware Back-End for Speaker Verification: Scoring, Normalization, and Calibration</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#说话人验证</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一不确定性感知后端，将协方差信息贯穿评分、归一化与校准，提升说话人验证性能。</div>
<div class="card-action">
<a href="a-unified-uncertainty-aware-back-end-for-speaker-verificatio-2609-01221/">详情 →</a> · <a href="https://arxiv.org/abs/2609.01221" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="soft-posterior-speaker-injection-for-multi-talker-speech-rec-2609-01287/">Soft Posterior Speaker Injection for Multi-Talker Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出软后验说话人注入（SPSI），通过轻量头预测帧级说话人后验，以FiLM和记忆提示注入Whisper，降低多说话人语音识别的词错误率。</div>
<div class="card-action">
<a href="soft-posterior-speaker-injection-for-multi-talker-speech-rec-2609-01287/">详情 →</a> · <a href="https://arxiv.org/abs/2609.01287" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="vocalaffectbench-evaluating-vocal-emotion-recognition-in-ai--2608-28932/">VocalAffectBench: Evaluating Vocal Emotion Recognition in AI Audio Models</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">VocalAffectBench是一个公开的语音情感识别测试基准，包含273个音频片段，评估六个基线模型，平均准确率仅35.5%，表明离散情感识别仍不稳健。</div>
<div class="card-action">
<a href="vocalaffectbench-evaluating-vocal-emotion-recognition-in-ai--2608-28932/">详情 →</a> · <a href="https://arxiv.org/abs/2608.28932" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
