---
title: "语音/音频论文速递 2026-06-08"
date: 2026-06-08T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 2 篇 · 最高分 9.2（#多模态世界模型）"
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
| #多模态世界模型 | 1篇 | `██████████` |
| #听觉注意力解码 | 1篇 | `██████████` |
| #语音识别 | 1篇 | `██████████` |
| #音频编辑 | 1篇 | `██████████` |
| #语音情感转换 | 1篇 | `██████████` |
| #语音克隆 | 1篇 | `██████████` |
| #音频生成 | 1篇 | `██████████` |
| #语音情感识别 | 1篇 | `██████████` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ca-tcn-a-causal-anticausal-temporal-convolutional-network-fo-2603-26394/">CA-TCN: A Causal-Anticausal Temporal Convolutional Network for Direct Auditory Attention Decoding</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#听觉注意力解码</span>
</div>
<div class="card-tldr">提出CA-TCN，一种因果-反因果时间卷积网络，直接从EEG信号分类注意说话人，在多个数据集上提升解码准确率0.5%-3.2%。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="audio-visual-world-models-grounding-multisensory-imagination-2512-00883/">Audio-Visual World Models: Grounding Multisensory Imagination for Embodied Agents</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#多模态世界模型</span>
</div>
<div class="card-tldr">提出音频-视觉世界模型AVWM，通过条件扩散Transformer联合预测双耳音频与视觉未来帧，并验证其在具身导航中的实用性。</div>
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
| 🥇 | [Audio-Visual World Models: Grounding Multisensory Imaginatio…](audio-visual-world-models-grounding-multisensory-imagination-2512-00883/) 🎯 | **9.2** | #多模态世界模型 |
| 🥈 | [CA-TCN: A Causal-Anticausal Temporal Convolutional Network f…](ca-tcn-a-causal-anticausal-temporal-convolutional-network-fo-2603-26394/) 🎯 | **8.8** | #听觉注意力解码 |
| 🥉 | [Whisper Hallucination Detection and Mitigation via Hidden Re…](whisper-hallucination-detection-and-mitigation-via-hidden-re-2606-07473/) | **8.2** | #语音识别 |
| 4. | [DirectAudioEdit: Inversion-Free Text-Guided Audio Editing vi…](directaudioedit-inversion-free-text-guided-audio-editing-via-2606-07356/) | **7.8** | #音频编辑 |
| 5. | [TargetSEC: Plug-and-Play In-the-Wild Speech Emotion Conversi…](targetsec-plug-and-play-in-the-wild-speech-emotion-conversio-2606-07293/) | **7.8** | #语音情感转换 |
| 6. | [KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 202…](kit-s-submission-to-cross-lingual-voice-cloning-in-iwslt-202-2606-07240/) | **7.2** | #语音克隆 |
| 7. | [Audio-Oscar: A Multi-Agent System for Complex Audio Scene Ge…](audio-oscar-a-multi-agent-system-for-complex-audio-scene-gen-2606-07397/) | **7.2** | #音频生成 |
| 8. | [Acoustic Cue Alignment in Audio Language Models for Speech E…](acoustic-cue-alignment-in-audio-language-models-for-speech-e-2606-07309/) | **7.2** | #语音情感识别 |
| 9. | [How Far Can Chord-Symbol Time-Series Adaptation Carry Genre …](how-far-can-chord-symbol-time-series-adaptation-carry-genre--2606-07334/) | **6.8** | #音乐信息检索 |
| 10. | [Where Rectified Flows Leak: Characterising Membership Signal…](where-rectified-flows-leak-characterising-membership-signals-2606-07271/) | **6.5** | #生成模型安全 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="audio-visual-world-models-grounding-multisensory-imagination-2512-00883/">Audio-Visual World Models: Grounding Multisensory Imagination for Embodied Agents</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#多模态世界模型</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音频-视觉世界模型AVWM，通过条件扩散Transformer联合预测双耳音频与视觉未来帧，并验证其在具身导航中的实用性。</div>
<div class="card-action">
<a href="audio-visual-world-models-grounding-multisensory-imagination-2512-00883/">详情 →</a> · <a href="https://arxiv.org/abs/2512.00883" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="ca-tcn-a-causal-anticausal-temporal-convolutional-network-fo-2603-26394/">CA-TCN: A Causal-Anticausal Temporal Convolutional Network for Direct Auditory Attention Decoding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#听觉注意力解码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CA-TCN，一种因果-反因果时间卷积网络，直接从EEG信号分类注意说话人，在多个数据集上提升解码准确率0.5%-3.2%。</div>
<div class="card-action">
<a href="ca-tcn-a-causal-anticausal-temporal-convolutional-network-fo-2603-26394/">详情 →</a> · <a href="https://arxiv.org/abs/2603.26394" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="whisper-hallucination-detection-and-mitigation-via-hidden-re-2606-07473/">Whisper Hallucination Detection and Mitigation via Hidden Representation Steering and Sparse AutoEncoders</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用Whisper内部表示和稀疏自编码器检测并缓解ASR幻觉，将幻觉率从72.63%降至14.11%。</div>
<div class="card-action">
<a href="whisper-hallucination-detection-and-mitigation-via-hidden-re-2606-07473/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07473" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="directaudioedit-inversion-free-text-guided-audio-editing-via-2606-07356/">DirectAudioEdit: Inversion-Free Text-Guided Audio Editing via Diffusion Prediction Contrast</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个免训练免反演的文本引导音频编辑方法，通过扩散预测对比实现高效编辑。</div>
<div class="card-action">
<a href="directaudioedit-inversion-free-text-guided-audio-editing-via-2606-07356/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07356" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="targetsec-plug-and-play-in-the-wild-speech-emotion-conversio-2606-07293/">TargetSEC: Plug-and-Play In-the-Wild Speech Emotion Conversion via Arousal-Conditioned Latent Style Diffusion</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音情感转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出TargetSEC，一种基于嵌入驱动的潜在扩散框架，通过唤醒度条件实现非平行野外语音情感转换，兼顾转换准确性和语音质量。</div>
<div class="card-action">
<a href="targetsec-plug-and-play-in-the-wild-speech-emotion-conversio-2606-07293/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07293" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="kit-s-submission-to-cross-lingual-voice-cloning-in-iwslt-202-2606-07240/">KIT's Submission to Cross-Lingual Voice Cloning in IWSLT 2026</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音克隆</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">基于FishAudio-S2-Pro，通过语言标签提示、RL微调和词汇匹配提升跨语言语音克隆的语音质量和领域术语发音。</div>
<div class="card-action">
<a href="kit-s-submission-to-cross-lingual-voice-cloning-in-iwslt-202-2606-07240/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07240" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="audio-oscar-a-multi-agent-system-for-complex-audio-scene-gen-2606-07397/">Audio-Oscar: A Multi-Agent System for Complex Audio Scene Generation, Orchestration, and Refinement</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多智能体框架Audio-Oscar，通过协作专家代理实现复杂音频场景的生成、编排与优化。</div>
<div class="card-action">
<a href="audio-oscar-a-multi-agent-system-for-complex-audio-scene-gen-2606-07397/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07397" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="acoustic-cue-alignment-in-audio-language-models-for-speech-e-2606-07309/">Acoustic Cue Alignment in Audio Language Models for Speech Emotion Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过在音频语言模型中插入可解释的声学概念token，研究模型是否真正利用这些线索进行语音情感识别。</div>
<div class="card-action">
<a href="acoustic-cue-alignment-in-audio-language-models-for-speech-e-2606-07309/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07309" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="how-far-can-chord-symbol-time-series-adaptation-carry-genre--2606-07334/">How Far Can Chord-Symbol Time-Series Adaptation Carry Genre Identity? Capabilities and Boundaries in Multi-Genre Chord-Symbol Modeling</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音乐信息检索</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">评估多种参数高效微调方法将预训练和弦符号模型适应到11种音乐流派的能力，发现微调可提升流派内和弦预测，但和弦符号本身不足以完全表征流派身份。</div>
<div class="card-action">
<a href="how-far-can-chord-symbol-time-series-adaptation-carry-genre--2606-07334/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07334" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="where-rectified-flows-leak-characterising-membership-signals-2606-07271/">Where Rectified Flows Leak: Characterising Membership Signals Along the Interpolation Path</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#生成模型安全</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究Rectified Flow在插值路径上泄露训练数据成员信息的现象，发现训练与测试数据重构误差呈钟形曲线差异，并利用此进行成员推断攻击。</div>
<div class="card-action">
<a href="where-rectified-flows-leak-characterising-membership-signals-2606-07271/">详情 →</a> · <a href="https://arxiv.org/abs/2606.07271" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
