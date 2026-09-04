---
title: "语音/音频论文速递 2026-09-04"
date: 2026-09-04T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 9 篇 · 重点领域 3 篇 · 最高分 8.8（#语音增强）"
ShowToc: false
---

<div class="daily-stats">
<div class="stat-card"><div class="stat-num">9</div><div class="stat-label">分析论文</div></div>
<div class="stat-card stat-focus"><div class="stat-num">3</div><div class="stat-label">重点领域</div></div>
<div class="stat-card stat-top"><div class="stat-num">8.8</div><div class="stat-label">最高分</div></div>
</div>

## ⚡ 今日方向分布

| 方向 | 数量 | 分布 |
| --- | --- | --- |
| #语音增强 | 2篇 | `██████████` |
| #语音识别 | 2篇 | `██████████` |
| #音频深度伪造检测 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #音乐生成 | 1篇 | `█████` |
| #音频生成 | 1篇 | `█████` |
| #音乐分析 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="test-time-adaptation-for-speech-enhancement-with-an-autoregr-2609-03622/">Test-time adaptation for speech enhancement with an autoregressive speech prior</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出一种基于自回归语音先验的单句测试时自适应方法，通过最小化KL散度正则化预训练语音增强模型，在噪声失配条件下提升语音质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="masked-autoregressive-speech-enhancement-with-continuous-neu-2609-03940/">Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations</a>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出MARSE，利用连续神经音频编解码器表示进行掩码自回归语音增强，通过不同解码策略实现性能与计算开销的灵活权衡。</div>
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
<a class="card-title" href="geometric-ceilings-on-time-frequency-masking-for-single-chan-2609-03481/">Geometric Ceilings on Time-Frequency Masking for Single-Channel Separation</a>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">本文从几何角度分析单通道分离中时频掩蔽的极限，提出嵌套类与正交投影框架，并在MUSDB18上验证了理论界限。</div>
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
| 🥇 | [Test-time adaptation for speech enhancement with an autoregr…](test-time-adaptation-for-speech-enhancement-with-an-autoregr-2609-03622/) 🎯 | **8.8** | #语音增强 |
| 🥈 | [Masked Autoregressive Speech Enhancement with Continuous Neu…](masked-autoregressive-speech-enhancement-with-continuous-neu-2609-03940/) 🎯 | **8.5** | #语音增强 |
| 🥉 | [ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Aud…](tooldf-tool-integrated-reasoning-for-mixed-authenticity-audi-2609-03620/) | **8.2** | #音频深度伪造检测 |
| 4. | [Dual-Form ASR: Semantics-Aware Inverse Text Normalization fo…](dual-form-asr-semantics-aware-inverse-text-normalization-for-2609-02901/) | **7.8** | #语音识别 |
| 5. | [Compressing Streaming Neural Audio Encoders via Latent-Space…](compressing-streaming-neural-audio-encoders-via-latent-space-2609-04102/) | **7.8** | #语音识别 |
| 6. | [Geometric Ceilings on Time-Frequency Masking for Single-Chan…](geometric-ceilings-on-time-frequency-masking-for-single-chan-2609-03481/) 🎯 | **7.5** | #语音分离 |
| 7. | [One Timeline, Many Renderings: A Wolfram Language Paclet for…](one-timeline-many-renderings-a-wolfram-language-paclet-for-h-2608-24683/) | **6.5** | #音乐生成 |
| 8. | [Local Chord Corruption Is Not Recognizer Replay: Chord-Condi…](local-chord-corruption-is-not-recognizer-replay-chord-condit-2609-03584/) | **6.2** | #音频生成 |
| 9. | [From local kernels to global form: modeling the emergence of…](from-local-kernels-to-global-form-modeling-the-emergence-of--2608-24660/) | **5.5** | #音乐分析 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="test-time-adaptation-for-speech-enhancement-with-an-autoregr-2609-03622/">Test-time adaptation for speech enhancement with an autoregressive speech prior</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出一种基于自回归语音先验的单句测试时自适应方法，通过最小化KL散度正则化预训练语音增强模型，在噪声失配条件下提升语音质量。</div>
<div class="card-action">
<a href="test-time-adaptation-for-speech-enhancement-with-an-autoregr-2609-03622/">详情 →</a> · <a href="https://arxiv.org/abs/2609.03622" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="masked-autoregressive-speech-enhancement-with-continuous-neu-2609-03940/">Masked Autoregressive Speech Enhancement with Continuous Neural Audio Codec Representations</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.5</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出MARSE，利用连续神经音频编解码器表示进行掩码自回归语音增强，通过不同解码策略实现性能与计算开销的灵活权衡。</div>
<div class="card-action">
<a href="masked-autoregressive-speech-enhancement-with-continuous-neu-2609-03940/">详情 →</a> · <a href="https://arxiv.org/abs/2609.03940" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="tooldf-tool-integrated-reasoning-for-mixed-authenticity-audi-2609-03620/">ToolDF: Tool-Integrated Reasoning for Mixed-Authenticity Audio Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#音频深度伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">ToolDF利用音频大语言模型作为编排器，通过工具集成推理实现混合真实性音频深度伪造检测，并引入新基准。</div>
<div class="card-action">
<a href="tooldf-tool-integrated-reasoning-for-mixed-authenticity-audi-2609-03620/">详情 →</a> · <a href="https://arxiv.org/abs/2609.03620" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="dual-form-asr-semantics-aware-inverse-text-normalization-for-2609-02901/">Dual-Form ASR: Semantics-Aware Inverse Text Normalization for Chinese Speech Recognition</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出双形式ASR框架，通过成对口语/书面语监督和ITN-MWER损失，实现语义感知的逆文本正则化，提升中文ASR书面语输出的可读性。</div>
<div class="card-action">
<a href="dual-form-asr-semantics-aware-inverse-text-normalization-for-2609-02901/">详情 →</a> · <a href="https://arxiv.org/abs/2609.02901" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="compressing-streaming-neural-audio-encoders-via-latent-space-2609-04102/">Compressing Streaming Neural Audio Encoders via Latent-Space Distillation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音识别</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">通过蒸馏预量化器潜在表示，将流式语音编码器压缩2.8倍，在保持WER接近的同时减少内存占用。</div>
<div class="card-action">
<a href="compressing-streaming-neural-audio-encoders-via-latent-space-2609-04102/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04102" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="geometric-ceilings-on-time-frequency-masking-for-single-chan-2609-03481/">Geometric Ceilings on Time-Frequency Masking for Single-Channel Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">7.5</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">本文从几何角度分析单通道分离中时频掩蔽的极限，提出嵌套类与正交投影框架，并在MUSDB18上验证了理论界限。</div>
<div class="card-action">
<a href="geometric-ceilings-on-time-frequency-masking-for-single-chan-2609-03481/">详情 →</a> · <a href="https://arxiv.org/abs/2609.03481" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="one-timeline-many-renderings-a-wolfram-language-paclet-for-h-2608-24683/">One Timeline, Many Renderings: A Wolfram Language Paclet for heterogeneous musical output</a>
<div class="card-meta">
<span class="card-score">6.5</span>
<span class="tag-pill">#音乐生成</span>
<span class="card-tier">前50%</span>
</div>
<div class="card-tldr">提出一个Wolfram语言paclet，通过共享时间线存储和渲染契约，同步生成Csound、MusicXML、OSC和节拍器输出。</div>
<div class="card-action">
<a href="one-timeline-many-renderings-a-wolfram-language-paclet-for-h-2608-24683/">详情 →</a> · <a href="https://arxiv.org/abs/2608.24683" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="local-chord-corruption-is-not-recognizer-replay-chord-condit-2609-03584/">Local Chord Corruption Is Not Recognizer Replay: Chord-Condition Propagation in MIDI-SAG</a>
<div class="card-meta">
<span class="card-score">6.2</span>
<span class="tag-pill">#音频生成</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">本文比较局部和弦损坏与完整自动和弦识别回放在MIDI-SAG生成器中的条件传播差异，发现局部损坏测试机制而完整回放评估部署传播。</div>
<div class="card-action">
<a href="local-chord-corruption-is-not-recognizer-replay-chord-condit-2609-03584/">详情 →</a> · <a href="https://arxiv.org/abs/2609.03584" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="from-local-kernels-to-global-form-modeling-the-emergence-of--2608-24660/">From local kernels to global form: modeling the emergence of musical content</a>
<div class="card-meta">
<span class="card-score">5.5</span>
<span class="tag-pill">#音乐分析</span>
<span class="card-tier">后50%</span>
</div>
<div class="card-tldr">本文提出一种基于滑动窗口的局部转移核估计方法，用于分析德彪西《Syrinx》的音乐结构，但结论保守，证据有限。</div>
<div class="card-action">
<a href="from-local-kernels-to-global-form-modeling-the-emergence-of--2608-24660/">详情 →</a> · <a href="https://arxiv.org/abs/2608.24660" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
