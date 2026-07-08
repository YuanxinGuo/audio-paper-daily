---
title: "语音/音频论文速递 2026-07-08"
date: 2026-07-08T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 1篇 | `██████████` |
| #音乐生成 | 1篇 | `██████████` |
| #视频到音频生成 | 1篇 | `██████████` |
| #活动说话人检测 | 1篇 | `██████████` |
| #音频表征学习 | 1篇 | `██████████` |
| #自监督学习分析 | 1篇 | `██████████` |
| #音频编码器可解释性 | 1篇 | `██████████` |
| #音乐推荐 | 1篇 | `██████████` |

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
<a class="card-title" href="flow-matching-based-speech-source-separation-with-best-of-n--2607-06088/">Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出基于条件流匹配的语音分离方法，利用说话人编码器排序源并实现最佳N采样和块级对齐，在Libri2Mix上达到有竞争力的分离质量和最低的下游ASR/SV错误率。</div>
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
| 🥇 | [Flow Matching-Based Speech Source Separation with Best-of-N …](flow-matching-based-speech-source-separation-with-best-of-n--2607-06088/) 🎯 | **8.8** | #语音分离 |
| 🥈 | [HeartMuLa: A Family of Open Sourced Music Foundation Models](heartmula-a-family-of-open-sourced-music-foundation-models-2601-10547/) | **8.5** | #音乐生成 |
| 🥉 | [Precise Video-to-Audio Generation with Cross-Modal Alignment…](precise-video-to-audio-generation-with-cross-modal-alignment-2607-06405/) | **8.2** | #视频到音频生成 |
| 4. | [$C^3$ASD: Multi-Level Consistency-Driven Representation Lear…](c-3-asd-multi-level-consistency-driven-representation-learni-2607-03018/) | **7.8** | #活动说话人检测 |
| 5. | [Perceptually Aligning Representations of Music via Noise-Aug…](perceptually-aligning-representations-of-music-via-noise-aug-2511-05350/) | **7.8** | #音频表征学习 |
| 6. | [InsideSSL: Understanding Self-Supervised Speech Representati…](insidessl-understanding-self-supervised-speech-representatio-2607-06392/) | **7.8** | #自监督学习分析 |
| 7. | [Towards Interpretable Framework for Neural Audio Codecs via …](towards-interpretable-framework-for-neural-audio-codecs-via--2603-18359/) | **7.2** | #音频编码器可解释性 |
| 8. | [Multimodal Video-to-Music Recommendation via Semantic Retrie…](multimodal-video-to-music-recommendation-via-semantic-retrie-2607-05971/) | **7.2** | #音乐推荐 |
| 9. | [Determinantal point process sampling for bioacoustic active …](determinantal-point-process-sampling-for-bioacoustic-active--2607-06063/) | **7.2** | #生物声学 |
| 10. | [What Counts as Real? Speech Restoration and Voice Quality Co…](what-counts-as-real-speech-restoration-and-voice-quality-con-2603-14033/) | **7.2** | #音频深度伪造检测 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="flow-matching-based-speech-source-separation-with-best-of-n--2607-06088/">Flow Matching-Based Speech Source Separation with Best-of-N Biometric Sampling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于条件流匹配的语音分离方法，利用说话人编码器排序源并实现最佳N采样和块级对齐，在Libri2Mix上达到有竞争力的分离质量和最低的下游ASR/SV错误率。</div>
<div class="card-action">
<a href="flow-matching-based-speech-source-separation-with-best-of-n--2607-06088/">详情 →</a> · <a href="https://arxiv.org/abs/2607.06088" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="heartmula-a-family-of-open-sourced-music-foundation-models-2601-10547/">HeartMuLa: A Family of Open Sourced Music Foundation Models</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">开源音乐基础模型系列，包含对齐、歌词识别、编解码和可控歌曲生成，首次用学术资源复现商业级系统。</div>
<div class="card-action">
<a href="heartmula-a-family-of-open-sourced-music-foundation-models-2601-10547/">详情 →</a> · <a href="https://arxiv.org/abs/2601.10547" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="precise-video-to-audio-generation-with-cross-modal-alignment-2607-06405/">Precise Video-to-Audio Generation with Cross-Modal Alignment in Latent Space</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#视频到音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Flowley，一种端到端单阶段视频到音频生成架构，通过渐进式软掩码交叉注意力实现音视频同步，并引入SoundCap生成声音感知描述以提升音频质量。</div>
<div class="card-action">
<a href="precise-video-to-audio-generation-with-cross-modal-alignment-2607-06405/">详情 →</a> · <a href="https://arxiv.org/abs/2607.06405" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="c-3-asd-multi-level-consistency-driven-representation-learni-2607-03018/">$C^3$ASD: Multi-Level Consistency-Driven Representation Learning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#活动说话人检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多级一致性驱动的活动说话人检测框架，通过嵌入级、序列级和预测级约束提升对音频/视觉/联合退化的鲁棒性。</div>
<div class="card-action">
<a href="c-3-asd-multi-level-consistency-driven-representation-learni-2607-03018/">详情 →</a> · <a href="https://arxiv.org/abs/2607.03018" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="perceptually-aligning-representations-of-music-via-noise-aug-2511-05350/">Perceptually Aligning Representations of Music via Noise-Augmented Autoencoders</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频表征学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过噪声增强自编码器结合感知损失，使音频表征按感知层次结构化，在音高惊讶估计和EEG预测上超越先前方法。</div>
<div class="card-action">
<a href="perceptually-aligning-representations-of-music-via-noise-aug-2511-05350/">详情 →</a> · <a href="https://arxiv.org/abs/2511.05350" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="insidessl-understanding-self-supervised-speech-representatio-2607-06392/">InsideSSL: Understanding Self-Supervised Speech Representations using a Model-Centric Perspective</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#自监督学习分析</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出InsideSSL框架，从压缩、几何、鲁棒性三个内在视角分析SSL语音模型层内动力学，并引入跨层生成兼容性矩阵评估功能可迁移性。</div>
<div class="card-action">
<a href="insidessl-understanding-self-supervised-speech-representatio-2607-06392/">详情 →</a> · <a href="https://arxiv.org/abs/2607.06392" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="towards-interpretable-framework-for-neural-audio-codecs-via--2603-18359/">Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频编码器可解释性</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">使用稀疏自编码器分解神经音频编解码器的隐表示，以口音信息为案例量化可解释性。</div>
<div class="card-action">
<a href="towards-interpretable-framework-for-neural-audio-codecs-via--2603-18359/">详情 →</a> · <a href="https://arxiv.org/abs/2603.18359" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="multimodal-video-to-music-recommendation-via-semantic-retrie-2607-05971/">Multimodal Video-to-Music Recommendation via Semantic Retrieval and Temporal Reranking</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音乐推荐</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出VTMR两阶段框架，通过多模态语义检索和时序重排序实现视频到音乐推荐，在R@10和Median Rank上显著超越基线。</div>
<div class="card-action">
<a href="multimodal-video-to-music-recommendation-via-semantic-retrie-2607-05971/">详情 →</a> · <a href="https://arxiv.org/abs/2607.05971" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="determinantal-point-process-sampling-for-bioacoustic-active--2607-06063/">Determinantal point process sampling for bioacoustic active learning</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出CARE-DPP方法，结合不确定性、新颖性和DPP采样进行批量主动学习，在BioDCASE挑战中提升生物声学分类性能。</div>
<div class="card-action">
<a href="determinantal-point-process-sampling-for-bioacoustic-active--2607-06063/">详情 →</a> · <a href="https://arxiv.org/abs/2607.06063" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="what-counts-as-real-speech-restoration-and-voice-quality-con-2603-14033/">What Counts as Real? Speech Restoration and Voice Quality Conversion Pose New Challenges to Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文发现传统二分类伪造检测在语音恢复和音质转换后失效，提出将标签分解为源真实性和处理状态，实验表明检测器能识别处理但无法区分真假源。</div>
<div class="card-action">
<a href="what-counts-as-real-speech-restoration-and-voice-quality-con-2603-14033/">详情 →</a> · <a href="https://arxiv.org/abs/2603.14033" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
