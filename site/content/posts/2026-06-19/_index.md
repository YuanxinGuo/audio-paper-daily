---
title: "语音/音频论文速递 2026-06-19"
date: 2026-06-19T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#语音增强）"
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
| #语音增强 | 2篇 | `██████████` |
| #语音合成 | 2篇 | `██████████` |
| #音频编辑 | 1篇 | `█████` |
| #音频-语言预训练 | 1篇 | `█████` |
| #语音转换 | 1篇 | `█████` |
| #认知障碍检测 | 1篇 | `█████` |
| #语音属性编辑 | 1篇 | `█████` |
| #语音质量评估 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="time-unconditional-generative-speech-enhancement-via-autonom-2606-20001/">Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出时间无条件的自主整流流框架，去除显式时间步嵌入，提升语音增强质量与推理效率。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="latency-configurable-streaming-speech-enhancement-via-asymme-2606-19688/">Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种通过非对称时间填充和双缓冲流式机制实现可配置延迟的语音增强方法，在极低延迟下达到或超越先前因果SOTA。</div>
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
| 🥇 | [Time-Unconditional Generative Speech Enhancement via Autonom…](time-unconditional-generative-speech-enhancement-via-autonom-2606-20001/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [Latency-Configurable Streaming Speech Enhancement via Asymme…](latency-configurable-streaming-speech-enhancement-via-asymme-2606-19688/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Hybrid Diffusion Transformer for Instruction-Guided Audio Ed…](hybrid-diffusion-transformer-for-instruction-guided-audio-ed-2606-20101/) | **8.2** | #音频编辑 |
| 4. | [FineCombo-TTS: Collaborative and Precise Controllable Speech…](finecombo-tts-collaborative-and-precise-controllable-speech--2606-19209/) | **7.8** | #语音合成 |
| 5. | [MixProLAP: Mixture-Induced Uncertainty Modeling for Probabil…](mixprolap-mixture-induced-uncertainty-modeling-for-probabili-2606-20418/) | **7.8** | #音频-语言预训练 |
| 6. | [Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speak…](zero-vc-zero-lookahead-streaming-voice-conversion-via-speake-2606-20218/) | **7.8** | #语音转换 |
| 7. | [Segment-Level Mandarin Chinese Speech-Based Cognitive Impair…](segment-level-mandarin-chinese-speech-based-cognitive-impair-2606-19996/) | **7.2** | #认知障碍检测 |
| 8. | [RIVET: Robust Idempotent Voice Attribute Editing](rivet-robust-idempotent-voice-attribute-editing-2606-19629/) | **7.2** | #语音属性编辑 |
| 9. | [PrefSQA: Pairwise Preference Prediction for Speech Quality A…](prefsqa-pairwise-preference-prediction-for-speech-quality-as-2606-19597/) | **7.2** | #语音质量评估 |
| 10. | [Exploring Pre-training Benefits on Phoneme Addition through …](exploring-pre-training-benefits-on-phoneme-addition-through--2606-19792/) | **6.5** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="time-unconditional-generative-speech-enhancement-via-autonom-2606-20001/">Time-Unconditional Generative Speech Enhancement via Autonomous Rectified Flow</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出时间无条件的自主整流流框架，去除显式时间步嵌入，提升语音增强质量与推理效率。</div>
<div class="card-action">
<a href="time-unconditional-generative-speech-enhancement-via-autonom-2606-20001/">详情 →</a> · <a href="https://arxiv.org/abs/2606.20001" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="latency-configurable-streaming-speech-enhancement-via-asymme-2606-19688/">Latency-Configurable Streaming Speech Enhancement via Asymmetric Temporal Padding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种通过非对称时间填充和双缓冲流式机制实现可配置延迟的语音增强方法，在极低延迟下达到或超越先前因果SOTA。</div>
<div class="card-action">
<a href="latency-configurable-streaming-speech-enhancement-via-asymme-2606-19688/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19688" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="hybrid-diffusion-transformer-for-instruction-guided-audio-ed-2606-20101/">Hybrid Diffusion Transformer for Instruction-Guided Audio Editing via Rectified Flow</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出混合扩散Transformer架构，通过粗到精的两阶段策略实现高效指令引导音频编辑。</div>
<div class="card-action">
<a href="hybrid-diffusion-transformer-for-instruction-guided-audio-ed-2606-20101/">详情 →</a> · <a href="https://arxiv.org/abs/2606.20101" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="finecombo-tts-collaborative-and-precise-controllable-speech--2606-19209/">FineCombo-TTS: Collaborative and Precise Controllable Speech Synthesis Using Text Descriptions and Reference Speech</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FineCombo-TTS，通过文本描述和参考语音联合控制语音合成，实现灵活精确的声学属性调控。</div>
<div class="card-action">
<a href="finecombo-tts-collaborative-and-precise-controllable-speech--2606-19209/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19209" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="mixprolap-mixture-induced-uncertainty-modeling-for-probabili-2606-20418/">MixProLAP: Mixture-Induced Uncertainty Modeling for Probabilistic Language-Audio Pretraining</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频-语言预训练</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出概率性音频-语言预训练框架MixProLAP，通过混合音频-文本对建模多对多对齐的不确定性，在检索任务上优于确定性基线。</div>
<div class="card-action">
<a href="mixprolap-mixture-induced-uncertainty-modeling-for-probabili-2606-20418/">详情 →</a> · <a href="https://arxiv.org/abs/2606.20418" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="zero-vc-zero-lookahead-streaming-voice-conversion-via-speake-2606-20218/">Zero-VC: Zero-Lookahead Streaming Voice Conversion via Speaker Anonymization</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Zero-VC，利用说话人匿名化作为扰动机制，在零前瞻流式语音转换中平衡音色泄露与效用保持。</div>
<div class="card-action">
<a href="zero-vc-zero-lookahead-streaming-voice-conversion-via-speake-2606-20218/">详情 →</a> · <a href="https://arxiv.org/abs/2606.20218" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="segment-level-mandarin-chinese-speech-based-cognitive-impair-2606-19996/">Segment-Level Mandarin Chinese Speech-Based Cognitive Impairment Detection via an Autoencoder with Contrastive Learning</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#认知障碍检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于自编码器和对比学习的段级语音表征学习框架，用于普通话认知障碍检测，在四个数据集上表现稳定。</div>
<div class="card-action">
<a href="segment-level-mandarin-chinese-speech-based-cognitive-impair-2606-19996/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19996" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="rivet-robust-idempotent-voice-attribute-editing-2606-19629/">RIVET: Robust Idempotent Voice Attribute Editing</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音属性编辑</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出RIVET训练框架，利用幂等性约束提升语音属性编辑模型对标签噪声的鲁棒性。</div>
<div class="card-action">
<a href="rivet-robust-idempotent-voice-attribute-editing-2606-19629/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19629" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="prefsqa-pairwise-preference-prediction-for-speech-quality-as-2606-19597/">PrefSQA: Pairwise Preference Prediction for Speech Quality Assessment and the Critical Role of High Quality Datasets</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音质量评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出PrefSQA，通过偏好预测替代MOS评分进行语音质量评估，并强调高质量偏好数据集的关键作用。</div>
<div class="card-action">
<a href="prefsqa-pairwise-preference-prediction-for-speech-quality-as-2606-19597/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19597" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="exploring-pre-training-benefits-on-phoneme-addition-through--2606-19792/">Exploring Pre-training Benefits on Phoneme Addition through Fine-tuning in Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">探究预训练在语音合成中音素扩展时的作用，发现预训练主要提升自然度，但对新音素识别率帮助有限。</div>
<div class="card-action">
<a href="exploring-pre-training-benefits-on-phoneme-addition-through--2606-19792/">详情 →</a> · <a href="https://arxiv.org/abs/2606.19792" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
