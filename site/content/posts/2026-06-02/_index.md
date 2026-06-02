---
title: "语音/音频论文速递 2026-06-02"
date: 2026-06-02T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 8 篇 · 重点领域 6 篇 · 最高分 9.2（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">8</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">6</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 2篇 | `██████████` |
| #语音增强 | 2篇 | `██████████` |
| #音频表示学习 | 1篇 | `█████` |
| #说话人日志 | 1篇 | `█████` |
| #声源定位 | 1篇 | `█████` |
| #声音事件检测与分离 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="exploiting-noise-inseparability-for-weakly-supervised-discri-2606-02327/">Exploiting Noise Inseparability for Weakly-Supervised Discriminative Speech Denoising Using Noisy Targets</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">利用噪声不可分离性，通过噪声估计抵消残差噪声，实现弱监督语音去噪，支持联合训练人工与自然噪声数据。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="advancing-electrolaryngeal-speech-enhancement-through-speech-2606-01905/">Advancing Electrolaryngeal Speech Enhancement Through Speech-Text Representation Learning</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种融合语音和文本表征的seq2seq语音转换框架，用于将电子喉语音增强为自然语音，通过多级融合策略和重构损失提升映射质量。</div>
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
<a class="card-title" href="echo-a-joint-embedding-predictive-architecture-for-speaker-d-2606-01909/">Echo: A Joint-Embedding Predictive Architecture for Speaker Diarization and Speech Recognition in a Shared Latent Space</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
</div>
<div class="card-tldr">Echo提出单一ViT编码器，通过JEPA预训练和分阶段特化，在共享潜在空间中同时支持说话人日志、语音分离和语音识别，无需任务特定微调。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="hrtfformer-a-spatially-aware-transformer-for-individual-hrtf-2510-01891/">HRTFformer: A Spatially-Aware Transformer for Individual HRTF Upsampling in Immersive Audio Rendering</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出HRTFformer，利用Transformer在球谐域对稀疏测量的HRTF进行高保真上采样，引入邻域差异损失提升空间平滑性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="diffau-diffusion-based-ambisonics-upscaling-2510-00180/">DiffAU: Diffusion-Based Ambisonics Upscaling</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出DiffAU，利用扩散模型将一阶Ambisonics上采样到三阶，提升空间音频分辨率。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="systematic-evaluation-of-time-frequency-features-for-binaura-2511-13487/">Systematic Evaluation of Time-Frequency Features for Binaural Sound Source Localization</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#声源定位</span>
</div>
<div class="card-tldr">系统评估双耳声源定位中时频特征组合对CNN性能的影响，发现精心选择的特征组合可超越增加模型复杂度。</div>
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
| 🥇 | [HRTFformer: A Spatially-Aware Transformer for Individual HRT…](hrtfformer-a-spatially-aware-transformer-for-individual-hrtf-2510-01891/) 🎯 | **9.2** | #双耳音频 |
| 🥈 | [DiffAU: Diffusion-Based Ambisonics Upscaling](diffau-diffusion-based-ambisonics-upscaling-2510-00180/) 🎯 | **8.8** | #双耳音频 |
| 🥉 | [Exploiting Noise Inseparability for Weakly-Supervised Discri…](exploiting-noise-inseparability-for-weakly-supervised-discri-2606-02327/) 🎯 | **8.8** | #语音增强 |
| 4. | [Advancing Electrolaryngeal Speech Enhancement Through Speech…](advancing-electrolaryngeal-speech-enhancement-through-speech-2606-01905/) 🎯 | **8.8** | #语音增强 |
| 5. | [VocSim: A Training-free Benchmark for Zero-shot Content Iden…](vocsim-a-training-free-benchmark-for-zero-shot-content-ident-2512-10120/) | **8.2** | #音频表示学习 |
| 6. | [Echo: A Joint-Embedding Predictive Architecture for Speaker …](echo-a-joint-embedding-predictive-architecture-for-speaker-d-2606-01909/) 🎯 | **8.2** | #说话人日志 |
| 7. | [Systematic Evaluation of Time-Frequency Features for Binaura…](systematic-evaluation-of-time-frequency-features-for-binaura-2511-13487/) 🎯 | **7.5** | #声源定位 |
| 8. | [Description and Discussion on DCASE 2026 Challenge Task 4: S…](description-and-discussion-on-dcase-2026-challenge-task-4-sp-2604-00776/) | **7.2** | #声音事件检测与分离 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="hrtfformer-a-spatially-aware-transformer-for-individual-hrtf-2510-01891/">HRTFformer: A Spatially-Aware Transformer for Individual HRTF Upsampling in Immersive Audio Rendering</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出HRTFformer，利用Transformer在球谐域对稀疏测量的HRTF进行高保真上采样，引入邻域差异损失提升空间平滑性。</div>
<div class="card-action">
<a href="hrtfformer-a-spatially-aware-transformer-for-individual-hrtf-2510-01891/">详情 →</a> · <a href="https://arxiv.org/abs/2510.01891" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="diffau-diffusion-based-ambisonics-upscaling-2510-00180/">DiffAU: Diffusion-Based Ambisonics Upscaling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出DiffAU，利用扩散模型将一阶Ambisonics上采样到三阶，提升空间音频分辨率。</div>
<div class="card-action">
<a href="diffau-diffusion-based-ambisonics-upscaling-2510-00180/">详情 →</a> · <a href="https://arxiv.org/abs/2510.00180" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="exploiting-noise-inseparability-for-weakly-supervised-discri-2606-02327/">Exploiting Noise Inseparability for Weakly-Supervised Discriminative Speech Denoising Using Noisy Targets</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">利用噪声不可分离性，通过噪声估计抵消残差噪声，实现弱监督语音去噪，支持联合训练人工与自然噪声数据。</div>
<div class="card-action">
<a href="exploiting-noise-inseparability-for-weakly-supervised-discri-2606-02327/">详情 →</a> · <a href="https://arxiv.org/abs/2606.02327" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="advancing-electrolaryngeal-speech-enhancement-through-speech-2606-01905/">Advancing Electrolaryngeal Speech Enhancement Through Speech-Text Representation Learning</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种融合语音和文本表征的seq2seq语音转换框架，用于将电子喉语音增强为自然语音，通过多级融合策略和重构损失提升映射质量。</div>
<div class="card-action">
<a href="advancing-electrolaryngeal-speech-enhancement-through-speech-2606-01905/">详情 →</a> · <a href="https://arxiv.org/abs/2606.01905" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="vocsim-a-training-free-benchmark-for-zero-shot-content-ident-2512-10120/">VocSim: A Training-free Benchmark for Zero-shot Content Identity in Single-source Audio</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频表示学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出VocSim，一个无需训练的基准，用于评估冻结音频嵌入在零样本内容身份识别中的几何对齐能力，涵盖语音、动物叫声和环境声音。</div>
<div class="card-action">
<a href="vocsim-a-training-free-benchmark-for-zero-shot-content-ident-2512-10120/">详情 →</a> · <a href="https://arxiv.org/abs/2512.10120" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="echo-a-joint-embedding-predictive-architecture-for-speaker-d-2606-01909/">Echo: A Joint-Embedding Predictive Architecture for Speaker Diarization and Speech Recognition in a Shared Latent Space</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#说话人日志</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">Echo提出单一ViT编码器，通过JEPA预训练和分阶段特化，在共享潜在空间中同时支持说话人日志、语音分离和语音识别，无需任务特定微调。</div>
<div class="card-action">
<a href="echo-a-joint-embedding-predictive-architecture-for-speaker-d-2606-01909/">详情 →</a> · <a href="https://arxiv.org/abs/2606.01909" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="systematic-evaluation-of-time-frequency-features-for-binaura-2511-13487/">Systematic Evaluation of Time-Frequency Features for Binaural Sound Source Localization</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#声源定位</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">系统评估双耳声源定位中时频特征组合对CNN性能的影响，发现精心选择的特征组合可超越增加模型复杂度。</div>
<div class="card-action">
<a href="systematic-evaluation-of-time-frequency-features-for-binaura-2511-13487/">详情 →</a> · <a href="https://arxiv.org/abs/2511.13487" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="description-and-discussion-on-dcase-2026-challenge-task-4-sp-2604-00776/">Description and Discussion on DCASE 2026 Challenge Task 4: Spatial Semantic Segmentation of Sound Scenes</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#声音事件检测与分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">DCASE 2026挑战赛任务4：空间语义分割（S5），聚焦复杂空间音频中声音事件的联合检测与分离，并更新了数据集和评估指标。</div>
<div class="card-action">
<a href="description-and-discussion-on-dcase-2026-challenge-task-4-sp-2604-00776/">详情 →</a> · <a href="https://arxiv.org/abs/2604.00776" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
