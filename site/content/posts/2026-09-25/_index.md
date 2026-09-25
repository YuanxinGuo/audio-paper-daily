---
title: "语音/音频论文速递 2026-09-25"
date: 2026-09-25T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 7 篇 · 最高分 8.8（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">7</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 5篇 | `██████████` |
| #语音合成 | 2篇 | `████` |
| #目标说话人提取 | 1篇 | `██` |
| #语音分离 | 1篇 | `██` |
| #语音识别 | 1篇 | `██` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="beyond-model-size-redesigning-lisennet-for-embedded-speech-e-2609-29866/">Beyond Model Size: Redesigning LiSenNet for embedded speech enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">将37k参数的子带双路径LiSenNet重构为NPU兼容的静态int8图，在STM32上以RTF 0.30实时运行且PESQ不降。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="damsep-distance-aware-monaural-source-separation-using-multi-2609-29749/">DAMSEP: Distance-Aware Monaural Source Separation using Multi-RIR Estimation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">DAMSEP 首次端到端联合做单通道语音分离与多源 RIR 估计，用 RIR 的 DRR 推断声源远近顺序，并发布 HETMIXR 数据集。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="configurable-bandwidth-time-frequency-modeling-for-efficient-2609-29463/">Configurable-Bandwidth Time-Frequency Modeling for Efficient Full-Band Speech Enhancement Across Sampling Rates</a>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出 TF-Refiner，将深度分析带宽与全带输入输出解耦，用单套参数跨 16/48 kHz 及未见采样率做全带语音增强。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="does-per-frame-early-exit-pay-a-compute-matched-study-of-dyn-2609-29867/">Does per-frame early exit pay? A compute-matched study of dynamic depth for on-device speech enhancement</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">研究逐帧早退在端侧语音增强中是否划算，用监督所有中间深度并微调输出头的方式，得到比同算力静态模型更优的Pareto前沿。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="deep-filter-estimation-from-inter-frame-correlations-for-mon-2603-14986/">Deep Filter Estimation from Inter-Frame Correlations for Monaural Speech Dereverberation</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出 IF-CorrNet，用帧间相关性作为网络输入，经双路径 Transformer 估计多帧深度滤波器，实现单通道去混响。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-vulnerability-of-neural-audio-watermarks-under-speech-en-2609-29040/">The Vulnerability of Neural Audio Watermarks under Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">将高斯噪声与语音增强模型级联作为黑盒攻击，测试六种神经音频水印的可去除性，发现生成式SE破坏性最强。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="exploring-a-single-autoregressive-llm-for-unified-target-spe-2609-29238/">Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Cues</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用单个自回归 LLM 主干统一处理同步（唇动/手势）与异步（注册音频/文本）线索的目标说话人提取，并提出 self-enrollment 机制。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="exploring-a-single-autoregressive-llm-for-unified-target-spe-2609-29238/">Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Cues</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">用单个自回归 LLM 主干统一处理同步（唇动/手势）与异步（注册音频/文本）线索的目标说话人提取，并提出 self-enrollment 机制。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="damsep-distance-aware-monaural-source-separation-using-multi-2609-29749/">DAMSEP: Distance-Aware Monaural Source Separation using Multi-RIR Estimation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">DAMSEP 首次端到端联合做单通道语音分离与多源 RIR 估计，用 RIR 的 DRR 推断声源远近顺序，并发布 HETMIXR 数据集。</div>
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
| 🥇 | [Exploring a Single Autoregressive LLM for Unified Target Spe…](exploring-a-single-autoregressive-llm-for-unified-target-spe-2609-29238/) 🎯 | **8.8** | #目标说话人提取 |
| 🥈 | [Beyond Model Size: Redesigning LiSenNet for embedded speech …](beyond-model-size-redesigning-lisennet-for-embedded-speech-e-2609-29866/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [DAMSEP: Distance-Aware Monaural Source Separation using Mult…](damsep-distance-aware-monaural-source-separation-using-multi-2609-29749/) 🎯 | **8.8** | #语音分离 |
| 4. | [Configurable-Bandwidth Time-Frequency Modeling for Efficient…](configurable-bandwidth-time-frequency-modeling-for-efficient-2609-29463/) 🎯 | **8.6** | #语音增强 |
| 5. | [Does per-frame early exit pay? A compute-matched study of dy…](does-per-frame-early-exit-pay-a-compute-matched-study-of-dyn-2609-29867/) 🎯 | **8.2** | #语音增强 |
| 6. | [Deep Filter Estimation from Inter-Frame Correlations for Mon…](deep-filter-estimation-from-inter-frame-correlations-for-mon-2603-14986/) 🎯 | **8.0** | #语音增强 |
| 7. | [The Vulnerability of Neural Audio Watermarks under Speech En…](the-vulnerability-of-neural-audio-watermarks-under-speech-en-2609-29040/) 🎯 | **7.8** | #语音增强 |
| 8. | [STAM-ASR: Speaker-Temporal Anchoring with Memory for Multi-S…](stam-asr-speaker-temporal-anchoring-with-memory-for-multi-sp-2609-29805/) | **6.8** | #语音识别 |
| 9. | [ReaFlow-TTS: Realization-Conditioned Flow Matching for High-…](reaflow-tts-realization-conditioned-flow-matching-for-high-q-2609-28906/) | **6.8** | #语音合成 |
| 10. | [Accent Analogy Guidance: More Speaker Similarity at Equal Ac…](accent-analogy-guidance-more-speaker-similarity-at-equal-acc-2609-29123/) | **6.8** | #语音合成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="exploring-a-single-autoregressive-llm-for-unified-target-spe-2609-29238/">Exploring a Single Autoregressive LLM for Unified Target Speech Extraction across Synchronous and Asynchronous Cues</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用单个自回归 LLM 主干统一处理同步（唇动/手势）与异步（注册音频/文本）线索的目标说话人提取，并提出 self-enrollment 机制。</div>
<div class="card-action">
<a href="exploring-a-single-autoregressive-llm-for-unified-target-spe-2609-29238/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29238" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="beyond-model-size-redesigning-lisennet-for-embedded-speech-e-2609-29866/">Beyond Model Size: Redesigning LiSenNet for embedded speech enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将37k参数的子带双路径LiSenNet重构为NPU兼容的静态int8图，在STM32上以RTF 0.30实时运行且PESQ不降。</div>
<div class="card-action">
<a href="beyond-model-size-redesigning-lisennet-for-embedded-speech-e-2609-29866/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29866" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="damsep-distance-aware-monaural-source-separation-using-multi-2609-29749/">DAMSEP: Distance-Aware Monaural Source Separation using Multi-RIR Estimation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">DAMSEP 首次端到端联合做单通道语音分离与多源 RIR 估计，用 RIR 的 DRR 推断声源远近顺序，并发布 HETMIXR 数据集。</div>
<div class="card-action">
<a href="damsep-distance-aware-monaural-source-separation-using-multi-2609-29749/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29749" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="configurable-bandwidth-time-frequency-modeling-for-efficient-2609-29463/">Configurable-Bandwidth Time-Frequency Modeling for Efficient Full-Band Speech Enhancement Across Sampling Rates</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.6</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 TF-Refiner，将深度分析带宽与全带输入输出解耦，用单套参数跨 16/48 kHz 及未见采样率做全带语音增强。</div>
<div class="card-action">
<a href="configurable-bandwidth-time-frequency-modeling-for-efficient-2609-29463/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29463" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="does-per-frame-early-exit-pay-a-compute-matched-study-of-dyn-2609-29867/">Does per-frame early exit pay? A compute-matched study of dynamic depth for on-device speech enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">研究逐帧早退在端侧语音增强中是否划算，用监督所有中间深度并微调输出头的方式，得到比同算力静态模型更优的Pareto前沿。</div>
<div class="card-action">
<a href="does-per-frame-early-exit-pay-a-compute-matched-study-of-dyn-2609-29867/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29867" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="deep-filter-estimation-from-inter-frame-correlations-for-mon-2603-14986/">Deep Filter Estimation from Inter-Frame Correlations for Monaural Speech Dereverberation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出 IF-CorrNet，用帧间相关性作为网络输入，经双路径 Transformer 估计多帧深度滤波器，实现单通道去混响。</div>
<div class="card-action">
<a href="deep-filter-estimation-from-inter-frame-correlations-for-mon-2603-14986/">详情 →</a> · <a href="https://arxiv.org/abs/2603.14986" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="the-vulnerability-of-neural-audio-watermarks-under-speech-en-2609-29040/">The Vulnerability of Neural Audio Watermarks under Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将高斯噪声与语音增强模型级联作为黑盒攻击，测试六种神经音频水印的可去除性，发现生成式SE破坏性最强。</div>
<div class="card-action">
<a href="the-vulnerability-of-neural-audio-watermarks-under-speech-en-2609-29040/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29040" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="stam-asr-speaker-temporal-anchoring-with-memory-for-multi-sp-2609-29805/">STAM-ASR: Speaker-Temporal Anchoring with Memory for Multi-Speaker ASR</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">STAM-ASR 用 AudioLLM 中间特征学习说话人活动与说话人感知表示，无需外部日志系统即可为多说话人 ASR 提供 who/when 线索。</div>
<div class="card-action">
<a href="stam-asr-speaker-temporal-anchoring-with-memory-for-multi-sp-2609-29805/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29805" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="reaflow-tts-realization-conditioned-flow-matching-for-high-q-2609-28906/">ReaFlow-TTS: Realization-Conditioned Flow Matching for High-Quality and Controllable Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在流匹配TTS中引入话语级随机realization隐变量，并用VAD语义约束该空间，实现无需目标语音的可控韵律与属性调节。</div>
<div class="card-action">
<a href="reaflow-tts-realization-conditioned-flow-matching-for-high-q-2609-28906/">详情 →</a> · <a href="https://arxiv.org/abs/2609.28906" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="accent-analogy-guidance-more-speaker-similarity-at-equal-acc-2609-29123/">Accent Analogy Guidance: More Speaker Similarity at Equal Accent in Cross-Lingual Voice Cloning</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出免训练的 accent analogy guidance，用同一合成音色的双语预测相减得到口音方向，在等口音条件下提升跨语言克隆的说话人相似度。</div>
<div class="card-action">
<a href="accent-analogy-guidance-more-speaker-similarity-at-equal-acc-2609-29123/">详情 →</a> · <a href="https://arxiv.org/abs/2609.29123" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
