---
title: "语音/音频论文速递 2026-09-07"
date: 2026-09-07T09:00:00+08:00
draft: false
categories: ["每日速递"]
tags: []
summary: "今日 10 篇 · 重点领域 5 篇 · 最高分 9.2（#空间音频编辑）"
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
| #空间音频编辑 | 1篇 | `█████` |
| #语音分离 | 1篇 | `█████` |
| #乐器分离 | 1篇 | `█████` |
| #音频理解 | 1篇 | `█████` |
| #语音处理 | 1篇 | `█████` |
| #语音伪造检测 | 1篇 | `█████` |
| #音视频生成评估 | 1篇 | `█████` |

## 🎯 本站重点领域

> 语音增强 · 目标说话人提取 · 语音分离 · 双耳音频 · 乐器分离

### #语音增强

<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="swanweave-one-stage-multi-task-instruction-guided-3d-spatial-2609-04975/">SwanWeave:One-Stage Multi-Task Instruction-Guided 3D Spatial Audio Editing</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#空间音频编辑</span>
</div>
<div class="card-tldr">首个基于指令的一阶段多任务3D空间音频编辑框架，通过SE-MoE和SPO实现高质量FOA编辑。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="grounded-decoding-for-autoregressive-speech-enhancement-via--2609-04245/">Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement</a>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出证据接地生成式语音增强框架，结合确定性估计与LLM自回归生成，通过SNR条件接地和局部细化提升低信噪比感知质量。</div>
</div></div>
<div class="paper-card paper-card-focus">
<div class="card-rank">⭐</div>
<div class="card-body">
<a class="card-title" href="discriminative-flow-matching-beyond-time-conditioning-in-gen-2609-04525/">Discriminative Flow Matching: Beyond Time-Conditioning in Generative Restoration via Flow-State Representations</a>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
</div>
<div class="card-tldr">提出判别流匹配，用判别模型表示替代时间条件，在语音增强和图像去噪上超越CFM和扩散基线。</div>
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
<a class="card-title" href="what-selects-what-reconstructs-repairing-exemplar-based-comp-2609-04756/">What Selects, What Reconstructs: Repairing Exemplar-Based Complex-Spectrum Separation</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
</div>
<div class="card-tldr">本文理论分析范例分离方法中选择与重建角色的混淆，指出当变形类可插值时选择失效，并提出修复方案，在MUSDB18上显著降低准则与oracle差距。</div>
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
<a class="card-title" href="beyond-sdr-how-music-source-separation-reshapes-rhythm-relev-2609-04224/">Beyond SDR: How Music Source Separation Reshapes Rhythm-Relevant Signal Properties</a>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
</div>
<div class="card-tldr">本文评估四种音乐源分离器对鼓点节奏关键信号属性的影响，发现SDR无法反映瞬态和动态失真，模型排名会反转。</div>
</div></div>

## 📊 完整排行榜

| 排名 | 论文 | 评分 | 主任务 |
| --- | --- | --- | --- |
| 🥇 | [SwanWeave:One-Stage Multi-Task Instruction-Guided 3D Spatial…](swanweave-one-stage-multi-task-instruction-guided-3d-spatial-2609-04975/) 🎯 | **9.2** | #空间音频编辑 |
| 🥈 | [Grounded Decoding for Autoregressive Speech Enhancement via …](grounded-decoding-for-autoregressive-speech-enhancement-via--2609-04245/) 🎯 | **9.2** | #语音增强 |
| 🥉 | [Discriminative Flow Matching: Beyond Time-Conditioning in Ge…](discriminative-flow-matching-beyond-time-conditioning-in-gen-2609-04525/) 🎯 | **8.8** | #语音增强 |
| 4. | [What Selects, What Reconstructs: Repairing Exemplar-Based Co…](what-selects-what-reconstructs-repairing-exemplar-based-comp-2609-04756/) 🎯 | **8.2** | #语音分离 |
| 5. | [Beyond SDR: How Music Source Separation Reshapes Rhythm-Rele…](beyond-sdr-how-music-source-separation-reshapes-rhythm-relev-2609-04224/) 🎯 | **8.2** | #乐器分离 |
| 6. | [Who Wins the Conflict? Mechanistic Interpretability of Text …](who-wins-the-conflict-mechanistic-interpretability-of-text-b-2606-18924/) | **7.8** | #音频理解 |
| 7. | [AudioKV: KV Cache Eviction in Efficient Large Audio Language…](audiokv-kv-cache-eviction-in-efficient-large-audio-language--2604-06694/) | **7.8** | #语音处理 |
| 8. | [SNAP: Speaker Nulling for Artifact Projection in Speech Deep…](snap-speaker-nulling-for-artifact-projection-in-speech-deepf-2603-20686/) | **7.8** | #语音伪造检测 |
| 9. | [PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-…](prism-bench-an-audio-centric-diagnostic-benchmark-for-text-t-2609-04867/) | **7.8** | #音视频生成评估 |
| 10. | [Sound-based Multi-Person 3D Pose Estimation](sound-based-multi-person-3d-pose-estimation-2609-04902/) | **7.2** | #人体姿态估计 |

## 📋 论文卡片速览

<div class="paper-card">
<div class="card-rank">🥇</div>
<div class="card-body">
<a class="card-title" href="swanweave-one-stage-multi-task-instruction-guided-3d-spatial-2609-04975/">SwanWeave:One-Stage Multi-Task Instruction-Guided 3D Spatial Audio Editing</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#空间音频编辑</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首个基于指令的一阶段多任务3D空间音频编辑框架，通过SE-MoE和SPO实现高质量FOA编辑。</div>
<div class="card-action">
<a href="swanweave-one-stage-multi-task-instruction-guided-3d-spatial-2609-04975/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04975" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥈</div>
<div class="card-body">
<a class="card-title" href="grounded-decoding-for-autoregressive-speech-enhancement-via--2609-04245/">Grounded Decoding for Autoregressive Speech Enhancement via Adaptive Code-Space Grounding and Local LLM Refinement</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">9.2</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出证据接地生成式语音增强框架，结合确定性估计与LLM自回归生成，通过SNR条件接地和局部细化提升低信噪比感知质量。</div>
<div class="card-action">
<a href="grounded-decoding-for-autoregressive-speech-enhancement-via--2609-04245/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04245" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">🥉</div>
<div class="card-body">
<a class="card-title" href="discriminative-flow-matching-beyond-time-conditioning-in-gen-2609-04525/">Discriminative Flow Matching: Beyond Time-Conditioning in Generative Restoration via Flow-State Representations</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.8</span>
<span class="tag-pill">#语音增强</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出判别流匹配，用判别模型表示替代时间条件，在语音增强和图像去噪上超越CFM和扩散基线。</div>
<div class="card-action">
<a href="discriminative-flow-matching-beyond-time-conditioning-in-gen-2609-04525/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04525" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">4.</div>
<div class="card-body">
<a class="card-title" href="what-selects-what-reconstructs-repairing-exemplar-based-comp-2609-04756/">What Selects, What Reconstructs: Repairing Exemplar-Based Complex-Spectrum Separation</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#语音分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文理论分析范例分离方法中选择与重建角色的混淆，指出当变形类可插值时选择失效，并提出修复方案，在MUSDB18上显著降低准则与oracle差距。</div>
<div class="card-action">
<a href="what-selects-what-reconstructs-repairing-exemplar-based-comp-2609-04756/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04756" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">5.</div>
<div class="card-body">
<a class="card-title" href="beyond-sdr-how-music-source-separation-reshapes-rhythm-relev-2609-04224/">Beyond SDR: How Music Source Separation Reshapes Rhythm-Relevant Signal Properties</a> <span class="focus-mark">🎯</span>
<div class="card-meta">
<span class="card-score">8.2</span>
<span class="tag-pill">#乐器分离</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">本文评估四种音乐源分离器对鼓点节奏关键信号属性的影响，发现SDR无法反映瞬态和动态失真，模型排名会反转。</div>
<div class="card-action">
<a href="beyond-sdr-how-music-source-separation-reshapes-rhythm-relev-2609-04224/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04224" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">6.</div>
<div class="card-body">
<a class="card-title" href="who-wins-the-conflict-mechanistic-interpretability-of-text-b-2606-18924/">Who Wins the Conflict? Mechanistic Interpretability of Text Bias in Audio LLMs</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音频理解</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首次从机制层面分析音频大语言模型中的文本主导偏差，发现文本路径抑制而非擦除音频信息，并提出无需训练的反向修补干预以缓解该偏差。</div>
<div class="card-action">
<a href="who-wins-the-conflict-mechanistic-interpretability-of-text-b-2606-18924/">详情 →</a> · <a href="https://arxiv.org/abs/2606.18924" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">7.</div>
<div class="card-body">
<a class="card-title" href="audiokv-kv-cache-eviction-in-efficient-large-audio-language--2604-06694/">AudioKV: KV Cache Eviction in Efficient Large Audio Language Models</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音处理</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">AudioKV提出语义-声学对齐机制识别音频关键注意力头并动态分配KV缓存预算，结合FFT频谱平滑实现高效长上下文推理。</div>
<div class="card-action">
<a href="audiokv-kv-cache-eviction-in-efficient-large-audio-language--2604-06694/">详情 →</a> · <a href="https://arxiv.org/abs/2604.06694" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">8.</div>
<div class="card-body">
<a class="card-title" href="snap-speaker-nulling-for-artifact-projection-in-speech-deepf-2603-20686/">SNAP: Speaker Nulling for Artifact Projection in Speech Deepfake Detection</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#语音伪造检测</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">SNAP通过正交投影抑制说话人信息，缓解语音伪造检测中的说话人纠缠问题，提升跨说话人泛化性能。</div>
<div class="card-action">
<a href="snap-speaker-nulling-for-artifact-projection-in-speech-deepf-2603-20686/">详情 →</a> · <a href="https://arxiv.org/abs/2603.20686" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">9.</div>
<div class="card-body">
<a class="card-title" href="prism-bench-an-audio-centric-diagnostic-benchmark-for-text-t-2609-04867/">PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation</a>
<div class="card-meta">
<span class="card-score">7.8</span>
<span class="tag-pill">#音视频生成评估</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">提出首个以音频为中心的文本到音视频生成诊断基准PRISM-Bench，通过双轴分类和35项细粒度标准，系统评估生成系统的音频能力。</div>
<div class="card-action">
<a href="prism-bench-an-audio-centric-diagnostic-benchmark-for-text-t-2609-04867/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04867" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
<div class="paper-card">
<div class="card-rank">10.</div>
<div class="card-body">
<a class="card-title" href="sound-based-multi-person-3d-pose-estimation-2609-04902/">Sound-based Multi-Person 3D Pose Estimation</a>
<div class="card-meta">
<span class="card-score">7.2</span>
<span class="tag-pill">#人体姿态估计</span>
<span class="card-tier">前25%</span>
</div>
<div class="card-tldr">首次尝试仅用声音估计多人3D姿态，提出SoundMHPE编码器-解码器框架，并构建AMP数据集验证其有效性。</div>
<div class="card-action">
<a href="sound-based-multi-person-3d-pose-estimation-2609-04902/">详情 →</a> · <a href="https://arxiv.org/abs/2609.04902" target="_blank" rel="noopener">arXiv</a>
</div>
</div>
</div>
