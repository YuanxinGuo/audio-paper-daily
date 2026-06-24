---
title: "语音/音频论文速递 2026-06-24"
date: 2026-06-24T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 8 篇 · 最高分 9.2（#目标说话人提取）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">8</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.2</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 3篇 | `██████████` |
| #双耳音频 | 2篇 | `███████` |
| #目标说话人提取 | 1篇 | `███` |
| #声音场景分割 | 1篇 | `███` |
| #音乐生成 | 1篇 | `███` |
| #语音处理 | 1篇 | `███` |
| #空间音频编码 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-fast-solver-for-interpolating-stochastic-differential-equa-2603-09508/">A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种针对插值随机微分方程扩散模型的快速求解器，在语音修复任务中仅需10步网络评估即可达到高质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="beyond-u-net-a-latent-representation-aligned-skip-free-backb-2606-24745/">Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种无跳跃连接的编码器-解码器架构，通过潜在表示对齐替代U-Net跳跃连接，用于流匹配语音增强。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="neuromorphic-speech-enhancement-with-dual-branch-spiking-neu-2606-23761/">Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出双分支脉冲神经网络GSU-DBNet，通过门控脉冲单元联合建模幅度和复数谱，以极低参数量实现优于现有SNN方法的语音增强性能。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="balalaika-data-centric-prosody-aware-annotation-pipeline-for-2507-13563/">Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音处理</span>
</div>
<div class="card-tldr">提出Balalaika开源数据标注流水线，结合语义VAD、多ASR集成和自动过滤，构建5.1k小时俄语语料库，提升语音增强和TTS性能。</div>
</div></div>

### #目标说话人提取

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="breaking-shortcut-learning-for-cross-trial-eeg-guided-target-2606-24164/">Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
</div>
<div class="card-tldr">提出两阶段训练框架TRUST-TSE，通过对比预训练抑制试次特异性捷径学习，提升跨试次EEG引导目标语音提取的泛化性。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="a-multi-stage-separation-and-classification-framework-guided-2606-24512/">A Multi-Stage Separation-and-Classification Framework Guided by Complementary Acoustic-to-Semantic Clues</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#声音场景分割</span>
</div>
<div class="card-tldr">提出多阶段分离-分类框架，利用声学与语义互补线索迭代优化，在DCASE 2026 S5任务上显著超越基线。</div>
</div></div>

### #双耳音频

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="statistical-validation-and-full-sphere-extension-of-a-bayesi-2606-24367/">Statistical validation and full-sphere extension of a Bayesian model for human static sound localisation</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">提出贝叶斯声源定位模型的显式似然函数，并通过参数恢复和行为拟合验证其可靠性，同时用于比较HRTF插值方法。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="evaluation-of-headrest-integrated-loudspeakers-for-enhanced--2606-24146/">Evaluation of Headrest-Integrated Loudspeakers for Enhanced Spatial Audio Immersion in Automotive Cabins</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">通过主观听音实验评估汽车头枕集成扬声器对沉浸式空间音频感知的提升效果。</div>
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
| 🥇 | [Breaking Shortcut Learning for Cross-Trial EEG-Guided Target…](breaking-shortcut-learning-for-cross-trial-eeg-guided-target-2606-24164/) 🎯 | **9.2** | #目标说话人提取 |
| 🥈 | [A Fast Solver for Interpolating Stochastic Differential Equa…](a-fast-solver-for-interpolating-stochastic-differential-equa-2603-09508/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [Beyond U-Net: A Latent-Representation-Aligned Skip-Free Back…](beyond-u-net-a-latent-representation-aligned-skip-free-backb-2606-24745/) 🎯 | **8.8** | #语音增强 |
| 4. | [Neuromorphic Speech Enhancement with Dual-Branch Spiking Neu…](neuromorphic-speech-enhancement-with-dual-branch-spiking-neu-2606-23761/) 🎯 | **8.8** | #语音增强 |
| 5. | [A Multi-Stage Separation-and-Classification Framework Guided…](a-multi-stage-separation-and-classification-framework-guided-2606-24512/) 🎯 | **8.8** | #声音场景分割 |
| 6. | [Statistical validation and full-sphere extension of a Bayesi…](statistical-validation-and-full-sphere-extension-of-a-bayesi-2606-24367/) 🎯 | **8.5** | #双耳音频 |
| 7. | [HAFM: Hierarchical Autoregressive Foundation Model for Music…](hafm-hierarchical-autoregressive-foundation-model-for-music--2604-09054/) | **8.2** | #音乐生成 |
| 8. | [Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline f…](balalaika-data-centric-prosody-aware-annotation-pipeline-for-2507-13563/) 🎯 | **8.2** | #语音处理 |
| 9. | [Evaluation of Headrest-Integrated Loudspeakers for Enhanced …](evaluation-of-headrest-integrated-loudspeakers-for-enhanced--2606-24146/) 🎯 | **7.5** | #双耳音频 |
| 10. | [Perceptual Evaluation of Higher-Order Ambisonic Codecs on Bo…](perceptual-evaluation-of-higher-order-ambisonic-codecs-on-bo-2606-24661/) | **7.2** | #空间音频编码 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="breaking-shortcut-learning-for-cross-trial-eeg-guided-target-2606-24164/">Breaking Shortcut Learning for Cross-Trial EEG-Guided Target Speech Extraction via Two-Stage Training</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#目标说话人提取</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出两阶段训练框架TRUST-TSE，通过对比预训练抑制试次特异性捷径学习，提升跨试次EEG引导目标语音提取的泛化性。</div>
<div class="card-action">
<a href="breaking-shortcut-learning-for-cross-trial-eeg-guided-target-2606-24164/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24164" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="a-fast-solver-for-interpolating-stochastic-differential-equa-2603-09508/">A Fast Solver for Interpolating Stochastic Differential Equation Diffusion Models for Speech Restoration</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种针对插值随机微分方程扩散模型的快速求解器，在语音修复任务中仅需10步网络评估即可达到高质量。</div>
<div class="card-action">
<a href="a-fast-solver-for-interpolating-stochastic-differential-equa-2603-09508/">详情 →</a> · <a href="https://arxiv.org/abs/2603.09508" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="beyond-u-net-a-latent-representation-aligned-skip-free-backb-2606-24745/">Beyond U-Net: A Latent-Representation-Aligned Skip-Free Backbone for Flow-Matching Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种无跳跃连接的编码器-解码器架构，通过潜在表示对齐替代U-Net跳跃连接，用于流匹配语音增强。</div>
<div class="card-action">
<a href="beyond-u-net-a-latent-representation-aligned-skip-free-backb-2606-24745/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24745" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="neuromorphic-speech-enhancement-with-dual-branch-spiking-neu-2606-23761/">Neuromorphic Speech Enhancement with Dual-Branch Spiking Neural Networks</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双分支脉冲神经网络GSU-DBNet，通过门控脉冲单元联合建模幅度和复数谱，以极低参数量实现优于现有SNN方法的语音增强性能。</div>
<div class="card-action">
<a href="neuromorphic-speech-enhancement-with-dual-branch-spiking-neu-2606-23761/">详情 →</a> · <a href="https://arxiv.org/abs/2606.23761" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="a-multi-stage-separation-and-classification-framework-guided-2606-24512/">A Multi-Stage Separation-and-Classification Framework Guided by Complementary Acoustic-to-Semantic Clues</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#声音场景分割</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出多阶段分离-分类框架，利用声学与语义互补线索迭代优化，在DCASE 2026 S5任务上显著超越基线。</div>
<div class="card-action">
<a href="a-multi-stage-separation-and-classification-framework-guided-2606-24512/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24512" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="statistical-validation-and-full-sphere-extension-of-a-bayesi-2606-24367/">Statistical validation and full-sphere extension of a Bayesian model for human static sound localisation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出贝叶斯声源定位模型的显式似然函数，并通过参数恢复和行为拟合验证其可靠性，同时用于比较HRTF插值方法。</div>
<div class="card-action">
<a href="statistical-validation-and-full-sphere-extension-of-a-bayesi-2606-24367/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24367" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="hafm-hierarchical-autoregressive-foundation-model-for-music--2604-09054/">HAFM: Hierarchical Autoregressive Foundation Model for Music Accompaniment Generation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出分层自回归基础模型HAFM，通过双速率标记化和三阶段级联生成，实现人声引导的音乐伴奏生成。</div>
<div class="card-action">
<a href="hafm-hierarchical-autoregressive-foundation-model-for-music--2604-09054/">详情 →</a> · <a href="https://arxiv.org/abs/2604.09054" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="balalaika-data-centric-prosody-aware-annotation-pipeline-for-2507-13563/">Balalaika: Data-Centric, Prosody-Aware Annotation Pipeline for Russian Speech</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音处理</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出Balalaika开源数据标注流水线，结合语义VAD、多ASR集成和自动过滤，构建5.1k小时俄语语料库，提升语音增强和TTS性能。</div>
<div class="card-action">
<a href="balalaika-data-centric-prosody-aware-annotation-pipeline-for-2507-13563/">详情 →</a> · <a href="https://arxiv.org/abs/2507.13563" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="evaluation-of-headrest-integrated-loudspeakers-for-enhanced--2606-24146/">Evaluation of Headrest-Integrated Loudspeakers for Enhanced Spatial Audio Immersion in Automotive Cabins</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过主观听音实验评估汽车头枕集成扬声器对沉浸式空间音频感知的提升效果。</div>
<div class="card-action">
<a href="evaluation-of-headrest-integrated-loudspeakers-for-enhanced--2606-24146/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24146" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="perceptual-evaluation-of-higher-order-ambisonic-codecs-on-bo-2606-24661/">Perceptual Evaluation of Higher-Order Ambisonic Codecs on Both Synthetic Mixing and Native Recordings</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#空间音频编码</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">评估IVAS编解码器对高阶Ambisonics内容的压缩性能，相比多单声道方法在相同码率下更优，尤其适用于高通道相关信号。</div>
<div class="card-action">
<a href="perceptual-evaluation-of-higher-order-ambisonic-codecs-on-bo-2606-24661/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24661" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
