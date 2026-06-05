---
title: "语音/音频论文速递 2026-06-05"
date: 2026-06-05T09:00:00+08:00
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
| #语音增强 | 3篇 | `██████████` |
| #语音识别 | 2篇 | `███████` |
| #对抗攻击 | 1篇 | `███` |
| #全双工语音对话 | 1篇 | `███` |
| #音频表征学习 | 1篇 | `███` |
| #对话管理 | 1篇 | `███` |
| #音频表示评估 | 1篇 | `███` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sb-rf-schr-odinger-bridge-rectified-flow-for-one-step-robust-2606-05575/">SB-RF: Schr\"odinger Bridge Rectified Flow for One-Step Robust Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出SB-RF，结合薛定谔桥与整流流实现一步生成式语音增强，在VoiceBank-DEMAND上达到领先性能，并在低信噪比场景下展现强鲁棒性。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="absorbing-discrete-diffusion-for-speech-enhancement-2602-22417/">Absorbing Discrete Diffusion for Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出ADDSE，利用吸收离散扩散模型对语音编解码码字进行条件生成，实现语音增强。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="dbhn-net-dual-branch-hybrid-neural-network-for-low-complexit-2606-05911/">DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexity Monaural Speech Enhancement</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出双分支混合神经网络DBHN-Net，结合ANN与SNN，在保持语音增强性能的同时大幅降低计算复杂度。</div>
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
| 🥇 | [SB-RF: Schr\"odinger Bridge Rectified Flow for One-Step Robu…](sb-rf-schr-odinger-bridge-rectified-flow-for-one-step-robust-2606-05575/) 🎯 | **9.2** | #语音增强 |
| 🥈 | [Absorbing Discrete Diffusion for Speech Enhancement](absorbing-discrete-diffusion-for-speech-enhancement-2602-22417/) 🎯 | **8.8** | #语音增强 |
| 🥉 | [DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexi…](dbhn-net-dual-branch-hybrid-neural-network-for-low-complexit-2606-05911/) 🎯 | **8.8** | #语音增强 |
| 4. | [Beyond Waveform Robustness: Robust Feature-Vocoder Adversari…](beyond-waveform-robustness-robust-feature-vocoder-adversaria-2606-05678/) | **8.5** | #对抗攻击 |
| 5. | [The Silent Thought: Modeling Internal Cognition in Full-Dupl…](the-silent-thought-modeling-internal-cognition-in-full-duple-2603-17837/) | **7.8** | #全双工语音对话 |
| 6. | [F3-Tokenizer: Taming Audio Autoencoder Latents for Understan…](f3-tokenizer-taming-audio-autoencoder-latents-for-understand-2606-06357/) | **7.8** | #音频表征学习 |
| 7. | [RAS: a Reliability Oriented Metric for Automatic Speech Reco…](ras-a-reliability-oriented-metric-for-automatic-speech-recog-2604-24278/) | **7.5** | #语音识别 |
| 8. | [LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dial…](llm-enhanced-dialogue-management-for-full-duplex-spoken-dial-2502-14145/) | **7.2** | #对话管理 |
| 9. | [FiLM-Based Speaker Conditioning of a SpeechLLM for Pathologi…](film-based-speaker-conditioning-of-a-speechllm-for-pathologi-2606-06211/) | **7.2** | #语音识别 |
| 10. | [Probing Spatial Structure in Pretrained Audio Representation…](probing-spatial-structure-in-pretrained-audio-representation-2606-05544/) | **7.2** | #音频表示评估 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="sb-rf-schr-odinger-bridge-rectified-flow-for-one-step-robust-2606-05575/">SB-RF: Schr\"odinger Bridge Rectified Flow for One-Step Robust Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SB-RF，结合薛定谔桥与整流流实现一步生成式语音增强，在VoiceBank-DEMAND上达到领先性能，并在低信噪比场景下展现强鲁棒性。</div>
<div class="card-action">
<a href="sb-rf-schr-odinger-bridge-rectified-flow-for-one-step-robust-2606-05575/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05575" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="absorbing-discrete-diffusion-for-speech-enhancement-2602-22417/">Absorbing Discrete Diffusion for Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出ADDSE，利用吸收离散扩散模型对语音编解码码字进行条件生成，实现语音增强。</div>
<div class="card-action">
<a href="absorbing-discrete-diffusion-for-speech-enhancement-2602-22417/">详情 →</a> · <a href="https://arxiv.org/abs/2602.22417" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="dbhn-net-dual-branch-hybrid-neural-network-for-low-complexit-2606-05911/">DBHN-Net: Dual-Branch Hybrid Neural Network For Low-Complexity Monaural Speech Enhancement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双分支混合神经网络DBHN-Net，结合ANN与SNN，在保持语音增强性能的同时大幅降低计算复杂度。</div>
<div class="card-action">
<a href="dbhn-net-dual-branch-hybrid-neural-network-for-low-complexit-2606-05911/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05911" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="beyond-waveform-robustness-robust-feature-vocoder-adversaria-2606-05678/">Beyond Waveform Robustness: Robust Feature-Vocoder Adversarial Attacks on Automatic Speech Recognition</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#对抗攻击</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于SSL特征空间的对抗攻击方法，通过声码器重构波形，提升黑盒迁移性和防御绕过能力。</div>
<div class="card-action">
<a href="beyond-waveform-robustness-robust-feature-vocoder-adversaria-2606-05678/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05678" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="the-silent-thought-modeling-internal-cognition-in-full-duple-2603-17837/">The Silent Thought: Modeling Internal Cognition in Full-Duplex Spoken Dialogue Models via Latent Reasoning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#全双工语音对话</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FLAIR方法，在用户说话时通过潜在推理模拟内部认知，实现全双工语音对话中的实时思考。</div>
<div class="card-action">
<a href="the-silent-thought-modeling-internal-cognition-in-full-duple-2603-17837/">详情 →</a> · <a href="https://arxiv.org/abs/2603.17837" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="f3-tokenizer-taming-audio-autoencoder-latents-for-understand-2606-06357/">F3-Tokenizer: Taming Audio Autoencoder Latents for Understanding and Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频表征学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出F3-Tokenizer，通过噪声正则化瓶颈和潜在表示编码器，统一音频理解与生成的连续潜在表示。</div>
<div class="card-action">
<a href="f3-tokenizer-taming-audio-autoencoder-latents-for-understand-2606-06357/">详情 →</a> · <a href="https://arxiv.org/abs/2606.06357" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="ras-a-reliability-oriented-metric-for-automatic-speech-recog-2604-24278/">RAS: a Reliability Oriented Metric for Automatic Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出面向ASR的可靠性指标RAS，并训练可弃权转录模型以平衡信息量与错误规避。</div>
<div class="card-action">
<a href="ras-a-reliability-oriented-metric-for-automatic-speech-recog-2604-24278/">详情 →</a> · <a href="https://arxiv.org/abs/2604.24278" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="llm-enhanced-dialogue-management-for-full-duplex-spoken-dial-2502-14145/">LLM-Enhanced Dialogue Management for Full-Duplex Spoken Dialogue Systems</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#对话管理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一个轻量级LLM作为语义VAD模块，用于全双工语音对话系统中的话轮管理，实现实时决策并降低计算开销。</div>
<div class="card-action">
<a href="llm-enhanced-dialogue-management-for-full-duplex-spoken-dial-2502-14145/">详情 →</a> · <a href="https://arxiv.org/abs/2502.14145" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="film-based-speaker-conditioning-of-a-speechllm-for-pathologi-2606-06211/">FiLM-Based Speaker Conditioning of a SpeechLLM for Pathological Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过FiLM注入x-vector信息到冻结ASR编码器各层，实现病理语音的说话人自适应，无需修改基座模型权重。</div>
<div class="card-action">
<a href="film-based-speaker-conditioning-of-a-speechllm-for-pathologi-2606-06211/">详情 →</a> · <a href="https://arxiv.org/abs/2606.06211" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="probing-spatial-structure-in-pretrained-audio-representation-2606-05544/">Probing Spatial Structure in Pretrained Audio Representations</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频表示评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出SARL基准，系统评估预训练音频模型的空间编码能力，发现源因素比房间因素更易解码。</div>
<div class="card-action">
<a href="probing-spatial-structure-in-pretrained-audio-representation-2606-05544/">详情 →</a> · <a href="https://arxiv.org/abs/2606.05544" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
