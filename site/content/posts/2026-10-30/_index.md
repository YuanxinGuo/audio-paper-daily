---
title: "语音/音频论文速递 2026-10-30"
date: 2026-10-30T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 3 篇 · 最高分 8.8（#双耳音频）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #双耳音频 | 3篇 | `██████████` |
| #语音识别 | 2篇 | `███████` |
| #音频处理 | 2篇 | `███████` |
| #房间冲激响应生成 | 1篇 | `███` |
| #音视频问答 | 1篇 | `███` |
| #语音合成 | 1篇 | `███` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="array-agnostic-high-order-ambisonics-encoding-via-diffusion--2610-39185/">Array-Agnostic High-Order Ambisonics Encoding via Diffusion Posterior Sampling</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用阵列无关的Ambisonics扩散先验加显式物理采集模型，通过score blending实现零样本编码与升阶。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="sonoworld4d-from-one-video-to-a-4d-audio-visual-scene-via-di-2610-40640/">SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">从单目视频生成可探索的4D音视频场景，重建动态物体轨迹并用双空间音频扩散同步合成空间声场。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="ambisonics-introducing-an-accessible-distributed-approach-2610-39898/">Ambisonics: Introducing an Accessible, Distributed Approach</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
</div>
<div class="card-tldr">用低成本微控制器网络分布式实现高阶Ambisonics解码，靠IEEE 1588 PTP同步达到亚微秒对齐，三阶原型验证可行。</div>
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
| 🥇 | [Array-Agnostic High-Order Ambisonics Encoding via Diffusion …](array-agnostic-high-order-ambisonics-encoding-via-diffusion--2610-39185/) 🎯 | **8.8** | #双耳音频 |
| 🥈 | [SonoWorld4D: From One Video to a 4D Audio-Visual Scene via D…](sonoworld4d-from-one-video-to-a-4d-audio-visual-scene-via-di-2610-40640/) 🎯 | **8.2** | #双耳音频 |
| 🥉 | [Ambisonics: Introducing an Accessible, Distributed Approach](ambisonics-introducing-an-accessible-distributed-approach-2610-39898/) 🎯 | **7.8** | #双耳音频 |
| 4. | [Streaming Speech Recognition on a Microcontroller: a 65.7M-P…](streaming-speech-recognition-on-a-microcontroller-a-65-7m-pa-2610-38739/) | **7.2** | #语音识别 |
| 5. | [Structured Pruning of Feedback Delay Networks](structured-pruning-of-feedback-delay-networks-2610-38768/) | **6.8** | #房间冲激响应生成 |
| 6. | [Efficient Agentic Audio-Visual Question Answering through To…](efficient-agentic-audio-visual-question-answering-through-to-2610-38960/) | **6.8** | #音视频问答 |
| 7. | [How Architecture, Typology, and Adaptation Strategies Shape …](how-architecture-typology-and-adaptation-strategies-shape-as-2610-39004/) | **6.8** | #语音识别 |
| 8. | [Reading-Level Verification of Kanji Words in Japanese Financ…](reading-level-verification-of-kanji-words-in-japanese-financ-2610-39168/) | **6.8** | #语音合成 |
| 9. | [Personalising Parametric Audio Effect Recommendation for Voc…](personalising-parametric-audio-effect-recommendation-for-voc-2610-38696/) | **6.0** | #音频处理 |
| 10. | [Automated Parameter Sensitivity Ranking in Audio Synthesis](automated-parameter-sensitivity-ranking-in-audio-synthesis-2610-38740/) | **6.0** | #音频处理 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="array-agnostic-high-order-ambisonics-encoding-via-diffusion--2610-39185/">Array-Agnostic High-Order Ambisonics Encoding via Diffusion Posterior Sampling</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">用阵列无关的Ambisonics扩散先验加显式物理采集模型，通过score blending实现零样本编码与升阶。</div>
<div class="card-action">
<a href="array-agnostic-high-order-ambisonics-encoding-via-diffusion--2610-39185/">详情 →</a> · <a href="https://arxiv.org/abs/2610.39185" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="sonoworld4d-from-one-video-to-a-4d-audio-visual-scene-via-di-2610-40640/">SonoWorld4D: From One Video to a 4D Audio-Visual Scene via Diffusion Synchronization</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">从单目视频生成可探索的4D音视频场景，重建动态物体轨迹并用双空间音频扩散同步合成空间声场。</div>
<div class="card-action">
<a href="sonoworld4d-from-one-video-to-a-4d-audio-visual-scene-via-di-2610-40640/">详情 →</a> · <a href="https://arxiv.org/abs/2610.40640" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="ambisonics-introducing-an-accessible-distributed-approach-2610-39898/">Ambisonics: Introducing an Accessible, Distributed Approach</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#双耳音频</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">用低成本微控制器网络分布式实现高阶Ambisonics解码，靠IEEE 1588 PTP同步达到亚微秒对齐，三阶原型验证可行。</div>
<div class="card-action">
<a href="ambisonics-introducing-an-accessible-distributed-approach-2610-39898/">详情 →</a> · <a href="https://arxiv.org/abs/2610.39898" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="streaming-speech-recognition-on-a-microcontroller-a-65-7m-pa-2610-38739/">Streaming Speech Recognition on a Microcontroller: a 65.7M-Parameter Transducer in 2 and 4 Bits on the ESP32-P4</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">在无神经网络加速器的ESP32-P4上以2/4比特量化运行65.7M参数Zipformer2流式语音识别，LibriSpeech test-clean WER 4.34%。</div>
<div class="card-action">
<a href="streaming-speech-recognition-on-a-microcontroller-a-65-7m-pa-2610-38739/">详情 →</a> · <a href="https://arxiv.org/abs/2610.38739" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="structured-pruning-of-feedback-delay-networks-2610-38768/">Structured Pruning of Feedback Delay Networks</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#房间冲激响应生成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">对 FDN 反馈矩阵做结构化剪枝，用固定置换加小正交块替代稠密正交矩阵，在保持混响音质的同时大幅降低乘加与存储开销。</div>
<div class="card-action">
<a href="structured-pruning-of-feedback-delay-networks-2610-38768/">详情 →</a> · <a href="https://arxiv.org/abs/2610.38768" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="efficient-agentic-audio-visual-question-answering-through-to-2610-38960/">Efficient Agentic Audio-Visual Question Answering through Toolset Pruning and Modality Consolidation</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#音视频问答</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">通过分阶段剪枝专用工具并将模态专用工具整合为全模态工具，构建仅含两个工具的精简 AVQA 智能体，精度持平或更优且推理成本降约 70%。</div>
<div class="card-action">
<a href="efficient-agentic-audio-visual-question-answering-through-to-2610-38960/">详情 →</a> · <a href="https://arxiv.org/abs/2610.38960" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="how-architecture-typology-and-adaptation-strategies-shape-as-2610-39004/">How Architecture, Typology, and Adaptation Strategies Shape ASR for Low-Resource African Languages: A Controlled Empirical Study</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">系统对比 Phi-4、Whisper、MMS 三种架构在五种低资源非洲语言上的微调与适应策略，给出数据效率与类型学影响的经验结论。</div>
<div class="card-action">
<a href="how-architecture-typology-and-adaptation-strategies-shape-as-2610-39004/">详情 →</a> · <a href="https://arxiv.org/abs/2610.39004" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="reading-level-verification-of-kanji-words-in-japanese-financ-2610-39168/">Reading-Level Verification of Kanji Words in Japanese Financial Speech Synthesis</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#语音合成</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">用CTC假名识别器对日语金融TTS中多音汉字做读音级校验，替代不可靠的ASR转写门控。</div>
<div class="card-action">
<a href="reading-level-verification-of-kanji-words-in-japanese-financ-2610-39168/">详情 →</a> · <a href="https://arxiv.org/abs/2610.39168" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="personalising-parametric-audio-effect-recommendation-for-voc-2610-38696/">Personalising Parametric Audio Effect Recommendation for Vocals from Parameter-only Style Priors</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">将混音师风格建模为效果链参数分布，用标签偏移下的闭式解实现无需配对音频的个性化人声效果推荐。</div>
<div class="card-action">
<a href="personalising-parametric-audio-effect-recommendation-for-voc-2610-38696/">详情 →</a> · <a href="https://arxiv.org/abs/2610.38696" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="automated-parameter-sensitivity-ranking-in-audio-synthesis-2610-38740/">Automated Parameter Sensitivity Ranking in Audio Synthesis</a>
<div class="card-meta">
<span class="card-score">6.0</span>
<span class="tag-pill">#音频处理</span>
<span class="card-tier">中等</span>
</div>
<div class="card-tldr">提出两阶段框架，用扫频测试与Sobol方差实验对合成器参数做敏感性排序并交叉验证。</div>
<div class="card-action">
<a href="automated-parameter-sensitivity-ranking-in-audio-synthesis-2610-38740/">详情 →</a> · <a href="https://arxiv.org/abs/2610.38740" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
