---
title: "语音/音频论文速递 2026-11-20"
date: 2026-11-20T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 5 篇 · 重点领域 0 篇 · 最高分 7.0（#语音合成）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">5</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">0</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">7.0</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音合成 | 1篇 | `██████████` |
| #音频生成 | 1篇 | `██████████` |
| #语音交互评测 | 1篇 | `██████████` |
| #语音生成 | 1篇 | `██████████` |
| #声学模拟 | 1篇 | `██████████` |

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
| 🥇 | [Rhythm-TTS: High-Fidelity Shortcut Latent Modeling and Proba…](rhythm-tts-high-fidelity-shortcut-latent-modeling-and-probab-2510-02848/) | **7.0** | #语音合成 |
| 🥈 | [AudioTurbo: Fast Text-to-Audio Generation with Rectified Dif…](audioturbo-fast-text-to-audio-generation-with-rectified-diff-2505-22106/) | **7.0** | #音频生成 |
| 🥉 | [TELEVAL: A Benchmark Designed for Spoken Language Models in …](televal-a-benchmark-designed-for-spoken-language-models-in-c-2507-18061/) | **6.8** | #语音交互评测 |
| 4. | [The landscape of AI speech generation and deepfake detection](the-landscape-of-ai-speech-generation-and-deepfake-detection-2611-24993/) | **4.5** | #语音生成 |
| 5. | [Modeling and Link Budget Feasibility Analysis of Secure LoRa…](modeling-and-link-budget-feasibility-analysis-of-secure-lora-2602-23924/) | **3.5** | #声学模拟 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="rhythm-tts-high-fidelity-shortcut-latent-modeling-and-probab-2510-02848/">Rhythm-TTS: High-Fidelity Shortcut Latent Modeling and Probabilistic Rhythm Generation for Zero-Shot Text-to-Speech</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用离散codec token作语义-声学先验，流匹配直接生成连续语音latent，并加入概率化时长与静音生成器提升韵律多样性。</div>
<div class="card-action">
<a href="rhythm-tts-high-fidelity-shortcut-latent-modeling-and-probab-2510-02848/">详情 →</a> · <a href="https://arxiv.org/abs/2510.02848" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="audioturbo-fast-text-to-audio-generation-with-rectified-diff-2505-22106/">AudioTurbo: Fast Text-to-Audio Generation with Rectified Diffusion</a>
<div class="card-meta">
<span class="card-score">7.0</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">将整流扩散引入预训练TTA扩散模型，学习一阶近似ODE路径，实现快速文本到音频生成。</div>
<div class="card-action">
<a href="audioturbo-fast-text-to-audio-generation-with-rectified-diff-2505-22106/">详情 →</a> · <a href="https://arxiv.org/abs/2505.22106" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="televal-a-benchmark-designed-for-spoken-language-models-in-c-2507-18061/">TELEVAL: A Benchmark Designed for Spoken Language Models in Chinese Interactive Scenarios</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音交互评测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出TELEVAL，一个面向中文口语交互的SLM评测基准，从内容可靠性与交互适当性两方面诊断模型缺陷。</div>
<div class="card-action">
<a href="televal-a-benchmark-designed-for-spoken-language-models-in-c-2507-18061/">详情 →</a> · <a href="https://arxiv.org/abs/2507.18061" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="the-landscape-of-ai-speech-generation-and-deepfake-detection-2611-24993/">The landscape of AI speech generation and deepfake detection</a>
<div class="card-meta">
<span class="card-score">4.5</span>
<span class="tag-pill">#语音生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">一篇面向大众的综述，梳理合成语音生成与语音深伪检测的历史、术语与文献。</div>
<div class="card-action">
<a href="the-landscape-of-ai-speech-generation-and-deepfake-detection-2611-24993/">详情 →</a> · <a href="https://arxiv.org/abs/2611.24993" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="modeling-and-link-budget-feasibility-analysis-of-secure-lora-2602-23924/">Modeling and Link Budget Feasibility Analysis of Secure LoRa-Based Peer-to-Peer Communication for Short-Range Tactical Networks</a>
<div class="card-meta">
<span class="card-score">3.5</span>
<span class="tag-pill">#声学模拟</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">提出基于LoRa的微型加密语音对讲设备方案，用链路预算论证1-1.5km视距通信可行性。</div>
<div class="card-action">
<a href="modeling-and-link-budget-feasibility-analysis-of-secure-lora-2602-23924/">详情 →</a> · <a href="https://arxiv.org/abs/2602.23924" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
