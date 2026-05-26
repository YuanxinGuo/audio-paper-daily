---
title: "语音/音频论文速递 2026-05-26"
date: 2026-05-26T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 9.2（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #语音分离 | 1篇 | `█████` |
| #音频-视觉定位与推理 | 1篇 | `█████` |
| #语音编辑检测 | 1篇 | `█████` |
| #语音表示学习 | 1篇 | `█████` |
| #音频水印 | 1篇 | `█████` |
| #音视频生成评估 | 1篇 | `█████` |
| #音频对抗攻击 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="diffusion-based-frameworks-for-unsupervised-speech-enhanceme-2601-09931/">Diffusion-based Frameworks for Unsupervised Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出无监督扩散语音增强框架，显式联合建模语音和噪声，在WSJ0-QUT和VoiceBank-DEMAND上优于现有无监督方法。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="focus-then-listen-exploring-plug-and-play-audio-enhancer-for-2603-04862/">Focus Then Listen: Exploring Plug-and-Play Audio Enhancer for Noise-Robust Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出即插即用的音频增强模块FTL，通过语音/非语音分离和模态路由，提升大音频语言模型在噪声环境下的鲁棒性，无需微调。</div>
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
<a class="card-title" href="focus-then-listen-exploring-plug-and-play-audio-enhancer-for-2603-04862/">Focus Then Listen: Exploring Plug-and-Play Audio Enhancer for Noise-Robust Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出即插即用的音频增强模块FTL，通过语音/非语音分离和模态路由，提升大音频语言模型在噪声环境下的鲁棒性，无需微调。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="cstmm-a-unified-complex-spherical-student-s-t-mixture-model--2605-25512/">cSTMM: A Unified Complex Spherical Student's $t$ Mixture Model for Directional Statistics in Mask-Based Blind Speech Separation</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">提出复球面学生t混合模型(cSTMM)，统一了cACGMM、cBMM、cWMM三种方向统计模型，通过自由度参数ν连接，在混响语音分离中取得优于cACGMM的SDRi。</div>
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
| 🥇 | [Diffusion-based Frameworks for Unsupervised Speech Enhanceme…](diffusion-based-frameworks-for-unsupervised-speech-enhanceme-2601-09931/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [Focus Then Listen: Exploring Plug-and-Play Audio Enhancer fo…](focus-then-listen-exploring-plug-and-play-audio-enhancer-for-2603-04862/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [cSTMM: A Unified Complex Spherical Student's $t$ Mixture Mod…](cstmm-a-unified-complex-spherical-student-s-t-mixture-model--2605-25512/) 🎯 | **8.8** | #语音分离 |
| 4. | [JAEGER: Joint 3D Audio-Visual Grounding and Reasoning in Sim…](jaeger-joint-3d-audio-visual-grounding-and-reasoning-in-simu-2602-18527/) | **8.5** | #音频-视觉定位与推理 |
| 5. | [Unifying Speech Editing Detection and Content Localization v…](unifying-speech-editing-detection-and-content-localization-v-2601-21463/) | **8.2** | #语音编辑检测 |
| 6. | [On the Distillation Loss Functions of Speech VAE for Unified…](on-the-distillation-loss-functions-of-speech-vae-for-unified-2604-12383/) | **7.8** | #语音表示学习 |
| 7. | [Hidden in Plain Tokens: Simply Robust, Gradient-Free Waterma…](hidden-in-plain-tokens-simply-robust-gradient-free-watermark-2605-25967/) | **7.8** | #音频水印 |
| 8. | [AVBench: Human-Aligned and Automated Evaluation Benchmark fo…](avbench-human-aligned-and-automated-evaluation-benchmark-for-2605-24652/) | **7.8** | #音视频生成评估 |
| 9. | [Sparse Tokens Suffice: Jailbreaking Audio Language Models vi…](sparse-tokens-suffice-jailbreaking-audio-language-models-via-2605-04700/) | **7.5** | #音频对抗攻击 |
| 10. | [Exploration of Perceptual Speech Features for Clinical Decis…](exploration-of-perceptual-speech-features-for-clinical-decis-2605-24678/) | **6.8** | #语音特征分析 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="diffusion-based-frameworks-for-unsupervised-speech-enhanceme-2601-09931/">Diffusion-based Frameworks for Unsupervised Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出无监督扩散语音增强框架，显式联合建模语音和噪声，在WSJ0-QUT和VoiceBank-DEMAND上优于现有无监督方法。</div>
<div class="card-action">
<a href="diffusion-based-frameworks-for-unsupervised-speech-enhanceme-2601-09931/">详情 →</a> · <a href="https://arxiv.org/abs/2601.09931" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="focus-then-listen-exploring-plug-and-play-audio-enhancer-for-2603-04862/">Focus Then Listen: Exploring Plug-and-Play Audio Enhancer for Noise-Robust Large Audio Language Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出即插即用的音频增强模块FTL，通过语音/非语音分离和模态路由，提升大音频语言模型在噪声环境下的鲁棒性，无需微调。</div>
<div class="card-action">
<a href="focus-then-listen-exploring-plug-and-play-audio-enhancer-for-2603-04862/">详情 →</a> · <a href="https://arxiv.org/abs/2603.04862" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="cstmm-a-unified-complex-spherical-student-s-t-mixture-model--2605-25512/">cSTMM: A Unified Complex Spherical Student's $t$ Mixture Model for Directional Statistics in Mask-Based Blind Speech Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出复球面学生t混合模型(cSTMM)，统一了cACGMM、cBMM、cWMM三种方向统计模型，通过自由度参数ν连接，在混响语音分离中取得优于cACGMM的SDRi。</div>
<div class="card-action">
<a href="cstmm-a-unified-complex-spherical-student-s-t-mixture-model--2605-25512/">详情 →</a> · <a href="https://arxiv.org/abs/2605.25512" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="jaeger-joint-3d-audio-visual-grounding-and-reasoning-in-simu-2602-18527/">JAEGER: Joint 3D Audio-Visual Grounding and Reasoning in Simulated Physical Environments</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音频-视觉定位与推理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出JAEGER框架，将音频-视觉大模型扩展到3D空间，通过RGB-D和一级环境声实现联合空间定位与推理。</div>
<div class="card-action">
<a href="jaeger-joint-3d-audio-visual-grounding-and-reasoning-in-simu-2602-18527/">详情 →</a> · <a href="https://arxiv.org/abs/2602.18527" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="unifying-speech-editing-detection-and-content-localization-v-2601-21463/">Unifying Speech Editing Detection and Content Localization via Prior-Enhanced Audio LLMs</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音编辑检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于音频大语言模型的统一框架，将语音编辑检测与内容定位重构为结构化文本生成任务，并引入先验增强提示和声学一致性损失。</div>
<div class="card-action">
<a href="unifying-speech-editing-detection-and-content-localization-v-2601-21463/">详情 →</a> · <a href="https://arxiv.org/abs/2601.21463" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="on-the-distillation-loss-functions-of-speech-vae-for-unified-2604-12383/">On the Distillation Loss Functions of Speech VAE for Unified Reconstruction, Understanding, and Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音表示学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统研究语音VAE中不同蒸馏损失对齐方式对重建、理解、生成三类任务的影响，提出联合边缘对齐与自适应加权方法。</div>
<div class="card-action">
<a href="on-the-distillation-loss-functions-of-speech-vae-for-unified-2604-12383/">详情 →</a> · <a href="https://arxiv.org/abs/2604.12383" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="hidden-in-plain-tokens-simply-robust-gradient-free-watermark-2605-25967/">Hidden in Plain Tokens: Simply Robust, Gradient-Free Watermark for Synthetic Audio</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频水印</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种无需微调tokenizer的梯度自由音频水印方法，通过社区检测缩减词汇表提升检测鲁棒性。</div>
<div class="card-action">
<a href="hidden-in-plain-tokens-simply-robust-gradient-free-watermark-2605-25967/">详情 →</a> · <a href="https://arxiv.org/abs/2605.25967" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="avbench-human-aligned-and-automated-evaluation-benchmark-for-2605-24652/">AVBench: Human-Aligned and Automated Evaluation Benchmark for Audio-Video Generative Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音视频生成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出AVBench，一个面向人类中心音视频生成的自动化评估基准，包含细粒度指标和通过偏好学习训练的专业评估器。</div>
<div class="card-action">
<a href="avbench-human-aligned-and-automated-evaluation-benchmark-for-2605-24652/">详情 →</a> · <a href="https://arxiv.org/abs/2605.24652" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="sparse-tokens-suffice-jailbreaking-audio-language-models-via-2605-04700/">Sparse Tokens Suffice: Jailbreaking Audio Language Models via Token-Aware Gradient Optimization</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#音频对抗攻击</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Token-Aware Gradient Optimization (TAGO)，通过保留高梯度能量的音频token对应波形梯度，实现稀疏越狱攻击，证明密集波形更新冗余。</div>
<div class="card-action">
<a href="sparse-tokens-suffice-jailbreaking-audio-language-models-via-2605-04700/">详情 →</a> · <a href="https://arxiv.org/abs/2605.04700" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="exploration-of-perceptual-speech-features-for-clinical-decis-2605-24678/">Exploration of Perceptual Speech Features for Clinical Decision-Support in Mental Health Care</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音特征分析</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出基于感知语音特征的分析框架，结合声学与语言特征，用可解释机器学习分析抑郁、焦虑、ADHD与语音关联。</div>
<div class="card-action">
<a href="exploration-of-perceptual-speech-features-for-clinical-decis-2605-24678/">详情 →</a> · <a href="https://arxiv.org/abs/2605.24678" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
