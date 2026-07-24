---
title: "语音/音频论文速递 2026-07-24"
date: 2026-07-24T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 9.5（#空间音频生成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #空间音频生成 | 1篇 | `██████████` |
| #语音分离 | 1篇 | `██████████` |
| #音乐生成 | 1篇 | `██████████` |
| #音频水印 | 1篇 | `██████████` |
| #语音匿名化 | 1篇 | `██████████` |
| #音频字幕评估 | 1篇 | `██████████` |
| #语音深度伪造检测 | 1篇 | `██████████` |
| #事件检测 | 1篇 | `██████████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="investigating-codec-internal-latent-audio-watermarking-for-n-2607-21132/">Investigating Codec-Internal Latent Audio Watermarking for Neural Codec Robustness</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频水印</span>
</div>
<div class="card-tldr">研究在神经音频编解码器的连续潜在空间中嵌入水印，以提升对编解码变换的鲁棒性，并分析了水印嵌入位置与质量/鲁棒性的权衡。</div>
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
<a class="card-title" href="tf-mossformer-integrating-convolution-gated-local-global-att-2607-21128/">TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出TF-MossFormer，在时频域结合卷积门控与局部-全局注意力，在WSJ0-2Mix上以5.9M参数达到22.6 dB SI-SDRi，超越此前方法。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dynfoa-generating-first-order-ambisonics-with-conditional-di-2602-06846/">DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#空间音频生成</span>
</div>
<div class="card-tldr">提出DynFOA，利用条件扩散模型和3D场景重建从360度视频生成一阶环绕声，在动态和声学复杂场景中优于现有方法。</div>
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
| 🥇 | [DynFOA: Generating First-Order Ambisonics with Conditional D…](dynfoa-generating-first-order-ambisonics-with-conditional-di-2602-06846/) 🎯 | **9.5** | #空间音频生成 |
| 🥈 | [TF-MossFormer: Integrating Convolution Gated Local-Global At…](tf-mossformer-integrating-convolution-gated-local-global-att-2607-21128/) 🎯 | **9.5** | #语音分离 |
| 🥉 | [LaDA-Band: Language Diffusion Models for Vocal-to-Accompanim…](lada-band-language-diffusion-models-for-vocal-to-accompanime-2604-11052/) | **8.5** | #音乐生成 |
| 4. | [Investigating Codec-Internal Latent Audio Watermarking for N…](investigating-codec-internal-latent-audio-watermarking-for-n-2607-21132/) 🎯 | **8.2** | #音频水印 |
| 5. | [Content Anonymization for Privacy in Long-form Audio](content-anonymization-for-privacy-in-long-form-audio-2510-12780/) | **7.2** | #语音匿名化 |
| 6. | [An Evaluation Framework for Structured Audio Captions Valida…](an-evaluation-framework-for-structured-audio-captions-valida-2607-21424/) | **7.2** | #音频字幕评估 |
| 7. | [Toward Interpretable Speech Deepfake Detection using Artifac…](toward-interpretable-speech-deepfake-detection-using-artifac-2607-21127/) | **7.2** | #语音深度伪造检测 |
| 8. | [Spectrogram-Based Joint Detection, Localization, and Classif…](spectrogram-based-joint-detection-localization-and-classific-2607-20817/) | **6.5** | #事件检测 |
| 9. | [Methods for pitch analysis in contemporary popular music: ph…](methods-for-pitch-analysis-in-contemporary-popular-music-phe-2502-08131/) | **5.5** | #音乐分析 |
| 10. | [Improving the performance of an ASV system using hybrid spee…](improving-the-performance-of-an-asv-system-using-hybrid-spee-2607-20706/) | **5.5** | #说话人确认 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="dynfoa-generating-first-order-ambisonics-with-conditional-di-2602-06846/">DynFOA: Generating First-Order Ambisonics with Conditional Diffusion for Dynamic and Acoustically Complex 360-Degree Videos</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#空间音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DynFOA，利用条件扩散模型和3D场景重建从360度视频生成一阶环绕声，在动态和声学复杂场景中优于现有方法。</div>
<div class="card-action">
<a href="dynfoa-generating-first-order-ambisonics-with-conditional-di-2602-06846/">详情 →</a> · <a href="https://arxiv.org/abs/2602.06846" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="tf-mossformer-integrating-convolution-gated-local-global-att-2607-21128/">TF-MossFormer: Integrating Convolution Gated Local-Global Attentions for Enhanced Time-Frequency Domain Monaural Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出TF-MossFormer，在时频域结合卷积门控与局部-全局注意力，在WSJ0-2Mix上以5.9M参数达到22.6 dB SI-SDRi，超越此前方法。</div>
<div class="card-action">
<a href="tf-mossformer-integrating-convolution-gated-local-global-att-2607-21128/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21128" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="lada-band-language-diffusion-models-for-vocal-to-accompanime-2604-11052/">LaDA-Band: Language Diffusion Models for Vocal-to-Accompaniment Generation</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出LaDA-Band，利用离散掩码扩散模型实现端到端的人声转伴奏生成，兼顾声学真实感、全局连贯性和动态编配。</div>
<div class="card-action">
<a href="lada-band-language-diffusion-models-for-vocal-to-accompanime-2604-11052/">详情 →</a> · <a href="https://arxiv.org/abs/2604.11052" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="investigating-codec-internal-latent-audio-watermarking-for-n-2607-21132/">Investigating Codec-Internal Latent Audio Watermarking for Neural Codec Robustness</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">研究在神经音频编解码器的连续潜在空间中嵌入水印，以提升对编解码变换的鲁棒性，并分析了水印嵌入位置与质量/鲁棒性的权衡。</div>
<div class="card-action">
<a href="investigating-codec-internal-latent-audio-watermarking-for-n-2607-21132/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21132" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="content-anonymization-for-privacy-in-long-form-audio-2510-12780/">Content Anonymization for Privacy in Long-form Audio</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音匿名化</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">针对长音频中基于内容风格的重识别攻击，提出在ASR-TTS流水线中对文本进行上下文改写以消除说话人特有风格，同时保留语义。</div>
<div class="card-action">
<a href="content-anonymization-for-privacy-in-long-form-audio-2510-12780/">详情 →</a> · <a href="https://arxiv.org/abs/2510.12780" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="an-evaluation-framework-for-structured-audio-captions-valida-2607-21424/">An Evaluation Framework for Structured Audio Captions Validated by Controlled Perturbations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频字幕评估</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一个多轴评估框架，结合LLM和确定性指标评估结构化音频字幕，并通过受控扰动验证其可靠性。</div>
<div class="card-action">
<a href="an-evaluation-framework-for-structured-audio-captions-valida-2607-21424/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21424" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="toward-interpretable-speech-deepfake-detection-using-artifac-2607-21127/">Toward Interpretable Speech Deepfake Detection using Artifact-Specific Experts and Calibrated Detection Scores</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音深度伪造检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于伪影特定专家的可解释语音深度伪造检测框架，通过校准的似然比提供可理解证据。</div>
<div class="card-action">
<a href="toward-interpretable-speech-deepfake-detection-using-artifac-2607-21127/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21127" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="spectrogram-based-joint-detection-localization-and-classific-2607-20817/">Spectrogram-Based Joint Detection, Localization, and Classification of Events in Continuously Recorded IBR Waveforms</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#事件检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于谱图的框架，在逆变器资源终端连续波形中联合检测、定位和分类事件。</div>
<div class="card-action">
<a href="spectrogram-based-joint-detection-localization-and-classific-2607-20817/">详情 →</a> · <a href="https://arxiv.org/abs/2607.20817" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="methods-for-pitch-analysis-in-contemporary-popular-music-phe-2502-08131/">Methods for pitch analysis in contemporary popular music: phenomenological analysis of Primaal's commercial works</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音乐分析</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">通过现象学分析研究当代流行音乐中的音高元素，以Primaal的商业作品为例，揭示音高不确定性等非传统特征。</div>
<div class="card-action">
<a href="methods-for-pitch-analysis-in-contemporary-popular-music-phe-2502-08131/">详情 →</a> · <a href="https://arxiv.org/abs/2502.08131" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="improving-the-performance-of-an-asv-system-using-hybrid-spee-2607-20706/">Improving the performance of an ASV system using hybrid speech features</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#说话人确认</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">研究混合语音特征（MFCC、CQCC、RAB）提升ASV系统在噪声下的性能，实验表明PNCC+RAB组合降低EER。</div>
<div class="card-action">
<a href="improving-the-performance-of-an-asv-system-using-hybrid-spee-2607-20706/">详情 →</a> · <a href="https://arxiv.org/abs/2607.20706" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
