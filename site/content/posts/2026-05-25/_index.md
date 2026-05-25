---
title: "语音/音频论文速递 2026-05-25"
date: 2026-05-25T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.5（#对抗攻击）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音可懂度预测 | 2篇 | `██████████` |
| #对抗攻击 | 1篇 | `█████` |
| #音频水印 | 1篇 | `█████` |
| #语音编解码 | 1篇 | `█████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #语音增强 | 1篇 | `█████` |
| #语音合成 | 1篇 | `█████` |
| #发音评分 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="data-augmentation-for-pathological-speech-enhancement-2602-14671/">Data Augmentation for Pathological Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">系统研究数据增强策略对帕金森病病理语音增强的效果，发现噪声增强最有效，生成式增强可能有害。</div>
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
| 🥇 | [Codec-Robust Attacks on Audio LLMs](codec-robust-attacks-on-audio-llms-2605-20519/) | **8.5** | #对抗攻击 |
| 🥈 | [XAttnMark: Learning Robust Audio Watermarking with Cross-Att…](xattnmark-learning-robust-audio-watermarking-with-cross-atte-2502-04230/) | **8.5** | #音频水印 |
| 🥉 | [AffectCodec: Emotion-Preserving Neural Speech Codec with Blo…](affectcodec-emotion-preserving-neural-speech-codec-with-bloc-2605-23373/) | **8.2** | #语音编解码 |
| 4. | [MixFake: Benchmarking and Enhancing Audio Deepfake Detection…](mixfake-benchmarking-and-enhancing-audio-deepfake-detection--2605-23201/) | **8.2** | #音频深度伪造检测 |
| 5. | [Data Augmentation for Pathological Speech Enhancement](data-augmentation-for-pathological-speech-enhancement-2602-14671/) 🎯 | **8.2** | #语音增强 |
| 6. | [Natural Yet Challenging to Detect: Robust In-the-Wild TTS th…](natural-yet-challenging-to-detect-robust-in-the-wild-tts-thr-2605-23859/) | **7.8** | #语音合成 |
| 7. | [Word-Level Modeling with Alignment-Aware Acoustic Fusion for…](word-level-modeling-with-alignment-aware-acoustic-fusion-for-2605-23604/) | **7.8** | #语音可懂度预测 |
| 8. | [Frame-Aligned Fusion of Canary and WavLM for Non-Intrusive I…](frame-aligned-fusion-of-canary-and-wavlm-for-non-intrusive-i-2605-23619/) | **7.5** | #语音可懂度预测 |
| 9. | [A study on weakly-supervised training approaches for phoneme…](a-study-on-weakly-supervised-training-approaches-for-phoneme-2605-23593/) | **7.2** | #发音评分 |
| 10. | [Articulatory strategy as a source of variation in acoustic v…](articulatory-strategy-as-a-source-of-variation-in-acoustic-v-2605-23416/) | **6.5** | #语音学 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="codec-robust-attacks-on-audio-llms-2605-20519/">Codec-Robust Attacks on Audio LLMs</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#对抗攻击</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CodecAttack，在神经音频编解码器潜空间优化扰动，实现对抗音频大模型的高成功率攻击，且对多种有损压缩鲁棒。</div>
<div class="card-action">
<a href="codec-robust-attacks-on-audio-llms-2605-20519/">详情 →</a> · <a href="https://arxiv.org/abs/2605.20519" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="xattnmark-learning-robust-audio-watermarking-with-cross-atte-2502-04230/">XAttnMark: Learning Robust Audio Watermarking with Cross-Attention</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出XAttnMark，利用交叉注意力和部分参数共享实现鲁棒音频水印，在检测和归因上达到SOTA。</div>
<div class="card-action">
<a href="xattnmark-learning-robust-audio-watermarking-with-cross-atte-2502-04230/">详情 →</a> · <a href="https://arxiv.org/abs/2502.04230" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="affectcodec-emotion-preserving-neural-speech-codec-with-bloc-2605-23373/">AffectCodec: Emotion-Preserving Neural Speech Codec with Block-Diagonal Residual FSQ</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音编解码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AffectCodec，通过块对角残差有限标量量化（BD-RFSQ）在低比特率下保留语音情感信息，同时保持声学质量。</div>
<div class="card-action">
<a href="affectcodec-emotion-preserving-neural-speech-codec-with-bloc-2605-23373/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23373" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="mixfake-benchmarking-and-enhancing-audio-deepfake-detection--2605-23201/">MixFake: Benchmarking and Enhancing Audio Deepfake Detection in Diverse Real-world Mixed Audio</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MixFake基准数据集和多流提示微调框架，在混合音频深度伪造检测中显著提升复杂背景下的性能。</div>
<div class="card-action">
<a href="mixfake-benchmarking-and-enhancing-audio-deepfake-detection--2605-23201/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23201" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="data-augmentation-for-pathological-speech-enhancement-2602-14671/">Data Augmentation for Pathological Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统研究数据增强策略对帕金森病病理语音增强的效果，发现噪声增强最有效，生成式增强可能有害。</div>
<div class="card-action">
<a href="data-augmentation-for-pathological-speech-enhancement-2602-14671/">详情 →</a> · <a href="https://arxiv.org/abs/2602.14671" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="natural-yet-challenging-to-detect-robust-in-the-wild-tts-thr-2605-23859/">Natural Yet Challenging to Detect: Robust In-the-Wild TTS through EMA and Dual-Scoring Prompt Selection -- Submission for WildSpoof 2026 TTS Track</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">基于F5-TTS架构，结合EMA和双评分提示选择，生成自然且难以被SASV系统检测的语音。</div>
<div class="card-action">
<a href="natural-yet-challenging-to-detect-robust-in-the-wild-tts-thr-2605-23859/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23859" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="word-level-modeling-with-alignment-aware-acoustic-fusion-for-2605-23604/">Word-Level Modeling with Alignment-Aware Acoustic Fusion for Text-Assisted Intelligibility Prediction in Listeners with Hearing Loss</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音可懂度预测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于对齐感知声学融合的词级建模方法，利用Whisper和参考文本预测听力受损者的语音可懂度。</div>
<div class="card-action">
<a href="word-level-modeling-with-alignment-aware-acoustic-fusion-for-2605-23604/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23604" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="frame-aligned-fusion-of-canary-and-wavlm-for-non-intrusive-i-2605-23619/">Frame-Aligned Fusion of Canary and WavLM for Non-Intrusive Intelligibility Prediction of Hearing-Aid-Processed Speech</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音可懂度预测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出帧对齐融合策略，结合Canary和WavLM编码器，在无参考条件下预测助听器处理语音的可懂度，在Clarity挑战中取得最优结果。</div>
<div class="card-action">
<a href="frame-aligned-fusion-of-canary-and-wavlm-for-non-intrusive-i-2605-23619/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23619" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-study-on-weakly-supervised-training-approaches-for-phoneme-2605-23593/">A study on weakly-supervised training approaches for phoneme-level pronunciation scoring</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#发音评分</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究利用话语级或词级标签弱监督训练音素级发音评分模型，两阶段微调可接近全监督性能。</div>
<div class="card-action">
<a href="a-study-on-weakly-supervised-training-approaches-for-phoneme-2605-23593/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23593" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="articulatory-strategy-as-a-source-of-variation-in-acoustic-v-2605-23416/">Articulatory strategy as a source of variation in acoustic vowel dynamics</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过超声舌成像数据，证明发音策略差异系统性地影响声学元音动态，为说话人识别中的个体差异提供发音学解释。</div>
<div class="card-action">
<a href="articulatory-strategy-as-a-source-of-variation-in-acoustic-v-2605-23416/">详情 →</a> · <a href="https://arxiv.org/abs/2605.23416" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
