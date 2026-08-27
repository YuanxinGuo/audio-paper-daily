---
title: "语音/音频论文速递 2026-08-27"
date: 2026-08-27T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#双耳音频）"
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
| #双耳音频 | 1篇 | `██████████` |
| #语音聚类 | 1篇 | `██████████` |
| #语音合成 | 1篇 | `██████████` |
| #共语手势生成 | 1篇 | `██████████` |
| #音乐理解 | 1篇 | `██████████` |
| #音乐文本检索 | 1篇 | `██████████` |
| #音频安全 | 1篇 | `██████████` |
| #音视频同步评估 | 1篇 | `██████████` |

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
<a class="card-title" href="csavocoder-a-causal-spatial-audio-vocoder-towards-real-time--2608-25404/">CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time Spatial Audio Generation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出因果GAN空间音频声码器CSAVocoder，通过空间适配器和一致性判别器提升空间保真度，支持实时流式推理。</div>
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
| 🥇 | [CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time…](csavocoder-a-causal-spatial-audio-vocoder-towards-real-time--2608-25404/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [AudioLens: Multi-Perspective Speech Clustering with Reasonin…](audiolens-multi-perspective-speech-clustering-with-reasoning-2608-25177/) | **8.2** | #语音聚类 |
| 🥉 | [CuteTTS: Efficient and High-Quality Speech Synthesis via Aut…](cutetts-efficient-and-high-quality-speech-synthesis-via-auto-2608-08638/) | **7.8** | #语音合成 |
| 4. | [Super Star: Towards Streaming Real-time Interactive Agents f…](super-star-towards-streaming-real-time-interactive-agents-fo-2608-24909/) | **7.8** | #共语手势生成 |
| 5. | [Dissonance Spectrum explicitly models perceptual frequency i…](dissonance-spectrum-explicitly-models-perceptual-frequency-i-2608-25621/) | **7.8** | #音乐理解 |
| 6. | [AllMusicCaps: Album Reviews as Complementary Supervision for…](allmusiccaps-album-reviews-as-complementary-supervision-for--2608-25244/) | **7.8** | #音乐文本检索 |
| 7. | [AOR-Bench: Do Large Audio Language Models Over-Refuse Pseudo…](aor-bench-do-large-audio-language-models-over-refuse-pseudo--2606-21147/) | **7.2** | #音频安全 |
| 8. | [What Do Audio-Visual Synchronization Metrics Actually Measur…](what-do-audio-visual-synchronization-metrics-actually-measur-2608-25157/) | **7.2** | #音视频同步评估 |
| 9. | [A Training-Free Proactive Defense Against Partial Speech Man…](a-training-free-proactive-defense-against-partial-speech-man-2608-25285/) | **7.2** | #音频取证 |
| 10. | [Combining Self-Embedding Audio Watermarking with Ultra-Low-B…](combining-self-embedding-audio-watermarking-with-ultra-low-b-2608-25289/) | **6.8** | #音频水印 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="csavocoder-a-causal-spatial-audio-vocoder-towards-real-time--2608-25404/">CSAVocoder: A Causal Spatial Audio Vocoder Towards Real-Time Spatial Audio Generation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出因果GAN空间音频声码器CSAVocoder，通过空间适配器和一致性判别器提升空间保真度，支持实时流式推理。</div>
<div class="card-action">
<a href="csavocoder-a-causal-spatial-audio-vocoder-towards-real-time--2608-25404/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25404" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="audiolens-multi-perspective-speech-clustering-with-reasoning-2608-25177/">AudioLens: Multi-Perspective Speech Clustering with Reasoning Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音聚类</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音频多视角聚类任务，构建基准并训练端到端音频语言模型AudioLens-R1，在多个领域上显著超越基线。</div>
<div class="card-action">
<a href="audiolens-multi-perspective-speech-clustering-with-reasoning-2608-25177/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25177" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="cutetts-efficient-and-high-quality-speech-synthesis-via-auto-2608-08638/">CuteTTS: Efficient and High-Quality Speech Synthesis via Autoregressive Modeling of Continuous Latents</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">CuteTTS提出连续自回归语音合成系统，结合因果VAE、补丁级自回归与流匹配头，并通过引导步蒸馏降低推理延迟，实现高质量零样本语音克隆。</div>
<div class="card-action">
<a href="cutetts-efficient-and-high-quality-speech-synthesis-via-auto-2608-08638/">详情 →</a> · <a href="https://arxiv.org/abs/2608.08638" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="super-star-towards-streaming-real-time-interactive-agents-fo-2608-24909/">Super Star: Towards Streaming Real-time Interactive Agents for Digital Humans</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#共语手势生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出流式共语手势生成框架，结合流式语音响应与在线手势生成，实现低延迟、语音同步的实时交互数字人。</div>
<div class="card-action">
<a href="super-star-towards-streaming-real-time-interactive-agents-fo-2608-24909/">详情 →</a> · <a href="https://arxiv.org/abs/2608.24909" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="dissonance-spectrum-explicitly-models-perceptual-frequency-i-2608-25621/">Dissonance Spectrum explicitly models perceptual frequency interactions for better music understanding</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出不和谐频谱（DS）表示，显式建模频率间感知交互，在音乐问答和情感识别中稳定提升基线。</div>
<div class="card-action">
<a href="dissonance-spectrum-explicitly-models-perceptual-frequency-i-2608-25621/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25621" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="allmusiccaps-album-reviews-as-complementary-supervision-for--2608-25244/">AllMusicCaps: Album Reviews as Complementary Supervision for Music CLAP</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐文本检索</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用AllMusic专辑评论经LLM预处理生成训练数据，提升音乐CLAP在检索与分类上的表现。</div>
<div class="card-action">
<a href="allmusiccaps-album-reviews-as-complementary-supervision-for--2608-25244/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25244" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="aor-bench-do-large-audio-language-models-over-refuse-pseudo--2606-21147/">AOR-Bench: Do Large Audio Language Models Over-Refuse Pseudo-Harmful Queries?</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频安全</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首个针对大音频语言模型的过度拒绝基准AOR-Bench，含3000个伪有害音频样本，评估12个模型发现过度拒绝普遍存在，并探索了两种缓解策略。</div>
<div class="card-action">
<a href="aor-bench-do-large-audio-language-models-over-refuse-pseudo--2606-21147/">详情 →</a> · <a href="https://arxiv.org/abs/2606.21147" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="what-do-audio-visual-synchronization-metrics-actually-measur-2608-25157/">What Do Audio-Visual Synchronization Metrics Actually Measure?</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音视频同步评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统审计多种自动音视频同步指标，发现它们在不同失真下表现各异且相互不一致，建议用可靠性卡片报告而非单一分数。</div>
<div class="card-action">
<a href="what-do-audio-visual-synchronization-metrics-actually-measur-2608-25157/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25157" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="a-training-free-proactive-defense-against-partial-speech-man-2608-25285/">A Training-Free Proactive Defense Against Partial Speech Manipulation via Self-Embedding Steganography</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频取证</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出利用自嵌入音频隐写作为主动防御，无需训练即可检测和恢复部分深度伪造语音。</div>
<div class="card-action">
<a href="a-training-free-proactive-defense-against-partial-speech-man-2608-25285/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25285" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="combining-self-embedding-audio-watermarking-with-ultra-low-b-2608-25289/">Combining Self-Embedding Audio Watermarking with Ultra-Low-Bitrate Neural Codecs</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文探索将自嵌入音频水印与超低比特率神经编解码器结合，在理想信道下实现篡改检测、定位与内容恢复。</div>
<div class="card-action">
<a href="combining-self-embedding-audio-watermarking-with-ultra-low-b-2608-25289/">详情 →</a> · <a href="https://arxiv.org/abs/2608.25289" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
