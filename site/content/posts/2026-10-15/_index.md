---
title: "语音/音频论文速递 2026-10-15"
date: 2026-10-15T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 4 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">4</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 1篇 | `██████████` |
| #音乐生成 | 1篇 | `██████████` |
| #音频生成 | 1篇 | `██████████` |
| #语音编辑 | 1篇 | `██████████` |
| #语音识别 | 1篇 | `██████████` |
| #空间音频推理 | 1篇 | `██████████` |
| #生物声学 | 1篇 | `██████████` |
| #音频取证与生成检测 | 1篇 | `██████████` |

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
<a class="card-title" href="hrtf-upsampling-and-personalization-via-neural-operators-2610-20400/">HRTF Upsampling and Personalization via Neural Operators</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出神经算子 SPARO，将稀疏方向 HRTF 测量映射为可任意查询的连续 HRTF 场，实现空间上采样与个性化。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sonicworld-source-centric-latent-dynamics-for-spatial-audio--2610-17131/">SonicWorld: Source-Centric Latent Dynamics for Spatial Audio Reasoning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#空间音频推理</span>
</div>
<div class="card-tldr">提出Sonic-Bench基准与SonicWorld模型，用源中心隐动态与Omni LLM做动态空间音频推理，方向准确率与方位误差均优于Spatial-Omni。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="remix-the-timbre-diffusion-based-style-transfer-across-polyp-2605-09259/">Remix the Timbre: Diffusion-Based Style Transfer Across Polyphonic Stems</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#音乐生成</span>
</div>
<div class="card-tldr">MixtureTT 用联合扩散 Transformer 直接从复音混音中为每个 stem 做音色迁移，避免先分离后迁移的级联误差。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="point-and-play-instrument-timbre-cloning-from-music-mixtures-2610-19445/">Point-and-Play: Instrument Timbre Cloning from Music Mixtures</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#音频生成</span>
</div>
<div class="card-tldr">提出 Point-and-Play，用 Cue-Gated Statistics Pooling 从多乐器混音中直接提取被指定乐器的音色码，条件化音符合成器生成新音高与力度。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [HRTF Upsampling and Personalization via Neural Operators](hrtf-upsampling-and-personalization-via-neural-operators-2610-20400/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [Remix the Timbre: Diffusion-Based Style Transfer Across Poly…](remix-the-timbre-diffusion-based-style-transfer-across-polyp-2605-09259/) 🎯 | **8.0** | #音乐生成 |
| 🥉 | [Point-and-Play: Instrument Timbre Cloning from Music Mixture…](point-and-play-instrument-timbre-cloning-from-music-mixtures-2610-19445/) 🎯 | **8.0** | #音频生成 |
| 4. | [AnyEdit: A Unified Framework for Speech and Singing Voice Ed…](anyedit-a-unified-framework-for-speech-and-singing-voice-edi-2610-15665/) | **7.8** | #语音编辑 |
| 5. | [ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented L…](elarspeech-a-30k-hour-dataset-across-675-underrepresented-la-2610-19388/) | **7.8** | #语音识别 |
| 6. | [SonicWorld: Source-Centric Latent Dynamics for Spatial Audio…](sonicworld-source-centric-latent-dynamics-for-spatial-audio--2610-17131/) 🎯 | **7.8** | #空间音频推理 |
| 7. | [C2GA: A Class-Controllable Generative Augmentation Framework…](c2ga-a-class-controllable-generative-augmentation-framework--2606-02212/) | **6.8** | #生物声学 |
| 8. | [MUSEBENCH: A Benchmark for AI-Generated Music Detection and …](musebench-a-benchmark-for-ai-generated-music-detection-and-a-2610-20310/) | **6.8** | #音频取证与生成检测 |
| 9. | [Evaluating perceptual transparency of lossy music audio comp…](evaluating-perceptual-transparency-of-lossy-music-audio-comp-2610-20246/) | **6.5** | #音频压缩 |
| 10. | [Window Size Matters: Benchmarking Voice Activity Detectors i…](window-size-matters-benchmarking-voice-activity-detectors-in-2610-14607/) | **5.5** | #语音活动检测 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="hrtf-upsampling-and-personalization-via-neural-operators-2610-20400/">HRTF Upsampling and Personalization via Neural Operators</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出神经算子 SPARO，将稀疏方向 HRTF 测量映射为可任意查询的连续 HRTF 场，实现空间上采样与个性化。</div>
<div class="card-action">
<a href="hrtf-upsampling-and-personalization-via-neural-operators-2610-20400/">详情 →</a> · <a href="https://arxiv.org/abs/2610.20400" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="remix-the-timbre-diffusion-based-style-transfer-across-polyp-2605-09259/">Remix the Timbre: Diffusion-Based Style Transfer Across Polyphonic Stems</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">MixtureTT 用联合扩散 Transformer 直接从复音混音中为每个 stem 做音色迁移，避免先分离后迁移的级联误差。</div>
<div class="card-action">
<a href="remix-the-timbre-diffusion-based-style-transfer-across-polyp-2605-09259/">详情 →</a> · <a href="https://arxiv.org/abs/2605.09259" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="point-and-play-instrument-timbre-cloning-from-music-mixtures-2610-19445/">Point-and-Play: Instrument Timbre Cloning from Music Mixtures</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 Point-and-Play，用 Cue-Gated Statistics Pooling 从多乐器混音中直接提取被指定乐器的音色码，条件化音符合成器生成新音高与力度。</div>
<div class="card-action">
<a href="point-and-play-instrument-timbre-cloning-from-music-mixtures-2610-19445/">详情 →</a> · <a href="https://arxiv.org/abs/2610.19445" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="anyedit-a-unified-framework-for-speech-and-singing-voice-edi-2610-15665/">AnyEdit: A Unified Framework for Speech and Singing Voice Editing with Real-World Environmental Consistency</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">AnyEdit 用两阶段分离式框架做语音与歌声编辑，先预测干净韵律内容 token，再用流匹配模型在源声学上下文中渲染，保留噪声与混响。</div>
<div class="card-action">
<a href="anyedit-a-unified-framework-for-speech-and-singing-voice-edi-2610-15665/">详情 →</a> · <a href="https://arxiv.org/abs/2610.15665" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="elarspeech-a-30k-hour-dataset-across-675-underrepresented-la-2610-19388/">ELARSpeech: A 30K-Hour Dataset Across 675 Underrepresented Languages for Long-Tail Multilingual Speech Technologies</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发布 ELARSpeech，30,202 小时、675 种低资源语言的语音数据集，支持 ASR/TTS 长尾多语言建模与伪标签实验。</div>
<div class="card-action">
<a href="elarspeech-a-30k-hour-dataset-across-675-underrepresented-la-2610-19388/">详情 →</a> · <a href="https://arxiv.org/abs/2610.19388" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="sonicworld-source-centric-latent-dynamics-for-spatial-audio--2610-17131/">SonicWorld: Source-Centric Latent Dynamics for Spatial Audio Reasoning</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#空间音频推理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出Sonic-Bench基准与SonicWorld模型，用源中心隐动态与Omni LLM做动态空间音频推理，方向准确率与方位误差均优于Spatial-Omni。</div>
<div class="card-action">
<a href="sonicworld-source-centric-latent-dynamics-for-spatial-audio--2610-17131/">详情 →</a> · <a href="https://arxiv.org/abs/2610.17131" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="c2ga-a-class-controllable-generative-augmentation-framework--2606-02212/">C2GA: A Class-Controllable Generative Augmentation Framework for Respiratory Sound Classification</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#生物声学</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用条件VQ-VAE构建离散隐空间，配合Transformer自回归先验生成类别可控的呼吸音梅尔谱，用于呼吸音分类数据增强。</div>
<div class="card-action">
<a href="c2ga-a-class-controllable-generative-augmentation-framework--2606-02212/">详情 →</a> · <a href="https://arxiv.org/abs/2606.02212" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="musebench-a-benchmark-for-ai-generated-music-detection-and-a-2610-20310/">MUSEBENCH: A Benchmark for AI-Generated Music Detection and Artifact Analysis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频取证与生成检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">构建36.1万首曲目的AI生成音乐检测基准MUSEBENCH，含10个生成模型产物与对抗扰动变体，评测11个检测器并分析声学伪影。</div>
<div class="card-action">
<a href="musebench-a-benchmark-for-ai-generated-music-detection-and-a-2610-20310/">详情 →</a> · <a href="https://arxiv.org/abs/2610.20310" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="evaluating-perceptual-transparency-of-lossy-music-audio-comp-2610-20246/">Evaluating perceptual transparency of lossy music audio compression with Opus codec</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音频压缩</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用 ITU-R BS.1116-3 双盲听测与 LMM/TOST 统计，判定 Opus 对 CD 音质音乐在 160 kbps 达到感知透明。</div>
<div class="card-action">
<a href="evaluating-perceptual-transparency-of-lossy-music-audio-comp-2610-20246/">详情 →</a> · <a href="https://arxiv.org/abs/2610.20246" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="window-size-matters-benchmarking-voice-activity-detectors-in-2610-14607/">Window Size Matters: Benchmarking Voice Activity Detectors in Noise</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#语音活动检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在LibriVAD-small含噪测试集上对TEN、Silero与RMS三种VAD做帧级基准，考察窗长与SNR影响。</div>
<div class="card-action">
<a href="window-size-matters-benchmarking-voice-activity-detectors-in-2610-14607/">详情 →</a> · <a href="https://arxiv.org/abs/2610.14607" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
