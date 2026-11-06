---
title: "语音/音频论文速递 2026-11-06"
date: 2026-11-06T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 9.2（#乐器分离）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">5</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #语音识别 | 1篇 | `█████` |
| #双耳音频 | 1篇 | `█████` |
| #语音转换 | 1篇 | `█████` |
| #关键词检测 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="route-dmd-distribution-matching-distillation-with-task-route-2611-08011/">Route-DMD: Distribution Matching Distillation with Task-Routed Mechanism for Speech Foundation Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出 Route-DMD，按任务路由蒸馏目标：分离任务改用回归损失，其余保留解耦分布匹配，4 步学生逼近 32 步教师。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="fastwave-optimized-diffusion-model-for-audio-super-resolutio-2603-04122/">FastWave: Optimized Diffusion Model for Audio Super-Resolution</a>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">FastWave 用改进的扩散训练技巧做任意采样率到 48 kHz 的音频超分，仅 1.3M 参数、约 50 GFLOPs，效果优于 NU-Wave 2。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="design-of-a-speech-enhancement-based-deep-semantic-autoencod-2611-07361/">Design of a Speech Enhancement-Based Deep Semantic Autoencoder for Wireless Communications</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">面向无线通信的语音增强型深度语义自编码器，用双分支编码器与自适应噪声解耦提升低SNR下的语义一致性与重建质量。</div>
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
<a class="card-title" href="route-dmd-distribution-matching-distillation-with-task-route-2611-08011/">Route-DMD: Distribution Matching Distillation with Task-Routed Mechanism for Speech Foundation Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出 Route-DMD，按任务路由蒸馏目标：分离任务改用回归损失，其余保留解耦分布匹配，4 步学生逼近 32 步教师。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="auditory-and-visual-virtualization-in-6dof-xr-effects-on-pla-2611-07612/">Auditory and Visual Virtualization in 6DoF XR: Effects on Plausibility and Dynamic Auditory Distance Perception</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">首个在6DoF XR中联合评估实时房间声学模拟与双耳渲染对可信度及动态听觉距离感知影响的感知研究。</div>
</div></div>

### #乐器分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="subroformer-subband-time-domain-representation-for-music-sou-2611-08130/">SubRoformer: Subband Time-Domain Representation for Music Source Separation</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">提出子带时域表示加残差 RoFormer 的 Transformer 系统，在 MUSDB18-HQ 上四轨平均 SDR 达 10.63 dB（目标专属模型）与 11.59 dB（单模型多轨）。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [SubRoformer: Subband Time-Domain Representation for Music So…](subroformer-subband-time-domain-representation-for-music-sou-2611-08130/) 🎯 | **9.2** | #乐器分离 |
| 🥈 | [Route-DMD: Distribution Matching Distillation with Task-Rout…](route-dmd-distribution-matching-distillation-with-task-route-2611-08011/) 🎯 | **8.8** | #语音分离 |
| 🥉 | [FastWave: Optimized Diffusion Model for Audio Super-Resoluti…](fastwave-optimized-diffusion-model-for-audio-super-resolutio-2603-04122/) 🎯 | **8.0** | #语音增强 |
| 4. | [Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recogni…](gabor-gabor-e-gaborformer-a-strictly-causal-speech-recognize-2611-08092/) | **7.8** | #语音识别 |
| 5. | [Auditory and Visual Virtualization in 6DoF XR: Effects on Pl…](auditory-and-visual-virtualization-in-6dof-xr-effects-on-pla-2611-07612/) 🎯 | **7.8** | #双耳音频 |
| 6. | [Adaptive and High-Fidelity Matching Algorithm for Retrieval-…](adaptive-and-high-fidelity-matching-algorithm-for-retrieval--2611-07420/) | **7.2** | #语音转换 |
| 7. | [Design of a Speech Enhancement-Based Deep Semantic Autoencod…](design-of-a-speech-enhancement-based-deep-semantic-autoencod-2611-07361/) 🎯 | **7.0** | #语音增强 |
| 8. | [Implementing Keyword Spotting on the MCXN947 Microcontroller…](implementing-keyword-spotting-on-the-mcxn947-microcontroller-2506-08911/) | **6.0** | #关键词检测 |
| 9. | [FFMT: Frequency-Factorized Multi-Rate Tokenization for Music…](ffmt-frequency-factorized-multi-rate-tokenization-for-music--2611-07384/) | **6.0** | #音乐生成 |
| 10. | [Latent Terrain: Adapting Neural Audio Autoencoders as Design…](latent-terrain-adapting-neural-audio-autoencoders-as-design--2611-07210/) | **5.5** | #音频生成 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="subroformer-subband-time-domain-representation-for-music-sou-2611-08130/">SubRoformer: Subband Time-Domain Representation for Music Source Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出子带时域表示加残差 RoFormer 的 Transformer 系统，在 MUSDB18-HQ 上四轨平均 SDR 达 10.63 dB（目标专属模型）与 11.59 dB（单模型多轨）。</div>
<div class="card-action">
<a href="subroformer-subband-time-domain-representation-for-music-sou-2611-08130/">详情 →</a> · <a href="https://arxiv.org/abs/2611.08130" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="route-dmd-distribution-matching-distillation-with-task-route-2611-08011/">Route-DMD: Distribution Matching Distillation with Task-Routed Mechanism for Speech Foundation Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 Route-DMD，按任务路由蒸馏目标：分离任务改用回归损失，其余保留解耦分布匹配，4 步学生逼近 32 步教师。</div>
<div class="card-action">
<a href="route-dmd-distribution-matching-distillation-with-task-route-2611-08011/">详情 →</a> · <a href="https://arxiv.org/abs/2611.08011" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="fastwave-optimized-diffusion-model-for-audio-super-resolutio-2603-04122/">FastWave: Optimized Diffusion Model for Audio Super-Resolution</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">FastWave 用改进的扩散训练技巧做任意采样率到 48 kHz 的音频超分，仅 1.3M 参数、约 50 GFLOPs，效果优于 NU-Wave 2。</div>
<div class="card-action">
<a href="fastwave-optimized-diffusion-model-for-audio-super-resolutio-2603-04122/">详情 →</a> · <a href="https://arxiv.org/abs/2603.04122" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="gabor-gabor-e-gaborformer-a-strictly-causal-speech-recognize-2611-08092/">Gabor Gabor: E-Gaborformer, a Strictly Causal Speech Recognizer with Gabor-Dictionary Convolutions and Delta-Rule Memory</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出严格因果的E-Gaborformer编码器，用Gabor字典卷积与DeltaNet-2记忆实现恒定显存流式ASR，并在生产级希伯来语/英语转导器上显著降WER。</div>
<div class="card-action">
<a href="gabor-gabor-e-gaborformer-a-strictly-causal-speech-recognize-2611-08092/">详情 →</a> · <a href="https://arxiv.org/abs/2611.08092" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="auditory-and-visual-virtualization-in-6dof-xr-effects-on-pla-2611-07612/">Auditory and Visual Virtualization in 6DoF XR: Effects on Plausibility and Dynamic Auditory Distance Perception</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">首个在6DoF XR中联合评估实时房间声学模拟与双耳渲染对可信度及动态听觉距离感知影响的感知研究。</div>
<div class="card-action">
<a href="auditory-and-visual-virtualization-in-6dof-xr-effects-on-pla-2611-07612/">详情 →</a> · <a href="https://arxiv.org/abs/2611.07612" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="adaptive-and-high-fidelity-matching-algorithm-for-retrieval--2611-07420/">Adaptive and High-Fidelity Matching Algorithm for Retrieval-Based Accent Conversion</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音转换</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出 AA-kNN-AC，用音素覆盖匹配池、各向异性自适应 kNN 与渐进 AdaIN 解码器改进检索式口音转换。</div>
<div class="card-action">
<a href="adaptive-and-high-fidelity-matching-algorithm-for-retrieval--2611-07420/">详情 →</a> · <a href="https://arxiv.org/abs/2611.07420" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="design-of-a-speech-enhancement-based-deep-semantic-autoencod-2611-07361/">Design of a Speech Enhancement-Based Deep Semantic Autoencoder for Wireless Communications</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">面向无线通信的语音增强型深度语义自编码器，用双分支编码器与自适应噪声解耦提升低SNR下的语义一致性与重建质量。</div>
<div class="card-action">
<a href="design-of-a-speech-enhancement-based-deep-semantic-autoencod-2611-07361/">详情 →</a> · <a href="https://arxiv.org/abs/2611.07361" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="implementing-keyword-spotting-on-the-mcxn947-microcontroller-2506-08911/">Implementing Keyword Spotting on the MCXN947 Microcontroller with Integrated NPU</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#关键词检测</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">在集成NPU的MCXN947微控制器上部署MFCC+CNN关键词检测系统，量化感知训练后模型仅30.58KB，NPU推理比CPU快59倍，准确率97.06%。</div>
<div class="card-action">
<a href="implementing-keyword-spotting-on-the-mcxn947-microcontroller-2506-08911/">详情 →</a> · <a href="https://arxiv.org/abs/2506.08911" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="ffmt-frequency-factorized-multi-rate-tokenization-for-music--2611-07384/">FFMT: Frequency-Factorized Multi-Rate Tokenization for Music-to-Dance Generation</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">将舞蹈运动按频率分解为低频编排骨架与高频细节残差，用非对称码本与token率做离散化，并据此设计先规划后细化的自回归生成。</div>
<div class="card-action">
<a href="ffmt-frequency-factorized-multi-rate-tokenization-for-music--2611-07384/">详情 →</a> · <a href="https://arxiv.org/abs/2611.07384" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="latent-terrain-adapting-neural-audio-autoencoders-as-design--2611-07210/">Latent Terrain: Adapting Neural Audio Autoencoders as Design Materials in NIME</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">将神经音频自编码器的潜空间作为生成式声音空间，做成 Max/MSP 工具包供 NIME 创作者使用。</div>
<div class="card-action">
<a href="latent-terrain-adapting-neural-audio-autoencoders-as-design--2611-07210/">详情 →</a> · <a href="https://arxiv.org/abs/2611.07210" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
