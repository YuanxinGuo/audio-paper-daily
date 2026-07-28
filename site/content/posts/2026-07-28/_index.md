---
title: "语音/音频论文速递 2026-07-28"
date: 2026-07-28T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 8.8（#乐器分离）"
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
| #语音识别 | 2篇 | `██████████` |
| #乐器分离 | 1篇 | `█████` |
| #音视频伪造定位 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频编解码 | 1篇 | `█████` |
| #抑郁症检测 | 1篇 | `█████` |
| #音乐界面设计 | 1篇 | `█████` |
| #对话系统 | 1篇 | `█████` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="music-source-separation-training-msst-a-unified-framework-fo-2607-23395/">Music-Source-Separation-Training (MSST): A Unified Framework for Training and Evaluating Music Demixing Models</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">提出统一开源框架MSST，支持多种音乐分离模型训练、评估与推理，集成滑动窗口、测试时增强、模型集成和LoRA微调等实用技术。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [Music-Source-Separation-Training (MSST): A Unified Framework…](music-source-separation-training-msst-a-unified-framework-fo-2607-23395/) 🎯 | **8.8** | #乐器分离 |
| 🥈 | [UniSkip-Mamba: A Frequency-Aware State Space Model for Audio…](uniskip-mamba-a-frequency-aware-state-space-model-for-audio--2607-04498/) | **8.5** | #音视频伪造定位 |
| 🥉 | [Qwen-Music Technical Report](qwen-music-technical-report-2607-11699/) | **8.5** | #音乐生成 |
| 4. | [The Equalizer: Introducing Shape-Gain Decomposition in Neura…](the-equalizer-introducing-shape-gain-decomposition-in-neural-2602-15491/) | **8.2** | #音频编解码 |
| 5. | [MoLGE: Mixture of Language Group Experts for Efficient Scali…](molge-mixture-of-language-group-experts-for-efficient-scalin-2607-24030/) | **8.2** | #语音识别 |
| 6. | [Multimodal Domain Generalization for Depression Detection: A…](multimodal-domain-generalization-for-depression-detection-an-2607-22794/) | **7.8** | #抑郁症检测 |
| 7. | [Voice-Driven Semantic Perception for UAV-Assisted Emergency …](voice-driven-semantic-perception-for-uav-assisted-emergency--2602-17394/) | **6.5** | #语音识别 |
| 8. | [Explainable AI through the Lens of Material Agency: Enabling…](explainable-ai-through-the-lens-of-material-agency-enabling--2607-23309/) | **6.5** | #音乐界面设计 |
| 9. | [Low-Latency Turn-Taking via Context-Aware Preface Generation…](low-latency-turn-taking-via-context-aware-preface-generation-2607-23204/) | **6.5** | #对话系统 |
| 10. | [EmotionAI: A Privacy-Preserving Computational Intelligence P…](emotionai-a-privacy-preserving-computational-intelligence-pi-2606-24941/) | **6.0** | #语音情感识别 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="music-source-separation-training-msst-a-unified-framework-fo-2607-23395/">Music-Source-Separation-Training (MSST): A Unified Framework for Training and Evaluating Music Demixing Models</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出统一开源框架MSST，支持多种音乐分离模型训练、评估与推理，集成滑动窗口、测试时增强、模型集成和LoRA微调等实用技术。</div>
<div class="card-action">
<a href="music-source-separation-training-msst-a-unified-framework-fo-2607-23395/">详情 →</a> · <a href="https://arxiv.org/abs/2607.23395" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="uniskip-mamba-a-frequency-aware-state-space-model-for-audio--2607-04498/">UniSkip-Mamba: A Frequency-Aware State Space Model for Audio-Visual Temporal Forgery Localization</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音视频伪造定位</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出UniSkip-Mamba，利用频率感知的状态空间模型实现音视频时序伪造定位，在低频/中频区域聚焦判别性模式，SOTA性能且推理加速6倍。</div>
<div class="card-action">
<a href="uniskip-mamba-a-frequency-aware-state-space-model-for-audio--2607-04498/">详情 →</a> · <a href="https://arxiv.org/abs/2607.04498" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="qwen-music-technical-report-2607-11699/">Qwen-Music Technical Report</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前10%</span>
</div>
<div class="card-tldr">提出Qwen-Music音乐生成模型，结合语义token自回归建模与立体声渲染，在16项客观指标中13项达到SOTA。</div>
<div class="card-action">
<a href="qwen-music-technical-report-2607-11699/">详情 →</a> · <a href="https://arxiv.org/abs/2607.11699" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="the-equalizer-introducing-shape-gain-decomposition-in-neural-2602-15491/">The Equalizer: Introducing Shape-Gain Decomposition in Neural Audio Codecs</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频编解码</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">将经典语音编码中的形状-增益分解引入神经音频编解码器，提升码率失真性能并降低量化复杂度。</div>
<div class="card-action">
<a href="the-equalizer-introducing-shape-gain-decomposition-in-neural-2602-15491/">详情 →</a> · <a href="https://arxiv.org/abs/2602.15491" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="molge-mixture-of-language-group-experts-for-efficient-scalin-2607-24030/">MoLGE: Mixture of Language Group Experts for Efficient Scaling of Massively Multilingual Speech Recognition</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MoLGE方法，通过语言分组专家和分层LoRA，高效扩展多语言ASR至495种语言，缓解多语言诅咒。</div>
<div class="card-action">
<a href="molge-mixture-of-language-group-experts-for-efficient-scalin-2607-24030/">详情 →</a> · <a href="https://arxiv.org/abs/2607.24030" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="multimodal-domain-generalization-for-depression-detection-an-2607-22794/">Multimodal Domain Generalization for Depression Detection: An Attention-Based BiLSTM Network with Domain-Adversarial Training</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#抑郁症检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个患者独立的多模态抑郁症检测框架，结合BiLSTM与注意力机制，通过域对抗训练提升跨说话人泛化能力，在Androids-Corpus上达到93.2%准确率。</div>
<div class="card-action">
<a href="multimodal-domain-generalization-for-depression-detection-an-2607-22794/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22794" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="voice-driven-semantic-perception-for-uav-assisted-emergency--2602-17394/">Voice-Driven Semantic Perception for UAV-Assisted Emergency Networks</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出SIREN框架，利用ASR和LLM将应急语音通信转化为结构化信息，用于无人机辅助网络管理。</div>
<div class="card-action">
<a href="voice-driven-semantic-perception-for-uav-assisted-emergency--2602-17394/">详情 →</a> · <a href="https://arxiv.org/abs/2602.17394" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="explainable-ai-through-the-lens-of-material-agency-enabling--2607-23309/">Explainable AI through the Lens of Material Agency: Enabling Musical Interface Design with Neural Audio Models</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐界面设计</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出材料可解释性概念，通过案例研究展示如何将神经音频模型转化为音乐界面设计的可访问材料。</div>
<div class="card-action">
<a href="explainable-ai-through-the-lens-of-material-agency-enabling--2607-23309/">详情 →</a> · <a href="https://arxiv.org/abs/2607.23309" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="low-latency-turn-taking-via-context-aware-preface-generation-2607-23204/">Low-Latency Turn-Taking via Context-Aware Preface Generation in a Real-World Dialogue Robot</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#对话系统</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出两阶段增量框架，通过上下文感知的前言生成降低对话机器人响应延迟，并在真实购物中心导览机器人上验证。</div>
<div class="card-action">
<a href="low-latency-turn-taking-via-context-aware-preface-generation-2607-23204/">详情 →</a> · <a href="https://arxiv.org/abs/2607.23204" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="emotionai-a-privacy-preserving-computational-intelligence-pi-2606-24941/">EmotionAI: A Privacy-Preserving Computational Intelligence Pipeline for Speech-Emotion-Grounded Conversational Analysis</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#语音情感识别</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一个完全本地的计算智能流水线，结合语音情感识别与生成式推理，实现隐私保护的对话情感分析。</div>
<div class="card-action">
<a href="emotionai-a-privacy-preserving-computational-intelligence-pi-2606-24941/">详情 →</a> · <a href="https://arxiv.org/abs/2606.24941" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
