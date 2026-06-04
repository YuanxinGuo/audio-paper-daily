---
title: "语音/音频论文速递 2026-06-04"
date: 2026-06-04T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 9.5（#语音分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音分离 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #双耳音频 | 1篇 | `█████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #音频语言模型 | 1篇 | `█████` |
| #AIGC检测 | 1篇 | `█████` |
| #空间音频编码 | 1篇 | `█████` |
| #声场重建 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="the-differentiable-auditory-loop-dal-an-ml-framework-for-hyp-2606-04103/">The Differentiable Auditory Loop (DAL): An ML Framework for Hyper-Personalized Hearing Aids</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出可微分听觉环路框架，结合CARFAC听觉模型与SEANet网络，通过优化听觉神经活动模式实现个性化助听器信号处理。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="feasibility-of-time-domain-dnn-based-speech-enhancement-on-e-2606-04221/">Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">在FPGA上部署轻量级SuDoRM-RF++实现语音增强，首次达到10ms临床延迟阈值。</div>
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
<a class="card-title" href="surf-separation-via-unsupervised-remixing-flow-2606-04921/">SURF: Separation via Unsupervised Remixing Flow</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出SURF，一种无监督流匹配方法，仅从混合信号学习源分离，无需干净源数据，在图像和音频基准上达到新SOTA。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-study-of-the-scale-invariant-signal-to-distortion-ratio-in-2508-14623/">A Study of the Scale Invariant Signal to Distortion Ratio in Speech Separation with Noisy References</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">研究语音分离中SI-SDR指标在含噪参考下的局限性，提出增强参考和混合数据的方法以缓解噪声学习问题。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="flow-hoa-generative-joint-optimization-for-ambisonics-encodi-2606-04570/">Flow-HOA: Generative Joint Optimization for Ambisonics Encoding via Flow Matching</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出Flow-HOA，利用条件流匹配联合优化时域、频谱和空间保真度，生成可部署的FIR编码滤波器组，用于从稀疏麦克风阵列进行高阶Ambisonics编码。</div>
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
| 🥇 | [SURF: Separation via Unsupervised Remixing Flow](surf-separation-via-unsupervised-remixing-flow-2606-04921/) 🎯 | **9.5** | #语音分离 |
| 🥈 | [Flow-HOA: Generative Joint Optimization for Ambisonics Encod…](flow-hoa-generative-joint-optimization-for-ambisonics-encodi-2606-04570/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [The Differentiable Auditory Loop (DAL): An ML Framework for …](the-differentiable-auditory-loop-dal-an-ml-framework-for-hyp-2606-04103/) 🎯 | **8.8** | #语音增强 |
| 4. | [FoeGlass: Simple In-Context Learning Is Enough for Red Teami…](foeglass-simple-in-context-learning-is-enough-for-red-teamin-2606-05101/) | **8.2** | #音频深度伪造检测 |
| 5. | [A Study of the Scale Invariant Signal to Distortion Ratio in…](a-study-of-the-scale-invariant-signal-to-distortion-ratio-in-2508-14623/) 🎯 | **8.2** | #语音分离 |
| 6. | [Feasibility of Time-Domain DNN-Based Speech Enhancement on E…](feasibility-of-time-domain-dnn-based-speech-enhancement-on-e-2606-04221/) 🎯 | **8.2** | #语音增强 |
| 7. | [Beyond Text Following: Repairable Arbitration Reversals in A…](beyond-text-following-repairable-arbitration-reversals-in-au-2606-05161/) | **7.8** | #音频语言模型 |
| 8. | [DetectZoo: A Unified Toolkit for AI-Generated Content Detect…](detectzoo-a-unified-toolkit-for-ai-generated-content-detecti-2606-04205/) | **7.2** | #AIGC检测 |
| 9. | [SHB-AE: Spherical harmonic beamforming based Ambisonics enco…](shb-ae-spherical-harmonic-beamforming-based-ambisonics-encod-2606-04584/) | **7.2** | #空间音频编码 |
| 10. | [Masked Wavelet Scattering Transform Neural Field for Sound F…](masked-wavelet-scattering-transform-neural-field-for-sound-f-2606-04370/) | **6.8** | #声场重建 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="surf-separation-via-unsupervised-remixing-flow-2606-04921/">SURF: Separation via Unsupervised Remixing Flow</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出SURF，一种无监督流匹配方法，仅从混合信号学习源分离，无需干净源数据，在图像和音频基准上达到新SOTA。</div>
<div class="card-action">
<a href="surf-separation-via-unsupervised-remixing-flow-2606-04921/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04921" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="flow-hoa-generative-joint-optimization-for-ambisonics-encodi-2606-04570/">Flow-HOA: Generative Joint Optimization for Ambisonics Encoding via Flow Matching</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Flow-HOA，利用条件流匹配联合优化时域、频谱和空间保真度，生成可部署的FIR编码滤波器组，用于从稀疏麦克风阵列进行高阶Ambisonics编码。</div>
<div class="card-action">
<a href="flow-hoa-generative-joint-optimization-for-ambisonics-encodi-2606-04570/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04570" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="the-differentiable-auditory-loop-dal-an-ml-framework-for-hyp-2606-04103/">The Differentiable Auditory Loop (DAL): An ML Framework for Hyper-Personalized Hearing Aids</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出可微分听觉环路框架，结合CARFAC听觉模型与SEANet网络，通过优化听觉神经活动模式实现个性化助听器信号处理。</div>
<div class="card-action">
<a href="the-differentiable-auditory-loop-dal-an-ml-framework-for-hyp-2606-04103/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04103" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="foeglass-simple-in-context-learning-is-enough-for-red-teamin-2606-05101/">FoeGlass: Simple In-Context Learning Is Enough for Red Teaming Audio Deepfake Detectors</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个黑盒自动化红队方法FoeGlass，利用LLM的上下文学习能力探索TTS输入空间，生成欺骗ADD模型的音频样本，无需人工监督。</div>
<div class="card-action">
<a href="foeglass-simple-in-context-learning-is-enough-for-red-teamin-2606-05101/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05101" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="a-study-of-the-scale-invariant-signal-to-distortion-ratio-in-2508-14623/">A Study of the Scale Invariant Signal to Distortion Ratio in Speech Separation with Noisy References</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">研究语音分离中SI-SDR指标在含噪参考下的局限性，提出增强参考和混合数据的方法以缓解噪声学习问题。</div>
<div class="card-action">
<a href="a-study-of-the-scale-invariant-signal-to-distortion-ratio-in-2508-14623/">详情 →</a> · <a href="https://arxiv.org/abs/2508.14623" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="feasibility-of-time-domain-dnn-based-speech-enhancement-on-e-2606-04221/">Feasibility of Time-Domain DNN-Based Speech Enhancement on Embedded FPGA for Hearing Aid</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">在FPGA上部署轻量级SuDoRM-RF++实现语音增强，首次达到10ms临床延迟阈值。</div>
<div class="card-action">
<a href="feasibility-of-time-domain-dnn-based-speech-enhancement-on-e-2606-04221/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04221" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="beyond-text-following-repairable-arbitration-reversals-in-au-2606-05161/">Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频语言模型</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">发现音频语言模型中文本与音频冲突时，音频证据被编码但被文本覆盖，提出无需训练的解码策略GACL来修正。</div>
<div class="card-action">
<a href="beyond-text-following-repairable-arbitration-reversals-in-au-2606-05161/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05161" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="detectzoo-a-unified-toolkit-for-ai-generated-content-detecti-2606-04205/">DetectZoo: A Unified Toolkit for AI-Generated Content Detection Across Text, Audio, and Image Modalities</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#AIGC检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">DetectZoo是一个统一的多模态AIGC检测工具包，集成了61个检测器、22个基准数据集和标准化评估流程。</div>
<div class="card-action">
<a href="detectzoo-a-unified-toolkit-for-ai-generated-content-detecti-2606-04205/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04205" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="shb-ae-spherical-harmonic-beamforming-based-ambisonics-encod-2606-04584/">SHB-AE: Spherical harmonic beamforming based Ambisonics encoding and upscaling method for smartphone microphone array</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#空间音频编码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于球谐波束形成的Ambisonics编码与升阶方法，利用智能手机四麦克风阵列实现四阶Ambisonics编码。</div>
<div class="card-action">
<a href="shb-ae-spherical-harmonic-beamforming-based-ambisonics-encod-2606-04584/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04584" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="masked-wavelet-scattering-transform-neural-field-for-sound-f-2606-04370/">Masked Wavelet Scattering Transform Neural Field for Sound Field Reconstruction</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#声场重建</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于掩蔽小波散射变换的神经场框架，用于声场重建，以HRTF上采样为验证任务。</div>
<div class="card-action">
<a href="masked-wavelet-scattering-transform-neural-field-for-sound-f-2606-04370/">详情 →</a> · <a href="https://arxiv.org/abs/2606.04370" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
