---
title: "语音/音频论文速递 2026-07-27"
date: 2026-07-27T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 1 篇 · 最高分 9.5（#语音理解）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">10</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">1</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">9.5</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音理解 | 1篇 | `██████████` |
| #声学侧信道攻击 | 1篇 | `██████████` |
| #多模态音乐对齐 | 1篇 | `██████████` |
| #副语言特征分析 | 1篇 | `██████████` |
| #音乐表示学习 | 1篇 | `██████████` |
| #乐谱跟踪 | 1篇 | `██████████` |
| #音频生成 | 1篇 | `██████████` |
| #音频检索 | 1篇 | `██████████` |

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

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="listen-do-not-copy-internalizing-audio-grounded-scaffold-con-2607-21943/">Listen, Do Not Copy: Internalizing Audio-Grounded Scaffold Context for Robust Omni-Model Speech Understanding</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音理解</span>
</div>
<div class="card-tldr">提出音频接地脚手架上下文（AGSC），通过从音频构建线索而非直接提供文本答案，防止全模态模型在重叠噪声语音中作弊，显著降低词错误率。</div>
</div></div>

### #语音分离

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="listen-do-not-copy-internalizing-audio-grounded-scaffold-con-2607-21943/">Listen, Do Not Copy: Internalizing Audio-Grounded Scaffold Context for Robust Omni-Model Speech Understanding</a>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音理解</span>
</div>
<div class="card-tldr">提出音频接地脚手架上下文（AGSC），通过从音频构建线索而非直接提供文本答案，防止全模态模型在重叠噪声语音中作弊，显著降低词错误率。</div>
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
| 🥇 | [Listen, Do Not Copy: Internalizing Audio-Grounded Scaffold C…](listen-do-not-copy-internalizing-audio-grounded-scaffold-con-2607-21943/) 🎯 | **9.5** | #语音理解 |
| 🥈 | [Transforming Keystroke Noise to Text: Self-Supervised Acoust…](transforming-keystroke-noise-to-text-self-supervised-acousti-2607-22094/) | **8.5** | #声学侧信道攻击 |
| 🥉 | [Local Multimodal Music Alignment from Global Supervision](local-multimodal-music-alignment-from-global-supervision-2607-10023/) | **7.8** | #多模态音乐对齐 |
| 4. | [Synthetic Speech, Real Signal: Paralinguistic Preservation a…](synthetic-speech-real-signal-paralinguistic-preservation-and-2607-22304/) | **7.8** | #副语言特征分析 |
| 5. | [Music-JEPA: Learning a World Model of Sound from Action](music-jepa-learning-a-world-model-of-sound-from-action-2607-22000/) | **7.8** | #音乐表示学习 |
| 6. | [CODA: Cascaded Online Discontinuity-Aware Alignment for Real…](coda-cascaded-online-discontinuity-aware-alignment-for-real--2607-21899/) | **7.8** | #乐谱跟踪 |
| 7. | [SoundscapeAgent: Agentic Soundscape Construction for Control…](soundscapeagent-agentic-soundscape-construction-for-controll-2607-21857/) | **7.8** | #音频生成 |
| 8. | [Reflector: Arrangement-Aware Harmonic Retrieval for Sample-B…](reflector-arrangement-aware-harmonic-retrieval-for-sample-ba-2607-22413/) | **7.2** | #音频检索 |
| 9. | [MemNMF: Memory-Augmented NMF on LPC Spectra for Anomalous So…](memnmf-memory-augmented-nmf-on-lpc-spectra-for-anomalous-sou-2607-22086/) | **6.8** | #异常声音检测 |
| 10. | [Kutti AI: A Voice-First, Offline-Capable Learning Companion …](kutti-ai-a-voice-first-offline-capable-learning-companion-wi-2607-22377/) | **5.5** | #教育语音交互 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="listen-do-not-copy-internalizing-audio-grounded-scaffold-con-2607-21943/">Listen, Do Not Copy: Internalizing Audio-Grounded Scaffold Context for Robust Omni-Model Speech Understanding</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.5</span>
<span class="tag-pill">#语音理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出音频接地脚手架上下文（AGSC），通过从音频构建线索而非直接提供文本答案，防止全模态模型在重叠噪声语音中作弊，显著降低词错误率。</div>
<div class="card-action">
<a href="listen-do-not-copy-internalizing-audio-grounded-scaffold-con-2607-21943/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21943" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="transforming-keystroke-noise-to-text-self-supervised-acousti-2607-22094/">Transforming Keystroke Noise to Text: Self-Supervised Acoustic Eavesdropping Attacks on Keyboards</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#声学侧信道攻击</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出自监督声学侧信道攻击方法，仅凭键盘敲击声重建文本，无需目标设备标注数据，在多种真实场景下达到高重建准确率。</div>
<div class="card-action">
<a href="transforming-keystroke-noise-to-text-self-supervised-acousti-2607-22094/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22094" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="local-multimodal-music-alignment-from-global-supervision-2607-10023/">Local Multimodal Music Alignment from Global Supervision</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#多模态音乐对齐</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出FuSiLi相似度，通过Sinkhorn软对齐实现仅需全局监督即可学习局部多模态音乐对应关系。</div>
<div class="card-action">
<a href="local-multimodal-music-alignment-from-global-supervision-2607-10023/">详情 →</a> · <a href="https://arxiv.org/abs/2607.10023" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="synthetic-speech-real-signal-paralinguistic-preservation-and-2607-22304/">Synthetic Speech, Real Signal: Paralinguistic Preservation and Cross-Lingual Augmentation via Voice Cloning</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#副语言特征分析</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">系统评估语音克隆对副语言信号保留能力，并验证其用于跨语言临床数据增强的有效性。</div>
<div class="card-action">
<a href="synthetic-speech-real-signal-paralinguistic-preservation-and-2607-22304/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22304" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="music-jepa-learning-a-world-model-of-sound-from-action-2607-22000/">Music-JEPA: Learning a World Model of Sound from Action</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音乐表示学习</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Music-JEPA，将钢琴音频视为状态、钢琴卷帘视为动作，通过预测未来音频状态学习音乐世界模型，支持多项下游任务。</div>
<div class="card-action">
<a href="music-jepa-learning-a-world-model-of-sound-from-action-2607-22000/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22000" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="coda-cascaded-online-discontinuity-aware-alignment-for-real--2607-21899/">CODA: Cascaded Online Discontinuity-Aware Alignment for Real-Time Image-Based Score Following</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#乐谱跟踪</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出CODA，首个利用级联结构（系统→小节→音符）实现实时乐谱跟踪的系统，并支持重复、跳转等不连续性恢复。</div>
<div class="card-action">
<a href="coda-cascaded-online-discontinuity-aware-alignment-for-real--2607-21899/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21899" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="soundscapeagent-agentic-soundscape-construction-for-controll-2607-21857/">SoundscapeAgent: Agentic Soundscape Construction for Controllable Synthesis and Scalable Audio-Language Supervision</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出基于LLM代理的声景构建框架，将文本到音频生成分解为场景规划、源选择、时间布局和渲染步骤，实现可控合成和可扩展的音频-语言数据构建。</div>
<div class="card-action">
<a href="soundscapeagent-agentic-soundscape-construction-for-controll-2607-21857/">详情 →</a> · <a href="https://arxiv.org/abs/2607.21857" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="reflector-arrangement-aware-harmonic-retrieval-for-sample-ba-2607-22413/">Reflector: Arrangement-Aware Harmonic Retrieval for Sample-Based Composition</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#音频检索</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出Reflector系统，通过固定音级类oracle和学习的嵌入空间，实现随编曲进程动态调整的样本检索。</div>
<div class="card-action">
<a href="reflector-arrangement-aware-harmonic-retrieval-for-sample-ba-2607-22413/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22413" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="memnmf-memory-augmented-nmf-on-lpc-spectra-for-anomalous-sou-2607-22086/">MemNMF: Memory-Augmented NMF on LPC Spectra for Anomalous Sound Detection</a>
<div class="card-meta">
<span class="card-score">6.8</span>
<span class="tag-pill">#异常声音检测</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出MemNMF，在LPC谱上结合NMF记忆模块进行约束重构，提升异常声音检测的鲁棒性。</div>
<div class="card-action">
<a href="memnmf-memory-augmented-nmf-on-lpc-spectra-for-anomalous-sou-2607-22086/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22086" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="kutti-ai-a-voice-first-offline-capable-learning-companion-wi-2607-22377/">Kutti AI: A Voice-First, Offline-Capable Learning Companion with Real-Time Struggle Detection for Visually-Impaired Children</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#教育语音交互</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">Kutti AI是一个面向视障儿童的语音优先学习伴侣，通过实时困难检测和离线语音处理实现自适应教育。</div>
<div class="card-action">
<a href="kutti-ai-a-voice-first-offline-capable-learning-companion-wi-2607-22377/">详情 →</a> · <a href="https://arxiv.org/abs/2607.22377" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
